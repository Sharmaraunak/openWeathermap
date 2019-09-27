import requests
from pprint import pprint
res = requests.get('https://ipinfo.io/')

data = res.json()

location = data['loc'].split(',')
lattitude,longitude = location[0],location[1]
print(lattitude,longitude)

