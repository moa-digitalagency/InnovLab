from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from models import db, User
from models.forms import FounderRequest, StartupRequest, InvestorRequest
from models.message import Message
from models.settings import SiteSettings, SeoSettings
from datetime import datetime, date, timedelta
import os

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

@admin_bp.route('/seo', methods=['GET', 'POST'])
@login_required
def seo():
    pages = ['index', 'founder', 'startup', 'investor']

    # Ensure defaults exist
    entries = SeoSettings.query.all()
    existing_pages = [e.page_name for e in entries]

    needs_commit = False
    for page in pages:
        if page not in existing_pages:
            new_seo = SeoSettings(
                page_name=page,
                title_tag=f'Shabaka - {page.capitalize()}',
                meta_desc='Shabaka InnovLab - Le Catalyseur de la Souveraineté Technologique'
            )
            db.session.add(new_seo)
            needs_commit = True

    if needs_commit:
        db.session.commit()

    if request.method == 'POST':
        # Handle Global SEO Settings (stored in 'index' page entry or specific global entry)
        global_seo = SeoSettings.query.filter_by(page_name='index').first()
        if global_seo:
            ga_id = request.form.get('google_analytics_id')
            robots = request.form.get('robots_txt_content')
            def_title = request.form.get('meta_title_default')
            def_desc = request.form.get('meta_description_default')
            def_keywords = request.form.get('meta_keywords_default')

            if ga_id is not None: global_seo.google_analytics_id = ga_id
            if robots is not None: global_seo.robots_txt_content = robots
            if def_title is not None: global_seo.meta_title_default = def_title
            if def_desc is not None: global_seo.meta_description_default = def_desc
            if def_keywords is not None: global_seo.meta_keywords_default = def_keywords

        # Handle Per-Page SEO Settings
        for page in pages:
            seo_entry = SeoSettings.query.filter_by(page_name=page).first()
            if seo_entry:
                title = request.form.get(f'title_{page}')
                desc = request.form.get(f'desc_{page}')
                if title: seo_entry.title_tag = title
                if desc: seo_entry.meta_desc = desc

        db.session.commit()
        flash('Paramètres SEO mis à jour.', 'success')
        return redirect(url_for('admin.seo'))

    seo_entries = SeoSettings.query.all()
    # Map entries for easier access in template
    seo_map = {e.page_name: e for e in seo_entries}

    return render_template('admin/seo.html', seo_map=seo_map, pages=pages)

@admin_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    settings_obj = SiteSettings.query.first()
    if not settings_obj:
        settings_obj = SiteSettings(
            site_title='Shabaka InnovLab',
            contact_email='nticshabaka@gmail.com',
            phone='+212 699 14 00 01',
            address="Centre d'affaires Gueliz, Bd My Rachid, Étage 1, Bureau 8, 40000 Marrakech"
        )
        db.session.add(settings_obj)
        db.session.commit()

    if request.method == 'POST':
        # Contact
        email = request.form.get('contact_email')
        phone = request.form.get('phone')
        address = request.form.get('address')

        if email: settings_obj.contact_email = email
        if phone: settings_obj.phone = phone
        if address: settings_obj.address = address

        # Telegram
        tg_token = request.form.get('telegram_bot_token')
        tg_chat = request.form.get('telegram_chat_id')
        if tg_token is not None: settings_obj.telegram_bot_token = tg_token
        if tg_chat is not None: settings_obj.telegram_chat_id = tg_chat

        # Social Media
        linkedin = request.form.get('linkedin_url')
        twitter = request.form.get('twitter_url')
        facebook = request.form.get('facebook_url')
        if linkedin is not None: settings_obj.linkedin_url = linkedin
        if twitter is not None: settings_obj.twitter_url = twitter
        if facebook is not None: settings_obj.facebook_url = facebook

        # File Uploads (Logos)
        # Ensure we use the configured static folder
        static_folder = current_app.static_folder if current_app.static_folder else 'static'
        upload_folder = os.path.join(current_app.root_path, static_folder, 'uploads', 'logos')

        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        def save_logo(file_key, db_field):
            file = request.files.get(file_key)
            if file and file.filename:
                filename = secure_filename(file.filename)
                final_name = filename

                file.save(os.path.join(upload_folder, final_name))
                # Store path relative to static folder for url_for
                setattr(settings_obj, db_field, f"uploads/logos/{final_name}")

        save_logo('header_logo', 'header_logo')
        save_logo('footer_logo', 'footer_logo')

        db.session.commit()
        flash('Paramètres du site mis à jour.', 'success')
        return redirect(url_for('admin.settings'))

    return render_template('admin/settings.html', settings=settings_obj)

@admin_bp.route('/view/<request_type>/<int:request_id>')
@login_required
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
