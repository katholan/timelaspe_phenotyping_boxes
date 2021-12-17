# A repository for building a phenotyping cabinet set up with Raspberry Pi-controlled timelapse photos.
This project uses a Raspberry Pi (controlled in headless mode) to take timelapse photos of leaves/plants in a plastic box. The price per unit is estimated to be $100-200 at the time of writing. It is based on the Navautron system from [this publication from Barbacci et al](https://doi.org/10.1111/tpj.14747).

![A gif of the photos taken from a 96 hour immune assay timecourse. It shows the progression of plant immune response on several Nicotiana benthamiana leaves](test_ir2.gif)

## Supplies needed for this project
1. Raspberry Pi 4, can be 1 or 2 Gb RAM
2. Pi power supply
3. Pi Case
4. Heat sinks and case fan
5. MicroSD card
6. MicroSD USB adapter
7. Raspberry Pi camera (V2), NoIR camera, or any Pi compatible camera or lens mount and lens
8. Camera case
9. Ethernet cable
10. Wifi
11. Laptop or computer
12. Clear plastic bin or acrylic box. I used clear plastic storage bins from Target.
13. White LED lights (eg strip lights or aquarium lights)
 
Raspberry Pis can be purchased from several places, eg Adafruit and Canakit. These brands also sell kits that often include at the very least a power supply. However, these kits can be more expensive than buying the parts individually. I ended up buying the standalone Pis [from Adafruit](https://www.adafruit.com/product/4295) and a cheaper case kit that included a power supply [here](https://www.amazon.com/gp/product/B07TTN1M7G/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1), heat sinks, and a fan. Some of the cases included in the kits also don't include a slot for the camera, meaning the case can't be closed completely when the camera is in use.

For the camera, I recommend getting a nicer lens mount like [this](https://www.amazon.com/dp/B013JTY8WY?psc=1&ref=ppx_yo2_dt_b_product_details) along with a [set of lenses](https://www.amazon.com/dp/B07NW8VR71?psc=1&ref=ppx_yo2_dt_b_product_details) or an [individual lens](https://www.amazon.com/dp/B08H512P4P?psc=1&ref=ppx_yo2_dt_b_product_details) if you know what angle you need for your project. For my boxes, I chose the M12 lens mount and the 70 degree low distortion lens, which seems to work well for my size boxes. These lenses do need to be hand focused. There are other lenses and modules that can be focuses programatically. 

Make sure the SD card is big enough to hold all of your pictures during the timecourse. For the NoIR camera with pictures at the highest resolution, 100 photos used ~3 Gb of memory. This setup does not include cloud backup. At the end of an experiment, I uploaded data from the Pi to Google Drive since the Pi file structure is unreadable by PC/Windows.

## Setting Up Your Raspberry Pi

To set up your Pi, first you'll need to format the microSD cards. Plug in your microSD card into a computer. Download the [Raspberry Pi Imager](https://www.raspberrypi.org/software/) software and follow instructions/[video](https://www.youtube.com/watch?v=ntaXWS8Lk34) for formatting your SD card.
You will only need to do this once. Make sure all important info is off of the SD card as this process will erase all existing data.

For a headless connection (using your laptop or computer to control the Pi), you can generally follow the instructions in this [tutorial](https://maker.pro/raspberry-pi/projects/how-to-connect-a-raspberry-pi-to-a-laptop-display), although some things might be a bit different. First, make a WiFi Config file. For WiFi networks that require a username as well, replace the network secion in the config file with the below code, substituting the username and password for the network:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=us

###Use for network with username and password
network={
        ssid="YOUR_WIFI_NAME"
        key_mgmt=WPA-EAP
	identity="USERNAME"
	password="PASSWORD"
}

###use for network with just password
network={
	ssid="YOUR_WIFI_NAME"
	psk="PASSWORD"
	key_mgmt=WPA-PSK
}
```

Once you have your config file, you can put the SD card into your Pi, connect your Pi directly to your computer with an Ethernet cable, and power on your Pi. All Pis default to "raspberrypi" as the hostname, so finding out the IP address with the "Advanced IP Scanner" isn't completely necessary, and you can move to the next step. Download [PuTTY](https://www.putty.org/) to your laptop and enter the hostname ('raspberrypi') or the IP address as determined by the Advanced IP Scanner software. Click "yes" on the security alert and it should connect to your Pi in the PuTTY terminal. The defaul username is "pi" and the defaul password is "raspberry" for all Pis. Type `sudo raspi-config` and enable VNC connection and change the resolution to something besides the default, then finish and reboot. The menu may be slightly different than the one in the tutorial.

Download [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) and search for the hostname ("raspberrypi"), enter the username and password ("pi" and "raspberry"). You should now be connected to your Pi. At this point, you can change the username and password if you want. After setting up once, you should be able to connect to your Pi through VNC anytime (sometimes it takes a couple tries to connect). If it's still not connecting after a couple tries, delete the connection from VNC and then search for your Pi again. It will ask you for the username and password and you should be able to connect. The Pi 4s do have WiFi and may be able to connect to your computer remotely, but reconnecting with the Ethernet cable should allow connection through VNC again.

To use the camera module, follow this [tutorial](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2). You'll need to install the camera in the Pi and enable the camera module.

Pis do not have their own internal clock; accurate timestamps rely on WiFi connection (or you can reset the time every single time you turn the Pi back on). I had issues getting the WiFi to connect and running `rfkill unblock wifi` in the terminal fixed it for me.

## Raspberry Pi Camera Timelapse

For this code, I am using the Python package [`PiCamera`](https://picamera.readthedocs.io/en/release-1.13/index.html).

The file `camera.py` contains the code I used for taking pictures with the Raspberry Pi. Do NOT name your files after already existing scripts (eg `picamera.py`).

## Analyzing Images

To make phenotyping easier, I decided to crop each individual leaf from each timepoint picture, and reorganize those cropped images of the same leaf in sequence in a single plot to easily view them side by side. Basically, instead of all leaves for one timepoint, I can see a specific leaf at every timepoint in the same image. This way, I can see that leaf's progression throughout the experiment at the same time without flipping between timepoint images.

I have a Google Colab notebook that contains the code for this reorganizing. For access to this notebook, please email me.

To reorganize, you will need the coordinates for each leaf. I get this manually using ImageJ:
1. Start ImageJ or Fiji
2. Open File -> Open one of your timecourse images. They should all be approximately in the same orientation/FOV, so it doesn't matter which one you pick.
3. Using the "Rectangle" selection tool, draw a large box to encapsulate all leaves in the image. Since I number the leaves starting at "1" but Python numbering starts at "0", the ROI containing all of the leaves essentially becomes the "0th" leaf, which makes numbering the rest of the leaves easier/more intuitive.
4. Press "Ctrl + B" to save the ROI selection.
5. Repeat this process for every individual leaf on the image.
6. Once the full image and all individual leaves have a box around them, click "Analyze" -> "Set Measurements" and make sure "Bounding Rectangle" is checked. You can check any of the other boxes if you want more information.
7. Image -> Overlay -> ROI Manager
8. Select all ROIs in the ROI Manager (Ctrl + A) -> Measure. This will pop up a table containing coordinate information.
9. File -> Save on the pop up table.
11. Open this saved file in Excel or a similar program. You will need to rename some columns and create new columns. There is an example of what this file should end up looking like in this repository.
12. You will end up with 5 total columns, "name", "x1", "y1", "x3", "y3". I rename the ROIs to "full_image", "leaf1", "leaf2", etc.
13. BX = x1
14. BY = y1
15. BX + Width = x3
16. BY + Height = y3
17. Save this file as a .csv file to your computer.
18. You can double check your math for x3,y3 if you want by returning to ImageJ and pressing Ctrl+Y -> Check show coordinates. You can also press Edit -> Selection -> Properties -> Check "Show Coordinates".




