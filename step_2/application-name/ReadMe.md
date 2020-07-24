## How to run

``flask db init`` It will generate migration folder. Nothing to do with that.

``flask db migrate`` It will generate create_table logic under migrations/versions folder 

``flask db upgrade`` Write create_table logic to database

``export FLASK_APP=server.py``

``flask run``