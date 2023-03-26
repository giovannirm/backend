from app import create_app

from flask import render_template
import os

# Models
from app.models import *

app = create_app()

# Datatable en la ruta raíz
@app.route('/')
def index():
    emails = Email.query.all()
    return render_template('index.html', emails=emails)

if __name__ == "__main__":
    app.run(debug=os.environ.get('FLASK_DEBUG'))