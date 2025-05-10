import requests
from voice_control import speak
import config


def get_weather(command):
    """Get weather information"""
    city = ("Kolkata") 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    try:
        complete_url = f"{base_url}appid={config.WEATHER_API_KEY}&q={city}"
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            temperature = main["temp"] - 273.15  
            pressure = main["pressure"]
            humidity = main["humidity"]
            weather_desc = data["weather"][0]["description"]

            speak(f"Weather in {city}: {weather_desc}")
            speak(f"Temperature: {temperature:.1f}°C")
            speak(f"Humidity: {humidity}%")
            speak(f"Atmospheric pressure: {pressure} hPa")
        else:
            speak("City not found")
    except Exception as e:
        print(f"Weather API error: {e}")
        speak("Sorry, I couldn't fetch the weather information")
