#!/usr/bin/env python
import time
from Reportes import Reportes
from PostgreSQL import Postgress

dPhishing = ''

def main():
	#Se conecta a la base de datos
	repe = Postgress()
	#Obtiene los registros de la tabla de los datos phishing
	dPhishing = repe.Get_dPhishing()
	print dPhishing
#	for linea in dPhishing:
#		for element in linea:
#			print element
	############################################################
	# Seccion que usa funciones para la generacion de reportes #
	############################################################
	generar = Reportes()
	generar.Reporte_Incidentes(dPhishing[0][1],dPhishing[0][2],dPhishing[0][3],dPhishing[0][4],dPhishing[0][5],dPhishing[0][6],dPhishing[0][7],dPhishing[0][8],dPhishing[0][9],dPhishing[0][10],dPhishing[0][11])

if __name__ =="__main__":
	main()
