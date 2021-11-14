"""Start app point"""
from flask import Flask, sessions
import pymongo
from werkzeug.utils import redirect

app = Flask(__name__)

'Calling key with python -c "import os; print(os.urandom(16))"'
app.secret_key = b'\xd3\xe0Rr8[\xfc\x83I\xb2\xce\x90\x9f\x84\x7f2'

'Conecting with mongodb'
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_sytem

'Decorators'
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        return redirect("/")
    return wrap


from app import routes, models
