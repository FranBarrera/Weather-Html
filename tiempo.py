# -*- coding: utf-8 -*-
import json
import os
import requests
from jinja2 import Template
html = open('index.html','w')

def direccion(orientacion):
#	if orientacion > 342,5 < 22,5:
#		return 'N'
#	if orientacion > 22,5 and orientacion < 90:
#		return 'NE'
	if orientacion == 90:
		return 'E'
	if orientacion > 90 and orientacion < 180:
		return 'SE'
	if orientacion == 180:
		return 'S'
	if orientacion > 180 and orientacion < 270:
		return 'SO'
	if orientacion == 270:
		return 'O'
	if orientacion > 270:
		return 'NO'

print ''

provincias = {'1':'Almería','2':'Cádiz','3':'Córdoba','4':'Granada','5':'Huelva','6':'Jaén','7':'Málaga','8':'Sevilla'}

for numero in provincias:
	print provincias[numero]

print ''

respuesta = raw_input('Elige una Provincia para ver el tiempo: ')

os.system('clear')

print 'El tiempo para la Provincia de:',provincias[respuesta]

print''

tiempo = requests.get('http://api.openweathermap.org/data/2.5/weather', params={'q':'%s,spain' % provincias[respuesta]})
jtemp = json.loads(tiempo.text)
temp = jtemp['main']['temp']
grados = round(temp - 273,2)
speed = round(jtemp['wind']['speed']*1.609,1)
orientacion = jtemp['wind']['deg']
orientacion = direccion(orientacion)

print 'La temperatura actual de %s es de %s grados centígrados' % (provincias[respuesta],grados)

print speed
print orientacion

html.write()

provincia = Template('hello {{ name }}!')
print template.render(name=provincias[numero])

html.close()