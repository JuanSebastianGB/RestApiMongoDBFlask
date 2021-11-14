from flask import Flask, redirect, session
from app import app
from flask.templating import render_template
from app.models import User
from functools import wraps

'Decorators'


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        return redirect("/")
    return wrap


@app.route('/')
def home():
    """Return to Home view"""
    return render_template("home.html")


@app.route('/dashboard/')
@login_required
def dashboard():
    """Return to Dashboard view"""
    return render_template("dashboard.html")


@app.route('/user/signup/', methods=['POST'])
def signup():
    """Stores a new user in the mongo database"""
    return User().signup()


@app.route('/user/signout')
def signout():
    """Implement signout by typting the route"""
    return User().signout()
