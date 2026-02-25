from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from models.contact import Contact
from models.forms import FounderRequest, StartupRequest, InvestorRequest
from models import db
from werkzeug.utils import secure_filename
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
    projects = [
        {"category": "PropTech", "title": "Shabaka Syndic", "description": "Gestion copro digitale."},
        {"category": "PropTech", "title": "Shabaka Alu+", "description": "Devis menuiserie 30s."},
        {"category": "PropTech", "title": "Shabaka IMMO", "description": "Rapports de visite IA."},
        {"category": "GovTech", "title": "SGI-GP (GoPass)", "description": "Recettes aéroportuaires, Zero Trust."},
        {"category": "GovTech", "title": "Intel ATM-RDC", "description": "Surveillance aérienne IA."},
        {"category": "GovTech", "title": "GEC", "description": "Gestion Électronique Courriels."},
        {"category": "HealthTech", "title": "Algorithme AAPCMLU", "description": "Diagnostic lithiases urinaires."},
        {"category": "HealthTech", "title": "Urgence Gabon", "description": "Logistique secours."},
        {"category": "Retail/Daily", "title": "Hannout AI", "description": "Reconnaissance produits."},
        {"category": "Retail/Daily", "title": "LexIA", "description": "Juridique IA."},
    ]
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
        flash('Votre demande a été envoyée avec succès!', 'success')
        return redirect(url_for('main.index'))
    return render_template('candidature/investor.html')
