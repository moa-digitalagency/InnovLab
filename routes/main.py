from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
from models.settings import SeoSettings
from services.submission_service import SubmissionService
from services.portfolio_service import PortfolioService

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
    projects = PortfolioService.get_all_projects(active_only=True)
    return render_template('portfolio.html', projects=projects)

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return redirect(url_for('main.index', _anchor='contact'))

    email = request.form.get('email')
    if email:
        SubmissionService.process_quick_contact(email)
        flash('Merci pour votre inscription!', 'success')
    return redirect(url_for('main.index'))

@main_bp.route('/contact-us', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        SubmissionService.process_contact_message(request.form)
        flash('Votre message a été envoyé avec succès!', 'success')
        return redirect(url_for('main.contact_us'))
    return render_template('contact_page.html')

@main_bp.route('/candidature/founder', methods=['GET', 'POST'])
def founder():
    if request.method == 'POST':
        file_pitch = request.files.get('file_pitch')
        SubmissionService.process_founder_application(request.form, file_pitch)
        flash('Votre candidature a été envoyée avec succès!', 'success')
        return redirect(url_for('main.index'))
    return render_template('candidature/founder.html')

@main_bp.route('/candidature/startup', methods=['GET', 'POST'])
def startup():
    if request.method == 'POST':
        file_pitch = request.files.get('file_pitch')
        SubmissionService.process_startup_application(request.form, file_pitch)
        flash('Votre candidature a été envoyée avec succès!', 'success')
        return redirect(url_for('main.index'))
    return render_template('candidature/startup.html')

@main_bp.route('/candidature/investor', methods=['GET', 'POST'])
def investor():
    if request.method == 'POST':
        file_intent = request.files.get('file_intent')
        SubmissionService.process_investor_application(request.form, file_intent)
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
