from app import db

class Email(db.Model):
    __tablename__ = 'emails'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    
    sender = db.Column(db.String(100), nullable=False)
    recipient = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    body = db.Column(db.Text)

    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    def __init__(self, sender, recipient, subject, body):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body