#!/usr/bin/env python
from time import sleep, strftime
from os import system
import datas
import sys

class Reportes:
	pathTemplate =''
	nombre = ''
	fiile=''
	def __init__(self):
		self.pathTemplate="./salcilocos/"
	def __del__(self):
		self.pathTemplate=''
	@staticmethod
	def puntitos():
		for c in ".......":
			sys.stdout.write("{0}".format(c))
			sys.stdout.flush()
			sleep(0.15)
	#def Reporte_Incidentes(self,pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9,pos10,pos11,pos12,pos13,pos14,pos15,pos16,pos17,pos18,pos19,pos20,pos21):
	def Reporte_Incidentes(self,url_Phishing,url_Redireccion,ip_Phishing,ip_Redireccion,url_Malware,institucion,md5_cuckoo,sha1_cuckoo,nombre_adjunto_cuckoo,extension_cuckoo,tipo_Aplicacion,archivo_Referencia,fInicio,fFin,yara_cuckoo,rule_Packet_filter,rule_Net_filter,rule_Snort,datos_asn,datos_tor,datos_proxy):
		try:
			print "Generando Reporte para el Equipo de Respuesta a incidentes"
			sleep(1)
			#archivoRI = open(self.pathTemplate+"template_csirt.html","r").read()
			archivoRI = datas.template_CSIRT
			archivoRI = archivoRI.format(url_Phishing,url_Redireccion,ip_Phishing,ip_Redireccion,url_Malware,institucion,md5_cuckoo,sha1_cuckoo,nombre_adjunto_cuckoo,extension_cuckoo,tipo_Aplicacion,archivo_Referencia,fInicio,fFin,yara_cuckoo,rule_Packet_filter,rule_Net_filter,rule_Snort,datos_asn,datos_tor,datos_proxy)
			nombre = self.pathTemplate+"ReportResponseTeam-"+strftime("%Y-%m-%d-%S")
			fiile = nombre+".html"
			pdfiile = nombre+".pdf"
			#############################
			# Genera el reporte en HTML #
			#############################
			rIncidentes = open(fiile,"w")
			rIncidentes.write(archivoRI)
			rIncidentes.close()
			############################
			# Genera el reporte en PDF #
			############################
			system("wkhtmltopdf {0} {1}".format(fiile,pdfiile))
			print """Reporte Generado {0}
Reporte Generado {1}
			""".format(fiile,pdfiile)
			return nombre
		except:
			print "No fue posible generar el reporte para el equipo de Respuesta a Incidentes"
	def Reporte_Admins(self,url_Phishing,url_Redireccion,ip_Phishing,ip_Redireccion,url_Malware,institucion,rule_Packet_filter,rule_Net_filter,rule_Snort,datos_asn):
		try:
			print "Generando Reporte para el Administrador"
			sleep(2)
			archivoRI = open(self.pathTemplate+"template_csirt.html","r").read()
			admRI = datas.template_Admin
			admRI = admRI.format(url_Phishing,url_Redireccion,ip_Phishing,ip_Redireccion,url_Malware,institucion,rule_Packet_filter,rule_Net_filter,rule_Snort,datos_asn)
			nombre = self.pathTemplate+"ReporteAdministrativo-"+strftime("%Y-%m-%d-%S")
			fiile = nombre+".html"
			pdfiile = nombre+".pdf"
			#############################
			# Genera el reporte en HTML #
			#############################
			rIncidentes = open(fiile,"w")
			rIncidentes.write(admRI)
			rIncidentes.close()
			############################
			# Genera el reporte en PDF #
			############################
			system("wkhtmltopdf {0} {1}".format(fiile,pdfiile))
			print """Reporte Generado {0}
Reporte Generado {1}
			""".format(fiile,pdfiile)
			return nombre
		except:
			print "No fue posible generar el reporte para los administradores"
