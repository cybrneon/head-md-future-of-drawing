# MORPHEUS SOFTWARE 0.1
# CYBRNEON SOFTWARE 2024


import RPi.GPIO as GPIO
import os
import vlc		#VLC Media Player library
sounds = vlc.MediaPlayer("/home/pi/Desktop/Morpheus/audio/story1.mp3")		#Locating the sound and setting it as sounds
from time import sleep		# this lets us have a time delay (see line 15)  
GPIO.setmode(GPIO.BCM)		# set up BCM GPIO numbering  
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)		# set GPIO4 as input (button)
  
try:  
    while True:            	#similar to Loop
        if GPIO.input(4): 	# if port 4 == 1
            print ("GPIO 4 is 1/HIGH/True - Sound Playing")
            sounds.play()
        else:  
            print ("GPIO 4 is 0/LOW/False - Sound Stopped")
            sounds.stop()
        sleep(0.1)         # wait 0.1 seconds  
        
except KeyboardInterrupt: # stop the program with Ctrl + C
    pass
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()