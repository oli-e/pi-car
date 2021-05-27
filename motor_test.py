import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 37
Motor1B = 35
Motor1E = 33

Turn1 = 36
Turn2 = 38
TurnE = 40
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Turn1,GPIO.OUT)
GPIO.setup(Turn2,GPIO.OUT)
GPIO.setup(TurnE,GPIO.OUT)
 
print("Turning motor on")
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
 
sleep(2)
 
print("Stopping motor")
GPIO.output(Motor1E,GPIO.LOW)

sleep(2)

print("Turning steering on")
GPIO.output(Turn1,GPIO.HIGH)
GPIO.output(Turn2,GPIO.LOW)
GPIO.output(TurnE,GPIO.HIGH)
 
sleep(2)
 
print("Stopping steering")
GPIO.output(TurnE,GPIO.LOW)

GPIO.cleanup()
