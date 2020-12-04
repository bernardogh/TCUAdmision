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
    print(data)
    items = []
    for exam in data:
        items.append({"EXM_CODIGO":exam[0], "NOMBRE": exam[2], "ANHO": exam[1]})
    return jsonify({'exams':items})


@app.route('/specificExam/<int:EXM_CODIGO>', methods=["GET"])
def specificExam(EXM_CODIGO):
    cur = mysql.get_db().cursor()
    cur.execute('SELECT * FROM EXAMEN WHERE EXM_CODIGO = '  + str(EXM_CODIGO))
    data = cur.fetchall()
    items = []
    for exam in data:
        items.append({"EXM_CODIGO":exam[0],"ANHO":exam[1],"NOMBRE":exam[2]})
    return jsonify({'exam':items})


@app.route('/questionFromExam/<int:EXM_CODIGO>', methods=["GET"])
def questionFromExam(EXM_CODIGO):
    cur = mysql.get_db().cursor()
    cur.execute('select * from PREGUNTA INNER JOIN EX_CONTIENE_PRE on PREGUNTA.CODIGO_PREGUNTA = EX_CONTIENE_PRE.CODIGO_PREGUNTA WHERE EXM_CODIGO ='  + str(EXM_CODIGO))
    data = cur.fetchall()
    items = []
    for question in data:
        items.append({"CODIGO_PREGUNTA":question[0], "PREGUNTA_IMAGEN":question[1], "TEXTO_PREGUNTA":question[3]})
    return jsonify({'question':items})

@app.route('/answersFromQuestion/<int:CODIGO_PREGUNTA>', methods=["GET"])
def answersFromQuestion(CODIGO_PREGUNTA):
    cur = mysql.get_db().cursor()
    cur.execute('SELECT * from RESPUESTA INNER JOIN PRES_COMPUESTA_RESP on RESPUESTA.RESP_CODIGO = PRES_COMPUESTA_RESP.RESP_CODIGO WHERE CODIGO_PREGUNTA ='  + str(CODIGO_PREGUNTA) + ' ORDER BY RAND() ')
    data = cur.fetchall()
    items = []
    for answers in data:
        items.append({"RESP_CODIGO":answers[0],"RESP_CORRECTO":answers[1],"TEXTO_RESPUESTA":answers[2]})
    return jsonify({'answers':items})

@app.route('/answersById/<int:CODIGO_PREGUNTA>', methods=["GET"])
def answersById(CODIGO_PREGUNTA):
    cur = mysql.get_db().cursor()
    cur.execute('SELECT * FROM PREGUNTA WHERE CODIGO_PREGUNTA = '  + str(CODIGO_PREGUNTA))
    data = cur.fetchall()
    items = []
    for answer in data:
        items.append({"CODIGO_PREGUNTA":answer[0],"PREGUNTA_IMAGEN":answer[1],"TEXTO_PREGUNTA":answer[3]})
    return jsonify({'answer':items})

@app.route('/cantidadPreguntas', methods=["GET"])
def cantidadPreguntas():
    cur = mysql.get_db().cursor()
    cur.execute('SELECT COUNT(*) CANTIDAD FROM PREGUNTA')
    data = cur.fetchall()
    items = []
    for answer in data:
        items.append({"cantidad":answer[0]})
    return jsonify({'cantidad':items})


