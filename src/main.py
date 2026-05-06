 import logging
from gpiozero import LineSensor

line_sensor_1 = LineSensor(14)
line_sensor_2 = LineSensor(15)
line_sensor_3 = LineSensor(23)

def init():
    pass

def left_is_over_black():
    value = line_sensor_1.value
    logging.info(f"left sensor: {value}")
    return bool(value)

def middle_is_over_black():
    value = line_sensor_2.value
    logging.info(f"middle sensor: {value}")
    return bool(value)

def right_is_over_black():
    value = line_sensor_1.value
    logging.info(f"right sensor: {value}")
    return bool(value)
