#!/usr/bin/env python

import psycopg2
import psycopg2.extras
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
			#print credentials[:-20]
			self.conn=psycopg2.connect(credentials)
			print "Successfull"
		except:
			print "Sorry, unable to connect to PostgreSQL server\ncheck your configurations"
	def __del__(self):
		try:
			self.conn.close()
		except:
			print "Sorry, unable to disconnect from database"
	###################################
	# Metodo para la cosecha de datos #	
	###################################
	def Get_dPhishing(self):
		try:
			queryEnferma = """
			select u.url, u.url, df.ip, df.ip, a.nombre_archivo, i.nombre,
			a.md5, a.sha1, a.nombre_archivo, a.extension, a.aplicacion, a.referencia, a.fecha_inicio, a.fecha_fin, a.yara,
			df.pf, df.nf, df.snort,
			df.asn, df.tor, df.proxy
			 from instituciones as i
			  join correos as c
			  on i.id_institucion = c.id_institucion
			   join adjuntos as a
			   on c.adjuntos_md5 = a.md5
				join urls as u
				on c.id_url = u.id_url
				 join datos_phishing as df
				 on u.id_url = df.id_url
				  where df.id_datos = 1;
			"""
			cursor = self.conn.cursor()
			#cursor.execute("select * from datos_phishing")
			cursor.execute(queryEnferma)
			datos_phishing = cursor.fetchall()
			return datos_phishing
		except:
			print "Sorry, An error has ocurred in Cosecha"
