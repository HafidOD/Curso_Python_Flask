from flask import Flask
from flask_bootstrap import Bootstrap 
from flask_wtf.csrf import CSRFProtect # pip install Flask-WTF
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
csrf = CSRFProtect() # from flask_wtf.csrf import CSRFProtect
bootstrap = Bootstrap() # from flask_bootstrap import Bootstrap

from .views import page
from .models import User

def create_app(config):
    app.config.from_object(config)
    
    csrf.init_app(app)
    bootstrap.init_app(app) #iniciar boots
    app.register_blueprint(page) # from .views import page

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app