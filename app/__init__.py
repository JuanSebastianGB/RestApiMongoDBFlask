from flask import Flask
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_sytem

from app import routes, models