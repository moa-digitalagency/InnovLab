from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required
from security.decorators import admin_required
from models import db
from models.forms import FounderRequest, StartupRequest, InvestorRequest
from models.message import Message
from models.analytics import VisitAnalytics
from models.security_logs import SecurityLog, BannedIP
from sqlalchemy import func
from datetime import datetime, date, timedelta

admin_bp = Blueprint('admin', __name__, url_prefix='/admin', static_folder='../../statics', static_url_path='/static')

@admin_bp.route('/')
def index():
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    founders_count = FounderRequest.query.count()
    startups_count = StartupRequest.query.count()
    investors_count = InvestorRequest.query.count()

    # Unread messages
    unread_messages_count = Message.query.filter_by(read=False).count()

    # Chart Data (Last 7 days)
    chart_labels = []
    chart_data = []

    today = date.today()
    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        day_str = day.strftime('%Y-%m-%d')
        chart_labels.append(day_str)

        # Calculate start and end of the day for filtering
        day_start = datetime.combine(day, datetime.min.time())
        day_end = datetime.combine(day, datetime.max.time())

        # Query counts for each model
        f_count = FounderRequest.query.filter(FounderRequest.created_at >= day_start, FounderRequest.created_at <= day_end).count()
        s_count = StartupRequest.query.filter(StartupRequest.created_at >= day_start, StartupRequest.created_at <= day_end).count()
        i_count = InvestorRequest.query.filter(InvestorRequest.created_at >= day_start, InvestorRequest.created_at <= day_end).count()

        chart_data.append(f_count + s_count + i_count)

    return render_template('admin/dashboard.html',
                           founders_count=founders_count,
                           startups_count=startups_count,
                           investors_count=investors_count,
                           unread_messages_count=unread_messages_count,
                           chart_labels=chart_labels,
                           chart_data=chart_data)

@admin_bp.route('/founders')
@login_required
@admin_required
def founders():
    founders = FounderRequest.query.order_by(FounderRequest.created_at.desc()).all()
    return render_template('admin/founders.html', founders=founders)

@admin_bp.route('/startups')
@login_required
@admin_required
def startups():
    startups = StartupRequest.query.order_by(StartupRequest.created_at.desc()).all()
    return render_template('admin/startups.html', startups=startups)

@admin_bp.route('/investors')
@login_required
@admin_required
def investors():
    investors = InvestorRequest.query.order_by(InvestorRequest.created_at.desc()).all()
    return render_template('admin/investors.html', investors=investors)

@admin_bp.route('/founders/delete/<int:id>', methods=['POST'])
@login_required
@admin_required
def delete_founder(id):
    founder = FounderRequest.query.get_or_404(id)
    db.session.delete(founder)
    db.session.commit()
    flash('Founder request deleted.', 'success')
    return redirect(url_for('admin.founders'))

@admin_bp.route('/startups/delete/<int:id>', methods=['POST'])
@login_required
@admin_required
def delete_startup(id):
    startup = StartupRequest.query.get_or_404(id)
    db.session.delete(startup)
    db.session.commit()
    flash('Startup request deleted.', 'success')
    return redirect(url_for('admin.startups'))

@admin_bp.route('/investors/delete/<int:id>', methods=['POST'])
@login_required
@admin_required
def delete_investor(id):
    investor = InvestorRequest.query.get_or_404(id)
    db.session.delete(investor)
    db.session.commit()
    flash('Investor request deleted.', 'success')
    return redirect(url_for('admin.investors'))

@admin_bp.route('/view/<request_type>/<int:request_id>')
@login_required
@admin_required
def view_request(request_type, request_id):
    if request_type == 'founder':
        request_obj = FounderRequest.query.get_or_404(request_id)
    elif request_type == 'startup':
        request_obj = StartupRequest.query.get_or_404(request_id)
    elif request_type == 'investor':
        request_obj = InvestorRequest.query.get_or_404(request_id)
    else:
        flash('Type de demande invalide', 'error')
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/request_detail.html', request_obj=request_obj, request_type=request_type)

@admin_bp.route('/toggle_status/<request_type>/<int:request_id>', methods=['POST'])
@login_required
@admin_required
def toggle_status(request_type, request_id):
    if request_type == 'founder':
        request_obj = FounderRequest.query.get_or_404(request_id)
    elif request_type == 'startup':
        request_obj = StartupRequest.query.get_or_404(request_id)
    elif request_type == 'investor':
        request_obj = InvestorRequest.query.get_or_404(request_id)
    else:
        flash('Type de demande invalide', 'error')
        return redirect(url_for('admin.dashboard'))

    if request_obj.status == 'processed':
        request_obj.status = 'new'
        flash('Demande marquée comme non lue.', 'info')
    else:
        request_obj.status = 'processed'
        flash('Demande marquée comme traitée.', 'success')

    db.session.commit()
    return redirect(url_for('admin.view_request', request_type=request_type, request_id=request_id))

# Analytics Routes

@admin_bp.route('/analytics')
@login_required
@admin_required
def analytics():
    # Get Period Filter (Default: 30 days)
    period = request.args.get('period', '30')
    try:
        days = int(period)
    except ValueError:
        days = 30

    start_date = datetime.utcnow() - timedelta(days=days)

    # 1. Visits Over Time (Line Chart)
    # Group by Date
    visits_data = db.session.query(
        func.date(VisitAnalytics.timestamp).label('date'),
        func.count(VisitAnalytics.id).label('count')
    ).filter(
        VisitAnalytics.timestamp >= start_date
    ).group_by(
        func.date(VisitAnalytics.timestamp)
    ).order_by(
        func.date(VisitAnalytics.timestamp)
    ).all()

    # Format for Chart.js
    chart_labels = []
    chart_values = []

    # Fill in missing dates with 0
    current_date = start_date.date()
    end_date = datetime.utcnow().date()

    # Create a dict for easy lookup
    visits_dict = {str(d.date): d.count for d in visits_data}

    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        chart_labels.append(date_str)
        chart_values.append(visits_dict.get(date_str, 0))
        current_date += timedelta(days=1)

    # 2. Device Distribution (Pie Chart)
    device_data = db.session.query(
        VisitAnalytics.device_type,
        func.count(VisitAnalytics.id)
    ).filter(
        VisitAnalytics.timestamp >= start_date
    ).group_by(
        VisitAnalytics.device_type
    ).all()

    device_labels = [d[0] for d in device_data]
    device_values = [d[1] for d in device_data]

    # 3. Top Pages (Table)
    top_pages = db.session.query(
        VisitAnalytics.path,
        func.count(VisitAnalytics.id).label('count')
    ).filter(
        VisitAnalytics.timestamp >= start_date
    ).group_by(
        VisitAnalytics.path
    ).order_by(
        func.count(VisitAnalytics.id).desc()
    ).limit(10).all()

    # 4. Top Referrers (Table)
    top_referrers = db.session.query(
        VisitAnalytics.referrer,
        func.count(VisitAnalytics.id).label('count')
    ).filter(
        VisitAnalytics.timestamp >= start_date,
        VisitAnalytics.referrer != None,
        VisitAnalytics.referrer != ''
    ).group_by(
        VisitAnalytics.referrer
    ).order_by(
        func.count(VisitAnalytics.id).desc()
    ).limit(10).all()

    return render_template(
        'admin/analytics.html',
        period=days,
        chart_labels=chart_labels,
        chart_values=chart_values,
        device_labels=device_labels,
        device_values=device_values,
        top_pages=top_pages,
        top_referrers=top_referrers
    )

# Security Routes

@admin_bp.route('/security')
@login_required
@admin_required
def security():
    # Fetch Security Logs
    logs = SecurityLog.query.order_by(SecurityLog.timestamp.desc()).limit(100).all()

    # Fetch Banned IPs
    banned_ips = BannedIP.query.order_by(BannedIP.banned_at.desc()).all()

    return render_template('admin/security.html', logs=logs, banned_ips=banned_ips)

@admin_bp.route('/security/ban', methods=['POST'])
@login_required
@admin_required
def ban_ip():
    ip_address = request.form.get('ip_address')
    reason = request.form.get('reason')

    if not ip_address:
        flash('Adresse IP requise.', 'error')
        return redirect(url_for('admin.security'))

    # Check if already banned
    existing_ban = BannedIP.query.filter_by(ip_address=ip_address).first()
    if existing_ban:
        flash('Cette adresse IP est déjà bannie.', 'warning')
        return redirect(url_for('admin.security'))

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

    return redirect(url_for('admin.security'))

@admin_bp.route('/security/unban/<int:id>', methods=['POST'])
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

    return redirect(url_for('admin.security'))
