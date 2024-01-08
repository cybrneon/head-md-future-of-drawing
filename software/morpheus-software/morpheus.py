MORPHEUS SOFTWARE
WRITTEN BY ADAM CLOUD, CYBRNEON, FROM 2023 TO 2024


import RPi.GPIO as GPIO
import vlc		#VLC Media Player library
p = vlc.MediaPlayer("/home/pi/Desktop/Morpheus/sound1.mp3")		#Locating the sound and setting it to letter p
from time import sleep		# this lets us have a time delay (see line 15)  
GPIO.setmode(GPIO.BCM)		# set up BCM GPIO numbering  
GPIO.setup(4, GPIO.IN)		# set GPIO4 as input (button)
  
try:  
    while True:            	#similar to Loop
        if GPIO.input(4): 	# if port 4 == 1
            print ("Port 4 is 1/HIGH/True - Play Sound")
            p.play()
        else:  
            print ("Port 4 is 0/LOW/False - Reset Sound flag")
            p.stop()
        sleep(0.1)         # wait 0.1 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()