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


@app.route('/users', methods=["GET"])
def users():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM USUARIO')
    data = cur.fetchall()
    items = []
    for user in data:
        items.append({"USU_CODIGO_USUARIO":user[0], "USU_NOMBRE": user[1], "USU_APELLIDO": user[2], "USU_CORREO": user[3], "USU_TIPO": user[5], })
    return jsonify({'users':items})