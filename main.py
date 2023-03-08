import lib
from PIL import Image, ImageDraw, ImageFont
import logging
from config import load_config
from plugins import DateTime, Weather


# def main():
#     logging.info("epd2in13_V3")
#
#     epd = epd2in13_V3.EPD()
#     logging.info("init and Clear")
#     epd.init()
#     epd.Clear(0xFF)
#
#     # Drawing on the image
#     # font24 = ImageFont.truetype(size=24)
#     font = ImageFont.load_default()
#
#     logging.info("4.show time...")
#     time_image = Image.new(mode='1', size=(epd.height, epd.width), color=255)
#     time_draw = ImageDraw.Draw(time_image)
#
#     epd.displayPartBaseImage(epd.getbuffer(time_image))
#     while True:
#         time_draw.rectangle((120, 80, 220, 105), fill=255)
#         time_draw.text((120, 80), f'{time:%H:%M:%S}', font=font24, fill=0)
#         time_image.rotate(180)
#         epd.displayPartial(epd.getbuffer(time_image))
#
#     logging.info("Clear...")
#     epd.init()
#     epd.Clear(0xFF)
#
#     logging.info("Goto Sleep...")
#     epd.sleep()


def main():
    conf = load_config()
    date_time = DateTime(conf)
    weather = Weather(conf)

    logging.info(f'initialization {conf.display_type}')
    epd = lib.get_display_driver('epd2in13_V3')
    epd.init()
    epd.clear()
    font = ImageFont.load_default()
    time_image = Image.new(mode='1', size=(epd.height, epd.width), color=255)
    time_image = time_image.rotate(180 * conf.is_upside_down)
    time_draw = ImageDraw.Draw(time_image)
    epd.displayPartBaseImage(epd.getbuffer(time_image))
    while True:
        time_draw.rectangle((120, 80, 220, 105), fill=255)
        time_draw.text((120, 80), f'{date_time.draw_data}', font=font, fill=0)
        # time_image.rotate(180)
        epd.displayPartial(epd.getbuffer(time_image))

    logging.info("Clear...")
    epd.init()
    epd.Clear(0xFF)


if __name__ == '__main__':
    main()
