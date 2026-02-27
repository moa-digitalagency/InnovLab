from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from security.decorators import admin_required
from models import db
from models.analytics import VisitAnalytics
from sqlalchemy import func
from datetime import datetime, timedelta

analytics_bp = Blueprint('analytics', __name__, url_prefix='/admin/analytics', static_folder='../../statics')

@analytics_bp.route('/')
@login_required
@admin_required
def index():
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
