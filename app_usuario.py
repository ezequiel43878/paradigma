from flask import Flask 
from flask import render_template
import forms
from wtforms import validators
from flask import request
import csv

app = Flask(__name__)

@app.route('/')
def index():
	lista = [21,12,312]
	with open ("lista.csv") as usuario:
		valores = csv.reader (usuario)
		
		for x in valores:
			print (x[0])
		
	return render_template('lista_bossa.html', valores = lista )
	print (lista)	
if __name__ == ('__main__'):
	app.run(debug = True)	