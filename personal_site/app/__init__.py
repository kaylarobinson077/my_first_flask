from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config) # config -> module, Config -> class

from app import routes # at bottom, needs to import app var defined above
