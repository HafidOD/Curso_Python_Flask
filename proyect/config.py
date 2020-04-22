class Config:
    SECRET_KEY = 'br84yjryh13weg51<ej48etrfhg5<egw'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='mysql://root:$$@localhost/python_web'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}