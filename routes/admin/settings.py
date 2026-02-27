from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models.settings import SiteSettings, SeoSettings
from models import db
from services.file_service import save_file
from security.decorators import admin_required

settings_bp = Blueprint('settings', __name__, url_prefix='/admin')

@settings_bp.route('/seo', methods=['GET', 'POST'])
@login_required
@admin_required
def seo():
    pages = [
        'index', 'about', 'services', 'portfolio', 'contact_us',
        'founder', 'startup', 'investor', 'privacy_policy', 'terms_conditions'
    ]

    # Ensure defaults exist
    entries = SeoSettings.query.all()
    existing_pages = [e.page_name for e in entries]

    needs_commit = False
    for page in pages:
        if page not in existing_pages:
            new_seo = SeoSettings(
                page_name=page,
                title_tag=f'Shabaka - {page.replace("_", " ").capitalize()}',
                meta_desc='Shabaka InnovLab - Le Catalyseur de la Souveraineté Technologique',
                keywords=''
            )
            db.session.add(new_seo)
            needs_commit = True

    if needs_commit:
        db.session.commit()

    if request.method == 'POST':
        # Handle Global SEO Settings
        global_seo = SeoSettings.query.filter_by(page_name='index').first()
        if global_seo:
            ga_id = request.form.get('google_analytics_id')
            robots = request.form.get('robots_txt_content')
            def_title = request.form.get('meta_title_default')
            def_desc = request.form.get('meta_description_default')
            def_keywords = request.form.get('meta_keywords_default')

            # Open Graph & Twitter Cards
            og_site_name = request.form.get('og_site_name')
            twitter_handle = request.form.get('twitter_handle')

            if ga_id is not None: global_seo.google_analytics_id = ga_id
            if robots is not None: global_seo.robots_txt_content = robots
            if def_title is not None: global_seo.meta_title_default = def_title
            if def_desc is not None: global_seo.meta_description_default = def_desc
            if def_keywords is not None: global_seo.meta_keywords_default = def_keywords
            if og_site_name is not None: global_seo.og_site_name = og_site_name
            if twitter_handle is not None: global_seo.twitter_handle = twitter_handle

            # Image OG Upload
            og_image = request.files.get('og_image_default')
            if og_image and og_image.filename:
                filename = save_file(og_image, subfolder='logos')
                if filename:
                    global_seo.og_image_default = f"uploads/logos/{filename}"

        # Handle Per-Page SEO Settings
        for page in pages:
            seo_entry = SeoSettings.query.filter_by(page_name=page).first()
            if seo_entry:
                title = request.form.get(f'title_{page}')
                desc = request.form.get(f'desc_{page}')
                keywords = request.form.get(f'keywords_{page}')

                if title is not None: seo_entry.title_tag = title
                if desc is not None: seo_entry.meta_desc = desc
                if keywords is not None: seo_entry.keywords = keywords

        db.session.commit()
        flash('Paramètres SEO mis à jour.', 'success')
        return redirect(url_for('settings.seo'))

    seo_entries = SeoSettings.query.all()
    seo_map = {e.page_name: e for e in seo_entries}

    return render_template('admin/seo.html', seo_map=seo_map, pages=pages)

@settings_bp.route('/settings', methods=['GET', 'POST'])
@login_required
@admin_required
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

        # Custom Head Code
        custom_head_code = request.form.get('custom_head_code')
        if custom_head_code is not None: settings_obj.custom_head_code = custom_head_code

        # Map Coordinates
        map_lat = request.form.get('map_latitude')
        map_lon = request.form.get('map_longitude')
        if map_lat is not None: settings_obj.map_latitude = map_lat
        if map_lon is not None: settings_obj.map_longitude = map_lon

        # File Uploads (Logos)
        def save_logo(file_key, db_field):
            file = request.files.get(file_key)
            if file and file.filename:
                # Use FileService
                filename = save_file(file, subfolder='logos')
                if filename:
                    # Store path relative to static folder for url_for
                    setattr(settings_obj, db_field, f"uploads/logos/{filename}")

        save_logo('header_logo', 'header_logo')
        save_logo('footer_logo', 'footer_logo')
        save_logo('favicon', 'favicon')

        db.session.commit()
        flash('Paramètres du site mis à jour.', 'success')
        return redirect(url_for('settings.settings'))

    return render_template('admin/settings.html', settings=settings_obj)


@settings_bp.route('/privacy-policy', methods=['GET', 'POST'])
@login_required
@admin_required
def privacy_policy():
    settings_obj = SiteSettings.query.first()
    if not settings_obj:
        # Should not happen if initialized, but safe fallback
        settings_obj = SiteSettings()
        db.session.add(settings_obj)
        db.session.commit()

    if request.method == 'POST':
        privacy = request.form.get('privacy_policy')
        if privacy is not None:
            settings_obj.privacy_policy = privacy
            db.session.commit()
            flash('Politique de confidentialité mise à jour.', 'success')
            return redirect(url_for('settings.privacy_policy'))

    return render_template('admin/privacy_policy.html', settings=settings_obj)


@settings_bp.route('/terms-conditions', methods=['GET', 'POST'])
@login_required
@admin_required
def terms_conditions():
    settings_obj = SiteSettings.query.first()
    if not settings_obj:
        settings_obj = SiteSettings()
        db.session.add(settings_obj)
        db.session.commit()

    if request.method == 'POST':
        terms = request.form.get('terms_conditions')
        if terms is not None:
            settings_obj.terms_conditions = terms
            db.session.commit()
            flash('Conditions générales mises à jour.', 'success')
            return redirect(url_for('settings.terms_conditions'))

    return render_template('admin/terms_conditions.html', settings=settings_obj)
