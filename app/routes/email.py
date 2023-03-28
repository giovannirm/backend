from flask import Blueprint, jsonify, request
from flask_mail import Message

from app.models import Email
from app.schemas import email_schema
from db import db, mail

import os

email = Blueprint('emails', __name__)

# Endpoint para ver las sedes que existen
@email.route('/send_mail', methods=['POST'])
def send_mail():
    email_details = request.get_json()

    if 'recipient' in email_details and 'subject' in email_details and 'body' in email_details:

        sender = os.environ.get('MAIL_USERNAME')
        recipient = email_details["recipient"]
        subject = email_details["subject"]
        body = email_details["body"]

        email = Email(sender, recipient, subject, body)
        db.session.add(email)

        msg = Message(sender=sender, recipients=[recipient], subject=subject)
        msg.html = body
        mail.send(msg)

        db.session.commit()

        return email_schema.dump(email)
    else:
        return jsonify({'message':'Los campos a contener son recipient:str, subject:str, body:text'})
    
    
