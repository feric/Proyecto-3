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
	######################################
	# Campos con sus respectivos valores #
	######################################
	url_Phishing = dPhishing[0][0]
	url_Redireccion = dPhishing[0][1]
	ip_Phishing = dPhishing[0][2]
	ip_Redireccion = dPhishing[0][3]
	url_Malware = dPhishing[0][4]
	institucion = dPhishing[0][5]
	#url_Phishing,url_Redireccion,ip_Phishing,ip_Redireccion,url_Malware,institucion,md5_cuckoo,sha1_cuckoo,nombre_adjunto_cuckoo,extension_cuckoo,tipo_Aplicacion,archivo_Referencia,fInicio,fFin,yara_cuckoo,rule_Packet_filter,rule_Net_filter,rule_Snort,datos_asn,datos_tor,datos_proxy
	
	###################
	# Datos de Cuckoo #
	###################
	md5_cuckoo = dPhishing[0][6]
	sha1_cuckoo = dPhishing[0][7]
	nombre_adjunto_cuckoo = dPhishing[0][8]
	extension_cuckoo = dPhishing[0][9]
	tipo_Aplicacion = dPhishing[0][10]
	archivo_Referencia = dPhishing[0][11]
	fInicio = dPhishing[0][12]
	fFin = dPhishing[0][13]
	yara_cuckoo = dPhishing[0][14]
	#######################
	# Datos de las Reglas #
	#######################
	rule_Packet_filter = dPhishing[0][15]
	rule_Net_filter = dPhishing[0][16]
	rule_Snort = dPhishing[0][17]
	##################
	# Datos de Whois #
	##################
	datos_asn = dPhishing[0][18]
	datos_tor = dPhishing[0][19]
	datos_proxy = dPhishing[0][20]
	#print dPhishing
	############################################################
	# Sección que usa funciones para la generacion de reportes #
	############################################################
	try:
		generar = Reportes()
		#ReportName = generar.Reporte_Incidentes(dPhishing[0][0],dPhishing[0][1],dPhishing[0][2],dPhishing[0][3],dPhishing[0][4],dPhishing[0][5],dPhishing[0][6],dPhishing[0][7],dPhishing[0][8],dPhishing[0][9],dPhishing[0][10],dPhishing[0][11],dPhishing[0][12],dPhishing[0][13],dPhishing[0][14],dPhishing[0][15],dPhishing[0][16],dPhishing[0][17],dPhishing[0][18],dPhishing[0][19],dPhishing[0][20])
		ReportName = generar.Reporte_Incidentes(url_Phishing,url_Redireccion,ip_Phishing,ip_Redireccion,url_Malware,institucion,md5_cuckoo,sha1_cuckoo,nombre_adjunto_cuckoo,extension_cuckoo,tipo_Aplicacion,archivo_Referencia,fInicio,fFin,yara_cuckoo,rule_Packet_filter,rule_Net_filter,rule_Snort,datos_asn,datos_tor,datos_proxy)
		ReportAdminName = generar.Reporte_Admins(url_Phishing,url_Redireccion,ip_Phishing,ip_Redireccion,url_Malware,institucion,rule_Packet_filter,rule_Net_filter,rule_Snort,datos_asn)
	except:
		print "Error unexpected trying generated reports"
	####################################################
	# Sección que usa módulos para el envío de correos #
	# 					con Postfix					   #
	####################################################
	try:
		enviar = Correos()
		time.sleep(1)
		#htmmlCSIRT = ReportName+".html"
		pdfCSIRT = ReportName+".pdf"
		#htmmlAdmin = ReportAdminName+".html"
		pdfAdmin = ReportAdminName+".pdf"
		#################################################################
		# Los destinatarios de los reportes se encuentran en el archivo #
		# 						datas.py 								#
		################################l################################
		#enviar.sendMail(datas.destinatarios,'iPhishing <reportes@iPhishing.com>','Reporte de Phishing','Reporte de Phishing generado Hoy :)',[pedefe])
		#enviar.sendMail(datas.destinatarios,'iPhishing <reportes@iPhishing.com>',datas.asunto,datas.cuerpo.format(dPhishing[0][0],dPhishing[0][2],dPhishing[0][5]),[pedefe])
		enviar.sendMail(datas.destinatarios,'iPhishing <reportes@iPhishing.com>',datas.asunto,datas.cuerpo.format(url_Phishing,ip_Phishing,institucion),[pdfCSIRT,pdfAdmin])
		print "Enviando el correo"
		Reportes.puntitos()
		print "[OK]\nCorreo enviado"
		time.sleep(2)
		limpieza((ReportName,ReportAdminName))
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
		Reportes.puntitos()
		os.unlink(FileName[0]+".html")
		os.unlink(FileName[0]+".pdf")
		os.unlink(FileName[1]+".html")
		os.unlink(FileName[1]+".pdf")
		print "[Ok]"
	except:
		print "Unable to delete files generated"

if __name__ =="__main__":
	main()
	#bdPSQL()
