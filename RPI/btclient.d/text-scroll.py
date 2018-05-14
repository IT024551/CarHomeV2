#!/usr/bin/python
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.set_rotation(180)
blue = (255, 0, 255)
sense.show_message("Welcome Home ***", text_colour=blue)
sense.show_message("Welcome Home", text_colour=blue)
sleep(1)
sense.clear(blue)

