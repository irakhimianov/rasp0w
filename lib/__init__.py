from .lcdhat import epd as lcdhat_epd
from .lcdhat144 import epd as lcdhat144_epd
from .oledhat import epd as oledhat_epd
from .v1 import epd2in13, epd2in13bc, epd2in13bcFAST
from .v2 import waveshare
from .v3 import epd2in13_V3
from .v27inch import epd2in7
from .v29inch import epd2in9
from .v154inch import epd1in54b
from .v213d import epd2in13d


def get_display_driver(display_type):
    match display_type:
        case 'lcd' | 'lcdhat':
            return lcdhat_epd.EPD()
        case 'lcd144' | 'lcdhat144':
            return lcdhat144_epd.EPD()
        case 'oledhat' | 'oled':
            return oledhat_epd.EPD()
        case 'v1' | 'waveshare1' | 'epd2in13':
            return epd2in13.EPD()
        case 'v1_color_fast' | 'waveshare1_color_fast' | 'epd2in13bcFAST':
            return epd2in13bcFAST.EPD()
        case 'v1_color' | 'waveshare1_color' | 'epd2in13bc':
            return epd2in13bc.EPD()
        case 'v2' | 'waveshare2':
            return waveshare.EPD()
        case 'v3' | 'waveshare3' | 'epd2in13_V3':
            return epd2in13_V3.EPD()
        case 'v27' | 'v27inch' | 'epd2in7':
            return epd2in7.EPD()
        case 'v29' | 'v29inch' | 'epd2in9':
            return epd2in9.EPD()
        case 'v154' | 'v154inch' | 'epd1in54b':
            return epd1in54b.EPD()
        case 'v213' | 'v213d' | 'epd2in13d':
            return epd2in13d.EPD()
        case _:
            raise SyntaxError('display type not found')
