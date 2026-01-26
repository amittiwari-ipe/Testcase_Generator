IPEmotion PlugIn IPETRONIK X
USER MANUAL V02.21.xx

October 2024

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00

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

2 Safety Instructions and General Information

2.1 Safety and Warning Instructions

2.2 General Information

2.2.1 About This Manual

2.2.2 Legend of the Icons

3 Abbreviations

4 X-PlugIn Overview

4.1 X-PlugIn Description

4.2 X-PlugIn Installation

4.2.1 PlugIn Versions

4.3 X-PlugIn Activation

4.4 System Overview

4.4.1 System Architecture

4.4.1.1 Ethernet and CAN Card Interface Architecture

4.4.1.2 Ethernet and CAN Modules Daisy Chain Setup

4.4.2 Connecting Two X-Devices to PC

5 PlugIn Options

5.1 Plugin-specific Settings

5.1.1 Ethernet Interfaces Settings

5.1.2 CAN Interfaces Settings

5.1.3 Options Settings

5.1.4 Components Settings

6 Hardware Modules Integration

6.1 X-Modules

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

8

8

8

9

11

12

12

12

13

13

14

14

14

16

18

20

21

21

6.1.1 X-Modules Cable Length

6.1.2 Mx-SENS2 4 Fast

6.1.2.1 Input Cables:

6.1.3 Mx-SENS2 8

6.1.3.1 Input Cables:

6.1.4 Mx-STG2 6

6.1.4.1 Input Cables:

6.1.4.2 STG Operation Mode

6.1.5 Sx-STG

6.1.5.1 Input Cables:

6.1.6 Signal Input Modes

6.1.6.1 STG Mode

6.1.6.2 SENS Mode

6.1.6.3 ICP Mode

6.1.7 TEDS Class 2

6.2 M-Modules

6.2.1 M-Modules Cable Length

6.2.2 M-SENS2

6.2.2.1 Input Cables

6.2.3 M-SENS3 8

6.2.4 M-Thermo2

6.2.4.1 Input Cables

6.2.5 M-Thermo2 u

6.2.5.1 Input Cables

6.2.6 M-Thermo3 16

6.2.7 M-RTD2

6.2.7.1 Input Cables

6.2.8 M-CNT2

6.2.8.1 Input Cables

6.2.8.2 Input / Principle Details

6.2.9 CANpressure

6.2.9.1 Pressure Connections

6.3 Module Identification by Base Type Number

6.4 Connecting the X-Modules/Ethernet Modules

6.4.1 X-Modules Hardware Setup - Example 1

TABLE OF CONTENTS

21

22

24

25

26

27

28

30

31

32

33

33

36

38

39

40

40

41

42

43

45

46

47

48

49

51

51

52

53

54

57

57

60

62

62

6.4.2 X-Modules Hardware Setup - Example 2

6.4.3 X-Modules Hardware Setup - Example 3 (CAN Tunneling)

6.5 CAN Card Hardware Interfaces

6.6 Connecting the M-Modules/CAN Modules

6.6.1 M-Modules Hardware Setup - Example 1

6.6.2 M-Modules Hardware Setup - Example 2

6.6.3 M-Modules Hardware Setup - Example 3

6.7 Introduction to CAN-FD

6.7.1 CAN Bus Termination

6.7.2 Structure of CAN-FD Message

6.8 LED Indication

6.8.1 M-Modules LED Status

6.8.2 X-Modules LED Status

6.8.2.1 Channel LED Indication

6.8.3 System LED Status

7 Software Interface

7.1 IPEmotion Signals Work Space

7.1.1 Ribbon Main Functions

7.1.1.1 Detecting the Hardware

7.1.1.2 IPETRONIK X-PlugIn

7.1.1.3 System

7.1.1.4 Components

7.1.1.5 Firmware Update

7.1.1.6 Configuration Check

7.1.1.7 Import and Export

7.2 Configuration Adjust Functions

7.2.1 Database

7.2.2 TEDS

7.2.2.1 TEDS Sensor Detection with Automatic Unit Transformation

7.2.2.2 TEDS Adjust on Channel Level

7.2.2.3 Compare TEDS Sensor with Configuration

7.2.3 Offset Adjust

7.2.4 Shunt Check

7.2.4.1 Hotkey Operation: Offset Adjust and Shunt Check

7.2.4.2 Adding a Hotkey for Offset Adjust and Shunt Check

TABLE OF CONTENTS

62

63

64

67

68

68

69

70

70

71

75

75

75

76

77

78

78

78

78

79

80

81

81

84

85

86

86

86

88

89

90

91

93

94

94

7.3 Access

7.3.1 Detect

7.3.1.1 Mapping

7.3.1.2 Synchronize

7.3.2 Initialize

7.3.2.1 Reset

7.3.3 Display

7.3.3.1 Quick Analyzer

7.4 View

7.4.1 Details Area

7.5 System Tree

7.5.1 Column Chooser

7.5.2 Context Menu

7.5.3 M3 Module Order

8 X-PlugIn Interface Configuration

8.1 System Details Area

8.1.1 General Tab

8.1.2 Ethernet Hardware Tab

8.1.3 CAN Hardware Tab

8.1.3.1 Module Health Status Channels

8.1.4 Options Tab

8.2 Module Details Area

8.2.1 General Tab

8.2.2 Extended Tab (For CAN-Modules)

8.2.3 Extended Tab (For X-Modules)

8.2.4 Information Tab

8.2.4.1 Module License Update

8.3 Channel Configuration

8.3.1 Column Chooser in the Channel Grid

8.4 Channel Details Area

8.4.1 General Tab

8.4.1.1 Defining the List Box Entries of Channel Names

8.4.2 Format Tab

8.4.3 Scaling Tab

8.4.4 Scaling Calculator

TABLE OF CONTENTS

95

95

96

98

99

101

102

102

105

105

106

106

107

112

113

113

113

114

116

117

119

120

120

121

122

124

126

127

127

133

133

133

135

141

143

8.4.4.1 Channel Settings

8.4.4.2 2-Point Scaling

8.4.4.3 Free 2-Point Scaling

8.4.4.4 Factor/Offset Scaling

8.4.4.5 Multipoint Scaling

8.4.4.6 STG Strain Gauge

8.4.4.7 VTAB Ranges

8.4.4.8 VTAB

8.4.4.9 Active Sensors

8.4.4.10 Passive Sensors

8.4.4.11 Snapshot - Test Measurement

8.4.5 Sensor Database

8.4.5.1 Adding New Sensors to Database

8.4.5.2 The Database Format

8.4.5.3 Multipoint Linearization

8.4.5.4 Adding New Sensors

8.4.6 Terminal Tab

8.4.7 Display Tab

8.4.7.1 Define Standard Decimal Templates on Module Level

8.4.7.2 Output Tab for Output Channel

8.4.8 Extended (X-Modules and M3-Modules)

8.4.9 Excitation Tab

8.4.10 Thermo Tab (M-Modules)

8.4.11 Signal Filters

8.4.11.1 Hardware Filters

8.4.11.2 DSP Software Filters

8.4.11.3 Aliasing Effect

8.4.12 Filter Tab (X-Modules)

8.4.13 Filter Tab (M-Modules)

8.4.14 Data Output Tab (X-Modules)

8.4.15 Characterstic Curve Tab (X-Modules)

8.4.15.1 Configuring the Characteritic Curve

9 Technical Data

9.1 System Requirements

9.1.1 Minimum System Requirements

TABLE OF CONTENTS

143

145

145

146

147

148

149

150

151

151

152

153

153

155

159

160

162

164

166

167

168

168

169

170

171

171

171

172

172

173

174

174

175

175

175

9.1.2 Recommended System Requirements

175

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

2

2 Safety Instructions and General Information

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

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

This manual describes the application and usage of Device.

© 2024 All rights reserved!

2.2.2 Legend of the Icons

Attention!

This icon indicates important information to avoid possible error messages.

Danger

This icon indicates possible danger to the user.

Heat

This icon indicates possible heat that might hurt the user.

High voltage

This icon indicates high voltage that might hurt the user.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

5

3 Abbreviations

Abbreviations

Definition

CAN

CAN-FD

CNT

CMRR

DAQ

DSP

ETH

FPGA

FRQ

+FS

-FS

GND

IAW

ICP

IEPE

LAN

MPC

PWR

Controller Area Network

Controller Area Network - Flexible Data rate

Counter

Common Mode Rejection Ration

Data Acquisition

Digital Signal Processor

Ethernet

Field Programmable Gate Array

Frequency

Plus Full Scale

Minus Full Scale

Ground

IPEmotion App Workspace

Integrated Circuit Piezoelectric

Integrated Electronics Piezo Electric

Local Area Network

Measurement Point Catalog

Power

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

6

Abbreviations

Definition

PTP

RTD

STG

TEDS

VDC

Precision Time Protocol

Resistance Temperature Detector

Strain Gauge

Transducer Electronic Data Sheet

Voltage Direct Current

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

7

4 X-PlugIn Overview

4.1 X-PlugIn Description

IPETRONIK X is a PlugIn which is an extension comes along with the IPEmotion PC software
and supports to configure analog and digital measurement modules from IPETRONIK. With the
X-PlugIn you can configure the measurement modules over a CAN and the Ethernet interface.
The two main module lines are:

▶ CAN modules (M-Modules)

▶ Ethernet Modules (X-Modules)

Therefore two configuration interfaces CAN and Ethernet are supported for the product lines.
However, it is also possible to daisy chain CAN modules after the X-Modules. This setup is
called X-LINK and is explained in the further sections. The Modules can be operated with the
IPEmotion PC software and on the IPEmotion RT data logger software.

This manual provides detailed description, usage and features available in the IPETRONIK X
PlugIn in the further sections.

The IPETRONIK X PlugIn is only available for the IPEmotion PC software. There are
multiple PlugIns which you can activate in the PlugIns tab as per your need.

4.2 X-PlugIn Installation

In order to use the PlugIn together with IPEmotion first you need to install it. The PlugIn is avail-
able for download from the IPETRONIK website: https://www.ipetronik.com/en/products-ser-
vices/software-digitalization/plugins.html. The X-PlugIn is available as a 64-bit version and
requires minimum IPEmotion 2024 R2 and later versions to be supported. For system require-
ments, please refer to "System Requirements" on page 175.

Download the latest version available in the website.

The X-PlugIn supports the 64bit Windows operating systems.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

8

Once the PlugIn is downloaded, follow the instructions shown on the screen and complete the
installation.

Figure 4.1 - PlugIn IPETRONIK-X Installation

4.2.1 PlugIn Versions

If desired, you can switch to previous PlugIn versions in the drop down box. In the column "Ver-
sion" you will see the selected PlugIn version. If you select a PlugIn with an equal sign (=) you
define this PlugIn as your standard PlugIn and newer PlugIn versions will be ignored. If you use
a PlugIn without an Equal sign and you install a more recent version, it will automatically load to
the Signals work space.

Figure 4.2 - Signal Work Space

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

9

To verify and select the PlugIn installed versions, do as follows:

1. Once the installation is completed, start the IPEmotion PC software.

2. Access the File menu and navigate to the Options or you can click

icon on the Quick

Access Toolbar ribbon to access Options.

3.

In the Options → PlugIn window below the Version column, click

icon to view the

installed versions.

4. Select the PlugIn versions as per your requirement.

Figure 4.3 - PlugIn Installation

You can also download the latest version through the IPEmotion
software.

▶ The selected PlugIn version will also reflect on the Signals work space.

▶ (=) is indicating that this PlugIn is fixed and will not be automatically replaced when a new

PlugIn version is installed.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

10

4.3 X-PlugIn Activation

In order use the PlugIn, you need activate the PlugIn in the Options. To activate the PlugIn, do
as follows:

1. Go to File menu.

2. Select Options from the dropdown or you can click

icon.

3. Select PlugIns from the left-hand pane.

4. Activate the PlugIn IPETRONIK-X.

Figure 4.4 - X-PlugIn Activation

5. Click OK to confirm your selection.

6.

If you need to modify settings for the ETH or CAN interface, open the Plugin-specific
settings by clicking to the wrench tool symbol. For more details on Plugin-specific
settings, refer to "PlugIn Options" on page 14.

In order to operate the PlugIn IPETRONIK-X and IPETRONIK-CAN in
parallel, you need to disable the use of the CAN modules (through the CAN
interface) for the PlugIn IPETRONIK-X.

The PlugIn that are activated here is also loaded in the Signals work space to
use.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

11

4.4 System Overview

4.4.1 System Architecture

There are two main system architectures. You can operate the X-Modules based on an Ethernet
communication via your LAN port of your computer.
The other setup requires a CAN card interface from IPETRONIK like IPEcanPro FD or IPEhub2
or other supported vendors for the CAN modules.

4.4.1.1 Ethernet and CAN Card Interface Architecture

Figure 4.5 - Ethernet and CAN Card Interface Architecture

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

12

4.4.1.2 Ethernet and CAN Modules Daisy Chain Setup

The below setup is to combine Ethernet and CAN modules in one daisy chain. This setup
requires that the Ethernet modules are connected first to the PC and the CAN modules are
following the Ethernet modules.

Figure 4.6 - Ethernet and CAN Modules Setup

The most common and recommended hardware setups and the required cable sets will be
explained. Please refer to "Connecting the X-Modules/Ethernet Modules" on page 62 or "Con-
necting the M-Modules/CAN Modules" on page 67.

4.4.2 Connecting Two X-Devices to PC

By using two network adapters, a simultaneous operation of two independent X-systems
connected to one notebook / PC is supported. Please consider, that the IP ranges have to differ
from one another.

Proceed as follows:

▶ Connect the first system and define its IP range.

▶ Connect the second system and configure an IP range that is different from the first system.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

13

5 PlugIn Options

5.1 Plugin-specific Settings

When you access the Options → PlugIns window in the IPEmotion you can access the
advanced Plugin-specific settings and the Help Manual.
However other PlugIns will have other settings which are explained in the dedicated PlugIn
manuals.

Figure 5.1 - Plugin-specific Settings

5.1.1 Ethernet Interfaces Settings

Ethernet interfaces tab lets you to configure functions for the IP-address and the detection
mode. The ethernet and IP-address range settings are relevant for the X-Modules only.

Enable all

Performs the scan for module across all Ethernet interfaces of the PC.
This setting consumes more time.

Disable all

Will not allow any detection of the modules on an Ethernet port.

Selected

Here you will perform the scan only on a dedicated Ethernet port of the
computer.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

14

Figure 5.2 - Ethernet Interface - Detection Mode

If the Detection mode is set to Only selected Ethernet ports, the user can Enable only the
required one and also access to an advanced configuration dialog to change the IP-address
ranges of the modules. The setting in the advanced dialog should be handled with care as it has
an impact on the Ethernet interface of the computer and address of the modules.

If the address ranges are changed to match corporate IT network
requirements is might be possible that the modules cannot be detected any
more on another computer with different network settings.

Figure 5.3 - Ethernet Interface Settings

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

15

Once you set the IP address range, click OK to confirm and a dialog pops up confirming that the
command to set ranges is sent. To update the firmware version of the X devices, please refer to
" Firmware Update " on page 81.

Figure 5.4 - Confirmation

5.1.2 CAN Interfaces Settings

The CAN interface settings are relevant when you work with the CAN modules. With the setting
in this dialog you have an impact on the detection process.

Figure 5.5 - CAN Interface Settings

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

16

▶ CAN hardware detection interfaces: Allows you to select the detection mode for

CAN hardware detection.

Enable all

Will perform the scan for module across all CAN
interfaces detected by the PC. The supported
CAN interfaces are managed in the CAN server.
A list of the vendors and devices is provided
in section 7.5. The full scan will take more time.

Disable all

Will not allow any detection of the modules on a
CAN card.

Only selected

Here you will perform the module scan on the
dedicated CAN card including the serial number
and CAN port. This focused scan will speed up
the detection process and avoid any detection of
modules connected to other CAN interfaces.

All except selected

Here you define which CAN hardware should be
ignored during the scan process.

▶ CAN device synchronisation mode: Allows you to select the CAN device

synchronisation mode (Free-running or Synchronous).

▶ CAN hardware detection bus type: Allows you to select the bus type for hardware detec-

tion on standard CAN or standard CAN + CAN FD.

▶ CAN baud rates: With the check box for the baud rate settings you can control which baud
rates should be considered for the scan process. If your modules run always on the same
baud rate can focus the scan process on this dedicated rate to speed up the process.

You can enable the baud rates between minimum 125 kBd and maximum 1 MBd for the
CAN hardware detection.

If the connected devices that currently are configured to one of the
50 kBd and 100 kBd baud rates. It might be required to reset those
devices. If a configuration containing a system with one of the removed
baud rates is loaded, the baud rate is updated to the next higher value
being supported (125 kBd).

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

17

▶ Automatic CAN ID placing: With this check box you can define where the software will
assign automatically the CAN IDs starting from the CAN ID defined in the box below.

▶ Start CAN ID: Here you define the first CAN ID to start the automatic placing. The start
CAN ID can be displayed in a hex, decimal or in the binary format. The CAN ID range
640 . . . 767 is used internally by the modules and will be skipped in the CAN ID placing
routine. With the column chooser function you can the CAN IDs information to the chan-
nel grid to display the software assigned IDs.

▶ Compatibility mode settings: X-PIugIn provides a special compatibility mode if SIM-STG

devices are used.

This mode should only be used, when using SIM-STGs. If no SIM-STGs
are used then this option should be turned off, since hardware oper-
ations may take much longer.

5.1.3 Options Settings

The basic option settings are as shown below:

Figure 5.6 - Options Settings

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

18

▶ Aliasing-free filter settings: This check box impacts the Digital Signal Processors (DSP)
and hardware software filter settings. The function is only supported for modules which
have an adjustable DSP and / or hardware filter. If aliasing-free filtering is active, the soft-
ware filter frequency is automatically adjusted when the sampling rate changes. The
frequency is changed so that the new value is always the maximum possible frequency,
where aliasing free measurement is guaranteed. If the filter frequency previously is
changed to a lower value intentionally, the filter frequency must be changed manually by
the user after the sample rate is changed. This also applies, if the sample rate is decreased.
The automatic adaptation of the software filter frequency is not applied, in case that the
aliasing free measurement is disabled. For more details, please refer to "Signal Filters" on
page 170.

▶ CSV import mode: Defines the behaviour of the CSV import. There are three types of

import modes:

▶ Default

▶ Creation

▶ Front number

▶ Calibration interval: Defines the calibration time interval for all the devices along with a

warning message duration.

▶ TEDS sensors: If enabled, the senor range for uniploar TEDS sensors is set to biploar

range, such that sensor values of 0 are not displayed as NoValue.

▶ Special measurement modes: This setting is available for the special measurement
cases and applicable for specific devices ("M-CNT2" on page 52 and "M-SENS2" on
page 41).

▶ Frequency drop tolerance: This factor controls the sensitivity, if the new measured

value is used instead of the previous one. Default value is 1.75

▶ Time before 1st data [in ms]:The time before the device sends the first data after the

start of a measurement. Defaul value is "0" (deactivated).

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

19

5.1.4 Components Settings

In the components you can see all supported modules. With the priority setting you have an
impact on the visibility. When a module is put into the status not used it will be made invisible in
the module tree for selection during the dry configuration.

You can reduce the number of device types to be used by assigning a priority:

▶ High

▶ Normal

▶ Low

▶ Not used

Figure 5.7 - Components

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

20

6 Hardware Modules Integration

Modules are the measurement devices which are connected along with the logger and designed
specifically to measure the particular parameter. The X-PlugIn supports two types of modules:

▶ X-Modules: Mode of communication via Ethernet.

▶ M-Modules: Mode of communication via CAN bus.

6.1 X-Modules

X-Modules are operating in a 100 Mbit Ethernet network based on the XCP protocol. You can
also find the datasheet for each modules at https://www.ipetronik.com/en/products-ser-
vices/modules.html. The X-Modules are:

▶ Mx-SENS2 4 FAST

▶ Mx-SENS2 4

▶ Mx-SENS2 8

▶ Mx-STG2 6

▶ Sx-STG

6.1.1 X-Modules Cable Length

300m cable length with a maximum of 40 devices and one Laptop/Logger.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

21

6.1.2 Mx-SENS2 4 Fast

Fast 4-Channel Analog Measurement Device with Excitation.

Figure 6.1 - Mx-SENS2 4 Fast

▶ 4 fast analog signal inputs for voltage / current supporting channel sample rates up to

400 kHz.

▶ 4 separate dual sensor excitations (up to ±15 V, up to ±60 mA)

▶ Sensor breakage detection (activation via software setting) Offset adjust during meas-

urement.

▶ ICP (Integrated Circuit Piezoelectric) mode supporting IEPE sensors (Integrated Elec-

tronics Piezo Electric)

▶ Measurement modes: SENS, mA, IEPE, individual for each input

▶ Status LED at each input channel (sensor break indication and configuration aid)

▶ Offset adjust functions

▶ TEDS Class-2 supported

▶ Measurement data output via XCPonEthernet or CAN

▶ Designed for engine compartment applications.

▶ Toolless module to module connection

▶ Ruggedized and compact modules for harsh environments

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

22

Figure 6.2 - Mx-SENS2 4 Circuit

Figure 6.3 - Mx-SENS2 4 Circuit

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

23

6.1.2.1 Input Cables:

Standard (open)

Figure 6.4 - 670-810.xxx M-SENS (TEDS) Cable

Specific (assembled, open)

620-695.xxx

670-807.xxx

600-861.xxx

600-864.xxx

Mx-SENS 1B 7pin Adapter BNC/S-ICP/TEDS for ICP
measurement.

SENS 1B 6pin Cable open (compatible to 670-810, no TEDS
support).

SENS 1B 6pin Cable Banana 6 (compatible to 670-810, no
TEDS support, all lines connected to banana plugs) .

SENS 1B 6pin Cable Banana 2 (VIN+/VIN- via banana
plugs).

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

24

6.1.3 Mx-SENS2 8

Fast 8-Channel Analog Measurement Device with Excitation

Figure 6.5 - Mx-SENS2 8

▶ 8 analog signal inputs for voltage / current

▶ 8 separate sensor excitations, supply voltage individually selectable (up to ±15 V, ±45 mA)

▶ 12 unipolar and 12 bipolar measuring ranges

▶ 2 current measuring ranges

▶ 10 mV range, e.g. for standby current applications

▶ Offset and target value adjust functions

▶ Status LED at each input channel (channel identification / channel error indication)

▶ Measurement data output to Ethernet using XCPonEthernet or CAN

▶ Complete galvanic isolation (inputs, excitation, CAN, Ethernet, power supply, enclosure)

▶ Designed for automotive use

▶ Toolless module to module connection.

Figure 6.6 - Mx-SENS2 8 Circuit

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

25

6.1.3.1 Input Cables:

Standard (open)

Figure 6.7 - 670-810.xxx M-SENS (TEDS) Cable open

Specific (assembled, open)

670-807.xxx

SENS 1B 6pin Cable open (compatible to 670-810, no TEDS support).

600-861.xxx

SENS 1B 6pin Cable Banana 6 (compatible to 670-810, no TEDS
support, all lines connected to banana plugs).

600-864.xxx

SENS 1B 6pin Cable Banana 2 (VIN+/VIN- via banana plugs).
IPETRONIK

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

26

6.1.4 Mx-STG2 6

Fast 6-Channel Analog Measurement Device with Excitation.

Figure 6.8 - Mx-STG2

▶ 6 fast analog signal inputs for voltage supporting channel sample rates up to 100 kHz

▶ STG (Strain Gauge) measurement mode supports different bridge types

▶ 6 separate dual sensor excitations (up to ±5 V, up to ±45 mA)

▶ Offset and target adjust functions within the measurement range

▶ Shunt check

▶ 6-wire and 4-wire bridge connection (full / half bridge)

▶ Internal resistors for bridge completion selectable

▶ TEDS class-2 support (input connectors Lemo 2B 10-pin)

▶ Channel status-LED for channel identification and error indication

▶ Measurement data output to Ethernet using XCPonEthernet or CAN

▶ Complete galvanic isolation (signal inputs, excitation, CAN, Ethernet, power supply)

▶ Designed for engine compartment applications

▶ Ruggedized and compact modules for harsh environments

▶ Toolless module to module connection.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

27

6.1.4.1 Input Cables:

Standard (open)

Figure 6.9 - 600-747.xxx STG 2B 10p. Cable open (10-pin TEDS)

If you do not use IPETRONIK input cables, please pay attention to the
correct pin configuration.

The connection Pin 5 <> Pin 10 is always required as the module
identifies by this, when a sensor is plugged in.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

28

Figure 6.10 - 670-850.xxx DMS/STG Cable open (7-pin DMS compatible)

Figure 6.11 - 620-700.xxx STG SubD9/P Cable open (9-pin SUBD)

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

29

6.1.4.2 STG Operation Mode

Application:

▶ Measurement with strain gauges (full / half / quarter bridges).

▶ Measurement with sensors which provide a fixed ground (GND) reference (with no definite
ground reference the input may drift, because of the high impedance of the signal input).

Features:

▶ Bridge connection supporting 2-wire, 4-wire and also 6-wire technique

▶ Bridge completion using internal resistors

▶ Shunt check in configuration mode as well as in measurement mode Adjustable shunt res-
istor 5 kΩ to 500 kΩ (minimum and maximum value depends on the current setting of the
excitation voltage), connectable to each bridge section (quadrant).
The complete adjust data can be output to the software (CSV format) and can be loaded
and applied to the sensor for verification of stability and repeatability.

▶ Sensor break detection for all 6 wires (IN [up to an input range of 200 mV], VOUT, SENS)

indication by output of -Full Scale.

Measurement ranges:

▶ ±5 mV to ±1 V in 8 bipolar measurement ranges

▶ Measurement ranges ±5/ 10/ 20/ 50/ 100/ 200 mV, ±0.5/ 1.0 V

Adjustable differential voltages:

▶ Mx-STG2 adjusts offset voltages up to ±0.9 x Full Scale (FS).

Common Mode Rejection Ration (CMRR): To guarantee a correct measurement of the input
signal over the complete measurement range (uncropped signal amplitude), the input voltage
on IN+ resp. IN- relating to the GND potential should not exceed 4 V.

Sensor excitation:

▶ Selectable bipolar voltage: ±0.50 / ±1.25 / ±2.50 / ±5.00 V

▶ Current load up to 45 mA per channel

Bridge completion: Please refer to "STG Mode" on page 33 (Bridge Completion).

Shunt Check: Please refer to "Sx-STG" on the next page.

TEDS: Please refer to "TEDS Class 2" on page 39.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

30

6.1.5 Sx-STG

Figure 6.12 - Sx-STG

▶ 8 analog signal inputs for voltage measurement

▶ Measurement modes: SENS, STG, ICP, individual for each input

▶ 8 separate dual sensor excitations (up to ±15 V, up to ±45 mA)

▶ Offset and target adjust functions by hardware (maximum accuracy)

▶ Shunt check

▶ 6-wire and 4-wire bridge connection (full / half bridge)

▶ Internal resistors for bridge completion selectable

▶ TEDS support (input connectors Lemo 2B)

▶ Channel status-LED for channel identification and error indication

▶ Measurement data output to Ethernet using XCPonEthernet or CAN

▶ Complete galvanic isolation (signal inputs, excitation, CAN, Ethernet, power supply)

▶ Designed for automotive in-vehicle use

▶ Toolless module to module connection as option

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

31

6.1.5.1 Input Cables:

Standard (open)

Figure 6.13 - 670-850.xxx DMS/STG Cable open (7-pin DMS compatible)

Figure 6.14 - 600-747.xxx STG 2B 10p. Cable open (10-pin TEDS)

If you do not use IPETRONIK input cables, please pay attention to the cor-
rect pin configuration.

The connection Pin 5 <> Pin 10 is always required as the module identifies
by this, when a sensor has been plugged in.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

32

6.1.6 Signal Input Modes

Each input channel can be set to one of three different signal input modes:

STG Mode

Strain gauge applications (4-wire and 6-wire bridge connection)

SENS Mode

Sensors with integrated amplifier unit (3-wire, 4-wire connection), and
common voltage measurement

ICP Mode

ICP sensors (Integrated Circuit Piezoelectric, e.g. acceleration
transducers).

6.1.6.1 STG Mode

Figure 6.15 - Topic Text

Application:

▶ Measurement with strain gages (full / half / quarter bridges).

▶ Measurement with sensors which provide a fixed ground (GND) reference (with no definite
ground reference the input may drift, because of the high impedance of the signal input).

Features:

▶ Bridge connection supporting 2-wire, 4-wire and also 6-wire technique.

▶ Bridge completion using internal resistors.

▶ Shunt check in configuration mode as well as in measurement mode. Adjustable shunt res-
istor 5 kΩ to 500 kΩ (minimum and maximum value depends on the current setting of the
excitation voltage), connectable to each bridge section (quadrant). The complete adjust
data can be output to the software (CSV format) and can be loaded and applied to the
sensor for verification of stability and repeatability.

▶ Sensor break detection for all 6 wires (IN [up to an input range of 200 mV], VOUT, SENS)

indication by output of –Full Scale.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

33

Measurement Ranges:

▶ 0 ... 2 mV to 0 ... 2 V in 2 mV steps

▶ ±2 mV to ±2 V in 2 mV steps

Adjustable Differential Voltages (Hardware Adjust):

STG Measurement Ranges

STG Measurement Ranges

STG Adjust
Ranges

Unipolar
Minimum

Unipolar
Maximum

Unipolar
Minimum

Unipolar
Maximum

Full Scale
(FS)*

2 mV

30 mV

±2 mV

±30 mV

32 mV

62 mV

±32 mV

±62 mV

64 mV

124 mV

±64 mV

±124 mV

126 mV

250 mV

±126 mV

±250 mV

252 mV

500 mV

±252 mV

±500 mV

502 mV

1000 mV

±502 mV

±1000 mV

1002 mV

2000 mV

±1002 mV

±2000 mV

*The upper range limit of the corresponding measurement range.

±3125 mV
±0.9 FS

±62.50 mV
±0.9 FS

±125.00 mV
±0.9 FS

±250.00 mV
±0.9 FS

±500.00 mV
±0.9 FS

±1000.00 mV
±0.9 FS

±2000.00 mV
±0.9 FS

Common Mode Rejection Ratio (CMRR): To guarantee a correct measurement of the input
signal over the complete measurement range (uncropped signal amplitude), the input voltage
on IN+ resp. IN- relating to the GND potential should not exceed 4 V.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

34

Sensor Excitation:

▶ Selectable bipolar voltage: ±0.50 / ±1.25 / ±2.50 / ±5.00 V

▶ Current load up to 45 mA per channel

Bridge Completion:

Figure 6.16 - Bridge Completion

Sx-STG supports the following types of bridge completion:

▶ Quarter bridge to full bridge (fixed half bridge + selectable supplementation resistor)

▶ Half bridge to full bridge (fixed half bridge)

Shunt Check:

Figure 6.17 - Shunt Check

With the shunt check an internal resistor is temporarily connected to one quadrant (section) or
consecutively to all sections of the bridge circuit. This has a definite affect on the output of the
bridge. Is the shunt check executed before start and after the end of each measurement task,
the correct function (offset, gain, stability) of the sensor can be validated by comparing the
results.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

35

The shunt check can be initiated during:

▶ The configuration mode

▶ The measurement mode

The parameters of the shunt check can be output in CSV format to the software to be stored and
used later on. In order to identify the shunt check results within the data record, start and end of
the shunt check process is marked with a series of - FS (Minus Full Scale) values.

6.1.6.2 SENS Mode

Figure 6.18 - SENS Mode

Applications:

▶ Measurement with sensors without a direct ground (GND) reference.

▶ Voltage measurement up to ±50 V.

Features:

▶ Sensor connection supporting 3-wire and 4-wire technique.

▶ Sensor break detection for the 4 wires (IN, VOUT) indication by output of –Full Scale.

Measurement Ranges:

▶ 0.01 / 0.02 / 0.05 / 0.1 / 0.2 / 0.5 / 1 / 2 / 5 / 10 / 20 / 50 V

▶ ±0.01 / ±0.02 / ±0.05 / ±0.1 / ±0.2 / ±0.5 / ±1 / ±5 / ±10 / ±20 / ±50 V

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

36

Adjustable Differential Voltages (Hardware Adjust):

SENS Measurement Ranges

Unipolar

Bipolar

SENS Adjust Ranges

5 V

10 V

20 V

50 V

±5 V

±10 V

±20 V

±50 V

±2.25 V

±4.50 V

±9.00 V

±22.50 V

Common Mode Rejection Ratio (CMRR): To guarantee a correct measurement of the input
signal over the complete measurement range (uncropped signal amplitude), the input voltage
on IN+ resp. IN- relating to the GND potential should not exceed the limits listed in the table
below.

SENS Measurement Ranges

Max. Input Voltages

Unipolar

Bipolar

IN+, IN- related to the channel GND

5 V

10 V

20 V

50 V

±5 V

±10 V

±20 V

±50 V

Sensor Excitation

±20 V

±20 V

±40 V

±100 V

▶ Adjustable unipolar voltage: 0.50 / 1.25 / 2.50 / 5.00 / 10.00 / 15.00 V

▶ Adjustable bipolar voltage: ±0.50 / ±1.25 / ±2.50 / ±5.00 / ±10.00 / ±12.00 / ±15.00 V

▶ Current load up to 45 mA per channel

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

37

6.1.6.3 ICP Mode

Figure 6.19 - ICP Mode

Applications:

▶ Measurement with ICP sensors (Integrated Circuit Piezoelectric), mainly dynamic accel-

eration transducers.

▶ Other Piezo electric sensors (e.g. condenser microphone) can be supported.

Features:

▶ DC decoupling through input capacitor.

▶ Output of the actual measurement value depending on the configured sampling rate (output
rate to LAN). In order to avoid measurement errors (aliasing) it may be reasonable to set
the sampling rate to a higher frequency.

▶ High speed regulation for sensor excitation current.

Measurement Ranges:

▶ ±0.1/ ±0.2/ ±0.5/±1.0/ ±2.0/ ±5.0 V

▶ Frequency response 5 Hz … 16 kHz

Sensor Excitation:

▶ Regulated supply current of typically 4.5 mA, at a maximum off-load voltage of approx. 24 V

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

38

6.1.7 TEDS Class 2

Figure 6.20 - TEDS Class 2

The LEMO 2B version of Sx-STG is capable of supporting the use of Transducer Electronic
Data Sheet (TEDS) enabled transducers. As a globally recognized industry Plug & Play stand-
ard, TEDS is defined under IEEE 1451.4 and distinguishes between two interface classes.

As soon as the input connector is plugged in, the Sx-STG module automatically detects Class II
TEDS sensors (e.g. multi-wire interfaces with bridge-type sensors) and is able to read out
sensor-specific data about the TEDS +/- interface, using a serial, master/slave model of
communication.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

39

6.2 M-Modules

The M-modules/M-devices are operating in a CAN bus network based on the XCP protocol. You
can also find the datasheet for each modules at https://www.ipetronik.com/en/products-ser-
vices/modules.html. The M-Modules are:

▶ M-SENS2

▶ M-SENS3 8

▶ M-THERMO2

▶ M-THERMO2 u

▶ M-THERMO3 16

▶ M-RTD2

▶ M-CNT2

▶ CANpressure

6.2.1 M-Modules Cable Length

CAN-FD (Switchable to pure CAN operation via software).

CAN-Bitrate
CAN-FD Bitrate Arbitration Phase

CAN-FD
Data-Bitrate

Max.
Bus Length

1MBit/s

1MBit/s

1MBit/s

1MBit/s

500kBits/s

500kBits/s

500kBits/s

500kBits/s

500kBits/s

250kBits/s

-

1MBit/s

2MBit/s

5MBit/s

-

500kBits/s

1MBit/s

2MBit/s

5MBit/s

25m

10m

10m

10m

50m

50m

20m

20m

10m

-

100m

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

40

6.2.2 M-SENS2

4-channel analog input module with sensor excitation

Figure 6.21 - M-SENS2

▶ 4 measurement inputs for voltage (V) / current (mA) selectable for each input

▶ 6 sensor excitation ranges (unipolar 15 V, up to ±60 mA)

▶ TEDS Class-2 supported

▶ Measurement data output to CAN

▶ Galvanic isolation (Signal inputs, CAN, power supply, enclosure)

▶ Designed for engine compartment applications

▶ Toolless module to module connection

▶ Ruggedized and compact modules for harsh environments

Figure 6.22 - M-SENS 4 Circuit Diagram

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

41

6.2.2.1 Input Cables

Standard (Open)

Figure 6.23 - 670-807.xxx SIM-SENS Cable Open (M-SENS, M-SENS2)

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

42

6.2.3 M-SENS3 8

8 channels with freely selectable operating modes are extraordinarily flexible and precise
thanks to the 18-bit high-resolution AD converter. The M-SENS3 8 is ultra-compact and
ruggedized. Its innovative wireless and magnetic connection concept reduces setup times and
guarantees an optimal and fail-safe data connection.

Figure 6.24 - M-SENS3 8

▶ Freely selectable operating mode for each input: voltage, current, and frequency

▶ Measurement data output to CAN FD

▶ System status information (system, devices, channel)

▶ TEDS class-2 support

▶ Toolless, magnetic connection

▶ Channel and device status display in the software (e.g. sensor excitation/undervoltage

monitoring)

▶ System connection without connection cable

▶ IP 67 and extended temperature range

▶ Highly compact and ruggedized

▶ Galvanic isolation (channel, CAN, supply, enclosure)

▶ Channel status LED for each input displaying the selected measurement mode

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

43

Input Cables

Standard (Open)

Figure 6.25 - M-SENS (TEDS) Cable Open

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

44

6.2.4 M-Thermo2

8-Channel Temperature Measurement for K-Type Thermocouples

Figure 6.26 - M-Thermo2

▶ 8 Thermocouple measurement inputs type K (NiCr/NiAl)

▶ Cold junction compensation per channel

▶ Separate ADC for each channel

▶ Status LED at each input channel (sensor break indication and configuration aid)

▶ Measurement data output to CAN

▶ Complete galvanic isolation (inputs, CAN, power supply, and enclosure)

▶ Designed for engine compartment applications

▶ Toolless module to module connection

Figure 6.27 - M-Thermo2 Circuit Diagram

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

45

6.2.4.1 Input Cables

Standard (open)

Figure 6.28 - 600-888.xxx SIM-TH-MIN Cable Open

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

46

6.2.5 M-Thermo2 u

8-Channel Universal Thermocouple Inputs

Figure 6.29 - M-Thermo2 u

▶ 8 Universal thermocouple inputs supporting type J, K, N, R, S, T, E

▶ Cold junction compensation for each channel

▶ Separate ADC for each channel

▶ Status LED at each input channel (sensor break indication and configuration aid)

▶ Measurement data output to CAN

▶ Complete galvanic isolation (inputs, CAN, power supply, and enclosure)

▶ Designed for automotive use

▶ Toolless module to module connection

Figure 6.30 - M-Thermo2 u Circuit Diagram

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

47

6.2.5.1 Input Cables

Standard (open)

Figure 6.31 - 600-888.xxx SIM-TH-MIN Cable open

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

48

6.2.6 M-Thermo3 16

16-Channel Universal Thermocouple Inputs

Figure 6.32 - M-Thermo3 16

▶ High-resolution 24-bit ADC technology

▶ Measurement data output on CAN-FD.

▶ Cable free system connection - connection cable not required

▶ Tool-free, magnetic connection technology

▶ Separate cold junction compensation for each channel

▶ Ultra compact and robust design

▶ IP 67 and extended temperature range

▶ Galvanic isolation (channel, CAN, supply, housing)

▶ Channel status LED at each measuring input with display of the selected thermocouple

type according to IEC/ANSI

▶ Display of channel and device status in software interface (e.g. sensor break / under-

voltage)

▶ System status information (system, devices, channel)

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

49

Figure 6.33 - M-Thermo3 16 Circuit Diagram

Input Cables

Standard (open)

Figure 6.34 - 600-888.xxx SIM-TH-MIN Cable open

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

50

6.2.7 M-RTD2

4-channel PT100 RTD temperature measurement inputs

Figure 6.35 - M-RTD2

▶ 4 measurement inputs for RTD

▶ Measurement data output to CAN

▶ Complete galvanic isolation (inputs, CAN, power supply, and enclosure)

▶ Designed for engine compartment applications

▶ Toolless module to module connection

▶ Ruggedized and compact modules for harsh environments

6.2.7.1 Input Cables

Standard (open)

Figure 6.36 - 670-937.xxx PT100/RTD 0S Cable Open

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

51

6.2.8 M-CNT2

4-channel universal counter module with sensor excitation

Figure 6.37 - M-CNT2

▶ 4 signal inputs with adjustable ON and OFF thresholds

▶ Measurement modes: frequency from period duration, period duration, pulse duration,

pause duration, duty cycle, event counter, detection of rotating direction (mode frequency
and event counter)

▶ 4 separate sensor excitations, supply voltage individually selectable (up to 15 V, 60 mA)

▶ Status LED at each input channel indicates signal processing

▶ Measurement data output to CAN

▶ Complete galvanic isolation (signal inputs, excitation, CAN, power supply, and enclosure)

▶ Designed for engine compartment applications

▶ Toolless module to module connection

Figure 6.38 - M-CNT2 Circuit Diagram

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

52

6.2.8.1 Input Cables

Standard (open)

Figure 6.39 - 670-858.xxx CNT/FRQ-IN Cable Open

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

53

6.2.8.2 Input / Principle Details

Measuring Method: The analog and digital input signal is evaluated with a programmable com-
parator threshold (switching threshold, hysteresis) and the following 48 bit counter. The FPGA
and Digital Signal Processor (DSP) convert the respective counter values online into a fre-
quency output (and duty cycle or time period).

Figure 6.40 - Signal at the Measuring Input

The input signal is compared with the defined switching thresholds by using a comparator (refer
to "Signal at the Measuring Input" above). The result is a square wave voltage similar to the fre-
quency at the comparator output. The pulse and interval duration of this square wave voltage is
detected with the internal 100 MHz counter.

If the timeout expires without any detection of an ON threshold, the zero indication will output
the user defined minimal value. The setting of the timeout is recommended in order to avoid
time delays in signal evaluation. A correct signal evaluation is supported only with detections
that follows in a sequence of ON and OFF thresholds.

▶ Frequency: The frequency is acquired with the interval duration acquisition described

above. The reciprocal value of the counter result of the interval duration measurement is
scaled and sent correspondingly to the measuring range setting.

▶ Duty cycle: The counter value of the pulse duration is divided by the counter value of the
interval duration and correspondingly scaled and sent to the measuring range setting.

If the frequency is too low (or 0 Hz), 0% (low level) or 100% (high level) is sent depending
on the signal level.

The thresholds on and off do usually differ and cause different results of the pulse duration
and the duty cycle if the signal edges are low, depending on the defined thresholds.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

54

▶ Interval duration: The interval duration is acquired with the acquisition described above.

The counter value between two thresholds on is detected, scaled, and sent correspondingly
to the measuring range setting.

▶ Pulse duration: The pulse duration is acquired with the acquisition described above. The
counter value between the threshold on and the threshold off is detected, scaled, and sent
correspondingly to the measuring range setting.

The thresholds on and off do usually differ and cause different results of the pulse duration
if the signal edges are low, depending on the defined thresholds.

▶ Pause duration: The pause duration acquisition corresponds to the pulse duration acquis-

ition with inverted input signal.

Mode - Ignore Frequency Drop:The module supports in the mode tab sheet a function called:
“Ignore frequency drop”. With this function it is possible to measure RPM when
several teeth on the reflector are missing.

Figure 6.41 - Ignore Frequency Drop

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

55

The drop voltage can be configured in the PlugIn options:

Figure 6.42 - Special Measurement Modes- PlugIn Options

Status LED at the Input: The status LED at the respective input indicates the acquisition of a
frequency signal. This is the case if both switching thresholds of every value are reached
(threshold ON and OFF).

The status LED is on / flashes in time with the signal frequency if:

▶ Corresponding channel is active

▶ Device is in the acquisition mode (acquiring data) and

▶ Switching thresholds are correctly defined.

Due to the slowness of visual proceeding, only frequencies under approx. 10 Hz can be seen as
flashing. The LED is permanently ON at higher signal frequencies.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

56

6.2.9 CANpressure

Pressure transducer with CAN output for automotive applications

Figure 6.43 - CANpressure

▶ Absolute and relative pressure gauge in the range of 1 to 250 bar

▶ Internal temperature sensor at gauge point

▶ Measurement data output to CAN

▶ Galvanic isolation (inputs, CAN, power supply, enclosure)

▶ Designed for engine compartment applications

▶ Ruggedized and compact modules for harsh environments

6.2.9.1 Pressure Connections

Figure 6.44 - Male Thread

Figure 6.45 - Female Thread

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

57

Dimensions

D

L1

L2

Fastening
Torque

Wrench
Size

M10 x 1 male

10 mm
(0.39 in)

8.5 mm
(0.33 in)

M10 x 1 female

10 mm
(0.39 in)

9.5 mm
(0.37 in)

M14 x 1.5 male

14 mm
(0.55 in)

9.5 mm
(0.37 in)

M14 x 1.5
female

14 mm
(0.55 in)

G ¼ male

G ¼ female

13.2
mm
(0.51 in)

13.2
mm
(0.51 in)

10.5
mm
(0.41 in)

9.5 mm
(0.37 in)

10.5
mm
(0.41 in)

25.5
mm

(1.00 in)

26.5
mm
(1.04 in)

25.5
mm
(1.00 in)

26.5
mm
(1.04 in)

25.5
mm
(1.00 in)

26.5
mm
(1.04 in)

17-23 Nm

17-23 Nm

17-23 Nm

17-23 Nm

17-23 Nm

17-23 Nm

24 mm
(0.94 in)

24 mm
(0.94 in)

24 mm
(0.94 in)

24 mm
(0.94 in)

24 mm
(0.94 in)

24 mm
(0.94 in)

Keep the stated range of the fastening torque when mounting
CANpressure to ensure full accuracy.

Do not exceed the upper limit of the fastening torque to avoid an
irreversible damage of the pressure transmitter.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

58

Pressure Transducer
(Realtive, Absolute)

0-1 bar / 0-14.5 psi
0-2 bar / 0-29.0 psi
0-5 bar / 0-72.5 psi
0-10 bar / 0-145 psi
0-20 bar / 0-290 psi
0-25 bar / 0-363 psi

0-50 bar / 0-725 psi
0-100 bar / 0-1450 psi
0-150 bar / 0-2175 psi
0-250 bar / 0-3626 psi

Overload Pressure

Burst Pressure

3 x FS (Full Scale)
3 x FS
3 x FS
3 x FS
3 x FS
3 x FS

3 x FS (Full Scale)
3 x FS
3 x FS
3 x FS

> 200 bar / 2901 psi
> 200 bar / 2901 psi
> 200 bar / 2901 psi
> 200 bar / 2901 psi
> 200 bar / 2901 psi
> 200 bar / 2901 psi

> 850 bar / 12328 psi
> 850 bar / 12328 psi
> 850 bar / 12328 psi
> 850 bar / 12328 psi

Other pressure ranges - On request

Medium compatibility
Gases and fluids (also fuels and break fluids) up to 200 bar / 2901 psi, other conditions on
request.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

59

6.3 Module Identification by Base Type Number

The modules contain a unique Base type number for M-Module and X-Module through which
the users can identify the modules with ease. The modules and base type number is shown in
the below table. The following modules are supported in the IPETRONIK X PlugIn

M-Module Family

M-Module

Base Type Number

M-THERMO3 16 (NEW)

M-SENS2 (EOL)

M-SENS2 DSP

M-SENS2 250Hz

M-SENS2 250Hz DSP

M-SENS

M-SENS DSP

M-SENS 8 (EOL)

M-SENS 8 DSP

M-SENS 8plus

M-SENS 8plus DSP

M-THERMO2

M-THERMO2 HV

M-THERMO2 u

M-RTD2

M-UNI2 (EOL)

Mc-THERMO (EOL)

540

587

587

591

591

561

561

567

567

568

568

578

557

579

581

584

573

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

60

M-Module

M-THERMO

M-THERMO 16 (EOL)

M-THERMO T

M-THERMO 16T

µ-THERMO (EOL)

M-CNT2

M-FRQ (EOL)

CANpressure

M-THERMO96 16

SIM-STG (EOL)

M-Flow

X-Module Family

X-Module

Mx-SENS(2)8

Sx-STG

Mx-STG2 6

Mx-SENS2-4

Mx-SENS2-4 FAST

Base Type Number

560

566

569

575

563

586

562

595

593

519

519

Base Type Number

911

920

912

916

917

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

61

6.4 Connecting the X-Modules/Ethernet Modules

In the following 3 main X-module hardware configurations and cable sets examples are shown.

6.4.1 X-Modules Hardware Setup - Example 1

In this setup the power supply is provided from the very end of the module chain. This setup is
applicable only when there are few modules in the measurement setup and one source of
supply 9 - 36 VDC is sufficient.

Figure 6.46 - X-Modules Hardware Setup -

Example 1

6.4.2 X-Modules Hardware Setup - Example 2

In this setup many modules are involved and therefore intermediate power supply is required.
With the X-FEED power feeder the modules can get power feed into the middle of the
measurement chain. As a rule of thumb 7 X-Modules can be supplied with one power feeder. If
the system grows lager power supply from the very end or additional X-FEED modules can be
added to the system. As indicated the X-FEED provides power only to the X-Modules.

Figure 6.47 - X-Modules Hardware Setup - Example 2

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

62

6.4.3 X-Modules Hardware Setup - Example 3 (CAN Tunneling)

Another system architecture can combine X-modules and M-modules in one daisy chain. In this
case a dedicated cable is required to link-up the Ethernet based X-modules to the CAN based
M-modules.
The architecture requires that the Ethernet modules at the start followed by the M-modules as
shown. In smaller setups one power feed from the very end can be sufficient. However, if the
system grows lager, you can extend the power alimentation through adding X-FEED modules
for the X-modules and CAN POWER FEEDER to the M-modules.

It is not possible to add any Ethernet modules/X-Modules behind the CAN mod-
ules/M-modules.

Figure 6.48 - X-Modules Hardware Setup - Example 3 (CAN Tunneling)

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

63

6.5 CAN Card Hardware Interfaces

List of supported CAN card interfaces:

Vendor

IPETRONIK
IPETRONIK
IPETRONIK
IPETRONIK
IPETRONIK
IPETRONIK
IPETRONIK
IPETRONIK
IPETRONIK
IPETRONIK

Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector
Vector

CAN Interface

IPETRONIK

IPEhub2
IPEcan FD
IPEcan FD PRO
IPEcan
IPEcan PRO
ETH Gateway CLFD V1.1
ETH Gateway CLFD V1.2
ETH Gateway CAN FD Satellite
ETH Gateway FlexRay Satellite
ETH Gateway LIN Satellite

Vector

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

64

Vendor

Kvaser
Kvaser
Kvaser
Kvaser
Kvaser
Kvaser
Kvaser
Kvaser
Kvaser
Kvaser
Kvaser
Kvaser
Kvaser
Kvaser
Kvaser
Kvaser
Kvaser
Kvaser
Kvaser

Peak
Peak
Peak
Peak
Peak

Softing
Softing
Softing
Softing
Softing
Softing
Softing

CAN Interface

Kvaser

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

Peak

Softing

PCAN-USB X6
PCAN-PCI
PCAN-PCIe
PCAN-PCIe FD
PCAN-M2 FD

CANcard2
EDICcardC
EDICcard2
CAN-Acx-PCI
CAN-Acx-PCI/DN
CANusb
CAN-PROx-PCI

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

65

ICS

ETAS

Vendor

ICS
ICS
ICS
ICS

DREWTECH
I+ME ACTIA

ETAS
ETAS
ETAS
ETAS

EthernetSystems

CAN Interface

ValueCAN
ValueCAN3
ValueCAN4
ValueCAN4-4

Mongoose
Basic+24 XS

ES581
ES582
ES593
ES595

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

66

6.6 Connecting the M-Modules/CAN Modules

In the following 3 main M-module hardware configurations and cable sets examples are shown.

The required cable sets and lengths are depending on the physical installation environment.
The cables are available in different lengths. The last 3 digits of the cable number are indicating
the length. The required cable to interconnect the M-CAN modules is number: 620-560.xxx. The
available lengths for the placeholder .xxx are for example:

▶ 002 = 0.15 meter

▶ 015 = 1.5 meter

▶ 030 = 3 meter

▶ 050 = 5 meter

▶ 100 = 10 meter

Every cable has a dedicated cable data sheet indicating the connectors, cable pins and the
color of the cable as indicated in the example below.

Figure 6.49 - Cable Datasheet

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

67

6.6.1 M-Modules Hardware Setup - Example 1

In this setup the power supply is provided from the very end of the module chain. This setup is
applicable only when there are few modules in the measurement setup and one source of
supply 9 - 36 VDC is sufficient.

Figure 6.50 - M-Modules Hardware Setup - Example 1

6.6.2 M-Modules Hardware Setup - Example 2

In this setup the supply is provided through a SUBD 9 and Y-splitter cable at the beginning of
the module chain. This setup is also practical in case the power supply and CAN interface are
located at the same end. This system works well for smaller chain modules where one supply is
sufficient.

It is important to finish the measurement system on the last module with a
CAN bus termination plug.

Figure 6.51 - M-Modules Hardware Setup - Example 2

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

68

6.6.3 M-Modules Hardware Setup - Example 3

In this case you operate many modules in the measurement setup and interconnection between
the different modules might be also large which causes voltage drops along the modules. It is
recommended to add a power feeder T-Junction to the system. Within very large systems is
many be required to have several power feeder and to use additional power supply via the last
module or the first modules, as indicated in the two scenarios above. However, it is important to
consider a separate power supply cable when using the power feeder. This cable has no
internal CAN bus termination. As a rule of thumb every 15 modules a power feeder should be
considered.

The CAN-Modules require their own power supply either from the very end or
using the M-CAN power feeder.

Figure 6.52 - M-Modules Hardware Setup - Example 3

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

69

6.7 Introduction to CAN-FD

This improved protocol overcomes two CAN limits: You can transmit data faster than with 1
Mbit/s and the payload (data field) is now up to 64 byte long and not limited to 8 byte anymore.
In general, the idea is simple: When just one node is transmitting, the bit-rate can be increased,
because no nodes need to be synchronized. Of course, before the transmission of the ACK slot
bit, the nodes need to be re-synchronized.

CAN-FD data frames can be transmitted with two different bit-rates: In the arbitration phase the
bit-rate depends on the network topology and is limited to 1 Mbit/s; in the data phase the bit-rate
is limited by the transceiver characteristics.

Figure 6.53 - CAN-FD Phase

6.7.1 CAN Bus Termination

A complete termination of the CAN bus with a resistor of 120Ohm each is mandatory for the cor-
rect functioning of the CAN bus.

This is automatically realized in the IPETRONIK measuring system by using the recommended
voltage and CAN cables with integrated termination.

In case of a pure M3 system and use of the Y-cable 623-500.xxx with lines for voltage and CAN
integrated, the termination of the "open" side is realized by the M3 device itself.

Using a ratio of 1:8 for the bit-rates in the arbitration and data phase leads to an approximately
six-times higher throughput considering that the CAN-FD frames use more bits in the header
(control field) and in the CRC field.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

70

Figure 6.54 - Classical CAN v/s CAN-FD

6.7.2 Structure of CAN-FD Message

CAN-FD data frames uses reserved bits, called FDF (FD frame) bit. If it is of recessive value,
the following bit sequence is interpreted as a CAN-FD data frame. If it is of dominant value, it is
a Classical data or remote frame. In the newly introduced BRS (bit rate switch) bit, the second
bit-rate is applied, when it is of recessive (r) value. If it is of dominant (d) value, the arbitration
phase bit-time setting is used in the data phase.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

71

Figure 6.55 - Structure of CAN FD Data Frames

Abbrevation

SOF

CRC

ACK

EOF

IMF

Description

Start-Of-Frame

Cyclic Redundancy Check

Acknowledgement

End-Of-Frame

Intermission Field

The CAN-FD protocol controller has to also support Classical CAN frames. Both CAN protocols
(Classical as well as CAN-FD) are internationally standardized in ISO 11898-1:2015. CAN-FD
data frames with 11-bit identifiers use the FBFF (FD Base Frame Format) and those with 29-bit
identifiers use the FEFF (FD Extended Frame Format). The CAN-FD protocol doesn’t support
remotely requested data frames.

Figure 6.56 - CAN-FD Frame Formats

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

72

Abbrevation

Description

RRS

SRR

IDE

FDF

d

r

r0

Remote Request Substitution

Substitute Remote Request

Identifier Extension

Flexible Data rate Format

Dominant

Recessive

Reserved

The control field comprises additional bits not provided by the Classical CAN data frames. The
FDF (FD Dormat) bit indicates the usage of FD frame formats. At the sample-point of the BRS
(Bit-Rate Switch) bit, the bit-rate switch is performed. This guarantees a maximum of robust-
ness. The following ESI (Error State Indicator) bit provides information about the error status: a
dominant value indicates an error active state.

Figure 6.57 - Extended Control Field

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

73

Abbrevation

Description

IDE

FDF

BRS

ESI

Identifier Extension

Flexible Data rate Format

Bit Rate Switch; recessive, if alternate bit-rate

Error State Indicator; recessive, if error passive

During the standardization process of the CAN-FD protocol, some additional safe guards were
introduced in order to improve the communication reliability. This is why the CRC field com-
prises 17-Bit (for frames with payloads up to 16 byte) or 21-Bit (for frames larger than 16 byte)
polynomials and an 8-Bit stuff-bit counter plus a parity bit. The CRC field use Fixed-Stuff Bits
(FSB) with an opposite value of the previous bit. All these safe guards guarantee that all single
failures are detected under all conditions. Even the possibility to detect multiple failures is
improved.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

74

6.8 LED Indication

The device and channel LED state is displayed in IPEmotion. Depending on the device type,
firmware version and different states.

6.8.1 M-Modules LED Status

The LED status indicates the specific behaviour of the devices as shown in the table below.

LED Status

Off

Green Continuous

Description

No power supply

Power supply switched on, ready for operation

Green 1 Hz 25%/75% flashing

Measurement running

Green 5 Hz 50%/50% flashing

Boot up, Initialization, Firmware download run-
ning

Red Continuous

Internal error (Hardware)

Red 1 Hz 50%/50% flashing

Communication error,
e.g. connector unplugged respectively not fully
plugged in, cable broken or squeezed, faulty
bus communication

Firmware download successfully completed

Red 5 Hz 25%/70% flashing

Bus Overload

Green/Red 1 Hz 50%/50% flashing

Supply voltage out of range, check voltage level

6.8.2 X-Modules LED Status

Link LED

Off

Description

Status IN: Ethernet disconnected

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

75

Link LED

Description

Green 5 Hz 50%/50% flashing

Yellow 5 Hz 50%/50% flashing

Yellow/Green 5 Hz 50%/50% flash-

ing

6.8.2.1 Channel LED Indication

Status OUT: Ethernet disconnected

Status IN: Ethernet connected

Status OUT: Ethernet disconnected

Status IN: Ethernet disconnected

Status OUT: Ethernet connected

Status IN: Ethernet connected

Status OUT: Ethernet connected

Channel LED

Description

Off

Device start up, Channel inactive

Yellow 1 Hz flashing

Yellow Continuous

Identification of the selected
channel during Configuration

Waiting for user action

Sensor is plugged in but the channel is not
initialized.
Respective channel is still inactive

Green Continuous

OK - Signal measurement is running
(Sensor connected)

Red 1 Hz flashing

Error!

Source of the fault could be:

-Over-current on excitation detected
- Sensor break or bridge break detected
- Counter overflow
- General Hardware error

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

76

Channel LED

Description

Red Continuous

No sensor plugged in although channel is
active or Connection lost

6.8.3 System LED Status

The system LED status need a better understanding.- Amith

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

77

7 Software Interface

7.1 IPEmotion Signals Work Space

The Signals work space is dedicated to configure your PlugIns and take measurements. All con-
figuration functions are explained in reference to the IPETRONIK X-PlugIn.

Figure 7.1 - X-PlugIn Signals Work Space

7.1.1 Ribbon Main Functions

The ribbon provides many functions but in this manual we only focus on the ribbon functions
related to the X-PlugIn. For detailed explanation of the ribbon and its functions, please refer to
the IPEmotion Software Manual.

7.1.1.1 Detecting the Hardware

When you start working with the analog measurement modules first you need setup the hard-
ware and cable sets as discussed (Refer to "Connecting the X-Modules/Ethernet Modules" on
page 62 or "Connecting the M-Modules/CAN Modules" on page 67).

A supported CAN card hardware and power supply is required for the CAN mod-
ule setup.

The simple way to get started is to run the Detect function. Once you are done with the
hardware setup, click the Detect function on the ribbon, IPEmotion PC automatically detects all
hardwares that are connected to the PC.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

78

IPEmotion PC detects both Ethernet and CAN modules depending on the hardware setup con-
nected to the system. For more details of the Detect function, please refer to "Detect" on
page 95.

Figure 7.2 - Detecting the Hardware

7.1.1.2 IPETRONIK X-PlugIn

In the ribbon select the Hardware you would like to use for your dry configuration. In this case
select the IPETRONIK X PulgIn. The drop down list includes all PlugIns which were activated in
the OPTIONS→PlugIns. For more details, please refer to "X-PlugIn Activation" on page 11.

Sometimes users cannot access the list box and make manual
configurations. In this case, in Options → Basic settings the measurement
configuration by MPC (Measurement Point Catalog) data base file is activ-
ated. Doubt

See the chapter
APPENDIX : Options of the IPEmotion Software Manual for more details.

Select IPETRONIK X PlugIn from the active hardware list, you will see the currently loaded
PlugIn version or activated PlugIns in the list.

For changing the PlugIn version you need to go back to Options → PlugIns. There you can
switch to previous versions.
An equal sign (=) behind the PlugIn version indicates that you will always use this version even
if a more recent PlugIn version is installed. For more details, please refer to "PlugIn Versions"
on page 9.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

79

7.1.1.3 System

The system is the next step after the PlugIn is selected. The system is basically the specific
hardware or interface that you are using to set up your data acquisition system. Each PlugIn
consists at least of one system.

Figure 7.3 - Two X-System Nodes Detected

▶ Import: This function lets you import a system. If you have an existing system setup that is
previously saved as .isf file, you can import the system setup using the .isf file and all
respective system and modules will be added to the system tree.

You can save a system file as .isf, only when there is a single system
and multiple modules in the system tree.

If there are multiple system in the system tree, IPEmotion lets you to
save, as an configuration file (i.e .iwf or .iac).

Figure 7.4 - Import a System

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

80

7.1.1.4 Components

Below the system node you can add components provided the hardware is modular. In the
example the components are grouped in different categories like Voltage, Temperature, Pres-
sure, etc. measurement modules. For more details on Context Menu, please refer to "Context
Menu" on page 107.

Figure 7.5 - Access Components from the Ribbon

Figure 7.6 - Access Components from the Context Menu

7.1.1.5 Firmware Update

With the firmware update function, you can update the module firmware directly from the PlugIn.

To update the firmware of the module, you need to click on the X-system node then click the
Functions option on the ribbon. In the Functions dropdown select Update devices.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

81

Figure 7.7 - Firmware Update

The update dialog will show the current firmware version of the detected modules and will also
indicate the Target firmware available on the computer. Select the module that is required to
update and click Update.

Figure 7.8 - Module Firmware Update Interface.

Once you click the Update button the update, process is started and a progress bar will indicate
the percentage of completion.

Figure 7.9 - Module Firmware Update Progress Information

In the library tab of X update you can see the detailed information about the firmware latest
firmware version available on the computer.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

82

Figure 7.10 - Firmware Library

During the PulgIn installation process the firmware data base will be installed together with the
IPETRONIK-X PlugInin the default directory.

▶ C: \ProgramData\IPETRONIK\Firmware

Figure 7.11 - Firmware Default Directory

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

83

In the case you install an older IPETRONIK-X PlugIn version after a newer
version was installed, the firmware folder will be overwritten by the latest
installation. To prevent this from happening you may choose a different dir-
ectory for the firmware folder of each PlugIn version. Then you can import
the firmware directories accordingly to your needs.

7.1.1.6 Configuration Check

This function checks the configuration on consistency. However, this function does not work for
all PlugIns. Messages are only returned if the PlugIn supports the check function.
For example considering the duplicate channel names across all active PlugIns across the
Signals and Acquisition work space. A comfortable function for message refresh and
configuration error searching is implemented in the configuration check function.

Figure 7.12 - Possible Configuration Issues / Problems

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

84

7.1.1.7 Import and Export

Whether a PlugIn supports import or export functions also depends on the PlugIn imple-
mentation. The import is usually a shortcut to build your configuration. The import and export
functions depend on the selected interface of the system or module.
The below table shows the kind of files that can be imported and exported by the X-PlugIn.

X-PlugIn overview for description file import and export

IPETRONIK
PlugIn

Interface
Level

Configuration
Imports

Configuration
Exports

IPETRONIK X

System

No

A2L
CANdb (.dbc)
CANdb (.xml)
IPEmotion App (.iaw)

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

85

7.2 Configuration Adjust Functions

7.2.1 Database

If you use sensors from the sensor database and run the Adjust → Database function, the
software automatically retrieves the latest sensor configuration from the database. With this
process you can automatically update all sensors with the latest calibration data from the data-
base in one click. Details on the sensor data base are discussed in the chapter "Sensor Data-
base" on page 100

7.2.2 TEDS

When a hardware detection is executed with the TEDS (Transducer Electronic Data Sheet)
sensors connected to the analog inputs. The TEDS data stored in the TEDS chip in the sensor
are transferred to the channel scaling. You can view the TEDS icon if you add the symbol
column to the channel grid as shown below.

Figure 7.13 - TEDS Sensors

If the channel sensor modes are not a suitable range, the TEDS sensor will not be supported or
detected and an error message for the same is shown in the message tab.

Figure 7.14 - TEDS Error

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

86

The following M-module and X-module support TEDS:

▶ M-SENS2

▶ M-SENS2 DSP

▶ M-SENS2 250Hz

▶ M-SENS2 250Hz DSP

▶ M-SENS 8

▶ M-SENS 8 DSP

▶ M-SENS 8 plus

▶ M-SENS 8 plus DSP

▶ M-SENS3 8

▶ M-FLOW

▶ Mx-SENS(2) 8

▶ Mx-SENS2 - 4

▶ Mx-STG2 6

▶ Mx-SENS 2 - 4 FAST

▶ Sx-STG

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

87

7.2.2.1 TEDS Sensor Detection with Automatic Unit Transformation

When you detect the TEDS sensors you can define an automatic unit conversion. This function
is required when the unit defined for the sensor does not meet the unit format required for the
measurement application. In order to activate this feature you need to add an additional entry in
the settings .xml file. In the example above the standard sensor was detected with the unit
[Nm].

When you add the following code into the settings.XML file the unit are automatically converted
to the preferred unit defined in the Options > Unit settings.

▶ C:\ProgramData\IPETRONIK\IPEmotion 2024 R2\Settings.XML

The new entry in the XML file is defined as:

<detectWithPreferredUnit>True </detectWithPreferredUnit>

Figure 7.15 - Add New Function for TEDS Unit Conversion to Settings.xml

The default unit defined in the Options > Units is [Nm/rad].

Figure 7.16 - Options: Example - Default Unit for Torque = Nm/rad

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

88

7.2.2.2 TEDS Adjust on Channel Level

All modules supporting the TEDS (Transducer Electronic Data Sheets) function support in the
IPETRONIK X-PlugIn a TEDS adjustment on channel level. Rather than synchronizing your
whole configuration across all TEDS channels you can focus on a dedicated channel to integ-
rate the TEDS data from a connected sensor.

Figure 7.17 - Adjust TEDS Function changed unit from [Nm] to [Nm/rad]

Once the synchronization is completed the channel is updated with the TEDS data from the
sensor including the preferred unit defined in the Settings.xml file.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

89

7.2.2.3 Compare TEDS Sensor with Configuration

When a channel is already scaled based on TEDS parameters, you can use from the TEDS
compare function in the context menu to update the TEDS data e.g. when a new sensor was
connected to the input.

Figure 7.18 - Compare TEDS on Channel Level

When a TEDS sensor is detected the data is saved into a database file called IPESensorData-
base.xmt. In the "Scaling Calculator" on page 143 section we will discuss "How to retrieve
sensor data from the sensor database".

▶ C:\Users\Public\Documents\IPETRONIK\IPEmotion\Database\IPESensorDatabase.xmt

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

90

7.2.3 Offset Adjust

The offset adjustment is a very useful function to check and update the physical measurements
to the configured measurement range. With an offset operation you can shift the current sensor
signals on the analog inputs as your new base reference. The offset function can be performed
during the online measurements of the system.

If the user provide the Reference value the offset value is adjusted in
reference with the reference value. If no reference value is provided then the
offset value is adjusted in reference with the input value given to the device.

Figure 7.19 - Offset Adjust Dialog

The offset operation can be performed for all channels or only for dedicated groups. In this
example below 2 sensor groups are defined. Each channel can be rated to a group. In the below
example for channel 3 and channel 7(assigned to group 1) a sample reference value of 3 .00 V
and 7.00 V is provided then with the selection option you select the channel that you grouped or
all based on your requirements and Start the adjustment.

Figure 7.20 - Offset Operation Organized by Groups

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

91

After the offset operation the initial analog measurement of 3.012 V and 7.012 V is considered
as an offset value and the incoming signal of 3 V and 7 V as reference value . With the offset
operation the 3 V and 7 V channel line is shifted by 0.012 V. This is graphically indicated on the
available measurement range column which is now reduced (red section).

Figure 7.21 - Updated Offset Values

The data of the offset dialog can be exported as .TXT file.

Figure 7.22 - Export Offset Data to .TXT File

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

92

7.2.4 Shunt Check

The shunt check function is only implemented for the strain gauge module Sx-STG. A strain
gauge is used to measure structural load e.g. a chassis frame.

During installation and test sensors can be overstretched or damaged. This overload or damage
of the sensor is not visible without applying a shunt check. Those damages can result in wrong
measurements.

Shunt check is used to verify the installed sensor. Shunt checks are performed before and after
a measurement. The step response of the shunt check must be the same before and after the
test.

Figure 7.23 - Shunt Check Dialog for Strain Sensors

When the shunt check is raised the bridge resistance is measured and the results are displayed

Need to input the information.- AMIT

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

93

7.2.4.1 Hotkey Operation: Offset Adjust and Shunt Check

You can operate IPEmotion through hot keys. This is practical for re-occurring operations in
situations where manual navigation with a mouse is too difficult. In the list box Command you
select the a specific function from a work space. Then you define the key to execute this com-
mand. Valid hot key combinations are those which do not create any characters (letters, num-
bers or special signs).

With a hotkey you can access to functions without using the software user interface. For the
offset adjust and shunt check operation and many other functions custom hot key can be con-
figured in the options.

Figure 7.24 - Hotkey Operation: Offset Adjust and Shunt Check

7.2.4.2 Adding a Hotkey for Offset Adjust and Shunt Check

To add a new hot key function you need to select the required workspace area first. Within each
area, the dedicated functions are implemented.
In the example of shunt check or offset adjust you need to select the Area: Signals. Once the
function is selected, click the down arrow to expand the dropdown further later you select and
define the hotkey function via keyboard.

Figure 7.25 - Hotkey Functions

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

94

7.3 Access

7.3.1 Detect

When you start working with your analog measurement modules you need setup the hardware
and cable sets as discussed above. A supported CAN card hardware and power supply is
required. The simple way to get started is to run the Detect function as indicated below.

Figure 7.26 - Detect

The Detect function is a very convenient function to identify any hardware connected to the IPE-
motion software. Not every PlugIn supports automatic hardware detection. Usually, USB device
interfaces support automatic hardware detection.

The Detect function is applied to all active PlugIns. It is recommended to use the Detect func-
tion only for the very first time when you start to set up your measurement configuration. If the
hardware configuration changes by adding or removing the modules, you need to execute the
Synchronize function to update the complete hardware configuration in the system tree.
For more details on the Synchronize function, please refer to "Synchronize" on page 98 .

The user can customize the name of the channel as per their usage or requirement of the mod-
ules and to factory reset the modules, click "Reset" on page 101.

Figure 7.27 - M-modules and Custom Channel Naming

If you execute the Detect function the complete configuration of
Signals of all connected devices is recreated. Additionally, all the
configurations from the Acquisition work space are removed.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

95

7.3.1.1 Mapping

The Hardware Mapping is a very convenient function for merging configuration (IWF) files to
the currently connected hardware. If you execute the Mapping function, the current con-
figuration is compared to the currently connected hardware. IPEmotion starts the hardware
detection to identify all currently connected modules.

The Mapping function compares the current configuration (IWF) to the currently detected hard-
ware across all PlugIns.

Figure 7.28 - Mapping

The Mapping function only support those PlugIns which support
automatic hardware detection.

In the below example you will see how to use the mapping function in practice. There are
applications in which the same configuration is applied to different hardware setups.
For example, every IPETRONIK module consists of an unique front number. When you
initiate the Mapping process it detects one new module as shown below, with the mapping func-
tion you can match the actual hardware configuration to the configuration file.

Figure 7.29 - Configuration and New Detected Hardware

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

96

You can define several mapping relations by linking one module from the right side to one mod-
ule of the left side.
In order to perform the mapping, you need to select the modules that you like to map from the
detected hardware to the corresponding configuration. The mapping process works basically
from right to left with the arrow button to save the mapping between the modules.

To map the newly detecte device, do as follows:

1. Select the modules you like to map (one on each side only)

2. Press the [←] button to execute the mapping process.

Figure 7.30 - Mapping Process

The Mapping function can be applied across different modules of same types.
The system does not let you to map different modules with characteristic.
For example: M-SENS module to a M-THERMO module.

When you confirm the mapping process via the OK button the new module type including the
device serial number is updated. However, the channel configuration remains untouched.

Figure 7.31 - Old and New Module Mapping

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

97

7.3.1.2 Synchronize

The Synchronize function is designed to update an initial configuration (IWF) with an updated
hardware setup. Synchronizefunction is the counterpart of the Detect function.

As discussed above the Detect function helps to create your initial module setup. In practice the
module setup can change where new modules are added or removed to the configuration. With
the Synchronize function you can update your modules easily to your configuration.

Figure 7.32 - Synchronize- Before Sync

The Synchronize function do not change any configurations defined in the
Acquisition work space.

If you make changes to your measurement hardware by adding new modules or removing
modules, it is recommended to use the Synchronize function to reflect the hardware changes in
your module tree. When you click Synchronize after adding the new modules to the hardware
setup they are added to the tree on the left pane.

Figure 7.33 - Synchronize - After Sync

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

98

If in case the modules are removed, an error icon is shown in front of the module serial number.

Figure 7.34 - Sync - Error

7.3.2 Initialize

With the Initialize function you can test the communication between your hardware and
IPEmotion.

If there are any configuration errors or the hardware cannot be reached, messages are
displayed in the message tab. Depending on the PlugIn version the error, info or warning icons
are indicated.

Figure 7.35 - Initialize

The Initialize function updates the connected hardware with the latest configuration
parameters defined in IPEmotion. The configuration is downloaded to the devices, so when you
run a hardware detection the latest configuration settings like channel name, scaling etc., are
automatically retrieved from the module and displayed in IPEmotion. However, in many cases
the hardware cannot store a configuration. In this case, the configuration is stored only in the PC
but is not transferred and stored in the hardware.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

99

Configuration settings that are stored in the IPETRONIK modules internally:

▶ Channel name

▶ Physical units

▶ 2-Point scaling

▶ Free 2 point scaling

▶ Factor offset scaling

▶ Sensor measurement range

▶ STG mode

▶ Data type (format)

▶ Characteristic curves (for X-modules only) (Refer to "Characterstic Curve Tab (X-Modules)"

on page 174).

Configuration settings that are not stored in the IPETRONIK modules internally:

▶ Channel Description

▶ NoValue

▶ V-TAB (Refer to "VTAB " on page 150)

▶ V-TAB range (Refer to "VTAB Ranges" on page 149)

▶ Multipoint scaling (Refer to "Multipoint Scaling" on page 147)

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

100

7.3.2.1 Reset

The reset function is for the instruments which can store a configuration in the device. After
reset, all configurations stored inside the device are set back to factory default.

Figure 7.36 - Reset to Default / Factory Settings

The Reset is applied to all PlugIns which support the Reset function. The
Reset function is implemented and used for IPETRONIK modules and data log-
gers as these instruments can store default configuration.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

101

7.3.3 Display

The Display button turns your configuration into measurement mode. Then the user can view
the measurement values for all active channels.

Figure 7.37 - Display Online Measurements

7.3.3.1 Quick Analyzer

With the Quick analyzer you get a direct preview to the channel signal. The analyzer
performs auto scale and shows the current value. Within the instrument you can switch easily
between channels of the same module. Some of the IPETRONIK X-Modules with the latest
firmware support a Fast Setup functionality. With the Fast Setup, some channel properties can
be changed without device initialization. These configuration elements are performed on the fly
while measuring without interrupting the actual measurement.

Figure 7.38 - Quick Analyzer

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

102

Figure 7.39 - Quick Analyzer Window

Only X-Modules and M3-Modules support fast setup functionalities and refers to
software filter settings, offset adjust and shunt check. The function shunt check is for the strain
gauge inputs. The offset adjustment is supported on all voltage inputs.

Figure 7.40 - Quick Analyzer - Offset and Shunt Check Adjustment

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

103

The default time window or update rate of the quick analyzer scope window is 1000 ms (1
second). However, if you access the properties via a right click on the x (time axis), you can
change the display time range from 0.001 ms (1 micro second) up to 2000 ms (2 seconds).
For more details on the Block factor, please refer to IPEmotion Software Manual.

Figure 7.41 - Quick Analyzer - Time Range / Update Settings

In the quick analyzer window you can also set the Sensor excitation for the X-modules
during the fast setup.

Figure 7.42 - Quick Analyzer - Sensor Excitation

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

104

7.4 View

7.4.1 Details Area

With the Details button in the ribbon you can view or hide all detail tabs for systems, modules
and channels configuration.

Figure 7.43 - Details Enabled

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

105

7.5 System Tree

7.5.1 Column Chooser

Column chooser lets the user to view or add additional properties to the devices and modules
connected via IPEmotion. The user can right click on the column header and activate the
column chooser in the system tree. The scope of functions in the column chooser depends on
the scope of the implementation of the PlugIn.

Figure 7.44 - Column Chooser

In the example below 3 additional columns are added on device and try to indicate the Front
number, Device Type and Firmware version. You can filter and sort across all
additional columns if required.

Figure 7.45 - Column Chooser on Module / Device Level

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

106

7.5.2 Context Menu

The context menu offers convenient functions for setting up your application. With right click on
the system, module or channel you can access the context menu. The functions provided in
the context menu depend on the PlugIn. Some PlugIns offer plenty of functions and other just
provide some basic functions.

Figure 7.46 - Context Menu

▶ Components: The user can add the components to modular hardware structure based on
the requirements. Components can be added in the Ribbon and as well as from the Con-
text Menu, please refer to "Components" on page 81.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

107

▶ Change into: Change into function can convert a component/module to another type.

Basically, if you build your configuration offline and you change the type of some modules
without rebuilding the complete configuration, you switch modules with the ”Change into”
function.
The Change into function will also try to shift the software configuration to the new module
provided the function are supported. The configuration between SENS modules is most
likely compatible. When the configuration is transferred between module types, the sensor
excitation is set to zero as modules support different sensor excitation types (unipolar or
bipolar) and sometimes different voltage levels.

Figure 7.47 - Change Into

▶ Functions: With the Functions you can do Firmware update by right click on the system
on CAN or ETH interface level. However, on Module level you can run an offset-adjust of
all channel or different channel groups when those groups are defined. You can also
access the Functions from the ribbon, please refer to " Firmware Update " on page 81

Figure 7.48 - Function Options

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

108

▶ Import/Export: This function refers to the same function as implemented in the main rib-

bon. There are plenty of different import and export functions available. It is mainly related
to configuration files like A2L, CANdb, Autosar etc. For more details, please refer to "Import
and Export" on page 85.

▶ Adjust TEDS: For more details on TEDS, please refer to "TEDS" on page 86.

▶ Use as default: This function is useful for all users who need to create the same con-

figuration several times. If the user saves the master configuration as Default, all systems
are created with this order of modules, automatically. The default configuration is saved
and can be deleted in the File menu and the user can only define one template for one
interface.
For example: You cannot have different module configurations for IPETRONIK X.

Figure 7.49 - Use as Default Template

▶ Cut: With the cutting function you can cut out selected modules. After cutting components
you can paste them in other sections of the system tree. There is a difference between
”Paste” and ”Paste behind”.

▶ Paste: Insert on module.

▶ Paste behind: Inserting all modules you have cut out and paste them behind a selected

module.

▶ Copy: With the copying function the user can duplicate the one module or a list of selected

modules.

▶ Delete: With ”Delete” the user can permanently remove the items from this configuration.

▶ Clean: The ”Clean” function only works on an interface or system level. With clean function

the user can remove all modules beneath the interface.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

109

▶ Copy to file: With this function the user can save module configurations in a separate file

with the extension .ITF. The .ITF file can be imported, as well.

▶ Paste from file: Import .ITF files which include all selected modules, channels and con-

figuration elements.

Figure 7.50 - Import ITF file

▶ Properties: If you select ”Properties” from the Context menu, another display pop up

opens summarizing the Settings tab for configuration. The properties are context sensitive.
If you select a module you will get the context for Module configuration. If you open the con-
text menu on Channel level you can see all configuration tab sheets related to the channel.
You can also view the properties by selecting the Details on the ribbon. Please refer to
"Details Area" on page 105.

Figure 7.51 - System Properties

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

110

Figure 7.52 - Module Properties

Figure 7.53 - Channel Properties

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

111

7.5.3 M3 Module Order

With the new M3 module generation, the modules detected order in the software system tree is
same as their physical location in the measurement chain. This has significant benefits com-
pared to the older M2 and X-Module series. Here the user can back trace better in case of mod-
ule problems or replacement activities in the measurement chain.

Figure 7.54 - M3 Module Order

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

112

8 X-PlugIn Interface Configuration

As discussed in the earlier sections the IPETRONIK X-PlugIn is the main module product lines
available for CAN bus or Ethernet communication. Both CAN and Ethernet interface settings
are discussed below. There are also plenty of device-specific tab settings which are
individual to each PlugIn. Detailed descriptions about different settings are part of the individual
PlugIn manuals.

8.1 System Details Area

8.1.1 General Tab

Figure 8.1 - General Tab

▶ Active: Here you can activate or deactivate the system.

▶ Name: Here you can define the name of the system.

▶ Description: Here you can define an individual description for the system.

▶ Reference: The reference is automatically generated and defined by the software.

▶ Comment: Here you can add a comment.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

113

8.1.2 Ethernet Hardware Tab

Figure 8.2 - Ethernet Hardware

▶ IP4 address range: The default IP4 address range for the X-modules is defined as

192.168.232.1 to 192.168.232.40. However, in some cases the company Ethernet network
settings can require a different IP-address range which can be modified in the PlugIn
Options discussed in "Ethernet Interfaces Settings" on page 14.

▶ Network interface: Here, the name of the network interface of the computer or data logger
is indicated. This information is indicating on with Ethernet port the modules are connected.
The fist X-Module is working as a DHCP server and assigns the right IP-address matching
to the module factory settings.

▶ X-Link load: This is a calculated statistical value indication how much data is running over

the Ethernet interface.

▶ Internal time synchronization: The Precision Time Protocol (PTP) time synchronization
master is installed together with the PlugIn to synchronize the time between modules.
However, in some cases external time synchronization might be required.

▶ Default send interval: The Ethernet communication support block data transfer with is

sending data every 10 ms which is equal to 100 Hz. However if higher block data transfer is
required it can be deactivated. In this case the block data transfer is every 2 ms with is
equal 500 Hz.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

114

The X-module assigns an IP-address to the LAN port of your computer. The X-module operates
as a DHCP server. However, if your computer requires a different IP-address range because IT
policies you can change the IP-address range of the modules in the X-PlugIn settings.

Figure 8.3 - Ethernet- Computer Network Settings

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

115

8.1.3 CAN Hardware Tab

Figure 8.4 - CAN Hardware Settings

▶ Medium: The automatic hardware detect function identifies all CAN interfaces

implemented in the CAN server. A list of all supported CAN interfaces ID are provided in the
dropdown.

▶ Serial Number: The automatic CAN hardware detect process is also identifying the serial

number of the CAN interface devices. In the cases you start a dry configuration without any
hardware available you can type in the serial number manually of the hardware which will
be used.

▶ CAN bus: When the device has more than one CAN interface, the CAN server will identify

on which CAN port number where the module are connected.

▶ Device baud rate: The factory settings for the M-Modules have a CAN bus baud rate of

500 K Baud. However depending on cable length, the baud rate can be set to lower values.
For more information on cable length, please refer to "M-Modules Cable Length" on
page 40.

▶ Bus load: The bus load is a calculated statistical value by the CAN server, indication how

much data is running over the CAN bus.

▶ Baud rate initialization: Here you can define if the Baud rate configured above will be ini-

tialized to the modules.

Additional CAN interface settings like supported CAN card vendors, scanning baud rates, CAN
ID placing etc., can be configured in the PlugIn Options, please refer to "CAN Interfaces Set-
tings" on page 16.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

116

8.1.3.1 Module Health Status Channels

The M3-Module generation is supporting internal health status information as separate chan-
nels. These channels can be activated as an optional components from the module context
menu.

Figure 8.5 - M3-Module Health Status Signals

▶ Device supply voltage: Indicates the level of supply voltage.

▶ Device supply current: Indicates the supply current to the module.

▶ Device power consumption: Calculates the power consumption of the individual

module.

▶ Device temperature: Indicates the internal temperature of the module.

▶ Channel error status: Indicates the channels error status for "sensor break" and sup-

ports the same sample rates 1 / 2 / 5 / 10 Hz.

Depending on the device type, the signal is defined as 8-Bit or 16-Bit
unsigned integer value.

▶ If the device has 8 input channels, then the signal data type is 8-

Bit integer unsigned.

▶ If the device has 16 input channels, then the signal data type is

16-Bit integer unsigned.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

117

▶ Status undervoltage: Provides 0 or 1 status when the module is operated in the under-

voltage range. The minimum voltage for operation is 6 V.

For the X-Modules only the Status undervoltage is implemented.

Figure 8.6 - X-Module Health Status Signal

▶ Status undervoltage: Provides 0 or 1 status when the module is operated in the under

voltage range. The minimum voltage for operation is 6 V.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

118

8.1.4 Options Tab

Figure 8.7 - Options Tab

▶ Automatic CAN ID placing: With this check box you can define where the software will
assign automatically the CAN IDs starting from the CAN ID defined in the box below.

▶ Start CAN ID: Here you define the first CAN ID to start the automatic placing. The start

CAN ID can be displayed in a hex, decimal or in the binary format. The CAN ID range 640-
767 is used internally by the modules and will be skipped in the CAN ID placing routine.
With the column chooser function you can add the CAN IDs information to the channel grid
to display the software assigned IDs.

▶ Excluded CAN IDs: Here you can load a DBC file and exclude CAN IDs from the automatic
generation process. This is particularly useful in the case the CAN measurement modules
are integrated to another CAN bus data stream to ensure that there is no overlap of the
CAN IDs from different CAN buses.

▶ Name out of serial numbers: With this function all channel names are generated auto-
matically considering the module serial number followed by an incrementing index for the
channel number.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

119

8.2 Module Details Area

8.2.1 General Tab

Figure 8.8 - General Tab

▶ Active: You can activate or deactivate the module.

▶ Name: You can define the name of the module. The default name is based on the serial

number.

▶ Description: You can define an individual description for the module.

▶ Reference: The reference is automatically generated and defined by the software.

▶ Comment: Here you can add a comment.

▶ Sampling rate: In the drop down box, the sample rate for the module can be defined. The

sample rate is set for the entire module. The lowest sample rate is 1 Hz and the fast sample
rate is depending on the module type and can reach up to 5 kHz for the SIM-STG module.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

120

8.2.2 Extended Tab (For CAN-Modules)

Figure 8.9 - Extended Tab (For CAN-Modules)

▶ Front number: In this field the device front number is displayed. When you run a detect

function the front number is automatically detected and extracted from the serial number.
The serial number is composed of the front number and the device type number.

▶ Clock: The default configuration is the Free-running mode. However, a synchronized mode
is supported too, where the first module operate as a Master and all the other modules as
Slaves. The clock can only be changed in the PlugIn settings discussed in the section,
"CAN Interfaces Settings" on page 16.

▶ CAN bus load: This is a statical value calculated by the PlugIn. Higher sample rates will

increase the bus load.

▶ 29-bit identifier: With this check box you can activate the extended CAN identifier. The

standard CAN identifier is 11-bit.

▶ Time before 1st data [in ms]: Please refer to "Options Settings" on page 18.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

121

8.2.3 Extended Tab (For X-Modules)

Figure 8.10 - Extended Tab (For X-Modules)

▶ Front number: In this field the device front number is displayed. When you run a detect

function the front number is automatically detected and extracted from the serial number.
The serial number is composed of the front number and the device type number.

▶ Signal simulation: Signal simulation parameter can be configured by a drop down box
either in channel grid's column 'Signal simulation' or on the module configuration page
'Extended'.

On the Module's configuration page 'Extended', the user can select one of the following set-
tings for 'Signal simulation' parameter:

▶ Off

▶ Sawtooth

▶ Multiple settings: Multiple settings has only informational character to reflect, that the

device's channels have different settings.

▶ If the channel's settings are all identical, this setting is hidden.

▶ If any one of the channel's settings are changed, this setting is visible.

Selecting 'Off' or 'Sawtooth' will set all measurement channels into the corresponding sim-
ulation mode.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

122

Figure 8.11 - Signal Simulation

▶ CAN send rate: This function is only available when on channel level a CAN output is con-

figured.

▶ CAN bus load: This is a statical value calculated by the PlugIn. Higher sample rates will

increase the CAN bus load.

▶ X-Link load: This is a statical value calculated by the PlugIn. Higher sample rates will

increase the Ethernet bus load.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

123

8.2.4 Information Tab

Figure 8.12 - Information Tab (M2-Modules and X-Modules)

▶ Calibration date: In this field the last calibration date is indicated.

▶ Hardware version: In this field the hardware version of is indicated.

▶ Firmware version: In this field the current firmware version is indicated. The firmware can

be updated as discussed above in the section, " Firmware Update " on page 81.

▶ License information: Some modules support additional licensing functions like the TEDS

functionality, additional DSP filters and the FAST sample rates. These licenses are
delivered from the company as a part of the order. However, it is also possible to update the
modules with new license after purchase.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

124

Some modules provide additional information.

▶ The M3-Modules provide additional information about the Adjustment date, Download

kernal version and Device variant.

Figure 8.13 - Information M3-Modules

▶ The SIM STG and all Ethernet X-modules provides information about the FPGA version.

▶ The MULTIdaq and M-SENS24 indicate a Cluster information which includes the serial

number and the size of the cluster. On module level inside the cluster additional information
about the cluster position and the sub-serial number of the individual device is indicated.

Figure 8.14 - Cluster Information

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

125

The M-FLOW device provides information about the M-FLOW signal conditioning unit and sep-
arate information about the flow turbine. A firmware updated is not supported via X-UPDATE
function of the PlugIn.

Figure 8.15 - M-Flow Information

8.2.4.1 Module License Update

In order to perform a license update, you need to detect the module in the first place. After that
you add the module specific license key into the IPEmotion license dialog. With the assign
function in the license dialog the new license key is activated on the module. After the detection
of the new hardware, new licenses information is displayed.

Figure 8.16 - Module License Update

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

126

8.3 Channel Configuration

8.3.1 Column Chooser in the Channel Grid

In the channel grid head line you can access the context menu to add additional columns to your
channel grid. The available columns depends on the PlugIn.

Figure 8.17 - Column Chooser

You can add your own columns into your channel grid. In order to add individual columns you
need to create a new xml file called: Customize.XML in the installation directory.

▶ C:\Program Files\IPETRONIK\IPEmotion 2024 R2\Customize.xml.

Figure 8.18 - Customize.XML - User Defined Key Fields

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

127

With the ”readOnly” status (true/false) you define if the field can be edited though the channel
grid. XML Code to be included in the customize.xml file:

Customize.xml

<Settings Version="1">
<UserDefinedKeyValues>
<UserDefinedKeyValue>
<index>1</index>
<name>testKey1</name>
<caption>Key1</caption>
<description>My own key 1</description>
<readOnly>false</readOnly>
</UserDefinedKeyValue>
<UserDefinedKeyValue>
<index>2</index>
<name>testKey2</name>
<caption>Key2</caption>
<description>My own key 2</description>
<readOnly>false</readOnly>
</UserDefinedKeyValue>
<UserDefinedKeyValue>
<index>3</index>
<name>testKey3</name>
<caption>Key3</caption>
<description>My own key 3</description>
<readOnly>true</readOnly>
</UserDefinedKeyValue>
</UserDefinedKeyValues>
</Settings>

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

128

The following screenshot shows a channel grid which includes 3 individually defined ”KEY
fields”.

Figure 8.19 - Key Fields

The following list provides an overview of all additional column chooser fileds.

Not all modules support all functions.

▶ Active

▶ Aliasing-free

▶ Averaging

▶ Averaging depth

▶ Bridge resistance

▶ Bridge type

▶ Bus type

▶ CAN FD

▶ CAN identifier [hex]

▶ CAN send rate

▶ Channel controller version

▶ Comment

▶ Connection

▶ Cyclic

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

129

▶ Data type

▶ DC compensation

▶ Decimal places

▶ Default value

▶ Description

▶ Display Max

▶ Display Min

▶ Display name

▶ Edge

▶ Factor

▶ Frequency time out mode

▶ Gate time

▶ Group

▶ Hardware filter

▶ IEPE highpass filter

▶ Ignore frequency drop

▶ Index

▶ Info 1

▶ Info 2

▶ Input

▶ LSB

▶ NoValue

▶ Offset

▶ Offset value

▶ Output

▶ PAK active

▶ Phys High

▶ Phys Low

▶ Phys Max

▶ Phys Min

▶ Port

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

130

▶ Reference

▶ Reference 1

▶ Reference 2

▶ Reference 3

▶ Reference 4

▶ Reference 5

▶ Reference 6

▶ Reference 7

▶ Reference value

▶ Reset value

▶ Sampling rate

▶ Selected Curve

▶ Selected Medium

▶ Sensor break detection

▶ Sensor calibration

▶ Sensor excitation

▶ Sensor High

▶ Sensor Low

▶ Sensor Max

▶ Sensor Min

▶ Sensor mode

▶ Sensor name

▶ Sensor serial

▶ Sensor unit

▶ Set start value

▶ Shuntcheck resistance

▶ Shuntcheck tolerance

▶ Signal output medium

▶ Signal simulation

▶ Software filter cutoff frequency

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

131

▶ Software filter type

▶ Source

▶ Source type

▶ Start value

▶ Static direction input

▶ Status

▶ Subconfig

▶ Symbol

▶ Threshold on

▶ Transformation

▶ Unit

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

132

8.4 Channel Details Area

8.4.1 General Tab

Figure 8.20 - General Tab

▶ Active: Checkbox to activate or deactivate a channel.

▶ Name: Default name but can be changed to individual names.

▶ Description: Default description but can be changed to any individual description.

▶ Reference: Is automatically generated and very useful to check where the channel is linked

to.

▶ Comment: Here you can add a comment.

▶ Sampling rate (X-Modules Only): Select the module sample rate from the drop down list.

8.4.1.1 Defining the List Box Entries of Channel Names

For the channel name you can also define a pull down menu.

Figure 8.21 - Channel Names

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

133

The entries of the pull down menu are stored in a CSV file with the name (ChannelNames.csv)
in the following user settings directory.

▶ C:\ProgramData\IPETRONIK\IPEmotion 2024 R2\UserSettings.

Figure 8.22 - Structure of the ChannelNames.csv file

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

134

8.4.2 Format Tab

The Format tab sheet is only visible for the users who activates this function in
Options→Expert mode→Extended tabs. In the Format tab sheet we can configure a couple
of functions which are usually only relevant for expert users. The different configuration func-
tions are explained below.

Figure 8.23 - Format Tab

▶ Data type: This refers to the data format (resolution) of the measurements. Depending on
the module/instrument, sometimes different formats are supported. On most of the instru-
ments, it is not possible to change the configuration of the data type. They always transmit
data in the same format. For IPETRONIK modules the signed or unsigned format is import-
ant.
Some modules support a change in the data type format from a drop downlist as indicated
below.

Figure 8.24 - Data type Change

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

135

▶ Task: The task is a very special setting developed for some specific PlugIns.

▶ Task (GPS Recording): The settings for a special task are needed for the GPS sig-

nals. This sensor sends the NMEA protocol in a special format and in order to convert
this signal to a standard format which can be used by IPEmotion, the measurement
channels need a task configuration for longitude, latitude etc., to get a correct data
dispaly in the map instrument in the Analysis works pace. A correct configuration of
the task is also required when you would like to save or export data in the GPX format.
The coordinates longitude, latitude and altitude are only correctly interpreted in the
GPX export when the corresponding task is defined.

Figure 8.25 - Task (GPS Recording)

▶ Task (Audio Recording): When you like to record audio e.g. via an MX-SENS2 4

FAST module or over the PC-Sound PlugIn you should check the setting of the task
which should configured to ”Audio mono”.

Figure 8.26 - Task (Audio Recording)

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

136

▶ NoValue: This configuration is important for all users who would like to see a certain beha-
vior when NO measurements are received in the IPEmotion. The default configuration is
that NoValues are recorded in the data file. They are indicated as NoValue in the Data
manager. In the Yt-chart in the Analysis work space you will see missing data points in
the graph. The software will always store NoValue in the data file
irrespectively what you select from the drop down box. In the data file NoValue is stored
and in the diagrams you will see missing data points.

▶ DefaultValue: Another configuration option is a check box to enables the DefaultValue.

With this check box you change the storage and display behavior when no measurements
are received. With the check box you can show and store +FullScale,
−FullScale or NULL as a numerical value. (You can only select NULL if you have a signed
+− measurement range data format). An unsigned measurement is only covering positive
measurements.

Drop down selection has no impact when the check box
"Deactivate Novalue" is deactivated.

Figure 8.27 - NoValue/DefaultValue

Figure 8.28 - Data Manager and Analysis

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

137

The NoValue configuration also has an impact on the data display in the View work area. As
the screen shot below indicates. When the check box ”Deactivate NoValue and use
DefaultValue” is not activated the instrument will show always Novalue.
Filter has an impact when check box "Deactivate NoValue" is activated. In this example
+FullScale of the measurement range will be stored.

Figure 8.29 - Activate the Default Value

However if the check box ”Deactivate NoValue and use Default Value” is activated you will
enable the the list box entries and the instrument will show the selected values for:

▶ +Full Scale

▶ -Full Scale

▶ Null

Figure 8.30 - Data Manager and Analysis

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

138

DefaultValue Null: The DefaultValue (NULL) is related to the Null value of the binary
measurement range. If you select a signed 16-Bit (2^16 = 65536) measurement range, the
temperature signal for the IPETRONIK thermo module it is split up between the values
-65.536 and +65.536 as the graphic demonstrates below.

Figure 8.31 - DefaultValue Null

Figure 8.32 - NoValue=NULL

The binary NULL value of this measurement range is 655 °C. This value is then indicated to the
online instruments and stored in the data file.

Figure 8.33 - NULL Value

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

139

Figure 8.34 - Data Points for NULL Shows 655°C

▶ Channel type: The channel type indicates the data direction Input or Output.

Output channels can be updated through manual entries, through slide controllers or alpha-
numerical displays in the View work area. Some PlugIns support channels which can be
operated as input and output.

Figure 8.35 - Channel Type

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

140

8.4.3 Scaling Tab

IPEmotion Sensor Scaling - Please refer to the video link: https://youtu.be/7uWNIrpT0AM to
understand "How do Analog Sensors Work".

Figure 8.36 - Scaling Tab

The basic scaling operations can be defined directly in the scaling tab sheet. The scope of
functions depends on the PlugIn and IO module type. Some inputs, especially analog inputs,
support many different functions, ranges and provide more scaling options.

▶ Sensor mode: The sensor mode covers the main measurement type, for example Volt or

Current, accelerometers (IEPE). You can select the sensor mode from your drop-down list.
In this example, the analog input module supports many different measurements of thermo
element. The supported sensor modes are defined by the PlugIn and you can only select
the mode which is supported. Many modules only support one static sensor mode.

Figure 8.37 - Sensor Mode and Thermo Module Example

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

141

▶ Sensor range: The next configuration option is the sensor measurement range. The range
is related to the measurement mode. For thermo elements, the measurement range is pre-
defined and cannot be changed. The available voltage and current measurement ranges
depend on the functionality of the analog input. In the example below you can select ranges
from -0.1 V up to 100 V. The Unit is automatically linked to the selected
measurement mode Voltage >V or Current >A or Temperature >°C and cannot be
changed manually.

Figure 8.38 - Sensor Range

▶ Physical range and engineering units: The physical range is related to your engineering
units. Here you can define into which unit (mm, bar, etc.) the electrical signal is converted.

Figure 8.39 - Physical Range and Engineering Units

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

142

8.4.4 Scaling Calculator

For advanced scaling functions you can use the scaling calculator. This interface provides many
different scaling functions which is discussed in the below sections.

Figure 8.40 - Scaling Calculator

8.4.4.1 Channel Settings

Figure 8.41 - Channel Settings

▶ Sensor mode: Is related to the type of measurement mode as discussed above in "Scaling

Tab" on page 141.

▶ Sensor range: Is related to the measurement range as discussed above in "Scaling Tab"

on page 141.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

143

▶ Unit: To simplify the conversion between engineering units you can use the change unit

editor. Switching between the units only works within the same engineering unit family like
temperatures, pressures, weight, energy, etc.

Figure 8.42 - Converting V into mV

▶ The main advantage is that the new engineering unit automatically converts the physical
measurement range. As shown in the screenshot, 100 V are automatically converted to
100000 mV. This conversion also works across different metric standards.

Conversion for Example:

Name

Pressure

Unit

Bar >kbar >mbar >psi >etc.

Temperature

C >K >F

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

144

8.4.4.2 2-Point Scaling

This is a classical scaling configuration using two points, usually the Min and Max value of the
physical range of the sensor. The scaling information is included in the data sheet / calibration
sheet of the sensor.

Figure 8.43 - 2-Point Scaling

8.4.4.3 Free 2-Point Scaling

This scaling mode offers the possibility to scale the sensor range and the physical range (engin-
eering units) at the same time.

Figure 8.44 - Free 2-Point Scaling

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

145

8.4.4.4 Factor/Offset Scaling

This scaling method uses the Linear equation Physical value (y) = m *x + b (b= offset) with
(m = slope factor). The m-factor influences the slope >1 steeper slope / <1 flatter slope. The
offset-b shifts the physical value by a constant value.

Figure 8.45 - Factor/Offset Scaling

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

146

8.4.4.5 Multipoint Scaling

The multipoint scaling is a scaling method that allows to define a nonlinear scaling with as many
data points as possible.

The multipoint scaling parameters are only stored in IPEmotion. They are
not transferred to the instrument unless the instrument is supporting this-
function. Please refer to "Introduction to CAN-FD" on page 70.

Figure 8.46 - Multipoint Scaling

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

147

8.4.4.6 STG Strain Gauge

In this interface, strain gauge bridge types like 1/4; 1/2 or full, etc. can be configured.

Figure 8.47 - STG Strain Gauge

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

148

8.4.4.7 VTAB Ranges

This scaling method converts measurements of a specific range into a text message. If the
measurement value is in a defined range you can see the corresponding text information on an
alphanumerical instrument in the View work area.

The multipoint scaling parameters are only stored in IPEmotion. They are
not transferred to the instrument unless the instrument is supporting this
function. For more details, please refer to "Initialize" on page 99.

Figure 8.48 - VTAB Ranges

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

149

8.4.4.8 VTAB

In this mode you can relate a specific integer (1, 2, 3, 4, ..) value to a specific text display. You
can display this text on the View work area for example in an alphanumerical instrument.

The multipoint scaling parameters are only stored in IPEmotion. They are
not transferred to the instrument unless the instrument is supporting this
function. For more details, please refer to "Initialize" on page 99.

Figure 8.49 - VTAB

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

150

8.4.4.9 Active Sensors

Figure 8.50 - Active Sensors

8.4.4.10 Passive Sensors

Figure 8.51 - Passive Sensors

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

151

8.4.4.11 Snapshot - Test Measurement

You can perform a test measurement within the scaling calculator to check your scaling and to
see the actual measurements. Three different test measurements are supported:

▶ Snapshot

▶ Average over values

▶ Average over time

Figure 8.52 - Snapshot

Figure 8.53 - Test Measurements

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

152

8.4.5 Sensor Database

The scaling calculator supports a sensor database. In this database, the scaling parameters of
many different sensors are included. If you select a sensor from the database, you have directly
defined the measurement range and the physical range and, if needed, a sensor excitation.

Figure 8.54 - Sensor Database

In this example, you see a shunt for high current measurements. This shunt can measure ±10
Ampheres and the output of the shunt is ±1 Volt. The sensor requires a 10 Volt sensor excit-
ation.

Figure 8.55 - Shunt Sensor

8.4.5.1 Adding New Sensors to Database

The sensor database (SDB.exe) is installed with each IPEmotion installation in the following dir-
ectory:

▶ C:\Program Files (x86)\IPETRONIK\IPEmotion 2024 R2\Tools

If you like to add your sensor to the existing standard database, it is recommended to import the
standard sensor database. The database is installed in the following directory.

▶ C:\ProgramData\IPETRONIK\IPEmotion 2024 R2\Database

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

153

You can also create your own sensor database XML file from scratch. If you like to use your own
database file, you have to store it in the right directory and give the file the correct name:
IPESensorDatabase.xml

IPEmotion can only work with one database XML file.

You can add new sensor by means of the SensorDB editor. This tool is installed along with IPE-
motion and entries can be made through the GUI.

ADD IMAGE - AMITH- Pending

If you save the new sensor and restart IPEmotion, the new sensor will be included in the data-
base and can be selected for channel scaling. Serial numbers and calibration dates can be
defined, as well.

ADD IMAGE - AMITH - Pending

However, you can import your own database from Excel using the import function of the
SensorDB Editor. The import function is explained in the help manual of the SensorDB Editor.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

154

8.4.5.2 The Database Format

The standard Excel template for importing sensors has the following structure:

▶ sensorName

▶ sensorTypeId (see next page for details)

▶ sensorType

▶ sensorManufacturer

▶ physicalUnitName

▶ physicalMin

▶ physicalMax

▶ outputUnitName

▶ outputMin

▶ outputMax

▶ sensorSupplyMin

▶ sensorSupplyMax

▶ outputProportionalToSupply

▶ referenceSensorSupply

▶ sensorSupplySymetric

▶ sensorSupplyCurrentMax

▶ propertyName1

▶ propertyValue1

▶ propertyName2

▶ propertyValue2

▶ propertyName3

▶ propertyValue3

▶ serialNumber

▶ CalibrationDate

▶ calibrationValidMonths

▶ calibrationValidDays

▶ physicalMin

▶ physicalMax

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

155

▶ outputMin

▶ outputMax

The Sensor type ID:

0=UNKNOWN

User-defined sensor

1=DisplacementTransducer

Displacement transducer

2=LoadCell

3=Shunt

Load cell

Shunt

4=CurrentTransformer

Current transformer

5=VoltageTransformer

Voltage transformer

6=ForceTransducer

Force transducer

7=PressureTransmitter

Pressure transmitter

8=AbsolutePressureTransmitter

Absolute pressure transmitter

9=GaugePressureTransmitter

Gauge pressure transmitter

10=DifferentialPressureTransmitter

Differential pressure transmitter

11=FlowRateTurbine

12=PistonFlowmeter

13=ScrewFlowmeter

Flow rate turbine

Piston flow meter

Screw flow meter

14=VortexSheddingDevice

Vortex shedding device

15=Accelerometer

Accelerometer

16=TriAxialAccelerometer

Triaxial Accelerometer

17=TorqueMeter

18=Counter

Torque meter

Counter

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

156

19=StrainGauge

20=LVDT

STG

LVDT

21=StrainGaugeBridge

STG bridges (Strain)

22=TemperatureSensor

Temperature sensor

If none of the predefined types meets your requirements, you can add user-defined types to the
sensor database. The ”sensorTypeId” value must be set to 0. A short description text should
classify the corresponding sensor.

If you want to use sensors of the same type within the sensor database, use the
”SpecificSensors” entry. Each one of the sensors must get a unique serial number
(”serialNumber”). In addition, each one of these sensors can get a calibration date
(”calibrationDate”), as well as a period of validity of the calibration
(”CalibrationValidDuration”) including the data ”calibrationnValidYears”,
”calibrationValidMonths”, and ”calibrationValidDays”. Furthermore, the values for ”phys-
icalMin”, ”physicalMax”, ”outputMin”, and ”outputMax”, which can be found in the data sheet,
can be overwritten by values, which are read at the calibration.

You can add non-relevant information for the functionality of the sensor data base like the
working temperature range under the ”UserProperties” entry. These are Key/Value pairs,
which are used for displaying the information.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

157

Please note that these data are not used in any calculation. All the sensor data is stored in an
XML file with the following structure.

The sensor names ("SensorName") must be unique.

SensorName

<Sensor name=SSensor2">
<sensorName type=SString">Sensor2</sensorName>
<sensorTypeId type=Ïnt32">7</sensorTypeId>
<sensorManufacturer type=SString">IPETRONIK</sensorManufacturer>
<physicalUnitName type=SString">bar</physicalUnitName>
<physicalMin type="Double">1</physicalMin>
<physicalMax type="Double">50</physicalMax>
<outputUnitName type=SString">V</outputUnitName>
<outputMin type="Double">-4</outputMin>
<outputMax type="Double">4</outputMax>
<sensorSupplyMin type="Double">-5</sensorSupplyMin>
<sensorSupplyMax type="Double">5</sensorSupplyMax>
<sensorSupplyCurrentMax type="Double">0.01</sensorSupplyCurrentMax>
<PreferedSensorModes>
<sensorMode />
</PreferedSensorModes>
<UserProperties>
<UserProperty>
<propertyName type=SString">Genauigkeit</propertyName>
<propertyValue type=SString">+- 4,7 %</propertyValue>
</UserProperty>
</UserProperties>
<SpecificSensors>
<SpecificSensor>
<serialNumber type=SString/>
</SpecificSensor>
<SpecificSensor>
<serialNumber type=SString">SN01277</serialNumber>
<calibrationDate type="Date">2012-04-04</calibrationDate>
<CalibrationValidDuration>
<calibrationValidYears type=Ïnt32">1</calibrationValidYears>
<calibrationValidMonths type=Ïnt32">6</calibrationValidMonths>
<calibrationValidDays type=Ïnt32">0</calibrationValidDays>
</CalibrationValidDuration>
<outputMin type="Double">-3.895</outputMin>
<outputMax type="Double">4</outputMax>
</SpecificSensor>
</SpecificSensors>
</Sensor>

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

158

8.4.5.3 Multipoint Linearization

The sensor data base is supporting sensor linearization functions. You can add for sensors mul-
tipoint linearization into sensor data base XML file. In the XML file you can add value pairs of
”Physical reading / Sensor Output”.

Figure 8.56 - Multipoint Linearization

The sensor specific linearization information can only be added through the
XML file directly. The Sensor Database Editor and the corresponding CSV/Ex-
cel import function is currently not supporting this function.

When you select a sensor with linearization values they are directly indicated in the sensor para-
meter overview. In this example the scaling is integrated to the ”Sensor type properties”.

ADD IMAGE AMITH- Pending

The linearization values are imported from the sensor database into the multipoint scaling mode
with a graphical presentation of the calibration curve.

ADD IMAGE AMITH- pending

You can integrate multi point scaling also to the ”Sensor specific” properties.

ADD IMAGE AMITH- pending

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

159

8.4.5.4 Adding New Sensors

The sensor data base is a powerful tool to simplify the channels scaling and reduce scaling
error. You can now add your own sensor to the data base. All the settings defined in the sailing
interface are saved to the data base. All scaling entry modes are supported to add individual
sensors. For more info please refer to "Scaling Calculator" on page 126.

Figure 8.57 - Adding New Sensors

When the sensor parameters are defined you can add the sensor header information by
accessing the add button.

Figure 8.58 - Sensor Header Information

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

160

After you have created the sensor in the database you can search for your sensor. The example
below shows the parameters as defined in the scaling calculator.

Figure 8.59 - Sensor Properties Defined

When a sensor was added to a user define sensor data base file it is saved in:

▶ C:\Users\Public\Documents\IPETRONIK\IPEmotion\Database\ IPESensorData-

base.xmu

▶ Extension u = User defined sensor database.

If you like to modify a manually created sensor you need select the sensor from the sensor data
base and you can modify settings in the scaling interface. With the function save sensor to data
base the modifications are overwritten.

There is no possibility to delete a sensor from the sensor data base. If you need
to remove a sensor permanently you need to delete it from the XML files.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

161

8.4.6 Terminal Tab

In the Terminal tab, you have the information about the analog input and circuit design. This
function is only available for all X-Modules, M-thermo and new CAN based M3-Module. The
graphic is indicating on which pin which signal is running. The graphic is aligned to the input con-
figuration or measurement mode. Some modules support different modes in one
module like the Sx-STG where IEPE, strain gauge, or voltage measurement can be con-
figured.

Figure 8.60 - Terminal Tab

The terminal tab circuit diagram changes depending on the Sensor mode that the user select in
the Scaling tab. The user can view the circuit diagram in the Terminal tab and also the user can
click on the diagram and enlarge the view for a better understanding.

Figure 8.61 - Scaling and Terminal Tab

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

162

Figure 8.62 - Magnified View

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

163

8.4.7 Display Tab

Display tab covers the display settings for the online View work area. The display tab is also rel-
evant for formula channels and scaling channels. The main configuration elements are:

Figure 8.63 - Display Tab

▶ Displaying area: Covers the initial Y-axis scaling of the y-t chart.

Figure 8.64 - Displaying Area

▶ Formatting: Covers the decimal places. The default setting is Automatic which will show

as many decimal places as provided by the PlugIn.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

164

▶ Name (Display): Covers the display name which can differ from the channel name. The

display name is only relevant for the View work area. The display name will not be used for
formulas and other functions like limit or range monitoring. If you like to see the display
name on the instruments, you need to activate this function in IPEmotion Options → View.

Figure 8.65 - Display Name

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

165

8.4.7.1 Define Standard Decimal Templates on Module Level

When detecting modules, the default setting of the decimal paces is defined as Automatic.
However, if you like to define a default setting for the number of decimal places you like to use
you can add to the Settings.XML a new command line in order to use the template as default.

The settings XML file is stored on the following directory:

▶ C:\ProgramData\IPETRONIK\IPEmotion 2024 R2\Settings.xml

In the settings XML you have to add in the section ”Common Settings” the following
command line: <detectWithTemplate>True <\detectWithTemplate>

Figure 8.66 - Detect Modules

You can disable the function also by setting the command line to "False".
Command line: <detectWithTemplate>False <\detectWithTemplate>

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

166

With this command line you can save a lot of time because all modules will be detected with the
number of decimal places as defined in the template. The template is applied to all channels of
the module. For example: Template with 2 decimal places for the Mx-SENS2 4 is created as
shown below.

Figure 8.67 - Decimal Place and Save the Template

8.4.7.2 Output Tab for Output Channel

The output tab sheet is only visible for analog and digital output channels. Its main function is to
define a start value. This value will be set to the output when you start the measurement. You
can also define an output level. The output level is related to the user administration which is
discussed in detail in the IPEmotion Software Manual → Options →User administration.

Figure 8.68 - Output Tab for Output Channel

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

167

8.4.8 Extended (X-Modules and M3-Modules)

In the X-Modules and M3-Modules signal simulation can be configured individually on meas-
urement channels. However, it is not possible to configure signal simulation for monitoring sig-
nals (device supply voltage, current consumption, etc.).

Allowed values for each measurement channel are:

▶ Off

▶ Sawtooth

Figure 8.69 - Extended - Channel

8.4.9 Excitation Tab

Defines the excitation for the connected channel. The default value is "0" and the sensor excit-
ation range can vary from 0V to ± 15V.

Figure 8.70 - Excitation Tab

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

168

8.4.10 Thermo Tab (M-Modules)

The thermo tab setting is only specific for the M-Thermo Modules. In the M2-Modules the user
can activate/deactivate the Averaging and Sensor break detection, whereas in the
M3-Modules the user can input the Averaging depth value.

Figure 8.71 - Thermo

▶ Averaging depth: Defines window width of the averaging with the minimum value as 1 to
maximum values as 100. For other M-Devices, you can find the Averaging depth option in
the "Filter Tab (M-Modules)" on page 172.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

169

8.4.11 Signal Filters

Filters of analog measuring amplifiers are used for avoiding interrupting frequencies (frequency
spectra, which do not contribute to the signal and/or which cannot be processed by the system).
A low pass filter, which reduces the amplitudes of the frequencies above a specific cut-off
frequency, is usually used for avoiding negative effects to the useful signal. The threshold in the
range of the cut-off frequency (the barrier between the useful and the unrequested signal) is
continuous. Useful signals below the cut-off frequency are also damped. A damping of 3 dB at
the cut-off frequency means a reduction of the initial signal of 30 .

The image below shows the result of two inputs with the same input signal of 4 V amplitude and
12.5 Hz frequency.

Figure 8.72 - Impact of Filter (Signal Shift)

▶ Channel 2: Black curve without filter

▶ Channel 3: Red curve with 30 Hz hardware filter (Bessel type). Channel 3 shows the main
behaviors of filters like the damping, the phase shifting, and the start oscillation of the
filtered signal.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

170

8.4.11.1 Hardware Filters

Although today's microprocessors provide a high processing power, the use of hardware filters
is still essential. Especially when users cannot exclude that (periodic) signals can pass the AD
converter and software filter, which cannot process the signals. Every sampling system follows
Shannons sampling theorem whereby one must at least sample with twice the signal frequency.
Otherwise, aliasing effects can occur, whereas the acquired frequency is considerably lower
than the actual signal (See image "Aliasing Effect" below).

8.4.11.2 DSP Software Filters

The hardware filter at the input excludes a distortion by frequency spectra above the system
limit with the maximum sampling rate. Depending on the application, it can be required to lower
the cut-off frequency.
For example: M-SENS devices provide a switchable hardware filter with 150 Hz cut-off
frequency. If the cut-off frequency is e.g. 50 Hz, interrupting frequency spectra (of devices with
additional software filter) in the range between 50 Hz and the hardware filter frequency can be
filtered with DSP. The filter frequency can be configured in defined steps up to the hardware
filter frequency.

8.4.11.3 Aliasing Effect

Despite sophisticated measurement engineering, errors can occur due to wrong settings.

For example: A 100 Hz signal is acquired with a sampling rate of 100 Hz system can
independently acquire the correct signal, but the result is wrong because the sampling rate was
set too low.

Figure 8.73 - Aliasing Effect

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

171

8.4.12 Filter Tab (X-Modules)

Figure 8.74 - Filter Tab - X-Modules

▶ Hardware filter: For more details, please refer to "Hardware Filters" on the previous page.

▶ Software filter: For more details, please refer to "DSP Software Filters" on the previous

page.

▶ Type: The user can define the filter characterstic to the read the data. There are 3 dif-

ferent types:

▶ Bessel

▶ Butterworth

▶ Elliptical

▶ Frequency: The user can define the frequencty limit.

8.4.13 Filter Tab (M-Modules)

Figure 8.75 - Filter Tab - M-Modules

▶ Hardware filter: For more details, please refer to "Hardware Filters" on the previous page.

▶ Software filter:For more details, please refer to "DSP Software Filters" on the previous

page.

▶ Type: The user can define the filter characterstic to the read the data. There are 3 dif-

ferent types:

▶ Bessel

▶ Butterworth

▶ Elliptical

▶ Frequency: The user can define the frequencty limit.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

172

▶ Averaging depth: For more information, please refer to "Thermo Tab (M-Modules)" on

page 169.

8.4.14 Data Output Tab (X-Modules)

Here you can configure the signal output medium. This configuration setting is only available for
the X-Modules.

Figure 8.76 - Data Output Tab (X-Modules)

▶ Configuration Signal output: You can select the signal output medium as CAN, Ethernet
or Ethernet +CAN. The user can set the CAN send rate for the CAN based output medium
as per the send rates that the module support.

▶ CAN settings: Here the user can define the identifier of the CAN message and first byte of

the signal within the CAN message.

This setting only available to edit when the Automatic CAN ID placing is
disabled. Please refer to "Options Tab" on page 119

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

173

8.4.15 Characterstic Curve Tab (X-Modules)

Here you can configure the use of characterstic curves instead of default sensor mode.

Figure 8.77 - Characterstic Curve Tab

▶ Select curve: You can select the characteristic curve for each invidual channel to use
instead of the default sensor mode. The user can select to configure the characteristic
curve for each channel. - AMITH- Pending

8.4.15.1 Configuring the Characteritic Curve

Need understanding from - AMITH- Pending

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

174

9 Technical Data

The user can download the latest version of IPETRONIK X-PlugIn from the IPETRONIK
official website : https://www.ipetronik.com/en/products-services/software-digit-
alization/plugins.html.

9.1 System Requirements

9.1.1 Minimum System Requirements

▶ Screen resolution: min. 1080 x 800 pixel

▶ Processor: min. 2 GHz

▶ RAM: min. 2048 MB/ 2 GB

▶ IPEmotion Version: min. IPEmotion 2024 R2

9.1.2 Recommended System Requirements

▶ Screen resolution: min. 1920 x 1200 pixel

▶ Processor: min. 3 GHz Multi-Core

▶ RAM: min. 6144 MB/ 6 GB

▶ Storage medium type: SSD

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2024. ALL RIGHTS RESERVED. | VERSION V02.21.00 | OCTOBER 2024

175


