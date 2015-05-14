#!/usr/bin/env python
#coding: utf-8
#############################################
# Ingresar los correos de los destinatarios #
# 			separados por comas 			#
#############################################
#destinatarios = ['dafteric@gmail.com','eric.castaneda.nazario@gmail.com']
destinatarios = ['dafteric@gmail.com']
#################################################################################
# Plantilla para los reportes enviados para el Equipo de Respuesta a Incidentes #
#################################################################################
template_CSIRT="""
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="./estilos.css" type="text/css" />
	</head>
	<body>
		<div class="log">
				<table class="Logos">
					<tr>
						<td rowspan=2><img src="../logos/unam_cert.jpg" width="100" height="100"></img></td>
						<td colspan=2><h1>UNAM-CERT</h1></td>
						<td rowspan=2><img src="../logos/cert_key.png" width="100" height="65"></img></td>
					</tr>
					<tr>
						<td><h5>Coordinación de Seguridad de la Información</h5></h5></td>
					</tr>
					<tr><th colspan="100%">Reporte de Phishing</th></tr>
				</table>
		</div>
		<div>
			<table>
				<tr>
					<td colspan="100%">Resumen del analisis realizado a la muestra X</td>
				</tr>
				<br />
				<tr>
					<th colspan="100%" class="Header">URL Phishing</th>
				</tr>
				<tr>
					<td colspan="100%">
						{0}
					</td>
				</tr>
				<tr id="">
					<th colspan="100%" class="Header">URL Redirección</th>
				</tr>
				<tr>
					<td colspan="100%">{1}</td>
				</tr>
				<tr>	
					<th colspan="100%" class="Header">IP phishing</th>
				</tr>
				<tr>
					<td colspan="100%">{2}</td>
				</tr>
				<tr>
					<th colspan="100%" class="Header">IP redirección</th>
				</tr>
				<tr>
					<td colspan="100%">{3}</td>
				</tr>
				<tr>
					<th colspan="100%" class="Header">URL Malware</th>
				</tr>
				<tr>
					<td colspan="100%">{4}</td>
				</tr>
				<tr>
					<th colspan="100%" class="Header">Institución Afectada</th>
				</tr>
				<tr>
					<td colspan="100%">{5}</td>
				</tr>
				<tr>
					<td colspan="100%"><h5>Remplazar "numero" por los registros cosechados de la Base de datos con la funcion format</h5></td>
				</tr>
				<tr>
					<th colspan="100%"><h1 id="cuckoo">Análsis del Cuckoo</h1></th>
				</tr>
				<tr>
					<td colspan="100%">
						En base al análisis realizado a la muestra X con el software Cuckoo, se muestra a detalle la siguiente información.
					</td>
				</tr>
				<tr>
					<td colspan="100%">MD5:::: {6}</td>
				</tr>
				<tr>
					<td colspan="100%">SHA 1:::: {7}</td>
				</tr>
				<tr>
					<td colspan="100%">Nombre del adjunto :::: {8}</td>
				</tr>
				<tr>
					<td colspan="100%">Extensión :::: {9}</td>
				</tr>
				<tr>
					<td colspan="100%">Tipo de Aplicación :::: {10}</td>
				</tr>
				<tr>
					<td colspan="100%">Archivo de Referencia :::: {11}</td>
				</tr>
				<tr>
					<td colspan="100%">Fecha de inicio :::: {12}</td>
				</tr>
				<tr>
					<td colspan="100%">Fecha de Fin :::: {13}</td>
				</tr>
				<tr>
					<td colspan="100%">Yara :::: {14}</td>
				</tr>
				<tr>
					<th colspan="100%">
						<h1 id="reglas">Reglas de Filtrado</h1>
					</th>
				</tr>
				<tr>
					<td colspan="100%">Packet Filter :::: {15}</td>
				</tr>
				<tr>
					<td colspan="100%">NetFilter :::: {16}</td>
				</tr>
				<tr>
					<td colspan="100%">Snort :::: {17}</td>
				</tr>
				<tr>
					<th colspan="100%">
						<h1 id="whois">Registros de Whois</h1>
					</th>
				</tr>
				<tr>
					<td colspan="100%"> Whois
						<ul>
							<li>
								<label>Dominio: </label><label>ASN :::: {18}</label>
							</li>
						
							<li>
								<label>Admin: </label><labelto>webmaster@example.com</label>
							</li>
						</ul>
					</td>
				</tr>
				<tr>
					<th  colspan="3" id="tor"><h1>TOR</h1></th>
					<th  colspan="3" id="proxy"><h1>Proxy</h1></th>
				</tr>
				
				<tr>
					<td  colspan="3"><h5>Datos del tor {19}</h5></td>
					<td  colspan="3"><h5>Datos del Proxy {20}</h5></td>
				</tr>
			</table>
		</div>
	</body>
</html>

"""
#tsoh="MTAuMTAuNjAuMTI4Cg=="
tsoh="MTI3LjAuMC4xCg=="
resu="cmVwb3J0ZWFkb3IK"
dwp="cmVwb3J0ZWFkb3IK"
#emanbd="cHJ1ZWJhcwo="
emanbd="bXlkYgo="
#emanbd="bXlkYjIK"
########################################################
# Plantilla de Reportes enviados a los administradores #
########################################################
template_Admin="""
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="./estilos.css" type="text/css" />
	</head>
	<body>
		<div class="log">
				<table class="Logos">
					<tr>
						<td rowspan=2><img src="../logos/unam_cert.jpg" width="100" height="100"></img></td>
						<td colspan=2><h1>UNAM-CERT</h1></td>
						<td rowspan=2><img src="../logos/cert_key.png" width="100" height="65"></img></td>
					</tr>
					<tr>
						<td><h5>Coordinación de Seguridad de la Información</h5></h5></td>
					</tr>
					<tr><th colspan="100%">Reporte de Pishing</th></tr>
				</table>
		</div>
		<div>
			<table>
				<tr>
					<td colspan="100%">Resumen del analisis realizado a la muestra X</td>
				</tr>
				<br />
				<tr id="summary">
					<th>Pishing</th>
					<th>Redirección</th>
					<th>IP phishing</th>
					<th>IP redirección</th>
					<th>IP redirección</th>
					<th>Malware URL</th>
				</tr>
				<tr>
					<td>Select * from piching</td>
					<td>Select * from redireccion</td>
					<td>Select * from ipPiching</td>
					<td>Select * from ipRedireccion</td>
					<td>select * from date</td>
					<td>select * from malware</td>
				</tr>
				<tr>
					<td>{0}</td>
					<td>{1}</td>
					<td>{2}</td>
					<td>{3}</td>
					<td>{4}</td>
					<td>{5}</td>
				</tr>
				<tr>
					<td colspan="100%"><h5>Remplazar {numero} por los registros cosechados de la Base de datos con la funcion format</h5></td>
				</tr>
				<tr>
					<td colspan="100%">{6}</td>
				</tr>
				<tr>
					<th colspan="100%">
						<h1 id="reglas">Reglas de Filtrado</h1>
					</th>
				</tr>
				<tr>
					<td colspan="100%">Aqui van las reglas del SNORT</td>
				</tr>
				<tr>
					<td colspan="100%">{8}</td>
				</tr>
				<tr>
					<th colspan="100%">
						<h1 id="whois">Otros Datos</h1>
					</th>
				</tr>
			</table>
		</div>
		<ul>
			{0}
		</ul>
	</body>
</html>
"""

asunto= "Reporte UNAM-CERT [TICKET] Sitio fraudulento en su red (Phishing Scam)"
cuerpo= """
Buen día
En UNAM-CERT hemos recibido y confirmado reportes sobre un sitio web fraudulento, localizado en su red:

URL: {0}
IP: {1}

Este sitio es utilizado para perjudicar a los usuarios legítimos de {2}. Los usuarios podrán comprometer sus datos y luego podrán ser defraudados
por favor, tome las medidas necesarias para dar de baja el sitio. UNAM-CERT le agradecerá cualquier información adicional que nos pueda proporcionar sobre este incidente de seguridad.

La base de datos de WHOIS nos mostró sus datos como contacto para este segmento de red. Si usted no es la persona indicada para recibir este tipo de mensajes,
por favor háganoslo saber o redirija el mensaje a la persona adecuada.

De antemano gracias por su atención a este reporte

--
UNAM-CERT
Equipo de Respuesta a Incidentes de Seguridad en Cómputo.
Coordinación de Seguridad de la Información, DGTIC, UNAM
email: incidentes@eguridad.unam.mx
Circuito Exterior, C.U.    Tel. +52 (55) 5622-81-69
Del. Coyoacán    http://www.seguridad.unam.mx
04510 México D.F.
"""




