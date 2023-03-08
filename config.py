import os
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class WeatherConfig:
    api_token: str
    update_time: int
    latitude: float
    longitude: float
    temperature_scale: str


@dataclass
class DateTimeConfig:
    timezone: str
    time_format: str
    date_format: str


@dataclass
class Config:
    display_type: str
    is_upside_down: bool
    date_time: DateTimeConfig
    weather: WeatherConfig


def load_config() -> Config:
    load_dotenv()
    return Config(
        display_type=os.getenv('DISPLAY_TYPE'),
        is_upside_down=bool(os.getenv('UPSIDE_DOWN')),
        date_time=DateTimeConfig(
            timezone=os.getenv('TIMEZONE'),
            time_format=os.getenv('TIMEFORMAT'),
            date_format=os.getenv('DATEFORMAT'),
        ),
        weather=WeatherConfig(
            api_token=os.getenv('API_TOKEN'),
            update_time=int(os.getenv('UPDATE_TIME')),
            latitude=float(os.getenv('LATITUDE')),
            longitude=float(os.getenv('LONGITUDE')),
            temperature_scale=os.getenv('TEMPERATURE'),
        ),
    )
