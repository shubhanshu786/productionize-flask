from app import app
from app.services import data_service
from flask import jsonify
from flask import request
from flask_api import status


@app.route('/')
@app.route('/index/')
def index():
    return jsonify("Welcome to Application"), status.HTTP_200_OK


@app.route('/api/all_results', methods=['GET'])
def get_all_data():
    all_data = data_service.get_all_data()
    if all_data:
        return jsonify(all_data), status.HTTP_200_OK
    else:
        return jsonify(all_data), status.HTTP_204_NO_CONTENT


@app.route('/api/result/<int:id>', methods=['GET'])
def get_results(id):
    search_result = data_service.get_result_by_id(id)
    if search_result:
        return jsonify(search_result), status.HTTP_200_OK
    else:
        return jsonify(search_result), status.HTTP_204_NO_CONTENT


@app.route('/api/result/<int:id>', methods=['DELETE'])
def delete_results(id):
    search_result = data_service.delete_result_by_id(id)
    return jsonify(search_result), status.HTTP_200_OK


@app.route('/api/process_doc', methods=['POST'])
def process_doc():
    text = request.args.get('text')
    task = request.args.get('task')
    result = data_service.process_query(text, task)
    if result == "":
        return jsonify(result), status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        return jsonify(result), status.HTTP_201_CREATED
