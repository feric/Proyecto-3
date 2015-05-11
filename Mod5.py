#!/usr/bin/env python
import time
from Reportes import Reportes
from PostgreSQL import Postgress

dPishing = ''

def main():
	#Se conecta a la base de datos
	repe = Postgress()
	#Obtiene los registros de la tabla de los datos phishing
	dPishing = repe.Get_dPhishing()
	#print dPishing
	generar = Reportes()
	generar.Reporte_Incidentes(dPishing)

if __name__ =="__main__":
	main()
