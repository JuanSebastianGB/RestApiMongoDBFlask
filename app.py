#!/usr/bin/env python3
"""Starting point of the app"""

from flask import Flask
from app import app


if __name__ == "__main__":
    app.run(debug=True, port=5001)
