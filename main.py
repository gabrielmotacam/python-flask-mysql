# https://www.youtube.com/watch?v=LP8besicfH4

import mysql.connector 
from flask import Flask, make_response, jsonify, request
from db import Users


mydb = mysql.connector.connect(
    host='localhost',
    user='MainUser',
    password='MainPassword',
    database='Pycodebr'
)

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

@app.route('/users', methods=['GET'])
def get_users():
    return make_response(
        jsonify(Users)
    )

@app.route('/create', methods=['POST'])
def create_user():
    add_user = request.json
    Users.append(add_user)
    return make_response(
        jsonify(
            message='user added successfully.',
            user=add_user
            )
    )

app.run()
