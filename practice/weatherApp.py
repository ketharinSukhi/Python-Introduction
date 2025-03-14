import requests
import json
import re

def get_weather(city):
    api_key ="Mymensingh"
    base_url ="http://api.openweathermap.org/data/2.5/weather"
    weather ={"q": city, "appid": api_key, "units": "metric"}
    try:
        response = requests.get(base_url, weather=weather)
        response.raise_for_status()
        data = response.json()

        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        city_name = data["name"]
        country = data["sys"]["country"]

def save_to_file(city):


def display_search():

def main():
   city = input ("Enter the city name: ")
   get_weather(city)

if __name__ == '__main__':
    main()
    