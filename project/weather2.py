import requests
from pprint import pprint
res = requests.get('https://ipinfo.io/')

data = res.json()

location = data['loc'].split(',')
lattitude,longitude = location[0],location[1]

url = 'https://openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=b6907d289e10d714a6e88b30761fae22&units=metric'.format(lattitude,longitude)

res = requests.get(url)

data = res.json()

pprint(data)