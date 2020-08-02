from app import app, logger
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


@app.errorhandler(404)
def all_errors(e):
    return jsonify(error="Requested API endpoint not found"), status.HTTP_400_BAD_REQUEST


@app.after_request
def log_request(response):
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    host = request.host.split(':', 1)[0]
    args = dict(request.args)
    log_params = [
        ('method', request.method),
        ('path', request.path),
        ('status', response.status_code),
        ('ip', ip),
        ('host', host),
        ('params', args)
    ]
    request_id = request.headers.get('X-Request-ID')
    if request_id:
        log_params.append(('request_id', request_id))

    parts = []
    for name, value in log_params:
        part = "{}={}".format(name, value)
        parts.append(part)
    line = " ".join(parts)
    if response.status_code == status.HTTP_200_OK or response.status_code == status.HTTP_201_CREATED or \
            response.status_code == status.HTTP_204_NO_CONTENT:
        logger.info(line)
    else:
        logger.error(line)
    return response

