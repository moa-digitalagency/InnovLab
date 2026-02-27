from models.forms import FounderRequest, StartupRequest, InvestorRequest
from models.message import Message
from models.contact import Contact
from models import db
from services.file_service import save_file
from services.notification_service import send_telegram_notification
from flask import current_app
import html

class SubmissionService:
    @staticmethod
    def process_quick_contact(email):
        """
        Processes quick contact (newsletter/simple email).
        """
        if email:
            new_contact = Contact(email=email)
            try:
                db.session.add(new_contact)
                db.session.commit()
                return new_contact
            except Exception as e:
                db.session.rollback()
                current_app.logger.error(f"Database Error in process_quick_contact: {e}")
                return None
        return None

    @staticmethod
    def process_contact_message(form_data):
        """
        Processes the contact us form.
        """
        name = form_data.get('name')
        email = form_data.get('email')
        subject = form_data.get('subject')
        message = form_data.get('message')

        new_message = Message(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        try:
            db.session.add(new_message)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Database Error in process_contact_message: {e}")
            return None

        # Telegram Notification
        try:
            msg = (
                f"🟢 <b>NOUVEAU MESSAGE DE CONTACT</b>\n\n"
                f"👤 <b>Nom:</b> {html.escape(name)}\n"
                f"📧 <b>Email:</b> {html.escape(email)}\n"
                f"📝 <b>Sujet:</b> {html.escape(subject)}\n\n"
                f"💬 <b>Message:</b>\n{html.escape(message)}"
            )
            send_telegram_notification(msg)
        except Exception as e:
            current_app.logger.error(f"Telegram Notification Error: {e}")

        return new_message

    @staticmethod
    def process_founder_application(form_data, file=None):
        """
        Processes the founder application form.
        """
        nom = form_data.get('nom')
        email = form_data.get('email')
        projet_name = form_data.get('projet_name')
        description = form_data.get('description')
        project_stage = form_data.get('project_stage')
        primary_need = form_data.get('primary_need')

        filename = None
        if file:
            filename = save_file(file)

        new_founder = FounderRequest(
            nom=nom,
            email=email,
            projet_name=projet_name,
            description=description,
            project_stage=project_stage,
            primary_need=primary_need,
            file_pitch=filename
        )

        try:
            db.session.add(new_founder)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Database Error in process_founder_application: {e}")
            return None

        # Telegram Notification
        try:
            msg = (
                f"🚀 <b>Nouvelle Candidature Founder !</b>\n\n"
                f"👤 <b>Nom:</b> {html.escape(nom)}\n"
                f"💡 <b>Projet:</b> {html.escape(projet_name)}\n"
                f"📧 <b>Email:</b> {html.escape(email)}\n"
                f"🎯 <b>Besoin:</b> {html.escape(primary_need)}"
            )
            send_telegram_notification(msg)
        except Exception as e:
            current_app.logger.error(f"Telegram Notification Error: {e}")

        return new_founder

    @staticmethod
    def process_startup_application(form_data, file=None):
        """
        Processes the startup application form.
        """
        nom_startup = form_data.get('nom_startup')
        email = form_data.get('email')
        secteur = form_data.get('secteur')
        # Handle MultiDict getlist if available, otherwise assume list or string
        if hasattr(form_data, 'getlist'):
            besoins = ', '.join(form_data.getlist('besoins'))
        else:
            besoins = form_data.get('besoins') # Fallback

        website_url = form_data.get('website_url')
        annual_revenue = form_data.get('annual_revenue')
        team_size = form_data.get('team_size')
        stage = form_data.get('stage')

        filename = None
        if file:
            filename = save_file(file)

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

        try:
            db.session.add(new_startup)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Database Error in process_startup_application: {e}")
            return None

        # Telegram Notification
        try:
            msg = (
                f"🚀 <b>Nouvelle Candidature Startup !</b>\n\n"
                f"🏢 <b>Startup:</b> {html.escape(nom_startup)}\n"
                f"🏭 <b>Secteur:</b> {html.escape(secteur)}\n"
                f"📧 <b>Email:</b> {html.escape(email)}\n"
                f"📈 <b>Stage:</b> {html.escape(stage)}"
            )
            send_telegram_notification(msg)
        except Exception as e:
            current_app.logger.error(f"Telegram Notification Error: {e}")

        return new_startup

    @staticmethod
    def process_investor_application(form_data, file=None):
        """
        Processes the investor application form.
        """
        nom = form_data.get('nom')
        email = form_data.get('email')
        type_investisseur = form_data.get('type_investisseur')
        ticket_moyen = form_data.get('ticket_moyen')

        if hasattr(form_data, 'getlist'):
            sectors_interest = ', '.join(form_data.getlist('sectors_interest'))
        else:
            sectors_interest = form_data.get('sectors_interest')

        linkedin_profile = form_data.get('linkedin_profile')

        filename = None
        if file:
            filename = save_file(file)

        new_investor = InvestorRequest(
            nom=nom,
            email=email,
            type_investisseur=type_investisseur,
            ticket_moyen=ticket_moyen,
            sectors_interest=sectors_interest,
            linkedin_profile=linkedin_profile,
            file_intent=filename
        )

        try:
            db.session.add(new_investor)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Database Error in process_investor_application: {e}")
            return None

        # Telegram Notification
        try:
            msg = (
                f"💰 <b>Nouvelle Demande Investisseur !</b>\n\n"
                f"👤 <b>Nom:</b> {html.escape(nom)}\n"
                f"🏷️ <b>Type:</b> {html.escape(type_investisseur)}\n"
                f"📧 <b>Email:</b> {html.escape(email)}\n"
                f"💵 <b>Ticket:</b> {html.escape(ticket_moyen)}"
            )
            send_telegram_notification(msg)
        except Exception as e:
            current_app.logger.error(f"Telegram Notification Error: {e}")

        return new_investor
