###using python
from picamera import PiCamera
from time import sleep

#setting fixed attributes to the camera will allow for consistency between photos, i.e. no auto-adjustment
camera = PiCamera(resolution=(1920, 1080), framerate=30)
camera.iso = 100 #this value sets sensitivity to light. Lower values are less noisy but perform worse in low light conditions.


camera.start_preview()
sleep(5) #important to sleep for a few seconds to adjust to light levels
for i in range(48): #will save a total of 48 photos
	sleep(3600) #wait 1 hour between photos
	camera.capture('immune_suppression_{timestamp:%m-%d-%Y-%H-%M}_' % i 'hour.jpg') #will save the file with current date and time and HPI
camera.stop_preview()




###practice with short time intervals
from picamera import PiCamera
from time import sleep

#setting fixed attributes to the camera will allow for consistency between photos, i.e. no auto-adjustment
camera = PiCamera(resolution=(1920, 1080), framerate=30)
camera.iso = 100 #this value sets sensitivity to light. Lower values are less noisy but perform worse in low light conditions.
camera.start_preview()
sleep(5) #important to sleep for a few seconds to adjust to light levels
for i in range(48): #will save a total of 48 photos
	sleep(5) #wait 1 hour between photos
	camera.capture('immune_suppression_{timestamp:%m-%d-%Y-%H-%M}_' % i 'hour.jpg') #will save the file with current date and time and HPI
#camera.stop_preview()




###alternative option using command line raspistill
#time is in milliseconds
#t = total period of time to take photos
#tl = take a picture every interval of this size
#this line takes a photos every hour for 48 hours and saves them with a time stamp and HPI
DATE=$(date+"%m-%d-%Y_%H-%M")
raspistill -t 172800000 -tl 3600000 -o immune_suppression_$DATE_%03d.jpg
