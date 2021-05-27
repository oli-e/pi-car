#!/usr/bin/python3

from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=24, trigger=23, max_distance=2.0)
while True:

	distance = sensor.distance * 100
	print("Distance : %.1f  cm " % distance)
	sleep(1)
