## How to run

``pip install -U flask-cors`` To enable CORS

``export FLASK_APP=server.py``

``gunicorn --bind 0.0.0.0:5000 -w 1 -t 150 app:app``