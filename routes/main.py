from flask import Blueprint, render_template, request, flash, redirect, url_for
from models.contact import Contact
from models import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main_bp.route('/contact', methods=['POST'])
def contact():
    email = request.form.get('email')
    if email:
        new_contact = Contact(email=email)
        db.session.add(new_contact)
        db.session.commit()
        flash('Merci pour votre inscription!', 'success')
    return redirect(url_for('main.index'))
