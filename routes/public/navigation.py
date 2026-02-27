from flask import Blueprint, render_template, request, redirect, url_for, Response
from models.settings import SeoSettings, SiteSettings
from models.testimonial import Testimonial
from services.portfolio_service import PortfolioService

main_bp = Blueprint('main', __name__, static_folder='../../statics', static_url_path='/static')

@main_bp.route('/', methods=['GET'])
def index():
    featured_test = Testimonial.query.filter_by(is_featured=True).first()
    standard_tests = Testimonial.query.filter_by(is_featured=False).order_by(Testimonial.created_at.desc()).limit(2).all()
    return render_template('index.html', featured_test=featured_test, standard_tests=standard_tests)

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

@main_bp.route('/sitemap.xml', methods=['GET'])
def sitemap_xml():
    pages = [
        ('main.index', 1.0),
        ('main.about', 0.8),
        ('main.services', 0.8),
        ('main.portfolio', 0.8),
        ('main.contact_us', 0.6),
        ('main.startup', 0.9),
        ('main.founder', 0.9),
        ('main.investor', 0.9),
        ('main.privacy_policy', 0.5),
        ('main.terms_conditions', 0.5)
    ]

    sitemap_content = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for endpoint, priority in pages:
        url = url_for(endpoint, _external=True)
        sitemap_content.append('  <url>')
        sitemap_content.append(f'    <loc>{url}</loc>')
        sitemap_content.append(f'    <priority>{priority}</priority>')
        sitemap_content.append('  </url>')

    sitemap_content.append('</urlset>')

    return Response('\n'.join(sitemap_content), mimetype='application/xml')

@main_bp.route('/robots.txt')
def robots_txt():
    seo_entry = SeoSettings.query.filter_by(page_name='index').first()
    content = ""
    if seo_entry and seo_entry.robots_txt_content:
        content = seo_entry.robots_txt_content
    else:
        content = f"User-agent: *\nDisallow: /admin/\nAllow: /\nSitemap: {request.url_root}sitemap.xml"

    return Response(content, mimetype='text/plain')

@main_bp.route('/privacy-policy', methods=['GET'])
def privacy_policy():
    settings = SiteSettings.query.first()
    content = settings.privacy_policy if settings and settings.privacy_policy else "Contenu non disponible."
    return render_template('legal.html', title="Politique de Confidentialité", content=content)

@main_bp.route('/terms-conditions', methods=['GET'])
def terms_conditions():
    settings = SiteSettings.query.first()
    content = settings.terms_conditions if settings and settings.terms_conditions else "Contenu non disponible."
    return render_template('legal.html', title="Conditions Générales", content=content)
