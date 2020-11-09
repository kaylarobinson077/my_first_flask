from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route("/")      # decorator, associates url '/' as arg to function
@app.route("/index") # decorator, associates url '/index' as arg to function
def index():
    user = {"username": "Kayla"}
    posts = [
        {
          "author": {"username": "Chris"},
          "body": "I like bikes!"
        },
        {
            "author": {"username": "Kayla"},
            "body": "I like programming!"
        }
    ]
    
    return render_template("index.html", title="Home", user=user, posts=posts)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data))
        return redirect("{{ url_for('index') }}")
    return render_template("login.html", title="Sign In", form=form)