from flask import Flask
from app.config.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Application declaration
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import all routes and models
from app.routes import *
from app.models.user import *


