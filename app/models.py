#!/usr/bin/env python3

"""[Module to handle users]
"""
from flask import Flask, request
from flask.json import jsonify
import uuid


class User:
    """[Class user]
    """

    def signup(self):
        """[Return the user object if json format]
        """
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }
        return jsonify(user), 200