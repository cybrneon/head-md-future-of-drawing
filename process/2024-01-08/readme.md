# Diving back into the project
I just came back yesterday afternoon from a week in the sun at 20 degrees, to the lovely swiss weather of 0 to -2 degrees with strong winds.

Diving back to the project is going to be slow, but fine.

## 3D print status
Fred launched the official and final print for my revised shapes. I should get it at the end of the day. Update: Two pieces didn't finish yet, so I'll get them on Tuesday.

## The Code for the program
```
# MORPHEUS SOFTWARE 1.0
# CYBRNEON SOFTWARE 2024


import RPi.GPIO as GPIO
import random
import vlc		#VLC Media Player library
sounds = vlc.MediaPlayer("/home/pi/Desktop/Morpheus/audio/test2.mp3")		#Locating the sound and setting it as sounds
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
```

## Thinking about the final presentation
For Thursday 11 Jan, at 15h, first draft of project documentation PDF.

On Monday 15 Jan, 17h final version of project documentation PDF.

And a big yay! I can finally present my project the way I want with a custom presentation (on top of the project documentation that will be given).

## Also thinking of the AI part
I'm trying to see how I can do what I wanted to do, easily without too much hassle.

Here's a link I used to encode Base64 to mp3 for tests I got with Google's TTS.
https://www.ipvoid.com/base64-to-mp3/

## And finally
Because I'm sick, I'm missing a day to go see my doctor about a quite serious issue.
But I'll still work a bit.