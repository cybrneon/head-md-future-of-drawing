# Software

## What I'm doing
I'm playing a sound each time the pen is removed from the pen holder, and stopping the sounds when the pen is inserted in the pen holder.

## Tutorial

### 1. Setting up the RP
This setup applies if you're flashing and connecting from Windows. MacOS should be slightly different.
#### Installing Rapberry Pi OS (64Bits), released on the 2023-12-05 (5dec23)
Flashing on a SD card, and setting up settings for automatic wifi connection and SSH.

When the RP is booting, connect by SSH from the Terminal to enable VNC that will allow connecting to the RP wirelessly without a screen connected.
<br>
`ssh pi@raspberrypi.local`
<br>
enter the password you set when flashing the SD card.
The RP will give you a welcome message and be ready for commands. Then type:
<br>
`sudo raspi-config`
<br>
First select Interface > VNC > Enable.
<br>
Go back with ESC and select Display Options > VNC Resolution > And set a resulution for the display you'll see in the VNC Viewer App you'll install on your computer. I recommend `1280x720`, `1280x1024` or `1200x1600`.

Now, you can use VNC Viewer on your computer to connect to the RP by connecting to the address `raspberrypi`.

> Attention!
> Your computer and the RP has to be on the same Wi-Fi network.

> Attention!
> VNC Viewer has some unexpected behavior. VNC never worked all the time.
><br>
> If VNC doesn't connect or if it takes too much time, close the app and relaunch it again. If it's still not working, keep doing that.

When booting into desktop, apply system updates before doing anything. (you can do these in SSH, on the Terminal)
<br>
`sudo apt-get update`
<br>
`sudo apt-get install`
<br>
`sudo apt-get upgrade`

You have now sucessfully set up the Raspberry Pi!

#### Installing Software
To install the Adafruit speaker bonnet, I type this into the Terminal to install i2s amplifier:
`curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash`

[GitHub Source](https://github.com/adafruit/Raspberry-Pi-Installer-Scripts)

Do this one time, reboot. Do it a second time, it will ask to test the speakers and type Yes.
If there's no sound, keep following the setup and reboot again.
Now, you should open up the terminal (on the desktop, or SSH) and type:
<br>
`sudo raspi-config`
<br>
Go to System > Default Audio > and select the new device that should be called "hi-fi-berry" or something like that.

If there's no sound when you play something, go to the top bar of the Desktop UI, on the Sound icon, right click and select the new device.

Normally, it should work now.

You can also check in the terminal:
`alsamixer`
<br>
It will open the system sound mixer. Press F6 and select the new device.

### 2. Enabling autostart
To enable a python script automatically at startup, you need to create a folder inside of home/pi/.config called `autostart`, where you'll put a file called `something.desktop` (the something can be replaced by what you want to call the file).

Open the file, and paste this inside:

[Desktop Entry]
<br>
Encoding=UTF-8
<br>
Type=Application
<br>
Name=<Something>
<br>
Comment=
<br>
Exec= python /home/pi/desktop/Morpheus/morpheus.py (here you can put the link to your python exec)
<br>
StartupNotify=false
<br>
Terminal=True
<br>
Hidden=False

And it's done! Now reboot and the python program should autostart.