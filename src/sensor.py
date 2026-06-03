import time

from gpiozero import LineSensor


def sensor_global():
    global sensorL
    global sensorM
    global sensorR

    sensorL = LineSensor(14)
    sensorM = LineSensor(15)
    sensorR = LineSensor(23)


def sensor_test():
    sensor_global()
    index = 0
    while index < 10:
        if sensorL.value == 1:
            print("Left Sensor: Line detected")
        else:
            print("Left Sensor: No line detected")

        if sensorM.value == 1:
            print("Middle Sensor: Line detected")
        else:
            print("Middle Sensor: No line detected")

        if sensorR.value == 1:
            print("Right Sensor: Line detected")
        else:
            print("Right Sensor: No line detected")
        time.sleep(1)
        index = index + 1


# sensor_test()     ##remove "#" to test the sensor.py program
