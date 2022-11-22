# https://www.youtube.com/watch?v=LP8besicfH4
# mysql denied
# https://stackoverflow.com/questions/10299148/mysql-error-1045-28000-access-denied-for-user-billlocalhost-using-passw


import mysql.connector 
from flask import Flask, make_response, jsonify, request
from db import Users


mydb = mysql.connector.connect(
    host='0.0.0.0',
    user='myuser',
    password='mypass',
    database='Pycodebr',
    # port=3307
    
)

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

@app.route('/users', methods=['GET'])
def get_users():

    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM users')
    my_users = my_cursor.fetchall()

    print(my_users)

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
