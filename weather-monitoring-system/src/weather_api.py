import requests
import json

API_KEY = "your_openweathermap_api_key"

def fetch_weather_data():
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    url = "http://api.openweathermap.org/data/2.5/weather"
    weather_data = []
    for city in cities:
        response = requests.get(url, params={'q': city, 'appid': API_KEY})
        data = response.json()
        weather_data.append(data)
    return weather_data
