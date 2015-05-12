#!/usr/bin/env python
import time
from Reportes import Reportes
from PostgreSQL import Postgress
from correo import Correos

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
	try:
		generar = Reportes()
		ReportName = generar.Reporte_Incidentes(dPhishing[0][1],dPhishing[0][2],dPhishing[0][3],dPhishing[0][4],dPhishing[0][5],dPhishing[0][6],dPhishing[0][7],dPhishing[0][8],dPhishing[0][9],dPhishing[0][10],dPhishing[0][11])
	except:
		print "Unable connect to Database"
	try:
		enviar = Correos()
		time.sleep(2)
		htmml = ReportName+".html"
		pedefe = ReportName+".pdf"
		adjuntos = htmml,pedefe
		#print adjuntos[0]
		#print adjuntos[1]
		enviar.sendMail('dafteric@gmail.com','iPhishing <root@localhost.com>','Reporte de Phishing','Reporte de Phishing generado Hoy :)',[htmml,pedefe])
	except:
		print "Unable send email"
if __name__ =="__main__":
	main()
