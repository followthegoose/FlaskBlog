
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager


app = Flask(__name__)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


from app import routes, models, errors