from app import app, db # flask app is member of app package
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}

# to run, in venv type
# export FLASK_APP=personal_site.py
# flask run

# to manage migrating databases,
# flask db init    --> create migration repository
# flask db migrate --> generate automatic migrations
# flask db upgrade --> apply migration scripts to the database
# flask db downgrade --> undo the recent migration upgrade