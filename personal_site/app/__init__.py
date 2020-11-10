from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config) # config -> module, Config -> class
db = SQLAlchemy(app)
login = LoginManager(app)
login = LoginManager(app)
login.login_view = "login"
migrate = Migrate(app, db)

from app import routes, models # at bottom, needs to import app var defined above
