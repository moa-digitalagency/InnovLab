from flask import Blueprint, request, flash, redirect, url_for, current_app
from services.submission_service import SubmissionService
from models import db

forms_bp = Blueprint('forms', __name__)

@forms_bp.route('/contact', methods=['POST'])
def contact_submit():
    email = request.form.get('email')
    if email:
        try:
            result = SubmissionService.process_quick_contact(email)
            if result is None:
                flash("Une erreur interne est survenue, veuillez réessayer plus tard.", "error")
            else:
                flash('Merci pour votre inscription!', 'success')
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Error in contact_submit: {e}")
            flash("Une erreur interne est survenue, veuillez réessayer plus tard.", "error")
    return redirect(url_for('main.index'))

@forms_bp.route('/contact-us', methods=['POST'])
def contact_us_submit():
    try:
        result = SubmissionService.process_contact_message(request.form)
        if result is None:
            flash("Une erreur interne est survenue, veuillez réessayer plus tard.", "error")
        else:
            flash('Votre message a été envoyé avec succès!', 'success')
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error in contact_us_submit: {e}")
        flash("Une erreur interne est survenue, veuillez réessayer plus tard.", "error")
    return redirect(url_for('main.contact_us'))

@forms_bp.route('/candidature/founder', methods=['POST'])
def founder_submit():
    try:
        file_pitch = request.files.get('file_pitch')
        result = SubmissionService.process_founder_application(request.form, file_pitch)
        if result is None:
            flash("Une erreur interne est survenue, veuillez réessayer plus tard.", "error")
        else:
            flash('Votre candidature a été envoyée avec succès!', 'success')
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error in founder_submit: {e}")
        flash("Une erreur interne est survenue, veuillez réessayer plus tard.", "error")
    return redirect(url_for('main.index'))

@forms_bp.route('/candidature/startup', methods=['POST'])
def startup_submit():
    try:
        file_pitch = request.files.get('file_pitch')
        result = SubmissionService.process_startup_application(request.form, file_pitch)
        if result is None:
            flash("Une erreur interne est survenue, veuillez réessayer plus tard.", "error")
        else:
            flash('Votre candidature a été envoyée avec succès!', 'success')
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error in startup_submit: {e}")
        flash("Une erreur interne est survenue, veuillez réessayer plus tard.", "error")
    return redirect(url_for('main.index'))

@forms_bp.route('/candidature/investor', methods=['POST'])
def investor_submit():
    try:
        file_intent = request.files.get('file_intent')
        result = SubmissionService.process_investor_application(request.form, file_intent)
        if result is None:
            flash("Une erreur interne est survenue, veuillez réessayer plus tard.", "error")
        else:
            flash('Votre demande a été envoyée avec succès!', 'success')
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error in investor_submit: {e}")
        flash("Une erreur interne est survenue, veuillez réessayer plus tard.", "error")
    return redirect(url_for('main.index'))
