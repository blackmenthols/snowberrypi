#!/usr/bin/python


from gpiozero import Button
import subprocess, shlex
button = Button(2)

#button.wait_for_press()
#button.when_pressed=subprocess.call("omxplayer -o local meep.mp3 --vol -2000")
#print('You pushed me')

subprocess.call(shlex.split("omxplayer -o local meep.mp3 --vol -2000"))
