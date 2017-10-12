
import csv

try:
	with open ("lista.csv") as archivo:
		print ("El archivo se abrio correctamente")
	
except FileNotFoundError:						
	print ("Archivo no existe")		
except PermissionError:
	print ("No tiene permisos para abrir este archivo") 





