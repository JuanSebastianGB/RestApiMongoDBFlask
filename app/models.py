#!/usr/bin/env python3

"""[Module to handle users]
"""
from flask import Flask, request, session, redirect
from flask import json
from flask.json import jsonify
import uuid
from passlib.hash import pbkdf2_sha256
from app import db


class User:
    """[Class user]
    """

    def start_session(self, user):
        """Start session variables logged_in and user and
        return code 200 if success"""
        del user["password"]
        session["logged_in"] = True
        session["user"] = user
        return jsonify(user), 200

    def signup(self):
        """[Adding a new user if success]
        """
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }
        user['password'] = pbkdf2_sha256.hash(user['password'])

        if db.users.find_one({"email": user["email"]}):
            return jsonify({"error": "Email already in use"}), 400

        if db.users.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "signup failed"}), 400

    def signout(self):
        """Implements signout by claring session and redirect to the form"""
        session.clear()
        return redirect("/")

    def login(self):
        """[Implements login into the system and redirect to dashboard]
        """
        user = db.users.find_one({
            "email": request.form.get("email")
        })
        if user and pbkdf2_sha256.verify(request.form.get("password"),
                                         user["password"]):
            return self.start_session(user)
        return jsonify({"error": "invalid login credentials"}), 401
