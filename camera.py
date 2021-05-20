#Once you're connected to your Pi, click the logo icon in the upper left, then programming, then Thonny Python IDE
#Copy/Paste the following code into the script and save as camera.py
#You can also move this onto the microSD card.
#You can run the code from the python shell in Thonny or from the Pi command prompt.
#Make sure your camera is enabled by going to home/preferences/raspberry configurations/interfaces/enable camera
#Make sure your setup is complete and your camera is in the right position before running. 
#It starts with a 0 hour photo that will take almost immediately after running.
#Use this photo to ensure your setup is correct before disconnecting your laptop/monitor.

from picamera import PiCamera
from time import sleep
import os

#set working directory where you want the photos to be saved.
os.chdir('/home/pi/kat_holan/test')

#setting fixed attributes to the camera will allow for consistency between photos, i.e. no auto-adjustment
camera = PiCamera(resolution=(1920, 1080), framerate=30) #the max for stills with the V2 camera is 3280 × 2464
camera.iso = 100 #this value sets sensitivity to light. Lower values are less noisy but perform worse in low light conditions. Since this setup uses constant external light we can keep this value low

camera.start_preview()
sleep(5) #important to sleep for a few seconds to adjust to light levels
for i in range(49): #will save a total of 49 photos
	camera.capture('immune_suppression_{0}_hour.jpg'.format(i)) #will save the file with the HPI from 0 to 48.
	sleep(3600) #wait 1 hour between photos
camera.stop_preview()
