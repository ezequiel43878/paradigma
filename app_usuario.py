from flask import Flask 
from flask import render_template
import forms
from wtforms import validators
from flask import request
import csv

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
	form_loguin = forms.Form_loguin(request.form)
	usuario = form_loguin.user.data
	password = form_loguin.password.data
	with open ("usuario.csv") as usuario:
		valores = csv.reader (usuario)
		for x in valores:
			print (x[0])
		    print (x[0])
		



	return render_template('index.html', form_loguin = form_loguin)

if __name__ == ('__main__'):
	app.run(debug = True)	
