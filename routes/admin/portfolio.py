from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from services.portfolio_service import PortfolioService
from security.decorators import admin_required

portfolio_bp = Blueprint('portfolio', __name__, url_prefix='/admin')

@portfolio_bp.route('/portfolio')
@login_required
@admin_required
def portfolio():
    projects = PortfolioService.get_all_projects()
    return render_template('admin/portfolio.html', projects=projects)

@portfolio_bp.route('/portfolio/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_portfolio():
    if request.method == 'POST':
        PortfolioService.create_project(request.form, request.files.get('image'))
        flash('Projet ajouté avec succès.', 'success')
        return redirect(url_for('portfolio.portfolio'))

    return render_template('admin/portfolio_form.html', project=None)

@portfolio_bp.route('/portfolio/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_portfolio(id):
    if request.method == 'POST':
        PortfolioService.update_project(id, request.form, request.files.get('image'))
        flash('Projet mis à jour avec succès.', 'success')
        return redirect(url_for('portfolio.portfolio'))

    project = PortfolioService.get_project_by_id(id)
    return render_template('admin/portfolio_form.html', project=project)

@portfolio_bp.route('/portfolio/delete/<int:id>', methods=['POST'])
@login_required
@admin_required
def delete_portfolio(id):
    PortfolioService.delete_project(id)
    flash('Projet supprimé.', 'success')
    return redirect(url_for('portfolio.portfolio'))
