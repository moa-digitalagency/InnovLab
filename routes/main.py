from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from models.contact import Contact
from models.message import Message
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
        {
            "category": "PropTech",
            "title": "Shabaka Alu+ (PWA Devis)",
            "description": "Standardise le chiffrage en menuiserie aluminium. En générant des devis techniques précis en moins de 30 secondes, il élimine l'erreur humaine et décuple la productivité commerciale."
        },
        {
            "category": "PropTech",
            "title": "Shabaka Syndic",
            "description": "Plateforme collaborative qui professionnalise la gestion des copropriétés. En digitalisant les appels de fonds et les quittances, elle instaure une transparence totale."
        },
        {
            "category": "PropTech",
            "title": "Gestion Chantiers (Partenariat Bellari)",
            "description": "Outil de contrôle financier en temps réel. Grâce au pointage automatisé et à la traçabilité des achats par preuve visuelle, il éradique le gaspillage sur site."
        },
        {
            "category": "PropTech",
            "title": "Shabaka IMMO",
            "description": "Synchronise reconnaissance d'image et traitement vocal pour générer instantanément des rapports de visite enrichis, accélérant la prise de décision client."
        },
        {
            "category": "GovTech",
            "title": "SGI-GP (GoPass)",
            "description": "Architecture Zero Trust et principe 'Flight-Bound' pour la maximisation des recettes aéroportuaires. Permet une réconciliation infaillible entre manifestes de vol et flux financiers."
        },
        {
            "category": "GovTech",
            "title": "Intel ATM-RDC",
            "description": "Système de Situational Awareness dédié à la sanctuarisation de l'espace aérien. Utilise l'IA comportementale pour détecter les menaces non déclarées."
        },
        {
            "category": "GovTech",
            "title": "GEC",
            "description": "Gestion Électronique des Courriels assurant la pérennité de la mémoire administrative et fluidifiant les circuits de décision via une traçabilité immuable."
        },
        {
            "category": "GovTech",
            "title": "AfrikaID (MOA Digital)",
            "description": "Rempart de KYC avancé protégeant les écosystèmes numériques contre les usurpations d'identité grâce à l'analyse des hash MRZ et la vérification biométrique."
        },
        {
            "category": "GovTech",
            "title": "MyCharika",
            "description": "Plateforme de dématérialisation simplifiant la création d'entreprise et l'extraction automatisée de données fiscales."
        },
        {
            "category": "GovTech",
            "title": "Shabaka Safety",
            "description": "Solution intégrée (hardware/software) réduisant les accidents de travail. Son IA détecte automatiquement le non-port des Équipements de Protection Individuelle (EPI)."
        },
        {
            "category": "GovTech",
            "title": "Busconnect",
            "description": "Optimise la mobilité urbaine par une analyse granulaire des flux, permettant une gestion prédictive des transports publics."
        },
        {
            "category": "HealthTech",
            "title": "Algorithme AAPCMLU (Dr. KALONJI)",
            "description": "Moteur d'inférence propriétaire utilisant une analyse probabiliste pour classifier les lithiases urinaires, fournissant un diagnostic de précision."
        },
        {
            "category": "HealthTech",
            "title": "Urgence Gabon",
            "description": "Système d'optimisation logistique pour les interventions médicales critiques, visant la réduction du temps de réponse vital."
        },
        {
            "category": "Retail/Daily",
            "title": "Hannout AI",
            "description": "Modernise le commerce de proximité grâce à la reconnaissance visuelle automatique des produits en caisse, fluidifiant le parcours client."
        },
        {
            "category": "Retail/Daily",
            "title": "LexIA (Jurisprudence IA)",
            "description": "Sécurise les arguments juridiques par une analyse sémantique des précédents judiciaires, offrant une certitude légale et un gain de temps stratégique."
        },
        {
            "category": "Retail/Daily",
            "title": "AI Journalist Manager",
            "description": "Plateforme de veille stratégique multilingue intégrant le clonage vocal ultra-réaliste et la validation factuelle en temps réel."
        },
        {
            "category": "Retail/Daily",
            "title": "Disparus.org",
            "description": "Solution à impact social utilisant l'IA pour générer des visuels optimisés pour les réseaux sociaux et des affiches avec QR Codes dynamiques pour les avis de recherche."
        },
        {
            "category": "Retail/Daily",
            "title": "Talento & Quick Receipt",
            "description": "Matching intelligent de talents par analyse sémantique de CV et simplification transactionnelle via quittances thermiques et WhatsApp."
        }
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
