from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit
import requests

'''

Get weather via Yahoo API

'''

def getWeather():

    url = 'http://ipinfo.io/json'
    data = requests.get(url).json()

    location = data['city']

    data = YahooWeather(APP_ID="t7nKZlaO",
                         api_key="dj0yJmk9ckw2ZDRVbUJld1ZxJmQ9WVdrOWREZHVTMXBzWVU4bWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTM0",
                         api_secret="4ffec13cee644a101daa4efacb63d7cb0e63497d")

    data.get_yahoo_weather_by_city(location, Unit.celsius)

    temp = data.condition.temperature

    return temp


