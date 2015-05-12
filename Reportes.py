#!/usr/bin/env python
from time import sleep, strftime
from os import system

class Reportes:
	pathTemplate =''
	nombre = ''
	fiile=''
	def __init__(self):
		self.pathTemplate="./salcilocos/"
	def __del__(self):
		self.pathTemplate=''
	def Reporte_Incidentes(self,pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9,pos10,pos11):
		try:
			print "Generando Reporte para el Equipo de Respuesta a incidentes"
			sleep(2)
			archivoRI = open(self.pathTemplate+"template_csirt.html","r").read()
			#print type(archivoRI)
			archivoRI = archivoRI.format(pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9,pos10,pos11)
			#print archivoRI
			# Descomentar lo de abajo
			nombre = self.pathTemplate+"ReportResponseTeam-"+strftime("%Y-%m-%d-%S")
			fiile = nombre+".html"
			pdfiile = nombre+".pdf"
			#print type(fiile)
			#Genera el reporte en HTML
			rIncidentes = open(fiile,"w")
			rIncidentes.write(archivoRI)
			rIncidentes.close()
			system("wkhtmltopdf {0} {1}".format(fiile,pdfiile))
			print """Reporte Generado {0}
Reporte Generado {1}
			""".format(fiile,pdfiile)
			return nombre
		except:
			print "No fue posible generar el reporte para el equipo de Respuesta a Incidentes"
	def Reporte_Admins(self):
		try:
			print "Generar reporte para los administradores"
			sleep(2)
			aAdmin = open(self.pathTemplate+"template_admin.html","r").read()
			adminFile = open()
			print adminFile
		except:
			print "No fue posible generar el reporte para los administradores"
