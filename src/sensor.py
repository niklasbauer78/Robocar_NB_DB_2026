import time

from gpiozero import LineSensor


def init():
    global SensorLeft
    global SensorMiddle
    global SensorRight

    SensorLeft = LineSensor(14)
    SensorMiddle = LineSensor(15)
    SensorRight = LineSensor(23)


def test():
    init()
    timer = 0
    while timer < 10:
        if SensorLeft.value == 1:
            print("Left Sensor: Line detected")
        else:
            print("Left Sensor: No line detected")

        if SensorMiddle.value == 1:
            print("Middle Sensor: Line detected")
        else:
            print("Middle Sensor: No line detected")

        if SensorRight.value == 1:
            print("Right Sensor: Line detected")
        else:
            print("Right Sensor: No line detected")
        time.sleep(1)
        timer = timer + 1


# test()     ##remove "#" to test the sensor.py program
