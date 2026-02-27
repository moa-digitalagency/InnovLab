from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from security.decorators import admin_required
from models import db
from models.security_logs import SecurityLog, BannedIP
from datetime import datetime

security_bp = Blueprint('security', __name__, url_prefix='/admin/security', static_folder='../../statics')

@security_bp.route('/')
@login_required
@admin_required
def index():
    # Fetch Security Logs
    logs = SecurityLog.query.order_by(SecurityLog.timestamp.desc()).limit(100).all()

    # Fetch Banned IPs
    banned_ips = BannedIP.query.order_by(BannedIP.banned_at.desc()).all()

    return render_template('admin/security.html', logs=logs, banned_ips=banned_ips)

@security_bp.route('/ban', methods=['POST'])
@login_required
@admin_required
def ban_ip():
    ip_address = request.form.get('ip_address')
    reason = request.form.get('reason')

    if not ip_address:
        flash('Adresse IP requise.', 'error')
        return redirect(url_for('security.index'))

    # Check if already banned
    existing_ban = BannedIP.query.filter_by(ip_address=ip_address).first()
    if existing_ban:
        flash('Cette adresse IP est déjà bannie.', 'warning')
        return redirect(url_for('security.index'))

    try:
        new_ban = BannedIP(ip_address=ip_address, reason=reason)
        db.session.add(new_ban)

        # Log the action
        log = SecurityLog(
            ip_address=request.remote_addr,
            event_type='manual_ban',
            description=f'Banned IP {ip_address} manually. Reason: {reason}',
            user_agent=request.user_agent.string
        )
        db.session.add(log)

        db.session.commit()
        flash(f'IP {ip_address} bannie avec succès.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erreur lors du bannissement: {e}', 'error')

    return redirect(url_for('security.index'))

@security_bp.route('/unban/<int:id>', methods=['POST'])
@login_required
@admin_required
def unban_ip(id):
    ban_record = BannedIP.query.get_or_404(id)
    ip_address = ban_record.ip_address

    try:
        db.session.delete(ban_record)

        # Log the action
        log = SecurityLog(
            ip_address=request.remote_addr,
            event_type='manual_unban',
            description=f'Unbanned IP {ip_address} manually.',
            user_agent=request.user_agent.string
        )
        db.session.add(log)

        db.session.commit()
        flash(f'IP {ip_address} débannie avec succès.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erreur lors du débannissement: {e}', 'error')

    return redirect(url_for('security.index'))
