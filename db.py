from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_mail import Mail

migrate = Migrate()
db = SQLAlchemy()
ma = Marshmallow()
mail = Mail()