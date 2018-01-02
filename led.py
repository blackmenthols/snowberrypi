#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
import os
import gpiozero
from gpiozero import LED, PWMLED, Button
from signal import pause
import subprocess, shlex
from multiprocessing import Process

gpio_leds = [18,23,24]
gpio_btn = 2

def setup_all():
	for pins in gpio_leds:
		GPIO.setup(pins, GPIO.OUT, initial=False)

def all_on():
	for pins in gpio_leds:
		GPIO.output(pins, GPIO.HIGH)

def all_off():
	for pins in gpio_leds:
		GPIO.output(pins, GPIO.LOW)

# first one on, the rest off
def sequence_on(first, second, third):
	GPIO.output(first,GPIO.HIGH)
	GPIO.output(second,GPIO.LOW)
	GPIO.output(third,GPIO.LOW)

def run_long_sequence():
	setup_all()
	for i in range(0, 4):
		print i
		sequence_on(18,23,24)
		sleep(1)
		sequence_on(24,23,18)
		sleep(1)
		sequence_on(23,24,18)
		sleep(1)
		all_off()

def run_omx():
	subprocess.call(shlex.split("omxplayer -o local /home/pi/meep.mp3 --vol -3000"))

def hacky():
	worker1 = Process(name='run_long_sequence', target=run_long_sequence)
	worker2 = Process(name='run_omx', target=run_omx)
	worker1.start()
	worker1.join()
	worker2.start()
	worker2.join()
	return None

# regular setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# button stuffs
GPIO.setup(gpio_btn, GPIO.IN)
GPIO.add_event_detect(gpio_btn, GPIO.RISING)
hacky()
GPIO.cleanup()
exit(1)

#if GPIO.event_detected(gpio_btn):
#	print('Button pressed')

'''
button.wait_for_press()
button.when_pressed=sequence_on(18,23,24)
sleep(2)
print "Pressed! 1"

button.wait_for_press()
button.when_pressed=all_off()
sleep(2)
print "Pressed! 0"

GPIO.setmode(GPIO.BCM)
button.wait_for_press()
button.when_pressed=hacky()
print "Pressed! meep"
exit(1)
'''

'''
for x in range(0, 30):
	all_on()
	print x

'''
