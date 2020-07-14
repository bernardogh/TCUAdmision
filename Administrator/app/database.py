from app import app
app.config['SECRET_KEY'] = 'super secret key'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'contra15'
app.config['MYSQL_DATABASE_DB'] = 'ADMISIONUCR'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3307