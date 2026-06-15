import json
import os
import time

import motor
import sensor

# Get the directory where the config script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, "config.json")

# open the config script to use it as a dictionary
with open(config_path, "r") as file:
    config = json.load(file)


def DriveFromSensors():
    if sensor.SensorLeft.value == config["Sensor over black"]:
        motor.front_left(config["Corner Speed inner wheels"])
        motor.front_right(config["Corner Speed outer wheels"])
        motor.rear_left(config["Corner Speed inner wheels"])
        motor.rear_right(config["Corner Speed outer wheels"])
    elif sensor.SensorMiddle.value == config["Sensor over black"]:
        motor.front_left(config["Speed forward"])
        motor.front_right(config["Speed forward"])
        motor.rear_left(config["Speed forward"])
        motor.rear_right(config["Speed forward"])
    elif sensor.SensorRight.value == config["Sensor over black"]:
        motor.front_left(config["Corner Speed outer wheels"])
        motor.front_right(config["Corner Speed inner wheels"])
        motor.rear_left(config["Corner Speed outer wheels"])
        motor.rear_right(config["Corner Speed inner wheels"])

    time.sleep(config["Cycle time"])


def test():
    timer = 0
    motor.init()
    sensor.init()

    while timer < 200:
        DriveFromSensors()
        timer = timer + 1

    motor.stop_all()


# test()  ##remove "#" to test the control.py program
