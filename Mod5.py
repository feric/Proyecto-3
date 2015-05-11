#!/usr/bin/env python
import time
import psycopg2
import datas
import base64

# Access to Database
host=base64.b64decode(datas.tsoh)[:-1]
user=base64.b64decode(datas.resu)[:-1]
pwd=base64.b64decode(datas.dwp)[:-1]
dbname=base64.b64decode(datas.emanbd)[:-1]

class Postgress:
	def __init__(self):
		try:
			credentials ="dbname={0} user={1} host={2} password={3}".format(dbname,user,host,pwd)
			print credentials
			self.conn=psycopg2.connect(credentials)
			print "Successfull"
			#self.conn.close()
		except:
			print "Sorry, unable to connect to PostgreSQL server\ncheck your configurations"
	def __del__(self):
		try:
			self.conn.close()
		except:
			print "Sorry, unable to disconnect from database"
	def version(self):
		try:
			cursor = self.conn.cursor()
			cursor.execute("select version()")
			reporte = open("salcilocos/template.html","r")
			reporte
			vers = cursor.fetchall()
			print vers
		except:
			print "Sorry, unable to connect execute sentence"
	def Cosecha(self):
		#Metodo para la recoleccion de datos que necesita el reporte
		try:
			cursor = self.conn.cursor()
			cursor.execute("select * from tabla")
			datos_pishing = cursor.fetchall()
			#Ahora se tiene que acomodar los datos en el reporte HTML
			print type(datos_pishing)
			for id in range(len(datos_pishing)):
				for e in datos_pishing[id]:
					print e
		except:
			print "Sorry, An error has ocurred in Cosecha"
if __name__ =="__main__":
	#print host
	repe = Postgress()
	repe.Cosecha()
