import time

import motor
import sensor


def main():
    motor.init()
    sensor.sensor_global()

    input("Press Enter to START (Ctrl+C to stop)...")

    try:
        while True:
            if sensor.sensorL.value == 1:
                motor.front_left(-30)
                motor.front_right(30)
                motor.rear_left(-30)
                motor.rear_right(30)
            elif sensor.sensorM.value == 1:
                motor.front_left(20)
                motor.front_right(20)
                motor.rear_left(20)
                motor.rear_right(20)
            elif sensor.sensorR.value == 1:
                motor.front_left(30)
                motor.front_right(-50)
                motor.rear_left(30)
                motor.rear_right(-30)

            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Keyboard interrupt received — stopping motors.")
        motor.stop_all()


main()
