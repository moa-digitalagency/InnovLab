from flask import Blueprint, request, flash, redirect, url_for
from services.submission_service import SubmissionService

forms_bp = Blueprint('forms', __name__)

@forms_bp.route('/contact', methods=['POST'])
def contact_submit():
    email = request.form.get('email')
    if email:
        SubmissionService.process_quick_contact(email)
        flash('Merci pour votre inscription!', 'success')
    return redirect(url_for('main.index'))

@forms_bp.route('/contact-us', methods=['POST'])
def contact_us_submit():
    SubmissionService.process_contact_message(request.form)
    flash('Votre message a été envoyé avec succès!', 'success')
    return redirect(url_for('main.contact_us'))

@forms_bp.route('/candidature/founder', methods=['POST'])
def founder_submit():
    file_pitch = request.files.get('file_pitch')
    SubmissionService.process_founder_application(request.form, file_pitch)
    flash('Votre candidature a été envoyée avec succès!', 'success')
    return redirect(url_for('main.index'))

@forms_bp.route('/candidature/startup', methods=['POST'])
def startup_submit():
    file_pitch = request.files.get('file_pitch')
    SubmissionService.process_startup_application(request.form, file_pitch)
    flash('Votre candidature a été envoyée avec succès!', 'success')
    return redirect(url_for('main.index'))

@forms_bp.route('/candidature/investor', methods=['POST'])
def investor_submit():
    file_intent = request.files.get('file_intent')
    SubmissionService.process_investor_application(request.form, file_intent)
    flash('Votre demande a été envoyée avec succès!', 'success')
    return redirect(url_for('main.index'))
