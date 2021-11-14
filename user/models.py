#!/usr/bin/env python3

"""[Module to handle users]
"""
from flask import Flask
from flask.json import jsonify


class User:
    """[Class user]
    """

    def signup(self):
        """[Return the user object if json format]
        """
        user = {
            "_id": "",
            "name": "",
            "email": "",
            "password": ""
        }
        return jsonify(user), 200
