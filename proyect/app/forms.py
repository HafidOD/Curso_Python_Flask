from wtforms import Form, StringField, PasswordField #, BooleanField,  validators
# stringfield convertira el texto en string y passwordfiel en tipo pass

from wtforms import validators

class LoginForm(Form):
    username = StringField('Username', [
        validators.length(min=4, max=20, message='El nombre de usuario tiene que ser mayor a 4 caracteres')
    ]) #reciben el label del form
    password = PasswordField('Password',[
        validators.Required()
    ])