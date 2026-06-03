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


def control_global():
    if sensor.sensorL.value == 1:
        motor.front_left(config["Corner Speed inner wheels"])
        motor.front_right(config["Corner Speed outer wheels"])
        motor.rear_left(config["Corner Speed inner wheels"])
        motor.rear_right(config["Corner Speed outer wheels"])
    elif sensor.sensorM.value == 1:
        motor.front_left(config["Speed forward"])
        motor.front_right(config["Speed forward"])
        motor.rear_left(config["Speed forward"])
        motor.rear_right(config["Speed forward"])
    elif sensor.sensorR.value == 1:
        motor.front_left(config["Corner Speed outer wheels"])
        motor.front_right(config["Corner Speed inner wheels"])
        motor.rear_left(config["Corner Speed outer wheels"])
        motor.rear_right(config["Corner Speed inner wheels"])

    time.sleep(0.05)


def control_test():
    index = 0
    motor.init()
    sensor.sensor_global()

    while index < 200:
        control_global()
        index = index + 1

    motor.stop_all()


# control_test()  ##remove "#" to test the control.py program for 10 seconds
