
import requests

#to dispay temperature by city
def by_city():

    city = input('Enter your city: ')
    url = 'http://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22&units=metric'.format(city)
    res = requests.get(url)
    data = res.json()
    show_data(data)

#to display temperature by location
def by_location():
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    location = data['loc'].split(',')
    lattitude,longitude = location[0],location[1]
    url = 'https://openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=b6907d289e10d714a6e88b30761fae22&units=metric'.format(lattitude,longitude)
    res = requests.get(url)
    data = res.json()
    show_data(data)

#to display 
def show_data(data):
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    lattitude = data['coord']['lat']
    longitude  = data['coord']['lon']

    description = data['weather'][0]['description']

    print('Temperature: {} C'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('lattitude: {} N'.format(lattitude))
    print('longitude: {} E'.format(longitude))
    print('description: {}'.format(description))

def main():
    print('1.Get data by city')
    print('2.Get data by location')
    print('3.Exit')

    choice = input('Enter your choice : ')

    if (choice == '1'):
        by_city()
    elif(choice == '2'):
        by_location()
    else:
        return



if __name__ == "__main__":
     main()
