import requests
from datetime import datetime
from pytz import timezone

from .base import Base
from config import Config


class Weather(Base):
    _last_update = None
    _last_full_data = None

    def __init__(self, config: Config):
        self.config = config
        self.timezone = config.date_time.timezone
        self.weather_config = config.weather
        self.api_token = config.weather.api_token
        self.weather_update_time = config.weather.update_time
        self.latitude = config.weather.latitude
        self.longitude = config.weather.longitude
        self.temperature_scale = config.weather.temperature_scale
        self.last_update = datetime.now()

    def _get_full_data(self):
        now = datetime.now(tz=timezone(self.timezone))
        units = 'metric'
        if self.temperature_scale.lower() == 'fahrenheit':
            units = 'imperial'
        url = f'https://api.openweathermap.org/data/2.5/onecall?'
        params = {
            'lat': self.latitude,
            'lon': self.longitude,
            'appid': self.api_token,
            'units': units,
        }
        if self._last_update is None:
            self._last_update = now
        if self._last_full_data is None or (now - self._last_update).seconds >= self.weather_update_time:
            response = requests.get(url=url, params=params).json()
            self._last_full_data = response
            self._last_update = now
        return self._last_full_data

    @property
    def current(self):
        data = self._get_full_data()['current']
        result = {
            'temp': data['temp'],
            'pressure': data['pressure'],
            'wind_speed': data['wind_speed'],
            'clouds': data['clouds'],
            'weather': data['weather'],
        }
        return result

    @property
    def draw_data(self):
        current_weather = self.current
        text = f'{current_weather["temp"]} {self.temperature_scale[0].upper()} ' \
               f'{current_weather["pressure"]}mmHg ' \
               f'{current_weather["wind_speed"]}m/s ' \
               f'{current_weather["clouds"]}%'
        return text
