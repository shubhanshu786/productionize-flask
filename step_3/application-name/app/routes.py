from app import app, logger
from app.services import data_service
from flask import jsonify
from flask import request
import json
from app.utils.db_utils import AlchemyEncoder


@app.route('/')
@app.route('/index/')
def index():
    return jsonify("Welcome to Application")


@app.route('/api/all_results', methods=['GET'])
def get_all_data():
    all_data = data_service.get_all_data()
    return jsonify(all_data)


@app.route('/api/result/<int:id>', methods=['GET'])
def get_results(id):
    search_result = data_service.get_result_by_id(id)
    return jsonify(search_result)
    #return json.dumps(search_result, cls=AlchemyEncoder)


@app.route('/api/result/<int:id>', methods=['DELETE'])
def delete_results(id):
    search_result = data_service.delete_result_by_id(id)
    return jsonify(search_result)


@app.route('/api/process_doc', methods=['POST'])
def process_doc():
    text = request.args.get('text')
    task = request.args.get('task')
    result = data_service.process_query(text, task)
    return jsonify(result)
