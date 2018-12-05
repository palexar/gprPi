
from time import sleep
import RPi.GPIO as GPIO

adcIn = 12
pulseSignal = 13


GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.OUT)
GPIO.setup(12, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)

#GPIO.setup(adcIn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



print("Start")
while True:

    GPIO.output(13,0)
    print("GPIO IN")    
    print(GPIO.input(adcIn))

    print("GPIO OUTPUTS")

    GPIO.output(13, 1)

    print(GPIO.input(adcIn))

    sleep(0.5)
