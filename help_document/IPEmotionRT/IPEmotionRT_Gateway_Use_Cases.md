Gateway use cases

As ASAM CMP supports all important traffic types, this can be used for sending and receiving traffic different types with

LAN respectivelyWiFi.

Therefore in 2025 R1 a modular CMP device was introduced in IPEmotion which can be freely configured concerning the

interfaces (CAN, LIN, FlexRay, ETHERNET).

Concerning WiFi the data shell be sent via WiFi Access Point of the logger.

In this article a table will give an overview which logger types supports CMP via which medium.

The following table lists the logger types and their availibilities.

Not available means that the connection is not provided by this logger type (e.g. WiFi Access Point at ARCOS2).

Not supported means that the connection is provided but does not support the CMP feature (e.g. IPElog2 cannot offer

CMP receiption due to the use of LANTRONIX).
Finally several use cases will be described using M-Gateway3 where all combinations are possible.

LAN

WiFi-AP

WiFi

IPE853

Send/Receive

Not available

Receive,(Send)

IPElog2-003/004

Send/Receive

Not-Supported

Not-Supported

IPElog2-001/002

Send/Receive

Not-Supported

Not-Supported

M-LOG V3

Send/Receive

Not-Supported

Not-Supported

ARCOS 2

Send/Receive

Not available

Receive,(Send)

ARCOS 1.5

Send/Receive

Not available

Not-Supported

µCROS-SL

Send/Receive

Not available

Receive,(Send)

IPE833

IPEhub2

Send/Receive

Send,(Receive)

Receive,(Send)

Not supported

Not supported

Not supported

M-Gateway3 use cases

 As source for all following use cases an M-Gateway3 is used even if all other RT loggers and also IPEmotionPC with

Protocols PlugIn can be used in the same way.

On M-Gateway3 the following elements are connected:

IPEspeed on CAN1

M-TH3 and M-SENS3 on CAN2

Mx-SENS2/4 on FEATURE-X-LINK

Route CANs via ETH to PC
CAN1 and 2 are forwarded to a PC via CMP traffic to a Windows PC where IPEmotionPC 2025 R1 with Protocols PlugIn

V03.11.00 are running.

The M-Gateway3 is connected via ETH interface to the PC which has the IP address 192.168.236.100.
M-Gateway3 CAN2ETH.rwf is running on M-Gateway3

PC CAN2ETH.iwf is running on PC

Route CANs via ETH to IPE853
CAN1 and 2 are forwarded to a PC via CMP traffic to ETH of IPE853.

The M-Gateway3 has the optional RT.UI address 192.168.136.201.

The M-Gateway3 is connected via ETH interface to the ETH2 which has the IP address 192.168.136.202.
M-Gateway3 CAN2ETH.rwf is running on M-Gateway3

IPE853 CAN2ETH2.rwf is running on IPE853.

Route CANs via WiFi to PC
CAN1 and 2 are forwarded to a PC via CMP traffic to a Windows PC where IPEmotionPC 2025 R1 with Protocols PlugIn

V03.11.00 are running.

The M-Gateway3 is connected via WiFi interface (AP) to the PC which has the IP address 192.168.237.100.

M-Gateway3 CAN2WIFI.rwf is running on M-Gateway3

PC CAN2WIFI.iwf is running on PC

Route CANs via WiFi to logger

For the M-gateway3 the same configuration as for connecting to the PC can be used.
M-Gateway3 CAN2WIFI.rwf is running on M-Gateway3 where M-Gateway3 is providing an WiFi access point.

On the other ´s logger side (IPE853, ARCOS2) the connection to this access point has to be set up on the  communication
tab.

Addtitionally the WiFi interface include a modular CMP device is to be added on the signal tab.

For the CMP device IP and bus ids need to match with the M-Gateway3 configuration.

Example for  IPE853 getting CAN-2 is to be found in IPE853 Wifi.rwf.


