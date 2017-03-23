import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:PostgreSQL@localhost/Project1Database'
app.debug = True
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
CSRF_ENABLED = True

from app import models

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads\\')

ALLOWED_EXTENSIONS = {"png", 'jpg', 'jpeg', 'gif'}

app.config.from_object(__name__)

from app import views