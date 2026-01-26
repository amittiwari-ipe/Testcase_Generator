IPEmotion_PlugIn_VIDEO_V01_03_00

20. Juli 2018

TABLE OF CONTENTS

Table of Contents

1 Important and general information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.1 Important information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.1.1 Safety and Warning instructions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Terms and conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2.1 Legend of used icons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2.2 Support

2 PlugIn overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1 PlugIn description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2 PlugIn Installation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.3 Functional architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

3 Create USB interface system . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.1 USB channel settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

3
3
3
4
4
4

5
5
5
6

7
9

4 Conﬁgure IP network cameras . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
4.1 PC network card settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
4.2 IP camera settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

5 PlugIn conﬁguration for IP camera . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
5.1 Create IP camera interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
5.2 Stream conﬁguration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
5.3 Video channel settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
5.4 Video stream processing examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
5.4.1 Image format
5.4.2 Motion format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
5.4.3 Motion with live picture format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
5.4.4 GOP factor
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
5.4.5 Quality factor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

6 PlugIn Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

2/29

1 Important and general information

1 Important and general information

1.1 Important information

Please follow these instructions before and during the use and application on any IPETRONIK product!

1.1.1 Safety and Warning instructions

Please follow the instructions and information as contained in the user manual!

1. The user can inﬂuence an electronic system by applying the IPETRONIK product. This might cause

risk of personal injury or property damages.

2. The use and application of the IPETRONIK product is permitted only to qualiﬁed professional

staff, as well as, only in appropriate manner and in the designated use.

3. Before using an IPETRONIK measurement system in the vehicle it has to be veriﬁed that no function

of the vehicle, which is relevant for secure operation, might be inﬂuenced:
- by the installation of the IPETRONIK measurement system in the vehicle,
- by an potential malfunction of the IPETRONIK system during the test drive.

In order to avoid possible danger or personal injury and property damages, appropriate actions are to be
taken; such actions have to bring the entire system into a secured condition (e.g. by using a system for
emergency stop, an emergency operation, monitoring of critical values).

Please check the following points to avoid errors:

- Adaption of sensors to components of the electrical system / electronics, brake system, engine and

transmission control, chassis, body.

- Tap of one or several bus systems (CAN, LIN, ETHERNET) including the required electrical

connection(s) for data acquisition.

- Communication with the vehicle’s control units (ECUs), especially with such of the brake system and/or

of the engine and transmission control (power train control system).

- Installation of components for remote data transmission (mobiles, GSM/GPRS modems, WiFi and

Bluetooth components).

The products can be operated in extended temperature ranges greater 70 ◦C and therefore the ope-
rator has to take safety measures to avoid any skin burnings on hot surfaces while touching the
products.

4. Before directly or indirectly using the data acquired by an IPETRONIK measurement system to cali-

brate control units, please review the data regarding to plausibility.

5. With regard to the application of IPETRONIK products in vehicles during use on public roads the manu-
facturer and/or registered user of the vehicle has to ensure that all changes/modiﬁcations have no
inﬂuence concerning the license of the vehicle or its license of operation.

6. User does agree to the instructions and regulations as mentioned above. In case the user does
not agree with the instructions and regulations as mentioned above, he has to notify this expressly and
immediately in writing to IPETRONIK before conﬁrming the sales contract.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

3/29

1.2 Terms and conditions

1.2 Terms and conditions

See IPETRONIK website for details: https://www.ipetronik.com/

1.2.1 Legend of used icons

Tip

Information

Attention!

This icon indicates a useful tip that facilitates the application of
the software.
This icon indicates additional information for a better understan-
ding.
This icon indicates important information to avoid potential error
messages.

1.2.2 Support

Headquarter:

IPETRONIK GmbH & Co. KG
Im Rollfeld 28
76532 Baden-Baden, Germany
Phone +49 7221 9922 0
Fax +49 7221 9922 100
info@ipetronik.com
www.ipetronik.com
Limited commercial partnership with its head ofﬁce in Baden-Baden, registry court HRA No. 201313
IPETRONIK Verwaltungs-GmbH Baden-Baden is an individually liable society, registry court Mannheim HRB
No. 202089
CEOs: A. Wocke, C. Buchholz

Technical support and product information
www.ipetronik.com

e-mail: support@ipetronik.com

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

4/29

2 PlugIn overview

2 PlugIn overview

2.1 PlugIn description

With the Video PlugIn you have access to a large range of USB cameras supporting the Windows WDM
driver and IP-Network cameras supporting the Real Time Streaming Protocol (RTSP).

2.2 PlugIn Installation

In order to use the PlugIn together with IPEmotion you need to install it. The PlugIn is available for download
from the IPETRONIK website: https://www.ipetronik.com/ When you have installed the PlugIn, you need to
launch the IPEmotion software. Then you need to access the application menu and open the OPTIONS. In
the OPTIONS you can activate the PlugIn as indicated below.

The PlugIn is supporting the following Windows operating systems:

(cid:73) 32 bit

(cid:73) 64 bit

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

5/29

2.3 Functional architecture

2.3 Functional architecture

You can interface multiple USB- and IP-cameras to your PC and record the data. The USB cameras get the
power supply via the USB port of the computer and can be automatically detected. The IP-Cameras are
connected to the Ethernet interface of the computer. They require more conﬁguration settings using ﬁxed
IP-addresses for the camera and the Ethernet interface of the PC. Also, framerate, GOV size, codec, login
authentication, stream link address and port numbers need to be deﬁned.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

6/29

3 Create USB interface system

3 Create USB interface system

In the SIGNALS work space, you can create video interfaces. For USB cameras it is recommended to use the
hardware detect function. Due to the standard USB drivers the cameras are automatically detected. Over the
USB interface it is also possible to use the PlugIn settings to update frame rate, compression and picture pixel
resolution on the USB camera. This is different to IP cameras where the setting have to be done in the web
based conﬁguration interfaces of the camera itself.

After successful detection the USB video interfaces is created and for every camera a video channel is
created too. The frame rate is automatically detected from the camera device and set to the maximum value.
The frame rate can be reduced but not increased.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

7/29

3 Create USB interface system

When you start the measurement you can see message picture data indicated as a measurement value on
video channel level.

You can view the video data in the VIEW workspace too. To see the online video stream, you can drag and
drop the video channels into the video instrument.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

8/29

3.1 USB channel settings

3.1 USB channel settings

On video channel level you can select from the following 3 data formats. Additional information about the data
processing mechanism are provided in the last chapter.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

9/29

3.1 USB channel settings

In the video settings tab sheet you have additional conﬁguration functions to deﬁne the resolution of the
stored pictures. 4 different modes with deﬁned quality settings are provided. Depending on the selected
quality rate an estimated data transfer rate is calculated.With the USB interface and the WDM driver it is
possible to update the camera settings from the PlugIn

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

10/29

4 Conﬁgure IP network cameras

4 Conﬁgure IP network cameras

The Video PlugIn is supporting IP cameras too. In the following the conﬁguration is explained based on a
one channel AXIS IP camera model P1214-E. The picture below shows the camera including a suction cup
mounting system which is not part of the standard delivery.

In the ﬁrst step you need to perform the hardware installation including power supply to the signal conditioning
unit. Connecting the camera lenses unit and establishing an Ethernet connection between your PC and the
conditioning unit. When the camera is powered up all LEDs are the signal conditioning unit are in green color.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

11/29

4.1 PC network card settings

4.1 PC network card settings

In order to establish a data communication connection to the camera, you need to deﬁne a static IP address
on the LAN interface of your computer, which is connected to your network camera. The network IP and
subnet mask should be in the same range to that of the IP-camera. The network address of the IP-camera is
mentioned in the manual. In this example the address of the camera is this: 192.168.234.102. This IP-address
was selected in order to make conﬁguration compatible to ETH 2 input of IPElog2.
For the PC LAN network setting the IP-address 192.168.234.200 was selected.

With a web browser you can access the conﬁguration interface. The link to the web browser is part of the
manual. In this example you enter the static IP-address to the browser to the live pciture:
http://192.168.234.102/

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

12/29

4.2 IP camera settings

4.2 IP camera settings

From the web interface you can access the settings area. The default user name and password for this
product is root.

In the conﬁguration menu you need to create an administrative user who is later used by IPEmotion to retrieve
the data from the camera. In the example below the user is called ipe with the corresponding password ipe.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

13/29

4.2 IP camera settings

In the TCP/IP setup you may change the IP-address. However, in this example the default ﬁxed IP is used.
The ﬁxed IP-address is an important setting to retrieve the video data in IPEmotion.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

14/29

4.2 IP camera settings

Another important conﬁguration part are the image settings. Her you can deﬁne the image size in pix and the
compression. The compression is ranging in percent from 0 = no compression to 100 = maximum
compression. In this example we will use 50 percent compression as an initial recommendation. As standard
frame rate 15 Hz is selected. The frame rate has to be considered for the settings in the PlugIn too. The
impact of the different settings will be explained at the end of the manual.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

15/29

4.2 IP camera settings

This camera is providing a h264 video stream. For the h264 codec you can deﬁne a GOV length. GOV is a
setting for the Group of Pictures. This factor has a considerable impact on the amount of data you store. The
factor is determining how many differential frames are transferred together with a full picture. Large GOV
factor will group many different frames together with one full frame. If conﬁgure the GOV factor to one ever
frame transferred is a full frame including all data which will cause high data storage volumes. In our example
we will use a GOV factor of 16. The GOV factor will be conﬁgured in IPEmotion too.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

16/29

4.2 IP camera settings

Finally, we need to enable the RTSP stream and deﬁne the port number. This are important settings so that
data is retrieved by the IPEmotion. The Port number will be used for the connection parameters in IPEmotion
too.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

17/29

5 PlugIn conﬁguration for IP camera

5 PlugIn conﬁguration for IP camera

5.1 Create IP camera interface

For IP cameras you need to create manually an interface system. An automatic hardware dietetic is not
supported for IP camera devices.

If the camera system is supporting several video streams you can create additional streams in the IP camera
system.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

18/29

5.1 Create IP camera interface

In the General tab sheet you deﬁne interface name and description.

In the Connection tab sheet you deﬁne the ﬁxed IP-ddress of the camera, the user and the password, which
was deﬁned in the web interface of the camera. See section 4.2

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

19/29

5.1 Create IP camera interface

In the Streaming tab sheet you have a check box to activate a function called

(cid:73) Automatic sample rate

When this check box is activated the PlugIn will check during an initialization process which is the sample rate
setting of the camera.

Information

It is recommended to deactivate this check box because is it ex-
tending the initialization time for each measurement. You can only
identify the deﬁned frame rate of the camera when all connection
parameters which are discussed below are deﬁned.

Information

When you make any updates in the web interface of the came-
ra like frame rate, compression, GOP factor, resolution, etc you
have to execute the initialize function in IPEmotion to make the
changes in the web interface also affective to the PlugIn.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

20/29

5.2 Stream conﬁguration

5.2 Stream conﬁguration

On Stream level you have to deﬁne the stream conﬁguration setting. When you use e.g. AXIS F44 camera
you have 4 cameras in one IP interface system. In this case you need to add 3 more streams to your
conﬁguration as discussed above. In the General tab sheet you deﬁne stream name and description.

In the Connection tab sheet the stream speciﬁc parameters are deﬁned.

When the settings are all deﬁned you can use the initialize function to test the communication to the camera.
When the automatic sample rate check box is still active, the PluIn retrieves the sample rate / frame rate
setting of the camera. Which match quite close to the setting in the web interface.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

21/29

5.2 Stream conﬁguration

(cid:73) Access name

(cid:73) Port number

(cid:73) Transport protocol

The access name cannot be directly obtained from the web in-
terface of the AXIS camera. To identify the correct access name,
you must consult the camera vendors user manual. In this exam-
ple the stream is deﬁned as: axis-media/media.amp

The port number was deﬁned in the advanced settings of the web
interface of the AXIS camera 4.2.

The transport protocol can be selected UPD or TCP. The default
setting for RTSP protocols is the UPD protocol. However, the cor-
rect setting of the transport protocol is depending on the camera
vendor. In some cases both TCP or UPD work alike.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

22/29

5.3 Video channel settings

5.3 Video channel settings

Similar to the USB cameras you can deﬁne on channel level the data format. For IP cameras the following 3
formats are supported.

(cid:73) Motion

(cid:73) Motion with live picture

(cid:73) Image

The default setting is the Motion format. With the Motion (Motion with live picture) format the h264 stream is
stored in the data ﬁle considers the GOP factor. The GOP factor (Group of Picture) was deﬁned in the web
interface of the camera and should match with the PlugIn settings. In this example the GOP factor was set 16.
See chapter: 4.2

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

23/29

5.3 Video channel settings

When you select the Image format for the channel, you have in the video settings tab sheet a conﬁguration
function of the JPEG quality. The quality factor is ranging between 0 and 100 percent. High quality settings
will lead to higher stored data volumes and better pictures in the video instrument. However, the picture
quality can be inﬂuenced with the compression setting in the web interface of the camera too. Some test data
ﬁle are presented in section 5.4.5

The Image data format is not supporting a GOP factor setting. The Image format requires more processing
CPU resources because h264 stream from the IP camera in this case is transformed into MJPEG picture data
stream for storage.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

24/29

5.4 Video stream processing examples

5.4 Video stream processing examples

Depending on the camera interface (USB / Ethernet) and the related drivers (WDM / Direct X) for USB
cameras or protocols like RTSP (Real Time Streaming) for IP cameras different processing mechanisms can
be applied. Not all drivers and data formats are compatible from all camera vendors. Therefor it is
recommended to test the camera together with the video PlugIn before to purchase the product.

5.4.1 Image format

The Image format is taking incoming data streams and converting them to JPEG pictures. However, this
format is consuming plenty of storage space.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

25/29

5.4 Video stream processing examples

5.4.2 Motion format

The Motion format is basically routing the incoming data stream in the same format to the data storage. That
means incoming h264 data streams are also stored in the format. An incoming MJPEG stream will be stoerd
in the MJPEG format. However, the driver of the camera hardware and the PlugIn must be compatible. Not all
cameras support the Motion format.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

26/29

5.4 Video stream processing examples

5.4.3 Motion with live picture format

This format is a derivate from the Motion format. The main difference is that the PlugIn is processing the
incoming data stream to an additional MJPEG picture in order to have a good update rate of the online picture
for the user. The Motion format supports for h264 streams the GOP factor. The GOP factor is a good setting
to save storage capacity, but it is causing on the downside a delay in the online picture screen update.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

27/29

6 PlugIn Options

5.4.4 GOP factor

In the example below a data ﬁles was recorded for 30 second with the resolution of 800x 600 pixel. As you
can see an increased GOP/GOV (Group of Picture) factor leads to smaller data ﬁles. However, when the GOP
factor is getting larger than for example 32 the impact on the storage volume is not much lower compared to
the factor 16.

5.4.5 Quality factor

Another setting is the quality when you store the data in the Image (MJPEG format). In this case the h264
stream is converted to MJPEG pictures by the PlugIn and you can change the storage and online display
quality. The data was stored again from a 800 x 600 pixel picture for 30 seconds duration. As you can see the
quality has a signiﬁcant impact on the storage volume.

6 PlugIn Options

In the PlugIn options 2 settings are supported.

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

28/29

6 PlugIn Options

(cid:73) Init hardware

(cid:73) Automatic recognition

This is the default setting. With this setting the hardware is initia-
lized before every measurement start.

This setting is developed for IP-cameras. When the measurement
is started the PlugIn will not check the hardware availability and
hardware initialization. The measurement and video stream is di-
rectly displayed. This reduces delay times during the start of the
measurement.

Author: FOT

IPEmotion_PlugIn_VIDEO_V01_03_00

IPETRONIK GmbH & Co. KG

ipetronik.com

29/29


