from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app, Response
from models.contact import Contact
from models.message import Message
from models.forms import FounderRequest, StartupRequest, InvestorRequest
from models.settings import SeoSettings
from models.portfolio import PortfolioProject
from models import db
from werkzeug.utils import secure_filename
from utils.telegram_bot import send_telegram_notification
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main_bp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@main_bp.route('/services', methods=['GET'])
def services():
    return render_template('services.html')

@main_bp.route('/portfolio', methods=['GET'])
def portfolio():
    projects = PortfolioProject.query.filter_by(is_active=True).order_by(PortfolioProject.created_at.desc()).all()
    return render_template('portfolio.html', projects=projects)

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return redirect(url_for('main.index', _anchor='contact'))

    email = request.form.get('email')
    if email:
        new_contact = Contact(email=email)
        db.session.add(new_contact)
        db.session.commit()
        flash('Merci pour votre inscription!', 'success')
    return redirect(url_for('main.index'))

@main_bp.route('/contact-us', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        new_message = Message(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        db.session.add(new_message)
        db.session.commit()

        # Telegram Notification
        try:
            msg = f"📩 **Nouveau Message Contact !**\nNom: {name}\nSujet: {subject}\nEmail: {email}\nMessage: {message}"
            send_telegram_notification(msg)
        except Exception as e:
            current_app.logger.error(f"Telegram Notification Error: {e}")

        flash('Votre message a été envoyé avec succès!', 'success')
        return redirect(url_for('main.contact_us'))
    return render_template('contact_page.html')

@main_bp.route('/candidature/founder', methods=['GET', 'POST'])
def founder():
    if request.method == 'POST':
        nom = request.form.get('nom')
        email = request.form.get('email')
        projet_name = request.form.get('projet_name')
        description = request.form.get('description')
        project_stage = request.form.get('project_stage')
        primary_need = request.form.get('primary_need')

        filename = None
        file_pitch = request.files.get('file_pitch')
        if file_pitch and file_pitch.filename:
            filename = secure_filename(file_pitch.filename)
            upload_folder = current_app.config['UPLOAD_FOLDER']
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            file_pitch.save(os.path.join(upload_folder, filename))

        new_founder = FounderRequest(
            nom=nom,
            email=email,
            projet_name=projet_name,
            description=description,
            project_stage=project_stage,
            primary_need=primary_need,
            file_pitch=filename
        )
        db.session.add(new_founder)
        db.session.commit()

        # Telegram Notification
        try:
            msg = f"🚀 **Nouvelle Candidature Founder !**\nNom: {nom}\nProjet: {projet_name}\nEmail: {email}\nBesoin: {primary_need}"
            send_telegram_notification(msg)
        except Exception as e:
            current_app.logger.error(f"Telegram Notification Error: {e}")

        flash('Votre candidature a été envoyée avec succès!', 'success')
        return redirect(url_for('main.index'))
    return render_template('candidature/founder.html')

@main_bp.route('/candidature/startup', methods=['GET', 'POST'])
def startup():
    if request.method == 'POST':
        nom_startup = request.form.get('nom_startup')
        email = request.form.get('email')
        secteur = request.form.get('secteur')
        besoins = ', '.join(request.form.getlist('besoins'))
        website_url = request.form.get('website_url')
        annual_revenue = request.form.get('annual_revenue')
        team_size = request.form.get('team_size')
        stage = request.form.get('stage')

        filename = None
        file_pitch = request.files.get('file_pitch')
        if file_pitch and file_pitch.filename:
            filename = secure_filename(file_pitch.filename)
            upload_folder = current_app.config['UPLOAD_FOLDER']
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            file_pitch.save(os.path.join(upload_folder, filename))

        new_startup = StartupRequest(
            nom_startup=nom_startup,
            email=email,
            secteur=secteur,
            besoins=besoins,
            website_url=website_url,
            annual_revenue=annual_revenue,
            team_size=team_size,
            stage=stage,
            file_pitch=filename
        )
        db.session.add(new_startup)
        db.session.commit()

        # Telegram Notification
        try:
            msg = f"🚀 **Nouvelle Candidature Startup !**\nNom Startup: {nom_startup}\nSecteur: {secteur}\nEmail: {email}\nStage: {stage}"
            send_telegram_notification(msg)
        except Exception as e:
            current_app.logger.error(f"Telegram Notification Error: {e}")

        flash('Votre candidature a été envoyée avec succès!', 'success')
        return redirect(url_for('main.index'))
    return render_template('candidature/startup.html')

@main_bp.route('/candidature/investor', methods=['GET', 'POST'])
def investor():
    if request.method == 'POST':
        nom = request.form.get('nom')
        email = request.form.get('email')
        type_investisseur = request.form.get('type_investisseur')
        ticket_moyen = request.form.get('ticket_moyen')
        sectors_interest = ', '.join(request.form.getlist('sectors_interest'))
        linkedin_profile = request.form.get('linkedin_profile')

        filename = None
        file_intent = request.files.get('file_intent')
        if file_intent and file_intent.filename:
            filename = secure_filename(file_intent.filename)
            upload_folder = current_app.config['UPLOAD_FOLDER']
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            file_intent.save(os.path.join(upload_folder, filename))

        new_investor = InvestorRequest(
            nom=nom,
            email=email,
            type_investisseur=type_investisseur,
            ticket_moyen=ticket_moyen,
            sectors_interest=sectors_interest,
            linkedin_profile=linkedin_profile,
            file_intent=filename
        )
        db.session.add(new_investor)
        db.session.commit()

        # Telegram Notification
        try:
            msg = f"🚀 **Nouvelle Demande Investisseur !**\nNom: {nom}\nType: {type_investisseur}\nEmail: {email}\nTicket: {ticket_moyen}"
            send_telegram_notification(msg)
        except Exception as e:
            current_app.logger.error(f"Telegram Notification Error: {e}")

        flash('Votre demande a été envoyée avec succès!', 'success')
        return redirect(url_for('main.index'))
    return render_template('candidature/investor.html')

@main_bp.route('/robots.txt')
def robots_txt():
    seo_entry = SeoSettings.query.filter_by(page_name='index').first()
    content = ""
    if seo_entry and seo_entry.robots_txt_content:
        content = seo_entry.robots_txt_content
    else:
        content = "User-agent: *\nDisallow:"

    return Response(content, mimetype='text/plain')
