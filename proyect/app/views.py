from flask import Blueprint
from flask import render_template, request

from .forms import LoginForm #importamos la clase definida en forms.py

page = Blueprint('page', __name__)

@page.app_errorhandler(404)
def page_not_found(error):
   return render_template('errors/404.html'), 404 # para renderisar paginas que no existen
   #se para el error , 404

@page.route('/')
def index():
   return render_template('index.html', title='Index')

@page.route('/about')
def about():
   return render_template('about.html', title='About')

@page.route('/login', methods=['GET', 'POST'])
def login():

   form = LoginForm(request.form) # se crea una nueva instancia de LoginForm
   #se pasa como argumento request.form que viene del formilario 

   if request.method == 'POST' and form.validate():
      #obtener los valores del form
      print(form.username.data)
      print(form.password.data)
      print('Nueva sesion')

   return render_template('auth/login.html', title='Login', form=form)
