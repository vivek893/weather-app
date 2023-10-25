# create a weather Api. That determine the temperture of City .
import requests

API_KEY = '2c3cc91cde7362d072ddab63b3282ce5'
CITY_NAME = 'Hyderabad'
API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric'

response = requests.get(API_URL)

if response.status_code == 200:
    data = response.json()
    city_name = data['name']
    temperature = data['main']['temp']
    weather_report = data['weather'][0]['description']

    print(f"{city_name}\nTemperature: {temperature}°C\nWeather Report: {weather_report}")
else:
    print("Error:", response.status_code)
