from flask import Flask
from app.config.app_config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler
import os
import logging
import coloredlogs

coloredlogs.install()
# Application declaration
app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Logging setup
if not os.path.exists('logs'):
    os.mkdir('logs')
handler = TimedRotatingFileHandler('logs/system.log', when='D', encoding='utf-8', interval=1, backupCount=30)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
app.logger.setLevel(logging.INFO)
app.logger.addHandler(handler)
# another_logger = logging.getLogger('werkzeug')
# another_logger.addHandler(handler)
# import this logger in whole of your application to log
logger = app.logger
logger.info('Application started')

# import all routes and models
from app.routes import *
from app.models.search_data import *
