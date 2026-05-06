from gpiozero import LineSensor
from time import sleep

sensorL = LineSensor(14)
sensorL.when_line = lambda: print('Left Sensor: Line detected')
sensorL.when_no_line = lambda: print('No line detected')

sensorM = LineSensor(15)
sensorM.when_line = lambda: print('Middle Sensor: Line detected')
sensorM.when_no_line = lambda: print('No line detected')

sensorR = LineSensor(23)
sensorR.when_line = lambda: print('Right Sensor: Line detected')
sensorR.when_no_line = lambda: print('No line detected')

sleep(30)