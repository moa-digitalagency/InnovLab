from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User
from models.forms import FounderRequest, StartupRequest, InvestorRequest
from datetime import datetime, date

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        flash('Invalid username or password', 'error')

    return render_template('admin/login.html')

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    founders_count = FounderRequest.query.count()
    startups_count = StartupRequest.query.count()
    investors_count = InvestorRequest.query.count()

    today = date.today()
    leads_today = (
        FounderRequest.query.filter(db.func.date(FounderRequest.created_at) == today).count() +
        StartupRequest.query.filter(db.func.date(StartupRequest.created_at) == today).count() +
        InvestorRequest.query.filter(db.func.date(InvestorRequest.created_at) == today).count()
    )

    return render_template('admin/dashboard.html',
                           founders_count=founders_count,
                           startups_count=startups_count,
                           investors_count=investors_count,
                           leads_today=leads_today)

@admin_bp.route('/founders')
@login_required
def founders():
    founders = FounderRequest.query.order_by(FounderRequest.created_at.desc()).all()
    return render_template('admin/founders.html', founders=founders)

@admin_bp.route('/startups')
@login_required
def startups():
    startups = StartupRequest.query.order_by(StartupRequest.created_at.desc()).all()
    return render_template('admin/startups.html', startups=startups)

@admin_bp.route('/investors')
@login_required
def investors():
    investors = InvestorRequest.query.order_by(InvestorRequest.created_at.desc()).all()
    return render_template('admin/investors.html', investors=investors)

@admin_bp.route('/founders/delete/<int:id>', methods=['POST'])
@login_required
def delete_founder(id):
    founder = FounderRequest.query.get_or_404(id)
    db.session.delete(founder)
    db.session.commit()
    flash('Founder request deleted.', 'success')
    return redirect(url_for('admin.founders'))

@admin_bp.route('/startups/delete/<int:id>', methods=['POST'])
@login_required
def delete_startup(id):
    startup = StartupRequest.query.get_or_404(id)
    db.session.delete(startup)
    db.session.commit()
    flash('Startup request deleted.', 'success')
    return redirect(url_for('admin.startups'))

@admin_bp.route('/investors/delete/<int:id>', methods=['POST'])
@login_required
def delete_investor(id):
    investor = InvestorRequest.query.get_or_404(id)
    db.session.delete(investor)
    db.session.commit()
    flash('Investor request deleted.', 'success')
    return redirect(url_for('admin.investors'))
