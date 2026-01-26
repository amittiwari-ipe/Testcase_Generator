IPEmotion PlugIn IPETRONIK X
USER MANUAL V02.23.00

July 2025

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00

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

4.2.1.1 Verifying the Installed PlugIn

4.3 X-PlugIn Activation

5 PlugIn Options

5.1 Plugin-specific Settings

5.1.1 Ethernet Interfaces Settings

5.1.2 CAN Interfaces Settings

5.1.3 Device Sorting Option

5.1.3.1 Device Sequence: Default

5.1.3.2 Device Sequence: Descending Serial Number

5.1.4 Options Settings

5.1.5 Components Settings

5.1.5.1 General Procedure for the Devices on the EOL List

6 Hardware Integration

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

10

11

12

12

12

15

18

19

20

21

24

25

26

26

6.1.1 X-Modules Cable Length

6.1.2 Mx-SENS2 4 Fast

6.1.2.1 Input Cables:

6.1.3 Mx-SENS2 8

6.1.3.1 Input Cables:

6.1.4 Mx-STG2 6

6.1.4.1 Input Cables:

6.1.5 Sx-STG

6.1.5.1 Input Cables:

6.1.6 Signal Input Modes

6.1.6.1 STG Mode

6.1.6.2 SENS Mode

6.1.6.3 ICP Mode

6.1.7 TEDS Class 2

6.2 M-Modules

6.2.1 M-Modules Cable Length

6.2.2 M-SENS 8 / M-SENS 8plus

6.2.2.1 Input Cables

6.2.3 M-SENS2

6.2.3.1 Input Cables

6.2.4 M-SENS3 8

6.2.4.1 Input Cables

6.2.5 M-THERMO2

6.2.5.1 Input Cables

6.2.6 M-THERMO2 u

6.2.7 M-THERMO3 16

6.2.7.1 Input Cables

6.2.7.2 Thermocouple Schematics

6.2.8 M-RTD2

6.2.8.1 Types of RTD Configurations

6.2.8.2 Input Cables

6.2.9 M-CNT2

6.2.9.1 Input Cables

6.2.9.2 Input / Principle Details

6.2.10 CANpressure

TABLE OF CONTENTS

26

27

30

31

33

35

36

38

39

41

41

46

48

49

52

52

54

56

57

59

60

63

64

65

65

66

67

68

70

70

74

75

77

78

80

6.2.10.1 Pressure Connections

6.3 Module Identification by Base Type Number

6.4 System Overview

6.4.1 System Architecture

6.4.1.1 Ethernet and CAN Card Interface Architecture

6.4.1.2 Ethernet and CAN Modules Daisy Chain Setup

6.4.1.3 CAN Bus Termination

6.4.2 Connecting Two X-Devices to PC

6.4.3 Detection of Ethernet Adapters with Conflicting IP Addresses

6.5 X-Modules/Ethernet Modules Connection

6.5.1 X-Modules Hardware Setup - Example 1

6.5.2 X-Modules Hardware Setup - Example 2

6.5.3 X-Modules Hardware Setup - Example 3 (CAN Tunneling)

6.5.4 M3-System Connection

6.5.4.1 M3-System

6.5.4.2 M3-System with Gateway

6.5.4.3 M3 and M2-System

6.5.4.4 M3 and M2-System with Gateway

6.5.4.5 X-M3-M2-System

6.5.4.6 X-M3-M2-System with Gateway

6.6 M-Modules/CAN Modules Connection

6.6.1 M-Modules Hardware Setup - Example 1

6.6.2 M-Modules Hardware Setup - Example 2

6.6.3 M-Modules Hardware Setup - Example 3

6.7 LED Indication

6.7.1 M3-System-LED

6.7.2 M3-Channel-LED

6.7.2.1 Thermocouple Color Coding IEC/ANSI

6.7.3 M-Modules Status-LED

6.7.4 M-Modules Channel-LED

6.7.5 X-Modules Status-LED

6.7.6 X-Modules-Link-LED

6.7.7 X-Modules Channel-LED

7 Software Interface

7.1 IPEmotion Signals Work Space

TABLE OF CONTENTS

80

83

86

86

86

87

87

87

88

89

90

91

92

93

93

93

94

94

95

95

96

97

97

98

99

99

101

102

103

104

105

106

107

108

108

7.1.1 Ribbon Main Functions

7.1.2 Create a Measurement System

7.1.2.1 Detect the Hardware

7.1.3 Dry Configuration

7.1.3.1 IPETRONIK X-PlugIn

7.1.3.2 System

7.1.3.3 Components

7.1.3.4 Import and Export

7.1.3.5 CSV Import/Export

7.1.3.6 A2L Export

7.1.4 Configuration Check

7.1.5 Status Signals

7.1.5.1 System Status Signals

7.1.5.2 Device Status Signals

7.1.5.3 Channel Status Signals

7.2 Configuration Adjust Functions

7.2.1 Database

7.2.2 TEDS

7.2.2.1 TEDS Sensor Detection with Automatic Unit Transformation

7.2.2.2 TEDS Adjust on Channel Level

7.2.2.3 Compare TEDS Sensor with Configuration

7.2.3 Offset Adjust

7.2.3.1 Group Offset Adjustment

7.2.4 Shunt Check

7.3 Hotkey Operation: Offset Adjust and Shunt Check

7.3.1 Adding a Hotkey for Offset Adjust and Shunt Check

7.4 Access

7.4.1 Detect

7.4.1.1 Mapping

7.4.1.2 Synchronize

7.4.1.3 Device Detection on Different Baudrates for Hardware Ini-
tialization

7.4.2 Initialize

7.4.2.1 Reset

7.4.3 Display

TABLE OF CONTENTS

108

108

108

109

109

110

111

113

113

114

116

117

117

120

123

126

126

126

128

130

131

132

135

136

138

139

140

140

141

143

145

146

148

149

7.4.3.1 Quick Analyzer

7.4.3.2 Tune-up

7.5 View

7.5.1 Details Area

7.6 Firmware Update

7.7 Module License Update

8 X-PlugIn Interface Configuration

8.1 System Tree

8.1.1 Column Chooser

8.1.2 Context Menu

8.1.3 M3-Module Order

8.1.4 X-Modules Order

8.1.5 Module Health Status Channels

8.2 System Details Area

8.2.1 General Tab

8.2.2 Ethernet Hardware Tab

8.2.3 CAN Hardware Tab

8.2.4 Options Tab

8.3 Module Details Area

8.3.1 General Tab

8.3.2 Extended Tab (For CAN-Modules)

8.3.3 Extended Tab (For M3-Modules)

8.3.4 Extended Tab (For X-Modules)

8.3.5 Information Tab

8.4 Channel Configuration

8.4.1 Column Chooser in the Channel Grid

8.4.2 Column Chooser Fields

8.4.3 Channel Supporting Reset to Factory Default

8.5 Channel Details Area

8.5.1 General Tab

8.5.1.1 Defining the List Box Entries of Channel Names

8.5.2 Format Tab

8.5.3 Scaling Tab

8.5.4 Scaling Calculator

8.5.4.1 Channel Settings

TABLE OF CONTENTS

150

153

154

154

155

158

159

159

159

160

167

168

169

171

171

172

174

175

176

176

177

178

182

183

186

186

186

190

191

191

192

193

198

200

200

8.5.4.2 2-Point Scaling

8.5.4.3 Free 2-Point Scaling

8.5.4.4 Factor/Offset Scaling

8.5.4.5 Multipoint Scaling

8.5.4.6 STG Strain Gauge

8.5.4.7 VTAB Ranges

8.5.4.8 VTAB

8.5.4.9 Active Sensors

8.5.4.10 Passive Sensors

8.5.4.11 Snapshot - Test Measurement

8.5.5 Sensor Database

8.5.5.1 Adding New Sensors to Database

8.5.5.2 The Database Format

8.5.5.3 Multipoint Linearization

8.5.5.4 Adding New Sensors

8.5.6 Terminal Tab

8.5.7 Display Tab

8.5.7.1 Define Standard Decimal Templates on Module Level

8.6 Module Dependent Tabs

8.6.1 Thermo Tab (M-Modules)

8.6.2 Excitation Tab

8.6.2.1 Resetting Sensor Excitation after Change of Sensor Mode

8.6.3 Mode Tab (M-CNT2)

8.6.4 STG Mode

8.6.4.1 Bridges

8.6.5 Signal Filters

8.6.5.1 Hardware Filters

8.6.5.2 DSP Software Filters

8.6.5.3 Aliasing Effect

8.6.5.4 Filter Tab (X-Modules)

8.6.5.5 Filter Tab (M-Modules)

8.6.6 Data Output Tab (X-Modules)

8.6.7 Characteristic Curve Tab (X-Modules/M3-Series/M-THERMO 96)

8.6.7.1 Configuring the Characteristic Curve

8.6.7.2 Custom Thermo Element

TABLE OF CONTENTS

202

202

203

204

205

207

208

209

209

210

211

212

214

218

219

221

223

225

227

227

228

228

229

231

231

233

234

234

234

235

236

237

238

239

242

8.6.8 Extended (X-Modules and M3-Modules)

8.7 Calculation Signals

8.7.1 Calculation Signal: RMS (Root Mean Square)

8.7.1.1 Adding RMS Signal Channels

8.7.2 Calculation Signal: Active/Reactive/Apparent Power

8.7.3 Calculation Signal: Phase Shift Angle

9 Technical Data

9.1 System Requirements

9.1.1 Minimum System Requirements

9.1.2 Recommended System Requirements

10 Appendix

10.1 Introduction to CAN-FD

10.1.1 Structure of CAN-FD Message

10.2 CAN Card Hardware Interfaces

10.3 Channel Customization

10.4 Hidden Options

10.4.1 Don't Permit to Change the CAN Interface Configuration

10.4.2 Ignore Cluster Information during Hardware Detection

10.4.3 Use Short Default Names for Devices

10.4.4 Aliasing Free Settings Per Channel

244

245

246

247

247

248

249

249

249

249

250

250

251

254

256

258

258

259

259

260

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

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

modems, WiFi and Bluetooth® components).

IPETRONIK devices are designed for applications in extended tem-
perature ranges > 70 °C (158 °F). A high environmental temperature and
the module’s self-heating may cause injuries of the skin when touching the
hot surface. In order to avoid the risk of injury we recommend to take care
for appropriate safety precautions (e.g. contact protection, cov-
ering/enclosure, warning sign, ... ).

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

6

Abbreviations

Definition

PTP

RMS

RTD

STG

TEDS

VDC

Precision Time Protocol

Root Mean Square

Resistance Temperature Detector

Strain Gauge

Transducer Electronic Data Sheet

Voltage Direct Current

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

7

4 X-PlugIn Overview

4.1 X-PlugIn Description

IPETRONIK X is a PlugIn which is an extension that comes along with the IPEmotion
PC software and supports to configure analog and digital measurement modules from
IPETRONIK. With the X-PlugIn you can configure the measurement modules over a CAN and
the Ethernet interface. The two main module lines are:

▶ CAN modules (M-Modules)

▶ Ethernet Modules (X-Modules)

Therefore two configuration interfaces CAN and Ethernet are supported for the product lines.
However, it is also possible to daisy chain CAN modules after the X-Modules. This setup is
called X-LINK and is explained in the further sections. The Modules can be operated with the
IPEmotion PC software and on the IPEmotion RT data logger software.

This manual provides detailed description, usage and features available in the IPETRONIK X-
PlugIn in the further sections.

The IPETRONIK X-PlugIn is only available for the IPEmotion PC software. There are multiple
PlugIns which you can activate in the PlugIns tab as per your need.

4.2 X-PlugIn Installation

In order to use the PlugIn together with IPEmotion first you need to install it. The PlugIn is avail-
able for download from the IPETRONIK.

Website: https://www.ipetronik.com/en/products-services/software-digitalization/plugins.html.

The X-PlugIn is available as a 64-bit version and requires minimum IPEmotion 2024 R2 and
later versions to be supported. For system requirements, please refer to "Technical Data" on
page 249.

Download the latest version available from the website.

The X-PlugIn supports the 64bit Windows operating systems.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

8

Once the PlugIn is downloaded, follow the instructions shown on the screen and complete the
installation.

Figure 4.1 - PlugIn IPETRONIK-X Installation

4.2.1 PlugIn Versions

If desired, you can use the drop-down box to switch to previous PlugIn versions. The "Version"
column will display the currently selected PlugIn version. If you select a PlugIn marked with an
equal sign (=), you designate it as your standard PlugIn and the system will ignore newer ver-
sions. However, if you select a PlugIn without an equal sign and install a more recent version,
the newer version will automatically load into the Signals workspace.

Figure 4.2 - Signal Work Space

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

9

4.2.1.1 Verifying the Installed PlugIn

To verify and select the PlugIn installed versions, do as follows:

1. Once the installation is completed, start the IPEmotion PC software.

2. Access the File menu and navigate to the Options or you can click

icon on the

QuickAccess Toolbar ribbon to access PlugIn Options.

3.

In the Options → PlugIn window below the Version column, click

icon to view the

installed versions.

4. Select the PlugIn versions as per your requirement.

Figure 4.3 - PlugIn Installation

You can also download the latest version through the IPEmotion soft-
ware.

▶ The selected PlugIn version will also reflect on the Signals work space.

▶ (=) is indicating that this PlugIn is fixed and will not be automatically replaced when a new

PlugIn version is installed.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

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

If you need to modify settings for the ETH or CAN interface, open the Plugin-specific set-
tings by clicking to the wrench tool symbol. For more details on Plugin-specific settings,
refer to "PlugIn Options" on page 12.

In order to operate the PlugIn IPETRONIK-X and IPETRONIK-CAN in par-
allel, you need to disable the use of the CAN modules (through the CAN
interface) for the PlugIn IPETRONIK-X.

The PlugIn that are activated here is also loaded in the Signals work space to
use.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

11

5 PlugIn Options

5.1 Plugin-specific Settings

When you access the Options → PlugIns window in the IPEmotion you can access the
advanced Plugin-specific settings and the Help Manual.
However, other PlugIns contain additional settings that are detailed in their respective manuals.

Figure 5.1 - Plugin-specific Settings

5.1.1 Ethernet Interfaces Settings

Ethernet interfaces tab allows you to configure functions for the IP-address and the detection
mode. The ethernet and IP-address range settings are relevant for the X-Modules only.

Enable all

Performs the scan for module across all Ethernet interfaces of the PC.
This setting consumes more time.

Disable all

Will not allow any detection of the modules on an Ethernet port.

Selected

Here you will perform the scan only on a dedicated Ethernet port of the
computer.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

12

Figure 5.2 - Ethernet Interface - Detection Mode

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

13

If the Detection mode is set to Only selected Ethernet ports, the user can Enable only the
required one and also access to an advanced configuration dialog to change the IP-address
ranges of the modules. The setting in the advanced dialog should be handled with care as it has
an impact on the Ethernet interface of the computer and address of the modules.

If the address ranges are changed to match corporate IT network
requirements is might be possible that the modules cannot be detected any
more on another computer with different network settings.

Figure 5.3 - Ethernet Interface Settings

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

14

Once you set the IP address range, click OK to confirm and a dialog pops up confirming that the
command to set ranges is sent. To update the firmware version of the X-Modules, please refer
to "Firmware Update " on page 155.

Figure 5.4 - Confirmation

5.1.2 CAN Interfaces Settings

The CAN interface settings are relevant when you work with the CAN modules. With the setting
in this dialog there is an impact on the detection process.

Figure 5.5 - CAN Interface Settings

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

15

▶ CAN hardware detection interfaces: Allows you to select the detection mode for

CAN hardware detection.

Enable all

Will perform the scan for module across all CAN
interfaces detected by the PC. The supported
CAN interfaces are managed in the CAN server.
A list of the vendors and devices is provided
in "CAN Card Hardware Interfaces" on page 254
The full scan will take more time.

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

16

▶ Automatic CAN ID placing: With this check box you can define where the software will
assign automatically the CAN IDs starting from the CAN ID defined in the box below.

▶ Start CAN ID: Here you define the first CAN ID to start the automatic placing. The start
CAN ID can be displayed in a hex, decimal or in the binary format. The CAN ID range
640 . . . 767 is used internally by the modules and will be skipped in the CAN ID placing
routine. With the column chooser function you can add the CAN IDs
information to the channel grid to display the software assigned IDs.

▶ Device sequence after hardware detection: Defines the sequence after hardware

detection.

▶ Default: X, M1/M2/SIM devices are listed with descending serial number. M3

devices are listed in the order, they are connected to the bus, directly after X and
above SIM/M1/M2 devices.

▶ Descending serial number:All devices are listed in the order of descending
serial numbers, such that M3 device are listed as last devices of a system.

For more details on the device sorting, please refer to "Device Sorting Option" on the
next page.

This also affects the listing when adding devices manually to the con-
figuration as well as hardware synchronization.

▶ Compatibility mode settings: X-PlugIn provides a special compatibility mode if SIM-STG

devices are used with increased timeouts.

This mode should only be used, when using SIM-STGs. If no SIM-STGs
are used then this option should be turned off, since hardware
operations may take much longer.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

17

5.1.3 Device Sorting Option

As of PlugIn version V02.23.00, a new configuration setting titled "Device sorting" is introduced
to enable users to define the order in which devices appear under the parent system.

This setting determines the default listing order of devices in the IPEmotion setup tree, provided
that no manual column sorting is applied. Additionally, it governs the sequence in which devices
are recorded within the configuration file.

The "Device sorting" option is accessible through the "CAN Interfaces" section within the
IPETRONIK X PlugIn Options.

Figure 5.6 - Device Sorting

The "Device sorting" option is located within the group box titled "Automatic CAN ID Placing
/ Device Sequence". It offers two selectable configuration values:

▶ Default

▶ Descending Serial Number

This setting influences device configuration in the following three use cases:

▶ Hardware Detection

▶ Hardware Synchronization

▶ Manual Device Creation

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

18

5.1.3.1 Device Sequence: Default

Setting the device sequence to "Default" retains the behavior observed in previous versions.

▶ Hardware Detection:Initially, all X devices are listed directly beneath the system node in
an unspecified order. Following the X devices, all M3 devices are displayed in the precise
sequence in which they are connected to either the X devices or the PC. Finally, all remain-
ing CAN devices (i.e., M1, M2, and SIM) are listed.

Figure 5.7 - Default - Hardware Detection

▶ Hardware Synchronisation: During hardware synchronisation, the system arranges

newly detected devices as follows:

▶ New X devices are inserted directly below existing X devices and above all M3

devices.

▶ New M3 devices are placed immediately below existing M3 devices and above all other

CAN devices.

▶ New M1, M2, and SIM devices are placed to the end of the device list.

Figure 5.8 - Default - Hardware synchronisation

▶ Manual Device Creation:Manually added devices are inserted in the same order as newly

detected devices during hardware synchronization.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

19

5.1.3.2 Device Sequence: Descending Serial Number

When the "Device sequence" option is set to "Descending serial number", detected devices
are added in order of decreasing serial number.

▶ Hardware Detection:All detected devices are listed in descending order of their serial num-

bers.

▶ X devices appear at the top of the list.

▶ M1and M2 devices are positioned in the middle section.

▶ M3 devices are listed at the bottom, regardless of their connection order to the CAN

interface.

▶ SIM(-STG) has a smaller serial number (519xxxxx) than M3 device. These devices will

be shown AFTER M3 devices.

Figure 5.9 - Device Sequence - Hardware Detection

▶ Hardware Synchronisation: New X devices are added between an already existing X and

CAN devices. All new CAN devices are added at the bottom of the existing devices.

Figure 5.10 - Device Sequence - Hardware Synchronisation

▶ Manual Device Creation: Manually added devices are inserted in the same order as newly

detected devices during hardware synchronization.

Changing the PlugIn option does not modify the device sequence in an
existing configuration. This means that devices in the current or a previously
loaded configuration will remain unchanged even if the PlugIn option is

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

20

altered after the configuration was created or differs from the option used
during its creation.

5.1.4 Options Settings

The basic option settings are as shown below:

Figure 5.11 - Options Settings

▶ Aliasing-free filter settings: This check box impacts the Digital Signal Processors (DSP)
and hardware software filter settings. The function is only supported for modules which
have an adjustable DSP and / or hardware filter. If aliasing-free filtering is active, the soft-
ware filter frequency is automatically adjusted when the sampling rate changes.
The frequency is changed so that the new value is always the maximum possible fre-
quency, where aliasing free measurement is guaranteed. If the filter frequency previously is
changed to a lower value intentionally, the filter frequency must be changed manually by
the user after the sample rate is changed. This also applies, if the sample rate is decreased.

The automatic adaptation of the software filter frequency is not applied, in case that the
aliasing free measurement is disabled. For more details, please refer to "Signal Filters" on
page 233.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

21

▶ CSV import mode: Controls the behaviour during CSV import.

Figure 5.12 - CSV Import Mode

There are three types of import modes:

▶ Default: In the initial implementation, no devices are created automatically. It is the
user's responsibility to ensure that the configuration includes enough devices of the
correct types before initiating the import process. If there are not enough suitable
devices in the configuration, any remaining rows in the import file will not be assigned
to any channel. The assignment of CSV rows to measurement channels follows a
specific prioritization, which is based on the channel name, channel, and device types.
The front number of the devices is not considered, meaning measurements are not
assigned to individual devices beyond the channel name. Any channels in the con-
figuration that are not assigned by a row in the CSV file will be reset to their default
settings and deactivated.

▶ Creation: CSV rows containing device type and front number information are assigned

to corresponding devices in the current configuration. If no matching devices are
found, new devices of the required type are created. Additionally, if the CSV data
includes channel number information, the channel is assigned based on its index in the
device. If none of these conditions are met, the "Default" behavior is applied, and new
devices are created if there are not enough devices in the configuration. Any remaining
devices and channels in the configuration that have not been assigned are left
unchanged.

▶ Front number: This import mode combines elements of both the "Default" and

"Device creation" modes. CSV rows containing device type and front number inform-
ation are assigned to the corresponding devices in the current configuration. For rows

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

22

that cannot be assigned based on device type and front number, the rules from the
"Default" import mode are applied. Additionally, channels in the configuration that
were not assigned by a row from the CSV file are reset to their default settings and
deactivated.

▶ Calibration interval: Defines the calibration time interval for all the devices along with a

warning message duration.

▶ TEDS sensors: The X-PlugIn provides the ability to configure how TEDS data are pro-

cessed.

▶ TEDS data processing: In the current version, the PlugIn supports 2 "processing

modes"

▶ Read / Write: This mode represents the default behavior of the PlugIn. In this con-
figuration, TEDS data is processed in the same manner as in previous PlugIn ver-
sions. Depending on the device type and the active license, the PlugIn will read
TEDS data during operations such as hardware detection and hardware syn-
chronization. Additionally, writing TEDS data to the TEDS sensor is supported.
Currently limited to M-SENS3 8 device types.

▶ Deactivated: In this operation mode, TEDS data processing is fully deactivated

within the PlugIn. As a result, the PlugIn does not update any TEDS-related inform-
ation in the configuration at any point. TEDS data cannot be viewed, edited, or writ-
ten to any connected TEDS sensor while this mode is active.

▶ Live-Zero settings: If enabled, the senor range for uniploar TEDS sensors is set to

biploar range, such that sensor values of 0 are not displayed as NoValue.

▶ Special measurement modes: This setting is available for the special measurement
cases and applicable for specific devices ("M-CNT2" on page 75 and "M-SENS2" on
page 57).

▶ Frequency drop tolerance:Frequency measurement for M-CNT2 on a gear wheel, in

which a tooth gap exists to determine the top dead center. This gap is
eliminated via the 'Ignore frequency drop' mode. If channel parameter 'Ignore fre-
quency drop' is active and measure frequency suddenly drops, this factor
controls the sensitivity if the new measured value is used instead of the previous one.
The value ranges from 1.1 to1.0 with 1.1 allowing small frequency drops and 10 being
the most tolerant. Default value is 1.75.

▶ Time before 1st data [in ms]: This option only affects M-SENS 2/8 with or without

DSP. The option defines the default value for the device parameter 'Time before 1st
data', which is the time before the device sends the first data after the start of a meas-
urement. The device prevents any data transfer to avoid sending bad
management values during transient conditions.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

23

▶ If the option is 0, the parameter can be edited on each device individually.

▶ If the option is not 0, this value will be used on any device supporting the para-

meter.

5.1.5 Components Settings

In the components you can see all supported modules. With the priority setting you have an
impact on the visibility. When a module is put into the status not used it will be made invisible in
the module tree for selection during the dry configuration.

You can reduce the number of device types to be used by assigning a priority:

▶ High

▶ Normal

▶ Low

▶ Not used

Figure 5.13 - Components

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

24

5.1.5.1 General Procedure for the Devices on the EOL List

In general, devices being listed as EOL (End of Life) are not completely removed from the
PlugIn. Primarily, they are marked as "Not used" on the PlugIn's page, please refer to "Com-
ponents Settings" on the previous page.

The devices marked as "Not used" will no longer appear in the drop down list "Components"
on IPEmotion's "Signals" page. By default, users cannot create them manually. However, if
these devices are connected to a bus and configured for hardware detection or synchronization,
they will still be detected.

On the other hand, devices being listed as "EOL" are no longer serviced by the PlugIn release
process (the functionality is no longer tested by IPETRONIK's testing department during the
PlugIn release process). Therefore IPETRONIK cannot guarantee the proper functionality in the
future versions. It is up to the users risk, to use them. For the list of EOL devices, please refer to
"Module Identification by Base Type Number" on page 83.

If you still wish to create these devices manually or have them appear in the "Components"
drop-down menu, you need to change their "Priority" setting to either "Low," "Normal," or
"High."

Figure 5.14 - EOL List

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

25

6 Hardware Integration

Modules are the measurement devices which are connected along with a laptop or with the
logger and designed specifically to measure the particular parameter. The X-PlugIn supports
two types of modules:

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

300 m overall cable length with a maximum of 40 devices and one Laptop/Logger. The cable
length between two X-Modules is 100 m.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

26

6.1.2 Mx-SENS2 4 Fast

Fast 4-Channel Analog Measurement Device with Excitation.

Figure 6.1 - Mx-SENS2 4 Fast

▶ 4 fast analog signal inputs for voltage / current supporting channel sample rates up to

400 kHz.

▶ 4 separate dual sensor excitations (up to ±15 V, up to ±60 mA)

▶ Measurement modes: Voltage, Current, IEPE, individual for each input.

▶ Status LED at each input channel (sensor break indication and configuration aid)

▶ Offset adjust functions and offset adjust during the measurement.

▶ TEDS Class-2 supported

▶ Measurement data output via XCPonEthernet or CAN

▶ Designed for engine compartment applications.

▶ Toolless module to module connection

▶ Ruggedized and compact modules for harsh environments

The Mx-SENS2 4 consists similar configuration when compared to
Mx-SENS24 FAST but there are few differences as shown below:

Mx-SENS2 4

Mx-SENS2 4 FAST

Sampling rate

10 Hz - 100 kHz

10 Hz - 400 kHz

Hardware filter

12 kHz (On/Off)

48 kHz (On/Off)

Software filter

10 Hz - 10 kHz

50 Hz - 25 kHz

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

27

Figure 6.2 - Mx-SENS2 4 Schematic: Sensor Measurement

Figure 6.3 - Mx-SENS2 4 Schematic: Voltage Measurement

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

28

Figure 6.4 - Mx-SENS2 4 Schematic: Current Measurement

Figure 6.5 - Mx-SENS2 4 Schematic: IEPE Sensor Measurement

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

29

6.1.2.1 Input Cables:

Standard (open)

Figure 6.6 - 670-810.xxx M-SENS (TEDS) Cable

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

SENS 1B 6pin Cable Banana 2 (VIN+/ VIN- via banana
plugs).

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

30

6.1.3 Mx-SENS2 8

Fast 8-Channel Analog Measurement Device with Excitation

Figure 6.7 - Mx-SENS2 8

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

31

Figure 6.8 - Mx-SENS2 8 Schematic (Sensor Measurement)

Figure 6.9 - Mx-SENS2 8 Schematic (Voltage Measurement)

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

32

Figure 6.10 - Mx-SENS2 8 Schematic (Current Measurement)

6.1.3.1 Input Cables:

Standard (open)

Figure 6.11 - 670-810.xxx M-SENS (TEDS) Cable open

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

33

Specific (assembled, open)

670-807.xxx

SENS 1B 6pin Cable open (compatible to 670-810, no TEDS support).

600-861.xxx

SENS 1B 6pin Cable Banana 6 (compatible to 670-810, no TEDS
support, all lines connected to banana plugs).

600-864.xxx

SENS 1B 6pin Cable Banana 2 (VIN+/ VIN- via banana plugs).
IPETRONIK

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

34

6.1.4 Mx-STG2 6

Fast 6-Channel Analog Measurement Device with Excitation.

Figure 6.12 - Mx-STG2

▶ 6 fast analog signal inputs for voltage supporting channel sample rates up to 100 kHz

▶ STG (Strain Gauge) measurement mode supports different bridge types

▶ 6 separate dual sensor excitations (up to ±5 V, up to ±45 mA)

▶ Offset and target adjust functions by hardware (maximum accuracy)

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

35

Figure 6.13 - MX-STG 6 Schematic

6.1.4.1 Input Cables:

Standard (open)

Figure 6.14 - 600-747.xxx STG 2B 10p. Cable open (10-pin TEDS)

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

36

If you do not use IPETRONIK input cables, please pay attention to the
correct pin configuration.

The connection Pin 5 <> Pin 10 is always required as the module
identifies by this, when a sensor is plugged in.

Figure 6.15 - 670-850.xxx DMS/STG Cable open (7-pin DMS compatible)

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

37

6.1.5 Sx-STG

Figure 6.16 - Sx-STG

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

38

Figure 6.17 - Sx-STG Schematic

6.1.5.1 Input Cables:

Standard (open)

Figure 6.18 - 670-850.xxx DMS/STG Cable open (7-pin DMS compatible)

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

39

Figure 6.19 - 600-747.xxx STG 2B 10p. Cable open (10-pin TEDS)

If you do not use IPETRONIK input cables, please pay attention to the
correct pin configuration.

The connection Pin 5 <> Pin 10 is always required as the module identifies
by this, when you plug in the sensor.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

40

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

Figure 6.20 - STG Mode

Application:

▶ Measurement with strain gauges (full / half / quarter bridges).

▶ Measurement with sensors which provide a fixed ground (GND) reference (with no definite
ground reference the input may drift, because of the high impedance of the signal input).

▶ For more details on STG Mode, please refer to "STG Mode" on page 231.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

41

Features:

▶ Bridge connection supporting 2-wire, 4-wire and also 6-wire technique

▶ Bridge completion using internal resistors

▶ Shunt check in configuration mode as well as in measurement mode. Adjustable shunt res-
istor 5 kΩ to 500 kΩ (minimum and maximum value depends on the current setting of the
excitation voltage), connectable to each bridge section (quadrant). The complete adjust
data can be output to the software (CSV format) and can be loaded and applied to the
sensor for verification of stability and repeatability.

▶ Sensor break detection for all 6 wires (IN [up to an input range of 200 mV], VOUT, SENS)

indication by output of -Full Scale.

Measurement ranges with Sx-STG:

▶ ±2 mV to ±2 V in 2 mV steps

Measurement ranges with Mx-STG:

▶ ±5 mV to ±1 V in 8 bipolar measurement ranges

Adjustable differential voltages:

▶ Sx-STG/Mx-STG2 adjusts the offset voltages up to ±0.9 x Full Scale (FS).

Common Mode Rejection Ratio (CMRR): To guarantee a correct measurement of the input
signal over the complete measurement range (uncropped signal amplitude), the input voltage
on IN+ resp. IN- relating to the GND potential should not exceed 4 V.

Sensor excitation:

▶ Selectable bipolar voltage: ±0.50 / ±1.25 / ±2.50 / ±5.00 V

▶ Sx-STG: In Sensor mode "Voltage including sensor excitation" ±10V / ±12V and ±15V

and unipolar sensor supply for all values are additionally available.

▶ Current load up to 45 mA per channel.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

42

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

43

Bridge Completion:

Figure 6.21 - Bridge Completion - Quarter Bridge

Figure 6.22 - Bridge Completion - Half Bridge

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

44

Shunt Check:

Figure 6.23 - Shunt Check

With the shunt check an internal resistor is temporarily connected to one quadrant (section) or
consecutively to all sections of the bridge circuit. This has a definite affect on the output of the
bridge. Is the shunt check executed before start and after the end of each measurement task,
the correct function (offset, gain, stability) of the sensor can be validated by comparing the
results.

The shunt check can be initiated during:

▶ Configuration mode

▶ Measurement mode

The parameters of the shunt check can be output in CSV format to the software to be stored and
used later on. In order to identify the shunt check results within the data record, start and end of
the shunt check process is marked with a series of -FS (Minus Full Scale) values.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

45

6.1.6.2 SENS Mode

Figure 6.24 - SENS Mode (Available Only for Sx-STG)

Applications:

▶ Measurement with sensors without a direct ground (GND) reference.

▶ Voltage measurement up to ±50 V.

Features:

▶ Sensor connection supporting 3-wire and 4-wire technique.

▶ Sensor break detection for the 4 wires (IN, VOUT) indication by output of –Full Scale.

Measurement Ranges:

▶ 0.01 / 0.02 / 0.05 / 0.1 / 0.2 / 0.5 / 1 / 2 / 5 / 10 / 20 / 50 V

▶ ±0.01 / ±0.02 / ±0.05 / ±0.1 / ±0.2 / ±0.5 / ±1 / ±5 / ±10 / ±20 / ±50 V

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

46

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

47

6.1.6.3 ICP Mode

Figure 6.25 - ICP Mode (Available Only for Sx-STG)

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

48

6.1.7 TEDS Class 2

Figure 6.26 - TEDS Class 2 - Sx-STG

The LEMO 2B version of Sx-STG is capable of supporting the use of Transducer Electronic
Data Sheet (TEDS) enabled transducers. As a globally recognized industry Plug & Play stand-
ard, TEDS is defined under IEEE 1451.4 and distinguishes between two interface classes.

As soon as the input connector is plugged in, the Sx-STG module automatically detects Class II
TEDS sensors (e.g. multi-wire interfaces with bridge-type sensors) and is able to read out
sensor-specific data about the TEDS +/- interface, using a serial, master/slave model of
communication.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

49

Figure 6.27 - TEDS Class 2 - Mx-STG 6

Figure 6.28 - TEDS Class 2 - Mx-SENS2 4 FAST

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

50

Figure 6.29 - TEDS Class 2 - Mx-SENS2 8

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

51

6.2 M-Modules

The M-modules/M-devices are operating in a CAN bus network based on the XCP protocol. You
can also find the datasheet for each modules at https://www.ipetronik.com/en/products-ser-
vices/modules.html. The M-Modules are:

▶ M-SENS 8

▶ M-SENS3 8

▶ M-THERMO2

▶ M-THERMO2 u

▶ M-THERMO3 16

▶ M-RTD2

▶ M-CNT2

▶ CANpressure

6.2.1 M-Modules Cable Length

CAN

CAN-Bitrate

Maximum Bus Length

125kBits/s

250kBits/s

500kBits/s

1MBit/s

200m

100m

50m

25m

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

52

CAN-FD (Switchable to pure CAN operation via IPEmotion software)

CAN-FD Bitrate Arbitration Phase

CAN-FD Data-Bitrate(1)

Max. Bus Length

1MBit/s

500kBits/s

1MBit/s

2MBit/s

5MBit/s

500kBits/s

1MBit/s

2MBit/s

5MBit/s

10m

10m

10m

50m

20m

20m

10m

(1) CAN-FD is only supported by the M3 series

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

53

6.2.2 M-SENS 8 / M-SENS 8plus

8-channel analog measurement module with sensor excitation

Figure 6.30 - M SENS 8

▶ Measurement modes: V, mA selectable for each input

▶ TEDS class 2 support

▶ Measurement data output to CAN

▶ Galvanic isolation (inputs, CAN, supply, enclosure)

▶ Designed for engine compartment applications

▶ Toolless module to module connection

▶ Ruggedized and compact modules for harsh environments

Parameters

M-SENS 8

M-SENS 8plus

Drift for ambient
temperature 105 °C
to 125 °C:

±250 ppm/K

±250 ppm/K
±450 ppm/K (for
10 mV measurement range)

Hardware filter
(switchable)

150 Hz (M-SENS 8/
M-SENS 8 DSP)
Accuracy 10 %

Butterworth (8-pole)
150 Hz (M-SENS 8plus/M-SENS
8plus DSP)
Accuracy 10 %

Software filter types

Bessel, Butterworth,
Elliptic (8-pole)

Bessel, Butterworth,
Elliptic (8-pole)

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

54

Figure 6.31 - M-SENS_8_M-SENS_8plus-Voltage In

Figure 6.32 - M-SENS_8_M-SENS_8plus-Current Loop

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

55

6.2.2.1 Input Cables

670-810.xxx M-SENS (TEDS) Cable Open

Figure 6.33 - 670-810.xxx M-SENS (TEDS) Cable Open

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

56

6.2.3 M-SENS2

4-channel analog input module with sensor excitation

Figure 6.34 - M-SENS2

▶ 4 measurement inputs for voltage (V) / current (mA) selectable for each input

▶ 6 sensor excitation ranges (unipolar 15 V, up to ±60 mA)

▶ TEDS Class-2 supported

▶ Measurement data output to CAN

▶ Galvanic isolation (Signal inputs, CAN, power supply, enclosure)

▶ Designed for engine compartment applications

▶ Toolless module to module connection

▶ Ruggedized and compact modules for harsh environments

Figure 6.35 - M-SENS2 Schematic Diagram: Voltage Measurement

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

57

Figure 6.36 - M-SENS2 Schematic Diagram: Current Measurement

Figure 6.37 - M-SENS2 Schematic: 20 mA Current Loop

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

58

6.2.3.1 Input Cables

Standard (Open)

Figure 6.38 - 670-807.xxx SIM-SENS Cable Open (M-SENS, M-SENS2)

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

59

6.2.4 M-SENS3 8

8 channels with freely selectable operating modes are extraordinarily flexible and precise
thanks to the 18-bit high-resolution AD converter. The M-SENS3 8 is ultra-compact and
ruggedized. Its innovative wireless and magnetic connection concept reduces setup times and
guarantees an optimal and fail-safe data connection.

Figure 6.39 - M-SENS3 8

▶ Freely selectable operating mode for each input: voltage, current, periodic duration, and

frequency

▶ Measurement data output to CAN/CAN FD

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

60

Figure 6.40 - M-SENS3 8 Schematic: Sensor Measurement

Figure 6.41 - M-SENS3 8 Schematic: Voltage Measurement

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

61

Figure 6.42 - M-SENS3 8 Schematic: Current Measurement

Figure 6.43 - M-SENS3 8 Schematic: Frequency / Periodic Duration

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

62

6.2.4.1 Input Cables

Standard (Open)

Figure 6.44 - M-SENS (TEDS) Cable Open

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

63

6.2.5 M-THERMO2

8-Channel Temperature Measurement for K-Type Thermocouples

Figure 6.45 - M-THERMO2

▶ 8 Thermocouple measurement inputs type K (NiCr/NiAl)

▶ Cold junction compensation per channel

▶ Separate ADC for each channel

▶ Status LED at each input channel (sensor break indication and configuration aid)

▶ Measurement data output to CAN

▶ Complete galvanic isolation (inputs, CAN, power supply, and enclosure)

▶ Designed for engine compartment applications

▶ Toolless module to module connection

Figure 6.46 - M-THERMO2 Schematic

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

64

6.2.5.1 Input Cables

Standard (open)

Figure 6.47 - 600-888.xxx SIM-TH-MIN Cable Open

6.2.6 M-THERMO2 u

8-Channel Universal Thermocouple Inputs

Figure 6.48 - M-THERMO2 u

▶ 8 Universal thermocouple inputs supporting type J, K, N, R, S, T, E

▶ Cold junction compensation for each channel

▶ Separate ADC for each channel

▶ Status LED at each input channel (sensor break indication and configuration aid)

▶ Measurement data output to CAN

▶ Complete galvanic isolation (inputs, CAN, power supply, and enclosure)

▶ Designed for automotive use

▶ Toolless module to module connection

For schematic and cable information, please refer to "M-THERMO2" on the previous page

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

65

6.2.7 M-THERMO3 16

16-Channel Universal Thermocouple Inputs

Figure 6.49 - M-THERMO3 16

▶ High-resolution 24-bit ADC technology

▶ Measurement data output on CAN-FD.

▶ Cable free system connection - connection cable not required

▶ Tool-free, magnetic connection technology

▶ Separate cold junction compensation for each channel

▶ Ultra compact and robust design

▶ IP 67 and extended temperature range

▶ Galvanic isolation (channel, CAN, supply, housing)

▶ Channel status LED at each measuring input with display of the selected thermocouple

type according to IEC/ANSI.

▶ Display of channel and device status in software interface (e.g. sensor break / under-

voltage)

▶ System status information (system, devices, channel)

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

66

Figure 6.50 - M-THERMO3 16 Schematic Diagram

6.2.7.1 Input Cables

Standard (open)

Figure 6.51 - 600-888.xxx SIM-TH-MIN Cable open

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

67

6.2.7.2 Thermocouple Schematics

Thermocouple
Type

Color Coding

IEC 584-3

ANSI MC 96.1

B

C

E

J

K

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

68

Thermocouple
Type

Color Coding

IEC 584-3

ANSI MC 96.1

N

R

S

T

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

69

6.2.8 M-RTD2

4-channel PT100 RTD temperature measurement inputs

Figure 6.52 - M-RTD2

▶ 4 measurement inputs for RTD

▶ Measurement data output to CAN

▶ Complete galvanic isolation (inputs, CAN, power supply, and enclosure)

▶ Designed for engine compartment applications

▶ Toolless module to module connection

▶ Ruggedized and compact modules for harsh environments

6.2.8.1 Types of RTD Configurations

RTDs are widely used for temperature measurements in industrial and laboratory settings. They
are typically classified into three types based on their wiring configurations:

▶ 2-Wire configuration

▶ 3-Wire configuration

▶ 4-Wire configuration

Each configuration determines how lead wire resistance compensation is implemented, directly
influencing the precision of temperature readings. The following section provides detailed
explanations and schematic representations for these wiring configurations.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

70

▶ 2-Wire configuration: The 2-wire RTD is the simplest and most cost-effective con-

figuration available. In a 2-wire RTD setup, two wires link the RTD element to the meas-
uring device. As a result, the measurement includes both the RTD element’s resistance and
the lead wire resistance.

Figure 6.53 - 2-Wire Configuration Schematic

▶ Advantages:

▶ A 2-wire RTD is easy to install and use, making it the most affordable option.

▶ Its reduced number of wires makes it ideal for compact installations or in spaces

where managing wires is challenging.

▶ Disadvantages:

▶ A significant drawback of the 2-wire RTD is that it does not account for lead wire
resistance. This can lead to measurement errors, particularly with longer lead
wires or in situations where accuracy is critical.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

71

▶ 3-Wire configuration: The 3-wire RTD configuration is the most commonly used in indus-
trial applications because it offers a balanced trade-off between cost and measurement
accuracy. In this setup, three wires connect to the RTD element:

▶ Two to one side and one to the other.

▶ The third wire acts as a reference, enabling the measurement instrument to measure

the lead wire resistance and partially compensate for it.

Figure 6.54 - 3-Wire Configuration Schematic

▶ Advantages:

▶ The system improves measurement accuracy by using the third wire to measure
and compensate for lead resistance, significantly enhancing precision compared
to the 2-wire RTD.

▶ The 3-wire RTD doesn't match the accuracy of the 4-wire RTD, but it delivers sig-
nificantly better performance than the 2-wire configuration, making it well-suited
for industrial applications.

▶ Disadvantages:

▶ The 3-wire RTD is slightly more complex to use than a 2-wire RTD, which results
in a moderate increase in cost though not as high as the cost of a 4-wire system.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

72

▶ 4-Wire configuration: The 4-wire RTD is the most accurate configuration, specifically

designed to fully eliminate lead resistance errors. In this setup, four wires are used: two to
carry the current and two to measure the voltage drop across the RTD element. This allows
the measuring device to completely disregard lead resistance errors during measurement.
IPETRONIK device M-RTD2 is equipped with the 4-Wire Configuration for more precise
and accurate results.

Figure 6.55 - M-RTD 2 Schematic

▶ Advantages:

▶ The 4-wire RTD configuration eliminates lead resistance errors, making it the most

precise of all RTD setups.

▶ This configuration is particularly well-suited for high-precision temperature meas-
urements in environments such as calibration laboratories, scientific research,
and critical industrial processes.

▶ Disadvantages:

The additional wiring in a 4-wire RTD setup makes it more complex and expensive to
install compared to 2-wire and 3-wire configurations.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

73

6.2.8.2 Input Cables

Standard (open)

Figure 6.56 - 670-937.xxx PT100/RTD 0S Cable Open

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

74

6.2.9 M-CNT2

4-channel universal counter module with sensor excitation

Figure 6.57 - M-CNT2

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

Figure 6.58 - M-CNT2 Schematic: Connection with Measuring Input

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

75

Figure 6.59 - M-CNT2 Schematic: Connection with Active Sensor

Figure 6.60 - M-CNT2 Schematic: Connection with Measuring Input Rotation Direction Recognition

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

76

Figure 6.61 - M-CNT2 Schematic: Connection with Active Sensor Rotation Direction Recognition

6.2.9.1 Input Cables

Standard (open)

Figure 6.62 - 670-858.xxx CNT/FRQ-IN Cable Open

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

77

6.2.9.2 Input / Principle Details

Measuring Method: The analog and digital input signal is evaluated with a programmable com-
parator threshold (switching threshold, hysteresis) and the following 48 bit counter. The FPGA
and Digital Signal Processor (DSP) convert the respective counter values online into a fre-
quency output or duty cycle or time period.

Figure 6.63 - Signal at the Measuring Input

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

78

▶ Duty cycle: The counter value of the pulse duration is divided by the counter value of the
interval duration and correspondingly scaled and sent to the measuring range setting.

If the frequency is too low (or 0 Hz), 0% (low level) or 100% (high level) is sent depending
on the signal level.

The thresholds on and off do usually differ and cause different results of the pulse duration
and the duty cycle if the signal edges are low, depending on the defined thresholds.

▶ Period duration: The interval duration is acquired with the acquisition described above.

The counter value between two thresholds on is detected, scaled, and sent correspondingly
to the measuring range setting.

▶ Pulse duration: The pulse duration is acquired with the acquisition described above. The
counter value between the threshold on and the threshold off is detected, scaled, and sent
correspondingly to the measuring range setting.

The thresholds on and off do usually differ and cause different results of the pulse duration
if the signal is not an ideal square wave signal, depending on the defined thresholds.

▶ Pause duration: The pause duration acquisition corresponds to the pulse duration acquis-

ition with inverted input signal.

Status LED at the Input: The status LED at the respective input indicates the acquisition of a
frequency signal. This is the case if both switching thresholds of every value are reached
(threshold ON and OFF).

The status LED is on / flashes in time with the signal frequency if:

▶ Corresponding channel is active

▶ Device is in the acquisition mode (acquiring data) and

▶ Switching thresholds are correctly defined.

Due to the slowness of visual proceeding, only frequencies under approx. 10 Hz you can see
LED flashing. The LED is permanently ON at higher signal frequencies.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

79

6.2.10 CANpressure

Pressure transducer with CAN output for automotive applications

Figure 6.64 - CANpressure

▶ Absolute and relative pressure gauge in the range of 1 to 250 bar

▶ Internal temperature sensor at gauge point

▶ Measurement data output to CAN

▶ Galvanic isolation (inputs, CAN, power supply, enclosure)

▶ Designed for engine compartment applications

▶ Ruggedized and compact modules for harsh environments

6.2.10.1 Pressure Connections

Figure 6.65 - Male Thread

Figure 6.66 - Female Thread

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

80

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

81

Pressure Transducer
(Relative, Absolute)

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

82

6.3 Module Identification by Base Type Number

The modules contain a unique Base type number for M-Module and X-Module through which
the users can identify the modules with ease. The modules and base type number is shown in
the below table. The following modules are supported in the IPETRONIK X PlugIn:

M-Module Family

M-Module Type Name

With
DSP/Without DSP

Support
Status

Base Type
Number

CANpressure

Mc-THERMO

M-CNT2

M-FLOW

M-FRQ

M-RTD2

M-RTD2 16

M-RTD2 32

M-SENS

M-SENS 8

M-SENS 8 plus

M-SENS 24

-

-

-

-

-

-

-

-

-

DSP

-

DSP

DSP

-

-

EOL

-

-

EOL

-

-

-

595

573

586

703

562

581

741

743

EOL

561

EOL

-

-

-

567

568

567

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

83

M-Module Type Name

With
DSP/Without DSP

Support
Status

Base Type
Number

M-SENS2

M-SENS2 250Hz

M-SENS3 8

M-THERMO

M-THERMO 16

M-THERMO3 16

M-THERMO T

M-THERMO 16T

M-THERMO2

M-THERMO2 HV

M-THERMO2 u

M-THERMO96

µ-THERMO

M-UNI2

MultiDAQ

SIM-STG

DSP

-

DSP

-

-

-

-

-

-

-

-

-

-

-

-

-

-

-

EOL

587

-

NEW

EOL

EOL

NEW

-

-

-

-

-

-

EOL

EOL

EOL

EOL

591

541

560

566

540

569

575

578

557

579

740

563

584

577

519

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

84

X-Module Family

X-Module

Support-Status

Base Type Number

Mx-SENS(2) 8

Mx-SENS2 4

Mx-SENS2-4 FAST

Sx-STG

Mx-STG2 6

EOL

EOL

-

EOL

-

911

916

917

920

912

End Of Life (EOL) - Provides the Product End of Life (EOL). You can also
find the updated document in the IPETRONIK official website - EOL
Announcements. In the EOL document you find more information about the
products as shown below:

▶ End of sales: Provides the last date when the sales of the product end.

▶ End of production: Provides the last date when the production of the

product end.

▶ Last Repair: Provides the last date that the product will be

repaired. After that time point, no further bug fixes will be made. Only
automated testing will be conducted. Any errors identified will be
documented, but not addressed.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

85

6.4 System Overview

6.4.1 System Architecture

There are two main system architectures. The first setup requires a CAN card interface from
IPETRONIK like IPEcanPro FD or IPEhub2 or other supported vendors for the CAN modules.

You can operate the X-Modules based on an Ethernet communication via your LAN port of your
computer.

6.4.1.1 Ethernet and CAN Card Interface Architecture

Figure 6.67 - Ethernet and CAN Card Interface Architecture

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

86

6.4.1.2 Ethernet and CAN Modules Daisy Chain Setup

The below setup is to combine Ethernet and CAN modules in one daisy chain. This setup
requires that the Ethernet modules are connected first to the PC and the CAN modules are
following the Ethernet modules.

Figure 6.68 - Ethernet and CAN Modules Daisy Chain Setup

The most common and recommended hardware setups and the required cable sets are
explained in the below sections. For more information, please refer to " X-Modules/Ethernet
Modules Connection" on page 89 or "M-Modules/CAN Modules Connection" on page 96.

6.4.1.3 CAN Bus Termination

A complete termination of the CAN bus with a resistor of 120Ohm each is mandatory for the cor-
rect functioning of the CAN bus.

This is automatically realized in the IPETRONIK measuring system by using the recommended
voltage and CAN cables with integrated termination.

In case of a pure M3 system and use of the Y-cable 623-500.xxx with lines for voltage and CAN
integrated, the termination of the "open" side is realized by the M3 device itself.

6.4.2 Connecting Two X-Devices to PC

By using two network adapters, a simultaneous operation of two independent X-systems
connected to one notebook / PC is supported. Please consider, that the IP ranges have to differ
from one another.

Proceed as follows:

▶ Connect the first system and define its IP range.

▶ Connect the second system and configure an IP range that is different from the first system.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

87

6.4.3 Detection of Ethernet Adapters with Conflicting IP Addresses

The XPI/MxDriver checks for network conflicts during the following situations:

▶ Hardware detection

▶ Hardware synchronization

▶ Hardware initialization

▶ Hardware reset

If the system detects an active second network adapter with an IP address configuration that
conflicts with the X-PlugIn settings (or with the IP addresses designated for detecting X-Mod-
ules ), the PlugIn displays warning messages. Additionally, it sets the error state for systems
affected by these conflicting addresses and provides corresponding error messages.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

88

6.5 X-Modules/Ethernet Modules Connection

In the following 3 main X-Module hardware configurations and cable sets examples are shown.
The required cable sets and lengths are depending on the physical installation environment.
The cables are available in different lengths. The last 3 digits of the cable number are indicating
the length. The required cable to interconnect the X-Modules is number: 630-503.xxx. The avail-
able lengths for the placeholder .xxx are for example:

▶ 002 = 0.15 meter

▶ 015 = 1.5 meter

▶ 030 = 3 meter

▶ 050 = 5 meter

▶ 100 = 10 meter

Every cable has a dedicated cable data sheet indicating the connectors, cable pins and the
color of the cable as indicated in the example below.

Figure 6.69 - 630-503.xxx X-Link Cable System XL

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

89

6.5.1 X-Modules Hardware Setup - Example 1

In this setup the power supply is provided from the very end of the module chain. This setup is
applicable only when there are few modules in the measurement setup and one source of
supply 9 - 36 VDC is sufficient.

Figure 6.70 - X-Modules Hardware Setup - Example 1

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

90

6.5.2 X-Modules Hardware Setup - Example 2

In this setup many modules are involved and therefore intermediate power supply is required.
With the X-FEED power feeder the modules can get power feed into the middle of the
measurement chain. As a rule of thumb 7 X-Modules can be supplied with one power feeder. If
the system grows lager power supply from the very end or additional X-FEED modules can be
added to the system. As indicated the X-FEED provides power only to the X-Modules.

Figure 6.71 - X-Modules Hardware Setup - Example 2

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

91

6.5.3 X-Modules Hardware Setup - Example 3 (CAN Tunneling)

Another system architecture can combine X-Modules and M-Modules in one daisy chain. In this
case a dedicated cable is required to link-up the Ethernet based X-Modules to the CAN based
M-Modules.
The architecture requires that the Ethernet modules at the start followed by the M-modules as
shown. In smaller setups one power feed from the very end can be sufficient. However, if the
system grows lager, you can extend the power alimentation through adding modules for the
X-Modules and CAN POWER FEEDER to the M-Modules.

It is not possible to add any Ethernet modules/X-Modules behind the CAN
modules/M-modules.

Figure 6.72 - X-Modules Hardware Setup - Example 3 (CAN Tunneling)

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

92

6.5.4 M3-System Connection

6.5.4.1 M3-System

Figure 6.73 - M3-System

6.5.4.2 M3-System with Gateway

Figure 6.74 - M3-System with Gateway

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

93

6.5.4.3 M3 and M2-System

Figure 6.75 - M3 and M2-Modules

6.5.4.4 M3 and M2-System with Gateway

Figure 6.76 - M3 and M2-System with Gateway

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

94

6.5.4.5 X-M3-M2-System

Figure 6.77 - X-M3-M2-System

6.5.4.6 X-M3-M2-System with Gateway

Figure 6.78 - X-M3-M2-System with Gateway

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

95

6.6 M-Modules/CAN Modules Connection

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

Figure 6.79 - M-CAN - Cable Datasheet

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

96

6.6.1 M-Modules Hardware Setup - Example 1

In this setup the power supply is provided from the very end of the module chain. This setup is
applicable only when there are few modules in the measurement setup and one source of
supply 9 - 36 VDC is sufficient.

Figure 6.80 - M-Modules Hardware Setup - Example 1

6.6.2 M-Modules Hardware Setup - Example 2

In this setup the supply is provided through a SUBD 9 and Y-splitter cable at the beginning of
the module chain. This setup is also practical in case the power supply and CAN interface are
located at the same end. This system works well for smaller chain modules where one supply is
sufficient.

It is important to finish the measurement system on the last module with a
CAN bus termination plug.

Figure 6.81 - M-Modules Hardware Setup - Example 2

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

97

6.6.3 M-Modules Hardware Setup - Example 3

In this case you operate many modules in the measurement setup and interconnection between
the different modules might be also large which causes voltage drops along the modules. It is
recommended to add a power feeder T-Junction to the system. Within very large systems is
many be required to have several power feeder and to use additional power supply via the last
module or the first modules, as indicated in the two scenarios above. However, it is important to
consider a separate power supply cable when using the power feeder. This cable has no
internal CAN bus termination. As a rule of thumb every 15 (mainly THERMO / RTD2) modules a
power feeder should be considered.

The CAN-Modules require their own power supply either from the very end or
using the M-CAN power feeder.

Figure 6.82 - M-Modules Hardware Setup - Example 3

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

98

6.7 LED Indication

The device and channel LED state is displayed in IPEmotion. Depending on the device type,
firmware version and different states.

6.7.1 M3-System-LED

LED Status

Off

Description

Power supply not available

Green Continuous

Power supply available / ready for use

Green flashing symmetrically at 1Hz
500ms on and 500ms off

Measuring end

Blue Continuous

Firmware update successful

Blue with 1Hz symmetrical flashing
500ms on and 500ms off

Booting / initializing / firmware update in pro-
gress

Red Continuous

Red with 1Hz symmetrical flashing
500ms on and 500ms off

- Internal error (hardware)
- Licence error (serial number invalid)

Communication error (e.g. cable not con-
nected correctly, crushed or interrupted /
auto-banding or auto address assignment
failed / bus error)

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

99

LED Status

Description

Violet Continuous

Violet with 1Hz symmetrical flashing
500ms on and 500ms off

Device in bootloader

Bus overload

Yellow Continuous

Power supply is below 9V

Yellow with 1Hz symmetrical flashing
500ms on and 500ms off for 10s after
start-up

Calibration expired

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

100

6.7.2 M3-Channel-LED

LED Status

Off

Description

Channel inactive

Colour depends on the set sensor type(1)
- for 10s after switching on
- for 10s after initialization

Display Sensor type

Yellow with 1Hz symmetrical flashing
500ms on and 500ms off

Orange with 1Hz symmetrical flashing
500ms on and 500ms off

Red with 1Hz symmetrical flashing 500ms
on and 500ms off

Colour continuous depending on the set
sensor type (1)

Recognition of the channel based on
the selected channel in IPEmotion /
IPEmotion ME

For devices with sensor detection:
TEDS data read out after plugging in
the TEDS sensor, but not yet initialized
in the device

Channel error:
- Over current (short circuit or
excessive current consumption of the
sensor)
- Counter overflow
- General channel hardware error

Sensor break (disconnected or cable
interrupted)
CNT: Frequency / period duration <
0.5Hz

(1) For example: ANSI/IEC colour of a thermocouple. For more details on thermocouple color
coding, please refer to "Thermocouple Color Coding IEC/ANSI" on the next page.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

101

6.7.2.1 Thermocouple Color Coding IEC/ANSI

The M-THERMO3 16 devices support the Thermocouple Color Coding. The device is
capable to control the channel's LED color in normal operation depending on the configured
thermo couple type, such that it fits either the IECor ANSI.

The user can choose between ANSI MC 96.1 or IEC 584-3 color coding for the
thermocouples. By default IEC 584-3 is selected.

The IPEmotion option can be found in the "IPEmotion options" → "Basic settings" → "Color
coding of thermocouples".

Figure 6.83 - Color Coding of Thermocouples

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

102

6.7.3 M-Modules Status-LED

LED Status

Off

Description

No power supply

Green Continuous

Power supply switched on, ready for operation

Free running mode
Green 1Hz 25%/75% flashing

Error
Green 5Hz 50%/50% flashing

Measurement running
(also synchronized)

Boot up, Initialization, Firmware download
running

Red Continuous

Internal error (Hardware)

CAN error
Red 1Hz 50%/50% flashing

Communication error,
e.g. connector unplugged respectively not fully
plugged in, cable broken or squeezed, faulty
bus communication

Red 5Hz 25%/70% flashing

Bus Overload

Red 1Hz 50%/50% flashing

Error in basic initialization of the module, cur-
rent configuration does not match to the device
firmware.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

103

6.7.4 M-Modules Channel-LED

Channel LED

Description

Off

No power supply

Yellow 1 Hz flashing

Recognition of the channel based on the selected
channel in IPEmotion / IPEmotion ME

Yellow Continuous

Channel Error:

-Over-current on excitation detected

- Sensor break or bridge break detected

- Counter overflow

- General Hardware error

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

104

6.7.5 X-Modules Status-LED

LED Status

Off

Description

No power supply

Green Continuous

Power supply switched on, ready for operation

Free running mode
Green 1Hz 25%/75% flashing

Error
Green 5Hz 50%/50% flashing

Measurement running
(also synchronized)

Boot up, Initialization, Firmware download
running

Red Continuous

Internal error (Hardware)

Red 1Hz 50%/50% flashing

Communication error,
e.g. connector unplugged respectively not fully
plugged in, cable broken or squeezed, faulty
bus communication

Red 5Hz 25%/70% flashing

Bus Overload

Green/Red 1Hz 50%/50% flashing

Supply voltage outside the valid range

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

105

6.7.6 X-Modules-Link-LED

Link LED

Off

Description

Status IN: Ethernet disconnected

Status OUT: Ethernet disconnected

Green 5 Hz 50%/50% flashing

Status IN: Ethernet connected

Status OUT: Ethernet disconnected

Yellow 5 Hz 50%/50% flashing

Status IN: Ethernet disconnected

Yellow/Green 5 Hz 50%/50% flash-
ing

Status OUT: Ethernet connected

Status IN: Ethernet connected

Status OUT: Ethernet connected

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

106

6.7.7 X-Modules Channel-LED

Channel LED

Description

Off

Device start up, Channel inactive

Yellow 1 Hz flashing

Identification of the selected
channel during Configuration

Yellow Continuous

Green Continuous

Red 1 Hz flashing

Waiting for user action

Sensor is plugged in but the channel is not
initialized.
Respective channel is still inactive

OK

- Signal measurement is running
(Sensor connected)

Error

Source of the fault could be:

-Over-current on excitation detected
- Sensor break or bridge break detected
- Counter overflow
- General Hardware error

Red Continuous

No sensor plugged in although channel is
active or Connection lost

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

107

7 Software Interface

7.1 IPEmotion Signals Work Space

The Signals work space is dedicated to configure your PlugIns and take measurements. All con-
figuration functions are explained in reference to the IPETRONIK X-PlugIn.

Figure 7.1 - X-PlugIn Signals Work Space

7.1.1 Ribbon Main Functions

The ribbon provides many functions but in this manual we only focus on the ribbon functions
related to the X-PlugIn. For detailed explanation of the ribbon and its functions, please refer to
the IPEmotion Software Manual.

7.1.2 Create a Measurement System

7.1.2.1 Detect the Hardware

When you start working with the analog measurement modules first you need setup the hard-
ware and cable sets as discussed (Refer to " X-Modules/Ethernet Modules Connection" on
page 89 or "M-Modules/CAN Modules Connection" on page 96).

A supported CAN card hardware and power supply is required for the CAN mod-
ule setup.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

108

The simple way to get started is to run the Detect function. Once you complete the
hardware setup, click the Detect function on the ribbon, IPEmotion PC automatically detects all
hardwares that are connected to the PC.

IPEmotion PC detects both Ethernet and CAN modules depending on the hardware setup con-
nected to the system. For more details of the Detect function, please refer to "Detect" on
page 140.

Figure 7.2 - Detecting the Hardware

7.1.3 Dry Configuration

7.1.3.1 IPETRONIK X-PlugIn

In the ribbon select the Hardware you would like to use for your dry configuration. In this case
select the IPETRONIK X PlugIn. The drop down list includes all PlugIns which were activated in
the OPTIONS→PlugIns. For more details, please refer to .

In some cases users cannot access the list box and make manual
configurations. In this case, in Options → Basic settings the
measurement configuration by MPC (Measurement Point Catalog) data
base file is activated.

For more details, refer to the chapter APPENDIX: Options of the IPEmotion
Software Manual.

Select IPETRONIK X PlugIn from the active hardware list, you will see the currently loaded
PlugIn version or activated PlugIns in the list.
For changing the PlugIn version you need to go back to Options → PlugIns. There you can
switch to previous versions.
An equal sign (=) behind the PlugIn version indicates that you will always use this version even
if a more recent PlugIn version is installed. For more details, please refer to "PlugIn Versions"
on page 9.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

109

7.1.3.2 System

The system is the next step after the PlugIn is selected. The system is basically the specific
hardware or interface that you are using to set up your data acquisition system. Each PlugIn
consists at least of one system.

Figure 7.3 - Two X-System Nodes Detected

▶ Import:-

This function allows the user to import a system. If you have an existing system setup that is
previously saved as .isf file, you can import the system setup using the .isf file and all
respective system and modules will be added to the system tree.

You can save a system file as .isf, only when there is a single system
and multiple modules in the system tree.

If there are multiple system in the system tree, IPEmotion lets you to
save as an configuration file (i.e .iwf or .iac).

Figure 7.4 - Import a System

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

110

7.1.3.3 Components

Below the system node you can add components provided the hardware is modular. In the
example the components are grouped in different categories like Voltage, Temperature, Pres-
sure, etc. measurement modules. For more details on Context Menu, please refer to "Software
Interface" on page 108.

Figure 7.5 - Access Components from the Ribbon

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

111

Figure 7.6 - Access Components from the Context Menu

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

112

7.1.3.4 Import and Export

Whether a PlugIn supports import or export functions also depends on the PlugIn imple-
mentation. The import is usually a shortcut to build your configuration. The import and export
functions depend on the selected interface of the system or module.
The below table shows the kind of files that can be imported and exported by the X-PlugIn.

IPETRONIK
PlugIn

Interface
Level

Configuration
Imports

Configuration
Exports

A2L (1)
CANdb (.dbc)
CANdb (.xml)
IPEmotion App (.iaw)
Measuring point plan

(.CSV) file

IPETRONIK X

System

No

(1) Only possible for X modules.

7.1.3.5 CSV Import/Export

▶ Operation mode of the CSV import:

The CSV import function does not create any new devices in the configuration. This means,
that the user is responsible for creating enough devices and channels of proper types
before starting to import.

The user selects an IPETRONIK-CAN node and later starts the CSV import (and selects the
file to be imported).

▶ Operation mode of the CSV export:

All channels of all supported devices below the selected IPETRONIK-CAN node are written
to the export file. The channels are written independent from the parameter "Active" of
affected IPETRONIK-CAN node, the device or channel.

Only parameters known to the specific channel are written to row data. All unknown para-
meters are left empty.

For example: The column "Supply Voltage" is written only for those channels supporting
the sensor supply voltage (e.g. Excluding M-THERMO channels).

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

113

▶ CSV File Structure:

▶ Column separator is the semicolon ';'

▶ The file contains exactly one header line

▶ The file must not contain any empty line above the header line

▶ The header line defines the column titles

▶ Every row below the header line contains the definition of one measurement channel

▶ Since the semicolon is defined as column separator, it MUST NOT be CONTAINED in

any element (comment, ...)

7.1.3.6 A2L Export

Export an A2L file containing the required data, which can be used by application software such
as ETAS INCA and Vector CANape to import the necessary configuration for measuring a
single X-Module or a system of X-Modules.

Figure 7.7 - A2L Export

A2L export supports different modes:

▶ Packed mode: When transmitting high sampling rates with XCP-DAQ lists, the computing

power and bus load increasingly became the limiting factor. To overcome this, the XCP spe-
cification V1.4 introduced Packed Mode, in which the Packed ID (PID), the time stamp (TS),
the number of transmitted sampling clocks and the data of the specified sampling clocks
are transmitted in a DAQ list packet.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

114

▶ Advantage:

▶ Medium bus load / medium CPU load

▶ Sampling rate up to several 100kHz

▶ Disadvantage:

▶ Not yet supported by all tools

▶ Non Packed Mode: The first implementation of XCP DAQ lists for the output of (meas-

urement) data was carried out with non-packed DAQ lists. The Packed ID (PID), the time
stamp (TS) and the data of a sampling clock are transmitted in a DAQ list packet.

▶ Advantage:

▶ Great support from many tools

▶ Disadvantage:

▶ High bus load / high CPU load

▶ Limited sampling rate (max. 10kHz)

▶ Dynamic DAQ lists: DAQ lists that can be defined by the XCP master in terms of sampling

rate and signals contained.

▶ Advantage:

▶ Broad support by many tools.

▶ Disadvantage:

▶ Must be configured first → Acquisition of measurement data is delayed by prior

configuration.

The Dynamic Lists are supported since X-PlugIn V02.22.01 and X-
FW V02.22.00

▶ Optional commands: Depending on the device firmware the A2L export of the IPEmotion

PlugIn IPETRONIK X adds the optional command 'GET_DAQ_CLOCK' to the exported file.

▶ Protocol version: Depending on the device firmware the A2L export uses XCP Protocol

Layer Version to export the DAQ list as a packed DAQ lists.

▶ Pre-defined DAQ lists: DAQ lists that are permanently stored in the X modules after con-

figuration with X-PlugIn and cannot be changed by the XCP master.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

115

▶ Advantage:

▶ Provides measurement data more quickly as no configuration is required.

▶ Disadvantage:

▶ No consistent support from all tools.

7.1.4 Configuration Check

This function checks the configuration on consistency. However, this function does not work for
all PlugIns. Messages are only returned if the PlugIn supports the check function.
For example considering the duplicate channel names across all active PlugIns across the
Signals and Acquisition work space. A comfortable function for message refresh and
configuration error searching is implemented in the configuration check function.

Figure 7.8 - Possible Configuration Issues / Problems

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

116

7.1.5 Status Signals

7.1.5.1 System Status Signals

The system LED status displayed in IPEmotion are shown in the table below:

System Status Colour

Signal System State

Green Continuous

Yellow Continuous

System active

No synchronization

Red Continuous

Cable not connected / cable error (error passive)

Incorrect baud rate / cable not terminated (bus-OFF)

The behaviour of system LED status reflects some error states of channels (and/or devices)
also by a yellow system LED status.

If the user uses the status column in the setup tree, it is easier to see which devices or channels
might have a problem without the need to look at all of the devices and/or channels.

▶ System Status Signal - Green : The system LED displays Green when all the connection

are active and no errors are found.

Figure 7.9 - System Status Color - Green

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

117

▶ System Status Signal - Yellow: The system LED lights up Yellow when the device syn-

chronization encounters an error.

The corresponding error messages are displayed in the Messages tab
located at the bottom of the IPEmotion software interface.

Figure 7.10 - System Status Color - Yellow

Figure 7.11 - Error Message

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

118

▶ System Status Signal - Red: The system LED displays Red when an error is found in the

cable connection.

Figure 7.12 - System Status Colour - Red

Figure 7.13 - Error Message - Cable Connection

The system LED status is independent from any device firmware.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

119

7.1.5.2 Device Status Signals

The X-PlugIn supports device status signals for M3-Modules and X-Modules. The device LED
status displayed in IPEmotion are shown in the table below:

Device Status Colour

Signal Device State

Green Continuous

Yellow Continuous

Red Continuous

Device active

Undervoltage detection

Missing license for an existing configuration

The behaviour of device LED status reflects some error states of channels also by a yellow
device LED status.

If the user uses the status column in the setup tree, it is easier to see which channels might have
a problem without the need to look at all of the channels.

The Device LED status is dependent on the Device type, Firmware and
PlugIn.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

120

▶ Device Status Signal - Green: The device LED displays Green when all the connection

are active and no errors are found.

Figure 7.14 - Device Status Signal - Green

▶ Device Status Signal - Yellow: The device LED displays Yellow when the device receives

an undervoltage. An undervoltage error message is displayed in the message tab.

Figure 7.15 - Device Status Signal - Yellow

Figure 7.16 - Error Message - Device Undervoltage

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

121

▶ Device Status Signal - Red: The device LED displays Red when there is an error in the

cable connection or a missing license for the existing configuration.

Figure 7.17 - Device Status Signal - Red

Figure 7.18 - Error Message - Red

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

122

7.1.5.3 Channel Status Signals

The channel LED status signal displays the status of a signal channel (e.g., sensor break or
overcurrent) in the status column of the channel grid.

Channel Status Colour

Channel Signal State

Green Continuous

Red Continuous

Transparent

Channel active

Sensor break/Overcurrent detected

Channel inactive

▶ Channel Status Signal - Green : The channel LED displays Green when all the con-

nection are active and no errors are found.

Figure 7.19 - Channel Status Signal - Green

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

123

▶ Channel Status Signal - Red: The channel LED displays Red when there is a Sensor

break or Overcurrent detected. In this case in the column Current value shows NoValue for
this channel.

Figure 7.20 - Channel Status Signal - Red

Figure 7.21 - Error Message - Channel

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

124

▶ Channel Status Signal - Transparent: The channel LED is Transparent when the channel

is inactive.

Figure 7.22 - Channel Status Signal - Transparent

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

125

7.2 Configuration Adjust Functions

7.2.1 Database

If you use sensors from the sensor database and run the Adjust → Database function, the
software automatically retrieves the latest sensor configuration from the database. With this
process you can automatically update all sensors with e.g. the latest calibration data from the
database in one click. Details on the sensor data base are discussed in the chapter "Sensor
Database" on page 211.

7.2.2 TEDS

When a hardware detection is executed with the TEDS (Transducer Electronic Data Sheet)
sensors connected to the analog inputs. The TEDS data stored in the TEDS chip in the sensor
are transferred to the channel scaling. You can view the TEDS icon if you add the symbol
column to the channel grid as shown below.

Figure 7.23 - TEDS Sensors

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

126

If the channel sensor modes are not a suitable range, the TEDS sensor will not be supported or
detected and an error message for the same is shown in the message tab.

Figure 7.24 - TEDS Error

The following M-Modules and X-Modules support TEDS:

▶ M-SENS

▶ M-SENS 8

▶ M-SENS 8 plus

▶ M-SENS2

▶ M-SENS2 250Hz

▶ M-SENS3 8

▶ Mx-SENS(2) 8

▶ Mx-SENS2 - 4

▶ Mx-STG2 6

▶ Mx-SENS 2 - 4 FAST

▶ Sx-STG

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

127

7.2.2.1 TEDS Sensor Detection with Automatic Unit Transformation

When you detect the TEDS sensors you can define an automatic unit conversion. This function
is required when the unit defined for the sensor does not meet the unit format required for the
measurement application. In order to activate this feature you need to add an additional entry in
the settings .xml file. In the example above the standard sensor was detected with the unit
[Nm].

When you add the following code into the settings.XML file the unit are automatically converted
to the preferred unit defined in the Options > Unit settings.

▶ C:\ProgramData\IPETRONIK\IPEmotion 2024 R2\Settings.XML

Always use the latest version of the IPEmotion software. The file path
remains the same, but the software version updates.

The new entry in the XML file is defined as:

<detectWithPreferredUnit>True </detectWithPreferredUnit>

Figure 7.25 - Add New Function for TEDS Unit Conversion to Settings.xml

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

128

The default unit defined in the Options → Units is [Nm/rad].

Figure 7.26 - Options: Example - Default Unit for Torque = Nm/rad

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

129

7.2.2.2 TEDS Adjust on Channel Level

All modules supporting the TEDS (Transducer Electronic Data Sheets) function support in the
IPETRONIK X-PlugIn a TEDS adjustment on channel level. Rather than synchronizing your
whole configuration across all TEDS channels, you can focus on a dedicated channel to
integrate the TEDS data from a connected sensor.

Figure 7.27 - Adjust TEDS Function changed unit from [Nm] to [Nm/rad]

Once the synchronization is completed the channel is updated with the TEDS data from the
sensor including the preferred unit defined in the Settings.xml file.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

130

7.2.2.3 Compare TEDS Sensor with Configuration

When a channel is already scaled based on TEDS parameters, you can use from the TEDS
compare function in the context menu to update the TEDS data e.g. when a new sensor was
connected to the input.

Figure 7.28 - Compare TEDS on Channel Level

When a TEDS sensor is detected the data is saved into a database file called IPESensorData-
base.xmt. In the "Scaling Calculator" on page 200 section we will discuss "How to retrieve
sensor data from the sensor database".

▶ C:\Users\Public\Documents\IPETRONIK\IPEmotion\Database\IPESensorDatabase.xmt

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

131

7.2.3 Offset Adjust

The offset adjustment is a very useful function to check and update the physical measurements
to the configured measurement range. With an offset operation you can shift the current sensor
signals on the analog inputs as your new base reference. The offset function can be performed
during the online measurements of the system.

If the user provide the Reference value the offset value is adjusted in
reference with the reference value. If no reference value is provided then the
offset value is adjusted in reference with the input value given to the device.

Figure 7.29 - Offset Adjust Dialog

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

132

The offset operation can be performed for all channels or only for dedicated groups. In this
example below 2 sensor groups are defined. Each channel can be rated to a group. In the below
example for channel 3 and channel 7(assigned to group 1) a sample reference value of
3 .00 V and 7.00 V is provided then with the selection option you select the channel that you
grouped or all based on your requirements and Start the adjustment.

Figure 7.30 - Offset Operation Organized by Groups

After the offset operation the initial analog measurement of 3.012 V and 7.012 V is considered
as an offset value and the incoming signal of 3 V and 7 V as reference value. With the offset
operation the 3 V and 7 V channel line is shifted by 0.012 V. This is graphically indicated on the
available measurement range column which is now reduced (red section).

Figure 7.31 - Updated Offset Values

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

133

The data of the offset dialog can be exported as .TXT file.

Figure 7.32 - Export Offset Data to .TXT File

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

134

7.2.3.1 Group Offset Adjustment

The user can add the Group channel to the column from the column chooser. Group channel
displays and enables editing the group index for offset adjustment directly in the channel grid.
With this extension, it is now possible to edit and display the parameter without the need to open
the offset adjustment dialog.
The values are presented with a drop down menu, where the user can select between "None"
and one of the Groups 1, 2, 3 or 4.

Figure 7.33 - Group Offset Adjustment

The displayed group names cannot be edited.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

135

7.2.4 Shunt Check

The shunt check function is only implemented for the strain gauge module Sx-STG and Mx-
STG2 6. A strain gauge is used to measure structural load e.g. a chassis frame.

During installation and test sensors can be overstretched or damaged. This overload or damage
of the sensor is not visible without applying a shunt check. Those damages can result in wrong
measurements.

Shunt check is used to verify the installed sensor. Shunt checks are performed before and after
a measurement. The step response of the shunt check must be the same before and after the
test.

Figure 7.34 - Shunt Check Dialog for Strain Sensors

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

136

When the shunt check is raised the bridge resistance is measured and the results are displayed

Figure 7.35 - Shunt Check Results

You can also execute the shunt check via a dedicated hot key command. The configuration of
the hotkeys is explained in "Hotkey Operation: Offset Adjust and Shunt Check" on the next
page. The shunt check can be also made visible in the online measurements like in the yt-chart
as indicated below. During the shunt check operation the measurements are online updated in
the yt-chart. The shunt check data can be saved into the measurement file which makes it con-
venient to compare the shunt check before and after your test.

Figure 7.36 - Shunt Check Results - Bridge Response

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

137

7.3 Hotkey Operation: Offset Adjust and Shunt Check

You can operate IPEmotion through hot keys. This is practical for re-occurring operations in
situations where manual navigation with a mouse is too difficult. In the list box Command you
select the a specific function from a work space. Then you define the key to execute this com-
mand. Valid hot key combinations are those which do not create any characters (letters, num-
bers or special signs).

With a hotkey you can access to functions without using the software user interface. For the
offset adjust and shunt check operation and many other functions custom hot key can be con-
figured in the options.

Figure 7.37 - Hotkey Operation: Offset Adjust and Shunt Check

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

138

7.3.1 Adding a Hotkey for Offset Adjust and Shunt Check

To add a new hot key function you need to select the required workspace area first. Within each
area, the dedicated functions are implemented.
In the example of shunt check or offset adjust you need to select the Area: Signals. Once the
function is selected, click the down arrow to expand the dropdown further later you select and
define the hotkey function via keyboard.

Figure 7.38 - Hotkey Functions

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

139

7.4 Access

7.4.1 Detect

When you start working with your analog measurement modules you need setup the hardware
and cable sets as discussed above. A supported CAN card hardware and power supply is
required. The simple way to get started is to run the Detect function as indicated below.

Figure 7.39 - Detect

The Detect function is a very convenient function to identify any hardware connected to the IPE-
motion software. Not every PlugIn supports automatic hardware detection. Usually, USB device
interfaces support automatic hardware detection.

The Detect function is applied to all active PlugIns. It is recommended to use the Detect func-
tion only for the very first time when you start to set up your measurement configuration. If the
hardware configuration changes by adding or removing the modules, you need to execute the
Synchronize function to update the complete hardware configuration in the system tree.
For more details on the Synchronize function, please refer to "Synchronize" on page 143 .

The user can customize the name of the channel as per their usage or requirement of the mod-
ules and to factory reset the modules, click "Reset" on page 148.

Figure 7.40 - M-modules and Custom Channel Naming

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

140

If you execute the Detect function the complete configuration of
Signals of all connected devices is recreated. Additionally, all the
configurations from the Acquisition work space are removed.

7.4.1.1 Mapping

The Hardware Mapping is a very convenient function for merging configuration (IWF) files to
the currently connected hardware. If you execute the Mapping function, the current con-
figuration is compared to the currently connected hardware. IPEmotion starts the hardware
detection to identify all currently connected modules.

The Mapping function compares the current configuration (IWF) to the currently detected hard-
ware across all PlugIns.

Figure 7.41 - Mapping

The Mapping function only support those PlugIns which support
automatic hardware detection.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

141

In the below example you will see how to use the mapping function in practice. There are
applications in which the same configuration is applied to different hardware setups.
For example, every IPETRONIK module consists of an unique front number. When you
initiate the Mapping process it detects one new module as shown below, with the mapping func-
tion you can match the actual hardware configuration to the configuration file.

Figure 7.42 - Configuration and New Detected Hardware

You can define several mapping relations by linking one module from the right side to one mod-
ule of the left side.
In order to perform the mapping, you need to select the modules that you like to map from the
detected hardware to the corresponding configuration. The mapping process works basically
from right to left with the arrow button to save the mapping between the modules.

To map the newly detected device, do as follows:

1. Select the modules you like to map (one on each side only)

2. Press the [←] button to execute the mapping process.

Figure 7.43 - Mapping Process

The Mapping function can be applied across different modules of same types.
The system does not let you to map different modules with characteristic.
For example:M-SENS module to a M-THERMO module.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

142

When you confirm the mapping process via the OK button the new module type including the
device serial number is updated. However, the channel configuration remains untouched.

Figure 7.44 - Old and New Module Mapping

7.4.1.2 Synchronize

The Synchronize function is designed to update an initial configuration (IWF) with an updated
hardware setup. Synchronize function is the counterpart of the Detect function.
As discussed above the Detect function helps to create your initial module setup. In practice the
module setup can change where new modules are added or removed to the configuration. With
the Synchronize function you can update your modules easily to your configuration.

Figure 7.45 - Synchronize- Before Sync

The Synchronize function do not change any configurations defined in the
Acquisition work space.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

143

If you make changes to your measurement hardware by adding new modules or removing
modules, it is recommended to use the Synchronize function to reflect the hardware changes in
your module tree. When you click Synchronize after adding the new modules to the hardware
setup they are added to the tree on the left pane.

Figure 7.46 - Synchronize - After Sync

If in case the modules are removed, an error icon is shown in front of the module serial number.

Figure 7.47 - Sync - Error

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

144

7.4.1.3 Device Detection on Different Baudrates for Hardware Initialization

Hardware initialization is significantly improved to simplify the setup process and enhance
device detection reliability.

Previously, users were required to manually configure and initialize all connected devices to
match the system’s current baud rate before making any changes. This meant, devices must be
first detected or initialized at the system’s default baud rate, after which users could modify baud
rate settings and reinitialize the devices. This process was especially limiting when switching
between the configurations with different baud rate.

Starting with version V02.23.00, the PlugIn now offers automatic baud rate detection to resolve
this limitation.
If no device responds at the system’s configured baud rate during initialization, the PlugIn will
automatically attempt communication using alternative baud rates defined in the PlugIn options
under Hardware Detection. Once a device is detected at one of these alternative rates, the
PlugIn establishes communication and automatically reconfigures the device to match the sys-
tem’s baud rate (For example: Switching from 500 kBd to 1 MBd).

This enhancement removes the need for manual pre-configuration and allows for seamless
device detection and initialization, even when the baud rates of the devices and the system do
not initially match.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

145

7.4.2 Initialize

With the Initialize function you can write the changes in the configuration to the hardware and at
the same time test the communication between the hardware and IPEmotion.
If there are any configuration errors or the hardware cannot be reached, messages are
displayed in the message tab. Depending on the PlugIn version the error, info or warning icons
are indicated.

Figure 7.48 - Initialize

The Initialize function updates the connected hardware with the latest configuration
parameters defined in IPEmotion. The configuration is downloaded to the devices, so when you
run a hardware detection the latest configuration settings like channel name, scaling etc., are
automatically retrieved from the module and displayed in IPEmotion. However, in many cases
the hardware cannot store a configuration. In this case, the configuration is stored only in the PC
but is not transferred and stored in the hardware.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

146

Configuration settings that are stored in the IPETRONIK modules internally:

▶ Channel name

▶ Physical units

▶ 2-Point scaling

▶ Free 2 point scaling

▶ Factor offset scaling

▶ Sensor measurement range

▶ STG mode

▶ Data type (format)

▶ Characteristic curves (for X-Modules only) (Refer to "Characteristic Curve Tab (X-Mod-

ules/M3-Series/M-THERMO 96)" on page 238).

Configuration settings that are not stored in the IPETRONIK modules internally:

▶ Channel Description (only 32 characters will be stored)

▶ NoValue

▶ V-TAB (Refer to "VTAB " on page 208)

▶ V-TAB range (Refer to "VTAB Ranges" on page 207)

▶ Multipoint scaling - The internal multipoint scaling of both the X-Modules and M3-Modules

will be stored (Refer to "Multipoint Scaling" on page 204).

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

147

7.4.2.1 Reset

The reset function is for the instruments which can store a configuration in the device. After
reset, all configurations stored inside the device are set back to factory default.

Figure 7.49 - Reset to Default / Factory Settings

The Reset is applied to all PlugIns which support the Reset function. The
Reset function is implemented and used for IPETRONIK modules and data log-
gers as these instruments can store default configuration.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

148

7.4.3 Display

The Display button turns your configuration into measurement mode. Then the user can view
the measurement values for all active channels.

By using Tune-up button instead of Display button it is possible to change ALL parameters. For
more details, please refer to "Quick Analyzer" on the next page and "Tune-up" on page 153.

Figure 7.50 - Tune-up

Figure 7.51 - Display Online Measurements

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

149

7.4.3.1 Quick Analyzer

With the Quick analyzer you get a direct preview to the channel signal. The analyzer
performs auto scale and shows the current value. Within the instrument you can switch easily
between channels of the same module. Some of the IPETRONIK X-Modules and all
M3-Modules with the latest firmware support a Fast Setup functionality. With the Fast Setup,
some channel properties can be changed without device initialization. These
configuration elements are performed on the fly while measuring without interrupting the actual
measurement.

Figure 7.52 - Quick Analyzer

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

150

Figure 7.53 - Quick Analyzer Window

Only X-Modules and M3-Modules support fast setup functionalities and refers to
sensor mode, measurement range, physical scaling, sensor excitation, filter settings, other HW
specific settings, offset adjust and shunt check. The function shunt check is for the strain gauge
inputs. The offset adjustment is supported on all voltage inputs.

Figure 7.54 - Quick Analyzer - Offset and Shunt Check Adjustment

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

151

The default time window or update rate of the quick analyzer scope window is 1000 ms (1
second). However, if you access the properties via a right click on the x (time axis), you can
change the display time range from 0.001 ms (1 micro second) up to 2000 ms (2 seconds).
For more details on the Block factor, please refer to IPEmotion Software Manual.

Figure 7.55 - Quick Analyzer - Time Range / Update Settings

In the quick analyzer window you can also set the Sensor excitation for the X-Modules
during the fast setup.

Figure 7.56 - Quick Analyzer - Sensor Excitation

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

152

7.4.3.2 Tune-up

The fast setup functionality is extended by some parameters, that require IPEmotion to operate
in the special "Tune-up" mode.
To start IPEmotion's "Tune-up" mode, the user must select "Tune-up" in the sub menu of the
ribbon button "Display"

Figure 7.57 - Tune-up

Following parameters are affected when you use the Tune-up feature:

▶ Sensor Mode

▶ Sensor Min / Max

▶ Physical Min / Max / Unit

▶ Sensor Excitation

▶ STG devices further supporting

▶ Bridge Type

▶ Bridge Resistance

▶ Bridge Connection

The Tune-up feature is supported by following devices:

▶ M3-Modules

▶ X-Modules Only

▶ Mx-STG2 6

▶ Mx-SENS2 4

▶ Mx-SENS2 4 FAST

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

153

When exiting the fast setup or tune-up mode, a message box appears to prompt you to either
save the changed parameters or discard them.

Figure 7.58 - Message box

7.5 View

7.5.1 Details Area

With the Details button in the ribbon you can view or hide all detail tabs for systems, modules
and channels configuration.

Figure 7.59 - Details Enabled

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

154

7.6 Firmware Update

With the firmware update function, you can update the module firmware directly from the PlugIn.

To update the firmware of the module, you need to click on the X-system node then click the
Functions option on the ribbon. In the Functions dropdown select Update devices.

Figure 7.60 - Firmware Update

The update dialog will show the current firmware version of the detected modules and will also
indicate the Target firmware available on the computer. Select the module that is required to
update and click Update.

Figure 7.61 - Module Firmware Update Interface.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

155

Once you click the Update button the update, process is started and a progress bar indicates
the percentage of completion.

Figure 7.62 - Module Firmware Update Progress Information

In the library tab of X update you can see the detailed information about the firmware latest
firmware version available on the computer.

Figure 7.63 - Firmware Library

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

156

During the PlugIn installation process the firmware data base will be installed together with the
IPETRONIK-X PlugIn in the default directory.

▶ C: \ProgramData\IPETRONIK\Firmware

Figure 7.64 - Firmware Default Directory

In the case you install an older IPETRONIK-X PlugIn version after a newer
version was installed, the firmware folder will be overwritten by the latest
installation. To prevent this from happening you may choose a
different directory for the firmware folder of each PlugIn version. Then you
can import the firmware directories accordingly to your needs.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

157

7.7 Module License Update

In order to perform a license update, you need to detect the module in the first place. After that
you add the module specific license key into the IPEmotion license dialog. With the assign
function in the license dialog the new license key is activated on the module. After a power-cycle
and the detection of the new hardware, new licenses information is displayed.

Figure 7.65 - Module License Update

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

158

8 X-PlugIn Interface Configuration

As discussed in the earlier sections the IPETRONIK X-PlugIn is the main PlugIn for
IPETRONIK module product lines available for CAN bus or Ethernet communication. Both CAN
and Ethernet interface settings are discussed below. There are also plenty of device-specific
tab settings which are individual to each PlugIn. Detailed descriptions about different settings
are part of the individual PlugIn manuals.

8.1 System Tree

8.1.1 Column Chooser

Column chooser lets the user to view or add additional properties to the devices and modules
connected via IPEmotion. The user can right click on the column header and activate the
column chooser in the system tree. The scope of functions in the column chooser depends on
the scope of the implementation of the PlugIn.

Figure 8.1 - Column Chooser

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

159

In the example below 3 additional columns are added on device and try to indicate the
Frontnumber, Device Type and Firmware version. You can filter and sort across all
additional columns if required.

Figure 8.2 - Column Chooser on Module / Device Level

8.1.2 Context Menu

The context menu offers convenient functions for setting up your application. With right click on
the system, module or channel you can access the context menu. The functions provided in
the context menu depend on the PlugIn. Some PlugIns offer plenty of functions and other just
provide some basic functions.

Figure 8.3 - Context Menu

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

160

▶ Components: The user can add the components to modular hardware structure based on
the requirements. Components can be added in the Ribbon and as well as from the Con-
text Menu, please refer to " X-PlugIn Interface Configuration" on page 159.

▶ Change into: Change into function can convert a component/module to another type.

Basically, if you build your configuration offline and you change the type of some modules
without rebuilding the complete configuration, you switch modules with the ”Change into”
function.
The Change into function will also try to shift the software configuration to the new module
provided the function are supported. The configuration between SENS modules is most
likely compatible. When the configuration is transferred between module types, the sensor
excitation is set to zero as modules support different sensor excitation types (unipolar or
bipolar) and sometimes different voltage levels.

Figure 8.4 - Change Into

▶ Functions: With the Functions you can do Firmware update by right click on the system
on CAN or ETH interface level. However, on Module level you can run an offset adjust of
all channel or different channel groups when those groups are defined. You can also
access the Functions from the ribbon, please refer to " X-PlugIn Interface Configuration"
on page 159.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

161

Figure 8.5 - Function Options

▶ Import/Export: This function refers to the same function as implemented in the main rib-

bon. There are plenty of different import and export functions available. It is mainly related
to configuration files like A2L, CANdb, Autosar etc. For more details, please refer to " X-
PlugIn Interface Configuration" on page 159.

▶ Adjust TEDS: For more details on TEDS, please refer to " X-PlugIn Interface Con-

figuration" on page 159.

▶ Use as default: This function is useful for all users who need to create the same

configuration several times. If the user saves the master configuration as Default, all
systems are created with this order of modules, automatically. The default configuration is
saved and can be deleted in the File menu and the user can only define one template for
one interface.
For example: You cannot have different module configurations for IPETRONIK X.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

162

Figure 8.6 - Use as Default Template

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

▶ Copy to file: With this function the user can save module configurations in a separate file

with the extension .ITF. The .ITF file can be imported, as well.

▶ Paste from file: Import .ITF files which include all selected modules, channels and con-

figuration elements.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

163

Figure 8.7 - Import ITF file

▶ Properties: If you select ”Properties” from the Context menu, another display pop up

opens summarizing the Settings tab for configuration. The properties are context sensitive.
If you select a module you will get the context for Module configuration. If you open the con-
text menu on Channel level you can see all configuration tab sheets related to the channel.
You can also view the properties by selecting the Details on the ribbon. Please refer to " X-
PlugIn Interface Configuration" on page 159.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

164

Figure 8.8 - System Properties

Figure 8.9 - Module Properties

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

165

Figure 8.10 - Channel Properties

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

166

8.1.3 M3-Module Order

With the new M3-Module generation, the modules detected order in the software system tree is
same as their physical location in the measurement chain. This has significant benefits com-
pared to the older M2 series. Here the user can back trace better in case of module problems or
replacement activities in the measurement chain.

Figure 8.11 - M3 Module Order

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

167

8.1.4 X-Modules Order

The X-Modules detected order in the software system tree is same as their physical location in
the measurement chain. This provides significant benefits to the user where the user can back
trace better in case of module problems or replacement activities in the measurement chain.

Figure 8.12 - X-Modules Order

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

168

8.1.5 Module Health Status Channels

The M3-Module generation is supporting internal health status information as separate
channels. These channels can be activated as an optional components from the module context
menu.

Figure 8.13 - M3-Module Health Status Signals

▶ Device supply voltage: Indicates the level of supply voltage.

▶ Device supply current: Indicates the supply current to the module.

▶ Device power consumption: Calculates the power consumption of the individual

module.

▶ Device temperature: Indicates the internal temperature of the module.

▶ Channel error status: Indicates the channels error status for a channel error like "sensor
break" or "overcurrent" as a bit per channel (provides 1 status when channel error occur)
and supports the same sample rates 1 / 2 / 5 / 10 Hz.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

169

Depending on the device type, the signal is defined as 8-Bit or 16-Bit
unsigned integer value.

▶ If the device has 8 input channels, then the signal data type is 8-

Bit integer unsigned.

▶ If the device has 16 input channels, then the signal data type is

16-Bit integer unsigned.

▶ Status signal undervoltage: Provides 0 or 1 status when the module is operated in the

undervoltage range. The minimum voltage for operation is 6 V.

Figure 8.14 - Status Signal Undervoltage

For the X-Module only the Status undervoltage is implemented.

Figure 8.15 - X-Module Health Status Signal

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

170

8.2 System Details Area

8.2.1 General Tab

Figure 8.16 - General Tab

▶ Active: Here you can activate or deactivate the system.

▶ Name: Here you can define the name of the system.

▶ Description: Here you can define an individual description for the system.

▶ Reference: The reference is automatically generated and defined by the software.

▶ Comment: Here you can add a comment.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

171

8.2.2 Ethernet Hardware Tab

Figure 8.17 - Ethernet Hardware

▶ IP4 address range: The default IP4 address range for the X-Modules is defined as

192.168.232.1 to 192.168.232.40. However, in some cases the company Ethernet network
settings can require a different IP address range which can be modified in the PlugIn
Options discussed in "Ethernet Interfaces Settings" on page 12.

▶ Network interface: Here, the name of the network interface of the computer or data

logger is indicated. This information is indicating on with Ethernet port the modules are
connected. The first X-Module is working as a DHCP server and assigns the right IP
address matching to the module factory settings to the network interface (if configured).

▶ X-Link load: This is a calculated statistical value indication how much data is running over

the Ethernet interface.

▶ Internal time synchronization: The Precision Time Protocol (PTP) time synchronization
master is installed together with the PlugIn to synchronize the time between modules.
However, in some cases external time synchronization might be required.

▶ Default send interval: The Ethernet communication support block data transfer with is

sending data every 10 ms which is equal to 100 Hz. However if higher block data transfer is
required it can be deactivated. In this case the block data transfer is every 2 ms with is
equal to 500 Hz.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

172

The X-module assigns an IP-address to the LAN port of your computer. The first X-module
operates as a DHCP server. However, if your computer requires a different IP address range
because IT policies you can change the IP address range of the modules in the X-PlugIn
settings. Please refer to "Ethernet Interfaces Settings" on page 12.

Figure 8.18 - Ethernet- Computer Network Settings

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

173

8.2.3 CAN Hardware Tab

Figure 8.19 - CAN Hardware Settings

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

500 K Baud. However depending on cable length or necessary sample rates, the baud rate
can be set to lower or higher values. For more information on cable length, please refer to
table in "M-Modules Cable Length" on page 52.

▶ Device data rate: Baud rate used to transfer the payload of the CAN-FD frames. The non-
payload parts of the frame will still be transferred using the CAN baud rate. The user can
choose the device data rate between Standard CAN to 5 MBd as per their requirement.
For more details, please refer to table in "M-Modules Cable Length" on page 52.

▶ Bus load: The bus load is a calculated statistical value by the CAN server, indication how

much data is running over the CAN bus.

▶ Baud rate initialization: Here you can define if the Baud rate configured above will be ini-
tialized to the CAN hardware. This is necessary when using the same CAN hardware as
other PlugIns.

Additional CAN interface settings like supported CAN card vendors, scanning baud rates, CAN
ID placing etc., can be configured in the PlugIn Options, please refer to "CAN Interfaces Set-
tings" on page 15.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

174

8.2.4 Options Tab

Figure 8.20 - Options Tab

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

175

8.3 Module Details Area

8.3.1 General Tab

Figure 8.21 - General Tab

▶ Active: You can activate or deactivate the module.

▶ Name: You can define the name of the module. The default name is based on the serial

number.

▶ Description: You can define an individual description for the module.

▶ Reference: The reference is automatically generated and defined by the software.

▶ Comment: Here you can add a comment.

▶ Sampling rate: In the drop down box, the sample rate for the module can be defined. The
sample rate is set for the entire module. The lowest sample rate is 1/min and the fast
sample rate is depending on the module type and can reach up to 5 kHz for the SIM-STG
module. This parameter is only available for CAN modules of the M1/M2-Series.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

176

8.3.2 Extended Tab (For CAN-Modules)

Figure 8.22 - Extended Tab (For CAN-Modules)

▶ Front number: In this field the device front number is displayed. When you run a detect

function the front number is automatically detected and extracted from the serial number.
The serial number is composed of the front number and the device type number.

▶ Clock: The default configuration is the Free-running mode. However, a synchronized mode
is supported too, where the first module operate as a clock master and all the other mod-
ules as clock slaves. The clock can only be changed in the PlugIn settings discussed in the
section, "CAN Interfaces Settings" on page 15.

▶ CAN bus load: This is a statical value calculated by the PlugIn. Higher sample rates will

increase the bus load.

▶ 29-bit identifier: With this check box you can activate the extended CAN identifier. The

standard CAN identifier is 11-bit.

▶ Additionally:

▶ Fast break detection:

▶ Only for M-THERMO (T) (16)

▶ Device data rate:

▶ Only for M3-Series

▶ Time before 1st data [in ms]: Time before the device sends the first data after the start of a
measurement. The device prevents any data transfer to avoid sending bad measurement
values during transient conditions. Please refer to "Options Settings" on page 21.

▶ Only for M-SENS(2) devices.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

177

8.3.3 Extended Tab (For M3-Modules)

Figure 8.23 - Extended Tab (For M3-Modules)

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

This setting is only available for M3-Series but not possible for X-
Modules.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

178

Selecting 'Off' or 'Sawtooth' will set all measurement channels into the
corresponding simulation mode.

Figure 8.24 - Signal Simulation

▶ Clock: The default configuration is the Free-running mode. However, a synchronized mode
is supported too, where the first module operate as a clock master and all the other mod-
ules as clock slaves. The clock can only be changed in the PlugIn settings discussed in the
section, "CAN Interfaces Settings" on page 15

▶ CAN bus load: This is a statical value calculated by the PlugIn in percentage. Higher

sample rates will increase the bus load.

▶ Device data rate: For more information, please refer to "CAN Hardware Tab" on page 174

▶ Measurement mode (Only M-THERMO3 16): Minimum required Firmware version on

device V01.07.00. Earlier firmware versions may exhibit limitations related to the handling
of the number of active channels in accordance with the device license.

The device supports switching from the standard "Default" measurement mode to a "Raw
value" measurement mode. This setting can be configured via the device’s "Extended" con-
figuration page, using the "Measurement mode" parameter.

Figure 8.25 - Measurement Mode - M-THERMO3 16

The "Measurement mode" parameter provides two selectable options:

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

179

▶ Default: When "Default" is selected, the device operates in its standard temperature
measurement mode, consistent with behavior in previous PlugIn versions. In this
mode, the device provides one measurement channel per thermocouple input or hard-
ware channel.

Figure 8.26 - Default Measurement Mode

▶ Raw values: When "Raw values" is selected, the device is configured to

operate in raw value measurement mode, with standard temperature measurement
and processing disabled. In this mode, the typical temperature measurement channels
are deactivated and hidden from the user interface.

Instead, the system generates two channels per hardware input, which provide raw
measurement data for the following:

▶ Thermal voltage

▶ Cold junction temperature

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

180

Figure 8.27 - Raw Values Measuement Mode

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

181

8.3.4 Extended Tab (For X-Modules)

Figure 8.28 - Extended Tab (For X-Modules)

▶ Front number: In this field the device front number is displayed. When you run a detect

function the front number is automatically detected and extracted from the serial number.
The serial number is composed of the front number and the device type number.

▶ Signal simulation: For more details on Signal simulation, please refer to "Extended Tab

(For M3-Modules) " on page 178.

▶ CAN send rate: Output rate for sending CAN messages instead of / additionally to

Ethernet frames by the X-Module. This function is only available when on channel level a
CAN output is configured.

▶ CAN bus load: This is a statical value calculated by the PlugIn. Higher sample rates will

increase the CAN bus load.

▶ X-Link load: This is a statical value calculated by the PlugIn. Higher sample rates will

increase the Ethernet bus load.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

182

8.3.5 Information Tab

Figure 8.29 - Information Tab (M2-Modules and X-Modules)

▶ Calibration date: In this field the last calibration date is indicated.

▶ Hardware version: In this field the hardware version of the module is indicated.

▶ Firmware version: In this field the current firmware version of the module is indicated. The

firmware can be updated as discussed above in the section, "Software Interface" on
page 108.

▶ License information: Some modules support additional licensing functions like the TEDS

functionality, additional DSP filters and the FAST sample rates. These licenses are
delivered from the company as a part of the order. However, it is also possible to update the
modules with new license after purchase.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

183

Some modules provide additional information.

▶ The M3-Modules provide additional information about the Adjustment date, Download

kernel version and Device variant.

Figure 8.30 - Information M3-Modules

▶ Adjustment date: Provides the information about the date of last adjustment.

▶ Device variant: Identifies a certain variant of the device type. The Channel

connector type can be LEMO 1B 7p/ ODU-F 6p.

▶ The SIM STG and all Ethernet X-Modules provides information about the FPGA version.

▶ The MULTIdaq, M-SENS24, M-RTD2 16 and M-RTD2 32 indicates a Cluster information
which includes the serial number and the size of the cluster. On module level inside the
cluster additional information about the cluster position and the sub-serial number of the
individual device is indicated.

Figure 8.31 - Cluster Information

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

184

The M-FLOW device provides information about the M-FLOW signal conditioning unit and sep-
arate information about the flow turbine. A firmware updated is not supported via X-UPDATE
function of the PlugIn.

Figure 8.32 - M-Flow Information

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

185

8.4 Channel Configuration

8.4.1 Column Chooser in the Channel Grid

In the channel grid head line you can access the context menu to add additional columns to your
channel grid. The available columns depends on the PlugIn.

Figure 8.33 - Column Chooser

The channel grid can be customized as per user requirements. For more information channel
customization, please refer to "Channel Customization" on page 256.

8.4.2 Column Chooser Fields

The following list provides an overview of all additional column chooser fields.

Not all modules support all functions.

▶ Active

▶ Aliasing-free

▶ Averaging

▶ Averaging depth

▶ Bridge resistance

▶ Bridge type

▶ Bus type

▶ CAN FD

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

186

▶ CAN identifier [hex]

▶ CAN send rate

▶ Channel controller version

▶ Comment

▶ Connection

▶ Cyclic

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

187

▶ PAK active

▶ Phys High

▶ Phys Low

▶ Phys Max

▶ Phys Min

▶ Port

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

188

▶ Set start value

▶ Shuntcheck resistance

▶ Shuntcheck tolerance

▶ Signal output medium

▶ Signal simulation

▶ Software filter cutoff frequency

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

189

8.4.3 Channel Supporting Reset to Factory Default

All channels and signals are compatible with the IPEmotion context menu function "Reset to
factory default". This function essentially performs the same action as the "Reset to default"
option in the context menu, with the added feature of resetting the channel name to its default
value.

This method only resets all parameters and the channel name to their
default settings in the configuration. The values are NOT sent to the con-
nected devices.

It is important to note that the values on the hardware device remain
unchanged. The values are not written to the device until the next hardware
initialization, or implicitly when starting a measurement or saving data.

Figure 8.34 - Reset to Factory Default

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

190

8.5 Channel Details Area

8.5.1 General Tab

Figure 8.35 - General Tab

▶ Active: Checkbox to activate or deactivate a channel.

▶ Name: Default name but can be changed to individual names.

▶ Description: Default description but can be changed to any individual description.

▶ Reference: Is automatically generated and very useful to check where the channel is linked

to.

▶ Comment: Here you can add a comment.

▶ Sampling rate (X-Modules and M3-Modules Only): Select the module sample rate from

the drop down list.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

191

8.5.1.1 Defining the List Box Entries of Channel Names

For the channel name you can also define a pull down menu.

Figure 8.36 - Channel Names

The entries of the pull down menu are stored in a CSV file with the name (ChannelNames.csv)
in the following user settings directory.

▶ C:\ProgramData\IPETRONIK\IPEmotion 2024 R2\UserSettings.

Always use the latest version of the IPEmotion software. The file path
remains the same, but the software version updates.

Figure 8.37 - Structure of the ChannelNames.csv file

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

192

8.5.2 Format Tab

The Format tab sheet is only visible for the users who activates this function in
Options→Expert mode→Extended tabs. In the Format tab sheet we can configure a couple
of functions which are usually only relevant for expert users. The different configuration func-
tions are explained below.

Figure 8.38 - Format Tab

▶ Data type: This refers to the data format (resolution) of the measurements. Depending on
the module/instrument, sometimes different formats are supported. On most of the instru-
ments, it is not possible to change the configuration of the data type. They always transmit
data in the same format. For IPETRONIK modules only unsigned format and floating point
format is possible.
Some modules support a change in the data type format from a drop downlist as indicated
below.

Figure 8.39 - Data Type Change

▶ Task: The task is a very special setting developed for some specific PlugIns. For

X-PlugIn Task is always in "Default".

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

193

▶ NoValue: This configuration is important for all users who would like to see a certain beha-
vior when NO measurements are received in the IPEmotion or the channel suffers from an
hardware failure like sensor break or overcurrent. The default configuration is that NoVal-
ues are recorded in the data file. They are indicated as NoValue in the Data manager. In
the Yt-chart in the Analysis work space you will see missing data points in the graph. The
software will always store NoValue in the data file irrespectively what you select from the
drop down box. In the data file NoValue is stored and in the diagrams you will see missing
data points.

▶ Storing NoValue Value in Devices: NoValue values are stored in all device types.

The NoValue setting for M-Modules and X-Modules is stored within the devices solely
to enable the restoration after hardware detection.

This storage is for user convenience, as the device firmware does not process this vari-
able. Instead, the device sends its default value when it is required to send a NoValue,
typically corresponding to -FullScale or null.

▶ DefaultValue: Another configuration option is a check box to enables the DefaultValue.

With this check box you change the storage and display behavior when no measurements
are received. With the check box you can show and store +FullScale,
−FullScale or NULL as a numerical value.
(You can only select NULL if you have a bipolar (or signed) measurement range data
format with a negative an positive part like ± 10V). An unsigned measurement is only cov-
ering positive measurements.

Drop down selection has no impact when the check box
"Deactivate Novalue" is deactivated.

Figure 8.40 - NoValue/DefaultValue

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

194

Figure 8.41 - Data Manager and Analysis

The NoValue configuration also has an impact on the data display in the View work area. As
the screen shot below indicates. When the check box ”Deactivate NoValue and use
DefaultValue” is not activated the instrument will show always Novalue.
Filter has an impact when check box "Deactivate NoValue" is activated. In this example
+FullScale of the measurement range will be stored.

Figure 8.42 - Activate the Default Value

However if the check box ”Deactivate NoValue and use Default Value” is activated you will
enable the list box entries and the instrument will show the selected values for:

▶ +Full Scale

▶ -Full Scale

▶ Null

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

195

Figure 8.43 - Data Manager and Analysis

DefaultValue Null: The DefaultValue (NULL) is related to the Null value of the binary
measurement range. If you select a signed 16-Bit (2^16 = 65536) measurement range, the
temperature signal for the IPETRONIK thermo module it is split up between the values
-32768 and +32767 as the graphic demonstrates below.

Figure 8.44 - DefaultValue Null

Figure 8.45 - NoValue=NULL

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

196

The binary NULL value of this measurement range is 655 °C. This value is then indicated to the
online instruments and stored in the data file.

Figure 8.46 - NULL Value

Figure 8.47 - Data Points for NULL Shows 655 °C

For X-PlugIn signed 16Bit and signed 32Bit the above configuration is not
possible. In this case switch to unsigned 16Bit / 32Bit.

▶ Channel type: The channel type indicates the data direction Input or Output.

The X-PlugIn support only channel type input and it is not configurable.

Figure 8.48 - Channel Type

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

197

8.5.3 Scaling Tab

IPEmotion Sensor Scaling - Please refer to the video link: https://youtu.be/7uWNIrpT0AM to
understand "How do Analog Sensors Work".

Figure 8.49 - Scaling Tab

The basic scaling operations can be defined directly in the scaling tab sheet. The scope of
functions depends on the PlugIn and IO module type. Some inputs, especially analog inputs,
support many different functions, ranges and provide more scaling options.

▶ Sensor mode: The sensor mode covers the main measurement type, for example Volt or

Current, accelerometers (IEPE). You can select the sensor mode from your drop-down list.
In this example, the analog input module supports many different measurements of thermo
element. The supported sensor modes are defined by the PlugIn and you can only select
the mode which is supported. Many modules only support one static sensor mode.

Figure 8.50 - Sensor Mode and Thermo Module Example

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

198

▶ Sensor range: The next configuration option is the sensor measurement range. The range
is related to the measurement mode. For thermo elements, the measurement range is pre-
defined and cannot be changed. The available voltage and current measurement ranges
depend on the functionality of the analog input. In the example below you can select ranges
from -0.1 V up to 100 V. The Unit is automatically linked to the selected
measurement mode Voltage >V or Current >A or Temperature >°C and cannot be
changed manually.

Figure 8.51 - Sensor Range

▶ Physical range and engineering units: The physical range is related to your engineering
units. Here you can define into which unit (mm, bar, etc.) the electrical signal is converted.

Figure 8.52 - Physical Range and Engineering Units

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

199

8.5.4 Scaling Calculator

For advanced scaling functions you can use the scaling calculator. This interface provides many
different scaling functions which is discussed in the below sections.

Figure 8.53 - Scaling Calculator

8.5.4.1 Channel Settings

Figure 8.54 - Channel Settings

▶ Sensor mode: Is related to the type of measurement mode as discussed above in "Scaling

Tab" on page 198.

▶ Sensor range: Is related to the measurement range as discussed above in "Scaling Tab"

on page 198.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

200

▶ Unit: To simplify the conversion between engineering units you can use the change unit

editor. Switching between the units only works within the same engineering unit family like
temperatures, pressures, weight, energy, etc.

Figure 8.55 - Converting V into mV

▶ The main advantage is that the new engineering unit automatically converts the physical
measurement range. As shown in the screenshot, 100 V are automatically converted to
100000 mV. This conversion also works across different metric standards.

Conversion for Example:

Name

Pressure

Unit

Bar >kbar >mbar >psi >etc.

Temperature

°C >K >°F

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

201

8.5.4.2 2-Point Scaling

This is a classical scaling configuration using two points, usually the Min and Max value of the
physical range of the sensor. The scaling information is included in the data sheet / calibration
sheet of the sensor.

Figure 8.56 - 2-Point Scaling

8.5.4.3 Free 2-Point Scaling

This scaling mode offers the possibility to scale the sensor range and the physical range
(engineering units) at the same time.

Figure 8.57 - Free 2-Point Scaling

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

202

8.5.4.4 Factor/Offset Scaling

This scaling method uses the Linear equation Physical value (y) = m *x + b (b= offset) with
(m = slope factor). The m-factor influences the slope >1 steeper slope / <1 flatter slope. The
offset-b shifts the physical value by a constant value.

Figure 8.58 - Factor/Offset Scaling

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

203

8.5.4.5 Multipoint Scaling

The multipoint scaling is a scaling method that allows to define a nonlinear scaling with as many
data points as possible.

The multipoint scaling parameters are only stored in IPEmotion. They are
not transferred to the instrument unless the instrument is supporting this
function.

Figure 8.59 - Multipoint Scaling

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

204

8.5.4.6 STG Strain Gauge

In this interface, strain gauge bridge types can be configured. The types of strain gauge bridges
are as shown below. The types are visible in the drop down.

Figure 8.60 - STG Strain Gauge

The bridge types being displayed in the scaling calculator and the bridge
type parameter of the channel do not have 1:1 mapping.

The scaling calculator defines only certain scaling settings, so the channel's
bridge type parameter can be modified after exiting the dialog.
This is particularly important when selecting the general 'Bridge' type. If a
different bridge type, such as quarter or half, is connected the proper value
can be adjusted later.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

205

Bridge Types

Scaling Calculator

Channel Parameter (Device)

Quarter bridge

Half bridge, 2 active STG

Quarter bridge

Half bridge

Half bridge, 1 active, 1 transverse STG

Half bridge

Full bridge, 4 active STG

Full bridge

Full bridge, 2 active, 2 transverse STG (linear)

Full bridge

Full bridge, 2 active, 2 transverse STG (non-linear)

Full bridge

Bridge

Full bridge

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

206

8.5.4.7 VTAB Ranges

This scaling method converts measurements of a specific range into a text message. If the
measurement value is in a defined range you can see the corresponding text information on an
alphanumerical instrument in the View work area.

The VTAB Ranges are only stored in IPEmotion. They are not transferred to
the instrument unless the instrument is supporting this function.

Figure 8.61 - VTAB Ranges

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

207

8.5.4.8 VTAB

In this mode you can relate a specific integer (1, 2, 3, 4, ..) value to a specific text display. You
can display this text on the View work area for example in an alphanumerical instrument.

The VTAB are only stored in IPEmotion. They are not transferred to the
instrument unless the instrument is supporting this function.

Figure 8.62 - VTAB

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

208

8.5.4.9 Active Sensors

Figure 8.63 - Active Sensors

8.5.4.10 Passive Sensors

Figure 8.64 - Passive Sensors

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

209

8.5.4.11 Snapshot - Test Measurement

You can perform a test measurement within the scaling calculator to check your scaling and to
see the actual measurements. Three different test measurements are supported:

▶ Snapshot

▶ Average over values

▶ Average over time

Figure 8.65 - Snapshot

Figure 8.66 - Test Measurements

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

210

8.5.5 Sensor Database

The scaling calculator supports a sensor database. In this database, the scaling parameters of
many different sensors are included. If you select a sensor from the database, you have directly
defined the measurement range and the physical range and, if needed, a sensor excitation.

Figure 8.67 - Sensor Database

In this example, you see a shunt for high current measurements. This shunt can measure ±10
Amperes and the output of the shunt is ±1 Volt. The sensor requires a 10 Volt sensor excitation.

Figure 8.68 - Shunt Sensor

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

211

8.5.5.1 Adding New Sensors to Database

The sensor database (SDB.exe) is installed with each IPEmotion installation in the following dir-
ectory:

▶ C:\Program Files (x86)\IPETRONIK\IPEmotion 2024 R2\Tools

If you like to add your sensor to the existing standard database, it is recommended to import the
standard sensor database. The database is installed in the following directory.

▶ C:\ProgramData\IPETRONIK\IPEmotion 2024 R2\Database

You can also create your own sensor database XML file from scratch. If you like to use your own
database file, you have to store it in the right directory and give the file the correct name:
IPESensorDatabase.xml

IPEmotion can only work with one database XML file.

You can add new sensor by means of the SensorDB editor. This tool is installed along with IPE-
motion and entries can be made through the GUI.

Figure 8.69 - SensorDB Editor

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

212

If you save the new sensor and restart IPEmotion, the new sensor will be included in the data-
base and can be selected for channel scaling. Serial numbers and calibration dates can be
defined, as well.

Figure 8.70 - SensorDB Database Properties

However, you can import your own database from Excel using the import function of the
SensorDB Editor. The import function is explained in the help manual of the SensorDB Editor.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

213

8.5.5.2 The Database Format

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

214

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

215

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

216

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

217

8.5.5.3 Multipoint Linearization

The sensor data base is supporting sensor linearization functions. You can add for sensors
multipoint linearization into sensor data base XML file. In the XML file you can add value pairs of
”Physical reading / Sensor Output”.

Figure 8.71 - Multipoint Linearization

The sensor specific linearization information can only be added through the
XML file directly. The Sensor Database Editor and the corresponding
CSV/Excel import function is currently not supporting this function.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

218

8.5.5.4 Adding New Sensors

The sensor data base is a powerful tool to simplify the channels scaling and reduce scaling
error. You can now add your own sensor to the data base. All the settings defined in the sailing
interface are saved to the data base. All scaling entry modes are supported to add individual
sensors. For more info please refer to "Scaling Calculator" on page 200.

Figure 8.72 - Adding New Sensors

When the sensor parameters are defined you can add the sensor header information by
accessing the add button.

Figure 8.73 - Sensor Header Information

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

219

After you have created the sensor in the database you can search for your sensor. The example
below shows the parameters as defined in the scaling calculator.

Figure 8.74 - Sensor Properties Defined

When a sensor was added to a user define sensor data base file it is saved in:

▶ C:\Users\Public\Documents\IPETRONIK\IPEmotion\Database\ IPESensorData-

base.xmu

▶ Extension u = User defined sensor database.

If you like to modify a manually created sensor you need select the sensor from the sensor data
base and you can modify settings in the scaling interface. With the function save sensor to data
base the modifications are overwritten.

There is no possibility to delete a sensor from the sensor data base. If you need
to remove a sensor permanently you need to delete it from the XML files.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

220

8.5.6 Terminal Tab

In the Terminal tab, you have the information about the analog input and circuit design. This
function is only available for all X-Modules, all THERMO modules and new CAN based M3-
Module. The graphic is indicating on which pin which signal is running. The graphic is aligned to
the input configuration or measurement mode. Some modules support different modes in one
module like the Sx-STG where IEPE, strain gauge, or voltage measurement can be con-
figured.

Figure 8.75 - Terminal Tab

The terminal tab circuit diagram changes depending on the Sensor mode that the user select in
the Scaling tab. The user can view the circuit diagram in the Terminal tab and also the user can
click on the diagram and enlarge the view for a better understanding.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

221

Figure 8.76 - Scaling and Terminal Tab

Figure 8.77 - Magnified View

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

222

8.5.7 Display Tab

Display tab covers the display settings for the online View work area. The display tab is also rel-
evant for formula channels and scaling channels. The main configuration elements are:

Figure 8.78 - Display Tab

▶ Displaying area: Covers the initial Y-axis scaling of the y-t chart.

Figure 8.79 - Displaying Area

▶ Formatting: Covers the decimal places. The default setting is Automatic which will show

as many decimal places as provided by the PlugIn.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

223

▶ Name (Display): Covers the display name which can differ from the channel name. The

display name is only relevant for the View work area. The display name will not be used for
formulas and other functions like limit or range monitoring. If you like to see the display
name on the instruments, you need to activate this function in IPEmotion Options → View.

Figure 8.80 - Display Name

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

224

8.5.7.1 Define Standard Decimal Templates on Module Level

When detecting modules, the default setting of the decimal paces is defined as Automatic.
However, if you like to define a default setting for the number of decimal places you like to use
you can add to the Settings.XML a new command line in order to use the template as default.

The settings XML file is stored on the following directory:

▶ C:\ProgramData\IPETRONIK\IPEmotion 2024 R2\Settings.xml

Always use the latest version of the IPEmotion software. The file path
remains the same, but the software version updates.

In the settings XML you have to add in the section ”Common Settings” the following
command line: <detectWithTemplate>True <\detectWithTemplate>

Figure 8.81 - Detect Modules

You can disable the function also by setting the command line to "False".
Command line: <detectWithTemplate>False <\detectWithTemplate>

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

225

With this command line you can save a lot of time because all modules will be detected with the
number of decimal places as defined in the template. The template is applied to all channels of
the module.
For example: Template with 2 decimal places for the Mx-SENS2 4 is created as shown below.

Figure 8.82 - Decimal Place and Save the Template

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

226

8.6 Module Dependent Tabs

8.6.1 Thermo Tab (M-Modules)

The thermo tab setting is only specific for the M-Thermo Modules. In the M2-Modules the user
can Activate/Deactivate the Averaging and Sensor break detection, whereas in the
M3-Modules the user can input the Averaging depth value in the filter tab.

▶ Averaging depth: Activate/Deactivate averaging the values. For other M-Devices, you can

find the Averaging depth option in the "Filter Tab (M-Modules)" on page 236.

Figure 8.83 - Thermo

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

227

8.6.2 Excitation Tab

Defines the excitation for the connected channel. The default value is "0" and the sensor excit-
ation range can mostly vary from 0V to +/-15V but other limits depending on device type are also
possible.

Figure 8.84 - Excitation Tab

8.6.2.1 Resetting Sensor Excitation after Change of Sensor Mode

If the sensor mode of a channel is changed, the sensor excitation (if supported) is automatically
set to 0 V to protect the sensor from potential damage.

Certain channels and sensor modes have a fixed sensor excitation. If the
sensor mode is switched to one of these fixed modes (e.g., IEPE) or applied to
channels with preset excitation (e.g., channels 1-20 on a M-SENS 24), the ori-
ginal sensor excitation will be maintained.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

228

8.6.3 Mode Tab (M-CNT2)

Figure 8.85 - Mode

▶ Frequency time out mode: Influences the behaviour of the frequency measurement of the

decreasing values.

▶ Static direction input: Sets if the direction input is a static signal.

Ignore Frequency Drop: If activated, sudden drops of measured frequency values will be
ignored and the last measured frequency before the drop is used. The sensitivity of this feature
can be controlled by the PlugIn option "Frequency drop tolerance". The drop voltage can be
configured in the PlugIn options.
For more details refer to "Options Settings" on page 21.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

229

Figure 8.86 - Option Settings

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

230

8.6.4 STG Mode

This tab allows the user to define the general settings for the STG mode.

Figure 8.87 - STG Mode

8.6.4.1 Bridges

In this section the use can define the Bridge type, Bridge resistance and the Connection
which defines the conductor count that are connected to the bridge at the entry. Based on the
bridge type you select the terminal image also gets updated accordingly:

▶ Quarter bridge with 4 wire connection and bridge completion:

Figure 8.88 - Quarter Bridge

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

231

▶ Half bridge with 6 wire connection:

Figure 8.89 - Half Bridge

▶ Full bridge with 6 wire connection:

Figure 8.90 - Full Bridge

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

232

8.6.5 Signal Filters

Filters of analog measuring amplifiers are used for avoiding interrupting frequencies (frequency
spectra, which do not contribute to the signal and/or which cannot be processed by the system).
A low pass filter, which reduces the amplitudes of the frequencies above a specific cut-off
frequency, is usually used for avoiding negative effects to the useful signal. The threshold in the
range of the cut-off frequency (the barrier between the useful and the unrequested signal) is
continuous. Useful signals below the cut-off frequency are also damped. A damping of 3 dB at
the cut-off frequency means a reduction of the initial signal of 30 .

The image below shows the result of two inputs with the same input signal of 4 V amplitude and
12.5 Hz frequency.

Figure 8.91 - Impact of Filter (Signal Shift)

▶ Channel 2: Black curve without filter

▶ Channel 3: Red curve with 30 Hz hardware filter (Bessel type). Channel 3 shows the main
behaviors of filters like the damping, the phase shifting, and the start oscillation of the
filtered signal.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

233

8.6.5.1 Hardware Filters

Although today's microprocessors provide a high processing power, the use of hardware filters
is still essential. Especially when users cannot exclude that (periodic) signals can pass the AD
converter and software filter, which cannot process the signals. Every sampling system follows
Shannon sampling theorem whereby one must at least sample with twice the signal frequency.
Otherwise, aliasing effects can occur, whereas the acquired frequency is considerably lower
than the actual signal (See image "Aliasing Effect" below).

8.6.5.2 DSP Software Filters

The hardware filter at the input excludes a distortion by frequency spectra above the system
limit with the maximum sampling rate. Depending on the application, it can be required to lower
the cut-off frequency.
For example: M-SENS devices provide a switchable hardware filter with cut-off
frequency depending on the maximum internal sampling rate. If the cut-off frequency is e.g. 50
Hz, interrupting frequency spectra (of devices with additional software filter) in the range
between 50 Hz and the hardware filter frequency can be filtered with DSP. The filter frequency
can be configured in defined steps up to the hardware filter frequency.

8.6.5.3 Aliasing Effect

Despite sophisticated measurement engineering, errors can occur due to wrong settings.

For example: A 100 Hz signal is acquired with a sampling rate of 100 Hz system can
independently acquire the correct signal, but the result is wrong because the sampling rate was
set too low.

Figure 8.92 - Aliasing Effect

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

234

8.6.5.4 Filter Tab (X-Modules)

Figure 8.93 - Filter Tab - X-Modules

▶ Hardware filter: For more details, please refer to "Hardware Filters" on the previous page.

▶ Software filter:For more details, please refer to "DSP Software Filters" on the previous

page.

▶ Type: The user can define the filter characteristic to the read the data. There are 3 dif-

ferent types:

▶ Bessel

▶ Butterworth

▶ Elliptical

▶ Frequency: The user can define the frequency limit.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

235

8.6.5.5 Filter Tab (M-Modules)

▶ M2- Modules:

Figure 8.94 - Filter Tab - M2-Modules

▶ Hardware filter: Allows the user to select from given frequency. For the M-Modules

the hardware filter is only available for the supportive devices. For more details, please
refer to "Hardware Filters" on page 234.

▶ Averaging : Block average which do an averaging from the internal samplerate of the

module to the selected samplerate (sendrate on the CAN bus).

For an aliasing free measurement, please refer to "Options Settings" on page 21.

▶ M3-Modules:

Figure 8.95 - M3- Modules

▶ Hardware filter: Allows the user to select from given frequency. For the M-Modules

the hardware filter is only available for the supportive devices. For more details, please
refer to "Hardware Filters" on page 234.

▶ Software filter: For the M-THERMO3 16 the hardware filter is fix and cannot be

configured.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

236

▶ Type: The user can define the filter characteristic to the read the data. The soft-

ware filter type can be configured to:

▶ Off

▶ Bessel

▶ Butterworth

▶ Elliptical

▶ Frequency: The user can define the frequency limit. For the M-THERMO3 16 the

filter frequencies range from 0.1 Hz up to 16.666 Hz.

▶ Averaging depth: Defines window width of the averaging with the minimum value as

1 to maximum values as 100.

For an aliasing free measurement, please refer to "Options Settings" on page 21.

8.6.6 Data Output Tab (X-Modules)

Here you can configure the signal output medium. This configuration setting is only available for
the X-Modules.

Figure 8.96 - Data Output Tab (X-Modules)

▶ Configuration Signal output: You can select the signal output medium as CAN, Ethernet
or Ethernet +CAN. The user can set the CAN send rate for the CAN based output medium
as per the send rates that the module support.

▶ CAN settings: Here the user can define the identifier of the CAN message and first byte of

the signal within the CAN message.

This setting only available to edit when the Automatic CAN ID placing is
disabled. Please refer to "Options Tab" on page 175

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

237

8.6.7 Characteristic Curve Tab (X-Modules/M3-Series/M-THERMO 96)

Here you can configure the use of characteristic curves instead of default sensor mode.

Figure 8.97 - Characteristic Curve Tab

▶ Select curve: You can select the characteristic curve for each individual channel. For
THERMO-Modules the sensor mode would changed to thermo element (without type).

The X-Modules applies multipoint scaling in the same manner as M-SENS3 8. These devices
use multipoint scaling as the final step. Internally, the measurement value is first determined as
if no multipoint scaling is defined, based on the configured sensor range. The active multipoint
scaling is then applied in the last step before the result is sent.

The M-THERMO3 16 devices use the characteristic curve as a substitute for one of the stand-
ard thermoelement definitions. For custom thermo element, please refer to "Custom Thermo Ele-
ment" on page 242.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

238

8.6.7.1 Configuring the Characteristic Curve

The user can select to configure the characteristic curve for each channel. The general con-
figuration of the characteristic curve is described below but depending on the device type, there
are distinct usages and interpretations of the characteristic curves:

▶ Using the curve for (nonlinear) output value scaling

▶ Using the curve as custom response replacement for standard thermo element definitions

This manipulation of characteristic curves in the dialog is not directly related
to a certain channel.

The characteristic curve of the each channel can be configured. Either you can load the pre-
defined values in .csv file format or manually add the Physical value and Acquisition value in
the pop window. You can also save the configuration file in a .csv format with the Save char-
acteristic option.

To configure the characteristic curve for a channel, do as follows:

1. Go to the Characteristic curve tab.

2. Select the channel in the drop down and click Configure.

Figure 8.98 - Configure Window

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

239

3.

In the configure window, you get two options to configure the characteristic curve as
mentioned above.

▶ Load configuration: You can load the pre-defined values in the .csv file.

Figure 8.99 - Load Configuration

Figure 8.100 - Configuration Loaded

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

240

▶ Save configuration: You can manually add the Physical value and Acquisition value
also notice the graph variations during you input the value. Then save the file in a .csv
format.

Figure 8.101 - Save Configuration

▶ The dialog can be closed by pressing:

▶ OK: Applying all changes to the device (and adapt channel's physical ranges if

required).

▶ Cancel: Discard all changes made by the user in the dialog.

Any changes made to files on the disk are immediately permanent
and cannot be undone.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

241

8.6.7.2 Custom Thermo Element

M-THERMO3 16 devices support custom thermo element definition/characteristic curves/ mul-
tipoint scaling. To support this feature, devices require a minimum firmware version of
V01.05.00.

There are some special "rules" that apply to the use case of the M-THERMO3 16.

It’s important for users to note that the processing in the M-THERMO3 16 dif-
fers from the M-SENS3 8.

In the M-THERMO3 16, the characteristic curve replaces one of the standard thermoelement
curves (such as "Thermo element of type K") and is used to process both the cold junction
temperature and the measurement value. As a result, the following outcomes occur.

▶ Custom thermo element / characteristic curves / multipoint scaling can only be used if the

sensor mode "Thermo element" is configured.

▶ The sensor range values "Sensor Min" and "Sensor Max" are defined by the

configured curve. The values are adapted automatically and cannot be modified by the user
other than modification of the curve itself.

▶ It is an error, if the sensor mode is set to "Thermo element" but no curve is selected or an

invalid curve is chosen.

▶ It is an error, if a characteristic curve other than "None" is configured while the sensor mode

is set to something other than "Thermo element."

▶ In the configuration dialog for characteristic curves, the physical and sensor units are not

editable and are not interpreted in any way.

▶ The characteristic curve response or custom thermo element type is always defined such

that:

▶ Sensor range is given in "µV": Valid range is -156250µV ... +156250µV

▶ Physical range is given in "°C"

It is not possible to use different units for physical range (e.g. "mV"
or "°F" or "K").

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

242

▶ If the device temperature or the measurement value is out of the thermo couple defined

range, the complete device does not measure any valid value.

For Example: Defining a thermo couple in the range of 30°C ... 250°C but the device tem-
perature is 25°C which leads to invalid measurements such that the device will send NoVal-
ues. This is because of the internal calculations considering the cold junction
temperature which must also lie inside the thermo element definition.

▶ If the user needs the measurement value to be in a different temperature scale (e.g. "F"

instead of "°C", this is still possible using the normal scaling calculator).

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

243

8.6.8 Extended (X-Modules and M3-Modules)

In the X-Modules and M3-Modules signal simulation can be configured individually on meas-
urement channels. However, it is not possible to configure signal simulation for monitoring sig-
nals (device supply voltage, current consumption, etc.).

Allowed values for each measurement channel are:

▶ Off

▶ Sawtooth

Figure 8.102 - Extended - Channel

You can also configure the signal simulation in the "Module Details Area" on page 176.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

244

8.7 Calculation Signals

X-PlugIn provides calculation signals of M-SENS3 devices. The signals can be added to the con-
figuration either by selecting them from the device's "Components" or channel's "Functions"
menu.

Figure 8.103 - Calculation Signals

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

245

8.7.1 Calculation Signal: RMS (Root Mean Square)

The RMS signal calculates the root mean square value of the configured input channel.
The maximum number of the device's RMS signals is identical to the number of its meas-
urement channels (e.g. M-SENS3 8:8).
The RMS sensor and physical ranges are always identical to the source channel's ranges.

On the signal's configuration page 'Input signal', the relevant parameters for RMS
calculation can be configured.

▶ Source channel: This parameter defines the physical signal source, representing the

channel for which the RMS value will be calculated.

▶ Block averaging depth: This parameter defines the window width for averaging,

representing the number of internal blocks used. The minimum value is 1 (no averaging),
and the maximum value is 100.

Figure 8.104 - RMS Input Signal

▶ Each measurement channel can be referenced only by one RMS meas-

urement signal.

▶ Deactivating the source channel automatically deactivates the

calculation signal.

▶ Activating the source channel will not activate the calculation signal.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

246

8.7.1.1 Adding RMS Signal Channels

The "Source channel" parameter is automatically preset based on how an RMS signal is added
to the device configuration.

▶ Adding by the device's "Components" menu: "Source channel" is ALWAYS set to the 1st

channel.

▶ Adding by channel's "Functions" context menu: "Source channel" is set to the

selected channel(s).

8.7.2 Calculation Signal: Active/Reactive/Apparent Power

The power calculation signals calculate the power from 2 input measurements. These input
measurements are configured on the configuration page "Input signal".

The calculations rely on the assumption, that the physical value of "Source channel 1" is a
voltage measurement and the physical value of "Source channel 2" is a current
measurement.

The device support 3 different power calculations:

▶ Active Power ( W)

▶ Reactive Power ( VAr)

▶ Apparent Power ( VA)

Figure 8.105 - Calculation Signal: Active/Reactive/Apparent Power

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

247

8.7.3 Calculation Signal: Phase Shift Angle

The calculation Signal "Phase Shift Angle" calculates the phase shift angle between source
channel 1 (voltage) and source channel 2 (current). The angle is calculated in radiant (rad).
Sensor range is -3.15 to +3.15 rad.

The configuration signals "Phase Shift Angle" is principally done the same way as the power
signals.

Figure 8.106 - Calculation Signal: Phase Shift Angle

There are some special configuration rules for this signal:

▶ Sensor range is fix to -3.15to +3.15 rad and independent from the

input signals.

▶ Physical range and unit are editable ( it is possible to change physical

scaling e.g. degree).

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

248

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

249

10 Appendix

10.1 Introduction to CAN-FD

This improved protocol overcomes two CAN limits: You can transmit data faster than with 1
Mbit/s and the payload (data field) is now up to 64 byte long and not limited to 8 byte anymore.
In general, the idea is simple: When just one node is transmitting, the bit-rate can be increased,
because no nodes need to be synchronized. Of course, before the transmission of the ACK slot
bit, the nodes should be re-synchronized.

CAN-FD data frames can be transmitted with two different bit-rates: In the arbitration phase the
bit-rate depends on the network topology and is limited to 1 Mbit/s; in the data phase the bit-rate
is limited by the transceiver characteristics.

Figure 10.1 - CAN-FD Phase

Using a ratio of up to 1:10 (500kBit/s / 5MBit/s) for the bit-rates in the arbitration and data phase
leads to an approximately six-times higher throughput considering that the CAN-FD frames use
more bits in the header (control field) and in the CRC field.

Figure 10.2 - Classical CAN v/s CAN-FD

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

250

10.1.1 Structure of CAN-FD Message

CAN-FD data frames uses reserved bits, called FDF (FD frame) bit. If it is of recessive value,
the following bit sequence is interpreted as a CAN-FD data frame. If it is of dominant value, it is
a Classical data or remote frame. In the newly introduced BRS (bit rate switch) bit, the second
bit-rate is applied, when it is of recessive (r) value. If it is of dominant (d) value, the arbitration
phase bit-time setting is used in the data phase.

Figure 10.3 - Structure of CAN FD Data Frames

Abbreviation

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

251

Figure 10.4 - CAN-FD Frame Formats

Abbreviation

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

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

252

The control field comprises additional bits not provided by the Classical CAN data frames. The
FDF (FD Format) bit indicates the usage of FD frame formats. At the sample-point of the BRS
(Bit-Rate Switch) bit, the bit-rate switch is performed. This guarantees a maximum of robust-
ness. The following ESI (Error State Indicator) bit provides information about the error status: a
dominant value indicates an error active state.

Figure 10.5 - Extended Control Field

Abbreviation

Description

IDE

FDF

BRS

ESI

Identifier Extension

Flexible Data rate Format

Bit Rate Switch: Recessive, if alternate bit-rate

Error State Indicator: Recessive, if error passive

During the standardization process of the CAN-FD protocol, some additional safe guards were
introduced in order to improve the communication reliability. This is why the CRC field com-
prises 17-Bit (for frames with payloads up to 16 byte) or 21-Bit (for frames larger than 16 byte)
polynomials and an 8-Bit stuff-bit counter plus a parity bit. The CRC field use Fixed-Stuff Bits
(FSB) with an opposite value of the previous bit. All these safe guards guarantee that all single
failures are detected under all conditions. Even the possibility to detect multiple failures is
improved.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

253

10.2 CAN Card Hardware Interfaces

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

IPETRONIK

CAN Interface

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

CANcardXLe
CANcardXL
CANcaseXL
CANboardXL
CANboardXL compact
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
VX1131
VX1121

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

254

Vendor
Vector

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

ICS
ICS
ICS
ICS

DREWTECH
I+ME ACTIA

Kvaser

Peak

Softing

ICS

CAN Interface
VX1135

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
Memorator Pro
Memorator Light
USBcan Pro 5xHS
USBcan Light
Ethercan
BlackBird
BlackBird V2
Hybrid

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

ValueCAN
ValueCAN3
ValueCAN4
ValueCAN4-4

Mongoose
Basic+24 XS

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

255

Vendor

ETAS
ETAS
ETAS
ETAS

CAN Interface

ES581
ES582
ES593
ES595

ETAS

Ethernet Systems

10.3 Channel Customization

You can add your own columns into your channel grid. In order to add individual columns you
need to create a new xml file called: Customize.XML in the installation directory.

▶ C:\Program Files\IPETRONIK\IPEmotion 2024 R2\Customize.xml.

Figure 10.6 - Customize.XML - User Defined Key Fields

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

256

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

The following screenshot shows a channel grid which includes 3 individually defined ”KEY
fields”.

Figure 10.7 - Key Fields

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

257

10.4 Hidden Options

Only expert users of the IPEmotion software should modify these hidden
options.

10.4.1 Don't Permit to Change the CAN Interface Configuration

User can configure the system to prevent changes to the CAN interface configuration during
hardware device detection. This is especially useful when an M3 device is detected with a stand-
ard CAN 500 kB, while the device’s CAN configuration is set to CAN FD 500/500 kB.

The option "dontPermitToChangeCANInterfaceConfiguration" is inten-
ded ONLY for the INCA usage.

This feature is enabled by setting the following parameter in the PlugIn option file 'X.IMO'
under '%ProgramData%\IPETRONIK\IPEmotion VERSION\MAL\IPETRONIK\X'.

<?xml version="1.0" encoding="utf-16"?>
<IPEmotionXmlFile version="1" docType="MalOptionSettings">
 <MalOptionsSettings id="0" typePrefix="IPETRONIK.IPEmotion.Acquisition.MalPool">
    <ParameterList>
...
 <dontPermitToChangeCANInterfaceConfiguration type-
e="Boolean">true</dontPermitToChangeCANInterfaceConfiguration>
...
    </ParameterList>
  </MalOptionsSettings>
</IPEmotionXmlFile>

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

258

10.4.2 Ignore Cluster Information during Hardware Detection

You can configure the system to ignore specific cluster device information, allowing these
devices to be detected as individual units located directly under the system (specifically within
the hidden deviceSynchronisationNode).

The option "deviceDetectionIgnoreClusterInformation" is intended ONLY
for IPEmotion Calibration Edition.

This feature is enabled by setting the following parameter in the PlugIn option file 'X.IMO'
under '%ProgramData%\IPETRONIK\IPEmotion VERSION\MAL\IPETRONIK\X'.

<?xml version="1.0" encoding="utf-16"?>
<IPEmotionXmlFile version="1" docType="MalOptionSettings">
 <MalOptionsSettings id="0" typePrefix="IPETRONIK.IPEmotion.Acquisition.MalPool">
    <ParameterList>
...
 <deviceDetectionIgnoreClusterInformation type-
e="Boolean">true</deviceDetectionIgnoreClusterInformation>
...
    </ParameterList>
  </MalOptionsSettings>
</IPEmotionXmlFile>

10.4.3 Use Short Default Names for Devices

The user can configure whether the default device names after creation should include only the
front number instead of the complete serial number.

For Example: If the default name after manual creation usually is '59102468' only '2468' is dis-
played as name.

After a hardware reset (triggered by either IPEmotion or Default-Plug), the
device name is automatically reset by the firmware to the standard
'IPETRONIK' format (e.g., '59102468'). This name is stored in the device
parameters.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

259

However to provide a more consequent user experience, the PlugIn will displays only the short
name '2468', if the device parameter is equal to the 'IPETRONIK' default value.

This affects following operations:

▶ Hardware reset

▶ Hardware detection

▶ Hardware synchronisation

This feature is enabled by setting the following parameter in the PlugIn option file 'X.IMO'
under '%ProgramData%\IPETRONIK\IPEmotion VERSION\MAL\IPETRONIK\X'.

<?xml version="1.0" encoding="utf-16"?>
<IPEmotionXmlFile version="1" docType="MalOptionSettings">
 <MalOptionsSettings id="0" typePrefix="IPETRONIK.IPEmotion.Acquisition.MalPool">
    <ParameterList>
...
 <useShortDefaultDeviceNames type="Boolean">true</useShortDefaultDeviceNames>
...
    </ParameterList>
  </MalOptionsSettings>
</IPEmotionXmlFile>

10.4.4 Aliasing Free Settings Per Channel

By default (as in previous versions), this configuration applies globally across the entire PlugIn,
meaning that either all devices or none are limited to aliasing-free measurement settings.

However, you can specify whether a particular channel should be exclusively configured for ali-
asing-free measurement.

This feature is enabled by setting the following parameter in the PlugIn option file 'X.IMO'
under '%ProgramData%\IPETRONIK\IPEmotion VERSION\MAL\IPETRONIK\X'.

<?xml version="1.0" encoding="utf-16"?>
<IPEmotionXmlFile version="1" docType="MalOptionSettings">
 <MalOptionsSettings id="0" typePrefix="IPETRONIK.IPEmotion.Acquisition.MalPool">
    <ParameterList>
...
 <aliasingFreePerChannel type="Boolean">true</aliasingFreePerChannel>
...
    </ParameterList>
  </MalOptionsSettings>
</IPEmotionXmlFile>

The default value is taken from the PlugIn option 'aliasingFreeFilterSettings' that can be mod-
ified on the PlugIn options page 'Options'.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

260

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

261

The default value is used after:

▶ Manual device creation

▶ Hardware detection

▶ Hardware synchronisation (only new devices!)

▶ Hardware reset

This feature is specifically designed for certain custom setups and can only be modified through
the 'Aliasing Free' column in the channel grid. By default, this column displays the current
'aliasingFreeFilterSettings' option.

Supported Devices:

The aliasing-free measurement setting is available for the following devices:

▶ M-SENS2

▶ M-SENS2 250Hz

▶ ES313.1

▶ All M-SENS(2) types with DSP

▶ M-RTD2

▶ SIM-STG

▶ Mx-SENS2-8

▶ Mx-SENS2-4

▶ Sx-STG

▶ Mx-STG2

When enabled, the aliasing-free setting of one channel can affect the avail-
able settings of other channels. This rule applies to all M-devices and chan-
nels with CAN output on X-devices.

Specifically, this feature impacts the sample rate of devices and channels. If you configure one
channel for aliasing-free measurement, it restricts the available sample rates on certain
devices.

For M-Modules, which only support one sample rate per device, this limitation applies uni-
versally. As a result, even channels not configured for aliasing-free measurement will also face
restricted sample rate options.

IPETRONIK X-PLUGIN - USER MANUAL | ©IPETRONIK 2025. ALL RIGHTS RESERVED. | VERSION V02.23.00 | JULY 2025

262


