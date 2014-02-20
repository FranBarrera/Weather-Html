# -*- coding: utf-8 -*-
import json
import os
import requests
from jinja2 import Template
import webbrowser
f = open('template.html','r')
web = open('web.html','w')

def direccion(orientacion):
	if (orientacion > 337.5 and orientacion < 360) or (orientacion  > 0 and orientacion < 22.5):
		return 'N'
	if orientacion > 22.5 and orientacion < 67.5:
		return 'NE'
	if orientacion > 67.5 and orientacion < 112.5:
		return 'E'
	if orientacion > 112.5 and orientacion < 157.5:
		return 'SE'
	if orientacion > 157.5 and orientacion < 202.5:
		return 'S'
	if orientacion > 202.5 and orientacion < 245.5:
		return 'SO'
	if orientacion > 245.5 and orientacion < 292.5:
		return 'O'
	if orientacion > 292.5 and orientacion < 337.5:
		return 'NO'

print ''

html =''

for linea in f:
	html += linea

provincias = ['Almeria','Cadiz','Cordoba','Granada','Huelva','Jaen','Malaga','Sevilla']

for provincia in provincias:
	tiempo = requests.get('http://api.openweathermap.org/data/2.5/weather', params={'q':'%s,spain' % provincia})
	jtemp = json.loads(tiempo.text)
	#temp = jtemp['main']['temp']
	speed = round(jtemp['wind']['speed']*1.609,1)
	#orientacion = jtemp['wind']['deg']
	#orientacion = direccion(orientacion)
	temp_min = round(jtemp['main']['temp_min']-273,2)
	temp_max = round(jtemp['main']['temp_max']-273,2)
	mitemplate = Template(html)
	mitemplate = mitemplate.render(provincia=provincia,temp_min=temp_min,temp_max=temp_max,viento=speed)

web.write(mitemplate)



webbrowser.open('web.html')
