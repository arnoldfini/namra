from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit
import requests

'''

Get weather via Yahoo API

'''

def main():
    print(getWeather())
    #getClimate()

def getWeather():

    url = 'http://ipinfo.io/json'
    data = requests.get(url).json()

    location = data['city']
    
    data = YahooWeather(APP_ID="t7nKZlaO",
                         api_key="dj0yJmk9ckw2ZDRVbUJld1ZxJmQ9WVdrOWREZHVTMXBzWVU4bWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTM0",
                         api_secret="4ffec13cee644a101daa4efacb63d7cb0e63497d")

    data.get_yahoo_weather_by_city(location, Unit.celsius)

    temp = data.condition.temperature

    return temp, location

def getClimate():

    koppenclimate = [
        Af,
        Am,
        As,
        Aw,
        BSh,
        BSk,
        BWh,
        BWk,
        Cfa,
        Cfb,
        Cfc,
        Csa,
        Csb,
        Csc,
        Cwa,
        Cwb,
        Cwc,
        Dfa,
        Dfb,
        Dfc,
        Dfd,
        Dsa,
        Dsb,
        Dsc,
        Dwa,
        Dwb,
        Dwc,
        Dwd,
        EF,
        ET
    ]

    temp, location = getWeather()

    url = 'https://www.mindat.org/climate.php'
    print(requests.get(url).content)
    data = requests.get(url).json()
 #   logger.info(type(data))
 #   requests.post(url, data=json.dumps(data))
  #  data.encoding = 'utf-8'

  #  print(data.text)
main()