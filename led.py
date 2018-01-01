#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import os

def on_18():
	GPIO.output(18,GPIO.HIGH)
	GPIO.output(23,GPIO.LOW)
	GPIO.output(24,GPIO.LOW)
	time.sleep(.300)

def on_23():
	GPIO.output(23,GPIO.HIGH)
	GPIO.output(18,GPIO.LOW)
	GPIO.output(24,GPIO.LOW)
	time.sleep(.300)

def on_24():
	GPIO.output(24,GPIO.HIGH)
	GPIO.output(23,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)
	time.sleep(.300)

def all_on():
	on_18()
	on_23()
	on_24()


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

for x in range(0, 30):
	all_on()
	print x

GPIO.cleanup()




