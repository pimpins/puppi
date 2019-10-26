#calibration
from __future__ import division
import time
import Adafruit_PCA9685

from numpy import *
from math import *
import time
import numpy as np

pwm = Adafruit_PCA9685.PCA9685()

def set_servo_pulse(channel, pulse):
	pulse_length = 1000000
	pulse_length //=60
	print('{0}us per bit' .format (pulse_length))
	pulse *= 1000
	pulse //= pulse_length
	pwm.set_pwm(channel, 0, pulse)
	pwm.set_pwm_freq(60)

while True:
	pwm.set_pwm(0, 0, 598-244) #port zero : right front tibia
	time.sleep(0.001)
	
	pwm.set_pwm(1, 0, 770+289-89) #port 1: right front femur
	pwm.set_pwm(2, 0, 610)                            #port 2: right hip


	pwm.set_pwm(3, 0, 576-367) #port 3: left front tibia  add 100 to this
	pwm.set_pwm(4, 0, 623) #port 4: left front femur
	pwm.set_pwm(5, 0, 610)                            #port 5: left hip

	pwm.set_pwm(8, 0, 597+375) #port 8: left back femur
	pwm.set_pwm(9, 0, 742-364) #port 9: left back tibia
	pwm.set_pwm(10, 0, 610)                            #port 10: left back hip
	
	pwm.set_pwm(12, 0, 536) #port 6: right back femur  
	pwm.set_pwm(7, 0, 626) #port 7: right back tibia
	pwm.set_pwm(11, 0, 610)    