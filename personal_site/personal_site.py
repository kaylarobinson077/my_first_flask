from app import app # flask app is member of app package

# to run, in venv type
# export FLASK_APP=personal_site.py
# flask run

# to manage migrating databases,
# flask db init    --> create migration repository
# flask db migrate --> generate automatic migrations
# flask db upgrade --> apply migration scripts to the database
# flask db downgrade --> undo the recent migration upgrade