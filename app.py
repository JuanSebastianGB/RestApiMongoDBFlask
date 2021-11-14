#!/usr/bin/env python3
from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

#Routes
from user import routes

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
