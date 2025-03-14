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

        weather_info = (f"Weather in {city_name}, {country}: {weather_desc}\n"
                        f"Temperature: {temp}°C\n"
                        f"Humidity: {humidity}%")
        save_to_file(city)  
        return weather_info
    
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch weather data. {e}"
    except KeyError:
        return "Error: Invalid city name or data unavailable."


def save_to_file(city):
    with open("weather_history.txt", "a") as file:
        file.write(city + "\n")


def display_search():

def main():
   city = input ("Enter the city name: ")
   print(get_weather(city))
   print(display_search())


if __name__ == '__main__':
    main()
    