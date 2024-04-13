import math
import time

import Adafruit_CharLCD as LCD

rs        = 27  
en        = 22
d4        = 25
d5        = 24
d6        = 23
d7        = 18

columns = 16
rows    = 2

message = "Hello, /n world!"

lcd = LCD.Adafruit_CharLCD(rs, en, d4, d5, d6, d7, columns, rows)

lcd.message(mesasage)
