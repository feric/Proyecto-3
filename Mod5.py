#!/usr/bin/env python
# coding: utf-8

import time
from Reportes import Reportes
from PostgreSQL import Postgress
from correo import Correos
import datas
import os
import sys

dPhishing = ''

def main():
	#################################
	#  Conexión a la base de datos  #
	#################################
	repe = Postgress()
	###########################################################
	# Obtiene los registros de la tabla de los datos phishing #
	###########################################################
	dPhishing = repe.Get_dPhishing()
	print dPhishing
	############################################################
	# Sección que usa funciones para la generacion de reportes #
	############################################################
	try:
		generar = Reportes()
		ReportName = generar.Reporte_Incidentes(dPhishing[0][0],dPhishing[0][1],dPhishing[0][2],dPhishing[0][3],dPhishing[0][4],dPhishing[0][5],dPhishing[0][6],dPhishing[0][7],dPhishing[0][8],dPhishing[0][9],dPhishing[0][10],dPhishing[0][11],dPhishing[0][12],dPhishing[0][13],dPhishing[0][14],dPhishing[0][15],dPhishing[0][16],dPhishing[0][17],dPhishing[0][18],dPhishing[0][19],dPhishing[0][20])
	except:
		print "Error unexpected trying generated reports"
	####################################################
	# Sección que usa módulos para el envío de correos #
	# 					con Postfix					   #
	####################################################
	try:
		enviar = Correos()
		time.sleep(1)
		htmml = ReportName+".html"
		pedefe = ReportName+".pdf"
		#################################################################
		# Los destinatarios de los reportes se encuentran en el archivo #
		# 						datas.py 								#
		################################l#################################
		#enviar.sendMail(datas.destinatarios,'iPhishing <reportes@iPhishing.com>','Reporte de Phishing','Reporte de Phishing generado Hoy :)',[pedefe])
		enviar.sendMail(datas.destinatarios,'iPhishing <reportes@iPhishing.com>',datas.asunto,datas.cuerpo.format(dPhishing[0][0],dPhishing[0][2],dPhishing[0][5]),[pedefe])
		print "Enviando el correo"
		Reportes.puntitos()
		print "[OK]\nCorreo enviado"
		time.sleep(2)
		limpieza(ReportName)
	except:
		print "Falló el envio de correo."

def bdPSQL():
	#################################
	#  Conexión a la base de datos  #
	#################################
	repe = Postgress()
	###########################################################
	# Obtiene los registros de la tabla de los datos phishing #
	###########################################################
	dPhishing = repe.Get_dPhishing()
	pos = 0
	for i in dPhishing[0]:
		print "dPhishing[0][{0}] = {1}".format(pos,dPhishing[0][pos])
		pos+=1
	#print dPhishing

###################################################
# Funcion que se encarga de eliminar los archivos #
#	 	que se generan al enviar el reporte		  #
###################################################
def limpieza(FileName):
	try:
		print "Borrando Archivos Generados"
		os.unlink(FileName+".html")
		os.unlink(FileName+".pdf")
		Reportes.puntitos()
		print "[Ok]"
	except:
		print "Unable to delete files generated"

if __name__ =="__main__":
	main()
	#bdPSQL()
