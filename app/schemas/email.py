from app.models import Email
from app import ma

class EmailSchema(ma.Schema):
    class Meta:
        fields = ('id', 'sender', 'recipient', 'subject', 'body', 'created_at')
        model = Email

email_schema = EmailSchema()
emails_schema = EmailSchema(many=True)