How to implement Axis F9114 main unit IP cameras with a Logger
on IPEmotion.

1-How to implement Axis F9114 main unit  IP
cameras with a Logger on IPEmotion.

Connect the PC to the Axis F44 via a network cable.

- Assign your PC a static IP address, bearing in mind that the default device address is 192.168.0.90

- Connect via the web interface at the address 192.168.0.90

- You will be requested to assign a username and password.

Note: The device may already have an IP address assigned by another user.

You can reset the device by following the instructions in the official Axis document.

However, this usually involves pressing the reset button for 15 seconds when connecting the device to the power supply.

 -Configure each camera with the desired resolution and options.

Under System à Network : Assign the desired IP address. In my case, I have assigned the IP address 192.168.234.100 and 192.168.234.1 router address.

Setup the default router under system --> Plain Config –> None.

Setup the Alternative HTTP port to 8081 and select “allow anonymous viewers" under System-->plain config-->System.

*Note: For more information visit “Axis official website” there you can find the technical documentation for each device.

2-Device configuration in IPEmotion RT

Add under the ETH2 node where to add the Axis camera system.

Assign the same IP address that you assigned to the Axis device previously, in this case: 192.168.234.100

Also assign the same login and password that you assigned to the device in the previous step.

Add the streams , one for each camera.

For each camera, you must configure the access name and MQTT access name.

However, you need to identify the different streams correctly. The first stream has no index. The second up to the forth stream has the index camera=2,

camera=3, camera=4. For the quad stream the index is camera=quad is defined as indicated in the screenshot below.

For the Stream 1  :8081/mjpg/video.mjpg?resolution=640x480&fps=15

For the other streams you have to add the code marked on Green .

Stream 2  :8081/mjpg/video.mjpg?camera=2&resolution=640x480&fps=15

Stream 3  :8081/mjpg/video.mjpg?camera=3&resolution=640x480&fps=15

Stream 4  :8081/mjpg/video.mjpg?camera=4&resolution=640x480&fps=15

Camera 2

and so on with all the other cameras.

for the case you want a quad picture in one video instrument

 :8081/mjpg/video.mjpg?camera=quad&resolution=640x480&fps=15

Finally, add each stream to a video instrument to check that everything is correct.

Note : You can find this information on the official technical documentation “IPEmotion software manual 30.13 Stream configuration - single and multiple .

This configuration is based on the quadruple Axis F9114 model, but the configuration principle is the same for all models, whether they have one camera or more.

Please note that all test we doing are related to the Eth2 interface and for other interfaces like Eth1 or Eth3 another changes have to be done.


