# MORPHEUS SOFTWARE 0.1
# CYBRNEON SOFTWARE 2024

import RPi.GPIO as GPIO
import os
import vlc # VLC media player library
from time import sleep # to pause the script for a certain time

audio_folder = "/home/pi/Desktop/Morpheus/audio" # path to all audio files
audio_files = sorted([file for file in os.listdir(audio_folder) if file.endswith(".mp3")]) #List of mp3s in the audio folder

instance = vlc.Instance() # creating a VLC instance
media_list = instance.media_list_new([os.path.join(audio_folder, file) for file in audio_files]) #Creating a media list with all the mp3s in the audio folder
media_list_player = instance.media_list_player_new() # creating a media list player
media_list_player.set_media_list(media_list)

GPIO.setmode(GPIO.BCM) # set up BCM GPIO numbering
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set GPIO4 as input (button) with a pull-up resistor

try:
    while True:
        if GPIO.input(4): # monitoring the GPIO pin 4 state
            print("GPIO 4 is 1/HIGH/True - Sound Playing")
            if not media_list_player.is_playing():
                media_list_player.play()
        else:
            print("GPIO 4 is 0/LOW/False - Sound Stopped")
            media_list_player.stop()
            sleep(0.1)

except KeyboardInterrupt: # stop the program with Ctrl + C
    pass

finally:
    GPIO.cleanup() # release all GPIO resources