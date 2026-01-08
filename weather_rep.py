import requests


OPENWEATHER_APP_ID = "8d6ad4369535ebda8327482c712d92a1"


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"
#print(f"{get_weather_report}")
##As per the OpenWeatherMap API, we need to make a GET request on the above-mentioned URL with the city name. We'll get a JSON response as:
#"""{
#    "coord": {
#        "lon": 85,
#        "lat": 24.7833
#    },
#    "weather": [
#        {
#            "id": 721,
#            "main": "Haze",
#            "description": "haze",
#            "icon": "50d"
#        }
#    ],
#    "base": "stations",
#    "main": {
#        "temp": 26.95,
#        "feels_like": 26.64,
#        "temp_min": 26.95,
#        "temp_max": 26.95,
#        "pressure": 1011,
#        "humidity": 36
#    },
#    "visibility": 3000,
#    "wind": {
#        "speed": 2.57,
#        "deg": 310
#    },
#    "clouds": {
#        "all": 57
#    },
#    "dt": 1637227634,
#    "sys": {
#        "type": 1,
#        "id": 9115,
#        "country": "IN",
#        "sunrise": 1637195904,
#        "sunset": 1637235130
#    },
#    "timezone": 19800,
#    "id": 1271439,
#    "name": "Gaya",
#    "cod": 200
#}
#"""