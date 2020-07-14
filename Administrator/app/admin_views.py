from app import app
from flask import render_template
from flask import request, redirect
from flask import url_for, flash
from app import mysql
from flask import session
import base64
@app.route("/sign-in")
def login():
    return render_template('admin/login.html')


@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    if request.method == 'POST':
        user = request.form['user']
        passw = request.form['pass']
        cur = mysql.get_db().cursor()
        cur.execute('SELECT * FROM USUARIO WHERE USU_CORREO = %s AND USU_CONTRASENHA = %s',(user, passw))
        data = cur.fetchall()
        
        cur.execute('SELECT COUNT(USU_CODIGO_USUARIO) FROM USUARIO')
        counter_users = cur.fetchall()

        cur.execute('SELECT COUNT(CODIGO_PREGUNTA) FROM PREGUNTA')
        counter_questions = cur.fetchall()

        cur.execute('SELECT COUNT(EXM_CODIGO) FROM EXAMEN')
        counter_exam = cur.fetchall()

        cur.execute('SELECT COUNT(INT_CODIGO) FROM INTENTO')
        counter_int = cur.fetchall()

        if len(data) == 0:
            flash('El usuario o la contrasena son incorrectos!', 'danger')
            return redirect(url_for('login'))
        else:
            if data[0][5] == 'ADMIN':
                if not session.get("USERNAME") is None:
                    flash("Ya tienes una sesion iniciada")
                    return render_template('admin/dashboardIndex.html', user=data[0][3], counter_users=counter_users[0][0], counter_questions=counter_questions[0][0], counter_exam=counter_exam[0][0], counter_int=counter_int[0][0])
                else:
                    session["USERNAME"] = user
                    return render_template('admin/dashboardIndex.html', user=data[0][3], counter_users=counter_users[0][0], counter_questions=counter_questions[0][0], counter_exam=counter_exam[0][0], counter_int=counter_int[0][0])
            else:
                flash('Tu usuario no cuenta con los privilegios necesarios...!!!')
                return redirect(url_for('login'))
    else: 
        if not session.get("USERNAME") is None:
            users = session.get("USERNAME")
            print(users)
            print(type(users))
            cur = mysql.get_db().cursor()
            cur.execute("SELECT * FROM USUARIO WHERE USU_CORREO = %s", (users, ))
            data = cur.fetchall()
        
            cur.execute('SELECT COUNT(USU_CODIGO_USUARIO) FROM USUARIO')
            counter_users = cur.fetchall()

            cur.execute('SELECT COUNT(CODIGO_PREGUNTA) FROM PREGUNTA')
            counter_questions = cur.fetchall()

            cur.execute('SELECT COUNT(EXM_CODIGO) FROM EXAMEN')
            counter_exam = cur.fetchall()

            cur.execute('SELECT COUNT(INT_CODIGO) FROM INTENTO')
            counter_int = cur.fetchall()
            return render_template('admin/dashboardIndex.html', user=data[0][3], counter_users=counter_users[0][0], counter_questions=counter_questions[0][0], counter_exam=counter_exam[0][0], counter_int=counter_int[0][0])
        else:
            flash('Debes iniciar sesion...!!!', 'danger')
            return redirect(url_for('login'))
    return render_template('admin/dashboardIndex.html', user='aizehn')

@app.route("/sign-out")
def sign_out():
    session.pop("USERNAME", None)
    return redirect(url_for("login"))


@app.route("/dashboard/create_user")
def create_user():
    if not session.get("USERNAME") is None:
        return render_template('admin/create_user.html', user=session.get("USERNAME"))
    else:
        flash('Debes iniciar sesion...!!!')
        return redirect(url_for("login"))

@app.route("/dashboard/addexam")
def create_exam():
    if not session.get("USERNAME") is None:
        return render_template('admin/addexam.html', user=session.get("USERNAME"))
    else:
        flash('Debes iniciar sesion...!!!')
        return redirect(url_for("login"))


@app.route("/dashboard/create_user/save", methods=["POST"])
def saveuser():
    name = request.form['name']
    lastname = request.form['lastname']
    user = request.form['user']
    passw = request.form['pass']
    admin = 'ADMIN'
    cur = mysql.get_db().cursor()
    cur.execute('INSERT INTO USUARIO (USU_NOMBRE, USU_APELLIDO, USU_CORREO, USU_CONTRASENHA, USU_TIPO) VALUES (%s, %s, %s, %s, %s)', (name, lastname, user, passw, admin))
    mysql.get_db().commit()
    flash(u'El usuario se guardo existosamente', 'success')
    return redirect(url_for("dashboard"))

@app.route("/dashboard/modify_user")
def modify_user():
    cur = mysql.get_db().cursor()
    cur.execute('SELECT * FROM USUARIO')
    data = cur.fetchall()
    return render_template('admin/modify.html', users = data)

@app.route("/dashboard/exams")
def exams():
    cur = mysql.get_db().cursor()
    cur.execute('SELECT * FROM EXAMEN')
    data = cur.fetchall()
    return render_template('admin/exams.html', exams = data)

@app.route("/dashboard/mu/<id>")
def modifyUser(id):
    cur = mysql.get_db().cursor()
    cur.execute('SELECT * FROM USUARIO WHERE USU_CODIGO_USUARIO = %s', (id,))
    data = cur.fetchall()
    print(data[0])
    return render_template('admin/modify_specifcU.html', user=session.get("USERNAME"), muser=data[0])

@app.route("/dashboard/modify_user/modify/<id>", methods=["POST"])
def muser(id):
    name = request.form['name']
    lastname = request.form['lastname']
    user = request.form['user']
    passw = request.form['pass']
    admin = 'ADMIN'
    cur = mysql.get_db().cursor()
    cur.execute('UPDATE USUARIO SET USU_NOMBRE=%s, USU_APELLIDO=%s, USU_CORREO=%s, USU_CONTRASENHA=%s, USU_TIPO=%s WHERE USU_CODIGO_USUARIO= %s', (name, lastname, user, passw, admin, id))
    mysql.get_db().commit()
    flash(u'El usuario se modifico existosamente', 'success')
    return redirect(url_for("modify_user"))

@app.route('/dashboard/delete/<id>')
def delUser(id):
    cur = mysql.get_db().cursor()
    cur.execute('DELETE FROM USUARIO WHERE USU_CODIGO_USUARIO = %s', (id,))
    mysql.get_db().commit()
    flash(u'El usuario se elimino existosamente', 'success')
    return redirect(url_for("modify_user"))


def allowed_image(filename):
    
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route('/dashboard/modify-question')
def modifyquestion():
    cur = mysql.get_db().cursor()
    cur.execute('SELECT * FROM PREGUNTA')
    data = cur.fetchall()
    return render_template('admin/modifyquestion.html', questions=data)


@app.route('/dashboard/addquestion', methods=["GET", "POST"])
def addquestion():
    if request.method == "POST":
        question = "\\[ "+ request.form['pregunta'] + " \\]" 
        answer = "\\[ "+ request.form['respuesta'] + " \\]"
        link = request.form['enlace']
        answer1 = "\\[ "+ request.form['respuesta1'] + " \\]"
        answer2 = "\\[ "+ request.form['respuesta2'] + " \\]"
        answer3 = "\\[ "+ request.form['respuesta3'] + " \\]"
        if request.files:
            print('asdasdadasdddddddddddddddd')
            if "filesize" in request.cookies:
                if not allowed_image_filesize(request.cookies["filesize"]):
                    flash("Filesize exceeded maximum limit", "danger")
                    return redirect(request.url)
                image = request.files["imgInp"]
                if image.filename == "":
                    flash("No filename", "danger")
                    return redirect(request.url)
                if allowed_image(image.filename):
                    image_string = base64.b64encode(image.read())
                    cur = mysql.get_db().cursor()
                    
                    print('------------------------')
                    print(question)
                    print('------------------------')
                    cur.execute('INSERT INTO PREGUNTA (PREGUNTA_IMAGEN, PREGUNTA_ENLACE, TEXTO_PREGUNTA) VALUES (%s,%s,%s)', (image_string, link, question))
                    idpregunta = cur.lastrowid
                    cur.execute('INSERT INTO RESPUESTA (RESP_CORRECTO, TEXTO_RESPUESTA) VALUES (%s,%s)', (True, answer,))
                    id_respuesta = cur.lastrowid
                    cur.execute('INSERT INTO PRES_COMPUESTA_RESP (RESP_CODIGO, CODIGO_PREGUNTA) VALUES (%s,%s)', (id_respuesta, idpregunta,))

                    cur.execute('INSERT INTO RESPUESTA (RESP_CORRECTO, TEXTO_RESPUESTA) VALUES (%s,%s)', (False, answer1,))
                    id_respuesta = cur.lastrowid
                    cur.execute('INSERT INTO PRES_COMPUESTA_RESP (RESP_CODIGO, CODIGO_PREGUNTA)  VALUES (%s,%s)', (id_respuesta, idpregunta,))

                    cur.execute('INSERT INTO RESPUESTA (RESP_CORRECTO, TEXTO_RESPUESTA) VALUES (%s,%s)', (False, answer2,))
                    id_respuesta = cur.lastrowid
                    cur.execute('INSERT INTO PRES_COMPUESTA_RESP (RESP_CODIGO, CODIGO_PREGUNTA)  VALUES (%s,%s)', (id_respuesta, idpregunta,))

                    cur.execute('INSERT INTO RESPUESTA (RESP_CORRECTO, TEXTO_RESPUESTA) VALUES (%s,%s)', (False, answer3))
                    id_respuesta = cur.lastrowid
                    cur.execute('INSERT INTO PRES_COMPUESTA_RESP (RESP_CODIGO, CODIGO_PREGUNTA) VALUES (%s,%s)', (id_respuesta, idpregunta,))
                    mysql.get_db().commit()
                    flash('Se ha insertado correctamente','success')
                    return render_template('admin/addquestion.html') 
                else:

                    flash("That file extension is not allowed", "danger")
                    return redirect(request.url)
        else:
            flash("No image selected", "danger")
            return redirect(request.url)
    return render_template('admin/addquestion.html') 

def allowed_image_filesize(filesize):    
    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False


@app.route('/dashboard/modifyquestion/<id>')
def modifyquestionQ(id):
    cur = mysql.get_db().cursor()
    cur.execute('SELECT * FROM PREGUNTA INNER JOIN PRES_COMPUESTA_RESP ON PRES_COMPUESTA_RESP.CODIGO_PREGUNTA = PREGUNTA.CODIGO_PREGUNTA INNER JOIN RESPUESTA ON RESPUESTA.RESP_CODIGO = PRES_COMPUESTA_RESP.RESP_CODIGO WHERE PREGUNTA.CODIGO_PREGUNTA = %s;', (id,))
    question = cur.fetchall()
    return render_template('admin/modifyspecificQ.html', question=question)


@app.route('/dashboard/mud', methods=["GET","POST"])
def mud():
    if request.method == "POST":
        print('--------------------------')
        print(request.url)
        print('--------------------------')
        question = request.form['pregunta']
        idQ = request.form['id1']
        answer = request.form['respuesta']
        idC = request.form['respC']
        idI1 = request.form['respI1']
        idI2 = request.form['respI2']
        idI3 = request.form['respI3']
        link = request.form['enlace']
        answer1 = request.form['respuesta1']
        answer2 = request.form['respuesta2']
        answer3 = request.form['respuesta3']
        cur = mysql.get_db().cursor()
        if request.files:
            if "filesize" in request.cookies:
                if not allowed_image_filesize(request.cookies["filesize"]):
                    flash("Filesize exceeded maximum limit", "danger")
                    return redirect(request.url)
                image = request.files["imgInp"]
                if image.filename == "":
                    flash("No filename", "danger")
                    return redirect(request.url)
                if allowed_image(image.filename):
                    image_string = base64.b64encode(image.read())
                    cur.execute('UPDATE PREGUNTA SET PREGUNTA_IMAGEN = %s, PREGUNTA_ENLACE=%s, TEXTO_PREGUNTA=%s WHERE CODIGO_PREGUNTA=%s', (image_string, link, question, idQ))
            else:
                print('--------------------------')
                print(idQ)
                print('--------------------------')
                cur.execute('UPDATE PREGUNTA SET PREGUNTA_ENLACE=%s, TEXTO_PREGUNTA=%s WHERE CODIGO_PREGUNTA=%s', (link, question, idQ))
                cur.execute('UPDATE RESPUESTA SET TEXTO_RESPUESTA=%s WHERE RESP_CODIGO=%s', (answer, idC))
                cur.execute('UPDATE RESPUESTA SET TEXTO_RESPUESTA=%s WHERE RESP_CODIGO=%s', (answer1, idI1))
                cur.execute('UPDATE RESPUESTA SET TEXTO_RESPUESTA=%s WHERE RESP_CODIGO=%s', (answer2, idI2))
                cur.execute('UPDATE RESPUESTA SET TEXTO_RESPUESTA=%s WHERE RESP_CODIGO=%s', (answer3, idI3))
                mysql.get_db().commit()
    return redirect(url_for('modifyquestion'))