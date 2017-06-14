# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""
from flask import Flask
import requests
import pyrebase

config = {
    'apiKey': "AIzaSyCcb7m2E_hs8DqIHehqiqMLBJl9eOoYVGg",
    'authDomain': "bactive-4478f.firebaseapp.com",
    'databaseURL': "https://bactive-4478f.firebaseio.com",
    'projectId': "bactive-4478f",
    'storageBucket': "bactive-4478f.appspot.com",
    'messagingSenderId': "169114297124"
}
firebase = pyrebase.initialize_app(config)

import os

app = Flask(__name__)
db = firebase.database()
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("omerHaAdmin@gmail.com", "123456")
token = user['idToken']


@app.route('/')
def index():
    print(db.child('msgs').push({'hello': 'world'}, token))
    return "<html><body><h1>'Hello World'</h1></body></html>"


if __name__ == '__main__':
    app.run(debug=True)
