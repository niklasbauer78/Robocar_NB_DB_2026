from gpiozero import LineSensor


def sensor_global():
    global sensorL
    global sensorM
    global sensorR

    sensorL = LineSensor(14)
    sensorM = LineSensor(15)
    sensorR = LineSensor(23)
