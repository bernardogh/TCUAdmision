from flask import Flask
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL(app)
mysql.init_app(app)

app.secret_key = "b'p\x83|y\xe5iN\x1d\x98\tEB\xe0\t\xe5\xba'"
if app.config["ENV"] == 'production':
    app.config.from_object('config.ProductionConfig')
elif app.config["ENV"] == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.DevelopmentConfig')
    
from app import database
from app import views
from app import admin_views
from app import rest_api
