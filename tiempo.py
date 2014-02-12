# -*- coding: utf-8 -*-
import json
import os
import requests

print 'Aplicacion Provincias'

print ''

provincias = {'1':'Almería','2':'Cádiz','3':'Córdoba','4':'Granada','5':'Huelva','6':'Jaén','7':'Málaga','8':'Sevilla'}

print '''
1. Almería
2. Cádiz
3. Córdoba
4. Granada
5. Huelva
6. Jaén
7. Málaga
8. Sevilla
'''

print ''

respuesta = raw_input('Elige una Provincia para ver el tiempo: ')

os.system('clear')

print 'El tiempo para la Provincia de:',provincias[respuesta]

print''

tiempo = requests.get('http://api.openweathermap.org/data/2.5/weather', params={'q':'%s,spain' % provincias[respuesta]})
jtemp = json.loads(tiempo.text)
temp = jtemp['main']['temp']
grados = round(temp - 273,2)

print 'La temperatura actual de %s es de %s grados centígrados' % (provincias[respuesta],grados)
