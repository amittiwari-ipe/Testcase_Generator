IPEmotion_PlugIn_Protocols_V03_12_00
USER MANUAL

July 2025

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00-

Table of Contents

1 Introduction

Disclaimer

Limitation of Liability

Warranty

Copyright and Duplication

Trademark

Liability, Warranty, Copyright, License Agreement

Contact Information

Support

2 Safety Instructions and general Information

2.1 Safety and Warning Instructions

2.2 General Information

2.2.1 About This Manual

2.2.2 Legend of the Icons

3 PlugIn Overview

3.1 PlugIn description

3.2 PlugIn installation

3.3 Overview of supported vendors

3.4 Detailed list of vendors and devices

4 PlugIn configuration

4.1 Functional architecture

4.2 Creating interface systems

5 Device specific configurations

5.1 IPEhub2 specific functions

5.2 ETHgateway-CLFD specific function

5.3 CAN FD Satellite

5.4 FlexRay Satellite

5.5 LIN Satellite

6 Measurements on CAN FD, LIN, ETH, FlexRay interfaces

6.1 Description file import format overview

6.2 CAN interface

6.3 LIN interface

6.4 ETH interface

TABLE OF CONTENTS

1

1

1

1

1

2

2

2

2

3

3

4

4

4

6

6

7

8

9

13

13

14

16

16

18

19

20

20

21

22

26

30

34

6.4.1 ETH Status channels

6.4.2 ETH Traffic

6.4.3 Satellites for CAN FD, LIN, FlexRay

6.4.4 PLP Devices - Automotive Ethernet

6.4.5 WWH-OBD

6.4.6 DLT Diagnostic Log and Trace

6.5 A2L import - DAQ list with graphical filling level indication

6.5.1 DAQ list filling process

6.5.2 DAQ list overflow – rejected signal export

6.6 Edit A2L dynamic DAQ list ODT values during the import

6.6.1 A2L Import for array signals

6.6.2 A2L import with additional FlexRay parameters import

6.6.3 A2L import from zip files (X-Modules)

6.6.4 XCP, CCP second tester

6.6.5 XCP transport layers

6.6.6 XCPonETH for IPv6

6.7 A2L export with pre defined DAQ list

6.8 FIBEX import

6.8.1 Import CAN signals from FIBEX files

6.8.2 Import CAN FD signals from FIBEX files

6.8.3 Display of Sender name for FIBEX, DBC, AUTOSAR messages

6.9 Description file import with CSV file for channel reference

6.9.1 Multi column CSV selection for description file imports (DBC, A2L)

6.9.2 Check duplicate channel names during description file import

6.10 Description file import with INCA LAB file

6.11 Synchronization of description files

6.12 J1939 Diagnostics

6.12.1 Using J1939 DM1 error codes as trigger

6.13 UDS Diagnostics

6.13.1 Using UDS DTCs error codes as trigger

6.14 OBD-2 diagnostics

6.15 OBD-2 extended mode

36

37

39

42

43

44

45

47

48

49

51

54

57

58

60

61

62

63

63

64

65

66

68

70

74

76

80

84

85

88

90

94

TABLE OF CONTENTS

1 Introduction

Disclaimer

This manual provides important technical information concerning the conditions of use of
IPETRONIK products. This information has been thoroughly checked and refers to the current
development status of the product. It may change at any time at short notice.

No claims whatsoever can be made against the manufacturer based on the contents of this
manual. IPETRONIK GmbH & Co. KG assumes no liability, especially for editorial or technical
errors or missing information of any kind.

No liability is accepted for damage resulting from improper use of the product and/or failure to
observe the manual, in particular the safety instructions.

Limitation of Liability

Any liability of IPETRONIK, its agents, representatives and the like, especially for personal
injury or property damage of any kind, is excluded (to the extent permitted by law), if the above
instructions and warnings have not been followed.

Warranty

Products, accessories and services are under warranty for 12 months.

All product data, specifications, drawings, etc. are current as of the date of creation indicated.
For the purpose of the optimization of technical processes and production, some details of our
modules and auxiliary components may be changed at any time and without prior notice. Des-
pite the fact that this document has been prepared with the utmost care, it may not be free from
printing, typing or transmission errors. No warranty is given for these errors.

Copyright and Duplication

All rights, in particular ownership, copyright and trademark rights, are reserved by
IPETRONIK GmbH & Co. KG. The rights to all third-party trademarks mentioned remain unaf-
fected.

This document may only be reproduced with the permission of IPETRONIK GmbH & Co. KG. All
graphics and explanations of technical correlations are protected by copyright. Any use beyond
the scope of this manual is not permitted.

All concepts and procedures mentioned in this manual are the intellectual property of
IPETRONIK GmbH & Co. KG. Without the written permission of IPETRONIK GmbH & Co. KG,
use or copying by third parties is strictly prohibited. This manual may be changed at any time
without prior notice.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

1

Trademark

All trademarks mentioned in this document are the property of their respective owners.

Liability, Warranty, Copyright, License Agreement

Please refer to www.ipetronik.com/terms-and-conditions.html for detailed contract information:

▶ Limitation of liability

▶ Warranty

▶ Copyright and Duplication

▶ Software license agreement

Contact Information

IPETRONIK GmbH & Co. KG

Im Rollfeld 28

76532 Baden-Baden

Germany

+49 7221 9922 0

info@ipetronik.com

www.ipetronik.com

Support

support@ipetronik.com

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

2

2 Safety Instructions and general Information

2.1 Safety and Warning Instructions

Please follow the instructions and information as contained in the user manual!

1. The user can influence an electronic system by applying the IPETRONIK product. This

might cause risk of personal injury or property damages.

2. The use and application of the IPETRONIK product is permitted only to qualified pro-
fessional staff, as well as, only in appropriate manner and in the designated use.

3. Before using an IPETRONIK measurement system in the vehicle it has to be verified that no

function of the vehicle, which is relevant for secure operation, might be influenced:

▶ by the installation of the IPETRONIK measurement system in the vehicle,

▶ by a potential malfunction of the IPETRONIK system during the test drive.

In order to avoid possible danger or personal injury and property damages, appropriate
actions are to be taken; such actions have to bring the entire system into a secured con-
dition (e.g. by using a system for emergency stop, an emergency operation, monitoring of
critical values).

Please check the following points to avoid errors:

▶ Adaption of sensors to components of the electrical system / electronics, brake sys-

tem, engine and transmission control, chassis, body.

▶ Tap of one or several bus systems (CAN, LIN, ETHERNET) including the required elec-

trical connection(s) for data acquisition.

▶ Communication with the vehicle ECUs, especially with such of the brake system and/or

of the engine and transmission control (power train control system).

▶ Installation of components for remote data transmission (mobiles, GSM/GPRS

modems, WiFi and Bluetooth components).

IPETRONIK devices are designed for applications in extended tem-
perature ranges > 70 °C (158 °F). A high environmental temperature and
the module’s self-heating may cause injuries of the skin when touching the
hot surface. In order to avoid the risk of injury we recommend to take care
for appropriate safety precautions (e.g. contact protection, cov-
ering/enclosure, warning sign, ... ).

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

3

4. Before using the data directly or indirectly acquired by an IPETRONIK measurement sys-

tem used with vehicle ECUs, please review the data regarding plausibility.

5. With regard to the application of  IPETRONIK products in vehicles during use on public

roads the manufacturer and/or registered user of the vehicle has to ensure that all changes/-
modifications have no influence concerning the license of the vehicle or its license of oper-
ation.

6.

In case the user does not agree with the instructions and regulations as mentioned above,
he has to notify this expressly and immediately in writing to IPETRONIK before confirming
the sales contract.

2.2 General Information

2.2.1 About This Manual

This manual describes the application and usage of PlugIn_Protocol.

© 2025 All rights reserved!

2.2.2 Legend of the Icons

Attention!

This icon indicates important information to avoid possible error messages.

Danger

This icon indicates possible danger to the user.

Heat

This icon indicates possible heat that might hurt the user.

High voltage

This icon indicates high voltage that might hurt the user.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

4

Caution

This icon indicates caution to easily damageable devices.

Information

This icon indicates additional information for a better understanding.

Hint

This icon indicates a hint.

Important

This icon indicates important content.

Example

This icon indicates an example.

End of life

This icon indicates the end of life of a device.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

5

3 PlugIn Overview

3.1 PlugIn description

The Protocols PlugIn is supporting the measurement of traffic and bus networks protocols. A
large range of different hardware interfaces from various vendors is supported. The PlugIn can
measure bus network data, but you can also send traffic data to your network and ECUs. The
IPEmotion software is providing instruments and function for traffic analysis and traffic gen-
eration and output.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

6

3.2 PlugIn installation

In order to use the PlugIn together with IPEmotion you need to install it. The PlugIn is available
for download from the IPETRONIK website: https://www.ipetronik.com/. When you have
installed the PlugIn, you need to launch the IPEmotion software. Then you need to access the
application menu and open the OPTIONS. In the OPTIONS you can activate the PlugIn as indic-
ated below.

Figure 3.1 - PlugIn Activation

▶ The PlugIn is supporting 64 bit windows operating systems

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

7

3.3 Overview of supported vendors

Within the PlugIn a large rang of hardware interfaces is supported from different vendors, to per-
form you network measurements. The list of vendors and devices is continuously growing. If
your specific vendor or interface is missing, please contact our support to see if the imple-
mentation is possible in the oncoming releases.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

8

3.4 Detailed list of vendors and devices

Vector VN1670 and VN89xx devices can now be used via Ethernet connection
in addition to USB.

Vendor

IPETRONIK

ETH Gateway

Device Name

M-Gateway 3

IPEhub2

IPEcan FD

IPEcan FD PRO

IPEcan

IPEcan PRO

CLFD V1.1

CLFD V1.2

CAN FD Satellite

FlexRay Satellite

LIN Satellite

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

9

Vendor

VECTOR

Device Name

CANcardXLe

CANcardXL

CANcaseXL

CANboardXL

CANboardXLcompact

CANcardX

VN1530

VN1531

VN1610

VN1611

VN1630

VN1640

VN1670

VN5610

VN5610A

VN7570

VN7572

VN7600

VN7610

VN7640

VN8900

VN8950

VN8970

VN8972

VX0312

VX1121

VX1131

VX1135

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

10

Vendor

Kvaser

Kvaser

Softing

Device Name

LAPcan

PCIEcan

PCcan

PCIcan

PCIcan II

USBcan II

Leaf II

Leaf

PCIcanx II

Memorator Professional II

MemoratorPro

Memorator Light

USBcan Pro 5xHS

USBcanPro

USBcan Light

Ethercan

BlackBird

BlackBird V2

Hybrid

U100

DIN Rail SE410S-X10

CANcard2

EDICcardC

EDICcard2

CAN-Acx-PCI

CAN-Acx-PCI/DN

CANusb

CAN-PROx-PCI

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

11

Vendor

PEAK

ICS

DREWTECH

I+ME ACTIA

ETAS

Device Name

PCAN-USB X6

PCAN-PCI

PCAN-PCIe

PCAN-PCIe FD

PCAN-M2 FD

ValueCAN

ValueCAN3

ValueCAN4

ValueCAN4-4

Mongoose

Basic+24 XS

ES523

ES132

ES581

ES582

ES593

ES595

Ethernet System

Ethernet System

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

12

4 PlugIn configuration

4.1 Functional architecture

The following diagram shows the schematic system architecture when you would like to perform
network traffic and protocol measurements. You need the IPEmotion software and the cor-
responding Protocols PlugIn. Also you need to install the hardware drivers for your specific inter-
faces. For IPETRONIK interfaces the drivers are included in the setup and installed
automatically.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

13

4.2 Creating interface systems

In order to start your measurement, you need to change to the SIGNALS work space and select
the Protocols PlugIn from the hardware system drop down box. After that you need to create a
hardware interface system form the list of devices.

When the systems are manually created you have to enter device serial number or IP-address
to establish a connection for your measurement.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

14

Some devices support automatic hardware detection. In this case you do not need to create the
systems manually. You can use the detect function from the ribbon.

▶ The PlugIn might not support the same set of functions which are avail-

able through the vendors own software platforms.

▶ This can have several reasons, e.g. that the provided programming API
from the vendor is not offering all functions to external developers.
Another reason can be that IPETRONIK did not implement the function.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

15

5 Device specific configurations

5.1 IPEhub2 specific functions

The cable sets to interface IPEhub2 to the PC and the M-CAN modules on CAN2 or to the CAN
bus network via the SUB D9 interface are presented below:

The IPEhub2 device can be detected automatically over the LAN interface. The devices running
a DHCP server and when your LAN network interface of the PC is configured for automatic IP-
address you can directly detect it.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

16

The IPEhub2 device firmware is installed in the following directory of the Protocols PlugIn

▶ C:\Program Files\IPETRONIK\IPEmotion PlugIn Protocols V03.xx.xx\IPEhub2

The firmware update function is only available when you have detected the IPEhub2 device over
the LAN cable. Over WiFi connection the firmware update is not supported because the update
process is not stable.

Besides the firmware update you can access the web interface to configure the unit and you can
start and stop the data recording from the PlugIn. The web interface is also available from the fol-
lowing IP-address in your browser:

▶ IP-address to access web interface 192.168.232.1

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

17

5.2 ETHgateway-CLFD specific function

The cable sets to interface ETHgateway-CLFD to the PC and bus network are presented below:

The ETHgateway CLFD is supporting an automatic hardware detect provided the

IPETRONIK.IPEdhcpServerTool server tool is activated in the CAN-Server. The tool is available
in the following directory.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

18

▶ C:\Program Files\IPETRONIK\IPETRONIK CAN-Server V02.xx.xx (x64)\IPETRONIK.IPEd-

hcpServerTool.exe

The ETHgateway CLFD is not supporting an internal DHCP server, therefore an external DHCP
server tool is required to assign the device a fixed IP-address in order to be automatically detec-
ted by the PlugIn. You need to activate the Server Tool by checking the Active check box and
you need to use the SET operation to assign the IP-address to the ETHgateway. The SET func-
tion needs to be executed after you have defined a fixed IP-address to your PC network card.

5.3 CAN FD Satellite

The cable sets to interface CAN FD Satellite to the PC and bus network are presented below:

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

19

5.4  FlexRay Satellite

The cable sets to interface CAN FD Satellite to the PC and bus network are presented below:

5.5  LIN Satellite

The cable sets to interface LIN Satellite to the PC and bus network are presented below:

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

20

6 Measurements on CAN FD, LIN, ETH, FlexRay interfaces

3rd Party Data Acquisition System Integration - DBC & A2L Export and Import: https://www.y-
outube.com/watch?v=dTE7ymj3ho8

The interface hardware (CAN/LIN interface or Network card) may supports or several of the fol-
lowing functions. The supported functions are also depending on if you are using the Protocols
PlugIn of IPEmotion.

▶ CAN - Free running

▶ CAN - CCP and XCP (1.4 packed mode)

▶ CAN - Traffic

▶ CAN - J1939

▶ CAN FD - Free running

▶ CAN FD - XCP (1.4 packed mode)

▶ CAN FD - Traffic

▶ CAN FD - UDS Diagnostics

▶ LIN - Free running

▶ LIN - Traffic

▶ FlexRay - Free running

▶ FlexRay - Traffic

▶ FlexRay - XCP

▶ ETHERNET - Free running (TCP and UDP)

▶ ETHERNET - SOME/IP

▶ ETHERNET - Status and statistics

▶ ETHERNET - Traffic

▶ ETHERNET - PLP devices (Probe Logger Protocol - Technical, Automotive Ethernet)

▶ ETHERNET - WWH-OBD

▶ ETHERNET - DLT - Diagnostic Log and Trace

▶ ETHERNET - DoIP Diagnostic over IP

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

21

6.1 Description file import format overview

In order to measure data from your bus networks and ECUs you need to perform a description
file import. The available import functions and file formats are deepening on the selected inter-
face type. The screen shot below shows as an example import dialog and files for a CAN con-
nector.

On the CAN interface the following import formats are supported:

Figure 5.1 - CAN Import format

▶ CAN db (.dbc, .xml)

▶ J1939

▶ Autosar (.arxml)

▶ A2L (.a2l) with Seed & Key .skb support

▶ Fibex (.xml)

▶ UDS Diagnostic (.pdx, .idf)

▶ UDS Signals (.pdx, .xml)

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

22

▶ GM-LAN (.odx)

▶ CAN-Send (switching formats into output direction)

On the LIN interface the following import formats are supported:

Figure 5.2 - LIN Import format

▶ LDF db (.ldf)

▶ CAN db (.dbc, .xml)

▶ Autosar (.arxml)

▶ UDS Diagnostic (.pdx, .idf)

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

23

On the FlexRay interface the following import formats are supported:

Figure 5.3 - FlexRay Import format

▶ Autosar (.arxml)

▶ A2L (.a2l)

▶ FlexRay Parameter (.xml)

▶ Fibex (.xml)

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

24

On the ETHERNET interface the following imports are supported:

Figure 5.4 - Ethernet Import format

▶ Autosar (.arxml)

▶ A2L (.a2l)

▶ A2L zipped (.zip)

▶ Fibex (.xml)

▶ UDS Diagnostic (.pdx, .idf)

▶ UDS Signals (.pdx, .xml)

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

25

6.2 CAN interface

The CAN interface setting can vary in regard to the selected CAN hardware. The CAN hardware
can be one of the supported vendors like VECTOR, KVASA, PEAK, etc. or an IPETRONIK data
logger. On the General interface tab sheet you have the following settings.

Active

Activate the interface

Name

Default channel name

Description

Add an additional description to the interface

Reference

Is automatically generated by the system and stored in the data file to
back reference the data source.

On the CAN tab sheets the following settings are supported:

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

26

Baud rate

Here you can define the baud rate of the CAN bus

Send ACK
mode

With an active check box for normal mode the CAN interface is operating
in silence mode. The interface will not send any acknowledgment mes-
sages to the bus in order to avoid any disturbances on the bus network.

CAN FD

This check box can only be activated, when the CAN interface supports
CAN FD messages which are based on 64 bit message size.

Data rate

This reference to the CAN FD data rate.

Sample

Is relevant for CAN FD measurement and is usually taken from the

point

description file during the import process.

Sync jump

Is relevant for CAN FD measurement and is usually taken from the

with

description file during the import process.

The Option tab sheet provides the following settings.

Baud rate ini-
tializing

With this check box setting the baud rate of the CAN controller is
updated to the setting defined on the previous CAN tab sheet.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

27

Output mode

Off – no impact. Configuration – provides extended output messages
in the message window about the ECU communication.

The CAN interface support wider range of functions which will be discussed below.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

28

Diagnostics
J1939

Diagnostic messages

Status

This refers to CAN interface status channels

Traffic

With this channel you can perform CAN bus traffic measurements.

Manual mes-
sages

Here you can create manual CAN messages.

WWH-OBD

This refers to world wide harmonized OBD measurements.

OBD-2

With this interface a large grange of on board diagnostic channel
(OBD) are created which are accessible on almost all cars via the
OBD connector.

OBD-2 exten-
ded mode

This covers a special OBD mode.

GM-LAN

This covers a special GM diagnostic mode.

GM-LAN job-
based

This covers a special GM diagnostic mode.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

29

The overview of the CAN status channels is presented below.

6.3   LIN interface

The LIN interface has the following General configuration functions:

Active

Activate the interface

Name

Default channel name

Description

Add an additional description to the interface

Reference

Is automatically generated by the system and stored in the data file to
back deference the data source.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

30

On the LIN tab sheet the following settings are supported:

Baud rate

 From the drop down list you can select from 3 different baud rates
defines as: 19.2, 9.6, 4.8, 2.4, 1.2 kBaud

LIN version

The LIN version refers to the standards 1.3, 2.0 and 2.1/2.2.

Mode

 Here you define Master, Salve or Listen mode.

Send go-to-
sleep on
Stop

The function allows the go-to-sleep command to be sent to all nodes
when acquisition is complete and master mode is enabled.

The LIN interface of IPEmotion supports functions which will be discussed below.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

31

Status

Indication of the LIN interface status.

Traffic

With this channel you can perform LIN bus traffic measurements.

Manual mes-
sages

Here you can create manual LIN messages similar to CAN messages
discussed above.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

32

The sample rates of the measurement signals are calculated on import from the LIN schedule
table. The LIN schedule table shows the IDs and the delays between requests for data from dif-
ferent IDs.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

33

6.4 ETH interface

The ETH interfaces on an IPEmotion support the following main functions:

Status

Ethernet interface statistics.

Traffic

With the traffic channel you can record ETH traffic.

PLP Devices

The Technical Automotive Ethernet devices of the latest generation CM
100 and 1000 HIGH (Capture Modules) are supported using the PLP
(Logger Probe Protocol).

WWH-OBD

World Wide Harmonized-OBD.

DLT

Diagnostic Log and Trace.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

34

The ETH node has the following General configuration functions:

Active

Activate the interface

Name

Default channel name

Description

Add an additional description to the interface

Reference

Is automatically generated by the system and stored in the data file to
back reference the data source.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

35

6.4.1 ETH Status channels

On all ETH / LAN and PC interfaces status channel can added to monitor the interface status.
This statistics about the ETH bus load, link speed, bytes, packets, error etc.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

36

6.4.2 ETH Traffic

For the ETHERNET Traffic measurement on the PC, you need to define the name of the LAN
card of the PC which is PC dependent. This configuration is not required for data loggers where
the ETH interface names are pre-defined by the hardware setup of the system.

If you like to perform Ethernet traffic measurements on the Ethernet interface of your computer,
you must identify the Ethernet port name. For this you need the help of IPETRONIK support. To
identify the ETH name you need to open windows PowerShell. Within the program you run the
command:

▶ wmic nicconfig get ServiceName,description,macaddress,settingid

The IP address can also be used as a network name.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

37

The following screen shot indicates the windows PowerShell software to extract the detailed
names of all Ethernet network interfaces.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

38

6.4.3 Satellites for CAN FD, LIN, FlexRay

On the General interface tab sheet you have the following settings.

Active

Activate the interface

Name

Default channel name

Description

Add an additional description to the interface

Reference

Is automatically generated by the system and stored in the data file to
back reference the data source.

On the CAN tab sheets the following settings are supported:

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

39

Baud rate

Here you can define the baud rate of the CAN bus

Send ACK
mode

With an active check box for normal mode the CAN interface is operating
in silence mode. The interface will not send any acknowledgment mes-
sages to the bus in order to avoid any disturbances on the bus network.

CAN FD

This check box can only be activated, when the CAN interface supports
CAN FD messages which are based on 64 bit message size.

Data rate

This reference to the CAN FD data rate.

Sample

Is relevant for CAN FD measurement and is usually taken from the

point

description file during the import process.

Sync jump

Is relevant for CAN FD measurement and is usually taken from the

with

description file during the import process.

The Option tab sheet provides the following settings.

Baud rate ini-
tializing

With this check box setting the baud rate of the CAN controller is
updated to the setting defined on the previous CAN tab sheet.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

40

Output mode

Off – no impact. Configuration – provides extended output messages
in the message window about the ECU communication.

Device information about the firmware is available.

With the update function the device firmware can be updated with progress bar information.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

41

6.4.4 PLP Devices - Automotive Ethernet

To measure automotive Ethernet networks the following interfaces from Technical Engineering
are supported:

▶ Technical CM 100 High

▶ Technical CM 1000 High

▶ Technical CM LIN Combo

▶ Technical CM CAN Combo

▶ Technical CM Ethernet Combo

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

42

The system architecture below provides an overview of the ETHOS and other loggers with Eth-
ernet ports can be used to store the automotive Ethernet data.

6.4.5 WWH-OBD

The WWH-OBD (World Wide Harmonized on Board Diagnostics) protocol is now supported on
the ETH connector. The protocol is also supported on CAN.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

43

6.4.6 DLT Diagnostic Log and Trace

On the Ethernet ports of the logger and the PC using the PROTOCOLS PlugIn the diagnostic
log and trace protocol from AUTOSAR is supported. The DLT protocol is used in the devel-
opment phase of an ECU. It is assumed to use an external logging- and tracing tool to store the
debug information generated by the ECU.

On the DLP interface node the ECU connection IP-address settings and the log level is defined.
For the IP-address setting you can chose between IPv4 and the IPv6 standard.

For the measurement, 2 status channels for the communication status and the start trigger are
provided. The message channel will record the log information.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

44

6.5 A2L import - DAQ list with graphical filling level indication

Measurements on ECUs can easily reach the performance limits if many measurements are
required. With this graphical import and filling level indication overview you can now clearly
identify which signals are measured and which signals are rejected. To activate the DAQ list
filling level indication, you have to add the DAQ list from the column chooser to your channel
grid as shown below.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

45

Then you will see a new button to open the graphical DAQ filling level indication.

When you open the graphical filling level indication you will see how the signals are allocated to
the Data Transfer Objects (DTO). The number of supported DTO’s is defined by the A2L file. In
one DTO row you can have several signals. The color is randomly selected and is a visual aid
showing how many byte a signal is utilizing from a DTO.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

46

6.5.1 DAQ list filling process

The import dialog fills the DAQ list in an optimized way in order to use as much of the available
capacity as possible. The maximum capacity for signal measurement of a DTO is 7 byte for CCP
measurements and XCPonCAN. The first byte is used for the address header.

Example 1:

In comparison of you take an A2L file and measure XCPonETH on the Ethernet interface of
IPETRONIK data loggers like M-LOG have a lot more byte capacity on the DTO. The number of
available bytes is defined in the A2L file. In the screen-shot below you can see the import dialog
and the DTO fill level for an XCPonETH measurement with 60 byte capacity on each DTO.

Example2:

In the screen-shot below you can see that 4 DTOs are used for four 32-bit signals It is not pos-
sible to fill 2 signals of 32-bit signals in one 7 byte DTO.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

47

Example 3:

In the following example, 3 additional 8-bit signals are activated. Now you can see that the IPE-
motion software automatically fills up the 3 empty bytes on the first DTO (Data Transfer Object).

The allocation of signals to DTOs is optimized by IPEmotion, internally. It can-
not be influenced by users. Some A2L files support the reading of multiple sig-
nals from one common DTO address. In this case several signals are allocated
to the same DTO address and the mouse over tip text is indicating all channels
grouped together in this DTO

6.5.2 DAQ list overflow – rejected signal export

If you activate more channels than the DAQ list is able to support, you can create a list of rejec-
ted channels which can be exported to CSV. With the mouse over function you can read the
channel names which are included in the DAQ list.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

48

6.6 Edit A2L dynamic DAQ list ODT values during the import

When you import an A2L file for dynamic DAQ list measurements e.g. for XCPonCAN on your
ECU the import dialog considers by default the maximum ODT count = 252. (ODT = Object
Descriptor Table). The DAQ list fill level calculation is based on the default assumption that the
252 ODT can be serviced by the ECU.

In practice the user tend to overload the dynamic DAQ list why adding to many ODT. This prob-
lem can be solved in the way that the user can define in the import dialog the appropriate values
for the MAX ODT and MAX ODT entries to calculate the fill level correctly.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

49

If you now like to calculate the DAQ list fill level correctly you must correct the values for MAX
ODT and MAX ODT Entries. In order to do this you can take a template file from the following dir-
ectory:

▶ C:\ProgramData\IPETRONIK\IPEmotion 20xx Rx RC\Template\DaqListXcpCan.xml

This file has to be transferred into the following directory:

▶ C:\ProgramData\IPETRONIK\IPEmotion 20xx Rx RC\Template\DaqListXcpCan.xml

You need to close IPEmotion and edit the XML file and set the values for Max ODT and max
ODT Entries for read only into ”FALSE”.

With this setting in the XML file you are able to modify the ODT setting in the import dialog.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

50

In the example above the MAX ODT count was set to 10 and the fill level calculation is now con-
sidering this value.

6.6.1 A2L Import for array signals

The A2L import is supporting array signals. Array signals are basically grouping several meas-
urements together to one channel. In order to import the array signals you need to add in the
import dialog from the column chooser the field “Divide array” to the channel grid.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

51

When the array column is included in the channel grid, you can activate the check boxes which
include array signals.

After the import the array signals are all listed and available for measurement.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

52

When the A2L file includes array signals you can import specific signals with a CSV file selec-
tion. The standard process is that the complete array is imported. However, if you like to import
only specific signals from the array the CSV file selection is only possibility. In the CSV file you
define array signal name and the ID in brackets.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

53

6.6.2 A2L import with additional FlexRay parameters import

For FlexRay measurements you need to create a FlexRay interface. For IPEmotion RT and PC
based FlexRay measurements a FlexRay Satellite Interface is available.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

54

When you have an A2L description file for a FlexRay protocol measurement and the A2L is not
including any FlexRay parameter the import process will open automatically a file open dialog to
load the parameter file.

Import dialog to select the FlexRay signals.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

55

When the FlexRay parameter file as defined in the A2L is not available a second import dialog
will be opened automatically.

New dialog, to select FlexRay parameters.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

56

6.6.3 A2L import from zip files (X-Modules)

When X-Modules are configured on the ETH interface in the logger or on the PC with the
IPETRONIK PlugIn X the export function is creating one ZIP file which includes all A2L files of
each X-Module.

Figure 5.5 - Export A2L

The dedicated import of A2L ZIP format is then automatically importing all A2L files to create
the configuration. On the activated channels are included in the A2L file.

Figure 5.6 - Import A2L

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

57

6.6.4 XCP, CCP second tester

In the extended tab sheet, the second tester configuration for the CCP and XCP protocols on
the different layers (CAN, CAN FD, FlexRay, UDP, TCP) can be configured. A second tester is
defined as a second software program accessing an ECU while it is communicating with the
data logger.

To avoid communication conflicts between data logger and the second tester Ecu calibration
software, the logger provides specific functions to handle the parallel communication to the
ECU. The second tester software has a higher priority and established a connection and causes
a disconnect of the data logger. However, with timeout settings and reconnect settings the log-
ger can re-establish a connection after the second tester is disconnected or inactive. If the con-
nection between logger and ECU is interrupted due to a detected second tester, the next
connection attempt by the logger within this session is not done before this timeout expired.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

58

If the connection between logger and ECU is interrupted due to a
detected second tester, the next connection attempt by the log-
ger within this session is not done before this timeout expired.
The time out value is defined in seconds. The timeout is deac-
tivated when the value is set to 0 s. This is displayed as OFF. If
the If the Second Tester Retry Timeout is deactivated, the time
defined for Second Tester Timeout"will cyclically check, if a
second tester can be detected.

Example: ”Second Tester Timeout”: 5s ”Second Tester Retry
Timeout”: Off If a second tester is detected within the first 5
seconds, the system will immediately wait another 5 seconds
while searching for a second tester again. This continues as long
as a second tester is detected.

The input field ”Second Tester Retry Timeout” is inactive when
Second Tester Timeout"from above is set to OFF". The retry
timeout is deactivated when the value is set to 0 s. This is dis-
played as OFF. The retry timeout can be defined in the range of 0
. . . 3600 s. The step width is 30 s. Valid input data is e.g. 0 s, 30
s, 60 s, 90 s etc. If the Second Tester Retry Timeout is activated,
the time defined for ”Second Tester Retry Timeout” is cyclically
checked, if a second tester can be detected. An activation of the
”Protocol Trigger” resets the waiting time of ”Second Tester
Retry Timeout”

Here you can enable that an ECU firmware synchronization. With
this check box enabled, a new ECU firmware can be syn-
chronized from the data logger to the ECU via the IEV firmware
container. The IEV file can be created from an export function in
the SIGNALS workspace.

Here you define how often an ECU reconnect will be attempted.

Second Tester
Timeout

Sec. Tester Retry
Timeout

Firmware syn-
chronization

Max. reconnect
attempts

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

59

6.6.5 XCP transport layers

The A2L import for the XCP protocol supports different transport layers. The latest layer imple-
mented is based on CAN FD. CAN FD can only be selected when it is defined in the A2L file.

Figure 5.7 - Protocol Layers selection

When CAN FD is selected in the import dialog above the following dialog appears where addi-
tional protocol settings from the A2L file can be modified, when needed.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

60

6.6.6  XCPonETH for IPv6

The IPv6 IP-address standard was implemented on the XCPonEthernet measurement oper-
ation. The IPv6 IP-address range is much larger as the IPv4 address range and becomes more
important to handle the growing number of network devices.

When importing A2L or ARXML files including IPv6 IP-address they are supported, and the IP-
address is visible in the import property dialog.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

61

6.7 A2L export with pre defined DAQ list

The XCP (CAN, CANFD, FlexRay, TCP, UDP) protocol tab "Extended" has a parameter "Export
A2L" . When the parameter "Export A2L" checkbox is active, the configuration will be exported
to disk on measurement start (depending on trigger configuration).

▶ IPEmotionPC exports the A2L file to the A2L directory in the configured custom directory.

▶ IPEmotionRT exports the A2L file, which is included in the Ziprt container of the relevant

measurement.

The file name of the A2L file is the name of the protocol node plus "_IPE" and the extension
".a2l". An existing A2L file will be overwritten by a new export.

Only active non-polling DAQ lists with at least one configured and active signal
will be exported to the A2L file.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

62

6.8 FIBEX import

6.8.1 Import CAN signals from FIBEX files

You can import on all PlugIn supporting CAN interfaces for CANdb measurements a FIBEX file.
When the FIBEX file includes CAN messages it is an adequate replacement for the DBC file.

The import dialog is indicating in the protocol header ”Free running”.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

63

After the import you see you CAN messages and the channel.

6.8.2 Import CAN FD signals from FIBEX files

The FIBEX XML file is supports CAN FD protocol imports.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

64

6.8.3 Display of Sender name for FIBEX, DBC, AUTOSAR messages

The import properties of the CAN, FIBEX and AUTOSAR messages include now the sender
name when defined in the description file.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

65

6.9  Description file import with CSV file for channel reference

The CSV reference file significantly improves the description file import and channel activation.
Especially when you are working with large description files with many channels, sometimes
you are uncertain if all required channels are included in the description file. It is also time-con-
suming to search and activate only the relevant channels for your specific measurement manu-
ally.

With the CSV reference file you can compare your description file to a CSV channel list. This
comparing process covers two functions:

▶ All matching channel names from the CSV reference list are automatically activated. This

saves a lot of time compared to activating channel by channel. The channel selection is not
cases sensitive. Channels are selected even when the lower and upper cases do not
match.

▶ All the channels which are included in the CSV file but not in the description file are listed in
a separate ”missing channels” list. Missing channels can be saved in a separate CSV file
for later analysis purposes.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

66

Channels are selected even when the lower and upper cases do not match.

A second filter criteria can be added to the CSV file to optimize the import

e.g. to specify sample rate or DAQ list settings in the import process.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

67

6.9.1 Multi column CSV selection for description file imports (DBC, A2L)

The CSV filter can support additional columns apart from the channel name to select dedicated
channels in your description file import. In the example below you see how a DBC import can be
improved by adding the message name as a second selection criteria.

In this example we define only the channel names as selection criteria. In this case duplicate
channels across the whole DBC file get selected during the import process.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

68

If you add the message ID to the selection criteria in column 2, you can pick the specific chan-
nels of the messages you are interested in.

If you like you can set during the DBC import the sample rate by message ID too.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

69

The sample definition can be located on column 2 also. It is not required that the sample rate
definition must be located on column 3 at any time.

When you are using CSV filter for A2L import you can select channels by channel name in the
first column and associated to the signal a DAQ list or sample rate during the import too.

6.9.2 Check duplicate channel names during description file import

When run an import of any description file (DBC, FIBEX, A2L) the import process can check for
any duplicate channel name and provide a dialog to resolve duplicate channel name conflicts.

In order to activate this feature you have to make an additional entry in the Settings.XML file.

▶ C:\ProgramData\IPETRONIK\IPEmotion 20xx Rx\Settings.XML

The new entry in the XML file should be:

<ImportSettings>

<checkForDuplicateSignalNames>True</checkForDuplicateSignalNames> <ImportSettings>

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

70

With the new entry in the Settings.XML file the import dialog will guide you to a new dialog high-
lighting all duplicate channels out of the selected channel list. There are to functions available in
the drop down list:

Accept duplic-
ates

With this function you accept the duplicates and confirm them

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

71

Rename sig-
nals

When you select the rename function you have to edit the channel
names in the grid

Apply column chooser to get information about the channel reference.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

72

When all duplicate conflicts are resolved the import can be finalized and all channels are
renamed.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

73

6.10 Description file import with INCA LAB file

To support the workflow between INCA and IPEmotion measurements an INCA experiment
(LAB-file) import is supported besides the CSV import. You can save part of your INCA exper-
iment in the LAB file format. This LAB file can be used to create easily the same measurement
configuration for IPEmotion.

All description file imports on all PlugIns support the CSV and LAB file filter.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

74

After you have imported your complete description file you can use the CSV and LAB reference
to select only those channels which are relevant for your measurement application.

When the LAB file was selected the associated channels from the description file are auto-
matically activated in the import dialog. A message box is also returning all channels which are
included in the LAB-file and missing in the description file.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

75

6.11 Synchronization of description files

You can use the description file synchronization function to compare your existing meas-
urement configuration against a new description file. The description file synchronization is use-
ful to get a direct view about the differences between a new ECU description file and your
current measurement configuration. The following file formats are supported for syn-
chronization:

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

76

The default setting of the file synchronization is based on message ID and message name. In
the standard setup the description file is compared on Message ID and channel name. When
one of two parameters is different, the synchronization will not take place and you will get a noti-
fication in the message window. The standard synchronization behavior can cause an additional
workload when e.g. a channel is switched to a different message ID because then the syn-
chronization does not take place and the related links to the VIEW instruments and formulas or
storage in the ACQUISITION work space etc. is removed as well. In the following example the
default synchronization behaviour is presented by selecting the synchronization function on
description file level.

In the next step you select the description file you like to compare against and the processing
treatment operation. Here you can enable a message window to get an overview of the dif-
ferences detected and how to treat the differences. In this example we will get an message win-
dow to see the differences. The treatment deleted is: Deactivate the channels which cannot be
synchronized

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

77

The message popup window is now indicating that the channel Exhaust1 could not be syn-
chronized and was therefore accordingly to the treatment operation was deactivated.

The configuration is now indicating the deactivated channel Exhaust 1.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

78

With the EXPERT setting ”Synchronize signals by name” the synchronization mechanism is
focusing only on the channel name and not any more on the message ID and channel name
together. The benefit for the user is that the synchronization will take place and the links to the
VIEW instruments etc. remain intact to display online data.

The screen-shot below in indicating on the right hand side, that the channel Exhaust 1 was suc-
cessfully synchronized even so that it is included on a different CAN message ID.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

79

6.12 J1939 Diagnostics

For J1939 features refer to : https://youtu.be/dyqk3jh2V5c

You need to select on your CAN interface of your CAN card or data logger the J1939 diagnostic
function. In order to use the J1939 protocols function on a logger a licence is required.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

80

The J1939 import dialog provides a list of over 3000 default channels defined in the standard.
With the bus scan functionality, you can identify which channels are available on the connected
ECU. The default CAN bus baud rate is set during the bus scan to 250 kB.

When the bus scan is performed the available channels are activated.

When you start the measurement the actual messages and channel readings are displayed.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

81

On the J1939 interface you can select diagnostic messages too.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

82

When the channel is activated you select from a wide range of components. The DM1 channel is
created by default.

▶ DTC: 1, 2, 6, 12, 23, 27, 28, 35, 41, 42, 43, 44, 45, 46, 47,48, 49, 50, 51, 52

▶ Clear DTC: 3, 11

▶ DM 4, 19, 24, 25, 29, 31

▶ Multiplexed signals are supported too

The readability of the data in the channel is very limited. Therefor a dedicated diagnostic instru-
ment is available.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

83

6.12.1 Using J1939 DM1 error codes as trigger

DM1 error codes can be used as triggers for measurements. In the event that a DM1 message is
received, the error codes included in this message will be incorporated as values in the new sig-
nal, with all error codes having the same timestamp.

The J1939 DM1 message signal remains unchanged.

DM1 signal displaying 3 SPNs with FMI and OC as below in grid:

Address SPN SPN name

FMI FMI text

OC

27

27

27

97 WaterInFuelIndicator

3

3820 RearAxleGroupEngagementStatus 15

532 EngineSpeedAtHighIdlePoint6

2

9

Voltage Above Normal, Or Shorted To
High Source
Data Valid But Above Normal Oper-
ating Range - Least Severe LevelSAE
J1939-73 Revised FEB2010 Page
134 of 172
Data Erratic, Intermittent Or Incorrect 6

5

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

84

6.13 UDS Diagnostics

On CAN and ETH interfaces you can run UDS diagnostic measurements.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

85

The .PDX and .IDF import file format is currently supported.

The PDX file can contain several software versions. You need to select the one relevant for the
ECU in place.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

86

In the last stage you reach the jobs and service configuration dialog. This dialog consists of 4
distinctive areas with different functions.

Area 1

This includes all diagnostic services provided by the PDX file.

Area 2

Here you define the job sequences. You can have several sequences and
trigger them individually.

Area 3

Here you drag and drop the service you like to execute.

Area 4

Here you can define for some specific jobs which require a output values the
corresponding parameter to get data back from the ECU.

In this example a sob sequence with several service is configured. Within a job sequence the
service can operate in different modes.

▶ Start of measurement

▶ End of measurement

▶ Cyclic and Start of measurement

▶ Cyclic and End of measurement

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

87

When you have activated in OPTIONS > EXPERT MODE > View Diagnostics Jobs, you can see
all configured job sequences and the selected services. For each service a list of channels for
PR = positive responses and NR = negative responses is listed.

6.13.1 Using UDS DTCs error codes as trigger

UDS DTCs error codes can be used as triggers for measurements. In the event of a UDS DTC
message is received, the error codes included in the message will be incorporated into the new
signal, with all error codes having the same timestamp.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

88

The actual UDS message signal remains unchanged.

DTC error code value may not be visible in the View tab. However, you can find it in the Signals
tab.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

89

6.14 OBD-2 diagnostics

On all CAN interfaces you can measure data from the standard OBD-2 protocol to get standard
vehicle diagnostic information.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

90

When you activate the OBD-2 measurement over 200 standard OBD channels are created. You
can then activate the channels you require. Not all channels will provide data as this is vehicle
manufacturer specific.

Besides the standard OBD-2 channel you can activate additional components for measurement
as indcated below.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

91

With the user defined signals, you can request PID which are outside of the standard and not
available to the public. The identification and trouble code channels you can get additional
information too. With mode 4 you can use a trigger channel to clear fault codes.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

92

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

93

6.15 OBD-2 extended mode

The functionality of OBD extended mode is that you can define individual modes like mode 21,
22, 23 etc.

IPETRONIK PLUGIN_PROTOCOL - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION -03.12.00- | JULY 2025

94


