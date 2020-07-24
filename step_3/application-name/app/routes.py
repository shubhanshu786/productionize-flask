from app import app, logger
from app.services import data_service
from flask import jsonify

@app.route('/')
@app.route('/index/<name>')
def index(name):
    users = data_service.get_user_information(name)
    logger.info('log something something')
    return jsonify(users)
