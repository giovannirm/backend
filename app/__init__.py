from flask import Flask
from app.config import Config

# Import db, ma, migrate, mail
from db import db, ma, migrate, mail

from app.routes import *

def create_app(): # Función de fábrica
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Blueprints
    app.register_blueprint(email, url_prefix='/email')

    return app

