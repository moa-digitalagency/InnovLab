from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from security.decorators import admin_required
from models import db
from models.testimonial import Testimonial

testimonials_admin_bp = Blueprint('testimonials_admin', __name__, url_prefix='/admin/testimonials')

@testimonials_admin_bp.route('/')
@login_required
@admin_required
def index():
    testimonials = Testimonial.query.order_by(Testimonial.created_at.desc()).all()
    return render_template('admin/testimonials.html', testimonials=testimonials)

@testimonials_admin_bp.route('/add', methods=['POST'])
@login_required
@admin_required
def add():
    author_name = request.form.get('author_name')
    author_title = request.form.get('author_title')
    content = request.form.get('content')

    if not author_name or not author_title or not content:
        flash('Tous les champs sont requis.', 'error')
        return redirect(url_for('testimonials_admin.index'))

    testimonial = Testimonial(
        author_name=author_name,
        author_title=author_title,
        content=content
    )
    db.session.add(testimonial)
    db.session.commit()
    flash('Témoignage ajouté avec succès.', 'success')
    return redirect(url_for('testimonials_admin.index'))

@testimonials_admin_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
@admin_required
def delete(id):
    testimonial = Testimonial.query.get_or_404(id)
    db.session.delete(testimonial)
    db.session.commit()
    flash('Témoignage supprimé.', 'success')
    return redirect(url_for('testimonials_admin.index'))

@testimonials_admin_bp.route('/feature/<int:id>', methods=['POST'])
@login_required
@admin_required
def feature(id):
    testimonial = Testimonial.query.get_or_404(id)

    # Critical Logic: Unfeature all others first
    # Using bulk update for efficiency
    Testimonial.query.update({Testimonial.is_featured: False})

    # Feature the selected one
    testimonial.is_featured = True

    db.session.commit()
    flash(f'Témoignage de {testimonial.author_name} mis en vedette.', 'success')
    return redirect(url_for('testimonials_admin.index'))
