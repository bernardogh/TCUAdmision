from app import app
app.config['SECRET_KEY'] = 'super secret key'
app.config['MYSQL_DATABASE_USER'] = 'admisionucr'
app.config['MYSQL_DATABASE_PASSWORD'] = 'DBAdminTCU.2020'
app.config['MYSQL_DATABASE_DB'] = 'admisionucr$ADMISIONUCR'
app.config['MYSQL_DATABASE_HOST'] = 'admisionucr.mysql.pythonanywhere-services.com'