#!/usr/bin/python
#-*- coding: utf-8 -*-
import os

contenido = """
<!DOCTYPE html>
<html>
<meta charset="utf-8"/>
<body>
    <h1>Saludos Feric!</h1>
    <h3>Reporte de Malware</h3>
    <p>Contenido del primer párrafo. La banda del champy está bien loca, cámaras mijo ponte bien chingón
	o no te hagas maje!</p>
	<p>El partido del descenso está muy bueno, hasta el momento el puebla está empatando con el santos y los leones negros
	están ganandole al cruz azul. Con éste marcador descienden los leones negros.</p>
    </body>
</html>
"""

archivo = open('reporte_web.html','w')
archivo.write(contenido)
archivo.close()

#wkhtmltopdf reporte_web.html archivo.pdf
os.system("wkhtmltopdf reporte_web.html archivo.pdf")
