from flask import Blueprint, render_template, request, redirect, url_for, Response
from models.settings import SeoSettings
from services.portfolio_service import PortfolioService

main_bp = Blueprint('main', __name__, static_folder='../../statics', static_url_path='/static')

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

@main_bp.route('/contact', methods=['GET'])
def contact():
    # Only handles GET for redirect to anchor
    return redirect(url_for('main.index', _anchor='contact'))

@main_bp.route('/contact-us', methods=['GET'])
def contact_us():
    return render_template('contact_page.html')

@main_bp.route('/candidature/founder', methods=['GET'])
def founder():
    return render_template('candidature/founder.html')

@main_bp.route('/candidature/startup', methods=['GET'])
def startup():
    return render_template('candidature/startup.html')

@main_bp.route('/candidature/investor', methods=['GET'])
def investor():
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
