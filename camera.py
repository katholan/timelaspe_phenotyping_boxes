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

#set working directory
os.chdir('/home/pi/kat_holan/test_ir2')

#setting fixed attributes to the camera will allow for consistency between photos, i.e. no auto-adjustment
camera = PiCamera(resolution=(3280, 2464), framerate=30) #the max for stills with the V2 camera is 3280 × 2464
camera.iso = 100 #this value sets sensitivity to light. Lower values are less noisy but perform worse in low light conditions.
camera.start_preview()
sleep(5) #important to sleep for a few seconds to adjust to light levels
for i in range(0,96): #will save a total of 97 photos, starting at 0 HPI to 96 HPI. make sure everything is setup before running!
	camera.capture("test_ir_{0}.jpg".format(i)) #names each picture HPI
	sleep(3600) #wait 1 hour between photos
camera.stop_preview()
