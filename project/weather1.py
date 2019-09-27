
import requests
from pprint import pprint

city = input('Enter your city: ')


url = 'http://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22&units=metric'.format(city)

res = requests.get(url)

data = res.json()


temp = data['main']['temp']
print(temp)

