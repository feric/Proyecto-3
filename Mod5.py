#!/usr/bin/env python
import time
from Reportes import Reportes
from PostgreSQL import Postgress
from correo import Correos
import datas
import os
import sys

dPhishing = ''

def main():
	#Se conecta a la base de datos
	repe = Postgress()
	#Obtiene los registros de la tabla de los datos phishing
	dPhishing = repe.Get_dPhishing()
	print dPhishing
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
		time.sleep(1)
		htmml = ReportName+".html"
		pedefe = ReportName+".pdf"
		enviar.sendMail(datas.destinatarios,'iPhishing <reportes@iPhishing.com>','Reporte de Phishing','Reporte de Phishing generado Hoy :)',[pedefe])
		#os.system("rm -f "+ReportName+"*")
		print "Enviando el correo"
		Reportes.puntitos()
		print "[OK]\nCorreo enviado"
		time.sleep(2)
		limpieza(ReportName)
	except:
		print "Fallo el envio de correo."

#Funcion que se encarga de eliminar los archivos que se generan al enviar el reporte
def limpieza(FileName):
	try:
		print "Borrando Archivos Generados"
		os.system("rm -f "+FileName+"*")
		Reportes.puntitos()
		print "[Ok]"
	except:
		print "Unable to delete files generated"

if __name__ =="__main__":
	main()
