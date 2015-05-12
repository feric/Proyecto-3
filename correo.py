#!/usr/bin/env python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import os
import time
class Correos():
	def parametros(self, to, fro, subject, text,files=[],server="10.10.60.129"):
		datos = to, fro, subject, text,files,server
		for i in datos:
			print type(i)

	def sendMail(self, to, fro, subject, text,files=[],server="10.10.60.129"):
		#assert type(to)==list
		#assert type(files)==list
		msg = MIMEMultipart()
		msg['From'] = fro
		msg['To'] = COMMASPACE.join(to)
		msg['Date'] = formatdate(localtime=True)
		msg['Subject'] = subject

		msg.attach( MIMEText(text) )

		for file in files:
			part = MIMEBase('application', "octet-stream")
			part.set_payload( open(file,"rb").read() )
			Encoders.encode_base64(part)
			part.add_header('Content-Disposition', 'attachment; filename="%s"'
						   % os.path.basename(file))
			msg.attach(part)
		smtp = smtplib.SMTP(server)
		smtp.sendmail(fro, to, msg.as_string())
		smtp.close()
		print """
	====================================================
	==== Enviando Correo con los reportes Generados ====
	====    to: eric.castaneda.nazario@gmail.com    ====
	====================================================
	"""
		time.sleep(2)
#enviar = Correos()
#enviar.sendMail(['eric.castaneda.nazario@gmail.com'],'lalo <root@localhost.com>','Reporte de Phishing','Reporte de Phishing generado Hoy :)',['file1.html','file2.pdf'])
#sendMail(['eric@ServerCorreo.com'],'iPhishing <root@localhost.com>','Reporte de Phishing','Reporte de Phishing generado Hoy :)',['./salcilocos/ReportResponseTeam-2015-05-12-17.html','./salcilocos/ReportResponseTeam-2015-05-12-17.pdf'])
