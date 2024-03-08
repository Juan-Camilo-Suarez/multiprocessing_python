from multiprocessing import Pool
import requests


def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

    weather_json = requests.get(url=url, params=params).json()
    return f'{city}: {weather_json["weather"][0]["main"]}'


if __name__ == "__main__":
    cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
              'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']
    with Pool() as pool:
        result = pool.imap(get_weather, cities)
        for city in result:
            print(city)
