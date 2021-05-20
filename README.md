# A repository for various Raspberry Pi scripts, for example taking photos or measuring humidity and temperature.

## Materials needed for this project
1. Raspberry Pi and optional case
2. Pi power supply
3. MicroHDMI to HDMI cable
4. MicroSD card (Make sure it is big enough to hold all of your pictures during the timecourse. This setup does not include cloud backup.)
5. MicroSD USB adapter
6. Raspberry Pi camera (V2)
7. USB-connected eyboard and mouse
8. Monitor with HDMI (Note: You can use a monitor, TV, or laptop. If you use a laptop, there are some extra steps you'll need to do to use your laptop as a monitor. This requires an Ethernet and a WiFi connection.) 
    If using the laptop method, you'll also need a network cable (Ethernet).
9.  

##Setting Up Your Raspberry Pi

To setup your 

Plug in your microSD card into a computer. 
Download the [Raspberry Pi Imager](https://www.raspberrypi.org/software/) software and follow instructions/[video](https://www.youtube.com/watch?v=ntaXWS8Lk34) for formatting your SD card.
You will only need to do this once. Make sure all important info is off of the SD card as this process will erase all existing data.

If you are using a laptop to do a headless connection to your Pi, you'll need a few extra steps to connect.
After formatting your SD card, you'll need to make a WiFi Config file [as described here](https://maker.pro/raspberry-pi/projects/how-to-connect-a-raspberry-pi-to-a-laptop-display). Put the alternative file here as well that shows how to do it on a network that has a username and password. Once this is added, you can put the SD card into your Pi. Follow the rest of the instructions on this tutorial. Some things may be slightly different (this is an older tutorial). You'll know you did it right when the Pi desktop shows up in the VNC viewer.

Connect your Pi to power and use the Ethernet cable to connect the Pi to your laptop.

Have PuTTy downloaded to your laptop. Open PuTTy, in the hostname secion, type "raspberrypi". You'll probaby have to click "accept" or "yes" to show you know you're connecting to a trustworthy connection. After this, it'll ask you for the username (pi) and password (raspberry). These are the default. 

After this, you'll need the VNC software. After setting up once, you should be able to connect to your Pi through VNC anytime (sometimes it takes a couple tries to connect).

## Raspberry Pi Camera Timelapse

See [this tutorial](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera) for starting information.

For this code, I am using the Python package [`PiCamera`](https://picamera.readthedocs.io/en/release-1.13/index.html).

The file `camera.py` contains the code I used for taking pictures with the Raspberry Pi. Do NOT name your files after already existing scripts (eg `picamera.py`).
