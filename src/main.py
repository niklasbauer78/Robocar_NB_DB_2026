import control
import motor
import sensor


def main():
    motor.init()
    sensor.sensor_global()  # get sensor values

    input("Press Enter to START (Ctrl+C to stop)...")

    try:
        while True:
            control.control_global()  # activate wheels according to sensor values

    except KeyboardInterrupt:
        print("Keyboard interrupt received — stopping motors.")
        motor.stop_all()


main()
