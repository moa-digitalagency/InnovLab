from flask import Blueprint, request, flash, redirect, url_for, current_app
from services.submission_service import SubmissionService
from services.notification_service import send_telegram_notification
from models import db
from models.security_logs import SecurityLog
import json

forms_bp = Blueprint('forms', __name__)

def check_honeypot():
    """
    Checks if the honeypot field 'website_url_check' is filled.
    If it is, logs the attempt, sends a Telegram alert, and returns True.
    """
    if request.form.get('website_url_check'):
        ip = request.remote_addr

        # Log incident
        log = SecurityLog(
            ip_address=ip,
            event_type='spam_honeypot',
            description='Honeypot field filled in form submission',
            user_agent=request.user_agent.string
        )
        try:
            db.session.add(log)
            db.session.commit()
        except Exception as e:
            current_app.logger.error(f"Failed to log security event: {e}")
            db.session.rollback()

        # Construct Reply Markup for Ban
        reply_markup = {
            "inline_keyboard": [
                [
                    {"text": "🚫 Bannir cette IP", "callback_data": f"ban_ip_{ip}"}
                ]
            ]
        }

        # Send alert
        send_telegram_notification(
            f"🚨 *SPAM DETECTED*\n"
            f"Honeypot triggered by IP: `{ip}`\n"
            f"User-Agent: {request.user_agent.string}\n"
            f"Action: Block proposed.",
            reply_markup=reply_markup
        )

        return True
    return False

@forms_bp.route('/contact', methods=['POST'])
def contact_submit():
    # Honeypot Check
    if check_honeypot():
        flash('Merci pour votre inscription!', 'success') # Fake success
        return redirect(url_for('main.index'))

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
    # Honeypot Check
    if check_honeypot():
        flash('Votre message a été envoyé avec succès!', 'success') # Fake success
        return redirect(url_for('main.contact_us'))

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
    # Honeypot Check
    if check_honeypot():
        flash('Votre candidature a été envoyée avec succès!', 'success') # Fake success
        return redirect(url_for('main.index'))

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
    # Honeypot Check
    if check_honeypot():
        flash('Votre candidature a été envoyée avec succès!', 'success') # Fake success
        return redirect(url_for('main.index'))

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
    # Honeypot Check
    if check_honeypot():
        flash('Votre demande a été envoyée avec succès!', 'success') # Fake success
        return redirect(url_for('main.index'))

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
