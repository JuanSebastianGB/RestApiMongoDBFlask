from flask import Flask
from app import app
from flask.templating import render_template
from app.models import User


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")


@app.route('/user/signup/', methods=['POST'])
def signup():
    return User().signup()
