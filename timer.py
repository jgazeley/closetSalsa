import RPi.GPIO as io
import time
import datetime

LIGHT = 3

io.setmode(io.BCM)
io.setwarnings(False)
io.setup(LIGHT, io.OUT)

while True:
    currTime = datetime.datetime.now()

#LIGHTS ON @ 6 AM
    if (currTime.hour >= 6 and
        currTime.hour < 23 and
        io.input(LIGHT) != 0):

        io.output(LIGHT, 0)

#LIGHTS OFF @ 8 PM
    elif (currTime.hour >= 23 and
        io.input(LIGHT) != 1):

        io.output(LIGHT, 1)
