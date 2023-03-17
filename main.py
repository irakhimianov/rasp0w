import lib
from PIL import Image, ImageDraw, ImageFont
import logging
from config import load_config
from plugins import DateTime, Weather
from display import Display
import time


def main():
    # conf = load_config()
    d = Display()
    date_time = DateTime(d.config)
    weather = Weather(d.config)

    logging.info(f'initialization')
    #
    # d.reset()
    d.init_display()
    d.clear_display()


    font = ImageFont.load_default()
    time_image = Image.new(mode='1', size=(d.height, d.width), color=255)
    time_draw = ImageDraw.Draw(time_image)

    weather_image = Image.new(mode='1', size=(d.height, d.width), color=255)
    weather_draw = ImageDraw.Draw(weather_image)
    n = 0
    while True:
        if n == 1:
            n = 0
            d.init_display()
            d.clear_display()
            time_draw.rectangle((0, 0, d.height, d.width), fill=0)
            time_draw.text((60, 50), f'{date_time.draw_data}', font=font, fill=255)
            d.draw(d.to_bytes(image=time_image.rotate(180)))
        time_draw.rectangle((0, 0, d.height, d.width), fill=0)
        time_draw.text((60, 50), f'{date_time.draw_data}', font=font, fill=255)
        d.partial_draw(d.to_bytes(image=time_image.rotate(180)))
        time.sleep(10)
        d.init_display()
        d.clear_display()
        weather_draw.rectangle((0, 0, d.height, d.width), fill=0)
        weather_draw.text((60, 50), f'{weather.draw_data}', font=font, fill=255)
        d.draw(d.to_bytes(image=weather_image.rotate(180)))
        time.sleep(20)
        n += 1

    logging.info("Clear...")


if __name__ == '__main__':
    main()
