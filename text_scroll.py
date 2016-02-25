#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
PURPLE = (102,0,204)
PINK = (255,0,255)
ORANGE = (255,128,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
CYAN = (0,255,255)

sense.show_message("I love you Chantal!", text_colour=WHITE, back_colour=PINK, scroll_speed=0.05)

sense.clear()

