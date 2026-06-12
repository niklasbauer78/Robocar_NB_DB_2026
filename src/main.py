import control
import motor
import sensor


def main():
    motor.init()
    sensor.init()

    input("Press Enter to START (Ctrl+C to stop)...")

    try:
        while True:
            control.DriveFromSensors()

    except KeyboardInterrupt:
        print("Keyboard interrupt received — stopping motors.")
        motor.stop_all()


main()
