import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)        # Green
GPIO.setup(20, GPIO.OUT)        # Red

while True:
    GPIO.output(20, True)       # Red On
    GPIO.output(21, False)      # Green Off
    time.sleep(0.1)
    GPIO.output(20, False)
    GPIO.output(21, True)
    time.sleep(0.1)