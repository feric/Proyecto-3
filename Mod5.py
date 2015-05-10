#!/usr/bin/env python
import time
import psycopg2
import Hola
# Access to Database

host="10.10.60.128"
user="reporteador"
pwd="reporteador"
dbname="pruebas"
class Postgress:
	conn = ""
	def __init__(self):
		try:
			credentials ="dbname={0} user={1} host={2} password={3}".format(dbname,user,host,pwd)
			self.conn=psycopg2.connect(credentials)
			print "Successfull"
			#self.conn.close()
		except:
			print "Sorry, unable to connect to PostgreSQL server\ncheck your configurations"
	def version(self):
		try:
			cursor = self.conn.cursor()
			print "Version"
			cursor.execute("select * from tabla")
			vers = cursor.fetchall()
			print vers
		except:
			print "Sorry, unable to connect execute sentence"
	def __del__(self):
		try:
			self.conn.close()
		except:
			print "Sorry, unable to disconnect from database"



if __name__ =="__main__":
	repe = Postgress()
	repe.version()
	Hola.alo()







