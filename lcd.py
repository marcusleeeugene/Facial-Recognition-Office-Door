import lcddriver
from time import *

lcd = lcddriver.lcd()
lcd.lcd_backlight("On")
lcd.lcd_clear()
lcd.lcd_display_string("Su!", 1)

lcd.lcd_display_string("Welcome, " + id + "!",1)
