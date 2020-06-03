from app import app
from flask import jsonify
from app import mysql
import json
import base64

@app.route('/ping', methods=["GET"])
def ping():
    return jsonify({"Message": "ping correctly"})

@app.route('/questions', methods=["GET"])
def question():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM PREGUNTA')
    data = cur.fetchall()
    items = []
    for question in data:
        items.append({"id":question[0], "img": question[1], "enlace": question[2], "texto": question[3]})
    return jsonify({'questions':items})