#!/usr/bin/env python
class Reportes:
	csirt = False
	def __init__(self,csirt=False):
		if(csirt):
			print "Generar Reporte para el Equipo de Respuesta a incidentes"
		else:
			print "Generar reporte para los administradores"
	def Reporte_Incidentes(self):
		try:
			
		except:
			print "No fue posible generar el reporte para el equipo de Respjuesta a Incidentes"
	def Reporte_Admins(self):
		try:
			
		except:
			print "No fue posible generar el reporte para los administradores"
