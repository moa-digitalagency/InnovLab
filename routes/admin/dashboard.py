from flask import Blueprint, render_template, request, redirect, url_for, flash
from security.decorators import admin_required
from models import db
from models.forms import FounderRequest, StartupRequest, InvestorRequest
from models.message import Message
from datetime import datetime, date, timedelta

admin_bp = Blueprint('admin', __name__, url_prefix='/admin', static_folder='../../statics', static_url_path='/static')

@admin_bp.route('/dashboard')
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
@admin_required
def founders():
    founders = FounderRequest.query.order_by(FounderRequest.created_at.desc()).all()
    return render_template('admin/founders.html', founders=founders)

@admin_bp.route('/startups')
@admin_required
def startups():
    startups = StartupRequest.query.order_by(StartupRequest.created_at.desc()).all()
    return render_template('admin/startups.html', startups=startups)

@admin_bp.route('/investors')
@admin_required
def investors():
    investors = InvestorRequest.query.order_by(InvestorRequest.created_at.desc()).all()
    return render_template('admin/investors.html', investors=investors)

@admin_bp.route('/founders/delete/<int:id>', methods=['POST'])
@admin_required
def delete_founder(id):
    founder = FounderRequest.query.get_or_404(id)
    db.session.delete(founder)
    db.session.commit()
    flash('Founder request deleted.', 'success')
    return redirect(url_for('admin.founders'))

@admin_bp.route('/startups/delete/<int:id>', methods=['POST'])
@admin_required
def delete_startup(id):
    startup = StartupRequest.query.get_or_404(id)
    db.session.delete(startup)
    db.session.commit()
    flash('Startup request deleted.', 'success')
    return redirect(url_for('admin.startups'))

@admin_bp.route('/investors/delete/<int:id>', methods=['POST'])
@admin_required
def delete_investor(id):
    investor = InvestorRequest.query.get_or_404(id)
    db.session.delete(investor)
    db.session.commit()
    flash('Investor request deleted.', 'success')
    return redirect(url_for('admin.investors'))

@admin_bp.route('/view/<request_type>/<int:request_id>')
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
