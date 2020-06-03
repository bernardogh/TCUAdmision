class Config(object):
    """
        This class handles all app configuration
        This is the class father, it contains all general configuration
    """
    DEBUG = False
    TESTING = False 
    #DataBase Configuration
    DB_NAME = 'production-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'
    MYSQL_PORT = 3307
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'contra15'
    MYSQL_DB = 'FlaskContacts'
    #Upload Files and max size
    UPLOADS = '/home/aizehn/Documents/Proyectos/python/flask/flask-tutorial/app/static/client/img/'
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG", "GIF"]
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024
    MAX_IMAGE_FILESIZE = 0.5 * 1024 * 1024
    #session handler
    SESSION_COOKIE_SECURE = False

 
class ProductionConfig(Config):
    """
    This class contains the configuration for production mode
    """
    pass


class DevelopmentConfig(Config):
    """
    This class contains the configuration for development mode
    """
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'contra15'
    MYSQL_DB = 'AdmisionDB'
    SECRET_KEY = '8VHfafBXctE46uufFVKf1Q'
    DB_NAME = 'AdmisionDB'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'contra15'
    IMAGE_UPLOADS = '/home/aizehn/Documents/Proyectos/python/flask/flask-tutorial/app/static/img/uploads'
    UPLOADS = '/home/aizehn/Documents/Proyectos/python/flask/flask-tutorial/app/static/img/'
    
    CLIENT_IMAGES = '/home/aizehn/Documents/Proyectos/python/flask/flask-tutorial/app/static/client/img'
    CLIENT_CSV = '/home/aizehn/Documents/Proyectos/python/flask/flask-tutorial/app/static/client/csv'
    CLIENT_PDF = '/home/aizehn/Documents/Proyectos/python/flask/flask-tutorial/app/static/client/pdf'
    
    
class TestingConfig(Config):
    """
    This class contains the configuration for testing mode
    """
    TESTING = True
    
    DB_NAME = 'development-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'
    
    UPLOADS = '/home/aizehn/Documents/Proyectos/python/flask/flask-tutorial/app/static/img/'
    
    
