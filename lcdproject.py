import math
import time

import Adafruit_CharLCD as LCD

rs        = 26  
en        = 19
d4        = 13
d5        = 21
d6        = 20
d7        = 16

columns = 16
rows    = 2

message = "Hello, /n world!"

lcd = LCD.Adafruit_CharLCD(rs, en, d4, d5, d6, d7, columns, rows)

lcd.message(mesasage)
