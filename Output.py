import RPi.GPIO as GPIO # Documentation -> http://abyz.me.uk/rpi/pigpio/python.html
import time

PinNbr = 16
rest = 5
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # Disable warnings
GPIO.setup(PinNbr,GPIO.OUT)

while True:
    print("LED on")
    GPIO.output(PinNbr,GPIO.HIGH)
    time.sleep(rest)
    print("LED off")
    GPIO.output(PinNbr,GPIO.LOW)
    time.sleep(rest)