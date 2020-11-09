from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config) # config -> module, Config -> class
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models # at bottom, needs to import app var defined above
