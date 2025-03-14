import requests
import json
import re

def get_weather(city):
    api_key = "e4f243b7377afef526b662bd3850d97e"  # Replace with your valid OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)  # Corrected parameter name
        response.raise_for_status()
        data = response.json()

        if "weather" in data and "main" in data:
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
        else:
            return "Error: Invalid city name or data unavailable."

    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch weather data. {e}"

def save_to_file(city):
    with open("weather_history.txt", "a") as file:
        file.write(city + "\n")

def display_search():
    try:
        with open("weather_history.txt", "r") as file:
            searches = file.readlines()
            searches = [re.sub(r'\n', '', city) for city in searches]  # Removing newlines
            return "Recent Searches: " + ", ".join(searches)
    except FileNotFoundError:
        return "No recent searches found."

def main():
    city = input("Enter the city name: ")
    print(get_weather(city))
    print(display_search())

if __name__ == '__main__':
    main()