import time

import motor
import TRCT5000


def main():
    motor.init()
    TRCT5000.sensor_global()

    input("Press Enter to START (Ctrl+C to stop)...")

    try:
        while True:
            if TRCT5000.sensorL.value == 1:
                motor.front_left(-30)
                motor.front_right(30)
                motor.rear_left(-30)
                motor.rear_right(30)
            elif TRCT5000.sensorM.value == 1:
                motor.front_left(20)
                motor.front_right(20)
                motor.rear_left(20)
                motor.rear_right(20)
            elif TRCT5000.sensorR.value == 1:
                motor.front_left(30)
                motor.front_right(-50)
                motor.rear_left(30)
                motor.rear_right(-30)

            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Keyboard interrupt received — stopping motors.")
        motor.stop_all()


main()
