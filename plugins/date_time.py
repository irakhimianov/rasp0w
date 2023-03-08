from datetime import datetime
from pytz import timezone

from config import Config
from .base import Base


class DateTime(Base):
    def __init__(self, config: Config):
        self.config = config
        self.time_config = config.date_time
        self.timezone = config.date_time.timezone
        self.time_format = config.date_time.time_format
        self.date_format = config.date_time.date_format

    def _get_full_data(self):
        now = datetime.now(tz=timezone(self.timezone))
        time = now.strftime('%H:%M')
        if self.time_format == '12h':
            time = now.strftime('%I:%M')
        date = now.strftime(self.date_format)
        day = now.strftime('%A')
        data = {
            'time': time,
            'day': day,
            'date': date,
        }
        return data

    @property
    def current(self):
        return self._get_full_data()

    @property
    def draw_data(self):
        current_datetime = self.current
        text = f'{current_datetime["time"]} ' \
               f'{current_datetime["day"]} ' \
               f'{current_datetime["date"]}'
        return text
