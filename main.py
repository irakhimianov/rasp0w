from lib.v3 import epd2in13_V3
import time
from PIL import Image, ImageDraw, ImageFont
import os
import logging


def main():
    logging.info("epd2in13_V3")

    epd = epd2in13_V3.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)

    # Drawing on the image
    font24 = ImageFont.truetype(size=24)

    logging.info("4.show time...")
    time_image = Image.new(mode='1', size=(epd.height, epd.width), color=255)
    time_draw = ImageDraw.Draw(time_image)

    epd.displayPartBaseImage(epd.getbuffer(time_image))
    while True:
        time_draw.rectangle((120, 80, 220, 105), fill=255)
        time_draw.text((120, 80), f'{time:%H:%M:%S}', font=font24, fill=0)
        epd.displayPartial(epd.getbuffer(time_image))

    logging.info("Clear...")
    epd.init()
    epd.Clear(0xFF)

    logging.info("Goto Sleep...")
    epd.sleep()


if __name__ == '__main__':
    main()
