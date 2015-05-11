#!/usr/bin/env python
import time
from Reportes import Reportes
from PostgreSQL import Postgress

dPishing = ''

def main():
	#Se conecta a la base de datos
	repe = Postgress()
	#Obtiene los registros de la tabla de los datos phishing
	dPhishing = repe.Get_dPhishing()
	for linea in dPhishing:
		for element in linea:
			print element
	############################################################
	# Seccion que usa funciones para la generacion de reportes #
	############################################################
	#generar = Reportes()
	#generar.Reporte_Incidentes(dPishing)

if __name__ =="__main__":
	main()
