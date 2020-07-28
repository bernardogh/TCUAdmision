from app import app
from flask import jsonify
from app import mysql
import json
import base64
from flask_cors import CORS
CORS(app, support_credentials=True)

@app.route('/ping', methods=["GET"])
def ping():
    return jsonify({"Message": "ping correctly"})

@app.route('/questions', methods=["GET"])
def question():
    cur = mysql.get_db().cursor()
    cur.execute('SELECT * FROM PREGUNTA')
    data = cur.fetchall()
    items = []
    for question in data:
        items.append({"id":question[0], "img": question[1], "enlace": question[2], "texto": question[3]})
    return jsonify({'questions':items})


@app.route('/exams', methods=["GET"])
def exam():
    cur = mysql.get_db().cursor()
    cur.execute('SELECT * FROM EXAMEN')
    data = cur.fetchall()
    items = []
    for exam in data:
        items.append({"EXM_CODIGO":exam[0], "ANHO": exam[1], "NOMBRE": exam[2]})
    return jsonify({'exams':items})

@app.route('/questionFromExam/<int:EXM_CODIGO>', methods=["GET"])
def questionFromExam(EXM_CODIGO):
    cur = mysql.get_db().cursor() 
    cur.execute('select * from admisionucr.pregunta INNER JOIN admisionucr.ex_contiene_pre on admisionucr.pregunta.CODIGO_PREGUNTA = admisionucr.ex_contiene_pre.CODIGO_PREGUNTA where EXM_CODIGO ='  + str(EXM_CODIGO))
    data = cur.fetchall()
    items = []
    for question in data:
        items.append({"CODIGO_PREGUNTA":question[0], "PREGUNTA_IMAGEN":question[1], "TEXTO_PREGUNTA":question[3]})
    return jsonify({'question':items})

@app.route('/answersFromQuestion/<int:CODIGO_PREGUNTA>', methods=["GET"])
def answersFromQuestion(CODIGO_PREGUNTA):
    cur = mysql.get_db().cursor() 
    cur.execute('select * from admisionucr.respuesta INNER JOIN admisionucr.pres_compuesta_resp on admisionucr.respuesta.RESP_CODIGO = admisionucr.pres_compuesta_resp.RESP_CODIGO where CODIGO_PREGUNTA ='  + str(CODIGO_PREGUNTA))
    data = cur.fetchall()
    items = []
    for answers in data:
        items.append({"RESP_CODIGO":answers[0],"RESP_CORRECTO":answers[1],"TEXTO_RESPUESTA":answers[2]})
    return jsonify({'answers':items})

@app.route('/answersById/<int:CODIGO_PREGUNTA>', methods=["GET"])
def answersById(CODIGO_PREGUNTA):
    cur = mysql.get_db().cursor() 
    cur.execute('SELECT * FROM admisionucr.pregunta where Codigo_Pregunta = '  + str(CODIGO_PREGUNTA))
    data = cur.fetchall()
    items = []
    for answer in data:
        items.append({"CODIGO_PREGUNTA":answer[0],"TEXTO_PREGUNTA":answer[3]})
    return jsonify({'answer':items})


