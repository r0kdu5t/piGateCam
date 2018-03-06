# seccam.py - Mark Beckett
#
import os
import glob
import time
import RPi.GPIO as GPIO

GPIO.setmode( GPIO.BCM )
GPIO.setwarnigs( False )

# set GPIO 24 as an Output
GPIO.setup( 24, GPIO.OUT )
# set it LOW until we need it.
GPIO.output( 24, GPIO.LOW )
# set GPIO 23 as an input and use internal pullup resistor.

