import RPi.GPIO as io
io.setwarnings(False)
io.setmode(io.BCM)

LIGHT = 3
PUMP = 2

io.setup(LIGHT, io.OUT)
io.setup(PUMP, io.OUT)

io.output(LIGHT, 1)
io.output(PUMP, 1)

while True:
    print("----------------")
    print("Closet Plants:")
    if io.input(LIGHT) == 0:
        print("(l) Light - ON")
    if io.input(LIGHT) == 1:
        print("(l) Light - off")
    if io.input(PUMP) == 0:
        print("(w) Water Pump - ON")
    if io.input(PUMP) == 1:
        print("(w) Water Pump - off")
    print("(o) Off")
    print("(x) Exit" )
    print("----------------")
    key = input('Enter command: ')

##### GROW LIGHT #####

    if key == 'l':

        io.output(LIGHT, not io.input(LIGHT))
        if io.input(LIGHT) == 1:
            print("Light Off.")
        if io.input(LIGHT) == 0:
            print("Light On.")

##### WATER PUMP #####

    if key == 'w':

        io.output(PUMP, not io.input(PUMP))
        if io.input(PUMP) == 1:
            print("Water Pump Off.")
        if io.input(PUMP) == 0:
            print("Water Pump On.")

##### OFF #####

    if key == 'o':

        io.output(LIGHT, 1)
        io.output(PUMP, 1)
        print("All Systems Off.")

##### EXIT #####

    if key == 'x':
        exit()
    if key == 'exit':
        exit()
