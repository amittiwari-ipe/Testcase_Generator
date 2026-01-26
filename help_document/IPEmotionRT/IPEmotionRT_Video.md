USB-Cameras

Video

On the USB bus, only UVC compliant cameras are supported. Due to the UVC specification the cameras report a required bandwidth during

hardware initialization. The UVC driver then decides, if the remaining bandwidth on the USB bus is sufficient for the camera.

If the Bandwidth does not suffice, the driver rejects the connection of a camera.

However depending on the camera brand and model, some cameras always demand the maximum bandwidth possible per device (which is not the

maximum bandwidth of the bus)! Since this value is more than the half of the maximum bandwidth of the USB bus, only a single one of those camera

can be initialized and operated at once on the USB interface.

Further in the current Logger, using USB 3.0 does not help since the UVC driver / Version in current Kernel does only know of USB 2.0.

Below is a list with some being testet so far:

MISUMI - Single camera supported only MatNo: IPE-CAM-002 / IPE-CAM-003
ELP - Single camera supported only (Model tested: ELP-USB500W02M-AFC45S) MatNo: IPE-CAM-001
Logitech B525 HD Webcam - Single camera supported only

Logitech HD Webcam C270 (Supporting multiple cameras via USB hub - the number of cameras supported depends on the configuration:
IMAGE/MOTION, resolution and sample rate) MatNo: IPE-CAM-004

Data type IMAGE: up to 4 cameras with "standard" settings (320x240 @ 10, 15, 20 Hz)
Data type MOTION: 2 cameras with "high resolution" settings (640x480) - higher resolution only supporting one camera

Logitech Portable Webcam C905 (ID: 046d:0991) - (Supporting multiple cameras via USB hub - the number of cameras supported depends on

the configuration: IMAGE/MOTION, resolution and sample rate)
Logitech Quickcam for Notebooks Pro (2006 model) (ID: 046d:08cb) - Single camera supported only

Genius Slim 2020AF - Single camera supported only, only supporting data type IMAGE
Microsoft LifeCam Cinema (ID: 045e:075d) - on low resolution and sample rates 2 cameras supported - in general Single camera supported only

Microsoft LifeCam Studio (ID: 045e:0772) - on low resolution and sample rates 2 cameras supported - in general Single camera supported only

Microsoft LifeCam NX-6000 (ID: 045e:00f8) - ONLY supporting data type MOTION! - Supporting multiple cameras via USB hub
Endoscope camera: Somikon Modell: PX-1280-675 (ID: 090c:037c) - Single camera supported only - only supporting data type IMAGE

Motion format
When using the format 'MOTION' or 'MOTION with live picture' it is very important that the setting especially the GOP size is set properly.

The GOP size can not be determined automatically.

USB cameras e.g Logitech CS920 might use very large GOP size values (> 100), so that the acquisition might not work correctly if the value is not

correctly configured.

Supported formats
For an initialized USB camera on the logger, the menu 'List video fromats' can be used to visualize the supported formats, where 'H264' is the type
'MOTION'.

IPE-CAM 007
With the USB cameras being used by the UVC driver we are forcing two major disadvantages:

Many USB cameras reserve too many bandwidth on an USB (in worst case the whole USB), so that not as many cameras as required can be connected

to the logger.

Additionally the USB assignment is not guaranteed when rebooting the logger, so that the cameras might record the wrong data (especially when

using different settings).

In order to solve this major disadvantages, IPE CAM 007 is being used with a specific driver.

This way of using IPE-CAM 007 allows to connect several cameras on the same USB with high resolution (<=1920x1080) and high frame rates (<= 15

frames/s).

Additionally IPE-CAM 007 supports an explicit assignment of different cameras using a unique byte identifier.

The IPE-CAM 007 supports 3 different modes:

Autofocus (once):            Autofocus is called once at init and then the camera transmits the data in jpeg mode.

Long distance focus:       Long distance focus is called once at init and then the camera transmits the data in jpeg mode.

Autofocus (coninious):     Autofocus is used permanently and then the camera transmits the data in raw mode.

IP-Cameras
Most commonly used are Axis IP cameras.
The defautlt IP after a factory reset (pressing the control button at power on for 15-30 seconds) is 192.168.0.90.

Axis cameras delivered by IPE usually have 192.168.234.102.


