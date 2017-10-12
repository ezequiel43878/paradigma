from wtforms import Form 
from wtforms import StringField, PasswordField

class Form_loguin(Form):
	user = StringField('Usuario')
	password = PasswordField('Contraseña')

