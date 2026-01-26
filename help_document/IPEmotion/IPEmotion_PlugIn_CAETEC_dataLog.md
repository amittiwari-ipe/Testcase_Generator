Manual

IPEmotion PlugIn
CAETEC dataLog

V22.10.00
Date of issue: December 6, 2022

© Copyright 2007 - 2022 by:

IPEtronik GmbH & Co. KG
Niederlassung Bergkirchen
Kreuzackerstrasse 4a
85232 Bergkirchen
Germany

All rights reserved. Any reprinting, photocopying or translation of this manual, in whole or
in part, requires advance written approval of IPEtronik.

Pictures and sketches are for illustration purposes only and are not to be used as design
drawings nor to serve as offer or assembly drawings.

All specifications are based on the technical status of December 6, 2022. We reserve the
right to make any changes required to technically improve the equipment.

This manual has been produced with all due diligence.

IPEtronik shall not be held liable for any damage resulting from the use of this manual,
providing it is not due to gross negligence on our own part or the part of our legal rep-
resentative or vicarious agent, and to the extent that the damage does not stem from
personal injury, bodily harm or damage to health.

All related registered brands and trademarks are the property of the respective owners.

Changesanderrorsexcepted.

1

CONTENTS

Contents

1 Foreword

2 Introduction

2.1
2.2

Symbols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

3 Product description

3.1

3.2

Installation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.1.1
System requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.1.2 Where to get the installation file? . . . . . . . . . . . . . . . . . . . . .
How to know the right version? . . . . . . . . . . . . . . . . . . . . . .
3.1.3
3.1.4
Installation on Windows . . . . . . . . . . . . . . . . . . . . . . . . . . .
User interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2.1 Menu bar
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
“File” menu and Settings for working with the PlugIn . . . . . . . . . .
3.2.2
3.2.3 Working with the Ribbon . . . . . . . . . . . . . . . . . . . . . . . . . .
“Signals” tab . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2.4
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2.5 Quick Access Toolbar
3.2.6 Message area . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

4 Setting up a logger system

4.1

4.2

Supported logger models

Sorting tree elements by channel numbers

4.2.2
4.2.3
4.2.4
4.2.5 Column chooser
4.2.6

Choosing a logger-system . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.1.1
. . . . . . . . . . . . . . . . . . . . . . . . .
The measurement task workspace . . . . . . . . . . . . . . . . . . . . . . . . .
The measurement task tree . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.1
4.2.1.1
. . . . . . . . .
The details area . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
The grid area . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Plugin version . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Filter editor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3 Changing the logger system with the changeinto-command . . . . . . . .
4.4 Open / Import / Export the datalog.ccmc and other PlugIn specific files . .
Exporting the datalog.ccmc . . . . . . . . . . . . . . . . . . . . . . . .
4.4.1
4.4.2
Ignore errors and warnings at export . . . . . . . . . . . . . . . . . . .
4.4.3 Opening the datalog.ccmc via the “Open” dialog . . . . . . . . . .
4.4.4 Opening the datalog.ccmc via commandline . . . . . . . . . . . . .
4.4.5 Opening sub configurations . . . . . . . . . . . . . . . . . . . . . . . .
Including sub configurations . . . . . . . . . . . . . . . . . . . . . . . .
4.4.6
4.5 Online communication with the logger . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.1 Communication settings
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.2 Online functions
Licence information . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.3
4.5.4
Licence check . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.5 Updating licences, firmware and web interface of the logger . . . .
. . . . . . . . . . . . . . . . . . .

4.6 Changing a system’s default tree elements

Changesanderrorsexcepted.

16

17
17
17

18
18
18
18
18
19
22
22
23
42
45
46
46

47
47
48
49
49
50
52
57
57
58
59
61
62
62
63
64
65
66
67
68
68
71
72
73
73
75

2

CONTENTS

4.8

4.7 Comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Adding a comment . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.7.1
Tree elements for Comments . . . . . . . . . . . . . . . . . . . . . . . .
4.7.2
4.7.3 Grid area for Comments
. . . . . . . . . . . . . . . . . . . . . . . . . .
4.7.4 Details area for Comments . . . . . . . . . . . . . . . . . . . . . . . . .
Sub configurations
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.8.1 Creating a sub configuration . . . . . . . . . . . . . . . . . . . . . . .
The *.isz and the *.cfginclude files . . . . . . . . . . . . . . . . . . . . .
4.8.2
The *.isz file . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.8.2.1
The *.cfginclude file . . . . . . . . . . . . . . . . . . . . . . .
4.8.2.2
4.8.3 Adding new tree elements to an existing sub configuration . . . . .
. . . . . . .
4.8.4 Unlinking tree elements from existing sub configurations
. . . . . . . . . . . . . . . . . . .
4.8.5
Encrypt/Decrypt sub configurations
4.8.5.1
Encrypting a sub configuration . . . . . . . . . . . . . . . . .
4.8.5.2 Decrypting a sub configuration . . . . . . . . . . . . . . . .
Transfer of private key for encryption (Create dlua for en-
4.8.5.3
cryption) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Subconfig options
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Use alias references for includes . . . . . . . . . . . . . . . .
4.8.6.1
Importing sub configurations . . . . . . . . . . . . . . . . . . . . . . . .

4.8.7

4.8.6

5 Project settings

5.1
5.2
5.3
5.4 Grid area for Project settings
5.5
5.6
5.7

Adding project parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Assigning a template of project parameters . . . . . . . . . . . . . . . . . . .
Tree elements for Project settings . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
Details area for Project settings . . . . . . . . . . . . . . . . . . . . . . . . . . .
Using project parameters as variables in CAETEC dataLog PlugIn . . . . . .
Using system parameters as variables in CAETEC dataLog PlugIn . . . . . .

77
77
77
78
78
79
83
84
84
84
84
85
85
86
87

87
89
90
91

92
92
93
94
94
95
96
97

6 UPS (Uninterruptible power supply)

98
98
Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1
99
Adding the UPS interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2
99
6.3 Configuring the UPS interface . . . . . . . . . . . . . . . . . . . . . . . . . . . .
99
6.3.1
Tree elements for the UPS interface . . . . . . . . . . . . . . . . . . . .
6.3.2 Details area for the UPS interface . . . . . . . . . . . . . . . . . . . . .
99
UPS signal properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
6.4.1 Grid area for UPS signals
. . . . . . . . . . . . . . . . . . . . . . . . . . 101
6.4.2 Overview of UPS signals . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
6.4.3 Details area for UPS signals . . . . . . . . . . . . . . . . . . . . . . . . . 102

6.4

7 Drivebay (Arcos 1.5 and ETHOS)

106
Adding the Drivebay interface . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
Tree elements for Drivebay . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
Details area for Drivebay . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107

8 Signal Acquisition

108
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
CAN/CAN FD channels
8.1.1
Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
8.1.2 Adding CAN/CAN FD channels . . . . . . . . . . . . . . . . . . . . . . 109
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
8.1.3 CAN settings

Changesanderrorsexcepted.

3

7.1
7.2
7.3

8.1

CONTENTS

8.1.4

8.1.6

8.2.1
8.2.2
8.2.3
8.2.4

Tree elements for CAN signals

Adding Bus statistics
Bus statistic signals

111
8.1.3.1 General
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
111
8.1.3.2 CAN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.1.3.3 CAN (for CAN FD)
. . . . . . . . . . . . . . . . . . . . . . . . 112
8.1.3.4 Wake On CAN . . . . . . . . . . . . . . . . . . . . . . . . . . 113
Hardware (Channel number) . . . . . . . . . . . . . . . . . . 119
8.1.3.5
8.1.3.6
Bus check . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
Virtual CAN settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
8.1.4.1 General
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
Hardware (Channel number) . . . . . . . . . . . . . . . . . . 121
8.1.4.2
8.1.5 CAN channel Bus statistic . . . . . . . . . . . . . . . . . . . . . . . . . . 122
. . . . . . . . . . . . . . . . . . . . . . . 122
8.1.5.1
. . . . . . . . . . . . . . . . . . . . . . . . 122
8.1.5.2
Exporting (XML) CANdb . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
8.2 CAN/CAN FD signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
Importing CAN signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
Import properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
Signal properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
. . . . . . . . . . . . . . . . . 130
8.2.4.1
8.2.4.2 Grid area for CAN signals . . . . . . . . . . . . . . . . . . . . 131
8.2.4.3 Details area for CAN signals . . . . . . . . . . . . . . . . . . . 131
8.2.5 Manual messages / Manual signals . . . . . . . . . . . . . . . . . . . . 137
Adding manual messages and signals . . . . . . . . . . . . 137
8.2.5.1
8.2.5.2
Tree elementes for manual messages . . . . . . . . . . . . . 138
8.2.5.3 Grid area for manual messages . . . . . . . . . . . . . . . . 139
8.2.5.4 Details area for manual messages (defining a manual signal)140
PDU signals (CAN FD and FlexRay) . . . . . . . . . . . . . . . . . . . . . . . . . 142
Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
8.3.1
Importing PDU signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
8.3.2
Import properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
8.3.3
Signal properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
8.3.4
8.3.4.1
Tree elements for PDU signals . . . . . . . . . . . . . . . . . . 147
. . . . . . . . . . . . . . . . . . . . 148
8.3.4.2 Grid area for PDU signals
8.3.4.3 Details area for PDU signals . . . . . . . . . . . . . . . . . . . 148
J1939 signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
8.4.1
Importing J1939 signals . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
8.4.2
Import properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
8.4.3
Signal properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
8.4.4
Tree elements for J1939 signals . . . . . . . . . . . . . . . . . 158
8.4.4.1
8.4.4.2 Grid area for J1939 signals
. . . . . . . . . . . . . . . . . . . 159
8.4.4.3 Details area for J1939 signals . . . . . . . . . . . . . . . . . . 159
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
Importing CCP/XCP signals . . . . . . . . . . . . . . . . . . . . . . . . . 160
Importing XCP signals on CAN FD . . . . . . . . . . . . . . . . . . . . . 163
Import properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
Signal properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
8.5.5.1
. . . . . . . . . . . . . . 171
8.5.5.2 Grid area for CCP/XCP signals . . . . . . . . . . . . . . . . . 174

Tree elements for CCP/XCP signals

8.5.1
8.5.2
8.5.3
8.5.4
8.5.5

8.5 CCP/XCP signals

8.3

8.4

Changesanderrorsexcepted.

4

CONTENTS

8.6

Tree elements for OBD signals

8.5.5.3 Details area for CCP/XCP signals

. . . . . . . . . . . . . . . 174
8.5.6 A2L to Cfginclude converter . . . . . . . . . . . . . . . . . . . . . . . . 184
8.5.6.1 Convert .a2l to .cfginclude . . . . . . . . . . . . . . . . . . . 184
8.5.6.2 Compare two .a2l files . . . . . . . . . . . . . . . . . . . . . . 186
8.5.6.3 Decompress .cfginclude . . . . . . . . . . . . . . . . . . . . 187
UDS signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
8.6.1
Importing UDS signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
8.6.2
Import properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
8.6.3
Signal properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
8.6.4
Tree elements for UDS signals . . . . . . . . . . . . . . . . . . 192
8.6.4.1
. . . . . . . . . . . . . . . . . . . . 193
8.6.4.2 Grid area for UDS signals
8.6.4.3 Details area for UDS signals . . . . . . . . . . . . . . . . . . . 193
8.7 OBD signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
8.7.1
8.7.2 Adding the OBD signals interface . . . . . . . . . . . . . . . . . . . . . 198
User-defined OBD signals . . . . . . . . . . . . . . . . . . . . . . . . . . 198
8.7.3
Signal properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
8.7.4
. . . . . . . . . . . . . . . . . 199
8.7.4.1
8.7.4.2 Grid area for OBD signals . . . . . . . . . . . . . . . . . . . . 199
Details area for OBD signals . . . . . . . . . . . . . . . . . . . 200
8.7.4.3
8.8 Gateways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
8.8.1 Adding a gateway . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
8.8.2 Adding an ID filter
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
8.8.3 Gateway settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
. . . . . . . . . . . . . . . . . . 208
8.8.3.1
8.8.3.2 Grid area for Gateways . . . . . . . . . . . . . . . . . . . . . 208
8.8.3.3 Details area for Gateways . . . . . . . . . . . . . . . . . . . . 208
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209
ID filter settings
8.8.4
Runstate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 210
8.9.1 Add Runstate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 210
8.9.2
Tree elements for Runstate . . . . . . . . . . . . . . . . . . . . . . . . . 211
8.9.3 Grid area for Runstate . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211
8.9.4 Details area for Runstate . . . . . . . . . . . . . . . . . . . . . . . . . . 212
8.9.5
Export Runstate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212
ETH channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213
8.10.1 Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213
8.10.2 Adding ETH channels
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 214
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215
8.10.3 ETH settings
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
8.10.3.1 General
8.10.3.2 Settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
8.10.3.3 LAN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217
8.10.3.4 DHCP server . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217
8.10.3.5 PTP (Precision time protocol) . . . . . . . . . . . . . . . . . . 218
8.10.3.6 Bus statistic PTP (Precision time protocol) . . . . . . . . . . . 219
8.10.4 ETH channel Bus statistic . . . . . . . . . . . . . . . . . . . . . . . . . . 221
. . . . . . . . . . . . . . . . . . . . . . . 221
. . . . . . . . . . . . . . . . . . . . . . . . 222

8.10.4.1 Adding Bus statistics
8.10.4.2 Bus statistic signals

Tree elements for Gateways

8.10

8.9

8.10.5 CAN FD satellite, FlexRay satellite and LIN satellite on ETH (ETH feature

interface)

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223

Changesanderrorsexcepted.

5

CONTENTS

8.11

8.11.2.1
8.11.2.2
8.11.2.3
8.11.2.4
8.11.2.5
8.11.2.6
8.11.2.7

ETH signals
8.11.1
8.11.2 Importing ETH signals

8.10.5.1 Adding the ETH Feature interface . . . . . . . . . . . . . . . 223
8.10.5.2 Adding a CAN FD/FlexRay/LIN satellite . . . . . . . . . . . . 224
8.10.5.3 Tree elements for a CAN FD satellite . . . . . . . . . . . . . . 225
8.10.5.4 Tree elements for a FlexRay satellite . . . . . . . . . . . . . . 226
8.10.5.5 Tree elements for a LIN satellite . . . . . . . . . . . . . . . . . 226
8.10.6 DLT (Diagnostic, Log and Trace) on ETH . . . . . . . . . . . . . . . . . 227
8.10.6.1 Adding a DLT-Station . . . . . . . . . . . . . . . . . . . . . . . 227
8.10.6.2 Tree elements for DLT . . . . . . . . . . . . . . . . . . . . . . . 227
8.10.6.3 Details area for DLT . . . . . . . . . . . . . . . . . . . . . . . . 228
8.10.7 VLAN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230
8.10.7.1 Adding a VLAN . . . . . . . . . . . . . . . . . . . . . . . . . . 230
8.10.7.2 Configuration of a VLAN . . . . . . . . . . . . . . . . . . . . 230
8.10.7.3 VLAN specific settings . . . . . . . . . . . . . . . . . . . . . . 231
8.10.7.4 Available components for VLAN . . . . . . . . . . . . . . . . 231
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232
Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 232
Importing Autosar files (UDP) . . . . . . . . . . . . . . . . . . 232
Import properties for UDP . . . . . . . . . . . . . . . . . . . . 234
Importing Fibex files (SOME/IP) . . . . . . . . . . . . . . . . . 235
Import properties for SOME/IP . . . . . . . . . . . . . . . . . 237
. . . . . . . . . . . . . . . . 238
Importing A2L files (XCPonUDP)
IP settings when Importing A2L files (XCPonUDP) . . . . . . 241
Import properties for XCPonUDP . . . . . . . . . . . . . . . . 241
8.11.3 Signal properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242
Signal properties for UDP . . . . . . . . . . . . . . . . . . . . 242
Signal properties for SOME/IP . . . . . . . . . . . . . . . . . . 242
Signal properties for XCPonUDP . . . . . . . . . . . . . . . . 243
8.12 DoIP - UDS signals over ETH . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244
8.12.1 IP settings for DoIP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244
PLP/TECMP devices (Automotive Ethernet) . . . . . . . . . . . . . . . . . . . . 245
8.13.1 Supported PLP/TECMP devices and features . . . . . . . . . . . . . . 245
8.13.2 Adding a PLP/TECMP device . . . . . . . . . . . . . . . . . . . . . . . . 245
8.13.3 IP settings for PLP/TECMP devices . . . . . . . . . . . . . . . . . . . . . 246
8.13.4 Custom PLP/TECMP devices . . . . . . . . . . . . . . . . . . . . . . . . 247
. . . . . . . . . . . . . . . . . . 248
8.13.5 Tree elements for PLP/TECMP devices
8.13.6 Grid area for PLP/TECMP devices . . . . . . . . . . . . . . . . . . . . . 248
8.13.7 PLP/TECMP interface functionality and limitations . . . . . . . . . . . 249
. . . . . . . . . . . . . . . . . . . 249
8.13.8 Details area for PLP/TECMP Devices
8.13.8.1 Details area for PLP/TECMP-CANFD . . . . . . . . . . . . . . 249
8.13.8.2 Details area for PLP/TECMP-ETH . . . . . . . . . . . . . . . . 252
8.13.8.3 Details area for PLP/TECMP-FlexRay . . . . . . . . . . . . . . 252
8.13.8.4 Details area for PLP/TECMP-LIN . . . . . . . . . . . . . . . . . 253
8.13.9 PLP/TECMPdevice bus statistic . . . . . . . . . . . . . . . . . . . . . . . 255
. . . . . . . . . . . . . . . . . . . . . . . 256
. . . . . . . . . . . . . . . . . . . . . . . . 256
LIN channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257
8.14.1 Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257
8.14.2 Adding LIN channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258
8.14.3 LIN settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258

8.13.9.1 Adding Bus statistics
8.13.9.2 Bus statistic signals

8.11.3.1
8.11.3.2
8.11.3.3

8.13

8.14

Changesanderrorsexcepted.

6

CONTENTS

8.16

8.15

Tree elements for LIN signals

8.16.4.1 Adding Bus statistics
8.16.4.2 Bus statistic signals

8.14.3.1 General
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259
8.14.3.2 LIN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260
8.14.3.3 Wake On LIN . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260
8.14.3.4 Hardware (Channel number) . . . . . . . . . . . . . . . . . . 261
8.14.3.5 Bus check . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262
8.14.4 LIN channel Bus statistic . . . . . . . . . . . . . . . . . . . . . . . . . . . 262
LIN signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
8.15.1 Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
8.15.2 Importing LIN signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
8.15.3 Import properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265
8.15.4 Signal properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266
. . . . . . . . . . . . . . . . . . 266
8.15.4.1
8.15.4.2 Grid area for LIN signals . . . . . . . . . . . . . . . . . . . . . 267
8.15.4.3 Details area for LIN signals . . . . . . . . . . . . . . . . . . . . 268
FlexRay channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273
8.16.1 Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273
8.16.2 Adding FlexRay channels . . . . . . . . . . . . . . . . . . . . . . . . . . 274
8.16.3 FlexRay settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275
8.16.3.1 General
8.16.3.2 Wake On FlexRay . . . . . . . . . . . . . . . . . . . . . . . . . 275
8.16.3.3 Hardware (Channel number) . . . . . . . . . . . . . . . . . . 276
8.16.3.4 Bus check . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277
8.16.4 FlexRay channel Bus statistic . . . . . . . . . . . . . . . . . . . . . . . . 277
. . . . . . . . . . . . . . . . . . . . . . . 277
. . . . . . . . . . . . . . . . . . . . . . . . 278
FlexRay signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279
8.17.1
Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279
8.17.2 Importing FlexRay signals . . . . . . . . . . . . . . . . . . . . . . . . . . 279
. . . . . . . . . . . . . . . 279
. . . . . . . . . . . . . 282
8.17.3 Import properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 284
8.17.4 Signal properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286
Tree elements for FlexRay signals . . . . . . . . . . . . . . . . 286
8.17.4.1
8.17.4.2 Grid area for FlexRay signals
. . . . . . . . . . . . . . . . . . 287
8.17.4.3 Details area for FlexRay signals . . . . . . . . . . . . . . . . . 287
8.18 GPS Signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293
8.18.1 Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293
8.18.2 Adding GPS Signals
8.18.2.1 CAETEC GPS module . . . . . . . . . . . . . . . . . . . . . . . 293
. . . . . . . . . . 294
8.18.2.2 Other GPS signals (Assigning GPS signals)
8.18.3 Signal properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295
Tree elements for GPS signals . . . . . . . . . . . . . . . . . . 295
8.18.3.1
. . . . . . . . . . . . . . . . . . . . 295
8.18.3.2 Grid area for GPS signals
8.18.3.3 Details area for GPS signals . . . . . . . . . . . . . . . . . . . 295
8.19 Video devices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300
8.19.1 Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300
8.19.2 Video Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300
8.19.2.1 Adding the Video Interface . . . . . . . . . . . . . . . . . . 301
8.19.2.2 Tree elements for the Video Interface . . . . . . . . . . . . 301
8.19.2.3 Grid area for the Video Interface . . . . . . . . . . . . . . . 302

Importing Autosar and Fibex files
Importing A2L files (XCP on FlexRay)

8.17.2.1
8.17.2.2

8.17

Changesanderrorsexcepted.

7

CONTENTS

Signals

8.19.2.4 Details area for the Video Interface . . . . . . . . . . . . . . 303
8.19.3 USB camera . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 305
8.19.3.1 Adding a USB camera . . . . . . . . . . . . . . . . . . . . . . 305
8.19.3.2 Tree elements for USB camera . . . . . . . . . . . . . . . . . 306
8.19.3.3 Grid area for USB camera . . . . . . . . . . . . . . . . . . . . 306
8.19.3.4 Details area for USB camera . . . . . . . . . . . . . . . . . . 306
8.19.4 Ethernet camera . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 309
8.19.4.1 Adding an ETH camera . . . . . . . . . . . . . . . . . . . . . 309
8.19.4.2 Tree elements for ETH camera . . . . . . . . . . . . . . . . . 312
8.19.4.3 Grid area for ETH camera . . . . . . . . . . . . . . . . . . . . 312
8.19.4.4 Details area for ETH camera . . . . . . . . . . . . . . . . . . 312
8.20 Video signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315
8.20.1 Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315
. . . . . . . . . . . . . . . . . . . . . . . . . . 315
8.20.2 Settings for video signals
8.21 Audio recording . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 319
8.21.1 Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 319
8.21.2 Adding an Audio recording . . . . . . . . . . . . . . . . . . . . . . . . 319
8.21.3 Tree elements for Audio recordings . . . . . . . . . . . . . . . . . . . . 320
8.21.3.1 Grid area for Audio recordings . . . . . . . . . . . . . . . . . 321
8.21.4 Details area for Audio recording . . . . . . . . . . . . . . . . . . . . . . 322
8.21.5 Microphone settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325
8.21.5.1
8.21.5.2 LEDs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325
8.21.5.3 Buttons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 326
8.22 DIN (Digital input signals) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 328
8.22.1 Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 328
8.22.2 Adding the DIN-Interface . . . . . . . . . . . . . . . . . . . . . . . . . . 328
8.22.3 Signal properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 330
8.22.3.1 Tree elements for DIN signals . . . . . . . . . . . . . . . . . . 330
8.22.3.2 Grid area for DIN signals . . . . . . . . . . . . . . . . . . . . . 330
. . . . . . . . . . . . . . . . . . . 330
8.22.3.3 Details area for DIN signals
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 335
8.23.1 Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 335
8.23.2 Adding the DOUT-Interface . . . . . . . . . . . . . . . . . . . . . . . . 335
8.23.3 Signal properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 336
8.23.3.1 Tree elements for DOUT signals . . . . . . . . . . . . . . . . . 336
8.23.3.2 Grid area for DOUT signals
. . . . . . . . . . . . . . . . . . . 337
8.23.3.3 Details area for DOUT signals . . . . . . . . . . . . . . . . . . 337
8.24 Analog signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 341
8.24.1 Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 341
8.24.2 Adding the Analog Interface . . . . . . . . . . . . . . . . . . . . . . . 342
8.24.3 Signal properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 345
8.24.3.1 Tree elements for Analog signals . . . . . . . . . . . . . . . . 345
8.24.3.2 Grid area for Analog signals
. . . . . . . . . . . . . . . . . . 345
8.24.3.3 Details area for Analog signals (Voltage) . . . . . . . . . . . 345
8.24.3.4 Details area for Analog signals (Counter/frequenzy) . . . . 349
8.24.3.5 Details area for Analog signals (Duty cycle) . . . . . . . . . 354
8.24.4 Analog signals on μCros SL . . . . . . . . . . . . . . . . . . . . . . . . . 358
8.25 Thermo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 361
8.25.1 Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 361

8.23 DOUT (Digital output signals)

Changesanderrorsexcepted.

8

CONTENTS

8.25.2 Adding the Thermo-Interface . . . . . . . . . . . . . . . . . . . . . . . 361
8.25.3 Signal properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 363
8.25.3.1 Tree elements for Thermo signals . . . . . . . . . . . . . . . . 363
8.25.3.2 Grid area for Thermo signals
. . . . . . . . . . . . . . . . . . 363
8.25.3.3 Details area for Thermo signals . . . . . . . . . . . . . . . . . 363
8.26 Internal signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 368
8.26.1 Storage method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 368
8.26.2 Accessing internal signals . . . . . . . . . . . . . . . . . . . . . . . . . . 369
8.26.3 Internal signals properties . . . . . . . . . . . . . . . . . . . . . . . . . . 370
8.26.3.1 Tree elements for Internal signals . . . . . . . . . . . . . . . . 370
8.26.3.2 Grid area for Internal signals
. . . . . . . . . . . . . . . . . . 370
8.26.3.3 Details area for Internal signals . . . . . . . . . . . . . . . . . 370
8.26.4 Run state . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 374
8.26.5 System info . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 376
8.26.5.1 System info specific settings . . . . . . . . . . . . . . . . . . . 377
8.26.6 Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 380
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 381
8.27.1 Formulas (Calculated signals) . . . . . . . . . . . . . . . . . . . . . . . 381
Storage method . . . . . . . . . . . . . . . . . . . . . . . . . 384
8.27.1.1
8.27.1.2 Adding a formula . . . . . . . . . . . . . . . . . . . . . . . . . 384
8.27.1.3 Grid area for formulas . . . . . . . . . . . . . . . . . . . . . . 384
8.27.1.4 Details area for formulas . . . . . . . . . . . . . . . . . . . . . 385
8.27.2 Script expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 392
8.27.2.1 Adding a Script expression . . . . . . . . . . . . . . . . . . . 392
. . . . . . . . . . . . . . . . . . . . . 393
8.27.2.2 Script expression editor
8.28 Synchronizing signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 397
. . . . . . . . . . . . . . . . . . 399
8.29 Transferring measurement tasks to the logger

8.27 Formulas

9 Alias signal group

399
9.1
Creating an Alias signal group . . . . . . . . . . . . . . . . . . . . . . . . . . . 400
9.2 Grid area for an Alias signal group . . . . . . . . . . . . . . . . . . . . . . . . . 401
Details area for signal aliases . . . . . . . . . . . . . . . . . . . . . . . . . . . . 402
9.3

10 Triggers

403
10.1 Adding a trigger . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 404
10.2 Tree elements for triggers
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 405
10.3 Grid area for Triggers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 406
10.4 Details area for Triggers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 407
10.5 Standard Triggers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 408
10.6 Level Triggers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 410
10.7 Cyclic Triggers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 414
10.8 Trigger groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 416

11 Scripts

418
11.1 Adding the Scripts-Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . 418
11.2 Adding a script
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 419
Importing a script . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 419
11.3
Tree elements for Scripts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 420
11.4
. . . . . . . . . . . . . . . . . . . . 421
11.5 Grid area for Scripts (Composing a script)
Edit script code . . . . . . . . . . . . . . . . . . . . . . . . . . 422

11.5.0.1

Changesanderrorsexcepted.

9

CONTENTS

11.5.0.2 Prefabricated code blocks . . . . . . . . . . . . . . . . . . . 423
11.5.0.3 Syntax check . . . . . . . . . . . . . . . . . . . . . . . . . . . 424
11.5.0.4 Undo in scripts / Redo in scripts . . . . . . . . . . . . . . . . . 424
11.5.1 Triggers in Scripts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 425
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 425
11.5.2 Signals in Scripts
. . . . . . . . . . . . . . . . . . . . . 426
11.5.3 Methods in Scripts (deprecated)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 426
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 427

11.6 Details area for Scripts
Exporting a script
11.7

12 Includes

428
12.1 Adding the Includes-Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . 428
Tree elements for Includes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 429
12.2
12.3 Grid area for Includes
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 429
12.4 Details area for Includes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 429

13 External files

431
13.1 Automatically add external files
. . . . . . . . . . . . . . . . . . . . . . . . . . 431
13.2 Database extraction from external files . . . . . . . . . . . . . . . . . . . . . . 433
13.3 Adding the External files interface . . . . . . . . . . . . . . . . . . . . . . . . . 434
13.4 Adding an external file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 434
13.5
. . . . . . . . . . . . . . . . . . . . . . . . . . . 435
13.6 Grid area for External files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 435
13.7 Details area for External files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 436

Tree elements for External files

14 Surveillance

437
14.1 Displays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437
14.1.1 Adding a display . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 437
14.1.2 The “Displays” interface . . . . . . . . . . . . . . . . . . . . . . . . . . . 439
14.1.3 CAETEC Display-specific settings
. . . . . . . . . . . . . . . . . . . . . 440
14.1.4 openABK Display-specific settings . . . . . . . . . . . . . . . . . . . . . 441
14.1.5 General Display settings . . . . . . . . . . . . . . . . . . . . . . . . . . . 446
14.1.5.1
Tree elements for a Display . . . . . . . . . . . . . . . . . . . 446
14.1.5.2 Grid area for a Display . . . . . . . . . . . . . . . . . . . . . . 446
14.1.5.3 Details area for a Display . . . . . . . . . . . . . . . . . . . . 447
14.1.5.4
Signals for Display . . . . . . . . . . . . . . . . . . . . . . . . . 448
14.1.5.5 Buttons for Display . . . . . . . . . . . . . . . . . . . . . . . . 450
14.1.5.6 Messages for Display . . . . . . . . . . . . . . . . . . . . . . . 451
E-mails . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 453
14.2.1 Setting up the E-mails interface . . . . . . . . . . . . . . . . . . . . . . 453
14.2.1.1 Adding the E-mails interface . . . . . . . . . . . . . . . . . . 453
14.2.1.2 Configure SMTP . . . . . . . . . . . . . . . . . . . . . . . . . . 454
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 455
14.2.2.1 Creating a new e-mail . . . . . . . . . . . . . . . . . . . . . . 455
. . . . . . . . . . . . . . . . . . . . 455
14.2.2.2 Tree elements for E-mails
14.2.2.3 Grid area for E-mails . . . . . . . . . . . . . . . . . . . . . . . 456
14.2.2.4 Details area for E-mails (Composing) . . . . . . . . . . . . . 456
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 458
14.2.3.1 Signal attachments . . . . . . . . . . . . . . . . . . . . . . . . 458
. . . . . . . . . . . . . . . . . . . . . . 460
14.2.3.2 Datafile attachments
. . . . . . . . . . . . . . . . . . . . . . . 461
14.2.3.3 Logfile attachments

14.2.3 E-mail attachments

14.2.2 Composing e-mails

14.2

Changesanderrorsexcepted.

10

CONTENTS

14.3

14.2.3.4 Dataset attachments

14.3.3.1 Grid area for Log file messages
14.3.3.2 Details area for Log file messages (Composing)

. . . . . . . . . . . . . . . . . . . . . . 462
Log file messages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 464
14.3.1 Adding the Log file messages interface . . . . . . . . . . . . . . . . . 464
14.3.2 Create a new Log file messages interface . . . . . . . . . . . . . . . . 464
14.3.3 Composing Log file messages . . . . . . . . . . . . . . . . . . . . . . . 465
. . . . . . . . . . . . . . . . 465
. . . . . . 466
14.4 Monitoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 468
14.4.1 Tree elements for Monitoring . . . . . . . . . . . . . . . . . . . . . . . . 468
14.4.2 Booleans . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 469
14.4.2.1 Adding Booleans . . . . . . . . . . . . . . . . . . . . . . . . . 469
14.4.2.2 Grid area for Booleans . . . . . . . . . . . . . . . . . . . . . . 469
14.4.2.3 Details area for Booleans . . . . . . . . . . . . . . . . . . . . 470
14.4.3 Limit value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 474
14.4.3.1 Adding a limit value . . . . . . . . . . . . . . . . . . . . . . . 474
14.4.3.2 Grid area for Limit values
. . . . . . . . . . . . . . . . . . . . 474
14.4.3.3 Details area for Limit values . . . . . . . . . . . . . . . . . . . 475
14.4.4 Range . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 479
14.4.4.1 Adding a Range . . . . . . . . . . . . . . . . . . . . . . . . . 479
14.4.4.2 Grid area for Ranges . . . . . . . . . . . . . . . . . . . . . . . 479
. . . . . . . . . . . . . . . . . . . . . 480
14.4.4.3 Details area for Ranges
14.5 XCP slave . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 484
14.5.1 Adding XCP slave . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 484
14.5.2 Tree elements for XCP slave . . . . . . . . . . . . . . . . . . . . . . . . 484
14.5.3 Grid area for XCP slave . . . . . . . . . . . . . . . . . . . . . . . . . . . 484
14.5.4 Details area for XCP slave . . . . . . . . . . . . . . . . . . . . . . . . . . 485

15 Datasets

15.2 Ring buffer

487
15.1 Dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 487
15.1.1 Adding extra datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . 487
15.1.2 Tree elements for Datasets . . . . . . . . . . . . . . . . . . . . . . . . . 487
15.1.3 Details area for Datasets
. . . . . . . . . . . . . . . . . . . . . . . . . . 488
15.1.4 Setting up a dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 493
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 495
15.2.1 Adding a ring buffer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 495
. . . . . . . . . . . . . . . . . . . . . . . . . . . 495
15.2.2 Setting up a ring buffer
15.2.3 Tree elements for ring buffer
. . . . . . . . . . . . . . . . . . . . . . . . 496
15.2.4 Grid area for ring buffer . . . . . . . . . . . . . . . . . . . . . . . . . . . 496
15.2.5 Details area for Ring buffer . . . . . . . . . . . . . . . . . . . . . . . . . 496
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 499
. . . . . . . . . . . . . . . . . . . . . . . . 499
15.3.1 Adding project parameters
15.3.2 Assigning a template of project parameters
. . . . . . . . . . . . . . 500
15.3.3 Tree elements for Project settings . . . . . . . . . . . . . . . . . . . . . 500
15.3.4 Grid area for Project settings . . . . . . . . . . . . . . . . . . . . . . . . 501
. . . . . . . . . . . . . . . . . . . . . . 501
15.3.5 Details area for Project settings
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 503
15.4.1 Overview of available special settings . . . . . . . . . . . . . . . . . . 503
15.4.2 Adding Dataset special settings . . . . . . . . . . . . . . . . . . . . . . 503
15.4.3 Tree elements for Dataset special settings . . . . . . . . . . . . . . . . 504
. . . . . . . . . . . . . . . . . . 505
15.4.4 Grid area for Dataset special settings

15.4 Dataset special settings

15.3 Dataset Project settings

Changesanderrorsexcepted.

11

CONTENTS

15.4.5 Details area for Dataset special settings . . . . . . . . . . . . . . . . . 506
15.5 Includes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 507
15.5.1 Adding the Includes-Interface . . . . . . . . . . . . . . . . . . . . . . . 507
15.5.2 Tree elements for Includes
. . . . . . . . . . . . . . . . . . . . . . . . . 507
15.5.3 Grid area for Includes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 508
. . . . . . . . . . . . . . . . . . . . . . . . . . 508
15.5.4 Details area for Includes
15.6 Dataset Network Destinations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 509
15.6.1 Setting up Network Destinations . . . . . . . . . . . . . . . . . . . . . . 509
. . . . . . . . . . . . . . . . . 510
15.6.2 Tree elements for Network Destinations
15.6.3 Grid area for Network Destinations . . . . . . . . . . . . . . . . . . . . 510
15.6.4 Details area for Network Destinations . . . . . . . . . . . . . . . . . . . 511
15.7 ATFX . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 512
15.7.1 Tree elements for ATFX . . . . . . . . . . . . . . . . . . . . . . . . . . . . 512
15.7.2 Grid area for ATFX . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 512
15.7.3 Details area for ATFX . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 513
15.7.3.1 ATFX file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 513
15.7.3.2 ATFX Timelog . . . . . . . . . . . . . . . . . . . . . . . . . . . . 516
15.7.3.3 ATFX Signal Group . . . . . . . . . . . . . . . . . . . . . . . . 519
15.7.4 Working with Signal Groups for ATFX . . . . . . . . . . . . . . . . . . . 521
15.7.4.1 Assigning signals to Signal Groups . . . . . . . . . . . . . . . 521
15.7.4.2 Cross reference, Storage group and Storage group refer-

ence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 522
15.7.5 Trigger groups for ATFX . . . . . . . . . . . . . . . . . . . . . . . . . . . 525
15.7.5.1 Adding a trigger group to timelog . . . . . . . . . . . . . . . 525
15.7.5.2 Assigning triggers to a group . . . . . . . . . . . . . . . . . . 526
. . . . . . . . . . . . . . . . . 526
15.7.5.3 Details area for trigger groups
15.8 MDF 4.0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 528
15.8.1 Multiple timelogs in MDF 4.0 . . . . . . . . . . . . . . . . . . . . . . . . 528
15.8.2 Bus trace in MDF 4.0/4.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . 529
15.8.3 Event writer in MDF 4.0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 530
15.8.4 Tree elements for MDF 4.0 . . . . . . . . . . . . . . . . . . . . . . . . . . 531
15.8.5 Grid area for MDF 4.0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 532
15.8.5.1 Signal Group . . . . . . . . . . . . . . . . . . . . . . . . . . . . 532
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 532
15.8.5.2 Event writer
15.8.6 Details area for MDF 4.0 . . . . . . . . . . . . . . . . . . . . . . . . . . . 533
15.8.6.1 MDF 4.0 File . . . . . . . . . . . . . . . . . . . . . . . . . . . . 533
15.8.6.2 MDF 4.0 Timelog . . . . . . . . . . . . . . . . . . . . . . . . . 535
15.8.6.3 MDF 4.0 Event writer
. . . . . . . . . . . . . . . . . . . . . . . 538
15.8.6.4 MDF 4.0 Signal Group . . . . . . . . . . . . . . . . . . . . . . 541
15.8.7 Working with Signal Groups for MDF 4.0 . . . . . . . . . . . . . . . . . 543
15.8.7.1 Assigning signals to Signal Groups . . . . . . . . . . . . . . . 543
15.8.7.2 Cross reference, Storage group and Storage group refer-

ence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 544
15.8.8 Trigger groups for MDF 4.0/4.1 . . . . . . . . . . . . . . . . . . . . . . . 545
15.8.8.1 Adding a trigger group to timelog . . . . . . . . . . . . . . . 545
15.8.8.2 Assigning triggers to a group . . . . . . . . . . . . . . . . . . 546
. . . . . . . . . . . . . . . . . 546
15.8.8.3 Details area for trigger groups
15.9 MDF 4.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 548
15.9.1 File compression in MDF 4.1 . . . . . . . . . . . . . . . . . . . . . . . . . 548
15.9.2 Header profiles in MDF 4.1 . . . . . . . . . . . . . . . . . . . . . . . . . 548

Changesanderrorsexcepted.

12

CONTENTS

15.9.2.1 Comments reference . . . . . . . . . . . . . . . . . . . . . . 549
15.9.2.2 Overview of header profiles and their differences . . . . . 549
15.9.3 Video attachments in MDF 4.1 . . . . . . . . . . . . . . . . . . . . . . . 551
15.9.3.1 Attaching a video . . . . . . . . . . . . . . . . . . . . . . . . 551
15.9.3.2 Details area for video in MDF 4.1 . . . . . . . . . . . . . . . . 552
15.10 Vector BLF / Vector ASCII / Vector ASCII compressed . . . . . . . . . . . . . 554
15.10.1 Tree elements for bus/trigger tracing . . . . . . . . . . . . . . . . . . . 554
15.10.2 Grid area for trigger tracing . . . . . . . . . . . . . . . . . . . . . . . . 556
15.10.3 Grid area for bus tracing . . . . . . . . . . . . . . . . . . . . . . . . . . 556
15.10.4 Details area for bus/trigger tracing . . . . . . . . . . . . . . . . . . . . 557
15.10.4.1 Bus tracing file . . . . . . . . . . . . . . . . . . . . . . . . . . . 557
15.10.4.2 Trigger trace . . . . . . . . . . . . . . . . . . . . . . . . . . . . 560
15.10.4.3 Bus trace . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 562
. . . . . . . . . . . . . . . . . . . . . 565
15.10.4.4 Traceable Bus channel
15.10.5 Bus trace ID Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 566
15.10.6 Details area for bus tracing (Ring buffer) . . . . . . . . . . . . . . . . . 568
15.10.6.1 Bus tracing file . . . . . . . . . . . . . . . . . . . . . . . . . . . 568
15.11 PCAP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 571
15.11.1 Tree elements for PCAP . . . . . . . . . . . . . . . . . . . . . . . . . . . 571
15.11.2 Grid area for PCAP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 572
15.11.3 Details area for PCAP . . . . . . . . . . . . . . . . . . . . . . . . . . . . 572
15.11.3.1 PCAP file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 572
15.11.3.2 Eth trace . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 576
15.11.4 Details area for PCAP (Ring buffer) . . . . . . . . . . . . . . . . . . . . 579
15.11.4.1 PCAP file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 579
15.11.4.2 ETH trace . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 582
. . . . . . . . . . . . . . . . . . . . . 583
15.11.4.3 Traceable ETH channel
15.12 AVI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 584
15.12.1 Including a video signal in the Video Stream . . . . . . . . . . . . . . 584
15.12.2 Tree elements for AVI
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 585
15.12.3 Grid area for AVI
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 586
15.12.4 Details area for AVI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 586
15.12.4.1 AVI File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 586
15.12.4.2 Video . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 590
15.12.4.3 Video Stream . . . . . . . . . . . . . . . . . . . . . . . . . . . 592
15.12.5 Details area for AVI (Ring buffer) . . . . . . . . . . . . . . . . . . . . . . 593
15.12.5.1 AVI File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 593
15.12.5.2 Video . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 596
15.12.5.3 Video Stream . . . . . . . . . . . . . . . . . . . . . . . . . . . 598
15.13 WAV . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 599
15.13.1 Including an audio signal in the audio Stream . . . . . . . . . . . . . 599
15.13.2 Tree elements for WAV . . . . . . . . . . . . . . . . . . . . . . . . . . . 600
15.13.3 Grid area for WAV . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 601
15.13.4 Details area for WAV . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 601
15.13.4.1 Wav selected . . . . . . . . . . . . . . . . . . . . . . . . . . . 601
15.13.4.2 Audio xx selected . . . . . . . . . . . . . . . . . . . . . . . . . 602
15.14 GPX . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 605
15.14.1 Assigning GPS signals
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 605
15.14.2 Tree elements for GPX . . . . . . . . . . . . . . . . . . . . . . . . . . . . 605
15.14.3 Grid area for GPX . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 606

Changesanderrorsexcepted.

13

CONTENTS

15.14.4 Details area for GPX . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 606
15.14.4.1 GPX File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 606
15.14.4.2 GPS Tracking . . . . . . . . . . . . . . . . . . . . . . . . . . . . 607
15.15 CAETEC binary (Classings / Min/Max Values) . . . . . . . . . . . . . . . . . . . 610
15.15.1 Tree elements for CAETEC binary . . . . . . . . . . . . . . . . . . . . . 610
15.15.2 Details area for CAETEC binary . . . . . . . . . . . . . . . . . . . . . . 611
15.15.3 Adding a classing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 612
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 613
15.15.4 Min/Max Values
. . . . . . . 613
15.15.4.1 Adding Min/Max Values and selecting signals
15.15.4.2 Tree elements for Min/Max Values . . . . . . . . . . . . . . . 615
15.15.4.3 Grid area for Min/Max Values
. . . . . . . . . . . . . . . . . 615
15.15.4.4 Details area for Min/Max Values . . . . . . . . . . . . . . . . 616
. . . . . . . . . . . . . . . . . . . 619
15.16 CAETEC ASCII (Classings / Min/Max Values)
. . . . . . . . . . . . . . . . . . . . . . 619
15.16.1 Tree elements for CAETEC ASCII
. . . . . . . . . . . . . . . . . . . . . . . 620
15.16.2 Details area for CAETEC ASCII
15.16.3 Adding a classing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 621
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 622
15.16.4 Min/Max Values
15.17 Classing methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 623
15.18 Script log . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 624
15.18.1 Including a Script log as a target in a script . . . . . . . . . . . . . . . 624
15.18.2 Tree elements for Script log . . . . . . . . . . . . . . . . . . . . . . . . . 626
15.18.3 Details area for Script log . . . . . . . . . . . . . . . . . . . . . . . . . . 626
15.19 J1939 DM1 Log . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 629
15.19.1 Tree elements for J1939 DM1 Log . . . . . . . . . . . . . . . . . . . . . 629
15.19.2 Grid area for J1939 DM1 Log . . . . . . . . . . . . . . . . . . . . . . . . 629
15.19.3 Details area for J1939 DM1 Log . . . . . . . . . . . . . . . . . . . . . . 630
15.19.3.1 J1939 DM1 Log xx file . . . . . . . . . . . . . . . . . . . . . . . 630
15.19.3.2 J1939-Stations component
. . . . . . . . . . . . . . . . . . . 633
15.19.3.3 Traceable J1939 station . . . . . . . . . . . . . . . . . . . . . 637
15.20 DLT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 638
15.20.1 Tree elements for DLT
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 638
15.20.2 Grid area for DLT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 639
15.20.3 Details area for DLT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 639
15.20.3.1 DLT file . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 639
15.20.3.2 DLT-Stations
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 643
15.20.3.3 DLT-Station xx . . . . . . . . . . . . . . . . . . . . . . . . . . . 645

16 Datatransfer

16.1

646
Transfer events . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 646
. . . . . . . . . . . . . . . 647
16.1.1 General Information about transfer events
16.1.2 Export order . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 648
16.1.3 Transfer priority . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 648
16.1.4 Trigger events . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 650
16.1.4.1
Tree elements for Trigger events . . . . . . . . . . . . . . . . 651
16.1.4.2 Grid area for Trigger events . . . . . . . . . . . . . . . . . . . 651
. . . . . . . . . . . . . . . . . 652
16.1.4.3 Details area for Trigger events
16.1.5 Time events . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 653
16.1.5.1
. . . . . . . . . . . . . . . . . 653
16.1.5.2 Grid area for Time events . . . . . . . . . . . . . . . . . . . . 654
16.1.5.3 Details area for Time events . . . . . . . . . . . . . . . . . . . 654

Tree elements for Time events

Changesanderrorsexcepted.

14

CONTENTS

16.2

16.3

16.3.2 Data transfer via WIFI

16.1.6 System events . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 655
Tree elements for System events . . . . . . . . . . . . . . . . 656
16.1.6.1
16.1.6.2 Grid area for System events . . . . . . . . . . . . . . . . . . . 656
16.1.6.3 Details area for System events . . . . . . . . . . . . . . . . . 656
Transfer event targets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 657
16.2.1 Tree elements for transfer event targets
. . . . . . . . . . . . . . . . . 657
16.2.2 Grid area for transfer event targets . . . . . . . . . . . . . . . . . . . . 658
16.2.3 Details area for transfer event targets . . . . . . . . . . . . . . . . . . . 659
16.2.3.1 Transfer event target settings . . . . . . . . . . . . . . . . . . 659
16.2.3.2 Transfer event target dataset selection . . . . . . . . . . . . 660
16.2.3.3 Transfer event target fileserver selection . . . . . . . . . . . 662
Transfer connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 663
16.3.1 Data transfer via USB . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 663
16.3.1.1 Details area for USB . . . . . . . . . . . . . . . . . . . . . . . . 663
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 665
16.3.2.1 Tree elements for WIFI connections . . . . . . . . . . . . . . 666
16.3.2.2 Grid area for WIFI connections . . . . . . . . . . . . . . . . . 666
. . . . . . . . . . . . . . . . . . . . . . . 667
16.3.2.3 Details area for WIFI
16.3.3 Data transfer via LAN . . . . . . . . . . . . . . . . . . . . . . . . . . . . 672
16.3.3.1 Tree elements for LAN connections . . . . . . . . . . . . . . 672
16.3.3.2 Details area for LAN . . . . . . . . . . . . . . . . . . . . . . . 672
16.3.4 Data transfer via PPP/UMTS . . . . . . . . . . . . . . . . . . . . . . . . . 674
16.3.4.1 Setting up a PPP/UMTS connection . . . . . . . . . . . . . . 674
16.3.4.2 Details area for PPP/UMTS . . . . . . . . . . . . . . . . . . . . 675
16.3.4.3 PPP status signals . . . . . . . . . . . . . . . . . . . . . . . . . 676
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 678
16.3.5.1 Tree elements for Wake on Call/Text
. . . . . . . . . . . . . 679
16.3.5.2 Grid area for Wake on Call/Text . . . . . . . . . . . . . . . . 679
16.3.5.3 Details area for Wake on Call/Text . . . . . . . . . . . . . . . 679
16.3.6 Setting up a Fileserver . . . . . . . . . . . . . . . . . . . . . . . . . . . . 681
16.3.6.1 Multiple File servers . . . . . . . . . . . . . . . . . . . . . . . . 682
16.3.6.2 Tree elements for File servers . . . . . . . . . . . . . . . . . . 682
16.3.6.3 Grid area for File servers . . . . . . . . . . . . . . . . . . . . . 683
. . . . . . . . . . . . . . . . . . . 683
16.3.6.4 Details area for File servers

16.3.5 Wake on Call/Text

17 SecOC Certificates

686
17.1 Adding SecOC certificates to the configuration . . . . . . . . . . . . . . . . . 686
17.1.1
Importing a SecOC certificate . . . . . . . . . . . . . . . . . . . . . . . 687
17.1.2 Adding a SecOC certificate . . . . . . . . . . . . . . . . . . . . . . . . 688
Tree elements for SecOC Certificates . . . . . . . . . . . . . . . . . . . . . . . 689
17.2
17.3 Grid area for SecOC Certificates . . . . . . . . . . . . . . . . . . . . . . . . . . 689
. . . . . . . . . . . . . . . . . . . . . . . . 690
17.4 Details area for SecOC Certificates

18 Setting up a time server

19 Obtaining extended support

Changesanderrorsexcepted.

692

694

15

1 FOREWORD

1 Foreword

Changesanderrorsexcepted.

16

2 INTRODUCTION

2 Introduction

2.1 Symbols

Various paragraphs in this manual are marked with special symbols. These symbols have
the following meanings:

This symbol highlights important information that, if ignored, may prevent
successful use of the program.

This symbol refers to additional information supplementing this manual.

2.2 References

References to other sections of this manual are generally placed in brackets and are in-
dicated by an arrow:
(→ 2.1) refers to Section 2.1.
When this manual is read in digital form, a mouse-click on such a reference accesses the
particular section of the book.

Changesanderrorsexcepted.

17

3 PRODUCTDESCRIPTION

3 Product description

3.1 Installation

3.1.1 System requirements

Minimum:
Screen resolution: 1080 x 800 pixel
Processor: 2 GHz
RAM: 2048 MB
DirectX 9

Recommended:
Screen resolution: 1920 x 1200 pixel
Processor: 3 GHz Multi-Core
RAM: 6144 MB
Storage medium type: SSD
DirectX 11

Supported platforms:
Microsoft Windows 10 (32 Bit and 64 Bit operating systems)
Microsoft Windows 8.1 (32 Bit and 64 Bit operating systems)
Microsoft Windows 8 (32 Bit and 64 Bit operating systems)
Microsoft Windows 7 (32 Bit and 64 Bit operating systems)

The following additional software is required:
Microsoft .NET 4.6.1 Framework

3.1.2 Where to get the installation file?

The installation file can be downloaded from https://myipe.ipetronik.com/ or here https:
//www.ipetronik.com/software/plugins. Once you have logged in with your username
and password you will be able to locate the file in the section UP- & DOWNLOADS.

3.1.3 How to know the right version?

The format of the Plugin version is always Vxx.xx.xx (e.g. V15.10.00) and has to match the
target system’s dataLog firmware-version. To find out which firmware-version your target
system is running you can either use the the data logger’s web interface or open with a
text editor the logger’s logfile and look for the firmware version there. For further informa-
tion please also refer to your data logger’s documentation.

Multiple Plugin versions of the CAETEC Plugin for IPEmotion can be in-
stalled at the same time. This allows you to work with various data loggers
that are running on different firmware versions. Once you have multiple
Plugin versions installed, you will always have to ensure that your currently
used Plugin version and target system’s firmware version match. Please
refer to Switching between Plugin versions (→ 3.2.2).

Changesanderrorsexcepted.

18

3.1 INSTALLATION

3.1.4 Installation on Windows

Navigate to your download directory and extract the downloaded zip-file. For 32-bit ver-
sions of Microsoft Windows choose the following file for installation.

For 64-bit versions of Microsoft Windows choose the following file for installation.

You may be asked to confirm execution of the program. If so, please confirm and type in
your Windows user password if asked to do so.
In the next window you may choose the language in which you wish to install the plugin.
The language can be changed later on (→ 3.2.2).

Changesanderrorsexcepted.

19

3.1 INSTALLATION

The next window presents the terms of the licence agreement. Check the box I accept
the terms of the licence agreement and proceed to the next window by clicking next.

In the next window you select the target folder where the plugin is to be installed. The
standard installation path is set as default. Normally you can simply accept it. Click Install
to continue and start the installation process. Again you may be asked for confirmation
and/or your Windows user or admin password. Please type it in and click OK to continue.

Once installation has been comleted successfully you will need to acitvate the Plugin in
the Options dialogue in order start working with it. To do so please refer to the section
Activating the plugin (→3.2.2).

Changesanderrorsexcepted.

20

3.1 INSTALLATION

After completion of the installation we strongly advice you to acitvate
the expert mode and afterwards activate the extended tabs option and
change the number of maximum polling lists in the expert settings. For
detailed information refer to the sections Expert mode, Extended tabs
and Maximum polling lists (→ 3.2.2).

The plugin allows for a customizable user guidance by giving you the
option to choose which tree elements you would like to be available in
the measurement task tree. For detailed information refer to the section
Customizing tree elements (→ 3.2.2).

Changesanderrorsexcepted.

21

3.2 USERINTERFACE

3.2 User interface

This section describes the general appearance and funcionality of the CAETEC Plugin for
IPEmotion. However it will not describe specifics on how to create a measurement task or
on the single elements available to configure your data logger. For information on these
topics please refer to Chapter (→ 8).

3.2.1 Menu bar

The menu bar provides the core funcionality of IPEmotion. However when working with
the CAETEC Plugin you will only need to make use of the “File” menu and the “Signals” tab,
as the Plugin offers a closed working environment which includes all funcionality needed
in order to work with your data logger inside the “Signals”-tab.

Changesanderrorsexcepted.

22

3.2 USERINTERFACE

3.2.2 “File” menu and Settings for working with the PlugIn

A dropdown menu with basic IPEmotion funcionality. Only the item relevant for working
with the CAETEC Plugin for IPEmotion will be explained here. For information on items not
explained here, please refer to the IPEmotion documentation.

New
Creates a new configuration/project.

Open
Opens a previosly saved configuration/project. You can open a range of different file-
types. The IPEmotion configuration file (*.iwf) is a container holding the entire IPEmotion-
Project and its settings. The IPEmotion acquisition configuration file (*.iac) holds only the
configuration contained in the “Signals” tab.

The *.isf-filetype and *.ccmc-filetype can only be opened when working
inside the Signals tab of IPEmotion.

Save
Saves the current configuration/project.

Save as

Changesanderrorsexcepted.

23

3.2 USERINTERFACE

Save the current configuration/project under a new name and/or in a new location. You
can choose between two different file-types to save your projects, which will determine
the information your saved file will hold. The IPEmotion configuration file (*.iwf) is a con-
tainer holding the entire IPEmotion-Project and its settings. The IPEmotion acquisition con-
figuration file (*.iac) holds only the configuration contained in the “Signals” tab.

Options
Opens a window with options that affect the behaviour of IPEmotion. This manual will only
address the options important for working with the CAETEC Plugin for IPEmotion.

• Change language

The language can be changed in the options window by choosing the tab “Ap-
pearance” on the left and then choosing the desired language from the dropdown
menu “Language selection” on the right.

Changesanderrorsexcepted.

24

3.2 USERINTERFACE

• Change language

If this setting is activated, elements will be grouped under their interface type in the
measurement task tree. We highly recommend activating this setting.

• Expert mode

The Expert mode can be activated in the options window by choosing the tab “Ba-
sic settings” on the left and then checking the checkbox for Expert mode. Once
you activated the Expert mode, Expert settings will be accessible by clicking on the
button with the three dots next to the Expert mode checkbox.

Changesanderrorsexcepted.

25

3.2 USERINTERFACE

• Extended tabs

This Option should be activated. It will provide additional tabs in the Details area for
some elements of the Measurement task tree. Extended tabs can be activated by
checking the checkbox for Extended tabs in Expert settings.

• No value timeout

This option defines the default maximum time for no values to be replaced by the
last value for each signal. This setting can be individually adapted in each signals
“Signal” tab of the details area.

• Maximum polling lists

Defines the maximum number of polling lists. Multiple polling lists must be supported
by the connector. The value should be set to a maximum of 4 polling list. The maxi-
mum number of polling lists can be changed by choosing the desired number from
the Max. polling lists dropdown menu in Expert settings.

Changesanderrorsexcepted.

26

3.2 USERINTERFACE

• Edit protocol channel scaling

This option has to be activated in Expert settings in order for the scaling functionality
to be available for protocol channels as well.

• View protocols

Activating this expert setting will allow you to see not only the ECU in the “Measure-
ment task tree”, but also the associated daq lists and polling lists.

Changesanderrorsexcepted.

27

3.2 USERINTERFACE

• Ignore verbal tables (VTAB)

In the documentation for earlier version of this PlugIn it was recommended, to acti-
vate this setting, as the PlugIn did not support verbal tables.

From V17.10.00 on the Plugin does now support verbal tables for single values/integers,
so it is recommended to deactivate the “Ignore verbal tables” setting.
However, verbal table ranges are still not supported by this PlugIn and will be trans-
formed to a factor/offset scaling at export.

• Activating the Plugin

In order to work with the CAETEC Plugin you need to activate it inside IPEmotion. To
do so, choose PluIns on the left side of the Options window and then tick the check-
box saying Active for the CAETEC dataLog Plugin.

Changesanderrorsexcepted.

28

3.2 USERINTERFACE

• Switching between Plugin versions

The CAETEC Plugin allows for various versions of the plugin in to be installed at the
same time.
It offers you the option to switch between different Plugin versions ac-
cording to the firmware version your dataLog system is running, and therefore allows
the use of various dataLog systems with different firmware versions.
In order to switch between Plugin versions choose PluIns on the left side of the Op-
tions window and then you can choose the desired version in the yellow marked
dropdown menu on the right.

• Customizing tree elements

The CAETEC Plugin for IPEmotion allows for a customizable user guidance by letting
you specifically determine which elements of the Measurement task tree will be avail-
able or not. In order to do so, choose PlugIns on the left side of the Options window
and then press the small button with the blue wrench symbol to open the Plugin-
specific settings.

Changesanderrorsexcepted.

29

3.2 USERINTERFACE

By choosing an element in the “Components” tab of the following window and set-
ting its priority to “Not used”, as shown below, this element will not be available for
the respective Plugin version anymore. If you would like to make available an ele-
ment which you have previously set to “Not used” then you just have to set its priority
back to “Normal”.

• Create and synchonize external files

It is possible to set up the CAETEC dataLog PlugIn in such a way, that imported sig-
nal databases will automatically be added as external file to their respective signal
channel. This option is described in detail in the chapter “External files”. Please refer
to (→13.1).

Changesanderrorsexcepted.

30

3.2 USERINTERFACE

• Extended FlexRay namespaces

The CAETEC Plugin for IPEmotion provides the option to work with an extended FlexRay
namespace, including base cycle and cycle repetition parameters of signals in the
namespace. This may be useful, if the regular FlexRay namespace creates ambigu-
ous names. In order to do so, choose PlugIns on the left side of the Options window
and then press the small button with the blue wrench symbol to open the Plugin-
specific settings.

In the following window activate the option by marking active the “Extended FlexRay
namespace” tickbox in the “General” tab.

Changesanderrorsexcepted.

31

3.2 USERINTERFACE

• Extended connector namespaces

The CAETEC Plugin for IPEmotion provides the option to work with an extended con-
nector namespace, including the respective connector in namespaces. This may
be useful, if the regular namespace creates ambiguous names.
In order to do so,
choose PlugIns on the left side of the Options window and then press the small but-
ton with the blue wrench symbol to open the Plugin-specific settings.

In the following window activate the option by marking active the “Extended con-
nector namespace” tickbox in the “General” tab.

This is an example of an extended connector namespace, starting with the signal’s
respective connector.

Changesanderrorsexcepted.

32

3.2 USERINTERFACE

• Use namespace

The CAETEC Plugin for IPEmotion provides the option to disable namespaces. By de-
fault the setting “Use namespace” is activated, which means, that namespaces will
be used in your configuration and signalnames or other names must only be unique
within their respective namespaces.
If the setting “Use namespace” is deactivated, no namespaces will be used in your
configuration and all signalnames and other names need to be unique within the
entire configuration.

In order to change this setting, choose PlugIns on the left side of the Options window
and then press the small button with the blue wrench symbol to open the Plugin-
specific settings.

In the following you may activate/deactivate the setting “Use namespace” in the
“General” tab.

Changesanderrorsexcepted.

33

3.2 USERINTERFACE

• Derive timeout from samplerate

The setting “Derive timeout from samplerate” allows you to set the timeout of a sig-
nal (meaning the time a signal can be without value before being considered a
noValue) to a multiple of the signal’s sample rate.

In order to change this setting, choose PlugIns on the left side of the Options window
and then press the small button with the blue wrench symbol to open the Plugin-
specific settings.

In the following you may activate setting “Derive timeout from samplerate” and set
the multiplier to be applied to the sample rate for this function.

Changesanderrorsexcepted.

34

3.2 USERINTERFACE

• Preferred files

The setting “Preferred files” allows you to specify for external and display configura-
tion files, that have previously been imported as part of a CCMC/CCMI, whether at
repeated export of the CCMC/CCMI, the respective files should be included from
the file path, that is specified in the configuration or from the original CCMC/CCMI.

File type
Databases

Description

Display configura-
tion

• This setting refers to “External files” (→13).

If set to “From
include the file from
referenced directory”, the PlugIn will
the path specified in the configuration.
If no file can be
found there, the file from the original CCMC/CCMI will be
included.

• If set to “From CCMC/CCMI”, the PlugIn will include the file
that was originally contained in the CCMC/CCMI in the con-
figuration. If no file can be found there, the file from the path
specified in the configuration will be included.

• This setting refers to “Display configuration files” (EMBU-Chart
→14.1.4).
If set to “From referenced directory”, the PlugIn
will include the file from the path specified in the configura-
tion. If no file can be found there, the file from the original
CCMC/CCMI will be included.

• If set to “From CCMC/CCMI”, the PlugIn will include the file
that was originally contained in the CCMC/CCMI in the con-
figuration. If no file can be found there, the file from the path
specified in the configuration will be included.

Changesanderrorsexcepted.

35

3.2 USERINTERFACE

In order to change this setting, choose PlugIns on the left side of the Options window
and then press the small button with the blue wrench symbol to open the Plugin-
specific settings.

In the following you may set the settings as desired in the section “Preferred files”.

Changesanderrorsexcepted.

36

3.2 USERINTERFACE

• Delete old script export items

The setting “Delete old script export items” defines whether signals and/or triggers
which have been creted whithin a script will be deleted from the configuration upon
their (temporary) removal from the script.

This may be important as sometimes it is necessary to uncomment part of a script
temporarily. If the uncommented part contains a signal and/or trigger, they would
normally be deleted from the configuration and all the related data with them. In
order to prevent this you may deactivate this setting.

Uncommented or deleted signals/triggers will still be part of the configuration, they
wil just not produce any data anymore until they are reinstalled in the script again.

In order to change this setting, choose PlugIns on the left side of the Options window
and then press the small button with the blue wrench symbol to open the Plugin-
specific settings.

Changesanderrorsexcepted.

37

3.2 USERINTERFACE

In the following you may set the settings as desired in the section “Delete old script
export items”.

• DataLog decides decimal places

The setting “DataLog decides decimal places” defines whether IPEmotion or Dat-
aLog controls the handling of decimal places for signals, whenever the “decimal
places” value is set to “Automatic” in a signal’s details area.
If the “Decimal places” value is set to any other than “Automatic” in a signal’s de-
tails area, the “DataLog decides decimal places” setting will not be applied to the
respective signal.

In order to change this setting, choose PlugIns on the left side of the Options window
and then press the small button with the blue wrench symbol to open the Plugin-
specific settings.

Changesanderrorsexcepted.

38

3.2 USERINTERFACE

In the following you may set the settings as desired in the section “DataLog decides
decimal places”.

Changesanderrorsexcepted.

39

3.2 USERINTERFACE

• Export mode

The CAETEC Plugin for IPEmotion provides the option to change the export mode
and thus export configurations to a logger that might otherwise not be exported be-
cause they cause an error or warning.

The following table explains the three different export modes:

Export mode
Prevent export due to
warnings and/or errors

Prevent export due to er-
rors

Ignore all warnings and
errors

Explanation
Configurations that cause warnings and/or errors will
by default not be saved/exported/transferred to a log-
ger. They can be exported using the “Export DataLog
configuration (Ingore all warnings and errors)” function.
Configurations that cause errors will by default not be
saved/exported/transferred to a logger. They can be
exported using the “Export DataLog configuration (In-
gore all warnings and errors)” function.
Any warnings and/or errors that may occur at export
of a configuration will be ignored by default and the
configuration will be saved/exported/transferred to a
logger in any case.

In order to change this setting, choose PlugIns on the left side of the Options window
and then press the small button with the blue wrench symbol to open the Plugin-
specific settings.

Changesanderrorsexcepted.

40

3.2 USERINTERFACE

In the following you may choose the export mode in the dropdown menu in the
“General” tab.

• Communication settings

In order for online communication via Ethernet between The CAETEC Plugin for IPEmo-
tion and a PC to work, it may be necessary to specify some communication settings.
For instructions on how to do so, please refer to (→4.5).

Changesanderrorsexcepted.

41

3.2 USERINTERFACE

3.2.3 Working with the Ribbon

This area contains general functions regarding your configuration.

The “Ribbon’s” functionalities “Components”, “Functions”, “Import” and
“Export” are also accessible by rightclicking on the tree element to
which you would like to apply one of these options and then choosing
the respective option from the context menu.

System
A dropdown menu that lets you choose which data logger system you want to config-
ure. You can change the logger system into a different system at any given moment by
right-clicking on your current logger system in the measurement task tree and selecting
Change into.

Components
Offers a choice of additional components which are available for the element currently
selected in the measurement task tree. You add the desired component by clicking on
it. Each activated component will appear in the measurement task tree as a child el-
ement to your previously selected element. The same functionality is accessible through
right-clicking an element in the measurement task tree and then choosing Components.

Functions
Offers a choice of additional functions which are available for the element currently se-
lected in the measurement task tree. You activate the desired function by clicking on it.
The same functionality is accessible through right-clicking an element in the measurement
task tree and then choosing Functions.

Import
Offers a choice of import-options which are available for the element currently selected
in the measurement task tree. You choose the desired import-option by clicking on it. The
same functionality is accessible through right-clicking an element in the measurement
task tree and then choosing Import.

Changesanderrorsexcepted.

42

3.2 USERINTERFACE

Export
Offers a choice of export-options which are available for the element currently selected
in the measurement task tree. You choose the desired export-option by clicking on it. The
same functionality is accessible through right-clicking an element in the measurement
task tree and then choosing Export.

Check
Perform a check on your current configuration’s validity. The results will be automatically
presented in a pop-up window once the check has finished. In the pop-up window you
have the option of rerunning the check by clicking refresh and to export the results as a
csv-file or html-file. The check function will be automatically performed each time the
datalog.cfg is exported.

Adjust
This functionality is currently not supported by this plugin.

Detect
If a logger is connected to your PC, this function detects any connected logger and im-
ports the configuration currently in use on the logger. This gives you the possibility to modify
a pre-existing loggerconfiguration without the need of setting it up from scratch.

If there is no valid configuration in use on the connected logger, the plugin will detect
all the available interfaces of the logger and adjust the measurement task tree elements
accordingly.

If a logger is configured with a user-specific IP or protected with user
name and password, it may be necessary, to edit the communication
settings of the plugin first. Instruction on these settings can be found here
(→3.2.2).

Initialize
If a logger is connected to your PC, this function exports the configuration currently in use
in IPEmotion to the logger. During export the configuration will be checked for validity
and give notice if any errors occurr.

If a logger is configured with a user-specific IP or protected with user
name and password, it may be necessary, to edit the communication
settings of the plugin first. Instruction on these settings can be found here
(→3.2.2).

Changesanderrorsexcepted.

43

3.2 USERINTERFACE

Reset
If a logger is connected to your PC, this function deploys a basic configuration compati-
ble with your logger model to the logger.

If a logger is configured with a user-specific IP or protected with user
name and password, it may be necessary, to edit the communication
settings of the plugin first. Instruction on these settings can be found here
(→3.2.2).

Display
This functionality is currently not supported by this plugin.

Details
Allows you to hide/show the details area of your current configuration.

Changesanderrorsexcepted.

44

3.2 USERINTERFACE

3.2.4 “Signals” tab

The “Signals” tab, which is located in the menu bar (→ 3.2.1), contains your main workspace
when working with the CAETEC Plugin for IPEmotion.
It is divided in various areas which
allow you to create measurement tasks and configure your data logger.

Ribbon
A strip of icons that can be clicked for quick access to certain functions and tools.
(→ 3.2.3)
Measurement task tree
The measurement task tree shows a hierarchical view of the individual configuration
sections for the opened measurement task. Specific information on working with
the measurement task tree will be given in chapter (→ 4.2.1).
Details area
This area contains, for the selected section of the measurement task tree, a field
and/or tabs that allows you to set the parameter settings for your selected section.
Specific information on working with the Details area will be given in chapter (→
4.2.2).
Grid area
This area contains, for the selected section of the measurement task tree and its
child elements, a grid which shows an overview of available measurement chan-
nels. Specific information on working with the grid area will be given in chapter
(→ 4.2.3).
Message area
This area contains messages about errors, warnings and information of the current
configuration of the measurement task (→ 3.2.6).

Changesanderrorsexcepted.

45

3.2 USERINTERFACE

Plugin version
The current Plugin version in use is shown in a field located above the measurement
task tree. The format of the version is always Vxx.xx.xx and has to match the target
system’s dataLog firmware-version (→ 4.2.4).

3.2.5 Quick Access Toolbar

A customizable toolbar which allows you to quickly access your most frequently used tools.
For further information please refer to the IPEmotion documentation.

3.2.6 Message area

This area contains important messages, the status, potential conflicts and errors of the
current configuration of the system.

Changesanderrorsexcepted.

46

4 SETTINGUPALOGGERSYSTEM

4 Setting up a logger system

This section explains the workspace and the steps to set up the right logger system for
your project/configuration. It will also explain options to customize the use of your logger
system.

4.1 Choosing a logger-system

Once you have activated the Plugin (→3.2.2) choose the desired logger-system. Click the
System button on the top left in the ribbon and then select your desired system.
The system you choose should match your target system (e.g. if your hardware is an AR-
COS 1.5 then you should choose the ARCOS 1.5 as the system you wish to configure).

According to your hardware’s possible interfaces a preconfigured workspace will be opened
inside the Signals tab. This workspace will be explained in more detail in the following.

Changesanderrorsexcepted.

47

4.1 CHOOSINGALOGGER-SYSTEM

4.1.1 Supported logger models

Description
BigData data logger

Comment

Logger model
ETHOS (28CAN - 8 LIN - 2
FR - 8 ETH - 8 ADIO)
ARCOS 1.0
ARCOS 1.5
μCROS (4 CAN)
μCROS (8 CAN)

Modular data logger
Modular data logger
Compact data logger
Compact data logger

μCROS (4 CAN - 2 FR)

Compact data logger

μCROS XL (4 CAN - 2 FR -
1 ETH)
μCROS XL (4 CAN - 8 LIN
- 1 ETH)

Compact data logger

Compact data logger

The four additional CAN channels
of this logger model possess no
Wake On Can functionality.
The two additional FlexRay chan-
nels of this logger model possess no
Wake On FlexRay functionality.

Changesanderrorsexcepted.

48

4.2 THEMEASUREMENTTASKWORKSPACE

4.2 The measurement task workspace

The main parts of the measurement task workspace are the Measurement task tree (→
4.2.1), the details area (→ 4.2.2) and the grid area (→ 4.2.3). For information on other parts
please refer to (→ 3.2.4).

4.2.1 The measurement task tree

The measurement task tree shows a hierarchical view of the individual measurement task-
configuration pages of the Plugin. Clicking an item in the tree opens the corresponding
configuration pages in the details area and the grid area to the right of the tree, where
you can perform the desired settings.
Right-clicking an element in the measurement task trees opens a context menu showing
options for that element. Depending on the type of element, this context menu gives you
the option of adding additional child elements below the clicked element, for example,
or lets you remove or disable optional configuration elements.

Changesanderrorsexcepted.

49

4.2 THEMEASUREMENTTASKWORKSPACE

4.2.1.1 Sorting tree elements by channel numbers

The channels in the measurement task tree can be sorted according to their hardware
channel number. Other elements (non-channels) are not affected by this setting.
It is recommeded to activate the setting “Grouped by interface type” as described in the
“User interface” chapter of this manual (→3.2.2).

For detailed information regarding the “Column chooser” please refer to
the respective section of this manual (→4.2.5).

In order to sort the measurement task tree by channel number, right click on the title row of
the measurement task tree and in the resulting drop down menu select “Column chooser”.

Now drag the “Channel number” field into the title bar until the two arrows are visible and
drop it.

Changesanderrorsexcepted.

50

4.2 THEMEASUREMENTTASKWORKSPACE

You will now see a third column in the measurement task tree labeled “Channel number”,
which allows you to sort any channels according to their hardware channel number.

Channels will be sorted according to their hardware channel number,
that can be found in the “Hardware” tab of the details area of each
channel. The number in the “Name” field of the “General” tab does not
have any effect on sorting.

Changesanderrorsexcepted.

51

4.2 THEMEASUREMENTTASKWORKSPACE

4.2.2 The details area

The details area contains tabs which allow for additional settings for the selected tree ele-
ment. In this section we will quickly describe the Details settings available for your CAETEC
dataLog system, which you will see, once you clicked on your system on top of the mea-
surement task tree. More detailed settings for other tree elements will be handled in the
respective sections of this manual.

• General

This tab allows you to activate or deactivate the entire system by ticking/unticking
the checkbox, give a user specific name to your system if wished and add an addi-
tional description. The Reference field serves as the tree element’s unique identifier
inside the measurement task tree. It cannot be changed.

Changesanderrorsexcepted.

52

4.2 THEMEASUREMENTTASKWORKSPACE

• Identification

This tab allows for more specific Identification of your system. The Configuration name
serves as an identifier of your configuration for the user. This is the name of your sys-
tem that will be visible in the webinterface of your datalogger.
The Front number field allows you to enter a target system’s unique front number,
which will have the effect, that the created datalog.cfg will only work with that spe-
cific target system.

In the field “Configuration name” project parameters can be used as
variables. For more information please refer to (→5.6).

If a front number is entered, the configuration will exclusively function for
the logger with the corresponding front number. It will not work on any
other logger.

• System

This tab allows for system specific settings.

◦ Follow-up time

Defines how long the logger keeps measuring after the last wake-up condition
went away.

◦ Reserved disk space

Changesanderrorsexcepted.

53

4.2 THEMEASUREMENTTASKWORKSPACE

Determines the amount of disk space that is reserved for internal processing (e.g.
zip-compression).

◦ Shutdown delay

Sets how long the shutdown of the whole system will be delayed after having
ended current measuring. During this time a new measurement can be started
by a valid wake-up condition.

◦ Shutdown timeout

Determines the maximum allowed time for a shutdown of the system. If this time
is exceeded, a hard shutdown will be forced and all processes, including data-
transfers, will be cancelled.

◦ Stack trace core dump

This setting provides extended trouble-shooting functionality. If the regular stack
trace method is not sufficient for trouble shooting the activation of the “Stack
trace core dump” setting will store a complete image of the RAM at the event
of a system crash on the logger’s SSD. This image can then bu used for extended
trouble-shooting and error analysis.

The “Stack trace core dump” setting is disabled by default and should
only be used for explicit trouble-shooting cases. As it writes a complete
image of the RAM to the logger’s SSD, which, depending on the logger,
can occupy up to 20GB, this option can cause the logger’s SSD to fill up
quickly if used without caution.

• Wake on time

The “Wake on time” option allows you to set your logger to wake up on a specific
point of time. Whenever this point of time occurs the logger will wake up, if it is not
active already. I.e. if you set the mode to hourly at minute “0”, the logger will wake
up at every full hour. If you set it to hourly and minute “30”, the logger will wake up
alway at half past the full hour.

If in another case you would like the logger to wake up every monday at 8.30 in the
morning, the setting would be Mode: weekly, Minute: 30, Hour: 8, Day: Monday, as
seen in the figure below.

Changesanderrorsexcepted.

54

4.2 THEMEASUREMENTTASKWORKSPACE

• Signal check

The “Signal check” function allows to check, whether the logger receives a signal as
expected. If a signal is expected but the logger does not receive it, signal check (if
it is activated for this signal) will inform the user.
This tab allows you to define a set of global signal settings, which can then later be
applied to any signal. That way you can make sure, that all signals which are sup-
posed to be configured in the same way, will actually use the same settings.

The “Signal check” function allows to set one of three modes that define when the
logger shoud expect a signal: “Continuous”, “Start and stop trigger” and “Stop is
inverted start”.
It also allows to set the Start-trigger and the Stop-trigger and the timeout.

If any of these parameters gets changed, it will change also for any signal to which
is using the global signal check setttings.

In order to make these global settings available for use with signals, the tickbox “Use
global settings” needs to be marked active.

• Bus check

The “Bus check” function allows to check, whether the logger receives traffic on a
bus as expected. If traffic is expected on a bus but the logger does not receive it,
bus check (if it is activated for this bus) will inform the user.
This tab allows you to define a set of global bus check settings, which can then later
be used for bus check on CAN, CAN FD, FlexRay and LIN busses. That way you can
make sure, that all busses, that are supposed to use bus check, will use the same
settings, if the option “Use global settings” is activated for a bus.

The “Bus check” function allows to set one of three modes that define when the log-
ger shoud expect traffic: “Continuous”, “Start and stop trigger” and “Stop is inverted
start”.
It also allows to set the Start-trigger and the Stop-trigger and the timeout.

If any of these parameters gets changed, it will change also for any bus which is us-
ing the global bus check setttings.

Changesanderrorsexcepted.

55

4.2 THEMEASUREMENTTASKWORKSPACE

In order to make these global settings available for use with busses, the tickbox “Use
global settings” needs to be marked active.

Changesanderrorsexcepted.

56

4.2 THEMEASUREMENTTASKWORKSPACE

4.2.3 The grid area

The grid area shows all available signals of the selected tree element.
It also allows to
activate certain signals, to rename them and sort by the different column’s parameters.
The “column chooser” allows you to customize which columns will be shown in the grid
area. For more information on the “column chooser” please refer to (→4.2.5).

4.2.4 Plugin version

The current Plugin version in use is shown in a field located above the measurement task
tree. The format of the plugin version is always Vxx.xx.xx (Vmajor.minor.hotfix). The plugin
version has to match the target system’s dataLog firmware-version.

If you have multiple Plugin versions installed, you may switch between
versions. For detailed information please refer to Switching between Plu-
gin versions (→ 3.2.2).

Changesanderrorsexcepted.

57

4.2 THEMEASUREMENTTASKWORKSPACE

4.2.5 Column chooser

The “column chooser” allows you to customize which columns will be visible in the grid
area. You can customize your “grid area” in such a way, that every setting you can ad-
just in the “details area” for a given tree element can be made accessible through the
“grid area” of this tree element.

In order to access the “Column chooser” rightclick on any point of the column title bar
and choose “Column chooser” from the context menu.

The resulting window on the right called “Customization” will present you with a selection
of the available columns. In order to add an extra column, choose the one you would like
to add from the “Customaization” window and drag id to the column bar as shown above.

If you wish to remove a column just drag it to any point outside of the column title bar until
you see a big black cross and then release it.

Changesanderrorsexcepted.

58

4.2 THEMEASUREMENTTASKWORKSPACE

4.2.6 Filter editor

The “Filter editor” allows you to apply customized filter rules to your signals.
In order to access the “Filter editor” rightclick on any point of the column title bar and
choose “Filter editor” from the context menu.

Once the “Filter editor” has opened, click on the red “And” in the top left corner. The
resulting context menu allows you to choose the method of combining the different filter
conditions (And, Or, Not And, Not). It also allows you to add a condition (which can al-
ternatively be achieved by clicking the “+” sign right of the “And”) or add a new group
of filter conditions.

Changesanderrorsexcepted.

59

4.2 THEMEASUREMENTTASKWORKSPACE

Once you have added a filter condition, you will now need to specify this condition in
order to funciton properly. There are three fields you will need to set.

• The field on the left with blue letters defines to which column the filter will apply.

• The field in the middle with green letters sets a parameter for your filter condition.

• The field on the right with grey letters sets a value for the choosen parameter.

You can combine different filter conditions or groups of filter conditions to obtain the de-
sired filter result.
In the example shown above, the filter will select all CAN signals which
are not checked “Active”.

Changesanderrorsexcepted.

60

4.3 CHANGINGTHELOGGERSYSTEMWITHTHECHANGEINTO-COMMAND

4.3 Changing the logger system with the changeinto-command

A previously set up logger system can still be changed into another one of the same log-
gerfamily later. To do so, right-click on your system in the measurement task tree, navigate
to change into and choose the system you would like to change it to.

Interchangeability of logger systems

• ARCOS 1.0 ↔ ARCOS 1.5

• μCROS SL ↔ μCROS ↔ μCROS XL (FlexRay; LIN)

• μCROS XL (FlexRay) ↔ μCROS XL (LIN)

If you are trying to change into another logger system and one of your
currently used tree elements is not available in the system you are chang-
ing into, you will see a Warning-message in the Messages area (→3.2.6)
and this tree element will not be migrated.

Changesanderrorsexcepted.

61

4.4 OPEN/IMPORT/EXPORTTHEDATALOG.CCMCANDOTHERPLUGINSPECIFICFILES

4.4 Open / Import / Export the datalog.ccmc and other PlugIn specific

files

4.4.1 Exporting the datalog.ccmc

Once you have chosen the system you would like to configure, you will be able to export
the datalog.ccmc. That way you will be able to transfer your configuration to one or more
matching target systems, and also to reimport it into the plugin and edit it. To do so, just
select your system in the measurement task tree and then select either Export from the
Ribbon and choose datalog.ccmc. Alternatively you can right-click on your system in the
measurement task tree and select Export from the following context menu.

Preexisting configurations that have been imported into the plugin will
recommend a path and filename when being exported:

• Import via “File -> Open” and export via “File -> Save as”: The rec-
ommended path and filename correspond to the imported file’s
path and filename.

• Import via “File -> Open” and export via “Export -> Datalog configu-
ration”: The recommended filename corresponds to the imported
file’s filename, the recommended path is the standard IPEmotion
export path.

• Import via “System -> Import” and export via “Export -> Datalog
configuration”: The recommended filename corresponds to the
filename under which the current configuration was previously ex-
ported, the recommended path is the standard IPEmotion export
path.

The filename under which the exported .ccmc-file will be save cannot
contain any special characters such as “, §, ö and so forth. The spelling
of the filename will be checked during export and any special charac-
ter in the filename will be replaced with an underscore (”_“).

Changesanderrorsexcepted.

62

4.4 OPEN/IMPORT/EXPORTTHEDATALOG.CCMCANDOTHERPLUGINSPECIFICFILES

4.4.2 Ignore errors and warnings at export

The CAETEC Plugin for IPEmotion checks any configuration for errors and warnings before
exporting the ccmc-container or when using the “Check” function in the Ribbon.
If a
warning occurs, export will still happen, but the element causing the warning will not be
exported.
If an error occurs, the export will be canceled.

However, if you click “Export” in the Ribbon and then choose “Datalog configuration (ig-
nore warnings and errors)”, export will happen even if an error or warning occurs. The
error/warning will then appear as info-message instead and export will proceed.

Alternatively you can change the export mode in the Plugin settings so
that export ignore errors and warnings by default. For instructions on the
export mode please refer to this chapter (→3.2.2).

Changesanderrorsexcepted.

63

4.4 OPEN/IMPORT/EXPORTTHEDATALOG.CCMCANDOTHERPLUGINSPECIFICFILES

4.4.3 Opening the datalog.ccmc via the “Open” dialog

When within the “Signals” tab in IPEmotion, you can open an existing configuration via
the “Open” dialog. This will open the entire system inside the “Signals” tab.

To do so, open the “File” menu and then click “Open”.

In the next window it is important, that you first choose the “System file (*.isf, *.ccmc)” type
on the bottom right, before you select the *.ccmc file, you wish to import, and confirm with
“Open”. This will open the entire system and its configuration which can be modified from
here on.

Changesanderrorsexcepted.

64

4.4 OPEN/IMPORT/EXPORTTHEDATALOG.CCMCANDOTHERPLUGINSPECIFICFILES

4.4.4 Opening the datalog.ccmc via commandline

For automatition or working with third party programs it may be useful, to open the data-
log.ccmc from outside of IPEmotion. To do so, you may use the Windows command line
(cmd.exe).

Inside the commandline type in the command:

IPEmotion.exe

followed by the path of your *.ccmc file in double quotes.

An example for what your commandline prompt should look like:

IPEmotion.exe”D:\tmp\Logger-1.ccmc”

Changesanderrorsexcepted.

65

4.4 OPEN/IMPORT/EXPORTTHEDATALOG.CCMCANDOTHERPLUGINSPECIFICFILES

4.4.5 Opening sub configurations

When within the “Signals” tab in IPEmotion, you can open an existing sub configuration
via the “Open” dialog. This will open the entire sub configuration inside the “Signals” tab
and allows you to make changes to the sub configuration.

To do so, open the “File” menu and then click “Open”.

In the next window it is important, that you first choose the “Subconfiguration file (*.isz/*.ccmi)”
type on the bottom right, before you select the *.isz file, you wish to import, and confirm
with “Open”.

Changesanderrorsexcepted.

66

4.4 OPEN/IMPORT/EXPORTTHEDATALOG.CCMCANDOTHERPLUGINSPECIFICFILES

4.4.6 Including sub configurations

To include a sub configuration in an existing configuration you will need to use the “Sub-
configs” dialog.It is also possible to open a sub configuration via the “Sub-configs” dialog.

This will load the sub configuration into your configuration and place it into the measure-
ment task tree according to the “Use alias references for includes” setting of your con-
figuration. For details please refer to the section “Use alias references for includes” here
(→4.8.6.1).

To do so, open the “File” menu and then click “Sub-configs”.

In the next window click “Add sub-configs”, choose the desired *.isz/*.ccmi file and then
confirm with “Save”.

Changesanderrorsexcepted.

67

4.5 ONLINECOMMUNICATIONWITHTHELOGGER

4.5 Online communication with the logger

There are several functions that require online communication between the logger and
the pc via Ethernet. This section will explain how to set up the logger for online communi-
cation and also the different functions that require online communication.

4.5.1 Communication settings

In order for online communication via Ethernet between The CAETEC Plugin for IPEmotion
and a PC to work, it may be necessary to specify some communication settings. In order
to do so, choose PlugIns on the left side of the Options window and then press the small
button with the blue wrench symbol to open the Plugin-specific settings.

In the “Options” tabsheet of the following window you will find a field called “Communi-
cation”, containing all the relevant settings for online communication between a logger
and a PC.

Changesanderrorsexcepted.

68

4.5 ONLINECOMMUNICATIONWITHTHELOGGER

Use deprecated IP range
If activated, the secondary IP address will be used as primary IP address. This setting af-
fects the following configurations:

• Front channels, ETH channels and openABK channels on ARCOS 1.5

• Internal channels on ARCOS 1.0 and μcros

At the moment IPEmotion is not capable of displaying that the primary
and secondary IP address have been switched, when the function “Use
deprecated IP range” has been acitvated. Nevertheless, if the function
has been activated, secondary IP address will function as primary IP ad-
dress and this should be kept in mind.

Primary IP address
Primary IP address for communication with a logger. This IP address cannot be changed.

Secondary IP address
Secondary IP address for communication with a logger. This IP address cannot be changed.

Alternative IP address
If a logger is communicating on a user-specific IP address, type in this address here to en-
sure correct communication between the logger and the PC.

User name and Password
If a logger is protected via user name and password, type them in here to ensure correct
communication between the logger and the PC.

Changesanderrorsexcepted.

69

4.5 ONLINECOMMUNICATIONWITHTHELOGGER

Update logger on initialize
This section of the communication settings provides you with three settings that allow you
to automatically update one or more of the following when initializing the configuration:

• Firmware package: uploads a new firmware update package of the type *.dlua.

• WebIF package: uploads a new Web Inteface update package of the type *.dlua.

• Licence package: uploads a new licence update package of the type *.dlua.

The path and filename of the update package needs to be entered in the field next to
the tickbox of the setting, as seen in the picture above.

If any of these settings is activated and the logger is initialized with the PlugIn using either
the “Initialize” or “Reset” button in the Ribbon, the update will be installed on the logger
before transferring the configuration.

Changesanderrorsexcepted.

70

4.5 ONLINECOMMUNICATIONWITHTHELOGGER

4.5.2 Online functions

The online functions provided by the plugin can be found in the Ribbon and will be ex-
plained in the following.

Detect
If a logger is connected to your PC, this function detects any connected logger and im-
ports the configuration currently in use on the logger. This gives you the possibility to modify
a pre-existing loggerconfiguration without the need of setting it up from scratch.

If there is no valid configuration in use on the connected logger, the plugin will detect
all the available interfaces of the logger and adjust the measurement task tree elements
accordingly.

If a logger is configured with a user-specific IP or protected with user
name and password, it may be necessary, to edit the communication
settings of the plugin first. Instruction on these settings can be found here
(→4.5.1).

Initialize
If a logger is connected to your PC, this function exports the configuration currently in use
in IPEmotion to the logger. During export the configuration will be checked for validity
and give notice if any errors occurr.

If a logger is configured with a user-specific IP or protected with user
name and password, it may be necessary, to edit the communication
settings of the plugin first. Instruction on these settings can be found here
(→4.5.1).

Changesanderrorsexcepted.

71

4.5 ONLINECOMMUNICATIONWITHTHELOGGER

Reset
If a logger is connected to your PC, this function deploys a basic configuration compati-
ble with your logger model to the logger.

If a logger is configured with a user-specific IP or protected with user
name and password, it may be necessary, to edit the communication
settings of the plugin first. Instruction on these settings can be found here
(→4.5.1).

4.5.3 Licence information

If a logger is connected to the PC, it is possible for the plugin, to access that logger’s li-
cence information. Thus you can findout which licence keys are currently installed on your
logger and which are still needed for your current configuration to function properly.

To read the licence information out, select your system in the measurement task tree (the
topmost element), click the “Functions” button in the Ribbon and then choose “Licence
information”.

If a logger is configured with a user-specific IP or protected with user
name and password, it may be necessary, to edit the communication
settings of the plugin first. Instruction on these settings can be found here
(to3.2.2).

Changesanderrorsexcepted.

72

4.5 ONLINECOMMUNICATIONWITHTHELOGGER

4.5.4 Licence check

If a logger is connectet to the PC, it is possible for the plugin, to check whether all the
necessary licences for your current configuration are installed on the logger.

To perform a licence check, select your system in the measurement task tree (the topmost
element), click the “Functions” button in the Ribbon and then choose “Licence check”.

If a logger is configured with a user-specific IP or protected with user
name and password, it may be necessary, to edit the communication
settings of the plugin first. Instruction on these settings can be found here
(→3.2.2).

4.5.5 Updating licences, firmware and web interface of the logger

Updating licences, the logger’s firmware and web interface can be done via the “Func-
tions” button using the according *.dlua (datalog update archive) containers, containing
either the required licences, firmware or web interface installation packages.

To do so, select the logger in the measurement task tree, click the “Functions” button in
the Ribbon and then choose “Upload firmware/webinterface/licence”.

Changesanderrorsexcepted.

73

4.5 ONLINECOMMUNICATIONWITHTHELOGGER

In the following window choose the *.dlua file, which contains the licence/firmware/web
interface you wish to update. It is possible to select multiple files and thus update multiple
licences at the same time. Once you have selected all the update files you wish to give
to the logger, press “Open”.

You will now be prompted, whether you wish to restart the logger after successfully trans-
ferring the update packages. If you wish to give further update packages to the logger,
press “No” and repeat the above steps.

If you have given all the update packages to the logger, that you wish to apply, press
“Yes”. The logger will now upload the update packages and after having successfully
done so, will restart and install the update. After all the updates have been installed, the
logger will start again and is ready to use.

Changesanderrorsexcepted.

74

4.6 CHANGINGASYSTEM’SDEFAULTTREEELEMENTS

4.6 Changing a system’s default tree elements

The tree elements available by default for a given system are merely a preference, which
can be adjusted via the measurement task tree. If you see, that you usually use 8 instead
of 4 CAN busses, you can determine this setting as your default for the currently used
system type and the next time you set up a new logger system it will automatically start
with your new default settings. To do so, you will first need to add or remove the desired
components. (In this case we added another 4 CAN busses in order to get a total of 8).

Changesanderrorsexcepted.

75

4.6 CHANGINGASYSTEM’SDEFAULTTREEELEMENTS

In the next step you will have to right-click on the category of tree elements for which
you wish to define your new default settings as shown below. Note: it will not work, if you
right-click the single component or the system itself. Make sure to right-click the category,
in this case the CAN Interfaces and then choose Use as default.

Changesanderrorsexcepted.

76

4.7 COMMENTS

4.7 Comments

The “Comment” component allows you to add a comment to your logger system, which
will appear as a tree element and can be exported as part of the configuration. It is pos-
sible to add multiple “Comments” to a system.

4.7.1 Adding a comment

In order to add a “Comment” to your system, select the logger in the measurement task
tree, click the “Components” button in the Ribbon and then choose “Comment”.

4.7.2 Tree elements for Comments

Including a “Comment” in your configuration will add one new tree element. The tree
element is labeled “Comment xx”.

Changesanderrorsexcepted.

77

4.7 COMMENTS

4.7.3 Grid area for Comments

If the “Comment xx” element is selected in the Measurement task tree, the grid area will
provide you with a commentary editor, which allows you to type in your comments.
The Edit button allows to search and replace words.

4.7.4 Details area for Comments

If the “Comment xx” element has been selected in the measurement task tree, additional
settings are available in the details area.

General
This tab provides general settings for the selected “Comment xx”.

• Active

Activate/Deactivate the comment for export with the configuration.

• Name

Give a user-defined Name to the selected comment.

• Description

Give a user-defined description to the selected comment.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Changesanderrorsexcepted.

78

4.8 SUBCONFIGURATIONS

4.8 Sub configurations

Sub configurations allow you to set up a partial configuration and export it as a sub config-
uration, that can then be used as a module in other configurations. This can be especially
useful when handling large fleets of vehicle, loggers or different configurations.

Sub configurations can be created for the following tree elements:

• PPP

◦ Bus layer
◦ PPP status layer
◦ WakeOn PPP layer

• Databases (DBC, Autosar, A2l,etc.)

◦ ECU layer
◦ Protocol layer, when no ECU layer is available

• Bus statistics (on bus statistics layer of the respective connector)

◦ CAN
◦ CAN-FD
◦ LIN
◦ FlexRay
◦ ETH

• Video

◦ USB Video (on USB Video layer)
◦ Video interface (on camera layer)
◦ ETH video (on camera model layer)

• Audio

◦ CASM2T3L (on Gin CASM2T3L layer)
◦ Vocan (on Gin Vocan layer)
◦ openABK Display (on Microphone layer)

• Includes

• GPS

• UPS Status - on status layer

• Internal signals

◦ Run state layer
◦ System info layer
◦ Time layer

Changesanderrorsexcepted.

79

4.8 SUBCONFIGURATIONS

• Diagnostic, Log and Trace /DLT) - on “DLT-Station xx” layer

• Manual messages - on interface layer

• Formulas

• Monitoring

◦ Booleans
◦ Limit Values
◦ Ranges

• Trigger - each trigger individually

◦ Standard trigger
◦ Limit trigger
◦ Cyclic trigger
◦ Group trigger

• Scripts - each script individually

• Dataset - each dataset individually

• Ringbuffer - each ringbuffer individually

• ATFX

◦ ATFX xx layer
◦ Signal group layer

• MDF 4.0/4.1

◦ Timelog layer
◦ Bus trace layer
◦ Event writer layer
◦ Video Stream layer
◦ Signal group layer
◦ Trigger group layer

• Vector BLF/ASCII/ASCII compressed

• PCAP

• AVI

• WAV

• GPX

• CAETEC Binary

• CAETEC ASCII

• J1939 DM1 Log

• DLT

Changesanderrorsexcepted.

80

4.8 SUBCONFIGURATIONS

• Bus and ETH trace

◦ each ConnectorLink individually
◦ on Triggertrace layer

Regardless of whether the option “Use alias references for includes” is
activated in the plugin options (→4.8.6.1), subconfiguration for tracing
methods (Vector BLF/ASCII/ASCII compressed and PCAP) will always be
referenced using their alias.

• E-mails - each E-mail individually

• Log file messages - Each log file message individually

• Display - on Signals layer and on Messages layer

• Datatransfer - on Datatransfer layer

• SecOC Certificates - on SecOC Certificates interface layer

Subconfigurations for signals

It is also possible to create subconfigurations for certain grid elements. The follwoing list
shows you the grid elements for which a subconfiguration can be created, together with
their respective connector/parent elements in the measurement task tree.

• Methods

◦ Timelog

* on signal layer
* on trigger layer

◦ TriggerTrace

* on trigger layer

◦ Min/Max

* on signal layer

◦ Classings

* on signal layer

• Includes (Loggerincludes, not dataset includes)

◦ on signal layer

• Formulas

◦ on signal layer

• Monitoring

◦ Boolean

* on signal layer

Changesanderrorsexcepted.

81

4.8 SUBCONFIGURATIONS

◦ Limit Value

* on signal layer

◦ Range

* on signal layer

• Bus statistic for CAN/CAN FD, LIN, FlexRay and ETH

◦ Bus statistic

* on signal layer

• GPS

◦ on signal layer

• UPS status

◦ on signal layer

• Internal signals

◦ Run state

* on signal layer

◦ System

* on signal layer

◦ Time

* on signal layer

• PPP

◦ PPP status

* on signal layer

◦ WakeOn

* on signal layer

• Video

◦ USB Video

* on signal layer

◦ Videointerface

* on signal layer

◦ ETH Video

* on signal layer

Changesanderrorsexcepted.

82

4.8 SUBCONFIGURATIONS

4.8.1 Creating a sub configuration

In order to create a sub configuration, right click on the desired tree element (in this case
the “IPEmotionDemo” dbc on CAN 02) and select “Create sub-config”.

In the following window you may choose a filepath, where to save the sub configuration
and the filename. At creation of the sub configuration, one container file of the type
*.ccmi will be created. This *.ccmi file will contain two files with the same name but of a
different filetype, the *.isz file and the *.cfginclude file.

The tree element that has been converted into a sub configuration will be marked with
an arrow symbol.

A partial configuration, that has been converted into a sub configura-
tion, will no longer be automatically transferred to the logger at export,
although it will still be shown as a sub configuration in the measeurement
task tree. In order for any sub configuration to be transferred, the *.cfgin-
clude file, which has been created at creation of the sub configuration,
must be included via the “Includes” function. This will be explained in
the following.

Changesanderrorsexcepted.

83

4.8 SUBCONFIGURATIONS

4.8.2 The *.isz and the *.cfginclude files

As mentioned earlier, creating a sub configuration will result in a container *.ccmi file con-
taining two different files with the same name. The *.isz file and the *.cfginclude file. These
two files have different functions which will be explained here.

4.8.2.1 The *.isz file

The *.isz file ist the partial IPEmotion configuration, which you need in order to modify the
existing sub confiuration.
In order to modify the sub configuration, open the *.isz file in
IPEmotion, make the desired changes and save it. Once the *.isz file has been modified
and saved, the changes will be applied to the linked *.cfginclude file as well.

For instructions on how to open a sub configuration in IPEmotion please refer to (→4.4.5).

At the moment it is not possible to save an *.isz file, that has just been
modified, using the “Save as” function. Please use the “Save” function.

4.8.2.2 The *.cfginclude file

The *.cfginclude file, is the part of the sub configuration which will later be transferred to
the logger. It is a regular include file, as described in the chapter “Includes”.
This is also the part of your sub configuration which can be included in other configurations
using the includes function. That means if you have created a sub configuration and whish
to include this sub configuration in one of your configurations, you can either include the
*.cfginclude file or the *.ccmi file using the “Includes” function.
For instructions on “Includes” please refert to the respective chapter (→12).

4.8.3 Adding new tree elements to an existing sub configuration

It is possible to add new tree elements to an existing sub configuration. To do so, open the
sub configuration in IPEmotion and then make your changes in the desired tree elemenet.
Once the desired tree element is configured properly, you can then righclick on it and se-
lect “Create sub-config”.

In the following window choose the sub configuration file (*.isz) on which you are currently
working and confirm pressing “Save”. This will not result in overwriting the existing sub con-
figuration, but rather will the modification be added to the exisiting sub configuration.

Changesanderrorsexcepted.

84

4.8 SUBCONFIGURATIONS

4.8.4 Unlinking tree elements from existing sub configurations

If you have an existing sub configuration and wish, that one of the included tree elements
is not part of the sub configuration any longer, this can be achieved via the “Unlink sub-
config” function.
In order to do so, open the sub configuration file (*.isz) in IPEmotion, rightclick on the tree
element, that is not supposed to be part of the sub configuration any longer, choose “Un-
link sub-config” and then save the sub configuration.

The “Unlink sub-config” function also allows you to revert a tree element, which has pre-
viously been converted into a sub configuration. As soon as you apply the “Unlink sub-
config” function, the respective tree element will be part of the main configuration again.

4.8.5 Encrypt/Decrypt sub configurations

Once a sub configuration has been created it is possible to encrypt it using IPEmotion‘s
“Key management” function. For instructions on using the “Key management” function
please consult the IPEmotion manual.

Changesanderrorsexcepted.

85

4.8 SUBCONFIGURATIONS

Once a sub configuration file has been encrypted it can only be ac-
cessed by a logger with the corresponding decryption file containing
the correct password for decryption. Loss of the password will result in
the loss of all the vital data contained in the encrypted sub configura-
tion.

4.8.5.1 Encrypting a sub configuration

Only existing sub configuations can be encrypted, meaning, that a sub
configuration can not be created and encrypted in the same step. You
will first need to create the sub configuration and in a following step will
be able to encrypt it as described below.

In order to encrypt a sub configuration right-click the desired sub configuration in the mea-

surement task tree and then click “Encrypt subconfig”. The sub configuration is now en-
crypted.

An encrypted sub configuration can be recognized by the little lock symbol in the corre-
sponding tree element.

Changesanderrorsexcepted.

86

4.8 SUBCONFIGURATIONS

4.8.5.2 Decrypting a sub configuration

In order to decrypt a sub configuration right-click the desired sub configuration in the
measurement task tree and then click “Decrypt subconfig”. The sub configuration is now
decrypted.

4.8.5.3 Transfer of private key for encryption (Create dlua for encryption)

In order for the logger to be able to access encrypted sub configurations it needs to be
provided with the private key corresponding to the encrption certificate that has been
used.
To do so you will first need to create a *.dlua file containing the private key and in a sec-
ond step transfer this *.dlua file to the logger.

To create the *.dlua file, once a sub configuration has been encrypted, select the logger
in the measurement task tree, click the “Functions” button in the Ribbon and then choose
“Create dlua for encryption”.

Changesanderrorsexcepted.

87

4.8 SUBCONFIGURATIONS

In the resulting window specify a file name and path for the *.dlua and save it.

In a final step you will need to transfer the *.dlua file to the logger as described in the
chapter “Updating licences, firmware and web interface of the logger” (→4.5.5).

Even though it does not specifically mention *.dlua for encryption in this chapter, this is the
way to transfer *.dlua files for encryption to the logger.

Changesanderrorsexcepted.

88

4.8 SUBCONFIGURATIONS

4.8.6 Subconfig options

The “Subconfig options” provide a set of options specific for the behaviour of a subcon-
figuration. These options can be set for each subconfiguration individually.

In order to access these options right click on the desired subconfiguration in the mea-
surement task tree (it may be necessary to import the subconfiguration into your system
beforehand, to do so please refer to this chapter →4.4.6) and then click on “Edit subconfig
options” in the resulting context menu.

Changesanderrorsexcepted.

89

4.8 SUBCONFIGURATIONS

4.8.6.1 Use alias references for includes

This setting determines the referencing settings for includes when they get saved and
loaded and thus determines directly where in the measurement task tree the include will
appear, once it is imported into an existing configuration. Includes that are created and
saved with this option activated will later also be imported accordingly in any system,
even if this option is deactivated in the target system. The following table will explain the
behaviour of this setting according to the different connectors it can be applied to.

Tree element be-
low...

Option activated will
ence include using...

refer-

Option deactivated will refer-
ence include using...

CAN

LIN

Name of the connector

Name of the connector

FlexRay

Name of the connector

Channel number parameter
of the connector link
Channel number parameter
of the connector link
Channel number parameter
of the connector link
Channel number parameter
of the connector link
Name of the dataset link

Name of the ringbuffer link

Name of the method link

Name of the connector

of

the

parameter

Alias
dataset
Alias parameter of the ring-
buffer
Alias
method link

parameter

the

of

Name of the trace channel

Channel number parameter
of the connector link

ETH

Dataset

Ringbuffer

Methods
(Timelog,
Audio,
Classing,
Video, GPS, J1939,
DLT, no Trace chan-
nels)
Trace channel
(Vector
BLF/ASCII/ASCII
Compressed, MDF
4.1
trace,
PCAP)

- Bus

Twoexamplestogiveabetterunderstandingofhowthisworks:

Example1:
A sub configuration of a CAN channel named “CAN Test” with the hardware channel
number 02 is created.
If the “Use alias references for includes” option is active at cre-
ation of the sub configuration, this sub configuration will later be imported into an existing
configuration under the CAN channel named “CAN Test”. If the target system does not
contain a CAN channel named “CAN Test”, this channel will be created upon import.

If the “Use alias references for includes” option is inactive at creation of the sub configu-
ration, the sub configuration will later be imported into an existing configuration under the
CAN channel with the hardware channel number 02.

Example2:

Changesanderrorsexcepted.

90

4.8 SUBCONFIGURATIONS

A sub configuration of a Timelog named “Timelog 01” with the alias “Timelog Test” defined
in the details area is created. If the “Use alias references for includes” option is active at
creation of the sub configuration, this sub configuration will later be imported into an ex-
isting configuration under its alias “Timelog Test”.

If the “Use alias references for includes” option is inactive at creation of the sub configu-
ration, the sub configuration will later be imported into an existing configuration under its
name “Timelog 01”.

In order to change this setting, navigate to the “Subconfig options” (→4.8.6) as mentioned
above and activate the option “Use alias references”.

4.8.7 Importing sub configurations

For instructions on importing sub configurations please refer to the chapters “Opening sub
configurations” (→4.4.5) and “Including sub configurations” (→4.4.6).

Changesanderrorsexcepted.

91

5 PROJECTSETTINGS

5 Project settings

“Project settings” allow you to include project parameters such as company name, se-
rial number, project name etc. in your Configuration. It is also possible to create a set of
project settings, specific for a dataset. That way, you can define different project param-
eters for different datasets. Please refer to the section “Dataset Project settings” (→15.3).

5.1 Adding project parameters

It is possible to add user-specific project parameters in addition to the default project pa-
rameters. To do so, select the “Project settings” element in the measurement task tree,
select the “Components” button in the Ribbon and then choose “Project parameter”.

The new parameter will appear in the respective “Project settings xx” Grid area as cus-
tomizable parameter in the table.

Changesanderrorsexcepted.

92

5.2 ASSIGNINGATEMPLATEOFPROJECTPARAMETERS

5.2 Assigning a template of project parameters

It is also possible, to assign a template which contains a predefined set of user-specific
project parameters. To do so, right-click on the “Project settings” tree element and then
choose “Assign template”.

In the following window you may choose the template file and confirm wit “Open”. The
file type needs to be .xml.

The CAETEC dataLog PlugIn for IPEmotion currently supports two types
of templates, the “EDR” type and the “Feger” type. Both templates are
installed with the plugin in the format “projectPar.xml” and can be found
in the plugin’s installation directory under “UserData/ProjectTemplate”.

If at dataset creation either of these two template types is assigned, the
dataset will be treated especially.

Changesanderrorsexcepted.

93

5.3 TREEELEMENTSFORPROJECTSETTINGS

5.3 Tree elements for Project settings

Including “Project settings” in your configuration will add one new tree element. The tree
element is labeled “Project settings”.

5.4 Grid area for Project settings

If the “Project settings” element is selected in the Measurement task tree, the grid area
will provide you with a table, that allows you to access all default or previously defined
user-specific projet parameters.

Changesanderrorsexcepted.

94

5.5 DETAILSAREAFORPROJECTSETTINGS

5.5 Details area for Project settings

If the “Project settings” element has been selected in the measurement task tree, addi-
tional settings are available in the details area.
General
This tab provides general settings for the selected Project settings file.

• Name

Give a user-defined Name to the selected formula/signal.

• Description

Give a user-defined description to the selected formula/signal.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Info
Tells you the type of template that has been assigned.

Changesanderrorsexcepted.

95

5.6 USINGPROJECTPARAMETERSASVARIABLESINCAETECDATALOGPLUGIN

5.6 Using project parameters as variables in CAETEC dataLog PlugIn

If project settings have been added to your configuration, the Keys of these project set-
tings can be used as variables in some text fields. This can be helpful if the same Parameter
(e.g. “VehicleID”) should be used in many different contexts. It is then enough, to define
a value for that key. Whenever that key is used as a variable in the right context, at export
of the datalog.ccmc it will be replaced with the corresponding value.

To use this feature, select the “Project settings” interface in the measurement task tree
and navigate to the grid area. Access the column chooser (→4.2.5) and add the “Key”
column to the grid area.

This will add a new column with the exact keys, that can be used. Now a corresponding
value has to be defined for the key you which to use as variable. Click in the correspond-
ing “Value” field for the desired key (e.g. “VehicleID” and type in the Value that shall be
used (e.g. “Example Vehicle ID”).

The term “VehicleID” can now be used as a variable in certain text fields and will be re-
placed with the value “Example Vehicle ID” in the datalog.ccmc.

Changesanderrorsexcepted.

96

5.7 USINGSYSTEMPARAMETERSASVARIABLESINCAETECDATALOGPLUGIN

The syntax for variables is the following:

Variable

<Key>
<VehicleID>

in

Value written
log.ccmc
“Value”
“Example Vehicle ID”

data-

Wherever it is possible to use project parameters as variables, this maual
will point that out with an inforamtion box.

5.7 Using system parameters as variables in CAETEC dataLog PlugIn

In the same way, as it is possible to use project parameters as variables in CAETEC dataLog
PlugIn, it is also possible to use system parameters as variables wherever project parame-
ters can be used as variables, although the list is considerably shorter.

In the case of system parameters it is not necessary to create a set of parameters, there is
a fixed list of parameters available presented in the following table.

This function can be particularly useful when it comes to automated versioning of the
same configuration or subconfiguration file being exported. As the logger always uses
the current date and time at export, there is no need to label the different versions man-
ually anymore, but one can just use the data and time as orientation.

System parameters outrank project parameters in priority. So in case of
a redundancy where a system parameter and a project parameter are
identical, the project parameter will be ignored at export.

Variable

<[SystemDateTime]>

<[SystemDate]>

<[SystemTime]>

Value written in
datalog.ccmc
The current date and
time of the logger at ex-
port
The current date of the
logger at export
The current time of the
logger at export

Format

yyyyMMdd_HHmmss

yyyyMMdd

HHmmss

Changesanderrorsexcepted.

97

6 UPS(UNINTERRUPTIBLEPOWERSUPPLY)

6 UPS (Uninterruptible power supply)

The UPS (Uninterruptible power supply) module provides the logger with power for a lim-
ited time in case of loss of external power. The UPS can be configured through the root
element “UPS”, which will also provide a list of status signals about the “UPS” module.

“UPS” status signals are largely treated in the same manner as a regular signal. They can
be recorded over time, classed or processed; they can generate alarms or be displayed.
Only they can’t be directly stored in traces.

If a shut down occurs with no external power supply available, i.e. while
the “UPS” is active, the “UPS” will cause an emergency shut down. That
means, that the logger will shut down, but all configured data transfers
will be ignored.

6.1 Storage method

In order to store “UPS” status signals use one of the following signal storage methods.

• ATFX (→ 15.7)

• MDF 4.0 (→ 15.8)

• MDF 4.1 (→ 15.9)

• CAETEC binary (→ 15.15)

• CAETEC ASCII (→ 15.16)

Changesanderrorsexcepted.

98

6.2 ADDINGTHEUPSINTERFACE

6.2 Adding the UPS interface

In order to configure your “UPS” and make its signals accessible you will first need to add
the “UPS” interface to your system. To do so, select the system in the measurement task
tree (the topmost element in the tree),click the “Components” button in the Ribbon and
then choose “UPS”.

6.3 Configuring the UPS interface

6.3.1 Tree elements for the UPS interface

Adding the “UPS” interface to your system will produce two new tree elements: the inter-
face itself labeled “UPS” and its childelement labeled “Status”.

6.3.2 Details area for the UPS interface

Selecting the “UPS” interface in the tree allows you to access two tabs in the details area.

General
This tab allows you to activate or deactivate the “UPS” interface and thus to make its sig-
nals available for internal Recording and further use (e.g. triggers, formulas, display,...)
It also allows you to give a user specific name to your signal if wished and add an addi-
tional description. The Reference field serves as the tree element’s unique identifier inside
the measurement task tree. It cannot be changed.

Settings
This tab contains settings regarding the “UPS”.

• Charge threshold

Define a threshold in percentage of the battery charge. If the state of battery charge
falls below or is already below this threshold at loss of external power, the logger will

Changesanderrorsexcepted.

99

6.3 CONFIGURINGTHEUPSINTERFACE

shut down.

• Time threshold

Define a threshold in percentage of the remaining battery time.
If the state of re-
maining battery time falls below or is already below this threshold at loss of external
power, the logger will shut down.

• Ignore duration

If set, for the defined amount of time, the logger will ignore regular shutdown condi-
tions and only perform an emergency shut down if either the “Charge threshold” or
“Time threshold” are met.

If a shut down occurs with no external power supply available, i.e. while
the “UPS” is active, the logger will perform an emergency shut down.
That means, that the logger will shut down, but all configured data trans-
fers will be ignored.

Changesanderrorsexcepted.

100

6.4 UPSSIGNALPROPERTIES

6.4 UPS signal properties

“UPS” status signals do not need to be imported, as they are continuosly produced by the
“UPS” itself. As soon as the “UPS” interface has been added to the system, they can then
be activated in order to be used liked regular signals in further processing, for example as
triggers or in formulas.

6.4.1 Grid area for UPS signals

When selecting any of the “UPS” tree elements, the “Grid area” will present you with an
overview of the available “UPS” status signals. Also you can find here two important func-
tions, which are the “Column chooser” (→4.2.5) and the “Filter editor” (→4.2.6).

6.4.2 Overview of UPS signals

Signal

Meaning

Power lost

Loss of external power

Capacitator voltage

State of charge

Remaining runtime

Current voltage of the UPS
capacitors
Shows the state of charge
in percentage of the battery
capacity
Shows the remaining runtime
of the “UPS” in seconds

and/or
Val-

Unit
Possible
ues
0 = No
1 = Yes
V 0-29

% 0-100

s 0-10000

Changesanderrorsexcepted.

101

6.4 UPSSIGNALPROPERTIES

6.4.3 Details area for UPS signals

If a “UPS” status signal is selected in the grid area, the details area will additional tabs with
settings regarding these signals. These settings will be explained in the following.

General
This tab allows you to activate or deactivate the signal by ticking/unticking the checkbox
and thus to make it available for internal Recording and further use (e.g. triggers, formu-
las, display,...)
It also allows you to give a user specific name to your signal if wished and add an addi-
tional description. The Reference field serves as the tree element’s unique identifier inside
the measurement task tree. It cannot be changed. The “Sampling rate” allows you to set,
how frequently a signal should be requested. The tickbox “Cyclic” allows you to switch
between cyclic and event controlled sampling.

Format
This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “64-Bit floating point”) and allows you
to apply special tasks for this signal.

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a signal value is read as
invalid.

Changesanderrorsexcepted.

102

6.4 UPSSIGNALPROPERTIES

• Channel type

This field tells you whether you are dealing with a “Input” channel or “Output” chan-
nel.

Scaling
The fields accessible directly through the tab allow for basic scaling operations to con-
vert analog measurement in engineering units. The “Scaling calculator” allows for more
refined scaling options with a large range of functions. For details on how to use the
“Scaling calculator” please refer to the IPEmotion Documentation - Section 3.4.5 “Chan-
nel configuration and scaling”.

• Sensor Mode

The sensor mode tells the type of signal. It can be of different types such as “Status”,
“Voltage”, “Percent” or others.
It cannot be changed and serves for IPEmotion to
know what kind of signal it is dealing with.

• Sensor Range

Shows the raw value range of the signal.

• Physical Range

Allows you to set a range to which you would like to “scale” your signal and also de-
fine the unit to use. For more refined scaling please use the “Scaling calculator” and
refer to the IPEmotion Documentation - Section 3.4.5 “Channel configuration and
scaling”.

Changesanderrorsexcepted.

103

6.4 UPSSIGNALPROPERTIES

Display
This tab allows you to define what information about the current signal will be shown on a
display if one is connected.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

• Name

Allows you to set a Name to be shown on a display.

Signal
This tab allows you to define signal settings.

• Signal number

Assign a number to the current signal. This way you will later be able to sort the signals
in the grid according to their “Signal numbers”.

Changesanderrorsexcepted.

104

6.4 UPSSIGNALPROPERTIES

• Hold las value

Specify, for how long the last value of the signal will be hold.

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

• Origin

Tells the source of the signal. This can help identifying the source of a signal for which
a user defined signal name has been set.

Changesanderrorsexcepted.

105

7 DRIVEBAY(ARCOS1.5ANDETHOS)

7 Drivebay (Arcos 1.5 and ETHOS)

The “Drivebay” is an extension module available for the Arcos 1.5 and the ETHOS system.
It provides your logger with two extra slots, that can be equipped with a 2.5 inch SSD (Solid
State Disk) each, in order to expand your logger’s storage capacity.

The equipped SSDs can be defined as storage targets for datasets, so the dataset will be
stored on the SSD. For instructions on how to do so please refer to the “Dataset settings”
of the “Dataset” chapter (→15.1.3).

7.1 Adding the Drivebay interface

In order to use the equipped SSDs, you will need to add the “Drivebay” interface to your
system. To do so, select the System in the measurement task tree, click the “Components”
button in the ribbon and then choose “Drivebay”.

7.2 Tree elements for Drivebay

Once the “Drivebay” interface has been added to your system, it will appear as a new
tree element in the measurement task tree.

Changesanderrorsexcepted.

106

7.3 DETAILSAREAFORDRIVEBAY

7.3 Details area for Drivebay

The Details area shows settings either for the “Drivebay” interface.
General
Please refer to (→4.2.2).

Trigger
The “Trigger” tab allows you to select the triggers for unmounting the left and right drive-
bay. The trigger for each field may be selected using the “Select” button and then choos-
ing the desired trigger from all configured triggers of your configuration.

Settings (ARCOS 1.5 only)
The “Settings” tab contains the “Requires USB-Dongle” setting. If this setting is activated, a
USB-Dongle with a signed datalog.key is needed in order to eject an SSD from the “Drive-
bay” and remove it from the logger.

Changesanderrorsexcepted.

107

8 SIGNALACQUISITION

8 Signal Acquisition

8.1 CAN/CAN FD channels

All the CAN channels for your system are located in the tree element “CAN interfaces”.
There are two types of CAN channels, physical “CAN” channels and “Virtual CAN” chan-
nels.
According to the default settings, the tree element “CAN interfaces” will include a preset
number of CAN channels. By clicking the tree element CAN Interfaces you will see all
of its channels and signals in the grid area as well as a tab called General in the Details
area which allows you to set a name and description. These settings apply to the entire
element “CAN interfaces”.

In the following will be described how to add CAN channels and adjust their settings
(→8.1.3).

8.1.1 Storage method

In order to store all incoming traffic on a CAN channel use a bus tracing method for stor-
age. Please refer to (→ 15.10).

Changesanderrorsexcepted.

108

8.1 CAN/CANFDCHANNELS

8.1.2 Adding CAN/CAN FD channels

CAN channels can be added by selecting the system in the tree, then clicking the “Com-
ponents” button and finally choosing the desired type of CAN channel you wish to add.

• CAN/CAN FD

Adds a CAN channel that corresponds to a physical CAN channel of your logger.
For instructions on CAN settings refer to (→8.1.3).

• Virtual CAN

Adds a virtual CAN channel. For instructions on Virutal CAN settings refer to (→8.1.4).

Multiple selection Allows you to add multiple CAN channels of both types at the same
time. To do so set the counter for each type to the desired number of channels that
you wish to add as marked in the figure below.

Changesanderrorsexcepted.

109

8.1 CAN/CANFDCHANNELS

8.1.3 CAN settings

By selecting one of the CAN channels in the tree you will be able to define this channel’s
settings in the details area.

The same settings described in this section as part of the Details area can
also be adjusted when selecting the tree element CAN interfaces and
then directly changing the desired setting in the respective field of the
Grid area.

Changesanderrorsexcepted.

110

8.1 CAN/CANFDCHANNELS

8.1.3.1 General

This tab allows you to give a user specific name for the selected CAN channel if wished and
add an additional description. The Reference field serves as the tree element’s unique
identifier inside the measurement task tree. It cannot be changed.

The Active checkbox allows to deactivate the entire bus. If a bus is deac-
tivated all childelements of this bus will be deactivated, too, and cannot
be stored or traced, until the bus is reactivated.

8.1.3.2 CAN

Baud rate
The dropdown menu Baud rate allows you to set the Baud rate for the selected CAN chan-
nel. The baud rate defines the speed in bits/second at which data can be transmitted
through the CAN bus. The speed muss be adapted to the source. Only if all the users on
the bus are set at the same rate, is transfer possible.

Send/ACK mode
The checkbox Send/ACK mode allows you to determine whether the CAN channel may
communicate or is in silent mode. If the checkbox is marked, the channel may commu-
nicate, if the checkbox is not marked, the channel is in silent mode.

CAN FD
This option is only supported on CAN FD channels in the CAN FD interface.
If activated, you may customize the fast datarate of the CAN FD channel.

Data rate
This option is only supported on CAN FD channels in the CAN FD interface.

Changesanderrorsexcepted.

111

8.1 CAN/CANFDCHANNELS

If CAN FD is activated you may set the fast datarate for the channel here.

Sample point
Sample point for normal data rate.

Sync jump width
Sync jump width used for the CAN message bits.

8.1.3.3 CAN (for CAN FD)

Baud rate
The dropdown menu Baud rate allows you to set the Baud rate for the selected CAN chan-
nel. The baud rate defines the speed in bits/second at which data can be transmitted
through the CAN bus. The speed muss be adapted to the source. Only if all the users on
the bus are set at the same rate, is transfer possible.

Send/ACK mode
The checkbox Send/ACK mode allows you to determine whether the CAN channel may
communicate or is in silent mode. If the checkbox is marked, the channel may commu-
nicate, if the checkbox is not marked, the channel is in silent mode.

CAN FD
This option is only supported on CAN FD channels in the CAN FD interface.
If activated, you may customize the fast datarate of the CAN FD channel.

Data rate
This option is only supported on CAN FD channels in the CAN FD interface.
If CAN FD is activated you may set the fast datarate for the channel here.

Sample point
Sample point for the normal and fast data rate.

Sync jump width
Sync jump width used for the CAN/CAN FD message bits.

Changesanderrorsexcepted.

112

8.1 CAN/CANFDCHANNELS

8.1.3.4 Wake On CAN

Timeout
For Wake on CAN, timeout has a special significance. It defines how long a waking chan-
nel must be inactive to be recognized so and therefore allow for the logger to shut down.
If timeout is recognized, an entry is made in the log file and an error message with an alert
appears on the display, which has to be acknowledged.

Mode
This dropdwon menu allows you to set the wake-up function for your selected CAN chan-
nel.

Wake on CAN type
Disabled

Enabled

Enabled (no message lost)

Keep awake

Characteristics
No start on CAN messages, lowest en-
ergy consumption.
Start on a CAN message, with first mes-
sages lost; low energy consumption.
Start on CAN message, with no mes-
sage lost; slightly higher idle current.
The logger starts with Clamp 15, but only
shuts down if all the awakening condi-
tions (Clamp 15 and WakeOnX) are no
longer fullfilled.

CAN ID - Settings for starting on a specific CAN ID

The CAN ID consists of two fields in the “Wake on CAN” tab of the CAN channel’s details
area: The “CAN identifier” on the left and the “CAN ID bitmask” on the right.

The aim of this setting is to wake the logger with a message having a specific ID (or group
of IDs), regardless of what the content of the message is. In order to do so, you can de-
fine a “CAN identifier” and a “CAN ID bitmask” to limit the identifier. Both parameters are
used in their binary form. The “CAN ID bitmask” defines (or masks) the bit positions of a
message ID that are to be applied. The “CAN identifier”￿ specifies the contents that must
exist at these bit positions in order for a start to take place.

Changesanderrorsexcepted.

113

8.1 CAN/CANFDCHANNELS

Both fields can be defined as “standard CAN ID” or “extended CAN ID” by clicking the
button in the left corner of the field. Both fields can process and show the entered number
in its decimal or hexadecimal form. To switch between decimal or hexadecimal just click
the button in the right corner of the field as marked in the figure above.

The decimal number is processed in the logger in its binary form and if
the number set for the “CAN ID bitmask” = 0, the logger will start on any
message.

Example:
CANidentifier=22(binary=10110)
CANIDbitmask=28(binary=11100)

Inotherwords,themask(CANIDbitmask)specifiesthat,tostartthelogger,givenvalues
areexpectedatthepositionsBit2,Bit3,Bit4. Allothervaluesareirrelevant(“x”).
TheCANidentifiercallsforBit2tobe”1”￿,Bit3tobe”0”andBit4tobe”1”￿.
The following table lists the positions for an 11-bit CAN identifier (in red the masked posi-
tions,thenumberssignifyingtheexpectedvalues).

Bit10 Bit9 Bit8 Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0
x

1

0

1

x

x

x

x

x

x

x

ExampleofvaluesofaCANIDthatwouldstarttheloggerinthisconfiguration:

Bit10 Bit9 Bit8 Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0

1

0

1

0

0

0
1
1

0
1
0
1
0

0
0
0
1
0

1
1
1
1
1
1
1

0
0
0
0
0
0
0

1
1
1
1
1
1
1

0
1
0
1
1
0
0

1
1
0
1
0
0
1

CAN-ID
(dec)
277
87
1044
247
150
20
21

ValuesofaCANIDthatwouldNOTstarttheloggerinthisconfiguration(example):

Bit10 Bit9 Bit8 Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0

1

0

0

0

1

1

0

0

1

CAN-ID
(dec)
281

Datafield - Settings for starting on a specific message value of a CAN ID

The Datafield consists of two fields in the “Wake on CAN” tab of the CAN channel’s details
area: The “Datafield content” field, which will contain the “Datafield content value“ on
the left and the “Datafield bitmask” on the right.

Changesanderrorsexcepted.

114

8.1 CAN/CANFDCHANNELS

The aim of this setting is to wake the logger with a given content of a message with a
particular ID (or a group of IDs).

After defining the ID that is supposed to start the logger, you can follow the above pat-
tern to additionally specify which value within the message of the ID is to be an additional
requirement for start. The entire 64-bit message is considered, single bits of which can be
defined as start conditions. (In order to specify the values, it is necessary to decode the
binary structure of the message. There is no DBC file assistance available here.)

A “Datafield bitmask”￿ defines (masks) which bit positions of a message are to be applied.
A “1”￿ marks the bit positions to be used. Positions coded ”0” are ignored. The “Datafield
If “Datafield
content value” specifies the contents checked in the mask by the logger.
content value”￿ writes ”1”￿ (or ”0”) in the positions of the mask (Datafield bitmask), then the
mask positions of the ID must contain the identical values; i.e. ”1”￿ (or ”0”) too, otherwise
the logger is not started.

Both fields can process and show the entered number in its binary, decimal or hexadeci-
mal form. To switch between binary, decimal or hexadecimal just click the button in the
right corner of the field as marked in the figure above.

The decimal number is processed in the logger in binary form and if the
number set for the “Datafield bitmask” = 0, the logger will start on any
message. When the number entered in the “Datafield bitmask” is con-
sidered in binary form,
”1”￿ defines a bit position that is considered in filtering,
”0” means filtering ignored this bit position.

Example:
WakeonCANtriggerrawvalue=22(binary=10110)
WakeonCANrawvaluemask=20(binary=10100)

Themask“Datafieldbitmask”￿specifiesthat,theloggerisonlystartedifcertainvaluesare
foundatthepositionsBit2andBit4. Allothervaluesareirrelevant(“x”￿).
“Datafieldcontentvalue”￿callsforBit2tobe”0”andBit4tobe”1”￿.
Thefollowingtableliststhepositionsfora64-bitmessage(withthemaskedpositionscol-
oredredandthenumberssignifyingtheexpectedvalues).

Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0

x

x

x

1

x

0

x

x

Messagevaluesthatwouldstarttheloggerinthisconfiguration(example):

Changesanderrorsexcepted.

115

8.1 CAN/CANFDCHANNELS

Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0

1

1
0

0

1
0

1
1

1
1
1
1
1
1

0
1
0
1
0
1

0
0
0
0
0
0

0
1
0
1
1
0

1
1
0
1
0
0

Messagevalue
(dec)
17
27
16
251
146
24

NegativeexampleofmessagevaluesthatwouldNOTstarttheloggerinthisconfiguration:

Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0

0

0

0

1

1

1

0

0

Messagevalue
(dec)
28

Settings for starting on a specific signal

The settings described in the previous paragraphs apply to entire messages. This section
explains how to apply these settings to a specific signal contained in a message. It de-
scribes the procedure for deriving the required WoC parameters from the physical value
of a signal. Since a simple formula such as “signal > 30”￿ is not possible, it is necessary to
define the start condition at the bit level. The numeric format is important, as well. The
order in which the bit positions are counted depends on the numeric format (e.g., Intel
or Motorola). Please bear in mind, when selecting the signal and a particular start value,
that the start condition must be met during the entire measurement run. Remember: The
start signal is also the stop signal. If the start signal is missing for a set period of time, the
logger is stopped. This makes state bits good start signals. Signals such as temperature
signals that generally fluctuate, are only suitable providing the definition of the start con-
dition is sufficiently vague. Here vague means that not a specific bit combination switches
on the logger, but that a range of bit combinations is possible. When defining filters, be
sure to avoid gaps between the significant mask positions (marked), otherwise the cov-
ered range of values will also have gaps (see Filter 4), which would shut down the logger.
Several filters serve as examples below. The table shows which values start the logger with
which filter. In the column for each filter, these values are marked with an “X”￿.

Filter1:
Datafieldcontentvalue=16(binary=10000)
Datafieldbitmask=24(binary=11000)

Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0

x

x

x

1

0

x

x

x

Filter2:
Datafieldcontentvalue=24(binary=11000)
Datafieldbitmask=24(binary=11000)

Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0

x

x

x

1

1

x

x

x

Filter3:

Changesanderrorsexcepted.

116

8.1 CAN/CANFDCHANNELS

Datafieldcontentvalue=16(binary=10000)
Datafieldbitmask=16(binary=10000)

Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0

x

x

x

1

x

x

x

x

Filter4: (negativeexample)
Datafieldcontentvalue=18(binary=10010)
Datafieldbitmask=18(binary=10010)

Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0

x

x

x

1

x

x

1

x

Dec. value Binaryvalue Filter1 Filter2 Filter3 Filter4

15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32

x
x
x
x
x
x
x
x

0000001111
0000010000
0000010001
0000010010
0000010011
0000010100
0000010101
0000010110
0000010111
0000011000
0000011001
0000011010
0000011011
0000011100
0000011101
0000011110
0000011111
0000100000

x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x

x
x

x
x

x
x

x
x

x
x
x
x
x
x
x
x

The following example of a temperature in Intel format illustrates how to derive the filter
settings.

Example
With the logger operating in the temperature range of approx. 30 - 40 °C, the following
signaldefinitionisgiven:
DerivingWakeonCAN“Datafieldbitmask”andWakeonCAN“Datafieldcontentvalue”:

First you use the limit values to derive the raw value and thus the binary value of the op-
eratingrange.

Dataf ieldcontentvalue30degree

value − Of f set
Scale

=

30 − (−10)
0.1

= 400 = Binary : 110010000

Changesanderrorsexcepted.

117

8.1 CAN/CANFDCHANNELS

Dataf ieldcontentvalue40degree

value − Of f set
Scale

=

40 − (−10)
0.1

= 500 = Binary : 111110100

Thehighestbitpositionsthatareidenticalforbothvalues,withoutagap,arethetwoon
theleft,whichhavethevalue1. Thisyields,asmaskandfilterbinary: 110000000

SothelowerboundfortheDatafieldcontentvalueis:

• binary110000000

• decimal384

• physical28,4°C

SotheupperboundfortheDatafieldcontentvalueis:

• binary111111111

• decimal511

• physical41,1°C

Since the value has 9, but the signal 16 Bit, the 7most significant Bits have to be 0. This is
achievedbytheDatafieldbitmask.

Filter:
WakeonCANDatafieldcontentvalue=384(binary=0000000110000000)
WakeonCANDatafieldbitmask=65408(binary=1111111110000000)

Bit Bit Bit Bit Bit Bit Bit Bit Bit Bit Bit Bit Bit Bit Bit Bit
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
x
0 0 0 0 0 0 0 1 1 x

x

x

x

x

x

Since,however,thesignalliesinthemiddleofthe64bit-widemessage(bitoffset=16),the
bit positions to the right of the signal in themessagemust be filled with “0”￿ (left is equal
toBit0intheCAN-traffic).

Bit-Offset

T_Aussen

Don’tcare

0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
LSB

Binary
Intel:
Datafieldcontentvalue: 0000 0000 0000 0000 0000 1000 0001 0000 0000 0000 0000 0000 0000 0000 0000 0000
Hex:
Datafieldbitmask:
Hex:

0000 0000 0000 0000 0000 1000 1111 1111 0000 0000 0000 0000 0000 0000 0000 0000

MSB

0

0

0

0

0

0

0

0

0

8

1

0

0

0

0

0

0

0

0

0

0

0

0

8

0

0

0

0

0

0

F

F

SotheDatafieldcontentvalueisequalto:
Datafieldcontentvalue(hex)=0xFF800000
Datafieldcontentvalue(dec)=4,286,578,688

Sothemaskisequalto:
Datafieldbitmask(hex)=0x1800000
Datafieldbitmask(dec)=25,165,824

WakeonCANDatafieldcontentvalue=WakeonCANDatafieldbitmask

Changesanderrorsexcepted.

118

8.1 CAN/CANFDCHANNELS

DerivingWakeonCAN“CANidentifier”and“CANIDbitmask”:
The precise ID of the message is to be found – i.e. all the positions of the ID that are not
leading zeros are significant. All the significant positions are to be assigned the value of
theID.
Thismeans:

CANidentifier=MessageD=100

DerivingthesignificantbitpositionsoftheID:
ID(dec)=100=>ID(bin)=1100100
The ID also has 7 significant positions. So the mask must also be 7 bits long. All positions
mustbeassigned“1”￿.
“CANIDbitmask”=1111111=127(dec)

Eachnodecanthusbeassignedindividualstartsettings. Remember: Duringthebooting
phase,atthenodethatstartedthelogger,theWoCLEDonthefrontplateoftheinterface
blinksquicklyforapproximatelytenseconds.

Even if WoC (Wake on CAN) is set as start condition the logger starts on
clamp 15. So start on clamp 15 has priority over WoC. This is necessary
to have a fallback solution in case a start message or start value can no
longer be sent.
If the logger was started with clamp 15, it can likewise only be shut down
by “pulling” Clamp 15 – based on the principle, the source that starts,
also stops – providing there is not simultaneously another wake condition
(e.g. WoC) active.

8.1.3.5 Hardware (Channel number)

This tab allows you to set a Channel number for the selected CAN channel. This channel
number has to be unique within the CAN interface.

For better orientation and in order to avoid confusion regarding Chan-
nelnumbers and -names, a Channels physical number can be found in
the logger’s “Web Interface” and set accordingly.

Changesanderrorsexcepted.

119

8.1 CAN/CANFDCHANNELS

8.1.3.6 Bus check

This tab allows you to activate “Bus check” for this bus. You may choose whether you
wish to apply the global bus check settings to this bus or override the global settings with
settings specific for this bus.
Global bus check settings have to be defined first. For information on how to do so and
for general information on “Bus check” please refer to (→4.2.2).

8.1.4 Virtual CAN settings

By selecting one of the Virtual CAN channels in the tree you will be able to define this
channel’s settings in the details area.

Virtual CAN channels now also support “Manual messages” (refer her
for instructions on manual messages→8.2.5) as well as freerunning pro-
tocol databases of the types “DBC”, “Fibex” and “ARXML” (refer here
for instructions on handling DBC, Fibex and ARXML databases in CAN
channels →8.2).

Changesanderrorsexcepted.

120

8.1 CAN/CANFDCHANNELS

The same settings described in this section as part of the Details area can
also be adjusted when selecting the tree element CAN interfaces and
then directly changing the desired setting in the respective field of the
Grid area.

8.1.4.1 General

This tab allows you to give a user specific name to the selected Virtual CAN channel if
wished and add an additional description. The Reference field serves as the tree ele-
ment’s unique identifier inside the measurement task tree.
It cannot be changed. The
“Active” checkbox allows you to activate or deactivate the selected Virtual CAN chan-
nel.

8.1.4.2 Hardware (Channel number)

This tab allows you to set a Channel number for the selected Virtual CAN channel. This
channel number has to be uniqe within the CAN interface.

For better orientation and in order to avoid confusion regarding Chan-
nelnumbers and -names, a Channels physical number can be found in
the logger’s “Web Interface” and set accordingly.

Changesanderrorsexcepted.

121

8.1 CAN/CANFDCHANNELS

8.1.5 CAN channel Bus statistic

The “Bus statistic” provides a range of statistics and status signals for the respective CAN
channel. It contains information on the current state of the Bus, the Busload, as well as on
the messages that have been received and errors that ocurred.

The “Bus statistic” only shows statistics for the channel to which it belongs.
For each channel that you would like to see the statistic, you will have to
add the component “Bus statistic”.

8.1.5.1 Adding Bus statistics
Select the channel in the tree for which you would like to
add “Bus statistic”, then click the “Components” button in the Ribbon and choose “Bus
statistic”.

8.1.5.2 Bus statistic signals Once the component “Bus statistic” has been added to your
channel, it will appear in the measurement task tree as a child element of this channel
and the grid area will give you an overview of the available signals.

The signals included in “Bus statistics” are of the type “Internal signal” and may be ad-
justed in the same way. For more information on “Internal signals” please refer to (→8.26).

Changesanderrorsexcepted.

122

8.1 CAN/CANFDCHANNELS

Overview of signals

Subtype

Controller state

Busload (%)

Number of messages

Meaning
nan= Channel not available
1= Bus on
2= Bus warning
3= Bus off
Bus load of a CAN/LIN chan-
nel
Number of messages since
beginning of measurement
Current bus load
Number of messages with
standard ID
Number of messages with ex-
tended ID
Number of messages with re-
mote standard ID
Number of messages with re-
mote extended ID
Number of error frames

Message rate total
Number of messages with
standard ID
Number of messages with ex-
tended ID
Number of messages with re-
mote standard ID
Number of messages with re-
mote extended ID
Number of error frames
Message rate of standard IDs Messages with standard ID
Message rate of extended IDs Messages with extended ID
Message rate of standard IDs Messages with remote stan-

Unit

-

[%]

-

[frames/s]
-

-

-

-

-
[frames/s]
[frames/s]
[frames/s]

Message rate of extended IDs Messages with remote ex-

[frames/s]

Error frame rate

tended ID
Average of errors per second [frames/s]

dard ID

Changesanderrorsexcepted.

123

8.1 CAN/CANFDCHANNELS

8.1.6 Exporting (XML) CANdb

CAN/CAN-FD/Virtual CAN channels can be exported as CANdb or XML CANdb.

To do so, select the desired channel in the measurement task tree, click the “Export” but-
ton in the Ribbon and the choose either “CANdb” or “XML CANdb”.

In the following window define the path, where the database file should be saved and
confirm with “Save”.

Changesanderrorsexcepted.

124

8.2 CAN/CANFDSIGNALS

8.2 CAN/CAN FD signals

As of V16.10 CAN FD signals are supported. They are equal to regular CAN
signals in functionality. The same settings available for CAN signals are
available for CAN FD signals, thus CAN FD signals will not be mentioned
explicitly.

8.2.1 Storage method

In order to store incoming signals on a CAN channel use one of the following signal stor-
age methods.

• ATFX (→ 15.7)

• MDF 4.0 (→ 15.8)

• MDF 4.1 (→ 15.9)

8.2.2 Importing CAN signals

This section explains how to import CAN signals. There are three different filetypes which
can be used in order to import a single CAN signal or a group of CAN signals:
CANdb (DBC file), Autosar (ARXML) and Fibex.
The import procedure for all of these filetypes is the same and will be explained using the
example of the CANdb import.

To import Signals, select the CAN channel to which you wish to import your signal in the
tree, click the “Import” button in the ribbon and then choose which filetype the “descrip-
tion file”, you wish to use for the import, has. For more information on the “description file”
refer to (→8.2.4.1).

Changesanderrorsexcepted.

125

8.2 CAN/CANFDSIGNALS

The following window lets you choose which file you wish to import. According to the file-
type you have chosen earlier for your import, you will now be able to choose files of the
respective filetype. The dropdown menu on the bottom right of the window shows you,
which filetypes are available. Choose the file you wish to import and click “Open”.

Once you have opened your file, the “Importer” window will appear, that will present you
with a range of importing options.

In this dialog, all signals that can be imported from the description file are displayed. In
the left table, all signals, where the ”selection” checkboxes are selected, will be marked
for import. You can either choose manually, which signals to import, you can use the “Se-
lect/Deselect all” button on the bottom left, or you can use a CSV-file to determine which
signals are to be imported, by clicking “Select by CSV” on the bottom left.

Changesanderrorsexcepted.

126

8.2 CAN/CANFDSIGNALS

In the right table the metadata, properties of the selected signals, the control unit and the
protocol are displayed.

Once you have choosen all the signals you wish to import, click “OK” to complete the
import procedure.

Multiple description files can be imported into the same CAN channel.

Changesanderrorsexcepted.

127

8.2 CAN/CANFDSIGNALS

8.2.3 Import properties

The “Import properties” of a description file, Message or signal allow you to see certain
properties such as the Data format, The CAN identifier, the Bit mask, the start bit, bit count
and more. It shows the signal’s properties as described by the description file.

Figure 1: Example for “Import properties” of a CAN description file

Figure 2: Example for “Import properties” of a CAN Message

Figure 3: Example for “Import properties” of a CAN signal

Changesanderrorsexcepted.

128

8.2 CAN/CANFDSIGNALS

Figure 4: Example for “Import properties” of a multiplexed signal
To access the “Import properties” rightclick on any desired description file, Message or
signal and then choose “Import properties” from the resulting context menu.

Changesanderrorsexcepted.

129

8.2 CAN/CANFDSIGNALS

8.2.4 Signal properties

8.2.4.1 Tree elements for CAN signals

After having successfully imported the desired signals to your CAN channel, this channel
will contain two new layers of child elements in the measurement task tree: The “Descrip-
tion file” and the “Message”.

Description file
The “description file” is a database file which contains signal
information and can be
used to import those signals into a Signal channel in IPEmotion. The filetypes which are
supported by the CAETEC Plugin for IPEmotion depend on the type of signal you wish to
import.

The symbol in the left part of the tree element shows you the type of “description file” you
imported (in this case a “DBC” file), then follows the name of the imported “description
file” (in this case “IPEmotionDemo”) and on the right is a number indicating how many
signals the “description file” contains (in this case 10).

Changesanderrorsexcepted.

130

8.2 CAN/CANFDSIGNALS

Message
Each “description file” can contain one or more “Messages” (in this case 3), which then
contain the actual signals. A “Message” can be found in the “Measurement task tree”
as a child element of the “description file”, it belongs to.
Each “Message” can, again, contain one or more signals (in this case the three “Mes-
sages” contain 4, 4 and 2 signals), which is indicated by the number on the right of the
“Message’s” name.

8.2.4.2 Grid area for CAN signals

In the “grid area” you will be presented with an overview of your selected CAN channel’s
signals. Also you can find here two important functions, which are the “Column chooser”
(→4.2.5) and the “Filter editor” (→4.2.6).

8.2.4.3 Details area for CAN signals

The Details area shows settings either for the selected tree element (“description file” or
“Message”) or the selected signal in the grid area. In case a tree element is selected, the
details area will only show the “General” tab. Please refer to (→4.2.2).

In case a signal is selected in the grid area, the details area will contain additional tabs
which will be explained in the following.

General
Please refer to (→4.2.2).

Changesanderrorsexcepted.

131

8.2 CAN/CANFDSIGNALS

Format
This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “8-Bit integer unsigned”) and allows
you to apply special tasks for this signal such as “GPS Longitude”, “GPS Latitude”,
“UTC hour”, “Audio mono” and more.

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a signal value is read as
invalid.

• Channel type

This field tells you whether you are dealing with a “Input” channel or “Output”
channel.

Scaling
The fields accessible directly through the tab allow for basic scaling operations to con-
vert analog measurement in engineering units. The “Scaling calculator” allows for more
refined scaling options with a large range of functions. For details on how to use the
“Scaling calculator” please refer to the IPEmotion Documentation - Section 3.4.5 “Chan-
nel configuration and scaling”.

Changesanderrorsexcepted.

132

8.2 CAN/CANFDSIGNALS

• Sensor Mode

The sensor mode tells the type of signal. It can be of different types such as “Status”,
“Voltage”, “Frequenzy” or others.
It cannot be changed and serves for IPEmotion
to know what kind of signal it is dealing with.

• Sensor Range

Shows the raw value range of the signal.

• Physical Range

Allows you to set a range to which you would like to “scale” your signal and also
define the unit to use. For more refined scaling please use the “Scaling calculator”
and refer to the IPEmotion Documentation - Section 3.4.5 “Channel configuration
and scaling”.

Display
This tab allows you to define what information about the current signal will be shown on a
display if one is connected.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

• Name

Allows you to set a Name to be shown on a display.

Changesanderrorsexcepted.

133

8.2 CAN/CANFDSIGNALS

Limit values
This tab allows you to define limit values for a signal and what action to take upon a limit
value violation.

• Rejected value

Define what happens to a value, that has been rejected because it is out of bound
or invalid. By default this value will be dropped. It can also be written as NaN.

• Valid ranges (Lower/Upper)

Define up to three ranges of valid signal values. Activate a range in order to define
its upper/lower value (datatype double). Range 2 can only be activated if range 1
is and range 3 can only be activated if range 2 is.

• Invalid values (Physical/Raw)

Define up to three invalid values. Activate an invalid value in order to define the
physical value (datatype double) or raw value (datatype integer).
If one of the
two has been typed in, the other will be calculated according to the scale/offset
settings in the scaling calculator.
Invalid value 2 can only be activated if invalid value 1 is and invalid value 3 can
only be activated if invalid value 2 is.
For details on how to use the “Scaling calculator” please refer to the IPEmotion
Documentation - Section 3.4.5 “Channel configuration and scaling”.

Changesanderrorsexcepted.

134

8.2 CAN/CANFDSIGNALS

Signal
This tab allows you to define signal settings.

• Internal data type

Assign an internal data type to the signal. Available data types are “Double” and
“String”.

• Signal number

Assign a number to the current signal. This way you will later be able to sort the signals
in the grid according to their “Signal numbers”.

• Hold last value

Specify, for how long the last value of the signal will be hold.

• Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may here
select the dataset, to which this setting will refer.

• Timeout

Specify the timeout period for the current signal. If the data source doesn’t send data
for the specified time period, the value of the signal is set to “NaN (Not a Number)”
and will be displayed as “–” in a display.

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

• Special task

The field “Special task” allows you to assign a user specific special task to a signal, as
long as it has not been assigned to a logger default special task in the “Format” tab
yet. If a special task such as “GPS longitude/latitude/altitude in degrees”, “Vehicle
identification” (see also the “Format” tab of the details area for any signal) or other
has been assigned, in the “Format” tab, this field remains uneditable.

The field is a free text field and the entered string will function as a parameter. This
parameter has to be unique within the logger system and can be used in other parts
of the configuration, where parameters can be used. See the table below for an
overview. Other than the project parameters described in the chapter “Project set-
tings” (→5), the parameters from the “Special task” field will not be resolved by IPEmo-
tion at export of the configuration but by the logger in real time.

Changesanderrorsexcepted.

135

8.2 CAN/CANFDSIGNALS

This means for example for datasets/methods the ”special task” will be resolved at
dataset/file creation. For datatransfer paths it will be resolved on datatransfer occu-
rance.

User specific special tasks’ properties
The following table provides an overview of the parts of a configuration, where user
specific special tasks can be referenced and accordingly when the parameters will
be replaced with the respective values.

Reference field
Dataset name
Project Settings

Dataset method name

Datatransfer path

Parameter replacement
At creation of dataset file
At creation of dataset file RE-
VIEW
At
method file
At creation of transfer path

creation

dataset

of

User specific special tasks can also be created and referenced in scripts.
For further information please refer to the script documentaion.

Signal check
This tab allows you to activate “Signal check” for this signal. You may choose whether you
wish to apply the global signal check settings to this signal or override the global settings
with settings specific for this signal.
Global signal check settings have to be defined first. For information on how to do so and
for general information on “Signal check” please refer to (→4.2.2).

Changesanderrorsexcepted.

136

8.2 CAN/CANFDSIGNALS

8.2.5 Manual messages / Manual signals

On CAN/CAN FD and Virtual CAN channels it is possible to set up a manual signal message
which contains manually defined CAN signals. This allows you to define signals indepen-
dently of a description file. You can use manual messages additionally to a description
file or instead of a description file.

8.2.5.1 Adding manual messages and signals

In order to add a manual message to your CAN channel, select the desired channel
in the measurement task tree, click the “Components” button in the Ribbon and then
select “Manual message”.

Changesanderrorsexcepted.

137

8.2 CAN/CANFDSIGNALS

Once the manual message has been added, you can then add one or multiple manual
signals to the message. To do so, select the newly created “Message xx” in the measure-
ment task tree, click the “Components” button in the Ribbon and then select “Signal”.

8.2.5.2 Tree elementes for manual messages

Adding a manual message to your system will add two new layers fo tree elements
The first layer labeled “Manual messages xx” only serves for
to the CAN channel.
grouping together one or more manual messages. As an extra layer underneath you
will find the actual manual message labeled “Message xx”, which will contain your signals.

As you can see on the figure below, it is possible to have multiple “Manual message xx”
layers as well as multiple “Message xx” layers per “Manual message xx”. This allows for a
more structured possibility of organizing manual signals.

Changesanderrorsexcepted.

138

8.2 CAN/CANFDSIGNALS

8.2.5.3 Grid area for manual messages

In the “grid area” you will be presented with an overview of your selected message’s
signals. Also you can find here two important functions, which are the “Column chooser”
(→4.2.5) and the “Filter editor” (→4.2.6).

As you can see in the figure below, if the “Manual message xx” layer is selected, the grid
area will show the signals of all messages contained within the “Manual message xx”.
This may lead to multiple signals with the same name in the grid area.

If you wish to only see the signals of a specific “Message xx”, select the desired “Message
xx” in the measurement task tree.

Changesanderrorsexcepted.

139

8.2 CAN/CANFDSIGNALS

8.2.5.4 Details area for manual messages (defining a manual signal)

The details area provides settings regarding the messages and the signals. As the general
functionality of manual signals is that of a regular CAN signal, please refer to the section
“Details area for CAN signals” of this manual (→8.2.4.3).

Here will only be explained the settings that are specific for manual messages and signals.

Settings for manual messages

In order to access the settings for manual messages select the desired “Message xx” in
the measurement task tree and navigate to the details area.
General
Please refer to (→4.2.2).

Bus
This tab provides settings regarding the message itself. Here you determine the CAN ID of
the message and its DLC, which determines the data byte volume of the message.

Changesanderrorsexcepted.

140

8.2 CAN/CANFDSIGNALS

Settings for manual signals (defining a manual signal)

This part will explain how to define a manual signal.
In order to access the settings for
manual signals select the desired signal in the grid area and navigate to the details area
and select the tab “Bits”.

For instructions regarding the general signal settings please refer to the section “Details
area for CAN signals” of this manual (→8.2.4.3).

• Start bit

Define the the first bit of the signal within the datastream.

• Bit count

The bit count defines of how many bits a single sensor value of this signal is com-
posed (it defines the length of the signals in bits).

• Data format

The data format defines in which order the data bytes are sent.

Changesanderrorsexcepted.

141

8.3 PDUSIGNALS(CANFDANDFLEXRAY)

8.3 PDU signals (CAN FD and FlexRay)

As this chapter treats PDU signals on CAN FD channels as well as on
FLexRay channels, strictly speaking it treats two different types of signals.
This leads to some minor differences in screenshots of the metadata of
the importer, the import properties and the properties of the signals it-
self. However, the settings available to work with these signals and their
functionality remain the same for both signal types, therefore we will ex-
plain everything using mainly screenshots of PDU signals on CAN FD. The
insturctions for working with PDU on CAN FD and PDU on FlexRay are the
same.

8.3.1 Storage method

In order to store incoming signals on a CAN FD and FlexRay channels use one of the
following signal storage methods.

• ATFX (→ 15.7)

• MDF 4.0 (→ 15.8)

• MDF 4.1 (→ 15.9)

8.3.2 Importing PDU signals

This section explains how to import PDU signals on a CAN FD or a FlexRay channel. The
filetype associated with these signals is an “Autosar file”.

To import a PDU signal, select the CAN FD/FlexRay channel to which you wish to import
in the tree, click the “Import” button in the ribbon and then choose the
your signal
“Autosar” filetype for the import.

Changesanderrorsexcepted.

142

8.3 PDUSIGNALS(CANFDANDFLEXRAY)

The following window lets you choose which file you wish to import. According to the
filetype you have chosen earlier for your import.

Next the “Importer” window will appear, that will present you with a range of importing
options.

Figure 5: Importer with metadata for PDU on CAN FD

Changesanderrorsexcepted.

143

8.3 PDUSIGNALS(CANFDANDFLEXRAY)

Figure 6: Importer with metadata for PDU on FlexRay

In this dialog, all signals that can be imported from the description file are displayed. In
the left table, all signals, where the ”selection” checkboxes are selected, will be marked
for import. You can either choose manually, which signals to import, you can use the
“Select/Deselect all” button on the bottom left, or you can use a CSV-file to determine
which signals are to be imported, by clicking “Select by CSV” on the bottom left.

In the right table the metadata, properties of the selected signals, the control unit and
the protocol are displayed.

Once you have chosen all the signals you wish to import, click “OK” to complete the
import procedure.

Multiple description files can be imported into the same CAN FD/FlexRay
channel.

Changesanderrorsexcepted.

144

8.3 PDUSIGNALS(CANFDANDFLEXRAY)

8.3.3 Import properties

The “Import properties” of a “Description file”, “Signal message” or signal allow you to
see certain properties such as the Data format, the Adress, the Bit mask, the start bit, bit
count and more. It shows the properties as described by the description file.

Figure 7: Example for Import properties of a PDU Description file

Figure 8: Example for Import properties of a CAN FD message, that contains a PDU message

Figure 9: Example for Import properties of a FlexRay message, that contains a PDU message

Changesanderrorsexcepted.

145

8.3 PDUSIGNALS(CANFDANDFLEXRAY)

Figure 10: Example for Import properties of a PDU message

Figure 11: Example for Import properties of a PDU on CAN FD signal

Figure 12: Example for Import properties of a PDU on FlexRay signal

Changesanderrorsexcepted.

146

8.3 PDUSIGNALS(CANFDANDFLEXRAY)

Figure 13: Example for “Import properties” of a multiplexed signal

8.3.4 Signal properties

8.3.4.1 Tree elements for PDU signals

After having successfully imported the desired signals to your CAN FD/FlexRay channel,
this channel will contain three new layers of child elements in the measurement task
tree: The “Description file”-layer and the “Signal message”-layer, which is a regular CAN
message, and the “PDU message”-layer, which contains the PDU signals.

Description file
information and can be
The “description file” is a database file which contains signal
used to import those signals into a Signal channel in IPEmotion. The filetype associated
with PDU signals is the “Autosar file”.

Signal message
The “Signal message” is the CAN FD/FlexRay message, which contains the PDU message.
It can contain multiple PDU messages and there may be multiple “Signal messages” per
“description file”.

Changesanderrorsexcepted.

147

8.3 PDUSIGNALS(CANFDANDFLEXRAY)

PDU message
The “PDU message” is the data message, which contains the PDU signals. It can contain
multiple PDU signals and there may be multiple “PDU messages” per “Signal message”.

8.3.4.2 Grid area for PDU signals

In the “grid area” you will be presented with an overview of your selected CAN FD/FlexRay
channel’s signals. Also you can find here two important functions, which are the “Column
chooser” (→4.2.5) and the “Filter editor” (→4.2.6).

8.3.4.3 Details area for PDU signals

The Details area allows you to access settings for the selected signal in the grid area.
General
Please refer to (→4.2.2).

Format
This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “16-Bit integer unsigned”) and allows
you to apply special tasks for this signal such as “GPS Longitude”, “GPS Latitude”,
“UTC hour”, “Audio mono” and more.

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a signal value is read as
invalid.

Changesanderrorsexcepted.

148

8.3 PDUSIGNALS(CANFDANDFLEXRAY)

• Channel type

This field tells you whether you are dealing with a “Input” channel or “Output”
channel.

Scaling
The fields accessible directly through the tab allow for basic scaling operations to con-
vert analog measurement in engineering units. The “Scaling calculator” allows for more
refined scaling options with a large range of functions. For details on how to use the
“Scaling calculator” please refer to the IPEmotion Documentation - Section 3.4.5 “Chan-
nel configuration and scaling”.

• Sensor Mode

The sensor mode tells the type of signal. It can be of different types such as “Status”,
“Voltage”, “Frequenzy” or others.
It cannot be changed and serves for IPEmotion
to know what kind of signal it is dealing with.

• Sensor Range

Shows the raw value range of the signal.

• Physical Range

Allows you to set a range to which you would like to “scale” your signal and also
define the unit to use. For more refined scaling please use the “Scaling calculator”
and refer to the IPEmotion Documentation - Section 3.4.5 “Channel configuration
and scaling”.

Changesanderrorsexcepted.

149

8.3 PDUSIGNALS(CANFDANDFLEXRAY)

Display
This tab allows you to define what information about the current signal will be shown on a
display if one is connected.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

• Name

Allows you to set a Name to be shown on a display.

Signal
This tab allows you to define signal settings.

• Internal data type

Assign an internal data type to the signal. Available data types are “Double” and
“String”.

• Signal number

Assign a number to the current signal. This way you will
signals in the grid according to their “Signal numbers”.

later be able to sort the

• Hold last value

Specify, for how long the last value of the signal will be hold.

Changesanderrorsexcepted.

150

8.3 PDUSIGNALS(CANFDANDFLEXRAY)

• Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may here
select the dataset, to which this setting will refer.

• Timeout

Specify the timeout period for the current signal.
data for the specified time period, the value of the signal
Number)” and will be displayed as “–” in a display.

If the data source doesn’t send
is set to “NaN (Not a

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

• Special task

The field “Special task” allows you to assign a user specific task to a signal, as long as
it has not been assigned to a logger default special task in the “Format” tab yet. If a
special task such as “GPS longitude/latitude/altitude in degrees”, “Vehicle identifi-
cation” or other has been assigned, in the “Format” tab, this field remains uneditable.

For further information regarding user specific special tasks and their properties
please refer to this part of the maual (→8.2.4.3).

Signal check
This tab allows you to activate “Signal check” for this signal. You may choose whether you
wish to apply the global signal check settings to this signal or override the global settings
with settings specific for this signal.
Global signal check settings have to be defined first. For information on how to do so and
for general information on “Signal check” please refer to (→4.2.2).

Limit values
This tab allows you to define limit values for a signal and what action to take upon a limit
value violation.

• Rejected value

Define what happens to a value, that has been rejected because it is out of bound
or invalid. By default this value will be dropped. It can also be written as NaN.

Changesanderrorsexcepted.

151

8.3 PDUSIGNALS(CANFDANDFLEXRAY)

• Valid ranges (Lower/Upper)

Define up to three ranges of valid signal values. Activate a range in order to define
its upper/lower value (datatype double). Range 2 can only be activated if range 1
is and range 3 can only be activated if range 2 is.

• Invalid values (Physical/Raw)

Define up to three invalid values. Activate an invalid value in order to define the
physical value (datatype double) or raw value (datatype integer).
If one of the
two has been typed in, the other will be calculated according to the scale/offset
settings in the scaling calculator.
Invalid value 2 can only be activated if invalid value 1 is and invalid value 3 can
only be activated if invalid value 2 is.
For details on how to use the “Scaling calculator” please refer to the IPEmotion
Documentation - Section 3.4.5 “Channel configuration and scaling”.

Changesanderrorsexcepted.

152

8.4 J1939SIGNALS

8.4 J1939 signals

8.4.1 Storage method

In order to store incoming signals on a CAN channel use one of the following signal
storage methods.

• ATFX (→ 15.7)

• MDF 4.0 (→ 15.8)

• MDF 4.1 (→ 15.9)

8.4.2 Importing J1939 signals

This section explains how to import J1939 signals. J1939 signals are imported using a
CANdb file.

To import Signals, select the CAN channel to which you wish to import your signal in the
tree, click the “Import” button in the ribbon and then choose CANdb as the type of
“description file”. For more information on the “description file” refer to (→8.4.4.1).

Changesanderrorsexcepted.

153

8.4 J1939SIGNALS

The following window lets you choose which file you wish to import. Choose your J1939
file and click “Open”.

Once you have opened your file, the “Importer” window will appear, that will present
you with a range of importing options.

In this dialog, all signals that can be imported from the description file are displayed. In
the left table, all signals, where the ”selection” checkboxes are selected, will be marked
for import. You can either choose manually, which signals to import, you can use the
“Select/Deselect all” button on the bottom left, or you can use a CSV-file to determine
which signals are to be imported, by clicking “Select by CSV” on the bottom left.

In the right table the metadata, properties of the selected signals, the control unit and
the protocol are displayed.

Changesanderrorsexcepted.

154

8.4 J1939SIGNALS

Once you have choosen all the signals you wish to import, click “OK” to complete the
import procedure.

Compared to importing any other kind of signal, the importer for J1939
signals provides the user with an extra funtionality. As one can see in
the figure above, the importer possesses some extra columns for J1939
signals. The column labeled “SPN” is read only and tells the user, whether
the respective signal possesses additional status signals. If so, there are
three different types of status signals:

• Status

• FMI (Failure mod identifier)

• OC (occurrence counter)

Marking active any of these status signals will import them under the tree
element labeled “DM1” (diagnostic message).

Multiple description files can be imported into the same CAN channel.

Changesanderrorsexcepted.

155

8.4 J1939SIGNALS

8.4.3 Import properties

The “Import properties” of a description file, Message or signal allow you to see certain
properties such as the Data format, The CAN identifier, the Bit mask, the start bit, bit count
and more. It shows the signal’s properties as described by the description file.

Figure 14: Example for “Import properties” of a J1939 description file

Figure 15: Example for “Import properties” of a J1939 Message

Figure 16: Example for “Import properties” of a J1939 signal

Changesanderrorsexcepted.

156

8.4 J1939SIGNALS

Figure 17: Example for “Import properties” of a multiplexed signal
To access the “Import properties” rightclick on any desired description file, Message or
signal and then choose “Import properties” from the resulting context menu.

Changesanderrorsexcepted.

157

8.4 J1939SIGNALS

8.4.4 Signal properties

8.4.4.1 Tree elements for J1939 signals

After having successfully imported the desired signals to your CAN channel, this channel
will contain two new layers of child elements in the measurement task tree: The “Descrip-
tion file” and the “Messages” containing the signals.

Description file
The “description file” is a database file which contains signal
information and can be
used to import those signals into a Signal channel in IPEmotion. The filetypes which are
supported by the CAETEC Plugin for IPEmotion depend on the type of signal you wish to
import.

The symbol in the left part of the tree element shows you the type of “description file” you
imported (in this case a “DBC” file), then follows the name of the imported “description
file” (in this case “IPEmotionDemo”).

Message
Each “description file” can contain one or more “Messages” (in this case 5), which then
contains the actual signals. A “Message” can be found in the “Measurement task tree”
as a child element of the “description file”, it belongs to.
Each “Message” can, again, contain one or more signals.

In the case of J1939, there are two special “Messages”, labeled “Status” and “DM1”. The
“Status” message contains the “DTC count”, whereas the “DM1” message contains all
the other status signals of the J1939 description file, including the additionally imported
status signals for signals with SPN capability.

DTC stands for “Diagnostic trouble code” and the DTC count tells how many incidents
labeled with a dtc the logger receives.

Changesanderrorsexcepted.

158

8.4 J1939SIGNALS

8.4.4.2 Grid area for J1939 signals

In the “grid area” you will be presented with an overview of your selected CAN channel’s
signals. Also you can find here two important functions, which are the “Column chooser”
(→4.2.5) and the “Filter editor” (→4.2.6).

8.4.4.3 Details area for J1939 signals

The settings for J1939 signals contained in the details area are mainly identical to those of
regular CAN signals. Therefore please refer to the chapter “Details area for CAN signals”
(→8.2.4.3) for detailed description of the available settings.

There is, however, one setting regarding the details are, that is specific for J1939 signals,
the conversion method, which will be described in the following.

Settings
When selecting the tree element “DM1”, the settings tab of the details area contains the
setting “Conversion method”. The four different “Conversion methods” each define a
different dtc (diagnostic trouble code) byte order for conversion methods with the value
“1”.

Changesanderrorsexcepted.

159

8.5 CCP/XCPSIGNALS

8.5 CCP/XCP signals

8.5.1 Storage method

In order to store incoming signals on a CAN channel use one of the following signal
storage methods.

• ATFX (→ 15.7)

• MDF 4.0 (→ 15.8)

• MDF 4.1 (→ 15.9)

8.5.2 Importing CCP/XCP signals

This section explains how to import CCP or XCP signals. The filetype associated with these
signals is a “A2L file”.

To import a CCP/XCP signal, select the CAN channel to which you wish to import your
signal
in the tree, click the “Import” button in the ribbon and then choose the “A2L”
filetype for the import.

Changesanderrorsexcepted.

160

8.5 CCP/XCPSIGNALS

The following window lets you choose which file you wish to import. According to the
filetype you have chosen earlier for your import, you will now only be able to choose files
of the “A2L” filetype. Choose the file you wish to import and click “Open”.

The following window lets you choose whether you want to import a “CCP” signal or a
“XCP” signals. Choose the protocol you wish to import and click “OK”.

Once you have chosen the protocoll and confirmed, the “Importer” window will appear,
that will present you with a range of importing options.
In this dialog, all signals that can be imported from the description file are displayed. In
the left table, all signals, where the ”selection” checkboxes are selected, will be marked
for import. You can either choose manually, which signals to import, you can use the
“Select/Deselect all” button on the bottom left, or you can use a CSV-file to determine
which signals are to be imported, by clicking “Select by CSV” on the bottom left.

In the right table the metadata, properties of the selected signals, the control unit and
the protocol are displayed.

Changesanderrorsexcepted.

161

8.5 CCP/XCPSIGNALS

Once you have choosen all the signals you wish to import, click “OK” to complete the
import procedure.

Depending on the protocol, a sampling rate or the DAQ list to use, can
be assigned to the signals.
In the case of a protocol using DAQ lists (CCP, XCP), you can specify
via the column selection dialog, if the signals are configured by the
sampling rate or a DAQ list. To achieve this you should open the column
selection dialog, via the context menu of the table header, and then
drag the desired column (”sampling” or ”DAQ list”) from the column
selection dialog to the table header.
The other column is removed
automatically.
If in a protocol based on DAQ lists, sampling rates are used for the signal
configuration, during import the signals are assigned to the available
DAQ list with the most suitable sampling rate.
In case of a pre-
As of V18.02.00 predefined DAQ lists are supported.
defined DAQ-list the ECU provides the available signals defined by said
DAQ list. It is not possible for the user to customize which signals should
be requested by the DAQ list.
In case of protocols supporting array signals, you can specify via the
”split array” column whether all the signals of the array or just the first to
be imported. If this column does not appear it can be moved from the
column selection dialog into the table.

Changesanderrorsexcepted.

162

8.5 CCP/XCPSIGNALS

Multiple description files can be imported into the same CAN channel.

8.5.3 Importing XCP signals on CAN FD

This section explains how to import XCP signals on a CAN FD channel.
associated with these signals is a “A2L file”.

The filetype

To import an XCP signal, select the CAN FD channel to which you wish to import your
signal
in the tree, click the “Import” button in the ribbon and then choose the “A2L”
filetype for the import.

If an XCP database is imported into a CAN FD channel, the target CAN
channel’s settings will automatically be set to use compatible settings.
These settings can be found here (→8.1.3.3).

Changesanderrorsexcepted.

163

8.5 CCP/XCPSIGNALS

The following window lets you choose which file you wish to import. According to the
filetype you have chosen earlier for your import, you will now only be able to choose files
of the “A2L” filetype. Choose the file you wish to import and click “Open”.

The following window lets you choose which protocol you wish to use for signal import.
Choose XCPonCAN FD and click “OK”.

Changesanderrorsexcepted.

164

8.5 CCP/XCPSIGNALS

Now you will be presented with a range of XCPonCAN FD specific settings. After having
set these settings, confirm with “OK”.

Once you have confirmed the settings, the “Importer” window will appear, that will
present you with a range of importing options.

In this dialog, all signals that can be imported from the description file are displayed. In
the left table, all signals, where the ”selection” checkboxes are selected, will be marked
for import. You can either choose manually, which signals to import, you can use the
“Select/Deselect all” button on the bottom left, or you can use a CSV-file to determine
which signals are to be imported, by clicking “Select by CSV” on the bottom left.

In the right table the metadata, properties of the selected signals, the control unit and
the protocol are displayed.

Changesanderrorsexcepted.

165

8.5 CCP/XCPSIGNALS

Once you have choosen all the signals you wish to import, click “OK” to complete the
import procedure.

Depending on the protocol, a sampling rate or the DAQ list to use, can
be assigned to the signals.
In the case of a protocol using DAQ lists (CCP, XCP), you can specify
via the column selection dialog, if the signals are configured by the
sampling rate or a DAQ list. To achieve this you should open the column
selection dialog, via the context menu of the table header, and then
drag the desired column (”sampling” or ”DAQ list”) from the column
The other column is removed
selection dialog to the table header.
automatically.
If in a protocol based on DAQ lists, sampling rates are used for the signal
configuration, during import the signals are assigned to the available
DAQ list with the most suitable sampling rate.
As of V18.02.00 predefined DAQ lists are supported.
In case of a pre-
defined DAQ-list the ECU provides the available signals defined by said
DAQ list. It is not possible for the user to customize which signals should
be requested by the DAQ list.
In case of protocols supporting array signals, you can specify via the
”split array” column whether all the signals of the array or just the first to
be imported. If this column does not appear it can be moved from the
column selection dialog into the table.

Multiple description files can be imported into the same CAN FD chan-
nel.

Changesanderrorsexcepted.

166

8.5 CCP/XCPSIGNALS

8.5.4 Import properties

The “Import properties” of an “ECU”, “Description file”, “Polling list”, “DAQ list” or signal
allow you to see certain properties such as the Data format, the Adress, the Bit mask, the
start bit, bit count and more. It shows the properties as described by the description file.

Figure 18: Example for Import properties of a CCP/XCP ECU

Changesanderrorsexcepted.

167

8.5 CCP/XCPSIGNALS

Figure 19: Example for Import properties of a CCP/XCP Description file

Changesanderrorsexcepted.

168

8.5 CCP/XCPSIGNALS

Figure 20: Example for Import properties of a CCP/XCP Polling list

Changesanderrorsexcepted.

169

8.5 CCP/XCPSIGNALS

Figure 21: Example for signal properties of a CCP/XCP DAQ list

Changesanderrorsexcepted.

170

8.5 CCP/XCPSIGNALS

Figure 22: Example for Import properties of a CCP/XCP signal

Figure 23: Example for “Import properties” of a multiplexed signal

8.5.5 Signal properties

8.5.5.1 Tree elements for CCP/XCP signals

After having successfully imported the desired signals to your CAN channel, this channel
will contain three new layers of child elements in the measurement task tree: The “ECU”-
layer, the “Description file”-layer and the “Message”-layer.

ECU
The “ECU” (Electronic control unit) represents the control unit inside the vehicle that the
logger communicates with. It allows for an active communication between logger and
vehicle, where the logger can not only receive messages but also send messages.

Changesanderrorsexcepted.

171

8.5 CCP/XCPSIGNALS

Description file (Station)
The “description file” (also called station in case of CCP/XCP) is a database file which
contains signal information and can be used to import those signals into a Signal channel
in IPEmotion. The filetype associated with CCP/XCP signals is the “A2L file”.

The symbol in the left part of the tree element shows you the type of “database” you
imported (CCP or XCP), then follows the name of the imported “description file” (in this
case “IPEmotionDemo”) and on the right is a number indicating how many signals the
“description file” contains (in this case 15).

Changesanderrorsexcepted.

172

8.5 CCP/XCPSIGNALS

Signal lists
Each “description file” can contain one or more Signal lists, which then contain the actual
signals. A Signal list can be found in the “Measurement task tree” as a child element of
the “description file”, it belongs to.
Each Signal list can, again, contain one or more signals, which is indicated by the number
on the right of the Signal list’s name.

CCP/XCP Signal lists group the “description file’s” signals in groups with different function-
alities. The groups differ in the way that the logger obtains or requests a signal.

• Status list

The status list contains signals on the ECU status and the status of DAQ lists included
in the description file. Each signal list has two entries. “Configured” gives information
whether the list has been configured, “started” gives information whether the
respective list has been started and is running or not.
“Station connected” tells you whether the respective ECU is connected and “EPK
Versioncheck result” lets you know whether the “EPK check” has been passed
successfully or not.

Station connected
Tells you the status of the connection with the respective ECU.

NaN = not started The ECU has not been started.
0 = failed
1 = successful

The ECU has been started but the connection test has failed.
The ECU has been started and the connection test has been
passed successfully.

EPK Versioncheck result
Tells you about the result of the “EPK check”.

NaN = not started The “EPK check” has not been performed.
0 = failed
1 = successful

The “EPK check” has been performed but not passed.
The “EPK check” has been performed and passed successfully.

Changesanderrorsexcepted.

173

8.5 CCP/XCPSIGNALS

xxx_ms_task_configured
Tells you whether the respective DAQ list has been configured.

0 = not yet configured The DAQ list has not yet been configured.
1 = successful

The DAQ list has been configured.

xxx_ms_task_started
Tells you whether the respective DAQ list has been started.

0 = not yet started The DAQ list has not been started. It is inactive.
1 = successful

The DAQ list has been started.

• Polling list

Signals contained in a “Polling list”, will be actively requested by the logger. That
means, for each signal a sampling rate has to be defined, according to which the
logger will request the signals which will then be sent to the logger by the ECU.

• DAQ list

Signals contained in a “DAQ list” are assigned with a certain time intervall in which
the ECU is requested to send these signals. I.e. any signal contained in the DAQ list
“100ms sync event channel” will be sent to the logger in an intervall of 100ms. This
guarantees that there is no unintended delay.

8.5.5.2 Grid area for CCP/XCP signals

In the “grid area” you will be presented with an overview of your selected CAN channel’s
signals. Also you can find here two important functions, which are the “Column chooser”
(→4.2.5) and the “Filter editor” (→4.2.6).

8.5.5.3 Details area for CCP/XCP signals

The Details area shows settings either for the selected tree element (“ECU”,“description
file” or “signal list”) or the selected signal in the grid area.

• “ECU” selected

In this case the details area will only show the “General” tab. Please refer to (→4.2.2).

Changesanderrorsexcepted.

174

8.5 CCP/XCPSIGNALS

• “description file/station” selected

In this case the details area will contain the “General” tab (→4.2.2) plus additional
tabs.

CCP/XCP
This tab contains CCP and XCP specific options.

◦ Resume active

Activates the start of sending data by the ECU without the need of an initial-
ization. Thereto the configuration is transmitted into the flash of ECU once and
stays there, so that the configuration is stil available after power loss.

◦ Seed & Key

This field allows you to enter a Seed & Key binary file (*.skb) which contains the
information required to unlock the ECU if necessary.

◦ EPK check

Checks for differences in the chekcsums of the current configuration and the
ECU.

◦ Use optional commands (CCP only)

If marked active, the optional commands defined in the ECU file will be used.

Fixed Seed & Key
If no Seed & Key file has been specified, this tab allows you to define fixed Seed &
Key settings to be used.

◦ Use fixed value

If marked active, a fixed Seed & Key value will be used. The value has to be

Changesanderrorsexcepted.

175

8.5 CCP/XCPSIGNALS

defined below.

◦ Fixed key value

Define the fixed Seed & Key value. The button on the right allows to switch
between decimal, hexadecimal or binary mode.

◦ Fixed key length

The dropdown menu allows you to define the byte length of the fixed Seed &
Key value.

EPK
This tab allows for EPK settings.

◦ Checking mode

The dropdown menu allows you to choose the checking mode. It can be either
“EPK” or “GetID”. “GetID” is only available for XCP.

◦ GetID Identifier

Define the identifier for the GetID mode. The identifier is a string that corre-
It can be found under “EPK
sponds to the ECU’s software version number.
identification” by right-clicking on the ECU in the tree and then clicking “Import
properties”.

◦ Action at failure

Allows you to define what action to take upon an EPK check failure. Regardless
of the selected option the logger will always write an EPK check failure logging
message.

Changesanderrorsexcepted.

176

8.5 CCP/XCPSIGNALS

Extended
This tab allows for extended settings.

◦ Detection second tester CMD

Allows you to activate the detection of a second tester by commands on the
bus.

◦ Detection second tester DAQ

Allows you to activate the detection of a second tester by an existing DAQ
setup.

◦ Synchronize DAQ start

Allows you to activate or deactivate the synchronization of the start of all
DAQ-lists.

◦ Use settings from station (XCP only)

from the XCP station.

If activated, the logger tries to receive settings (such as DAQ lists, polling lists
If the logger successfully receives the settings
etc.)
from the station, he will then use these to overwrite the settings in the logger
configuration.

◦ BRS (Bit Rate Switch; XCP on CAN FD only)

This setting allows you to activate the “Bit Rate Switch” for outgoing messages
from the logger on XCP.

Changesanderrorsexcepted.

177

8.5 CCP/XCPSIGNALS

Trigger
This tab allows to define a trigger in order to stop or start the entire station. Stopping
the station means disconnecting from it. No data will be received from the station. In
order to stop/start single signals or signal groups, the trigger function of the daq-lists
has to be used.

◦ Mode

Define whether you wish to continuously acquire data or if you want to start/stop
data acquisition via a trigger. There are two modes to control data acqusition
via trigger:

Start and stop trigger allows you to set any previously defined trigger as start
and/or stop condition.

Stop is inverted start will acquire data as long as the start trigger condition is
met. Once it is no longer met, data acquisition will stop.

◦ Start-trigger

Allows you to choose a trigger upon whose activation the station will be
CONNECTED. A trigger has first to be defined. Please refer to (→10).

◦ Stop-trigger

Allows you to choose a trigger upon whose activation the station will be
DISCONNECTED. A trigger has first to be defined. Please refer to (→10).
If there is no “Stop-trigger” defined the acquisition will be stopped by inverted
start condition.

• “Polling list” or “DAQ list” selected

In this case the details area will additionally contain the “Trigger tab”. The “Trigger
tab” allows you to set a trigger upon whose activation the signals contained in the
list will be requested.

Changesanderrorsexcepted.

178

8.5 CCP/XCPSIGNALS

◦ Mode

Define whether you wish to continuously acquire data or if you want to start/stop
data acquisition via a trigger. There are two modes to control data acqusition
via trigger:

Start and stop trigger allows you to set any previously defined trigger as start
and/or stop condition.

Stop is inverted start will acquire data as long as the start trigger condition is
met. Once it is no longer met and a possibly set Post-trigger duration has run
out, data acquisition will stop.

◦ Start-trigger

Allows you to choose a trigger upon whose activation the list’s Signals will be
requested. A trigger has first to be defined. Please refer to (→10).

◦ Stop-trigger

Allows you to choose a trigger upon whose activation the list’s Signals will stop
being requested. A trigger has first to be defined. Please refer to (→10).
If there is no “Stop-trigger” defined the acquisition will be stopped by inverted
start condition.

◦ Post-trigger duration

You can determine here for how long after a stop request (either by explicit
“Stop-trigger” or inverted start condition) the stop will be delayed and data
acquisition will continue.

• Signal selcted

In this case the details area will contain additional tabs which will be explained in
the following.

General
Please refer to (→4.2.2).

Format
This tab contains information and options regarding file format, tasks and Channel

Changesanderrorsexcepted.

179

8.5 CCP/XCPSIGNALS

type.

◦ Data type

This field tells you the type of data (in this case “8-Bit integer unsigned”) and
allows you to apply special tasks for this signal such as “GPS Longitude”, “GPS
Latitude”, “UTC hour”, “Audio mono” and more.

◦ NoValue / DefaultValue

This field allows you to define the value that will be shown if a signal value is
read as invalid.

◦ Channel type

This field tells you whether you are dealing with a “Input” channel or “Output”
channel.

Scaling
The fields accessible directly through the tab allow for basic scaling operations to
convert analog measurement in engineering units. The “Scaling calculator” allows
for more refined scaling options with a large range of functions. For details on how to
use the “Scaling calculator” please refer to the IPEmotion Documentation - Section
3.4.5 “Channel configuration and scaling”.

◦ Sensor Mode

The sensor mode tells the type of signal.
“Status”, “Voltage”, “Frequenzy” or others.
for IPEmotion to know what kind of signal it is dealing with.

It can be of different types such as
It cannot be changed and serves

◦ Sensor Range

Shows the raw value range of the signal.

Changesanderrorsexcepted.

180

8.5 CCP/XCPSIGNALS

◦ Physical Range

Allows you to set a range to which you would like to “scale” your signal and
also define the unit to use. For more refined scaling please use the “Scaling
calculator” and refer to the IPEmotion Documentation - Section 3.4.5 “Channel
configuration and scaling”.

Changesanderrorsexcepted.

181

8.5 CCP/XCPSIGNALS

Display
This tab allows you to define what information about the current signal will be shown
on a display if one is connected.

◦ Displaying area

Shows the value range which will be shown on a display. It usually should match
the “Physical range” from the “Scaling” tab.

◦ Formatting

The dropdown menu “Decimal places” allows you to set how many decimal
numbers of the value will be shown on a display.

◦ Name

Allows you to set a Name to be shown on a display.

Limit values
This tab allows you to define limit values for a signal and what action to take upon a
limit value violation.

◦ Rejected value

Define what happens to a value, that has been rejected because it is out of
bound or invalid. By default this value will be dropped. It can also be written as
NaN.

◦ Valid ranges (Lower/Upper)

Define up to three ranges of valid signal values. Activate a range in order to
define its upper/lower value (datatype double). Range 2 can only be activated

Changesanderrorsexcepted.

182

8.5 CCP/XCPSIGNALS

if range 1 is and range 3 can only be activated if range 2 is.

◦ Invalid values (Physical/Raw)

Define up to three invalid values. Activate an invalid value in order to define
the physical value (datatype double) or raw value (datatype integer).
If one
of the two has been typed in, the other will be calculated according to the
scale/offset settings in the scaling calculator.
Invalid value 2 can only be activated if invalid value 1 is and invalid value 3 can
only be activated if invalid value 2 is.
For details on how to use the “Scaling calculator” please refer to the IPEmotion
Documentation - Section 3.4.5 “Channel configuration and scaling”.

Signal
This tab allows you to define signal settings.

◦ Signal number

Assign a number to the current signal. This way you will later be able to sort the
signals in the grid according to their “Signal numbers”.

◦ Hold last value

Specify, for how long the last value of the signal will be hold.

◦ Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may
here select the dataset, to which this setting will refer.

◦ Timeout

If the data source doesn’t
Specify the timeout period for the current signal.
send data for the specified time period, the value of the signal is set to “NaN
(Not a Number)” and will be displayed as “–” in a display.

◦ Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

Signal check
This tab allows you to activate “Signal check” for this signal. You may choose
whether you wish to apply the global signal check settings to this signal or override

Changesanderrorsexcepted.

183

8.5 CCP/XCPSIGNALS

the global settings with settings specific for this signal.
Global signal check settings have to be defined first. For information on how to do
so and for general information on “Signal check” please refer to (→4.2.2).

8.5.6 A2L to Cfginclude converter

The “A2L to Cfginclude converter” allows to convert an A2L database into a cfginclude
file. This is necessary when working with multiple versions of the same A2L database in
order to maintain access for the logger to older/newer versions of the same database.
In that case you may convert older/newer versions of the A2L database into a cfginclude
file and store them in one folder, thus creating a kind of library of all the available versions
of an A2L database. The logger will then be able to access this library and make use of
the various versions of the A2l stored within.

The “A2L to Cfginclude converter” contains the following three functions:

• Convert .a2l to .cfginclude (→8.5.6.1)

• Compare two .a2l files (→8.5.6.2)

• Decompress .cfginclude (→8.5.6.3)

8.5.6.1 Convert .a2l to .cfginclude

In order to convert an A2L file, import it to the desired channel (for instructions on import-
ing A2L databases please go here →8.5.2), right click on the ECU in the measurement
task tree, navigate to “Functions” and select “Convert .a2l to .cfginclude”.

In the next window choose the A2L file you wish to convert and confirm with “Open”.

Changesanderrorsexcepted.

184

8.5 CCP/XCPSIGNALS

The following window lets you set the destination for the exported cfginclude file.

This window also provides a second, very important option.
It lets you choose, whether
the exported file should be a plain text file or a zlib compressed file and whether you
want to save it as a *.cfginclude file or as a *.ccmi container, which will then contain the
*.cfgginclude file.

• “Zlib compressed” files are compressed and optimized for readability by the logger,
so they require less resources from the logger to be processed. This is the recom-
mended format for normal use.

• “Plain text” files are not compressed and optimized for human readability. They are

mainly intended for bug fixing purposes.

After choosing the path, filename and format, confirm with “Save”.
well, there will be no message. You can then find the file in the specified location.

If everything went

If there is a problem, that will result in an error message looking something like this.

Changesanderrorsexcepted.

185

8.5 CCP/XCPSIGNALS

8.5.6.2 Compare two .a2l files

In order to compare two A2L files, import one into a channel (for instructions on importing
A2L databases please go here →8.5.2), right click on the ECU in the measurement task
tree, navigate to “Functions” and select “Compare two .a2l files”.

In the next step the same window will appear twice. In the first choose the first of the two
files you wish to compare and confirm and then choose the second file and confirm.

You will then be presented with an overview of the result, which at the end tell you
whether there is any error or whether the two compared A2L files are compatible.

Changesanderrorsexcepted.

186

8.5 CCP/XCPSIGNALS

8.5.6.3 Decompress .cfginclude

This function allows you to decompress a .cfginclude file, that has previously been
exported in the zlib compressed format and convert it into a plain text format.

In order to do so, import an A2L file into a channel (for instructions on importing A2L
databases please go here →8.5.2), right click on the ECU in the measurement task tree,
navigate to “Functions” and select “Decompress .cfginclude”.

In the resulting window choose a zlib compressed *.cfginclude/*.ccmi file, which you
would like to decompress and confirm with “Open”.

In the next window specify the filename and the path for the decompressed plain text
*.cfginclude/*.ccmi file and confirm with “Save”.

Changesanderrorsexcepted.

187

8.6 UDSSIGNALS

You will now find your decompressed plain text *.cfginclude/*.ccmi file in the specified
filepath.

8.6 UDS signals

8.6.1 Storage method

In order to store incoming signals on a CAN channel use one of the following signal
storage methods.

• ATFX (→ 15.7)

• MDF 4.0 (→ 15.8)

• MDF 4.1 (→ 15.9)

8.6.2 Importing UDS signals

This section explains how to import UDS signals. The filetype associated with these signals
is a “XML/PDX file”.

To import a UDS signal, select the CAN channel to which you wish to import your signal in
the tree, click the “Import” button in the ribbon and then choose the “UDS” filetype for
the import.

Changesanderrorsexcepted.

188

8.6 UDSSIGNALS

If at signal import a CAN FD signal is recognized, the target CAN chan-
nel’s settings will automatically be set to use CAN FD compatible settings.
These settings can be found here (→8.1.3.3).

Changesanderrorsexcepted.

189

8.6 UDSSIGNALS

The following window lets you choose which file you wish to import. According to the
filetype you have chosen earlier for your import, you will now only be able to choose files
of the “XML/PDX” filetype. Choose the file you wish to import and click “Open”.

Next the “Importer” window will appear, that will present you with a range of importing
options.

In this dialog, all signals that can be imported from the description file are displayed. In
the left table, all signals, where the ”selection” checkboxes are selected, will be marked
for import. You can either choose manually, which signals to import, you can use the
“Select/Deselect all” button on the bottom left, or you can use a CSV-file to determine
which signals are to be imported, by clicking “Select by CSV” on the bottom left.

In the right table the metadata, properties of the selected signals, the control unit and
the protocol are displayed.

Changesanderrorsexcepted.

190

8.6 UDSSIGNALS

Once you have choosen all the signals you wish to import, click “OK” to complete the
import procedure.

Multiple description files can be imported into the same CAN channel.

8.6.3 Import properties

The “Import properties” of an “ECU”, “Description file” or signal allow you to see certain
properties such as the Data format, the Adress, the Bit mask, the start bit, bit count and
more. It shows the properties as described by the description file.

Figure 24: Example for Import properties of a UDS ECU

Figure 25: Example for Import properties of a UDS Description file

Changesanderrorsexcepted.

191

8.6 UDSSIGNALS

Figure 26: Example for Import properties of a UDS signal

Figure 27: Example for “Import properties” of a multiplexed signal

8.6.4 Signal properties

8.6.4.1 Tree elements for UDS signals

After having successfully imported the desired signals to your CAN channel, this channel
will contain two new layers of child elements in the measurement task tree: The “ECU”-
layer and the “Description file”-layer.

ECU
The “ECU” (Electronic control unit) represents the control unit inside the vehicle that the
logger communicates with. It allows for an active communication between logger and
vehicle, where the logger can not only receive messages but also send messages.

Description file
The “description file” is a database file which contains signal
information and can be
used to import those signals into a Signal channel in IPEmotion. The filetype associated
with UDS signals is the “UDS file”.

The symbol
in the left part of the tree element shows you the name of the imported
“description file” (in this case “IPEmotionDemo”) and on the right is a number indicating
how many signals the “description file” contains (in this case 10).

Changesanderrorsexcepted.

192

8.6 UDSSIGNALS

8.6.4.2 Grid area for UDS signals

In the “grid area” you will be presented with an overview of your selected CAN channel’s
signals. Also you can find here two important functions, which are the “Column chooser”
(→4.2.5) and the “Filter editor” (→4.2.6).

8.6.4.3 Details area for UDS signals

The Details area allows you to access settings for the selected signal in the grid area.
General
Please refer to (→4.2.2).

Format
This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “16-Bit integer unsigned”) and allows
you to apply special tasks for this signal such as “GPS Longitude”, “GPS Latitude”,
“UTC hour”, “Audio mono” and more.

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a signal value is read as
invalid.

• Channel type

This field tells you whether you are dealing with a “Input” channel or “Output”
channel.

Changesanderrorsexcepted.

193

8.6 UDSSIGNALS

Scaling
The fields accessible directly through the tab allow for basic scaling operations to con-
vert analog measurement in engineering units. The “Scaling calculator” allows for more
refined scaling options with a large range of functions. For details on how to use the
“Scaling calculator” please refer to the IPEmotion Documentation - Section 3.4.5 “Chan-
nel configuration and scaling”.

• Sensor Mode

The sensor mode tells the type of signal. It can be of different types such as “Status”,
It cannot be changed and serves for IPEmotion
“Voltage”, “Frequenzy” or others.
to know what kind of signal it is dealing with.

• Sensor Range

Shows the raw value range of the signal.

• Physical Range

Allows you to set a range to which you would like to “scale” your signal and also
define the unit to use. For more refined scaling please use the “Scaling calculator”
and refer to the IPEmotion Documentation - Section 3.4.5 “Channel configuration
and scaling”.

Display
This tab allows you to define what information about the current signal will be shown on a
display if one is connected.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

Changesanderrorsexcepted.

194

8.6 UDSSIGNALS

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

• Name

Allows you to set a Name to be shown on a display.

Limit values
This tab allows you to define limit values for a signal and what action to take upon a limit
value violation.

• Rejected value

Define what happens to a value, that has been rejected because it is out of bound
or invalid. By default this value will be dropped. It can also be written as NaN.

• Valid ranges (Lower/Upper)

Define up to three ranges of valid signal values. Activate a range in order to define
its upper/lower value (datatype double). Range 2 can only be activated if range 1
is and range 3 can only be activated if range 2 is.

• Invalid values (Physical/Raw)

Define up to three invalid values. Activate an invalid value in order to define the
If one of the
physical value (datatype double) or raw value (datatype integer).
two has been typed in, the other will be calculated according to the scale/offset
settings in the scaling calculator.
Invalid value 2 can only be activated if invalid value 1 is and invalid value 3 can
only be activated if invalid value 2 is.
For details on how to use the “Scaling calculator” please refer to the IPEmotion
Documentation - Section 3.4.5 “Channel configuration and scaling”.

Changesanderrorsexcepted.

195

8.6 UDSSIGNALS

Signal
This tab allows you to define signal settings.

• Internal data type

Assign an internal data type to the signal. Available data types are “Double” and
“String”.

• Signal number

Assign a number to the current signal. This way you will
signals in the grid according to their “Signal numbers”.

later be able to sort the

• Hold last value

Specify, for how long the last value of the signal will be hold.

• Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may here
select the dataset, to which this setting will refer.

• Timeout

Specify the timeout period for the current signal.
data for the specified time period, the value of the signal
Number)” and will be displayed as “–” in a display.

If the data source doesn’t send
is set to “NaN (Not a

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

• Special task

The field “Special task” allows you to assign a user specific task to a signal, as long as
it has not been assigned to a logger default special task in the “Format” tab yet. If a
special task such as “GPS longitude/latitude/altitude in degrees”, “Vehicle identifi-
cation” or other has been assigned, in the “Format” tab, this field remains uneditable.

For further information regarding user specific special tasks and their properties
please refer to this part of the maual (→8.2.4.3).

Changesanderrorsexcepted.

196

8.6 UDSSIGNALS

Signal check
This tab allows you to activate “Signal check” for this signal. You may choose whether you
wish to apply the global signal check settings to this signal or override the global settings
with settings specific for this signal.
Global signal check settings have to be defined first. For information on how to do so and
for general information on “Signal check” please refer to (→4.2.2).

Changesanderrorsexcepted.

197

8.7 OBDSIGNALS

8.7 OBD signals

8.7.1 Storage method

In order to store all
storage. Please refer to (→ 15.10).

incoming traffic on a CAN channel use a bus tracing method for

8.7.2 Adding the OBD signals interface

This section explains how to work with OBD (On-Board diagnosis) signals.

In order to work with “OBD signals”, you will first need to add the “OBD signals” interface,
which will contain all the available “OBD signals”. To do so, select a CAN channel in the
tree, click the “Components” button in the Ribbon and then choose “OBD-2”.

8.7.3 User-defined OBD signals

It is possible to define a user-specific “OBD signal”. To do so, select the “OBD signals”
interface in the measurement task tree, click the “Components” button in the Ribbon
and then choose “User-defined OBD signal”.

Changesanderrorsexcepted.

198

8.7 OBDSIGNALS

8.7.4 Signal properties

8.7.4.1 Tree elements for OBD signals

After having added the “OBD signals” interface, it will appear in the measurement task
tree as a ne tree element.

8.7.4.2 Grid area for OBD signals

In the “grid area” you will be presented with an overview of all the available “OBD signals”.
Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

Changesanderrorsexcepted.

199

8.7 OBDSIGNALS

8.7.4.3 Details area for OBD signals

The Details area allows you to access settings either for the “OBD signals” interface or for
the selected “OBD signal” in the grid area.

If the interface has been selected in the measurement task tree, the details area will
contain two tabs.

General
Please refer to (→4.2.2).

KWP station
Define the request and respond CAN ID of the addressed ECU.

• Request CAN ID

The Request CAN ID is typically between 7E0h and 7E7h.

• Respond CAN ID

The Respond CAN ID is typically between 7E8h and 7EFh.

Changesanderrorsexcepted.

200

8.7 OBDSIGNALS

If a signal has been selected in the Grid area, the details area will contain the following
tabs.

General
Please refer to (→4.2.2).

Format
This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “8-bit integer unsigned”) and allows
you to apply special tasks for this formula/signal such as “GPS Longitude”, “GPS Lat-
itude”, “UTC hour”, “Audio mono” and more.

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a formula/signal value is
read as invalid.

Changesanderrorsexcepted.

201

8.7 OBDSIGNALS

Scaling
The fields accessible directly through the tab allow for basic scaling operations to con-
vert analog measurement in engineering units. The “Scaling calculator” allows for more
refined scaling options with a large range of functions. For details on how to use the
“Scaling calculator” please refer to the IPEmotion Documentation - Section 3.4.5 “Chan-
nel configuration and scaling”.

• Sensor Mode

The sensor mode tells the type of signal. It can be of different types such as “Status”,
“Voltage”, “Frequenzy” or others. It cannot be changed and serves for IPEmotion to
know what kind of signal it is dealing with.

• Sensor Range

Shows the raw value range of the signal.

• Physical Range

Allows you to set a range to which you would like to “scale” your signal and also
define the unit to use. For more refined scaling please use the “Scaling calculator”
and refer to the IPEmotion Documentation - Section 3.4.5 “Channel configuration
and scaling”.

Display
This tab allows you to define what information about the current signal will be shown on a
display if one is connected.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal numbers
of the value will be shown on a display.

Changesanderrorsexcepted.

202

8.7 OBDSIGNALS

• Name

Allows you to set a Name to be shown on a display.

Trigger
This tab provides settings regarding the trigger for the start and stop of data acquisition on
this channel.

• Mode

Define whether you wish to continuously acquire data or if you want to start/stop
data acquisition via a trigger. There are two modes to control data acqusition via
trigger:

Start and stop trigger allows you to set any previously defined trigger as start and/or
stop condition.

Stop is inverted start will acquire data as long as the start trigger condition is met.
Once it is no longer met and a possibly set Post-trigger duration has run out, data
acquisition will stop.

• Start-trigger

Define a trigger, that will start data acquisition.

• Stop-trigger

Define a trigger, that will stop data acquisition.

• Post-trigger duration

Post-trigger duration allows you to define, how long after the start trigger was set,
data acquisition will stop.

Changesanderrorsexcepted.

203

8.7 OBDSIGNALS

Limit values
This tab allows you to define limit values for a signal and what action to take upon a limit
value violation.

• Rejected value

Define what happens to a value, that has been rejected because it is out of bound
or invalid. By default this value will be dropped. It can also be written as NaN.

• Valid ranges (Lower/Upper)

Define up to three ranges of valid signal values. Activate a range in order to define
its upper/lower value (datatype double). Range 2 can only be activated if range 1
is and range 3 can only be activated if range 2 is.

• Invalid values (Physical/Raw)

Define up to three invalid values. Activate an invalid value in order to define the
physical value (datatype double) or raw value (datatype integer).
If one of the
two has been typed in, the other will be calculated according to the scale/offset
settings in the scaling calculator.
Invalid value 2 can only be activated if invalid value 1 is and invalid value 3 can
only be activated if invalid value 2 is.
For details on how to use the “Scaling calculator” please refer to the IPEmotion
Documentation - Section 3.4.5 “Channel configuration and scaling”.

Changesanderrorsexcepted.

204

8.7 OBDSIGNALS

Signal
This tab allows you to define signal settings.

• Internal data type

Assign an internal data type to the signal. Available data types are “Double” and
“String”.

• Signal number

Assign a number to the current signal. This way you will later be able to sort the signals
in the grid according to their “Signal numbers”.

• Hold last value

Specify, for how long the last value of the signal will be hold.

• Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may here
select the dataset, to which this setting will refer.

• Timeout

Specify the timeout period for the current signal. If the data source doesn’t send data
for the specified time period, the value of the signal is set to “NaN (Not a Number)”
and will be displayed as “–” in a display.

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

• Special task

The field “Special task” allows you to assign a user specific task to a signal, as long as
it has not been assigned to a logger default special task in the “Format” tab yet. If a
special task such as “GPS longitude/latitude/altitude in degrees”, “Vehicle identifi-
cation” or other has been assigned, in the “Format” tab, this field remains uneditable.

For further information regarding user specific special tasks and their properties
please refer to this part of the maual (→8.2.4.3).

Changesanderrorsexcepted.

205

8.7 OBDSIGNALS

OBD-2(PID)
This tab allows shows extended OBD-2 specific settings.

Signal check
This tab allows you to activate “Signal check” for this signal. You may choose whether you
wish to apply the global signal check settings to this signal or override the global settings
with settings specific for this signal.
Global signal check settings have to be defined first. For information on how to do so and
for general information on “Signal check” please refer to (→4.2.2).

Changesanderrorsexcepted.

206

8.8 GATEWAYS

8.8 Gateways

The Gateway method makes it possible to take messages received on one CAN channel
(source) and output them on another channel (target). Messages are output as soon as
they are received ￿ with this method, it is neither possible to influence the time of transmis-
sion nor to modify the sent data (this can be achieved by means of programing, through
a script). Filters can be used to restrict the messages transmitted.

8.8.1 Adding a gateway

In order to add a gateway, select the desired source CAN channel in the measurement
task tree, click the components button in the Ribbon and then select “Gateway”. For
instructions regarding the settings of a gateway please refer to (→8.8.3).

8.8.2 Adding an ID filter

In order to limit the traffic passed through the gateway, one or more ID filter per gateway
can be defined. In order to add an ID filter select the desired gateway in the measurement
task tree, click the “Components” button in the Ribbon and then select “ID filter”. For
instruction regarding the settings of an ID filter please refer to (→8.8.4).

Changesanderrorsexcepted.

207

8.8 GATEWAYS

8.8.3 Gateway settings

8.8.3.1 Tree elements for Gateways

Each Gateway that has been added to a CAN channel will appear in the measurement
task tree as a child element to the respective CAN channel.

8.8.3.2 Grid area for Gateways

In the “grid area” you will be presented with an overview of all the previously added
ID filters for the selected gateway. You can activate or deactivate an ID filter by tick-
ing/unticking the “Active”-box. Also you can find here two important functions, which are
the “Column chooser” (→4.2.5) and the “Filter editor” (→4.2.6).

8.8.3.3 Details area for Gateways

The details area provides settings regarding the general behaviour of a gateway.
General
Please refer to (→4.2.2).
Settings
Settings regarding the target CAN channel and filter action.

• Default filter action

Define whether the gateway should pass or block all traffic except the specified ID
or ID range.

Changesanderrorsexcepted.

208

8.8 GATEWAYS

• Target

Select the desired target CAN channel.

8.8.4 ID filter settings

All setting regarding the ID filter can be found in the “Filter settings” tab of the details area
of the respective ID filter.

• Mode

Define whether the filter will affect a specific ID or an ID range.

• CAN ID

Define the specific or start ID for the filter. For detailed instructions on the topic CAN
ID pleaser refer to (→8.1.3.4).

• CAN ID

Define the stop ID for the filter if the mode ID range has been selected.

Changesanderrorsexcepted.

209

8.9 RUNSTATE

8.9 Runstate

Taking into account the variety of different run states, plus the fact that the ARCOS display
is not always used, we have created the possibility of using CAN messages to read out
the current logger state and export it into a CANdb file.

For this purpose, the start identifier can be freely selected, while the remaining messages
are sequentially put out on the subsequent identifiers.

Moreover, the output rate can be selected, and the content influenced by activat-
ing/deactivating individual messages.

8.9.1 Add Runstate

In order to read out the logger state using the “Runstate” functionality, you will first need
to add the “Runstate” interface to the CAN channel on which it should be sent. To do so,
select the desired CAN channel in the measurement task tree, click the “Components”
button in the Ribbon and then choose “Runstate”.

Changesanderrorsexcepted.

210

8.9 RUNSTATE

8.9.2 Tree elements for Runstate

Once the “Runstate” interface has been added to a CAN channel, it will appear in the
measurement task tree as a child element to that channel.

8.9.3 Grid area for Runstate

In the “Grid area” you will be presented with an overview of the available signal mes-
sages. Each signal message has a subject and contains various signals concerning the
respective subject. Marking/demarking active a signal message in the grid area will de-
termine, whether the contained information will be read out and saved or discarded at
export.
The description field tells you the subject of a signal message and the CAN ID field tells
you the CAN ID in hexadecimal of the signal message.
Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

Changesanderrorsexcepted.

211

8.9 RUNSTATE

8.9.4 Details area for Runstate

The details area for “Runstate” provides runstate settings.
General
Please refer to (→4.2.2).
Settings
This tab contains the runstate settings.

• First CAN-ID

This field defines the CAN identifier for sending of the first signal message. The remain-
ing messages are sequentially put out on the subsequent identifiers.

• Sending rate

Define the output rate for state information.

8.9.5 Export Runstate

In order to make the loggers runstate signals available for further processing or analysis,
they may be exported into a CANdb database. To do so, select the “Runstate” interface
in the measurement task tree and then click the “Export” button in the Ribbon and choose
“CANdb export”. Only the signal messages that have previously been marked active in
tht grid area will be exported.

Changesanderrorsexcepted.

212

8.10 ETHCHANNELS

8.10 ETH channels

All the ETH channels for your system are located in the tree element “ETH interfaces”.
According to the default settings, the tree element “ETH interfaces” will include a preset
number of ETH channels. By clicking the tree element ETH Interfaces you will see all of
its channels and signals in the grid area as well as a tab called General in the Details
area which allows you to set a name and description. These settings apply to the entire
element “ETH interfaces”.

In the following will be described how to add ETH channels and adjust their settings
(→8.10.3).

8.10.1 Storage method

In order to store all
method for storage. Please refer to (→ 15.11).

incoming traffic on an ETH channel use “PCAP” as a bus tracing

Changesanderrorsexcepted.

213

8.10 ETHCHANNELS

8.10.2 Adding ETH channels

ETH channels can be added by selecting the tree element “ETH interfaces”, then clicking
the “Components” button and finally choosing the desired type of ETH channel you wish
to add.

Changesanderrorsexcepted.

214

8.10 ETHCHANNELS

8.10.3 ETH settings

By selecting one of the ETH channels in the tree you will be able to define this channel’s
settings in the details area.

The same settings described in this section as part of the Details area
can also be adjusted when selecting the tree element ETH interfaces
and then directly changing the desired setting in the respective field of
the Grid area.

Changesanderrorsexcepted.

215

8.10 ETHCHANNELS

8.10.3.1 General

This tab allows you to give a user specific name for the selected ETH channel if wished
and add an additional description.
The Reference field serves as the tree element’s
unique identifier inside the measurement task tree. It cannot be changed.

The Active checkbox allows to deactivate the entire bus.
If a bus is
deactivated all childelements of this bus will be deactivated, too, and
cannot be stored or traced, until the bus is reactivated.

Front-, Internal- and openABK-buses cannot be deactivated.

8.10.3.2 Settings

This tab allows you to set your current ETH channel’s physical channel number and
whether it should be used for data transfer.

The ETH channel “Internal” cannot be used for data transfer.

Changesanderrorsexcepted.

216

8.10 ETHCHANNELS

8.10.3.3 LAN

This tab allows you to set your current ETH channel’s LAN settings. Whether it should
receive an IP address automatically or not. If you deactivate the setting “Get IP address
automatically” and set the IP address manually.
In addition there will appear a new
tab labeled “DHCP server”, which allows to configure this channel as a DHCP server
optionally. The next paragraph below will explain how.

Additionally this tab allows you to specify 5 alternative IP addresses
for your ETH channel
in order to configure one ETH channel for use in
multiple networks.

For the tree elements “OpenABK” and “Internal” the IP settings cannot
be adjusted.

8.10.3.4 DHCP server

This tab allows you to set up your ETH channal as a DHCP server, to set the acceptable IP
range and default and minimum lease time.

The manually set IP address, that has been specified in the “LAN” tab,
may not be part of the DHCP range.

Changesanderrorsexcepted.

217

8.10 ETHCHANNELS

8.10.3.5 PTP (Precision time protocol)

This tab allows you to synchronize the time of your logger with peripheral equipment, such
as the Analog module or Thermo module, that is connected via ETH.

PTP is only available for “Front” and “ETH” channels. It is not available for
“Internal” and “openABK”.

Active
Activate PTP for this channel.

Mode
Set whether the logger should function as master or slave. If set to master, all peripheral
equipment on this channel will use the loggers time. If set to slave, one piece of peripheral
must be set to master.

Domain
Choose a domain on which synchronization should happen. This allows to have multiple
masters in the same network. The master and its associated slaves need to use the same
domain.

Transport protocol
Set the transport protocol for ptp.

Announce interval
Specify the time for sending announce messages.

Synchonization interval
Specify the time for sending synchonization messages.

Changesanderrorsexcepted.

218

8.10 ETHCHANNELS

Force use ptpd
Because the dataLog firmware had to switch usage from ptpd to
linuxptp this setting provides a fallback if problems arise with the usage
of linuxptp. Activating this setting will cause the logger to revert to the
usage of the ptpd protocoll.
This setting is deactivated by default and only recommended to be
activated if problems with linuxptp arise.

8.10.3.6 Bus statistic PTP (Precision time protocol)

The “Bus statistic PTP” provide a range of statistics and status signals for PTP. The “Bus
statistics PTP” component can be added to CAN, CAN FD, FlexRay and LIN channels but
not to ETH channels.

To add the component select the desired channel in the measurement task tree, click
the “Components” button in the Ribbon and then choose “Bus statistics PTP”.

Once the component “Bus statistics PTP” has been added to your channel, it will appear
in the measurement task tree as a child element of this channel and the grid area will
give you an overview of the available signals.

The signals included in “Bus statistics” are of the type “Internal signal” and may be
adjusted in the same way. For more information on “Internal signals” please refer to
(→8.26).

Changesanderrorsexcepted.

219

8.10 ETHCHANNELS

Overview of signals

Subtype
Absolute number of ignored syncs
Absolute number of performed syncs
Number of time differences below 1μs
Number of time differences below 10μs
Number of time differences below 100μs
Number of time differences below 1ms
Number of time differences below 10ms
Number of time differences below 100ms
Number of time differences below 1s
Number of time differences below 10s
Number of time differences above 10s

Unit
Integer
Integer
Integer
Integer
Integer
Integer
Integer
Integer
Integer
Integer
Integer

Changesanderrorsexcepted.

220

8.10 ETHCHANNELS

8.10.4 ETH channel Bus statistic

The “Bus statistic” provides a range of statistics and status signals for the respective ETH
channel. It contains information on the current state of the Bus, the Busload, as well as on
the messages that have been received and errors that ocurred.

The “Bus statistic” only shows statistics for the channel to which it belongs.
For each channel that you would like to see the statistic, you will have to
add the component “Bus statistic”.

8.10.4.1 Adding Bus statistics
Select the channel in the tree for which you would like to
add “Bus statistic”, then click the “Components” button in the Ribbon and choose “Bus
statistic”.

Changesanderrorsexcepted.

221

8.10 ETHCHANNELS

8.10.4.2 Bus statistic signals Once the component “Bus statistic” has been added to
your channel, it will appear in the measurement task tree as a child element of this
channel and the grid area will give you an overview of the available signals.

The signals included in “Bus statistics” are of the type “Internal signal” and may be
adjusted in the same way. For more information on “Internal signals” please refer to
(→8.26).

Overview of signals

Subtype

Internal Link status

Internal Link speed
Internal Duplex mode
Internal Number of packets

Internal Current packet rate

Internal Number of bytes

Internal Byte rate

Internal Number of error
frames
Internal Error frame rate

transferred

Meaning
o= Link down
1= Link up
Speed of the Link
Mode of operation
Total number of
packets
Current rate of packets per
second
Total number of
bytes
Current rate of bytes per sec-
ond
Total number of error frames
ocurred
Current rate of error frames
per second

transferred

Unit

-

[Mb/s]
-
-

[frames/s]

-

[frames/s]

-

[frames/s]

Changesanderrorsexcepted.

222

8.10 ETHCHANNELS

8.10.5 CAN FD satellite, FlexRay satellite and LIN satellite on ETH (ETH feature interface)

The “ETH Feature” interface, allows for connection and configuration of CAN FD satellites,
FlexRay satellites and LIN satellites via ETH. A CAN FD satellite possesses four CAN FD
channels, a FlexRay satellite possesses two FlexRay channels and a LIN satellite possesses
8 LIN channels. Their functionality is identical to that of the regular CAN FD interface and
CAN FD channels, respectively FlexRay interface and FlexRay channels and LIN interface
and LIN channels.

Because the μCROS XL does not possess a feature connector satellites
need to be connected to an internal ETH connector.

This section will only explain how to add the “ETH Feature” interface and a satellite to your
configuration. For details on how to configure a CAN FD channel please refer to (→8.1)
and for CAN signals please refer to (→8.2).
For details on how to configure a FlexRay channel please refer to (→8.16) and for FlexRay
signals please refer to (→8.17).
For details on how to configure a LIN channel please refer to (→8.14) and for LIN signals
please refer to (→8.15).

8.10.5.1 Adding the ETH Feature interface

In order to add the “ETH Feature” interface to your configuration, select the ETH interface
in the measurement task tree, click the “Components” button in the Ribbon and then
choose “Feature”.

Changesanderrorsexcepted.

223

8.10 ETHCHANNELS

8.10.5.2 Adding a CAN FD/FlexRay/LIN satellite

In order to add a CAN FD/FlexRay/LIN satellite make sure, that you have added the “ETH
Feature” interface to your configuration (→8.10.5.1). Once the “ETH Feature” interface
has been added to your configuration, you will need to select it in the measurement
task tree (select ETH Internal for μ CROS XL). Then click the “Components” button in the
Ribbon and choose “CAN FD/FlexRay/LIN satellite”.

Adding satellites on the ETH Feature connector.

Changesanderrorsexcepted.

224

8.10 ETHCHANNELS

Adding satellites on the ETH Internal connector of a μCROS XL.

8.10.5.3 Tree elements for a CAN FD satellite

Each FlexRay satellite comes with two FlexRay channels which will appear as child
elements to the FlexRay satellite in the measurement task tree.

Changesanderrorsexcepted.

225

8.10 ETHCHANNELS

8.10.5.4 Tree elements for a FlexRay satellite

Each FlexRay satellite comes with two FlexRay channels which will appear as child
elements to the FlexRay satellite in the measurement task tree.

8.10.5.5 Tree elements for a LIN satellite

Each LIN satellite comes with eight LIN channels which will appear as child elements to
the LIN satellite in the measurement task tree.

Changesanderrorsexcepted.

226

8.10 ETHCHANNELS

8.10.6 DLT (Diagnostic, Log and Trace) on ETH

DLT provides the possibility of diagnosing, logging and tracing of an ECU via ETH Front
and ETH channels. If activated, the DLT-station will send Diagnostic, Log and Trace data
It therefore is necessary to have both a
to the DLT dataset method, which will store it.
DLT-station for an ETH channel set up, as well as the DLT dataset method, in order to work
with DLT.

For instructions on setting up the DLT dataset method please refer to (→15.20).

8.10.6.1 Adding a DLT-Station

In order to add a DLT-Station to an ETH channel, select the desired ETH or Front channel,
click on the “Components” button in the Ribbon and then choose “Diagnostic, Log and
Trace”. This will add a “DLT-Station xx” to your channel. Multiple DLT-Stations can be added
to each channel.

8.10.6.2 Tree elements for DLT

The “DLT-Station xx”, that you have just created, will appear as a child element to its re-
spective ETH/Front channel in the measurement task tree.

Changesanderrorsexcepted.

227

8.10 ETHCHANNELS

8.10.6.3 Details area for DLT

The Details area shows settings either for the selected “DLT-Station xx”.

General
Please refer to (→4.2.2).

DLT
This tab contains settings regarding the communication between the “DLT-Station” and
the ECU that it supposed to be diagnosed/logged/traced.

• IP address

Set the IP address the of the ECU. It must be in the same subnet as the connector of
the DLT-Station.

• IP port

Set the IP port that is used for DLT by the respective ECU.

• ECU identifier

Type in the ECU identifier of the respective ECU.

• Log level

Set the log level of the DLT-Station. A log level defines a classification for the severity
grade of a log message.

• Default trace status

The trace status provides information if a trace message should be sent.

Changesanderrorsexcepted.

228

8.10 ETHCHANNELS

Trigger
This tab contains settings regarding the data acquisition of this DLT-Station. Whether it
should continuously acquire data or be activated via a trigger.

• Continuous acquisition

Data will be continuously acquired starting with the beginning of the dataset and
stoping with the end of the dataset.

• Start and stop trigger

Define a start- and a strop-trigger that will start and stop data acquisition.

• Stop is inverted start

Define a start-trigger to start data acquisition. As soon as the trigger condition
ceases to exist, data acquisition will be stopped.

Changesanderrorsexcepted.

229

8.10 ETHCHANNELS

8.10.7 VLAN

The “VLAN” function allows you to connect your logger to a logical virtual LAN and to
configure the functionality of that connection.

8.10.7.1 Adding a VLAN

In order to configure communication with a VLAN you will need to add the VLAN inter-
face to an existing ethernet channel. To do so, select the desired ethernet channel in the
measurement taskt tree, click the “Components” button in the Ribbon and then choose
“VLAN”.

8.10.7.2 Configuration of a VLAN

The settings for configuration of a “VLAN” are mainly identical to those of a physical eth-
ernet channel, although the VLAN interface is limited in settings compared to a phyisical
ethernet channel.
The available settings tabs in the details area area

• General

• Settings

• LAN

• VLAN

For information regarding the “General”, “Settings” and “LAN” tab please refer to the
chapter “ETH settings” (→8.10.3).
Any “VLAN” specific settings will be desribed in the “VLAN specific settings” below.

Changesanderrorsexcepted.

230

8.10 ETHCHANNELS

8.10.7.3 VLAN specific settings

The tab “VLAN” contains the setting for the “VLAN identifier”. It represents the ID of the
logical subnet to which to connect and must be unique within its parent physical ethernet
channel.

8.10.7.4 Available components for VLAN

Once the “VLAN” interface has been configured you can add one or more compenents
with different functionality. The following components are available for VLAN and can
be configured to be used in the same way as via LAN.

• Diagnostic, Log and Trace (DLT) (→8.10.6)

• Alias signal group (→9)

• Eth channel Bus statistic (→8.10.4)

• External files (→13)

Changesanderrorsexcepted.

231

8.11 ETHSIGNALS

8.11 ETH signals

For data acqusition you can import A2L or Fibex databases on the “Front” channel of your
“ETH interface” or on any manually added ETH channel. The protocol for importing A2L
databases is XCPonUDP and the protocol for importing Fibex databases is SOME/IP.

8.11.1 Storage method

In order to store incoming signals on an ETH channel use one of the following signal
storage methods.

• ATFX (→ 15.7)

• MDF 4.0 (→ 15.8)

• MDF 4.1 (→ 15.9)

8.11.2 Importing ETH signals

8.11.2.1 Importing Autosar files (UDP)

In order to import an Autosar database, select either the “Front” channel or any manually
added “ETH xx” channel of your “ETH interface”, click the “Import” button in the Ribbon
and then choose “Autosar”.

Changesanderrorsexcepted.

232

8.11 ETHSIGNALS

The following window lets you choose which file you wish to import. Choose the file you
wish to import and click “Open”.

Next the “Importer” window will appear, that will present you with a range of importing
options.

In this dialog, all signals that can be imported from the description file are displayed. In
the left table, all signals, where the ”selection” checkboxes are selected, will be marked
for import. You can either choose manually, which signals to import, you can use the
“Select/Deselect all” button on the bottom left, or you can use a CSV-file to determine
which signals are to be imported, by clicking “Select by CSV” on the bottom left.

In the right table the metadata, properties of the selected signals, the control unit and
the protocol are displayed.

Changesanderrorsexcepted.

233

8.11 ETHSIGNALS

Once you have choosen all the signals you wish to import, click “OK” to complete the
import procedure.

8.11.2.2 Import properties for UDP

The “Import properties” of a ECU, Message or signal allow you to see certain properties
such as the Data format, EPK identification, the Bit mask, the start bit, bit count and more.
It shows the signal’s properties as described by the description file.

Figure 28: Example for “Import properties” of a UDP ECU

Figure 29: Example for “Import properties” of a UDP Network layer

Figure 30: Example for “Import properties” of a UDP Socket

Changesanderrorsexcepted.

234

8.11 ETHSIGNALS

Figure 31: Example for “Import properties” of a UDP message

Figure 32: Example for “Import properties” of a UDP signal

8.11.2.3 Importing Fibex files (SOME/IP)

In order to import a Fibex database, select either the “Front” channel or any manually
added “ETH xx” channel of your “ETH interface”, click the “Import” button in the Ribbon
and then choose “Fibex”.

Changesanderrorsexcepted.

235

8.11 ETHSIGNALS

The following window lets you choose which file you wish to import. Choose the file you
wish to import and click “Open”.

Next the “Importer” window will appear, that will present you with a range of importing
options.

In this dialog, all signals that can be imported from the description file are displayed. In
the left table, all signals, where the ”selection” checkboxes are selected, will be marked
for import. You can either choose manually, which signals to import, you can use the
“Select/Deselect all” button on the bottom left, or you can use a CSV-file to determine
which signals are to be imported, by clicking “Select by CSV” on the bottom left.

In the right table the metadata, properties of the selected signals, the control unit and
the protocol are displayed.

Changesanderrorsexcepted.

236

8.11 ETHSIGNALS

Once you have choosen all the signals you wish to import, click “OK” to complete the
import procedure.

8.11.2.4 Import properties for SOME/IP

The “Import properties” of a ECU, Message or signal allow you to see certain properties
such as the Data format, EPK identification, the Bit mask, the start bit, bit count and more.
It shows the signal’s properties as described by the description file.

Figure 33: Example for “Import properties” of a SOME/IP ECU

Figure 34: Example for “Import properties” of a SOME/IP protocol layer

Figure 35: Example for “Import properties” of a SOME/IP Socket

Changesanderrorsexcepted.

237

8.11 ETHSIGNALS

Figure 36: Example for “Import properties” of a SOME/IP message

Figure 37: Example for “Import properties” of a SOME/IP signal

8.11.2.5 Importing A2L files (XCPonUDP)

In order to import an A2L database, select either the “Front” channel or any manually
added “ETH xx” channel of your “ETH interface”, click the “Import” button in the Ribbon
and then choose “A2L”.

Changesanderrorsexcepted.

238

8.11 ETHSIGNALS

The following window lets you choose which file you wish to import. Choose the file you
wish to import and click “Open”.

Next the “Importer” window will appear, that will present you with a range of importing
options.

In this dialog, all signals that can be imported from the description file are displayed. In
the left table, all signals, where the ”selection” checkboxes are selected, will be marked
for import. You can either choose manually, which signals to import, you can use the
“Select/Deselect all” button on the bottom left, or you can use a CSV-file to determine
which signals are to be imported, by clicking “Select by CSV” on the bottom left.

In the right table the metadata, properties of the selected signals, the control unit and
the protocol are displayed.

Changesanderrorsexcepted.

239

8.11 ETHSIGNALS

Once you have choosen all the signals you wish to import, click “OK” to complete the
import procedure.

Depending on the protocol, a sampling rate or the DAQ list to use, can
be assigned to the signals.
In the case of a protocol using DAQ lists (CCP, XCP), you can specify
via the column selection dialog, if the signals are configured by the
sampling rate or a DAQ list. To achieve this you should open the column
selection dialog, via the context menu of the table header, and then
drag the desired column (”sampling” or ”DAQ list”) from the column
selection dialog to the table header.
The other column is removed
automatically.
If in a protocol based on DAQ lists, sampling rates are used for the signal
configuration, during import the signals are assigned to the available
DAQ list with the most suitable sampling rate.
In case of protocols supporting array signals, you can specify via the
”split array” column whether all the signals of the array or just the first to
be imported. If this column does not appear it can be moved from the
column selection dialog into the table.

Changesanderrorsexcepted.

240

8.11 ETHSIGNALS

8.11.2.6 IP settings when Importing A2L files (XCPonUDP)

When importing signals to an ETH channel from an A2L file, the PlugIn will automatically
set the description file’s source IP address (to be found in the import properties of the
description file) as the ETH channel’s IP address. If DHCP is activated it will be deactivated
and the existing IP address will be replaced with the source IP address. Also if DHCP is
deactivated but the IP address is set to 0.0.0.0, the existing IP address will be replaced
with the source IP address.

However, if DHCP is deactivated and a user specific IP address other than 0.0.0.0 is set,
this IP address will not be replaced.

8.11.2.7 Import properties for XCPonUDP

The “Import properties” for XCPonUDP are identical to XCPonCAN. Please refer to (→8.5.4).

Changesanderrorsexcepted.

241

8.11 ETHSIGNALS

8.11.3 Signal properties

8.11.3.1 Signal properties for UDP

The protocol used at Autosar import on ETH is PDU and the signal properties for UDP signals
are mainly the same as for PDU signals on CAN FD channels. Please refer to (→ 8.3.4).

The only difference betwen PDU signals on ETH and on CAN FD is, that importing PDU
signals on ETH will result in a different tree structure than on CAN FD. The structure is:

ETH channel → ECU (here labeled VGW) → Network → Socket xx → signal messages

The socket layer contains the signal messages and offers an extra possibility for grouping
these messages.

8.11.3.2 Signal properties for SOME/IP

The signal properties for SOME/IP signals are mainly the same as for Fibex signals on Flexray
channels. Please refer to (→ 8.17.4).

The only difference betwen Fibex signals on ETH and on Flexray is, that importing Fibex
signals on ETH will result in one extra layer of tree elements called “Socket x”.

The socket layer then contains the signal messages and offers an extra possibility for
grouping these messages.

Changesanderrorsexcepted.

242

8.11 ETHSIGNALS

8.11.3.3 Signal properties for XCPonUDP

The signal properties for XCPonUDP signals are the same as for XCP signals on CAN
channels. Please refer to (→ 8.5.5).

Changesanderrorsexcepted.

243

8.12 DOIP-UDSSIGNALSOVERETH

8.12 DoIP - UDS signals over ETH

The DoIP protocoll allows you to import UDS signals on “Front”, “ETH xx” and “SFP+”
ethernet channels.

UDS signals over ethernet function identically to regular UDS signals on CAN channels,
therefore please refer to the chapter “UDS signals” (→ 8.6).

8.12.1 IP settings for DoIP

When importing UDS signals into an ethernet channel, the channel’s IP
settings need to be set manually.
If the channel’s IP settings are set to
“Get IP address automatically” this will produce an error and cancel ex-
port.

In order to correctly set an ethernet channel’s IP settings for DoIP navigate to the channel’s
“LAN” tab in the details area, deactivate the “Get IP address automatically” setting and
then enter the desired IP address manually.

Changesanderrorsexcepted.

244

8.13 PLP/TECMPDEVICES(AUTOMOTIVEETHERNET)

8.13 PLP/TECMP devices (Automotive Ethernet)

The CAETEC dataLog PlugIn for IPEmotion supports a range of PLP/TECMP devices (or Cap-
ture module devices) that can be connected to a physical ETH channel of the following
types:

• Front

• ETH xx

• SFP+

PLP/TECMP devices provide the logger with a set of additional interfaces (PLP/TECMP-
CANFD, PLP/TECMP-ETH, PLP/TECMP-LIN, PLP/TECMP-FlexRay), which provide additional
hardware channels for signal acquisition connected via an Ethernet interface.

8.13.1 Supported PLP/TECMP devices and features

Manufacturer

Model

Technica Engineering
Technica Engineering

CM LIN Combo
CM CAN Combo

Technica Engineering

CM ETH Combo

Technica Engineering

CM 100 High

Technica Engineering

CM 1000 High

Supported
channels
10x LIN
6x CAN/CAN FD
1x FlexRay
3x
ETH
1000BaseT1,
2x 100BaseT1)
6x
ETH
100BaseT1)
6x
ETH
1000BaseT1)

(6x

(6x

(1x

Unsupported
channels
6x Analog
2x RS232/TTL

-

-

-

8.13.2 Adding a PLP/TECMP device

In order to add a PLP/TECMP device to your configuration choose either ETH channel of
the types Front/ETH xx/SFP+ in you measurement task tree, then click the “Components”
button in the Ribbon and choose the desired PLP/TECMP device.

Physical Ethernet connections for PLP/TECMP devices

Even though it is possible to use different types of physical ethernet
connection to connect a PLP/TECMP device (Front, ETH xx, SFP+) only
one physical channel per configuration can be used for connecting
PLP/TECMP devices.
If you set up multiple physical channels for con-
necting PLP/TECMP devices, that will produce a Warning at export of
the configuration.

Changesanderrorsexcepted.

245

8.13 PLP/TECMPDEVICES(AUTOMOTIVEETHERNET)

8.13.3 IP settings for PLP/TECMP devices

The IP settings for a PLP/TECMP device have to be set in the details area of the respective
ethernet channel.
In the “LAN” tab of the ethernet channel the setting “Get IP address automatically” must
be turned off.

In the next step navigate to the “PLP/TECMP” tab of the details area, activate the tickbox
for the desired protocol and then choose the desired IP Address to be used by your
PLP/TECMP device from the dropdown menu.

Changesanderrorsexcepted.

246

8.13 PLP/TECMPDEVICES(AUTOMOTIVEETHERNET)

8.13.4 Custom PLP/TECMP devices

It is possible to connect other PLP/TECMP devices than the above mentioned (→8.13.1).
In order to configure these devices you will need to add a “Custom PLP/TECMP Device”.
This is done in the same way as adding a regular PLP/TECMP device, please refer to
“Adding a PLP/TECMP device” (→8.13.2).

Once the “Custom PLP/TECMP device” has been added to your configuration it should
appear in the measurement task tree and you can now configure it according to your
needs. To do so select the “Custom PLP/TECMP device” in the measurement task tree,
select the “Components” button in the Ribbon and then choose the desired channel
type you wish to add to your device.
If you wish to add multiple channels at once, click on “Multiple selection” and select all
the desired channels.

Your custom PLP/TECMP device is now set up and can be configured like any other
PLP/TECMP device following the subsequent instructions of this chapter.

Changesanderrorsexcepted.

247

8.13 PLP/TECMPDEVICES(AUTOMOTIVEETHERNET)

8.13.5 Tree elements for PLP/TECMP devices

Even though PLP/TECMP devices provide hardware channels for a variety of bus types
they will alway be connected to the logger via the ethernet interface.
Therefore the various PLP/TECMP interfaces will appear in the measurement task tree
as child elements to their corresponding ethernet channel.
The supported hardware
channels of the device will appear as child elements to the PLP/TECMP device grouped
by PLP/TECMP interface type.

Databases that are imported to a PLP/TECMP device’s channel will apear as child ele-
ments with all associated elements, just as is the case with the logger’s native hardware
channels.

8.13.6 Grid area for PLP/TECMP devices

In the “grid area” you will be presented with an overview of your selected channel’s
signals. Also you can find here two important functions, which are the “Column chooser”
(→4.2.5) and the “Filter editor” (→4.2.6).

Changesanderrorsexcepted.

248

8.13 PLP/TECMPDEVICES(AUTOMOTIVEETHERNET)

8.13.7 PLP/TECMP interface functionality and limitations

While most of the PLP/TECMP devices’ fundamental functions are available in the PlugIn,
there remain some limitations as to what components can be added to a PLP/TECMP
interface channel and what protocols can be used for signal import. The following table
gives an overview about the available as well as unavailable functions of the different
PLP/TECMP interfaces.

PLP/TECMP inter-
face
PLP/TECMP-
CANFD

PLP/TECMP-ETH

compo-

Supported
nents
External files
Gateway (limited)
Manual messages
Alias signals
External files
Alias signals

Unsupported
components
Bus statistics
Audio Recording
OBD
Runstate
Bus statistics
Cameras
DLT

PLP/TECMP-
FlexRay

PLP/TECMP-LIN

External files
Alias signals

External files
Alias signals

Bus statistics

Bus statistics

8.13.8 Details area for PLP/TECMP Devices

Supported
protocols
CANdb
Autosar
Fibex

CANdb
Autosar
(UDP)
Fibex
(SOME/IP)
CANdb
Autosar
Fibex
CANdb

Unsupported
protocols
A2L
UDS

A2L

A2L
Flexray Pa-
rameter
-

Although PLP/TECMP devices all run on ethernet channels, they provide different signal
acquisition channels which are controlled by the respective PLP/TECMP interfaces.
The details area section for PLP/TECMP devices will therefore be structured according to
PLP/TECMP interface type.

• Details area for PLP/TECMP-CANFD (→8.13.8.1)

• Details area for PLP/TECMP-ETH (→8.13.8.2)

• Details area for PLP/TECMP-FlexRay (→8.13.8.3)

• Details area for PLP/TECMP-LIN (→8.13.8.4)

8.13.8.1 Details area for PLP/TECMP-CANFD

This section of the manual explaines the details area for a PLP/TECMP-CANFD interface.
The PLP/TECMP-CANFD interface must be selected in the measurement task tree in order
to access its details area.

Signals imported to any of the PLP/TECMP-CANFD interface’s CAN channels are regular
CAN/CAN FD signals. For instructions on working with CAN/CAN FD signals please refer to
the chapter “CAN/CAN FD signals” (→8.2).

Changesanderrorsexcepted.

249

8.13 PLP/TECMPDEVICES(AUTOMOTIVEETHERNET)

General
Please refer to (→4.2.2).

CAN
This tab allows for CAN specific settings.

• Baud rate

This function for PLP/TECMP devices is not supported by this PlugIn.

• Baud rate

This function for PLP/TECMP devices is not supported by this PlugIn.

• CAN FD

This option is only supported on CAN FD channels in the CAN FD interface.
If activated, you may customize the fast datarate of the CAN FD channel.

• Data rate

This function for PLP/TECMP devices is not supported by this PlugIn.

Wake On CAN
This tab allows for Wake On CAN specific settings.

• Timeout

For Wake on CAN, timeout has a special significance. It defines how long a waking
channel must be inactive to be recognized so and therefore allow for the logger
to shut down. If timeout is recognized, an entry is made in the log file and an error
message with an alert appears on the display, which has to be acknowledged.

Changesanderrorsexcepted.

250

8.13 PLP/TECMPDEVICES(AUTOMOTIVEETHERNET)

• Mode

This dropdwon menu allows you to set the wake-up function for your selected CAN
channel.

Wake on CAN type
Disabled

Keep awake

Characteristics
No start on CAN messages, lowest en-
ergy consumption.
The logger starts with Clamp 15, but only
shuts down if all the awakening condi-
tions (Clamp 15 and WakeOnX) are no
longer fullfilled.

• CAN ID

This option has been explained in great detail here (→8.1.3.4).

• Data field

This option has been explained in great detail here (→8.1.3.4).

Hardware
This tab allows you to change the channel number of your channel.

Bus check
This tab allows you to activate “Bus check” for this bus. You may choose whether you
wish to apply the global bus check settings to this bus or override the global settings with
settings specific for this bus.
Global bus check settings have to be defined first. For information on how to do so and
for general information on “Bus check” please refer to (→4.2.2).

Changesanderrorsexcepted.

251

8.13 PLP/TECMPDEVICES(AUTOMOTIVEETHERNET)

8.13.8.2 Details area for PLP/TECMP-ETH

This section of the manual explaines the details area for a PLP/TECMP-ETH interface.
The PLP/TECMP-ETH interface must be selected in the measurement task tree in order to
access its details area.

General
Please refer to (→4.2.2).

Hardware
This tab allows you to change the channel number of your channel.

8.13.8.3 Details area for PLP/TECMP-FlexRay

This section of the manual explaines the details area for a PLP/TECMP-FlexRay interface.
The PLP/TECMP-FlexRay interface must be selected in the measurement task tree in order
to access its details area.

General
Please refer to (→4.2.2).

Wake On FlexRay
This tab allows for Wake On FlexRay specific settings.

• Timeout

Timeout defines how long a waking channel must be inactive to be recognized so
and therefore allow for the logger to shutdown.
If timeout is recognized, an entry
is made in the log file and an error message with an alert appears on the display,
which has to be acknowledged.

Changesanderrorsexcepted.

252

8.13 PLP/TECMPDEVICES(AUTOMOTIVEETHERNET)

• Mode

This dropdwon menu allows you to set the wake-up function for your selected
FlexRay channel.

Wake on FlexRay type
Disabled

Keep awake

Characteristics
No start on FlexRay messages, lowest
energy consumption.
The logger starts with Clamp 15, but only
shuts down if all the awakening condi-
tions (Clamp 15 and WakeOnX) are no
longer fullfilled.

Hardware
This tab allows you to change the channel number of your channel.

Bus check
This tab allows you to activate “Bus check” for this bus. You may choose whether you
wish to apply the global bus check settings to this bus or override the global settings with
settings specific for this bus.
Global bus check settings have to be defined first. For information on how to do so and
for general information on “Bus check” please refer to (→4.2.2).

8.13.8.4 Details area for PLP/TECMP-LIN

This section of the manual explaines the details area for a PLP/TECMP-LIN interface.
The PLP/TECMP-LIN interface must be selected in the measurement task tree in order to
access its details area.

General

Changesanderrorsexcepted.

253

8.13 PLP/TECMPDEVICES(AUTOMOTIVEETHERNET)

Please refer to (→4.2.2).

LIN
LIN specific settings for PLP/TECMPdevices are not supported by this PlugIn.

Wake On LIN
This tab allows for Wake On LIN specific settings.

• Timeout

For Wake On LIN, timeout has a special significance. It defines how long a waking
channel must be inactive to be recognized so and therefore allow for the logger
to shutdown. If timeout is recognized, an entry is made in the log file and an error
message with an alert appears on the display, which has to be acknowledged.

• Mode

This dropdwon menu allows you to set the wake-up function for your selected LIN
channel.

Wake on LIN type
Disabled

Keep awake

Characteristics
No start on LIN messages, lowest energy
consumption.
The logger starts with Clamp 15, but only
shuts down if all the awakening condi-
tions (Clamp 15 and WakeOnX) are no
longer fullfilled.

• LIN ID

This option has been explained in great detail here (→8.1.3.4).

• Data field

This option has been explained in great detail here (→8.1.3.4).

Changesanderrorsexcepted.

254

8.13 PLP/TECMPDEVICES(AUTOMOTIVEETHERNET)

Hardware
This tab allows you to change the channel number of your channel.

Bus check
This tab allows you to activate “Bus check” for this bus. You may choose whether you
wish to apply the global bus check settings to this bus or override the global settings with
settings specific for this bus.
Global bus check settings have to be defined first. For information on how to do so and
for general information on “Bus check” please refer to (→4.2.2).

8.13.9 PLP/TECMPdevice bus statistic

It is possible to read out bus statistics on a PLP/TECMPdevice’s channel. The “Bus statistic”
provides a range of statistics and status signals for the respective PLP/TECMPdevice’s
channel. It contains information on the current state of the Bus, the Busload, as well as on
the messages that have been received and errors that ocurred.

The “Bus statistic” only shows statistics for the channel to which it belongs.
For each channel that you would like to see the statistic, you will have to
add the component “Bus statistic”.

Changesanderrorsexcepted.

255

8.13 PLP/TECMPDEVICES(AUTOMOTIVEETHERNET)

8.13.9.1 Adding Bus statistics
Select the channel in the tree for which you would like to
add “Bus statistic”, then click the “Components” button in the Ribbon and choose “Bus
statistic”.

8.13.9.2 Bus statistic signals Once the component “Bus statistic” has been added to
your channel, it will appear in the measurement task tree as a child element of this
channel and the grid area will give you an overview of the available signals.

The signals included in “Bus statistics” are of the type “Internal signal” and may be
adjusted in the same way. For more information on “Internal signals” please refer to
(→8.26).

Overview of signals

Subtype

Link status (Technica CM 100
highonly)
Number of messages

Message rate total

Number of error frames

Error frame rate

Meaning
o= Link down
1= Link up

transferred

Total number of
messages
Current rate of messages per
second
Total number of error frames
ocurred
Current rate of error frames
per second

Unit

-

-

[frames/s]

-

[frames/s]

Changesanderrorsexcepted.

256

8.14 LINCHANNELS

8.14 LIN channels

To work with “LIN channels”, you will first have to add the tree element “LIN interfaces”
to your measurement task tree. To do so, select your system in the measurement task
tree, click the “Components” button in the ribbon and choose “LIN interfaces” from the
resulting dropdown menu.

Once the “LIN interfaces” component has been added it will appear in the measurement
task tree as a tree element with one “LIN channel” as a child element.

8.14.1 Storage method

In order to store all incoming traffic on a LIN channel use a bus tracing method for storage.
Please refer to (→ 15.10).

Changesanderrorsexcepted.

257

8.14 LINCHANNELS

8.14.2 Adding LIN channels

LIN channels can be added by selecting the tree element “LIN interfaces”, then clicking
the “Components” button and then choosing “LIN channel”.

LIN
Adds a LIN channel that corresponds to a physical LIN channel of your logger.
instructions on LIN settings refer to (→8.14.3).

For

Multiple selection
Allows you to add multiple LIN channels of both types at the same time. To do so set the
counter for each type to the desired number of channels that you wish to add as marked
in the figure below.

8.14.3 LIN settings

By selecting one of the LIN channels in the tree you will be able to define this channel’s
settings in the details area.

The same settings described in this section as part of the Details area
can also be adjusted when selecting the tree element LIN interfaces and
then directly changing the desired setting in the respective field of the
Grid area.

Changesanderrorsexcepted.

258

8.14 LINCHANNELS

8.14.3.1 General

This tab allows you to give a user specific name for the selected LIN channel if wished and
add an additional description. The Reference field serves as the tree element’s unique
identifier inside the measurement task tree. It cannot be changed.

The Active checkbox allows to deactivate the entire bus. If a bus is deac-
tivated all childelements of this bus will be deactivated, too, and cannot
be stored or traced, until the bus is reactivated.

Changesanderrorsexcepted.

259

8.14 LINCHANNELS

8.14.3.2 LIN

Baud rate
The Baud rate is determined automatically by the logger.

LIN version
This field shows you the version of the LIN protocol that is used as described in the
“Description file”. This field cannot be changed.

8.14.3.3 Wake On LIN

Timeout
For Wake On LIN, timeout has a special significance.
It defines how long a waking
channel must be inactive to be recognized so and therefore allow for the logger to
shutdown. If timeout is recognized, an entry is made in the log file and an error message
with an alert appears on the display, which has to be acknowledged.

Mode
This dropdown menu allows you to set the wake-up function for your selected LIN channel.

Changesanderrorsexcepted.

260

8.14 LINCHANNELS

Wake on LIN type
Disabled

Enabled

Enabled (no message lost)

Keep awake

Characteristics
No start on LIN messages, lowest energy
consumption.
Start on a LIN message, with first mes-
sages lost; low energy consumption.
Start on LIN message, with no message
lost; slightly higher idle current.
The logger starts to other awakenings,
but only shuts down if all the awakening-
conditions are no longer fullfilled and if
the keep awake condition is no longer
fullfilled.

LIN ID - Settings for starting on a specific LIN ID

This funtionality is the same for CAN and LIN interfaces and has been described in great
detail earlier. Please refer to (→8.1.3.4).

8.14.3.4 Hardware (Channel number)

This tab allows you to set a Channel number for the selected LIN channel. This channel
number has to be unique within the LIN interface.

For better orientation and in order to avoid confusion regarding Chan-
nelnumbers and -names, a Channels physical number can be found in
the logger’s “Web Interface” and set accordingly.

Changesanderrorsexcepted.

261

8.14 LINCHANNELS

8.14.3.5 Bus check

This tab allows you to activate “Bus check” for this bus. You may choose whether you
wish to apply the global bus check settings to this bus or override the global settings with
settings specific for this bus.
Global bus check settings have to be defined first. For information on how to do so and
for general information on “Bus check” please refer to (→4.2.2).

8.14.4 LIN channel Bus statistic

The “Bus statistic” provides a range of statistics and status signals for the respective LIN
channel. It contains information on the current state of the Bus, the Busload, as well as on
the messages that have been received and errors that ocurred.

An overview of the available signals follows below, the general functionality of bus
statistics is the same for CAN and LIN interfaces and has been described in great detail
earlier. Please refer to (→8.1.5).

Overview of signals

Subtype

Controller state

Busload (%)
Number of messages

Message rate total

Meaning
nan= Channel not available
1= Bus on
2= Bus warning
3= Bus off
Bus load of a LIN channel
Number of messages since
beginning of measurement
Current bus load

Unit

-

[%]
-

[frames/s]

Changesanderrorsexcepted.

262

8.15 LINSIGNALS

8.15 LIN signals

8.15.1 Storage method

In order to store incoming signals on a LIN channel use one of the following signal storage
methods.

• ATFX (→ 15.7)

• MDF 4.0 (→ 15.8)

• MDF 4.1 (→ 15.9)

8.15.2 Importing LIN signals

This section explains how to import LIN signals. The filetype to be used for importing LIN
signals is a LINdb (LDF file).

To import signals, select the LIN channel to which you wish to import your signal in the
tree, click the “Import” button in the ribbon and then choose “CANdb” as description file
for the import. For more information on the “description file” refer to (→8.2.4.1).

Changesanderrorsexcepted.

263

8.15 LINSIGNALS

The following window lets you choose which file you wish to import. The dropdown menu
on the bottom right of the window shows you, which filetypes are available. Choose the
file you wish to import and click “Open”.

Once you have opened your file, the “Importer” window will appear, that will present
you with a range of importing options.

In this dialog, all signals that can be imported from the description file are displayed. In
the left table, all signals, where the ”selection” checkboxes are selected, will be marked
for import. You can either choose manually, which signals to import, you can use the
“Select/Deselect all” button on the bottom left, or you can use a CSV-file to determine
which signals are to be imported, by clicking “Select by CSV” on the bottom left.

Changesanderrorsexcepted.

264

8.15 LINSIGNALS

In the right table the properties of the selected signals, the control unit and the protocol
are displayed.

Once you have choosen all the signals you wish to import, click “OK” to complete the
import procedure.

Multiple description files can be imported into the same LIN channel.

8.15.3 Import properties

The “Import properties” of a description file, Message or signal allow you to see certain
properties such as the Data format, the LIN identifier, the Bit mask, the start bit, bit count
and more. It shows the signal’s properties as described by the description file.

Figure 38: Example for “Import properties” of a LIN description file

Figure 39: Example for “Import properties” of a LIN Message

Figure 40: Example for “Import properties” of a LIN signal

Changesanderrorsexcepted.

265

8.15 LINSIGNALS

Figure 41: Example for “Import properties” of a multiplexed signal

To access the “Import properties” rightclick on any desired description file, Message or
signal and then choose “Import properties” from the resulting context menu.

8.15.4 Signal properties

8.15.4.1 Tree elements for LIN signals

After having successfully imported the desired signals to your LIN channel, this channel will
contain two new layers of child elements in the measurement task tree: The “Description
file” and the “Message”.

Description file
information and can be
The “description file” is a database file which contains signal
used to import those signals into a Signal channel in IPEmotion. The filetypes which are
supported by the CAETEC Plugin for IPEmotion depend on the type of signal you wish to
import.

The symbol in the left part of the tree element shows you the type of “description file” you
imported (in this case a “LDF” file), then follows the name of the imported “description
file” (in this case “WIPER_ROOF_...”) and on the right is a number indicating how many
signals the “description file” contains (in this case 117).

Changesanderrorsexcepted.

266

8.15 LINSIGNALS

Message
Each “description file” can contain one or more “Messages”, which then contain the
actual signals. A “Message” can be found in the “Measurement task tree” as a child
element of the “description file”, it belongs to.
Each “Message” can, again, contain one or more signals, which is indicated by the
number on the right of the “Message’s” name.

8.15.4.2 Grid area for LIN signals

In the “grid area” you will be presented with an overview of your selected LIN channel’s
signals. Also you can find here two important functions, which are the “Column chooser”
(→4.2.5) and the “Filter editor” (→4.2.6).

Changesanderrorsexcepted.

267

8.15 LINSIGNALS

8.15.4.3 Details area for LIN signals

The Details area shows settings either for the selected tree element (“description file” or
“Message”) or the selected signal in the grid area. In case a tree element is selected, the
details area will only show the “General” tab. Please refer to (→4.2.2).

In case a signal is selected in the grid area, the details area will contain additional tabs
which will be explained in the following.

General
Please refer to (→4.2.2).

Format
This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “8-Bit integer unsigned”) and allows
you to apply special tasks for this signal such as “GPS Longitude”, “GPS Latitude”,
“UTC hour”, “Audio mono” and more.

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a signal value is read as
invalid.

• Channel type

This field tells you whether you are dealing with a “Input” channel or “Output”
channel.

Changesanderrorsexcepted.

268

8.15 LINSIGNALS

Scaling
The fields accessible directly through the tab allow for basic scaling operations to con-
vert analog measurement in engineering units. The “Scaling calculator” allows for more
refined scaling options with a large range of functions. For details on how to use the
“Scaling calculator” please refer to the IPEmotion Documentation - Section 3.4.5 “Chan-
nel configuration and scaling”.

• Sensor Mode

The sensor mode tells the type of signal. It can be of different types such as “Status”,
“Voltage”, “Frequenzy” or others.
It cannot be changed and serves for IPEmotion
to know what kind of signal it is dealing with.

• Sensor Range

Shows the raw value range of the signal.

• Physical Range

Allows you to set a range to which you would like to “scale” your signal and also
define the unit to use. For more refined scaling please use the “Scaling calculator”
and refer to the IPEmotion Documentation - Section 3.4.5 “Channel configuration
and scaling”.

Changesanderrorsexcepted.

269

8.15 LINSIGNALS

Display
This tab allows you to define what information about the current signal will be shown on a
display if one is connected.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

• Name

Allows you to set a Name to be shown on a display.

Limit values
This tab allows you to define limit values for a signal and what action to take upon a limit
value violation.

• Rejected value

Define what happens to a value, that has been rejected because it is out of bound
or invalid. By default this value will be dropped. It can also be written as NaN.

Changesanderrorsexcepted.

270

8.15 LINSIGNALS

• Valid ranges (Lower/Upper)

Define up to three ranges of valid signal values. Activate a range in order to define
its upper/lower value (datatype double). Range 2 can only be activated if range 1
is and range 3 can only be activated if range 2 is.

• Invalid values (Physical/Raw)

Define up to three invalid values. Activate an invalid value in order to define the
physical value (datatype double) or raw value (datatype integer).
If one of the
two has been typed in, the other will be calculated according to the scale/offset
settings in the scaling calculator.
Invalid value 2 can only be activated if invalid value 1 is and invalid value 3 can
only be activated if invalid value 2 is.
For details on how to use the “Scaling calculator” please refer to the IPEmotion
Documentation - Section 3.4.5 “Channel configuration and scaling”.

Signal
This tab allows you to define signal settings.

• Internal data type

Assign an internal data type to the signal. Available data types are “Double” and
“String”.

• Signal number

Assign a number to the current signal. This way you will later be able to sort the signals
in the grid according to their “Signal numbers”.

• Hold last value

Specify, for how long the last value of the signal will be hold.

• Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may here
select the dataset, to which this setting will refer.

• Timeout

Specify the timeout period for the current signal. If the data source doesn’t send data
for the specified time period, the value of the signal is set to “NaN (Not a Number)”
and will be displayed as “–” in a display.

Changesanderrorsexcepted.

271

8.15 LINSIGNALS

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

• Special task

The field “Special task” allows you to assign a user specific task to a signal, as long as
it has not been assigned to a logger default special task in the “Format” tab yet. If a
special task such as “GPS longitude/latitude/altitude in degrees”, “Vehicle identifi-
cation” or other has been assigned, in the “Format” tab, this field remains uneditable.

For further information regarding user specific special tasks and their properties
please refer to this part of the maual (→8.2.4.3).

Signal check
This tab allows you to activate “Signal check” for this signal. You may choose whether you
wish to apply the global signal check settings to this signal or override the global settings
with settings specific for this signal.
Global signal check settings have to be defined first. For information on how to do so and
for general information on “Signal check” please refer to (→4.2.2).

Changesanderrorsexcepted.

272

8.16 FLEXRAYCHANNELS

8.16 FlexRay channels

To work with “FlexRay channels”, you will first have to add the tree element “FlexRay inter-
faces” to your measurement task tree. To do so, select your system in the measurement
task tree, click the “Components” button in the ribbon and choose “FlexRay interfaces”
from the resulting dropdown menu.

Once the “FlexRay interfaces” component has been added it will appear in the measure-
ment task tree as a tree element with one “FlexRay channel” as a child element.

8.16.1 Storage method

In order to store all incoming traffic on a FlexRay channel use a bus tracing method for
storage. Please refer to (→ 15.10).

Changesanderrorsexcepted.

273

8.16 FLEXRAYCHANNELS

8.16.2 Adding FlexRay channels

FlexRay channels can be added by selecting the tree element “FlexRay interfaces”, then
clicking the “Components” button and then choosing “FlexRay channel”.

FlexRay
Adds a FlexRay channel that corresponds to a physical FlexRay channel of your logger.
For instructions on FlexRay settings refer to (→8.16.3).

Multiple selection
Allows you to add multiple FlexRay channels of both types at the same time. To do so
set the counter for each type to the desired number of channels that you wish to add as
marked in the figure below.

8.16.3 FlexRay settings

By selecting the “FlexRay Interfaces” in the tree and the choosing one of the FlexRay
channels in the grid area you will be able to define this channel’s settings in the details
area.

The same settings described in this section as part of the Details area can
also be adjusted when selecting the desired channel in the grid area and
then directly changing the desired setting in the respective field of the
Grid area.

Changesanderrorsexcepted.

274

8.16 FLEXRAYCHANNELS

8.16.3.1 General

This tab allows you to give a user specific name for the selected FlexRay channel if wished
and add an additional description.
The Reference field serves as the tree element’s
unique identifier inside the measurement task tree. It cannot be changed.

The Active checkbox allows to deactivate the entire bus. If a bus is deac-
tivated all childelements of this bus will be deactivated, too, and cannot
be stored or traced, until the bus is reactivated.

8.16.3.2 Wake On FlexRay

Timeout
Timeout defines how long a waking channel must be inactive to be recognized so and
therefore allow for the logger to shutdown. If timeout is recognized, an entry is made in
the log file and an error message with an alert appears on the display, which has to be
acknowledged.

Changesanderrorsexcepted.

275

8.16 FLEXRAYCHANNELS

Mode
This dropdown menu allows you to set the wake-up function for your selected FlexRay
channel.

Wake on FlexRay type
Disabled

Enabled

Keep awake

Characteristics
No start on FlexRay messages, lowest
energy consumption.
Start on a FlexRay message, with first
messages lost;
low energy consump-
tion.
The logger starts to other awakenings,
but only shuts down if all the awakening-
conditions are no longer fullfilled and if
the keep awake condition is no longer
fullfilled.

8.16.3.3 Hardware (Channel number)

This tab allows you to set a Channel number for the selected FlexRay channel.
channel number has to be unique within the FlexRay interface.

This

For better orientation and in order to avoid confusion regarding Chan-
nelnumbers and -names, a Channels physical number can be found in
the logger’s “Web Interface” and set accordingly.

Changesanderrorsexcepted.

276

8.16 FLEXRAYCHANNELS

8.16.3.4 Bus check

This tab allows you to activate “Bus check” for this bus. You may choose whether you
wish to apply the global bus check settings to this bus or override the global settings with
settings specific for this bus.
Global bus check settings have to be defined first. For information on how to do so and
for general information on “Bus check” please refer to (→4.2.2).

8.16.4 FlexRay channel Bus statistic

The “Bus statistic” provides a range of statistics and status signals for the respective FlexRay
channel. It contains information on the current state of the Bus, the Busload, as well as on
the messages that have been received and errors that ocurred.

The “Bus statistic” only shows statistics for the channel to which it belongs.
For each channel that you would like to see the statistic, you will have to
add the component “Bus statistic”.

8.16.4.1 Adding Bus statistics

Select the channel in the tree for which you would like to add “Bus statistic”, then click the
“Components” button in the Ribbon and choose “Bus statistic”.

Changesanderrorsexcepted.

277

8.16 FLEXRAYCHANNELS

8.16.4.2 Bus statistic signals

Once the component “Bus statistic” has been added to your channel, it will appear in
the measurement task tree as a child element of this channel and the grid area will give
you an overview of the available signals.

The signals included in “Bus statistics” are of the type “Internal signal” and may be
adjusted in the same way. For more information on “Internal signals” please refer to
(→8.26).

Overview of signals

Subtype

FlexRay xx Controller state

FlexRay xx Number of static
messages

FlexRay xx Number of dy-
namic messages

Meaning
nan= Channel not available
1= Bus on
2= Bus warning
3= Bus off
Number of static messages
since beginning of measure-
ment
Number of dynamic mes-
since beginning of
sages
measurement
Number of frames since be-
ginning of measurement

Unit

-

-

-

-

[frames/s]

FlexRay xx Number of null
frames
FlexRay xx Message rate total Average of messages of all

FlexRay xx Number of error
frames
FlexRay xx Error frame rate
FlexRay xx Message rate of
static messages
FlexRay xx Message rate of
dynamic messages
FlexRay xx Null frame rate

types per second
Number of error frames

-

Average of errors per second [frames/s]
[frames/s]
Average of static messages
per second
Average of dynamic mes-
sages per second
Average of null
second

frames per

[frames/s]

[frames/s]

Changesanderrorsexcepted.

278

8.17 FLEXRAYSIGNALS

8.17 FlexRay signals

8.17.1 Storage method

In order to store incoming signals on a FlexRay channel use one of the following signal
storage methods.

• ATFX (→ 15.7)

• MDF 4.0 (→ 15.8)

• MDF 4.1 (→ 15.9)

8.17.2 Importing FlexRay signals

There are three different filetypes
This section explains how to import FlexRay signals.
which can be used in order to import a single FlexRay signal or a group of FlexRay signals:

• Autosar files

• A2L files

• Fibex files

8.17.2.1 Importing Autosar and Fibex files

The procedure for both filtetypes is the same and will be exemplary explained in the
following via the “Fibex” import.

To import Signals, select the FlexRay channel to which you wish to import your signal in
the tree, click the “Import” button in the ribbon and then choose “Autosar” or “Fibex” for
the import. For more information on the “description file” refer to (→8.2.4.1).

Changesanderrorsexcepted.

279

8.17 FLEXRAYSIGNALS

The following window lets you choose which file you wish to import. The dropdown menu
on the bottom right of the window shows you, which filetypes are available. Choose the
file you wish to import and click “Open”.

Once you have opened your file, the “Importer” window will appear, that will present
you with a range of importing options.
In this dialog, all signals that can be imported from the description file are displayed. In
the left table, all signals, where the ”selection” checkboxes are selected, will be marked
for import. You can either choose manually, which signals to import, you can use the
“Select/Deselect all” button on the bottom left, or you can use a CSV-file to determine
which signals are to be imported, by clicking “Select by CSV” on the bottom left.

Changesanderrorsexcepted.

280

8.17 FLEXRAYSIGNALS

In the right table the properties of the selected signals, the control unit and the protocol
are displayed.

Once you have choosen all the signals you wish to import, click “OK” to complete the
import procedure.

Multiple description files can be imported into the same FlexRay chan-
nel.

Flexray signals with multiple cycles, that are coming from the same
sender ECU, will be joined into one single signal.

Changesanderrorsexcepted.

281

8.17 FLEXRAYSIGNALS

8.17.2.2 Importing A2L files (XCP on FlexRay)

The Import of CCP/XCP databases via A2L files for FlexRay follows the same procedure as
the CCP/XCP import via A2L file for CAN. Please refer to (→8.5.2).

When importing signals from a CCP/XCP database via A2L file, you will
need to additionally import the flexray parameters from a Fibex file as
described below.

Importing FlexRay parameters
When creating a FlexRay XCP measurement task via an A2L file, it is necessary to import
the FlexRay parameters via a Fibex file once the A2L file has been imported. Otherwise,
the communication between ECU and FlexRay bus cannot be established.

To import FlexRay parameters, select the FlexRay channel to which you wish to import
your signal in the tree, click the “Import” button in the ribbon and then choose “FlexRay
parameters” for the import.

Changesanderrorsexcepted.

282

8.17 FLEXRAYSIGNALS

The following window lets you choose which Fibex file you wish to import. Choose the file
you wish to import and click “Open”.

The following window lets you choose the ECU controller with which the FlexRay bus
is supposed to communicate. Normally the right controller to choose is called “XCP
Master”. Select your desired controller and confirm with “OK”.

Changesanderrorsexcepted.

283

8.17 FLEXRAYSIGNALS

8.17.3 Import properties

The “Import properties” of a description file, Message or signal allow you to see certain
properties such as the Data format, the FlexRay identifier, the Bit mask, the start bit, bit
It shows the signal’s properties as described by
count, optional commands and more.
the description file.

Figure 42: Example for “Import properties” of a FlexRay description file

Figure 43: Example for “Import properties” of a FlexRay Message

Changesanderrorsexcepted.

284

8.17 FLEXRAYSIGNALS

Figure 44: Example for “Import properties” of a FlexRay signal

Figure 45: Example for “Import properties” of a multiplexed signal

To access the “Import properties” rightclick on any desired description file, Message or
signal and then choose “Import properties” from the resulting context menu.

Changesanderrorsexcepted.

285

8.17 FLEXRAYSIGNALS

8.17.4 Signal properties

8.17.4.1 Tree elements for FlexRay signals

The Tree elements available after import for your FlexRay channel depend on the Method
you used for importing the signals.

If you imported an A2L file, the resulting tree elements will be equal to a CCP/XCP import
on a CAN channel. Please refer to (→8.5.5.1).

If you imported a Fibex file to your FlexRay channel, this channel will contain two new layers
of child elements in the measurement task tree: The “Description file” and the “Message”.

Description file
The “description file” is the database file which contains signal information and can be
used to import those signals into a Signal channel in IPEmotion.

The tree element shows the “description file’s” name (in this case “IPEmotionDemo_Fibex”)
and, on the right, the number of signals it contains (in this case 6).

Message
Each “description file” can contain one or more “Messages”, which then contain the
actual signals. A “Message” can be found in the “Measurement task tree” as a child
element of the “description file”, it belongs to.
Each “Message” can, again, contain one or more signals, which is indicated by the
number on the right of the “Message’s” name.

Changesanderrorsexcepted.

286

8.17 FLEXRAYSIGNALS

8.17.4.2 Grid area for FlexRay signals

In the “grid area” you will be presented with an overview of your selected FlexRay chan-
nel’s signals. Also you can find here two important functions, which are the “Column
chooser” (→4.2.5) and the “Filter editor” (→4.2.6).

8.17.4.3 Details area for FlexRay signals

The Details area shows settings either for the selected tree element (“description file” or
“Message”) or the selected signal in the grid area. In case a tree element is selected, the
details area will only show the “General” tab. Please refer to (→4.2.2).

In case a signal is selected in the grid area, the details area will contain additional tabs
which will be explained in the following.

General
This tab allows you to activate or deactivate the entire signal by ticking/unticking the
checkbox, give a user specific name to your signal
if wished and add an additional
description. The Reference field serves as the tree element’s unique identifier inside the
measurement task tree.
It cannot be changed. The “Sampling rate” allows you to set,
how frequently a signal should be requested.

Format
This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “16-Bit integer unsigned”) and allows
you to apply special tasks for this signal such as “GPS Longitude”, “GPS Latitude”,
“UTC hour”, “Audio mono” and more.

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a signal value is read as
invalid.

• Channel type

This field tells you whether you are dealing with a “Input” channel or “Output”

Changesanderrorsexcepted.

287

8.17 FLEXRAYSIGNALS

channel.

Scaling
The fields accessible directly through the tab allow for basic scaling operations to
convert analog measurement in engineering units. The “Scaling calculator” allows for
more refined scaling options with a large range of functions. For details on how to use
the “Scaling calculator” please refer to the IPEmotion Documentation - Section 3.4.5
“Channel configuration and scaling”.

In some cases it may be necessary to activate editing of protocol
channel scaling in order to gain full acces to the scaling functionality.
For instructions please refer to the point “Edit protocol channel scaling”
of the Expert settings (→ 3.2.2).

• Sensor Mode

The sensor mode tells the type of signal. It can be of different types such as “Status”,
“Voltage”, “Frequenzy” or others.
It cannot be changed and serves for IPEmotion
to know what kind of signal it is dealing with.

• Sensor Range

Shows the raw value range of the signal.

• Physical Range

Allows you to set a range to which you would like to “scale” your signal and also
define the unit to use. For more refined scaling please use the “Scaling calculator”
and refer to the IPEmotion Documentation - Section 3.4.5 “Channel configuration
and scaling”.

Changesanderrorsexcepted.

288

8.17 FLEXRAYSIGNALS

Display
This tab allows you to define what information about the current signal will be shown on a
display if one is connected.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

• Name

Allows you to set a Name to be shown on a display.

If the regular FlexRay namespace creates ambiguous names, it may
be useful, to work with extended FlexRay namespaces. For instructions
please refer to (→3.2.2).

Changesanderrorsexcepted.

289

8.17 FLEXRAYSIGNALS

Limit values
This tab allows you to define limit values for a signal and what action to take upon a limit
value violation.

• Rejected value

Define what happens to a value, that has been rejected because it is out of bound
or invalid. By default this value will be dropped. It can also be written as NaN.

• Valid ranges (Lower/Upper)

Define up to three ranges of valid signal values. Activate a range in order to define
its upper/lower value (datatype double). Range 2 can only be activated if range 1
is and range 3 can only be activated if range 2 is.

• Invalid values (Physical/Raw)

Define up to three invalid values. Activate an invalid value in order to define the
physical value (datatype double) or raw value (datatype integer).
If one of the
two has been typed in, the other will be calculated according to the scale/offset
settings in the scaling calculator.
Invalid value 2 can only be activated if invalid value 1 is and invalid value 3 can
only be activated if invalid value 2 is.
For details on how to use the “Scaling calculator” please refer to the IPEmotion
Documentation - Section 3.4.5 “Channel configuration and scaling”.

Changesanderrorsexcepted.

290

8.17 FLEXRAYSIGNALS

Signal
This tab allows you to define signal settings.

• Internal data type

Assign an internal data type to the signal. Available data types are “Double” and
“String”.

• Signal number

Assign a number to the current signal. This way you will later be able to sort the signals
in the grid according to their “Signal numbers”.

• Hold last value

Specify, for how long the last value of the signal will be hold.

• Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may here
select the dataset, to which this setting will refer.

• Timeout

Specify the timeout period for the current signal. If the data source doesn’t send data
for the specified time period, the value of the signal is set to “NaN (Not a Number)”
and will be displayed as “–” in a display.

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

• Special task

The field “Special task” allows you to assign a user specific task to a signal, as long as
it has not been assigned to a logger default special task in the “Format” tab yet. If a
special task such as “GPS longitude/latitude/altitude in degrees”, “Vehicle identifi-
cation” or other has been assigned, in the “Format” tab, this field remains uneditable.

For further information regarding user specific special tasks and their properties
please refer to this part of the maual (→8.2.4.3).

Changesanderrorsexcepted.

291

8.17 FLEXRAYSIGNALS

Signal check
This tab allows you to activate “Signal check” for this signal. You may choose whether you
wish to apply the global signal check settings to this signal or override the global settings
with settings specific for this signal.
Global signal check settings have to be defined first. For information on how to do so and
for general information on “Signal check” please refer to (→4.2.2).

Changesanderrorsexcepted.

292

8.18 GPSSIGNALS

8.18 GPS Signals

The GPS module sends a constant stream of values to the logger. Its configuration defines
which values from this data stream are to be evaluated and made available for further
use.

8.18.1 Storage method

In order to store incoming GPS signals you can use the GPX storage method. These signals
will then be stored in a separate file only containing your GPS signals.

• GPX (→ 15.14)

You can also store your GPS signals together with signals from other buses. To do so use
one of the following signal storage methods.

• ATFX (→ 15.7)

• MDF 4.0 (→ 15.8)

• MDF 4.1 (→ 15.9)

8.18.2 Adding GPS Signals

8.18.2.1 CAETEC GPS module

In order to use the CAETEC GPS module, select your system (Arcos 1.x, μcros) in the “Mea-
surement task tree”, click the “Components” button in the Ribbon and choose “GPS”.

Changesanderrorsexcepted.

293

8.18 GPSSIGNALS

8.18.2.2 Other GPS signals (Assigning GPS signals)

If you are not using the CAETEC GPS module, but are receiving GPS signals on your logger
GPS tasks have to be manually assigned to the respective signals in order to store those
signals in a GPX file.
To assign a GPS task to a signal, select the desired signal in the “Grid area” and then
activate it by ticking the “Active” box in the signal’s “Details area”.

Then navigate to the “Format” tab in the signal’s “Details area” and use the dropdown
menu “Tasks” to assign the desired GPS task.

Changesanderrorsexcepted.

294

8.18 GPSSIGNALS

Each GPS task can only be assigned to one signal. That means, if you reassign a previ-
ously already assigned GPS task to a new signal, make sure to unassign this task from its
previously assigned signal.

Using the “Check” function will tell you, whether you have multiply assigned tasks.

8.18.3 Signal properties

8.18.3.1 Tree elements for GPS signals

There is one tree element for GPS signals, called “GPS”. In the right table of the “Measure-
ment task tree” a number will indicate how many active signals it contains (in this case 2).

8.18.3.2 Grid area for GPS signals

In the “Grid area” you will be presented with an overview of the availabe GPS signals.
Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

OverviewofGPSsignals

Subtype
GPS date
GPS altitude
GPS horizontal precision
GPS estimated horizontal pre-
cision

GPS track angle
GPS latitude
GPS longitude
GPS satellites number

GPS status

GPS time
GPS speed

Unit
-
[m]

[m]

[°]
[°]
[°]
-

Meaning
GPS date UTC yymmdd
Elevation above sea level
Horizontal Dilution of Precision -
Estimation of horizontal dilu-
tion of precision (probability
95%)
Inclination of the track
Latitude
Longitude
Number of received satellites
0 = no connection
1 = connection
2 = Egnos active
GPS time UTC hhmmss
Current speed

-

-
[km/h]

8.18.3.3 Details area for GPS signals

The Details area shows settings either for the tree element “GPS” or a selected signal in
the grid area. In case the tree element “GPS” is selected, the details area will only show
the “General” tab. Please refer to (→4.2.2).

Changesanderrorsexcepted.

295

8.18 GPSSIGNALS

In case a signal is selected in the grid area, the details area will contain additional tabs
which will be explained in the following.

General
This tab allows you to activate or deactivate the entire signal by ticking/unticking the
checkbox, give a user specific name to your signal
if wished and add an additional
description. The Reference field serves as the tree element’s unique identifier inside the
It cannot be changed. The “Sampling rate” allows you to set,
measurement task tree.
how frequently a signal should be requested.

Format
This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “32-Bit integer unsigned”) and allows
you to apply special tasks for this signal such as “GPS Longitude”, “GPS Latitude”,
“UTC hour”, “Audio mono” and more.

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a signal value is read as
invalid.

• Channel type

This field tells you whether you are dealing with a “Input” channel or “Output”
channel.

Changesanderrorsexcepted.

296

8.18 GPSSIGNALS

Scaling
The fields accessible directly through the tab allow for basic scaling operations to
convert analog measurement in engineering units. The “Scaling calculator” allows for
more refined scaling options with a large range of functions. For details on how to use
the “Scaling calculator” please refer to the IPEmotion Documentation - Section 3.4.5
“Channel configuration and scaling”.

In some cases it may be necessary to activate editing of protocol
channel scaling in order to gain full acces to the scaling functionality.
For instructions please refer to the point “Edit protocol channel scaling”
of the Expert settings (→ 3.2.2).

• Sensor Mode

The sensor mode tells the type of signal. It can be of different types such as “Status”,
“Voltage”, “Frequenzy” or others.
It cannot be changed and serves for IPEmotion
to know what kind of signal it is dealing with.

• Sensor Range

Shows the raw value range of the signal.

• Physical Range

Allows you to set a range to which you would like to “scale” your signal and also
define the unit to use. For more refined scaling please use the “Scaling calculator”
and refer to the IPEmotion Documentation - Section 3.4.5 “Channel configuration
and scaling”.

Changesanderrorsexcepted.

297

8.18 GPSSIGNALS

Display
This tab allows you to define what information about the current signal will be shown on a
display if one is connected.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

• Name

Allows you to set a Name to be shown on a display.

Signal
This tab allows you to define signal settings.

• Signal number

Assign a number to the current signal. This way you will
signals in the grid according to their “Signal numbers”.

later be able to sort the

• Hold last value

Specify, for how long the last value of the signal will be hold.

Changesanderrorsexcepted.

298

8.18 GPSSIGNALS

• Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may here
select the dataset, to which this setting will refer.

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

• Origin

Tells the source of the signal. This can help identifying the source of a signal for
which a user defined signal name has been set.

• Special task

The field “Special task” allows you to assign a user specific task to a signal, as long as
it has not been assigned to a logger default special task in the “Format” tab yet. If a
special task such as “GPS longitude/latitude/altitude in degrees”, “Vehicle identifi-
cation” or other has been assigned, in the “Format” tab, this field remains uneditable.

For further information regarding user specific special tasks and their properties
please refer to this part of the maual (→8.2.4.3).

Signal check
This tab allows you to activate “Signal check” for this signal. You may choose whether you
wish to apply the global signal check settings to this signal or override the global settings
with settings specific for this signal.
Global signal check settings have to be defined first. For information on how to do so and
for general information on “Signal check” please refer to (→4.2.2).

Changesanderrorsexcepted.

299

8.19 VIDEODEVICES

8.19 Video devices

In order to work with video signals, you will first need to add a video device to your system.
There are three different video devices, that you can work with:

• Video Interface (→8.19.2)

• USB camera (→8.19.3)

• Ethernet camera (→8.19.4)

8.19.1 Storage method

In order to store an incoming signal on a video device use “AVI” as storage method.
Please refer to (→ 15.12).

8.19.2 Video Interface

The “Video Interface” provides a set of four analog cameras, which are connected to
your logger. It provides five signals, one for each camera and a combination of all four
camera signals called “Quad camera”. The “Quad camera” provides a single video
signal which contains all four original signals at a quarter of their original resolution, and
presents a 4 in 1 picture.
For communication between the cameras and the interface it needs to have its own
subnet, in which only the “Video Interface” operates.

The “Video Interface” is a deprecated product and is not bein sold any-
more.

Changesanderrorsexcepted.

300

8.19 VIDEODEVICES

8.19.2.1 Adding the Video Interface

The “Video Interface” can be added by selecting the system in the “Measurement task

tree”, then clicking the “Components” button and finally choosing “Video Interface”

8.19.2.2 Tree elements for the Video Interface

Adding the “Video Interface” to your system will add seven new elements to your

“Measurement task tree”:

• Video Interface xx

This item represents the entire “Video Interface” and all the included child elements.

• Cameras

This item is a child element of the “Video Interfaces” element and represents all the
included cameras.

• Camera xx

There are four elements named “Camera xx”, they represent the four phyisical cam-
eras connected to the logger.

• Quad Camera

The “Quad Camera” is a virtual camera, that combines the four signals of the four

Changesanderrorsexcepted.

301

8.19 VIDEODEVICES

physical cameras in one single image. The image is divided into four quarters. Each
quarter contains one of the physical cameras images.

8.19.2.3 Grid area for the Video Interface

In the “grid area” you will be presented with an overview of the “Video Interface’s”
signals. There will be five signals. Signal five is the signal from the “Quad Camera”. Also
you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

Changesanderrorsexcepted.

302

8.19 VIDEODEVICES

8.19.2.4 Details area for the Video Interface

The Details area shows settings either for the tree element “Video Interface xx” or one of
its child elements.
In case the tree element “Cameras” is selected, the details area will
only show the “General” tab. Please refer to (→4.2.2).

The “Details area” for video signal will be handled in a separate chapter. Please refer to
the Chapter “Video signals” (→8.20).

In case the “Video Interface” or one of the “Camera” elements is selected in the tree,
the “Details area” will contain additional tabs, which will be explained in the following.

General
This tab allows you to activate or deactivate the entire tree element by ticking/unticking
the checkbox, give a user specific name to tree element if wished and add an additional
description. The Reference field serves as the tree element’s unique identifier inside the
measurement task tree. It cannot be changed.

Settings (for Video Interface)
This tab allows you to define the settings for the entire “Video Interface”.

• Channel number

Define the number of the “Video Interface” hardware channel.

Changesanderrorsexcepted.

303

8.19 VIDEODEVICES

For better orientation and in order to avoid confusion regarding Chan-
nelnumbers and -names, a Channels physical number can be found in
the logger’s “Web Interface” and set accordingly.

• Network address

Define the network adress of the subnet in which your “Video Interface” communi-
cates.

• Subnet mask

The subnet mask for your “Video Interface”. It cannot be changed.

Settings (for Camera elements)
This tab allows you to define the settings for the entire “Camera” child elements of your
“Video Interface”.

• Channel

The physical channel, on which the camera operates. It cannot be changed.

• Time compensation

Define the compensation of the video capture latency. This value is experience
based and can vary.

• Rotation

Allows you to rotate the video in steps of 90°.

• Resolution

Allows you to set the video’s resolution to either full or one quarter.

Changesanderrorsexcepted.

304

8.19 VIDEODEVICES

• Mirror

Checking the box will mirror the image of the video.

• Compression rate

Allows you to define the compression rate of your video.

8.19.3 USB camera

The“Camera” component for USB allows you to connect a digital video camera via USB
to your logger and control it.

It is possible to add multiple USB cameras to your logger.

8.19.3.1 Adding a USB camera

The “Camera” component for USB can be added by selecting the tree element “USB”
in the “Measurement task tree”, then clicking the “Components” button and finally
choosing “Camera”

Changesanderrorsexcepted.

305

8.19 VIDEODEVICES

8.19.3.2 Tree elements for USB camera

Adding the “Camera” component for USB to your system will add two new elements to

your “Measurement task tree”:

• Camera

This item represents the camera itself.

• USB Video

This item represents the video, that you will receive from the camera.

8.19.3.3 Grid area for USB camera

In the “grid area” you will see the video signal coming from your connected USB camera.

8.19.3.4 Details area for USB camera

The Details area shows settings either for the tree element “Camera” or its child element
“USB Video”.

Video signal settings will be handled in a separate chapter. Please refer
to the Chapter “Video signals” (→8.20).

Changesanderrorsexcepted.

306

8.19 VIDEODEVICES

Settings for “Camera”

General
“General” tab. Please refer to (→4.2.2).
Hardware
Set the digital hardware channel number, that corresponds with the camera’s physical
hardware channel number. To find out the corresponding hardware channel numbers
please consult your loggers webinterface.

Settings for “USB Video”

General
This tab allows you to activate or deactivate the entire tree element by ticking/unticking
the checkbox, give a user specific name to tree element if wished and add an additional
description. The Reference field serves as the tree element’s unique identifier inside the
measurement task tree. It cannot be changed.

Changesanderrorsexcepted.

307

8.19 VIDEODEVICES

Video
This tab allows you to define the settings for the incoming video.

• Time compensation

Define the compensation of the video capture latency. This value is experience
based and can vary.

• Width

Define the video capture resolution width in pixel.

• Height

Define the video capture resolution height in pixel.

• Autofocus

Allows you to enable or disable the the camera’s autofocus.

• Focus

When “Autofocus” has been disabled, this field allow you to set the focus of the
camera.
APPROXIMATE and CALIBRATED devices report the focus metadata in units of
diopters (1/meter), so 0.0f represents focusing at infinity, and increasing positive
The focus
numbers represent focusing closer and closer to the camera device.
distance control also uses diopters on these devices.

Changesanderrorsexcepted.

308

8.19 VIDEODEVICES

8.19.4 Ethernet camera

The “Camera” component for Ethernet allows you to connect a digital video camera via
Ethernet to your logger and control it.

8.19.4.1 Adding an ETH camera

The “Camera” component for ETH can be added by selecting the tree element “Front”,
which is a childelement to the tree element “ETH Interfaces” in the “Measurement task
tree” or by selecting any manually added “ETH” channel, then clicking the “Compo-
nents” button and finally choosing “Camera”.

Changesanderrorsexcepted.

309

8.19 VIDEODEVICES

In the next step you select the newly created tree element “Camera”, then click the
“Components” button and finally choose the desired camera model.
At the moment the Plugin support three third party cameras, “Basler”, “Linksys” and “Axis
F44”.
If your camera is not listed, you can simply choose “Custom” and then set the
necessary setting manually.

The “Axis F44” is a four channel camera, which provides 5 video signals. One for each
channel plus a combined signal which contains all four channel in a split screen. The
settings specific for the “Axis F44” signals can be found here (→8.20.2).

It is possible, to add multiple cameras on the same channel/network.
The PlugIn will check these cameras’ network settings for coherence. If
the network settings are not set correctly, this will produce a warning at
export.

Changesanderrorsexcepted.

310

8.19 VIDEODEVICES

Once a new camera for Ethernet has been added, you may encounter
problems regarding the cameras IP settings.
In order to resolve this problem, DHCP has to be disabled for the tree
element “Camera” and IP adresses have to be set for both, the tree
element “Camera” and its child element, the cameratype you have
previously choosen. The IP addresses must belong to the same subnet,
and this subnet must not be used by any other operator of the system.

To do so, select the tree element that contains your ETH camera navi-
gate to the “LAN” tab in the details area, untick the checkbox “Get IP
address automatically” and set a new IP address.
The first three numbers of your IP address mark the subnet, so they cannot
be equal to any other operators IP address, that is not a childelement
to the currently selected tree element. The last number marks the client
inside the subnet.
It has to be higher equal or higher than “1” and
unique inside its respective subnet.

Then select your chosen cameratype in the tree (Basler, Linksys or
Custom) and navigate to the “Connection” tab in the details area.
Here you need to set an IP address that belongs to the same subnet as
the one defined in the last step, but, again, with a unique client identifier.

Changesanderrorsexcepted.

311

8.19 VIDEODEVICES

8.19.4.2 Tree elements for ETH camera

Adding the “Camera” component for ETH to your system will add two new elements to

your “Measurement task tree”.

• Camera

This item represents the camera interface.

• Basler/Linksys/Axis F44/Custom

This item represents the specific type of camera, that you have connected are con-
figuring.

8.19.4.3 Grid area for ETH camera

In the “grid area” you will see the video signal coming from your connected ETH camera.

8.19.4.4 Details area for ETH camera

The Details area shows settings either for the tree element “Camera” or its child element
“Basler/Linksys/Custom”. In case the tree element “Camera” is selected, the details area
will only show the “General” tab. Please refer to (→4.2.2).

The “Details area” for video signals will be handled in a separate chapter. Please refer to
the Chapter “Video signals” (→8.20).

In case the childelement “Basler/Linksys/Custom” is selected in the tree, the “Details
area” will contain additional tabs, which will be explained in the following.

Changesanderrorsexcepted.

312

8.19 VIDEODEVICES

General
This tab allows you to activate or deactivate the entire tree element by ticking/unticking
the checkbox, give a user specific name to tree element if wished and add an additional
description. The Reference field serves as the tree element’s unique identifier inside the
measurement task tree. It cannot be changed.

Video
This tab allows you to define the settings for the incoming video.

• Time compensation

Define the compensation of the video capture latency. This value is experience
based and can vary.

• Width

Define the video capture resolution width in pixel.

• Height

Define the video capture resolution height in pixel.

Changesanderrorsexcepted.

313

8.19 VIDEODEVICES

Connection
This tab contains settings according the connection of the camera with the ETH interface.

• IP address

Define the IP address of your camera. It has to belong to the same unique subnet
(The first three out of the four numbers define the subnet) as the ETH channel to
which it belongs and it needs to have a unique client identifier (the last out of the
four number defines the client identifier).

• IP port

Define the IP port of the video stream.

• URL

Set the URL on which your cameras stream is to be found. This information should be
found in your camera’s manual or on the manufacturer’s website.

When working with one of the two already supported models (Basler
or Linksys) this field will not be accessible, as the URL is already defined.
When working with the Custom profile for other cameras you will need
to fill in the URL of your camera stream, otherwise the logger will not now
where to look for it and will not receive a video signal.

Changesanderrorsexcepted.

314

8.20 VIDEOSIGNALS

8.20 Video signals

The video signals, received from any of the three camera types is are equal in fuctionality.
The setting for these signals can be set over the “Details area” for each respective signal
and will be explained in the following.

8.20.1 Storage method

In order to store a video signal use “AVI” as storage method. Please refer to (→ 15.12).

8.20.2 Settings for video signals

General
This tab allows you to activate or deactivate the entire signal by ticking/unticking the
checkbox, give a user specific name to your signal if wished and add an additional de-
scription. The Reference field serves as the tree element’s unique identifier inside the mea-
surement task tree. It cannot be changed.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

Format
Settings in the “Format”-tab do not have any effect on video signals and will therefore
not be explained here.

Changesanderrorsexcepted.

315

8.20 VIDEOSIGNALS

Display
The only setting in the “Display”-tab relevant for video signals is the “Name” setting.
allows you to set a Name to be shown on a display.

It

Signal
This tab allows you to define signal settings.

• Signal number

Assign a number to the current signal. This way you will
signals in the grid according to their “Signal numbers”.

later be able to sort the

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

Changesanderrorsexcepted.

316

8.20 VIDEOSIGNALS

Extended (Axis F44 settings)
This tab contains information specific for signals coming from the “Axis F44” or other multi
channel cameras.

The URL under which the signal stream will be stored can be dynamically configured using
the drop down menus and check box of the options “Resolution”, “Rotation”, “Compres-
sion” and “Mirror” in this tab.

• Camera

Tells you from which camera channel the signal is coming from.

• URL

Tells you the URL under which the signal stream can be found.

• Framerate

Define the framerate of the video signal. The value in this field will be part of the
video stream’s URL.

• Resolution

Define the resolution of the video signal. The value in this field will be part of the
video stream’s URL.

• Rotation

Define the rotation of the video signal. The value in this field will be part of the video
stream’s URL.

• Compression

Define the compression of the video signal. The value in this field will be part of the
video stream’s URL.

Changesanderrorsexcepted.

317

8.20 VIDEOSIGNALS

• Mirror

Set whether the video signal should be mirrored. The value in this field will be part of
the video stream’s URL.

Extended (Custom cameras)
This tab allows you to define the URL under which the signal stream will be stored.

Signal check
This tab allows you to activate “Signal check” for this signal. You may choose whether you
wish to apply the global signal check settings to this signal or override the global settings
with settings specific for this signal.
Global signal check settings have to be defined first. For information on how to do so and
for general information on “Signal check” please refer to (→4.2.2).

Changesanderrorsexcepted.

318

8.21 AUDIORECORDING

8.21 Audio recording

For audio recordings you can connect a microphone to the logger via CAN. The logger
will receive the audio signals on one of the CAN channels.

8.21.1 Storage method

In order to store an audio recording use “WAV” as storage method. Please refer to (→
15.13).

8.21.2 Adding an Audio recording

To add an “Audio recording” select the CAN channel to which you wish to add the
recording, click the “Components” button in the Ribbon and then choose “Audio
recording”.

Changesanderrorsexcepted.

319

8.21 AUDIORECORDING

Once the “Audio recording” component has been added, select the newly created
tree element “Audio recording” in the respective CAN channel, click the “Components”
button in the Ribbon and then choose one of the two available microphones.

For instructions on microphone specific settings please refer to (→8.21.5).

8.21.3 Tree elements for Audio recordings

Adding an “Audio recording” to your system will add five new elements to your “Mea-
surement task tree”:

• Audio recording

This item represents the entire “Audio recording” and all the included child elements.

• G.I.N. CASM2T3L / G.I.N. VoCAN

This item represents the microphone which you have connected to the logger. At
the moment these are the only supported microphone models.

• Signals

This element contains the incoming audio signal.

• LEDs

This element represents the microphone’s LEDs. By selecting this item you will be
able to give user specific names to the single LEDs in the details area.

• Buttons

This element represents the microphone’s Buttons. By selecting this item you will be
able to give user specific names to the single Buttons in the details area.

Changesanderrorsexcepted.

320

8.21 AUDIORECORDING

8.21.3.1 Grid area for Audio recordings

In the “grid area” you will see the incoming audio signal. Also you can find here two
important functions, which are the “Column chooser” (→4.2.5) and the “Filter editor”
(→4.2.6).

Changesanderrorsexcepted.

321

8.21 AUDIORECORDING

8.21.4 Details area for Audio recording

When selecting the audio signal in the grid area, you will be able to access the signal’s
settings in the details area.

General
This tab allows you to activate or deactivate the entire signal by ticking/unticking the
checkbox, give a user specific name to your signal if wished and add an additional de-
scription. The Reference field serves as the tree element’s unique identifier inside the mea-
surement task tree. It cannot be changed.
The sampling rate allows you to set the frequency in which the logger will receive the sig-
nal.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

Changesanderrorsexcepted.

322

8.21 AUDIORECORDING

Format
This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “16-Bit integer unsigned”) and allows
you to special tasks for this signal such as “Audio mono”.

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a signal value is read as
invalid.

Scaling
The settings in the “Scaling”-tab are not relevant for working with audio recordings.

Display
The only setting in the “Display”-tab relevant for audio recordings is the “Name” setting. It
allows you to set a name to be shown on a display.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

Changesanderrorsexcepted.

323

8.21 AUDIORECORDING

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

• Name

Allows you to set a Name to be shown on a display.

Signal
This tab allows you to define signal settings.

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

Changesanderrorsexcepted.

324

8.21 AUDIORECORDING

8.21.5 Microphone settings

Both supported microphones, the G.I.N. VoCAN and the G.I.N. CASM2T3L allow for some
user specific configuration, which will be explained in the following. With the exception of
a few functions these settings are the same for both models. Whenever there is a function
specific to one of the models, this will be noted in parenthesis.

8.21.5.1 Signals

The signal settings for Audio recordings have been explained at the beginning of this
chapter in the section Grid area for Audio recording (→8.21.3.1) and the section Details
area for Audio recording (→8.21.4).

8.21.5.2 LEDs

Both models come with a number of LEDs (G.I.N. VoCAN with 4 LEDs and G.I.N. CASM2T3L
wit 3 LEDs), whose behaviour can be customized. To adapt the settings for a desired
LED, click on the “LEDs” element in the tree, select the desired LED in the grid area and
navigate to the details area.

General
This tab allows you to to give a user specific name and description to the LED.

Trigger
This tab allows you to assign a trigger to the LED, upon whose firing the LED will light up.

Changesanderrorsexcepted.

325

8.21 AUDIORECORDING

8.21.5.3 Buttons

Both models come with a number of buttons, whose activation will set a trigger. The
associated triggers cannot be changed. To see an overview of the available buttons
select the “Buttons” element in the tree and navigate to the grid area.

Select any of the Buttons (Triggers) in the grid area and navigate to the “Extended” tab
of the details area to finde the “Trigger groups” setting. This setting allows you to see
how many trigger groups this trigger has been assigned to. The “Assign” button opens a
selection dialog which lets you change the trigger group assignment of the trigger.

Triggergroupassignment:

Changesanderrorsexcepted.

326

8.21 AUDIORECORDING

Overviewofbuttonspermicrophonemodel

Microphone model
G.I.N. VoCAN
G.I.N. CASM2T3L

Overview of buttons
Red button 01 (physical)
Red button 01 (physical)
Microphone button 01 (physi-
cal)
Any button 01 (virtual)

While the “Red button 01” and the “Microphone button 01” are both physical buttons,
there is an additional button for the “G.I.N. CASM2T3L” model, labeled “Any button 01”,
that is strictly speaking no button, but only a trigger. It allows you set up the two physical
buttons (Red & Microphone button) as the same button. That means, they are both
connected with the same trigger and can be used as equals by the driver.

If the “Any button 01” is set to active in the grid area, this will automatically deactivate
the other two buttons. On the other hand, as soon as one of the other two buttons is set
to active in the grid area, the “Any button 01” will be set to inactive.

Changesanderrorsexcepted.

327

8.22 DIN(DIGITALINPUTSIGNALS)

8.22 DIN (Digital input signals)

The “DIN” module offers a digital bit-channel, which is directly configured as a digital signal
and then acquired.This means they can be used in the logger configuration in the same
way as conventional bus signals.

8.22.1 Storage method

In order to store incoming signals on a DIN channel use one of the following signal storage
methods.

• ATFX (→ 15.7)

• MDF 4.0 (→ 15.8)

• MDF 4.1 (→ 15.9)

8.22.2 Adding the DIN-Interface

In order to work with digital input signals, you will first need to add the “DIN” interface to
your system. To do so, select the system in the tree, click the “Components” button in the
Ribbon and then choose “DIN”.

Changesanderrorsexcepted.

328

8.22 DIN(DIGITALINPUTSIGNALS)

Once the “DIN” interface has been added to your system, you can then add multiple
“DIN” channels, in order to acquire digital signals. To do so, select the “DIN” interface in
the tree, click the “Components” button in the Ribbon and then choose “DIN”.

In order to acquire digital signals via “DIN” channels, each “DIN”
channel needs to be matched with the corresponding digital hardware
channels of the logger. To find out the digital hardware channel num-
bers please consult your loggers webinterface.
Once you know the hardware channel number, navigate to the “Sig-
nals” tab in “Details area” of the corresponding “DIN” channel
in the
grid area and enter the number.

Changesanderrorsexcepted.

329

8.22 DIN(DIGITALINPUTSIGNALS)

8.22.3 Signal properties

8.22.3.1 Tree elements for DIN signals

After having added the “DIN” interface to your system it will appear as a tree element
with the name “DIN”.

8.22.3.2 Grid area for DIN signals

In the “grid area” you will be presented with an overview of the DIN channels which have
been added to your system so far. Each DIN channel can only receive one signal and
therefore each DIN channel is treated as a signal.
Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

8.22.3.3 Details area for DIN signals

The Details area shows settings either for the selected tree element “DIN” or the selected

Changesanderrorsexcepted.

330

8.22 DIN(DIGITALINPUTSIGNALS)

“DIN” channel in the grid area. In case the tree element is selected, the details area will
only show the “General” tab. Please refer to (→4.2.2).

In case a “DIN” channel is selected in the grid area, the details area will contain additional
tabs which will be explained in the following.

General
Please refer to (→4.2.2).

Format
This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “1-Bit”) and allows you to apply
special tasks for this signal such as “GPS Longitude”, “GPS Latitude”, “UTC hour”,
“Audio mono” and more.

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a signal value is read as
invalid.

• Channel type

This field tells you whether you are dealing with a “Input” channel or “Output”
channel.

Scaling
The fields accessible directly through the tab allow for basic scaling operations to con-
vert analog measurement in engineering units. The “Scaling calculator” allows for more
refined scaling options with a large range of functions. For details on how to use the
“Scaling calculator” please refer to the IPEmotion Documentation - Section 3.4.5 “Chan-
nel configuration and scaling”.

• Sensor Mode

Changesanderrorsexcepted.

331

8.22 DIN(DIGITALINPUTSIGNALS)

The sensor mode tells the type of signal. It can be of different types such as “Status”,
“Voltage”, “Frequenzy” or others.
It cannot be changed and serves for IPEmotion
to know what kind of signal it is dealing with.

• Sensor Range

Shows the raw value range of the signal.

• Physical Range

Allows you to set a range to which you would like to “scale” your signal and also
define the unit to use. For more refined scaling please use the “Scaling calculator”
and refer to the IPEmotion Documentation - Section 3.4.5 “Channel configuration
and scaling”.

Changesanderrorsexcepted.

332

8.22 DIN(DIGITALINPUTSIGNALS)

Display
This tab allows you to define what information about the current signal will be shown on a
display if one is connected.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

• Name

Allows you to set a Name to be shown on a display.

Signal
This tab allows you to define signal settings.

• Signal number

Assign a number to the current signal. This way you will
signals in the grid according to their “Signal numbers”.

later be able to sort the

• Hold last value

Specify, for how long the last value of the signal will be hold.

Changesanderrorsexcepted.

333

8.22 DIN(DIGITALINPUTSIGNALS)

• Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may here
select the dataset, to which this setting will refer.

• Timeout

Specify the timeout period for the current signal.
data for the specified time period, the value of the signal
Number)” and will be displayed as “–” in a display.

If the data source doesn’t send
is set to “NaN (Not a

• Hardware channel

Assign the corresponding digital hardware channel number from which you would
like to acquire data.
The hardware channel number can be found out via the
logger’s webinterface.

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

• Special task

The field “Special task” allows you to assign a user specific task to a signal, as long as
it has not been assigned to a logger default special task in the “Format” tab yet. If a
special task such as “GPS longitude/latitude/altitude in degrees”, “Vehicle identifi-
cation” or other has been assigned, in the “Format” tab, this field remains uneditable.

For further information regarding user specific special tasks and their properties
please refer to this part of the maual (→8.2.4.3).

Signal check
This tab allows you to activate “Signal check” for this signal. You may choose whether you
wish to apply the global signal check settings to this signal or override the global settings
with settings specific for this signal.
Global signal check settings have to be defined first. For information on how to do so and
for general information on “Signal check” please refer to (→4.2.2).

Changesanderrorsexcepted.

334

8.23 DOUT(DIGITALOUTPUTSIGNALS)

8.23 DOUT (Digital output signals)

The “DOUT” module offers a digital bit-channel on which a calculated digital signal can
be put out.

8.23.1 Storage method

In order to store outgoing signals on a DOUT channel use one of the following signal
storage methods.

• ATFX (→ 15.7)

• MDF 4.0 (→ 15.8)

• MDF 4.1 (→ 15.9)

8.23.2 Adding the DOUT-Interface

In order to work with digital output signals, you will first need to add the “DOUT” interface
to your system. To do so, select the system in the tree, click the “Components” button in
the Ribbon and then choose “DOUT”.

Once the “DOUT” interface has been added to your system, you can then add multiple
“DOUT” channels, in order to put out digital signals. To do so, select the “DOUT” interface

Changesanderrorsexcepted.

335

8.23 DOUT(DIGITALOUTPUTSIGNALS)

in the tree, click the “Components” button in the Ribbon and then choose “DOUT”.

In order to put out digital signals via “DOUT” channels, each “DOUT”
channel needs to be matched with the corresponding digital hardware
channels of the logger. To find out the digital hardware hannel numbers
please consult your loggers webinterface.
Once you know the hardware channel number, navigate to the “Sig-
nals” tab in “Details area” of the corresponding “DOUT” channel in the
grid area and enter the number.

8.23.3 Signal properties

8.23.3.1 Tree elements for DOUT signals

Changesanderrorsexcepted.

336

8.23 DOUT(DIGITALOUTPUTSIGNALS)

After having added the “DOUT” interface to your system it will appear as a tree element
wit the name “DOUT”.

8.23.3.2 Grid area for DOUT signals

In the “grid area” you will be presented with an overview of the DOUT channels which
have been added to your system so far. Each DOUT channel can only receive one signal
and therefore each DOUT channel is treated as a signal.
Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

8.23.3.3 Details area for DOUT signals

The Details area shows settings either for the selected tree element “DOUT” or the selected
In case the tree element is selected, the details area
“DOUT” channel in the grid area.
will only show the “General” tab. Please refer to (→4.2.2).

In case a “DOUT” channel
additional tabs which will be explained in the following.

is selected in the grid area, the details area will contain

Changesanderrorsexcepted.

337

8.23 DOUT(DIGITALOUTPUTSIGNALS)

General
Please refer to (→4.2.2).

Format
This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “1-Bit”) and allows you to apply
special tasks for this signal such as “GPS Longitude”, “GPS Latitude”, “UTC hour”,
“Audio mono” and more.

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a signal value is read as
invalid.

• Channel type

This field tells you whether you are dealing with a “Input” channel or “Output”
channel.

Scaling
The fields accessible directly through the tab allow for basic scaling operations to con-
vert analog measurement in engineering units. The “Scaling calculator” allows for more
refined scaling options with a large range of functions. For details on how to use the
“Scaling calculator” please refer to the IPEmotion Documentation - Section 3.4.5 “Chan-
nel configuration and scaling”.

• Sensor Mode

The sensor mode tells the type of signal. It can be of different types such as “Status”,
It cannot be changed and serves for IPEmotion
“Voltage”, “Frequenzy” or others.
to know what kind of signal it is dealing with.

Changesanderrorsexcepted.

338

8.23 DOUT(DIGITALOUTPUTSIGNALS)

• Sensor Range

Shows the raw value range of the signal.

• Physical Range

Allows you to set a range to which you would like to “scale” your signal and also
define the unit to use. For more refined scaling please use the “Scaling calculator”
and refer to the IPEmotion Documentation - Section 3.4.5 “Channel configuration
and scaling”.

Display
This tab allows you to define what information about the current signal will be shown on a
display if one is connected.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

• Name

Allows you to set a Name to be shown on a display.

Changesanderrorsexcepted.

339

8.23 DOUT(DIGITALOUTPUTSIGNALS)

Calculation
In this tab you set the formula to calculate the “DOUT” signal. This functionality has been
explained in depth in the “Formulas” section. Please refer to (→8.27.1.4).

Signal
This tab allows you to define signal settings.

• Signal number

Assign a number to the current signal. This way you will
signals in the grid according to their “Signal numbers”.

later be able to sort the

• Hold last value

Specify, for how long the last value of the signal will be hold.

• Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may here
select the dataset, to which this setting will refer.

• Timeout

Specify the timeout period for the current signal.
data for the specified time period, the value of the signal
Number)” and will be displayed as “–” in a display.

If the data source doesn’t send
is set to “NaN (Not a

• Hardware channel

Assign the corresponding digital hardware channel number from which you would
The hardware channel number can be found out via the
like to put out data.
logger’s webinterface.

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

Changesanderrorsexcepted.

340

8.24 ANALOGSIGNALS

8.24 Analog signals

Your logger is equipped with a number of analog input channels and the “Analog”
interface of the plugin allows for direct acquisition of analog signals coming in on these
channels. There are three types of analog signals that can be acquired via the “Analog”
interface:

• Voltage (→8.24.3.3) Allows you to directly import a raw voltage and, with the help of

the “Scaling calculator”, to transform it into a signal type of your desire.

• Counter/frequenzy (→8.24.3.4) Allows you to define a voltage-threshold for the in-

coming signal and thus transform the raw voltage into a counter or frequenzy.

• Duty cycle (→8.24.3.5) Allows you to acquire the hightime or the lowtime in percent

of a signal.

8.24.1 Storage method

In order to store incoming signals on an analog channel use one of the following signal
storage methods.

• ATFX (→ 15.7)

• MDF 4.0 (→ 15.8)

• MDF 4.1 (→ 15.9)

Changesanderrorsexcepted.

341

8.24 ANALOGSIGNALS

8.24.2 Adding the Analog Interface

In order to work with incoming analog signals, you will first need to add the “Analog”
interface to your system. To do so, select the system in the tree, click the “Components”
button in the Ribbon and then choose “Analog”.

Changesanderrorsexcepted.

342

8.24 ANALOGSIGNALS

Once the “Analog” interface has been added to your system, you can then add multiple
“Analog” channels of three different types (each type will acquire a differeent type of
signal).
To do so, select the “Analog” interface in the tree, click the “Components” button in the
Ribbon and then choose one of the three types “Voltage” (→8.24.3.3),
“Counter/frequenzy” (→8.24.3.4) or “Duty cycle” (→8.24.3.5).
For specifics on the configuration for each of these signal types please click on the
respective links in the preceding paragraph.

Changesanderrorsexcepted.

343

8.24 ANALOGSIGNALS

In order to acquire signals on analog channels, each analog channel
needs to be matched with the corresponding analog hardware chan-
nels of the logger. To find out the analog hardware channel numbers
please consult your loggers webinterface.
Once you know the hardware channel number, navigate to the “Sig-
nals” tab in “Details area” of the corresponding analog channel in the
grid area and enter the number.

Changesanderrorsexcepted.

344

8.24 ANALOGSIGNALS

8.24.3 Signal properties

8.24.3.1 Tree elements for Analog signals

After having added the “Analog” interface to your system it will appear as a tree element
wit the name “Analog”.

8.24.3.2 Grid area for Analog signals

In the “grid area” you will be presented with an overview of the Analog channels which
have been added to your system so far. Each Analog channel can only receive one signal
and therefore each Analog channel is treated as a signal.
Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

8.24.3.3 Details area for Analog signals (Voltage)

The Details area shows settings either for the selected tree element “Analog” or the
selected “Voltage” channel in the grid area.
In case the tree element is selected, the
details area will only show the “General” tab. Please refer to (→4.2.2).

In case a “Voltage” channel
additional tabs which will be explained in the following.

is selected in the grid area, the details area will contain

General
Please refer to (→4.2.2).

Changesanderrorsexcepted.

345

8.24 ANALOGSIGNALS

Format
This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “16-Bit integer signed”) and allows
you to apply special tasks for this signal such as “GPS Longitude”, “GPS Latitude”,
“UTC hour”, “Audio mono” and more.

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a signal value is read as
invalid.

• Channel type

This field tells you whether you are dealing with a “Input” channel or “Output”
channel.

Scaling
The fields accessible directly through the tab allow for basic scaling operations to con-
vert analog measurement in engineering units. The “Scaling calculator” allows for more
refined scaling options with a large range of functions. For details on how to use the
“Scaling calculator” please refer to the IPEmotion Documentation - Section 3.4.5 “Chan-
nel configuration and scaling”.

Changesanderrorsexcepted.

346

8.24 ANALOGSIGNALS

• Sensor Mode

The sensor mode tells the type of signal. It can be of different types such as “Status”,
“Voltage”, “Frequenzy” or others.
It cannot be changed and serves for IPEmotion
to know what kind of signal it is dealing with.

• Sensor Range

Shows the raw value range of the signal.

• Physical Range

Allows you to set a range to which you would like to “scale” your signal and also
define the unit to use. For more refined scaling please use the “Scaling calculator”
and refer to the IPEmotion Documentation - Section 3.4.5 “Channel configuration
and scaling”.

Display
This tab allows you to define what information about the current signal will be shown on a
display if one is connected.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

• Name

Allows you to set a Name to be shown on a display.

Changesanderrorsexcepted.

347

8.24 ANALOGSIGNALS

Excitation
This tab allows you to provide the analog sensor with excitation if necessary and also to
set the voltage of the excitation.

Signal
This tab allows you to define signal settings.

• Signal number

Assign a number to the current signal. This way you will
signals in the grid according to their “Signal numbers”.

later be able to sort the

• Hold last value

Specify, for how long the last value of the signal will be hold.

• Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may here
select the dataset, to which this setting will refer.

• Timeout

Specify the timeout period for the current signal.
data for the specified time period, the value of the signal
Number)” and will be displayed as “–” in a display.

If the data source doesn’t send
is set to “NaN (Not a

• Hardware channel

Assign the corresponding digital hardware channel number from which you would
The hardware channel number can be found out via the
like to put out data.

Changesanderrorsexcepted.

348

8.24 ANALOGSIGNALS

logger’s webinterface.

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

• Special task

The field “Special task” allows you to assign a user specific task to a signal, as long as
it has not been assigned to a logger default special task in the “Format” tab yet. If a
special task such as “GPS longitude/latitude/altitude in degrees”, “Vehicle identifi-
cation” or other has been assigned, in the “Format” tab, this field remains uneditable.

For further information regarding user specific special tasks and their properties
please refer to this part of the maual (→8.2.4.3).

8.24.3.4 Details area for Analog signals (Counter/frequenzy)

The Details area shows settings either for the selected tree element “Analog” or the
selected “Counter/frequenzy” channel
In case the tree element is
selected, the details area will only show the “General” tab. Please refer to (→4.2.2).

in the grid area.

In case a “Counter/frequenzy” channel is selected in the grid area, the details area will
contain additional tabs which will be explained in the following.

General
Please refer to (→4.2.2).

Format
This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “32-Bit integer unsigned”) and allows
you to apply special tasks for this signal such as “GPS Longitude”, “GPS Latitude”,
“UTC hour”, “Audio mono” and more.

Changesanderrorsexcepted.

349

8.24 ANALOGSIGNALS

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a signal value is read as
invalid.

• Channel type

This field tells you whether you are dealing with a “Input” channel or “Output”
channel.

Changesanderrorsexcepted.

350

8.24 ANALOGSIGNALS

Scaling
The fields accessible directly through the tab allow for basic scaling operations to con-
vert analog measurement in engineering units. The “Scaling calculator” allows for more
refined scaling options with a large range of functions. For details on how to use the
“Scaling calculator” please refer to the IPEmotion Documentation - Section 3.4.5 “Chan-
nel configuration and scaling”.

• Sensor Mode

The sensor mode lets you further specify, in which way the signal should be used.
There are three options:

Frequenzy Determines the frequency of an analog input.
Event counter Determines the occurrence of an event for an analog input.
Event counter with direction Determines the occurrence of an event for an analog
input, including a directional input to count either up or down. This mode requires
two analog channels, the prefix of the second channel determines the direction of
the event counter.

• Sensor Range

Shows the raw value range of the signal.

• Physical Range

Allows you to set a range to which you would like to “scale” your signal and also
define the unit to use. For more refined scaling please use the “Scaling calculator”
and refer to the IPEmotion Documentation - Section 3.4.5 “Channel configuration
and scaling”.

Changesanderrorsexcepted.

351

8.24 ANALOGSIGNALS

Display
This tab allows you to define what information about the current signal will be shown on a
display if one is connected.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

• Name

Allows you to set a Name to be shown on a display.

Input signal
This tab provides settings regarding the Input signal. These settings are crucial for a correct
functionality of the Counter/frequenzy mode.

• Signal number

Assign a number to the current signal. This way you will
signals in the grid according to their “Signal numbers”.

later be able to sort the

Changesanderrorsexcepted.

352

8.24 ANALOGSIGNALS

• Hold last value

Specify, for how long the last value of the signal will be hold.

• Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may here
select the dataset, to which this setting will refer.

• Timeout

Specify the timeout period for the current signal.
data for the specified time period, the value of the signal
Number)” and will be displayed as “–” in a display.

If the data source doesn’t send
is set to “NaN (Not a

• Hardware channel

Assign the corresponding digital hardware channel number from which you would
like to put out data.
The hardware channel number can be found out via the
logger’s webinterface.

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

Excitation
This tab allows you to provide the analog sensor with excitation if necessary and also to
set the voltage of the excitation.

Signal
This tab allows you to define signal settings.

• Signal number

Assign a number to the current signal. This way you will
signals in the grid according to their “Signal numbers”.

later be able to sort the

• Hold last value

Specify, for how long the last value of the signal will be hold.

Changesanderrorsexcepted.

353

8.24 ANALOGSIGNALS

• Timeout

Specify the timeout period for the current signal.
data for the specified time period, the value of the signal
Number)” and will be displayed as “–” in a display.

If the data source doesn’t send
is set to “NaN (Not a

• Hardware channel

Assign the corresponding digital hardware channel number from which you would
The hardware channel number can be found out via the
like to put out data.
logger’s webinterface.

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

• Special task

The field “Special task” allows you to assign a user specific task to a signal, as long as
it has not been assigned to a logger default special task in the “Format” tab yet. If a
special task such as “GPS longitude/latitude/altitude in degrees”, “Vehicle identifi-
cation” or other has been assigned, in the “Format” tab, this field remains uneditable.

For further information regarding user specific special tasks and their properties
please refer to this part of the maual (→8.2.4.3).

8.24.3.5 Details area for Analog signals (Duty cycle)

The Details area shows settings either for the selected tree element “Analog” or the
selected “Duty cycle” channel in the grid area. In case the tree element is selected, the
details area will only show the “General” tab. Please refer to (→4.2.2).

In case a “Duty cycle” channel is selected in the grid area, the details area will contain
additional tabs which will be explained in the following.

General
Please refer to (→4.2.2).

Format

Changesanderrorsexcepted.

354

8.24 ANALOGSIGNALS

This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “16-Bit integer unsigned”) and allows
you to apply special tasks for this signal such as “GPS Longitude”, “GPS Latitude”,
“UTC hour”, “Audio mono” and more.

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a signal value is read as
invalid.

• Channel type

This field tells you whether you are dealing with a “Input” channel or “Output”
channel.

Scaling
The fields accessible directly through the tab allow for basic scaling operations to con-
vert analog measurement in engineering units. The “Scaling calculator” allows for more
refined scaling options with a large range of functions. For details on how to use the
“Scaling calculator” please refer to the IPEmotion Documentation - Section 3.4.5 “Chan-
nel configuration and scaling”.

• Sensor Mode

The sensor mode tells the type of signal.
IPEmotion to know what kind of signal it is dealing with.

It cannot be changed and serves for

Changesanderrorsexcepted.

355

8.24 ANALOGSIGNALS

• Sensor Range

Shows the raw value range of the signal.

• Physical Range

Allows you to set a range to which you would like to “scale” your signal and also
define the unit to use. For more refined scaling please use the “Scaling calculator”
and refer to the IPEmotion Documentation - Section 3.4.5 “Channel configuration
and scaling”.

Display
This tab allows you to define what information about the current signal will be shown on a
display if one is connected.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

• Name

Allows you to set a Name to be shown on a display.

Extended
This tab provides extended settings regarding the duty cycle mode.

• Duty cycle mode

Define whether the high time or the low time will be put out in percent.

Changesanderrorsexcepted.

356

8.24 ANALOGSIGNALS

• Noise cancellation

Define the noise cancellation delay time.

Excitation
This tab allows you to provide the analog sensor with excitation if necessary and also to
set the voltage of the excitation.

Signal
This tab allows you to define signal settings.

• Signal number

Assign a number to the current signal. This way you will
signals in the grid according to their “Signal numbers”.

later be able to sort the

• Hold last value

Specify, for how long the last value of the signal will be hold.

Changesanderrorsexcepted.

357

8.24 ANALOGSIGNALS

• Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may here
select the dataset, to which this setting will refer.

• Timeout

Specify the timeout period for the current signal.
data for the specified time period, the value of the signal
Number)” and will be displayed as “–” in a display.

If the data source doesn’t send
is set to “NaN (Not a

• Hardware channel

Assign the corresponding digital hardware channel number from which you would
like to put out data.
The hardware channel number can be found out via the
logger’s webinterface.

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

• Special task

The field “Special task” allows you to assign a user specific task to a signal, as long as
it has not been assigned to a logger default special task in the “Format” tab yet. If a
special task such as “GPS longitude/latitude/altitude in degrees”, “Vehicle identifi-
cation” or other has been assigned, in the “Format” tab, this field remains uneditable.

For further information regarding user specific special tasks and their properties
please refer to this part of the maual (→8.2.4.3).

8.24.4 Analog signals on μCros SL

The logger-model μCros SL supports analog signals and by default the “Analog” interface
is activated and can be found in the measurement task tree. These analog signals for
μCros SL are of the type “Voltage” but they have some differences compared to regular
analog voltage-signals on other loggers.
This section of the manual will explain how they differ from regular analog voltage signals.

Overview of the differences compared to regular analog voltage-signals

• Analog signals on μCros SL are always available in the “Analog” interface and can-
not be deleted. They are by default incactive and need to be marked active in
order to be used.

Changesanderrorsexcepted.

358

8.24 ANALOGSIGNALS

• The sampling rate for analog signals on μCros SL cannot exceed a maximum of 200

Hz.

Changesanderrorsexcepted.

359

8.24 ANALOGSIGNALS

• The sensor rate of analog signals on μCros SL is set fixed from 0 to 40 V. It cannot be

changed.

• The resolution of the signal is 10 bit.

• The μCros SL is not able to put out voltage on the analog channel, therefore the tab

“Exitation” does not exist.

Apart from these differences the analog signals on μCros SL are identical to regular
analog voltage signals and can be treated in the same way.
For more information
regarding regular analog voltage signals please refer to (→8.24.3.3).

Changesanderrorsexcepted.

360

8.25 THERMO

8.25 Thermo

The “Thermo” module offers an analog channel, through which a “Thermo” signal can be
acquired.

8.25.1 Storage method

In order to store incoming signals on a Thermo channel use one of the following signal
storage methods.

• ATFX (→ 15.7)

• MDF 4.0 (→ 15.8)

• MDF 4.1 (→ 15.9)

8.25.2 Adding the Thermo-Interface

In order to work with “Thermo” signals, you will first need to add the “Thermo” interface to
your system. To do so, select the system in the tree, click the “Components” button in the
Ribbon and then choose “Thermo”.

Changesanderrorsexcepted.

361

8.25 THERMO

Once the “Thermo” interface has been added to your system, you can then add multiple
To do so, select the “Thermo”
“Thermo” channels, in order to acquire digital signals.
interface in the tree, click the “Components” button in the Ribbon and then choose
“Thermo”.

In order to acquire “Thermo” signals via “Thermo” channels, each
“Thermo” channel needs to be matched with the corresponding hard-
ware channels of the logger. To find out the hardware channel numbers
please consult your loggers webinterface.
Once you know the hardware channel number, navigate to the “Sig-
nals” tab in “Details area” of the corresponding “Thermo” channel
in
the grid area and enter the number.

Changesanderrorsexcepted.

362

8.25 THERMO

8.25.3 Signal properties

8.25.3.1 Tree elements for Thermo signals

After having added the “Thermo” interface to your system it will appear as a tree element
wit the name “Thermo”.

8.25.3.2 Grid area for Thermo signals

In the “grid area” you will be presented with an overview of the Thermo channels which
have been added to your system so far. Each Thermo channel can only receive one signal
and therefore each Thermo channel is treated as a signal.
Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

8.25.3.3 Details area for Thermo signals

The Details area shows settings either for the selected tree element “Thermo” or the
selected “Thermo” channel in the grid area.
In case the tree element is selected, the
details area will only show the “General” tab. Please refer to (→4.2.2).

In case a “Thermo” channel
additional tabs which will be explained in the following.

is selected in the grid area, the details area will contain

General
Please refer to (→4.2.2).

Changesanderrorsexcepted.

363

8.25 THERMO

Format
This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “16-Bit integer unsigned”) and allows
you to apply special tasks for this signal such as “GPS Longitude”, “GPS Latitude”,
“UTC hour”, “Audio mono” and more.

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a signal value is read as
invalid.

• Channel type

This field tells you whether you are dealing with a “Input” channel or “Output”
channel.

Scaling
The fields accessible directly through the tab allow for basic scaling operations to con-
vert analog measurement in engineering units. The “Scaling calculator” allows for more
refined scaling options with a large range of functions. For details on how to use the
“Scaling calculator” please refer to the IPEmotion Documentation - Section 3.4.5 “Chan-
nel configuration and scaling”.

Changesanderrorsexcepted.

364

8.25 THERMO

• Sensor Mode

The sensor mode tells the type of signal.It cannot be changed and serves for
IPEmotion to know what kind of signal it is dealing with.

• Sensor Range

Shows the raw value range of the signal.

• Physical Range

Allows you to set a range to which you would like to “scale” your signal and also
define the unit to use. For more refined scaling please use the “Scaling calculator”
and refer to the IPEmotion Documentation - Section 3.4.5 “Channel configuration
and scaling”.

Terminal
Additional information regarding the kind of thermoelement, that is being used.

Changesanderrorsexcepted.

365

8.25 THERMO

Display
This tab allows you to define what information about the current signal will be shown on a
display if one is connected.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

• Name

Allows you to set a Name to be shown on a display.

Signal
This tab allows you to define signal settings.

• Signal number

Assign a number to the current signal. This way you will
signals in the grid according to their “Signal numbers”.

later be able to sort the

• Hold last value

Specify, for how long the last value of the signal will be hold.

Changesanderrorsexcepted.

366

8.25 THERMO

• Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may here
select the dataset, to which this setting will refer.

• Timeout

Specify the timeout period for the current signal.
data for the specified time period, the value of the signal
Number)” and will be displayed as “–” in a display.

If the data source doesn’t send
is set to “NaN (Not a

• Hardware channel

Assign the corresponding digital hardware channel number from which you would
like to put out data.
The hardware channel number can be found out via the
logger’s webinterface.

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

Changesanderrorsexcepted.

367

8.26 INTERNALSIGNALS

8.26 Internal signals

Internal signals are values that are not fed into the logger from the outside (CAN, GPS…),
but are generated within the logger and provide information about internal system states.

Internal signals are largely treated in the same manner as a CAN signal. They can be
recorded over time, classed or processed; they can generate alarms or be displayed.
Only they can’t be directly stored in traces, since the values, with the exception of the
bus statistics, are not, as required, in the form of bus messages.

The internal signals are divided into three groups and the details on each group can be
found in the respective section:

• Run state (→8.26.4)

• System info (→8.26.5)

• Time (→8.26.6)

8.26.1 Storage method

In order to store internal signals use one of the following signal storage methods.

• ATFX (→ 15.7)

• MDF 4.0 (→ 15.8)

• MDF 4.1 (→ 15.9)

Changesanderrorsexcepted.

368

8.26 INTERNALSIGNALS

8.26.2 Accessing internal signals

“Internal signals” do not need to be imported, as they are continuosly produced by the
logger itself. They only need to be made accessible and can then be activated for to be
used liked regular signals in further processing, for example as triggers or in formulas.

To access “Internal signals” select the tree element “Internal signals”, click the “Compo-
nents” button in the Ribbon and then choose, which of the three categories of internal
signals you wish to access.

If you wish to acces two or all three categories, you can either access them one by one
or through the button “Multiple selection...”.

Changesanderrorsexcepted.

369

8.26 INTERNALSIGNALS

8.26.3 Internal signals properties

8.26.3.1 Tree elements for Internal signals

Each category of “Internal signals” that has been accessed, will appear in the tree as
In the
a child element to the tree element “Internal signals” with its respective name.
right part of the tree it will also show, how many signals have been activated for further
processing.

8.26.3.2 Grid area for Internal signals

In the “Grid area” you will be presented with an overview of the available “Internal sig-
nals”. Also you can find here two important functions, which are the “Column chooser”
(→4.2.5) and the “Filter editor” (→4.2.6).

8.26.3.3 Details area for Internal signals

The Details area shows settings either for the selected tree element (“Internal signals”,
“Run state”, “System info” or “Time”) or the selected signal in the grid area.
In case a
tree element is selected, the details area will only show the “General” tab. Please refer to
(→4.2.2).

In case a signal is selected in the grid area, the details area will contain additional tabs
which will be explained in the following.

Changesanderrorsexcepted.

370

8.26 INTERNALSIGNALS

General
This tab allows you to activate or deactivate the signal by ticking/unticking the checkbox
and thus to make it available for internal Recording and further use (e.g. triggers, formu-
las, display,...)
It also allows you to give a user specific name to your signal if wished and add an addi-
tional description. The Reference field serves as the tree element’s unique identifier inside
the measurement task tree. It cannot be changed. The “Sampling rate” allows you to set,
how frequently a signal should be requested.

Format
This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “64-Bit floating point”) and allows you
to apply special tasks for this signal such as “GPS Longitude”, “GPS Latitude”, “UTC
hour”, “Audio mono” and more.

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a signal value is read as
invalid.

• Channel type

This field tells you whether you are dealing with a “Input” channel or “Output”
channel.

Changesanderrorsexcepted.

371

8.26 INTERNALSIGNALS

Scaling
The fields accessible directly through the tab allow for basic scaling operations to con-
vert analog measurement in engineering units. The “Scaling calculator” allows for more
refined scaling options with a large range of functions. For details on how to use the
“Scaling calculator” please refer to the IPEmotion Documentation - Section 3.4.5 “Chan-
nel configuration and scaling”.

• Sensor Mode

The sensor mode tells the type of signal. It can be of different types such as “Status”,
“Voltage”, “Frequenzy” or others.
It cannot be changed and serves for IPEmotion
to know what kind of signal it is dealing with.

• Sensor Range

Shows the raw value range of the signal.

• Physical Range

Allows you to set a range to which you would like to “scale” your signal and also
define the unit to use. For more refined scaling please use the “Scaling calculator”
and refer to the IPEmotion Documentation - Section 3.4.5 “Channel configuration
and scaling”.

Display
This tab allows you to define what information about the current signal will be shown on a
display if one is connected.

Changesanderrorsexcepted.

372

8.26 INTERNALSIGNALS

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

• Name

Allows you to set a Name to be shown on a display.

Signal
This tab allows you to define signal settings.

• Signal number

Assign a number to the current signal. This way you will later be able to sort the signals
in the grid according to their “Signal numbers”.

• Hold last value

Specify, for how long the last value of the signal will be hold.

• Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may here
select the dataset, to which this setting will refer.

• Timeout

Specify the timeout period for the current signal. If the data source doesn’t send data
for the specified time period, the value of the signal is set to “NaN (Not a Number)”
and will be displayed as “–” in a display.

• Namespace

The “Namespace” serves as unique identifier for the signal inside the logger.

• Special task

The field “Special task” allows you to assign a user specific task to a signal, as long as
it has not been assigned to a logger default special task in the “Format” tab yet. If a

Changesanderrorsexcepted.

373

8.26 INTERNALSIGNALS

special task such as “GPS longitude/latitude/altitude in degrees”, “Vehicle identifi-
cation” or other has been assigned, in the “Format” tab, this field remains uneditable.

For further information regarding user specific special tasks and their properties
please refer to this part of the maual (→8.2.4.3).

• Round (Time status signals only)

Signals showing time in split units will be round to full units.

Signal check
This tab allows to apply the global signal check settings to this signal.
global signal check settings have to be defined, please refer to (→4.2.2).

In order to do so,

The parameters defined by the global signal check settings may be manually overriden
for each signal.

This setting does not apply to all internal signals. As of V15.14 it applies to
UPS Status signals and as of V17.10 it applies to PPP Status signals.

8.26.4 Run state

This group of internal signals provides information about the states of external signals and
switches, as well as about the wake conditions of the buses that started the logger.

These internal channels can be used as a supplement to the standard logger responses,
for example, to start or stop defined methods on signal states.
They can also set off
warning messages and alarms.

If a bus wake condition is defined, it is output even if this condition was not used to start
the current measurement. This makes it possible, during operation, to check when wake
conditions are met and trigger methods/messages/alarms.

Changesanderrorsexcepted.

374

8.26 INTERNALSIGNALS

The following table gives an overview and explanation of “Run state” signals.

Signal

Main runstate

Description

Main runstate

Active wake up condition

Type of wake condition that currently
started the logger

State system switch

State Clamp 15

State wake up condition

Measuring time delay

Measuring input delay

Delay between the current logger time
and the timestamp of the data being
processed.
Sends the measuring time delay caused
by waiting for input data.

Measuring input delay source Tells you the biggest input delay source.
Sends the measuring time delay caused
Measuring processing delay
by processing the data.

Error

Tells you whether an error has occurred
in your present configuration.

Error missing channel

Error initialized interface

Error missing interface

Error persistencefile

Dataset size xx

Measuring time delay

File I/O buffer time delay

Tells you the current size of the dataset;
this signal can be created multiple times
and gets an index on creation; this sig-
nal and the referenced dataset, as well
as the possible use of the dataset’s alias
for this signal can be configured in the
“Dataset” tab in the details area.
Tells you the current measurement de-
lay.
Tells you the current delay for writing
data from the buffer to disk.

Possible Values
0 = off
1 = on
1 = A-switch
2 = Cl. 15
3 = WoX
0 = off
1 = on
0 = off
1 = on
0 = not met
1 = met
Value in [ms]

Value in [ms]

String value
Value in [ms]

0 = no error
1 = error

0 = no error
1 = error
0 = no error
1 = error
0 = no error
1 = error
0 = no error
1 = error
Value in MB

Value in ms

Value in ms

Changesanderrorsexcepted.

375

8.26 INTERNALSIGNALS

8.26.5 System info

These signals provide information on CPU status and allocation of both working memory
(mem) and hard drive (disk). Sizes are specified in absolute numbers (in MB or in °C) or as
relative values (in %).
This category also contains the loggers frontnumber.

The following table gives an overview and explanation of “System info” signals.

Signal
Total memory
Free memory
Used memory
Total partition space

Free partition space

Used partition space

Total external disk space
Free external disk space
Used external disk space
CPU load
CPU temperature
Frontnumber

I/O load internal disk

I/O load external disk

CPU load of specific process

CPU load of specific thread

CPU load of thread with high-
est CPU load
Name of thread with highest
CPU load

Description
total working memory (RAM)
free working memory
used working memory
total partition space; this signal can be
created multiple times and gets an in-
dex on creation; partition type and cus-
tom label can be set in the “Partition”
tab in the details area.
free partition space; this signal can be
created multiple times and gets an in-
dex on creation; partition type and cus-
tom label can be set in the “Partition”
tab in the details area.
used partition space; this signal can be
created multiple times and gets an in-
dex on creation; partition type and cus-
tom label can be set in the “Partition”
tab in the details area.
total disk space
free disk space
used disk space
processor load
processor temperature
Tells you the loggers unique frontnum-
ber
Tells you the writing load to the internal
disk
Tells you the writing load to the external
disk
processor load of a specific process (to
be specified in the details area under
“Process”)
processor load of a specific thread (to
be specified in the details area under
“Thread”)
processor load of the thread with the
highest processor load
the name of the thread with the highest
processor load

Unit
[MByte]
[%]
[%]
[MByte]

[%]

[%]

[MByte]
[%]
[%]
[%]
[°C]
Value

[%]

[%]

[%]

[%]

[%]

Changesanderrorsexcepted.

376

8.26 INTERNALSIGNALS

8.26.5.1 System info specific settings

There are some System info signal which possess some specific settings, which will be
explained in the following.

I/O load specific partition
As it is possible to define multiple custom partitions, the “I/O load specific partition” can
also exist in multiple instances. To add a new instance of the signal select the “System
info” tree element, click the “Components” button in the Ribbon and choose “I/O load
specific partition”.

In order to then assign the correct partition to the signal, navigate to the “Partition” tab
in the signal’s details area and fill in the partition’s name under “Name”.

Changesanderrorsexcepted.

377

8.26 INTERNALSIGNALS

CPU load of specific process
There are two different processes which can be assigned to this signal, the “dataLog”
and the “Web interface” process, and thus it is also possible to add a second instance of
this signal, in order to show the CPU load for both the processes. In order to do so, select
the “System info” element in the measurement task tree, click on the “Components”
button in the Ribbon and then select “CPU load of specific process”.

In order to then assign the correct process to the signal, navigate to the “Process” tab
in the respective signal’s details area and choose the desired process in the dropdown
menu.

Changesanderrorsexcepted.

378

8.26 INTERNALSIGNALS

CPU load of specific thread
There are different threads which can be assigned to this signal, and thus it is also possible
to add multiple instances of this signal, in order to show the CPU load for all these threads.
In order to do so, select the “System info” element in the measurement task tree, click
on the “Components” button in the Ribbon and then select “CPU load of specific thread”.

Assign thread

In order to then assign the correct thread to the signal, navigate to the “Thread” tab in
the respective signal’s details area and choose the desired thread in the dropdown menu.

Reference

For some threads an additional thread reference may be specified, for example if the
thread “Video signal” is selected, a video signal may here be specified.

Use alias

The setting “Use alias” can only be activated when the “Headerengine” thread has been
selected. If it is activated, the alias of the specified reference will be used.

Changesanderrorsexcepted.

379

8.26 INTERNALSIGNALS

8.26.6 Time

These signals provide information on time and date. They allow you to record a timeline
in order to trace the occurrence of events in the logger.

The following table gives an overview and explanation of “Time” signals.

Subtype
Time since beginning of day
Time sincefirmware start

Time since START MEAS
Current date
Current year
Current month
Current day

Current time

Current hour
Current minute
Current second
Current microseconds

Description
Time since 00:00:00 h UTC
Time since the firmware was started (val-
ues <0 represent values during booting
phase)
Time since measurement has started
Current date in the format ddmmyy
Current year in the format yyyy
Current month in the format mm
Current day in the format dd
Current time in the format
hhmmss
Current hour in the format hh
Current minute in the format mm
Current second in the format ss
Current microseconds

Unit
[s]
[s]

[s]
Value
Value
Value
Value

Value

[h]
[min]
[s]
[μs]

Changesanderrorsexcepted.

380

8.27 FORMULAS

8.27 Formulas

8.27.1 Formulas (Calculated signals)

A formula is a calculated signal. Apart from the fact of being calculated it has largely the
same properties as physical signals and can be modified or used for further processing
in the same way.
It allows you, to combine already existing signals into a new signal.
Therefore the existence of physical signals is requirement in order for formulas to function
properly.

All the signals/quantities, that have been individually defined can be further processed
in formulas. This also applies to internal signals.

A formula is a one-line term made up of operators and functions that are applied to
numbers and signals, which will have a calculated signal as a result. Calculated signals
can in turn be used as normal signals in another formula. Not only numbers and signals
can serve as function arguments, but also the name of any already defined formula.

The operator priorities used by the formula interpreter are listed in the Table In addition,
the interpreter observes the “multiplication/division before addition/subtraction” rule.
When uncertain about priorities, you should use brackets.
Bear in mind that signal names and operators, in particular, are case-sensitive. Through-
out the signals, whether they be bus, internal or computed, no name may be used twice.
The functions can have multiple applications within a formula – with the exception of
integration (int_std), differential (DIFF) and moving average (MEAN). So each formula
may apply only once the function int_std, DIFF or MEAN.

Operator
(
)
+
-
*
/
MOD
ABS()
SIGN()
PREV()
=
AND
OR
XOR
<=
>=
<>
>
<
^
SHL

Meaning
Begin of bracket block
End of bracket block
Addition
Subtraction
Multiplication
Division
Modulo operator
Absolute value
Calculation of sign
Previous value
Equality
Logical and
Logical or
Logical, exclusive or
Less than or equal to
Greater than or equal to
Not equal to
Greater than
Less than
Exponentiation (2^3 =>“raise 2 to the power of 3”)
Shift left

Changesanderrorsexcepted.

381

8.27 FORMULAS

SHR
SIN()
COS()
TAN()
SINH()
COSINH()
TANH()
ASING()
ACOS()
ATAN()
EXP()
LOG()
LN()
SQRT()
IF(;;)
ANDB
ORB
XORB
NOTB()
TESTBIT(;)
TESTMASK()
TESTMASK(;)
TIMER(;)
MIN()
MAX()
MEAN()
MINOR(;)
MAJOR(;)
FLOOR()
CEIL()
ROUND()
INT()
INT_ADD()
INT_UP()
DIFF()
TIME()
LIN(;;;;)
EDGE_POS()
EDGE_NEG()
TFF()
DFF(;)
MF(;)
COUNT(;)
TIMEDIFF(;)
IS_NOVALUE()
asinh()
acosh()
atanh()

Shift right
Sine function
Cosine function
Tangent function
Hyperbolic sine function
Hyperbolic cosine function
Hyperbolic tangent function
Arcus sine function
Arcus cosine function
Arcus tangent function
Exponential function
Tenner logarithm
Logarithmus naturalis
Root function
Condition
Bitwise And operator
Bitwise OR operator
Bitwise Exclusive-OR operator
Bitwise NOT operator
Control if the given bit is set
Comparison with the test mask
Comparison with specified test mask
Time emitter
Minimum
Maximum
Average
Smaller one of both values
Greater one of both values
Rounding to next smaller integer
Rounding to next greater integer
Rounding to next integer
Integration
Integration
Upper integral
Differential
Time counter
Linearization
Detection to a positive edge
Detection to a negative edge
T-FlipFlop
D-FlipFlop
Monoflop
Counter
Time difference
NoValue check
Inverse hyperbolic sine function
Inverse hyperbolic cosine function
Inverse hyperbolic tangent function

Changesanderrorsexcepted.

382

8.27 FORMULAS

log2()
int_std()
truesample()
lin_tab
(;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;)
lin_ext
(;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;)
lin_int_ext
(;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;)

Binary logarithm
Integration
Truesamples
Conversion table without interpolation and extrapolation

Conversion table with extrapolation and without interpola-
tion
Linearization with interpolation and extrapolation

Special features of moving averages
Unlike the other formulas, the moving average (MEAN) uses not only the current value
but also a certain number of previous values. This number is defined by the parameter
“Delay depth (values)”. The number is theoretically unlimited, but in practice it is limited
by the working memory and processing speed.
Assuming the number is =100, then this computes the average over the last 100 samples.
At the next sampling instance, the oldest of the 100 values is dropped and the current
value is included. At start-up no samples are available for review, so the buffer is still
empty. The buffer is filled up with the first valid value and then moves through the sample
values.
In the event of a signal timeout (“Not a Number”, abbreviated NaN, or as a
value, also called NoValue), this review is interrupted. As long as the value of the signal is
NaN, the moving average is also equal to NoValue (processing a NoValue yields another
NoValue). Once the signal goes back to a valid value, the buffer – just like at the start
of measurement – is filled with the first valid value, thus resuming processing of a valid
average.
In a triggered timelog, the moving average is based on the continuous, untriggered
value stream. Once the start trigger is activated, the moving average buffer is filled,
according to the depth of averaging, with the values gathered prior to the trigger time.
This means the moving average at trigger time is computed from values obtained before
the start trigger.

Special features of “logical“ operators
Basic rules for applying the logical operators from are:

• Note upper/lower case: always lowercase logical operators

• Always bracket operands, if you use logical operators. Example: (’signal1’) or (’sig-

nal2’).

The results derived by an operator fundamentally depends on the type of data to which
it is applied.
The formula “(’signal1’) and (’signal2’)” applies the logical operator “and” to two chan-
nels with rational numbers. In this case, the integer parts of the respective channels are
linked bit-wise. So if:

Signal1= 6 (dec) or 110 (bin)
Signal2= 3 (dec) or 011 (bin)

Then “(’signal1’) and (’signal2’)“ yields the result:

Changesanderrorsexcepted.

383

6 and 3 = 2 (dec) or 110 and 011 = 10 (bin)

8.27 FORMULAS

The formula “(’signal1’>5) and (’signal2’>2)” applies the logical operator “and” to the
The intermediate
binary intermediate results of two channels with rational numbers.
results (signal1>5) and (signal2>2) yield binary “0” or “1”, depending on the value of the
channels. The link “and” merely links these values and can have only “0” or “1” as a
result.

8.27.1.1 Storage method In order to store calculated signals use one of the following
signal storage methods.

• ATFX (→ 15.7)

• MDF 4.0 (→ 15.8)

• MDF 4.1 (→ 15.9)

8.27.1.2 Adding a formula To add a new formula select the tree element “Formulas”,
click on the “Components” button in the Ribbon and then choose “Formula”

This will add a generic formula, which in the beginning will have the value “1”. Instructions
on how to work with that formula and modify it, will be explained in the section “Calcula-
tion” (→8.27.1.4).

8.27.1.3 Grid area for formulas All the formulas, that have been added to your system so
far, will be presented in an overview in the grid area. Also you can find here two important
functions, which are the “Column chooser” (→4.2.5) and the “Filter editor” (→4.2.6).

Changesanderrorsexcepted.

384

8.27 FORMULAS

8.27.1.4 Details area for formulas

The Details area shows settings either for the tree element “Formulas” or for a single
formula/signal which has been selected in the grid area.
In case a tree element is
selected, the details area will only show the “General” tab. Please refer to (→4.2.2).

In case a single formula/signal is selected in the grid area, the details area will contain
additional tabs which will be explained in the following.

General
This tab provides general settings for the selected formula/signal.

• Active

Allows you to activate or deactivate the selected formula/signal.

• Name

Give a user-defined Name to the selected formula/signal.

• Description

Give a user-defined description to the selected formula/signal.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Changesanderrorsexcepted.

385

8.27 FORMULAS

• Sampling rate

This field allows you to set the formula/signal’s processing rate.

The processing frequency can be
Formulas are executed in cycles.
defined for each formula. This rate can be set independently of the
recording rate. The computation process is applied to the values of the
input quantities actually registered at the time of the processing phase.
If the processing rate is higher than the signal rate of an input quantity,
then the last value of the variable is used again.
If the processing
rate is lower, then some of the values of the quantity are omitted. (An
analogous procedure applies when the recording rate is higher or lower
than the processing rate.)

Particularly with such channel processing as min, max, sum or avg,
periodic processing means that results are derived for the current
￿sampling instance￿ and not over the entire channel. If, for example, the
minimum over an entire channel
is required, the minimum/maximum
value recording must be used.

Processing a timeout value (￿Not a Number￿, NaN) also yields a NaN
value.

Format
This tab contains information and options regarding file format, tasks and Channel type.

• Data type

This field tells you the type of data (in this case “64-Bit floating point”) and allows
you to apply special tasks for this formula/signal such as “GPS Longitude”, “GPS
Latitude”, “UTC hour”, “Audio mono” and more.

• NoValue / DefaultValue

This field allows you to define the value that will be shown if a formula/signal value is
read as invalid.

Changesanderrorsexcepted.

386

8.27 FORMULAS

Scaling
The fields accessible directly through the tab allow for basic scaling operations to con-
vert analog measurement in engineering units. The “Scaling calculator” allows for more
refined scaling options with a large range of functions. For details on how to use the
“Scaling calculator” please refer to the IPEmotion Documentation - Section 3.4.5 “Chan-
nel configuration and scaling”.

• Sensor Mode

The sensor mode tells the type of formula/signal.
It can be of different types such
as “Status”, “Voltage”, “Frequenzy” or others. It cannot be changed and serves for
IPEmotion to know what kind of formula/signal it is dealing with.

• Sensor Range

Shows the raw value range of the formula/signal.

• Physical Range

Allows you to set a range to which you would like to “scale” your formula/signal
and also define the unit to use. For more refined scaling please use the “Scaling
calculator” and refer to the IPEmotion Documentation - Section 3.4.5 “Channel
configuration and scaling”.

Changesanderrorsexcepted.

387

8.27 FORMULAS

Display
This tab allows you to define what information about the current formula/signal will be
shown on a display if one is connected.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

• Name

Allows you to set a Name to be shown on a display.

Calculation
This tab provides the main functionality for working with formulas. Here you can define the
functions and operators of your formula and what numbers and/or signals they should be
applied to.
The operator priorities used by the formula interpreter are listed in the Formula operator
table here (→8.27.1). In addition, the interpreter observes the “multiplication/division be-
fore addition/subtraction” rule. When uncertain about priorities, you should use brackets.
Bear in mind that signal names and operators, in particular, are case-sensitive. Through-
out the signals, whether they be bus, internal or computed, no name may be used twice.
The functions can have multiple applications within a formula – with the exception of in-
tegration (int_std), differential (DIFF) and moving average (MEAN). So each formula may
apply only once the function int_std, DIFF or MEAN.

• Formula

This field allows you to manually enter a formula.

• Formula editor

Changesanderrorsexcepted.

388

8.27 FORMULAS

Although there is the possibility to manually define formulas, most of the time it will
be more convenient to define formulas using the “Formula editor”.

The “Formula editor” provides an overview of your current formula (the upper table),
as well as the possible “Operands” (left table) and “Operators” (right table) and a
short description for each item in the lower table.

You can add items to your formula either by doubleclicking on them or per drag
and drop.
If you wish to delete an item from the formula, you can simply mark it with the mouse
and than delete it.
If you are uncertain about the operator priorities please refer to the table of formula
operators here (→8.27.1).
When confirming a formula that has been defined in the “Formula editor” by clicking
OK, the editor will automatically validate the formula’s correctness. If the formula is
not correct, that will result in an error message.

Changesanderrorsexcepted.

389

8.27 FORMULAS

• Value persistence

Defines the persistence of the signal, so that the value of the signal is sustained even
beyond logger restart.

• Dataset

If the setting “Value persistence” has been set to “Until end of dataset”, you may
here select the dataset, to which this setting will refer.

• Moving average buffer size

Defines buffer size of the MEAN() filter.

• Delay buffer size

Defines the size of the delay() buffer.

Changesanderrorsexcepted.

390

8.27 FORMULAS

Signal
This tab allows you to define formula/signal settings.

• Signal number

Assign a number to the current formula/signal. This way you will later be able to sort
the formulas/signals in the grid according to their “Signal numbers”.

• Namespace

The “Namespace” serves as unique identifier for the formula/signal inside the logger.

• Special task

The field “Special task” allows you to assign a user specific task to a signal, as long as
it has not been assigned to a logger default special task in the “Format” tab yet. If a
special task such as “GPS longitude/latitude/altitude in degrees”, “Vehicle identifi-
cation” or other has been assigned, in the “Format” tab, this field remains uneditable.

For further information regarding user specific special tasks and their properties
please refer to this part of the maual (→8.2.4.3).

Changesanderrorsexcepted.

391

8.27 FORMULAS

8.27.2 Script expressions

As of V17.10.00 the PlugIn supports, additional to regular formulas, also Script expressions
as formulas. Script expressions mainly function in the same way as regular formulas,
meaning they result in a calculated signal that can than be used like any other signal.
For further details on settings for formulas please refer to (→8.27.1).

The main difference is the editor, that is used to compose the Script expression, which
has a wider range of operators. An overview of the available operators for the “Script
expression” editor can be found here (→8.27.2.2) in this section.

8.27.2.1 Adding a Script expression

To add a “Script expression”, select the “Formulas” interface in the tree, click on the
“Components” button in the Ribbon and then select “Script expression”.

Changesanderrorsexcepted.

392

8.27 FORMULAS

8.27.2.2 Script expression editor

The “Script expression editor” allows you to compose dynamic messages using operands
and operators. As operands all signals, triggers and methods will be available.
The available operators are listed in the tables below with a short description.

Signaloperators

Operator
SYSTEM_TIME()
SYSTEM_TIME_FORMATTED()
MEAS_TIME()

MEAS_TIME_FORMATTED()
TO_CHAR(255)
TO_CHAR( SIGNAL_VALUE(”signal”) )
TO_CHAR( ( 3 - SIGNAL_VALUE(”signal”)
) * 5 )
TO_HEX( 0 )
TO_HEX( SIGNAL_VALUE(”signal”) )
TO_HEX_FULL( 255 )
TO_HEX_FULL( 255; 5 )
TO_HEX_FULL(
SIGNAL_VALUE(”signal2”) )
TO_ASCII( 5; 10 )
TO_ASCII( 5; 10; 3 )
TO_INTEGER( ”asdf” )
TO_INTEGER(
TEM_TIME_FORMATTED() )

SIGNAL_RAW(”signal”);

SYS-

Characteristics
Current time in microseconds as integer
”%Y-%m-%d %H:%M:%S”
Current time (minus Measdelay) in microseconds
as integer
”%Y-%m-%d %H:%M:%S”
Number to ASCII character

Hex value as string (e.g. 0x0a)

Hex value as string (e.g. a)

Decimal value as string

ASCII value of the string as integer

Changesanderrorsexcepted.

393

8.27 FORMULAS

Operator
COUNT_DATASETS_CLOSED()

SIGNAL_VALUE(”signal”);

CHECK_BUS( 10; ”CAN 01” )
CHECK_BUS(
”LIN 05” )
CHECK_BUS( ( EXP( 13 ) / 4 ); ”ETH 02” )
IS_VALID_SIGNAL( ”name” )
IS_VALID_SIGNAL( ”name” + 13 )
IS_VALID_METHOD( ”name” )

IS_VALID_DATAFILE( ”name” )

COS(255)
COS( SIGNAL_VALUE(”signal”) )
COS( ( 7 + COUNT_DATASETS_CLOSED()
) * 12 )
SIN(1)
TAN(0)
ACOS(255)
ASIN(0)
ATAN(1)
COSH(2)
SINH(3)
TANH(4)
EXP(5)
LOG(6)
LN(7)
POW(8;9)
SQRT(10)
CEIL(11.1234)
FLOOR(12.9876)
LN(7)
ABS(-13)
CRC8_SUM( 1; 2 )
CRC8_SUM( 1; 2; 3; 4; 5; 6; 7; 8 )
CRC8_SUM( 1; 2; 3; ... 255 )

Characteristics
Number of closed datasets, that have not been
transferred yet
True when bus has no timeout

Reports “True” when the string is a valid signal
name
Reports “True” when the string is a valid method
name
Reports “True” when the string is a valid datafile
name

Second operand is exponent

Calculation of the CRC8 sum

Changesanderrorsexcepted.

394

8.27 FORMULAS

Operator
FRONTNUMBER()
DATASET_ID_GLOBAL( ”name” )
DATASET_ID_LOCAL( ”name” )
SPECIAL_VIN()
SPECIAL_ODO()

Characteristics
e.g. specialtagvalue(“fn”)

The following tags are supported:

• $(fn)/$(sn): The logger’s frontnumber

• $(vin): Value of the signal with special role

“vin” (special=vin)

• $(odo): Value of the signal with special
role “odo” (special=odo, supported from
2016.06)

The following tags are supported from V 2017.10
inside of a dataset and refert to the respective
dataset:

• $(datasetglobalid): global index (unique for

all datasets

• $(datasetlocalid):

local

index (unique for

datasets within the same namespace)

SIGNAL_VALUE(“signal”)
SIGNAL_VALUE_STRING(“signal”)
SIGNAL_UNIT(“signal”)
SIGNAL_RAW(“signal”)
SIGNAL_NAME(“signal”)
SIGNAL_DESCRIPTION(“signal”)
SIGNAL_SCALE(“signal”)
SIGNAL_OFFSET(“signal”)
STATION_CONNECTED( ”station” )
STATION_VERSIONCHECK_RESULT( ”sta-
tion” )
STATION_VERSIONCHECK_VERSION(
”station” )
DAQ_CONFIGURED( ”station”; ”daqlist”
)
DAQ_STARTED( ”station”; ”daqlist” )

PARTITION_TOTAL( ”internal” )
PARTITION_TOTAL(
bel” )
PARTITION_USED_MB( ”partition” )

”customStorageLa-

PARTITION_USED_PERCENT( ”partition” )

TRIGGER_STATE()

as of V17.10.00

as of V17.10.00
as of V17.10.00

as of V17.10.00

the specified DAQ list has to belong to the speci-
fied station
the specified DAQ list has to belong to the speci-
fied station
in MB
as of V17.10.00

in MB
as of V17.10.00
in percent
as of V17.10.00
Reports the state of the trigger

Changesanderrorsexcepted.

395

8.27 FORMULAS

Operator
TRIGGER_LEVEL()
TRIGGER_PRETIME()
TRIGGER_POSTTIME()
TRIGGER_COUNT()
METHOD_STATE()
METHOD_PRETIME()
METHOD_POSTTIME()
METHOD_DATAFILES()
METHOD_DATASIZE()
METHOD_SNAPSHOTS()
METHOD_SNAPSHOTFILES()
METHOD_SNAPSHOTSIZE()
DATASET_SIZE( ”dataset” )
TEXT( ”hello world!” )
SIGNAL_VALUE( ”signal” ) == 5
( 1 + 2 ) == ( 3 - 4 )
1 <> 0
1 > 0
1 < 0
1 >= 0
1 <= 0
1 AND 0
1 OR 0
1 XOR 0
1 ORB 0
1 XORB 0
1 ANDB 0
NOTB( 1 )
NOTB( SIGNAL_VALUE( ”signal” ) )
1 + 0
1 - 0
1 * 0
1 / 0
1 MOD 0
PARAMETER_VALUE()
ON EVENT <event name> SYSTEM
(USBPLUGGED) <Statement>
ON EVENT <event name> SYSTEM
(USBUNPLUGGED) <Statement>

Characteristics
Index of the active trigger level
Pre-trigger time
Post-trigger time
Trigger event counter
Reports the state of the method
Pre-trigger time
Post-trigger time
Number fo files in the current dataset
Size of the current file in bytes
Number of markers
Number of marked files
Total size of marked files

equal

not equal
greater
less than
not less than
equal or less than
AND
OR
XOR
Bitwise-OR
Bitwise-XOR
Bitwise-AND
Bitwise-NOT

Plus
Minus
Times
Divide
Modulo
Fill in any project parameter value

Changesanderrorsexcepted.

396

8.28 SYNCHRONIZINGSIGNALS

8.28 Synchronizing signals

This option allows you to synchronize the signals of a already imported description file
with a newer or older version of the same description file.

To do so, select the CAN channel or description file you wish to synchronize in the
measurement task tree, click “Import” in the ribbon and then choose “Synchronize”.

In the resulting window you will be shown which is the file preivously used under “Previous
file” and you will be able to choose a new file with which you would like to synchronize.
To do so, click in the field for the new file and then click the button with the three dots as
shown in the following figure.

In the resulting window you will be able to choose the file with which you would like to
synchronize and confirm by clicking “Open”.

Changesanderrorsexcepted.

397

8.28 SYNCHRONIZINGSIGNALS

Before you complete the synchronization process, you may adjust two settings on how to
handle differences between the two description files.

• Show differences

If marked active and there are differences between the current configuration and
the new description file, a dialog with all these differences will be displayed before
the synchronization is be performed. Properties, that cannot be edited, will not be
taken into account in this comparison.

• Missing signal handling

This dropdown menu allows you to specify how signals, that are no longer available
in the new description file, should be handled.

To complete the synchronization process click “OK”.

Changesanderrorsexcepted.

398

8.29 TRANSFERRINGMEASUREMENTTASKSTOTHELOGGER

8.29 Transferring measurement tasks to the logger

9 Alias signal group

The function “Alias signal group is available for the following Tree elements:

• CAN/CAN FD

• Virtual CAN

• LIN

• FlexRay

• Front (Ethernet)

• ETH xx (Ethernet)

The function “Alias signal group” allows you to create groups, to which you can add ex-
isting signals as aliases. The signals in the “Alias signal group” are read only and get their
properties from the original signal, with some exceptions:

• Active Activate/Deactivate this signal alias for export

• Name You may set a user specific name for the signal alias

• Description You may set a user specific description for the signal alias

• Name (Display) In the “Display” tab you may set a user specific display name for the

signal alias

At export each activated signal alias will be exported with the original signal’s settings
but with the user specific name and description.

It is possible to create multiple aliases for the same signal.

It is not possible to create signal aliases for audio signals.

Changesanderrorsexcepted.

399

9.1 CREATINGANALIASSIGNALGROUP

9.1 Creating an Alias signal group

The “Alias signal group” has to belong to the same channel as the signals, that you would
like to include in it. In order to create an “Alias signal group” select the desired CAN/CAN
FD channel, click the “Components” button in the Ribbon and select “Alias signal group”.

Changesanderrorsexcepted.

400

9.2 GRIDAREAFORANALIASSIGNALGROUP

If your CAN/CAN FD channel already contains signals, you will now be presented with
a selection window, that allows you to select all the signals, for which you would like to
create an alias. If your channel does not contain any signals yet, import signals. Now that
your channel contains signals, select the previously created “Alias signal group” in the
measurement task tree, click the “Components” button in the Ribbon and choose “Alias
signal.

You will now be presented with the previously mentioned selection window. Select all the
signals, for which you wish to create an alias and confirm with ”OK“.

9.2 Grid area for an Alias signal group

In the “grid area” you will be presented with an overview of all the signal aliases in the
group. Also you can find here two important functions, which are the “Column chooser”
(→4.2.5) and the “Filter editor” (→4.2.6).

Changesanderrorsexcepted.

401

9.3 DETAILSAREAFORSIGNALALIASES

9.3 Details area for signal aliases

The details area for signal aliases does not contain settings that allow to modify the signal
itself, as any signal alias receives these settings directly from its source signal. However,
there are two functional tabs for signal aliases, the “General” tab and the “Source” tab.

General
In this tab you may specify a name and description for the signal alias.

Source
This tab contains the source information of the signal alias. So even if you change the
name of the alias, you can here still find out the source signal and namespace.

Changesanderrorsexcepted.

402

10 TRIGGERS

10 Triggers

Triggers define a certain event or condition in a way, that they can trigger an action. They
possess two distinguishing features compared to formulas:

• They are not a signal but a trigger event

• A trigger always has to be a truth condition and therefore can only have two possible

values: true or false

Other than that, they are similar to formulas and can mainly be treated in the same way:

A trigger allows you, to combine already existing signals.
physical signals is requirement in order for triggers to function properly.
A trigger is a one-line term made up of operators and operands that are applied to
numbers and signals, which will have a calculated condition (trigger event) as a result.
All the signals/quantities, that have been individually defined can be further processed
as operands in a trigger’s formula. This also applies to internal signals.
An existing trigger event can again be used as operand in a different trigger’s formula.

Therefore the existence of

The triggers are divided into four groups and the details on each group can be found in
the respective section:

• Standard Triggers (→10.5)

• Level Triggers (→10.6)

• Cyclic Triggers (→10.7)

• Trigger groups (→10.8)

Changesanderrorsexcepted.

403

10.1 ADDINGATRIGGER

10.1 Adding a trigger

To add a new trigger select the desired type of trigger in the tree, click on the “Compo-
nents” button in the Ribbon and then again choose the desired type of trigger.

This will add a generic trigger condition, which in the beginning will have the value “1”.
Technically this trigger condition works the same way as a formula and instructions on how
to modify it will be explained in the section “Calculation” (→8.27.1.4).

Changesanderrorsexcepted.

404

10.2 TREEELEMENTSFORTRIGGERS

10.2 Tree elements for triggers

By default the “Measurement task tree” will contain all four categories of triggers.

Each trigger that you add to your system will be shown and accessible in the measurement
task tree in its respective trigger category.

Changesanderrorsexcepted.

405

10.3 GRIDAREAFORTRIGGERS

10.3 Grid area for Triggers

The grid area for each Trigger category will present you with an overview of the triggers
that have been added to your system so far.

Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

Changesanderrorsexcepted.

406

10.4 DETAILSAREAFORTRIGGERS

10.4 Details area for Triggers

The Details area shows settings either for a selected tree element. In case the “Triggers”
element or one of the four categories (“Standard Trigger”, “Level Triggers”, “Cyclic
Triggers” or “Trigger groups”) is selected, the details area will only show the “General”
tab. Please refer to (→4.2.2).

Settings
In case a single trigger is selected in the tree or the grid area, the details area will
additionally contain the “Settings” tab.

This tab provides the main functionality for working with Triggers. Here you can define the
functions and operators for the formula of your trigger and what numbers and/or signals
they should be applied to, as well as cycling rates, levels and groups.

As this tab is different for each trigger category, it will be explained in the respective section
for each trigger category:

• Standard Triggers (→10.5)

• Level Triggers (→10.6)

• Cyclic Triggers (→10.7)

• Trigger groups (→10.8)

Changesanderrorsexcepted.

407

10.5 STANDARDTRIGGERS

10.5 Standard Triggers

For standard triggers, only an activation condition is specified. If the condition is met, the
trigger is set; once it is no longer met, the trigger is reset. This makes the standard trigger a
simple and quick way to define a trigger. In the following will be explained how work with
“Standard Triggers”.

• Trigger mode

This field allows you to manually enter a formula for your trigger condition.

• Formula editor

Although there is the possibility to manually define formulas, most of the time it will
be more convenient to define formulas using the “Formula editor”. To do so, please
refer to the section “Formula editor” (→8.27.1.4).

• Continuity

Define the required minimum duration of trigger condition being met.

• Hold last value

Specify, for how long the last value of the signal will be hold.

• Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may here
select the dataset, to which this setting will refer.

• max activations

Specify a maximum number of trigger activations. Once this number has been
reached, the trigger will not be activated even if the trigger condition is met.

• Logfile

If set, a message will be written into the logfile at trigger occurrence.

Changesanderrorsexcepted.

408

10.5 STANDARDTRIGGERS

• Trigger groups

This setting allows you to see how many trigger groups this trigger has been assigned
to. The “Assign” button opens a selection dialog which lets you change the trigger
group assignment of the trigger.

Changesanderrorsexcepted.

409

10.6 LEVELTRIGGERS

10.6 Level Triggers

A “Level Trigger” is an event with multiple levels of conditions, which have to be set
consecutively, in a specified order. As trigger condition for one level, you can either
define a single condition, which if met activates the level, and once it is no longer met,
resets the trigger. Or else two conditions are defined, one to activate the level (set
condition) and one to reset the trigger (reset condition). The program always checks the
reset condition of the current level and the set condition of the next level, and reacts
accordingly.
The trigger is set once the highest defined level is reached, and remains set until the reset
condition of this level is met.
In the following will be explained how to work with “Level Triggers”.

Settings
If a “Level trigger” is selected in the tree or the grid are, the settings tab allows for settings
regarding the general behaviour of a level trigger.

• Hold last value

Specify, for how long the last value of the signal will be hold.

• Dataset

If the setting “Hold last value” has been set to “Until end of dataset”, you may here
select the dataset, to which this setting will refer.

• Timeout

Timeout [in ms], after which the trigger is reset, even if neither the highest level is
reached nor another reset condition is met.

• Continuity

Minimum duration of the trigger condition [in ms] before the trigger is activated.

• Maximum trigger count

Maximum number of activations for this trigger (0 = unlimited)

Changesanderrorsexcepted.

410

10.6 LEVELTRIGGERS

• Logfile message

If activated, an information on this trigger event will be written to the logfile.

• Trigger groups

This setting allows you to see how many trigger groups this trigger has been assigned
to. The “Assign” button opens a selection dialog which lets you change the trigger
group assignment of the trigger.

Changesanderrorsexcepted.

411

10.6 LEVELTRIGGERS

Adding trigger levels
Working with a “Level trigger”, allows you to add additional trigger levels, for which you
can later define trigger conditions and settings. To add a trigger level, select the desired
“Level trigger” in the tree, click the “Components” button of the Ribbon and choose
“Level”.

Changesanderrorsexcepted.

412

10.6 LEVELTRIGGERS

An overview of all Levels of a “Level trigger” will be presented in the grid area of the
respective “Level trigger”.

Level xx
The settings for each separate level of a “Level trigger”can be accessed by selecting the
desired Level in the grid area and then navigating to the “Settings” tab in the details area.

• Priority

The priority defines in which order the single levels of a “Level trigger” have to be met.
A “Level trigger” will always ascend in priority starting from “Priority 1” to “Priority 2”
and so on until the final defined priority is met or a reset condition is met.

• Mode

Define the Mode of this trigger level.

◦ “Inactive” means, this trigger level is deactivated.
◦ “Reset is inverted set” meanst, this trigger level is activated and will be reset, as

soon as the defined set condition is no longer met.

◦ “Set- and Reset-condition” means that you can define a set condition as well,

as a reset condition.

• Set condition

Formula for the condition to activate this level.
The result of the formula must always be 0 (not met) or 1(met), apart from that
creating a formula is described in section (→8.27).

Changesanderrorsexcepted.

413

10.7 CYCLICTRIGGERS

• Reset condition

Formula for the condition to reset the trigger from this level. Once the reset condition
is met, the entire trigger is reset and must therefore run through all levels again.
If
reset term =1 is set for the highest level, the trigger is immediately reset, i.e. only a
If no resetterm is specified, the end of the set
single trigger impulse is generated.
condition is automatically used as the reset condition. This can be prevented by
setting =0.
The result of the formula must always be 0 (not met) or 1(met), apart from that
creating a formula is described in section (→8.27).

• Timeout

Define a level timeout after which the trigger is reset, regardless of whether the reset
condition has been mat or the highest level has been reached.

10.7 Cyclic Triggers

A “Cyclic Trigger” is an event, that is not defined by a formula.
Its only condition is the
cycle time to which it is set. According to this time, the trigger will be set periodically. In
the following will be explained how to work with “Level Triggers”.

Settings
If a “Cyclic trigger” is selected in the tree or the grid are, the settings tab allows for settings
regarding the general behaviour of a cyclic trigger.

• Cycle time

Define the cycle time according to which the trigger will fire.

• Trigger groups

This setting allows you to see how many trigger groups this trigger has been assigned
to. The “Assign” button opens a selection dialog which lets you change the trigger
group assignment of the trigger.

Changesanderrorsexcepted.

414

10.7 CYCLICTRIGGERS

Changesanderrorsexcepted.

415

10.8 TRIGGERGROUPS

10.8 Trigger groups

“Trigger groups” allow you to combine two or more existing triggers and thus create a
new trigger condition. Source trigger signals can be combined via “disjunction (or)” or
“conjunction (and)”.

Creating a trigger group
In order to create a new “Trigger group” select the “Trigger groups” element in the
measurement task tree, click the “Components” button in the Ribbon and then choose
“Trigger group”.

It is also possible to create trigger groups from within a script. For instruc-
tions on scripts please refer to the according section of this manual (→11)
or for more detailed information refer to the Script documentation.

Changesanderrorsexcepted.

416

10.8 TRIGGERGROUPS

Selecting Triggers
In order for a “Trigger group” to function you will need to select at least two existing
triggers to be part of the “Trigger group”. To do so, select the “Trigger group” you wish to
work with in the measurement task tree.
This will present you with an overview of all available triggers in the details area. Set active
the tickbox “Assign to group” for each trigger, that you wish to assign to the group.

Settings
en The “Settings” tab in the details area of your “Trigger group” allows you to set the
operation mode of the group and whether a logfile should be created.

• Operation Mode

Allows you to set the operation mode of the “Trigger group”. You may choose
between “AND” or “OR”.

• Logfile message

If activated, an information on this trigger event will be written to the logfile.

Changesanderrorsexcepted.

417

11 SCRIPTS

11 Scripts

Defining methods for your configuration from within a script is no longer
supported, unless your logger is running in “Compatibility mode” for old
configurations.

It is therefore still possible to define methods from within a script but at
Check/Export this will cause a warning saying the method defined by
the script is no longer supported.

The “Scripts” interface allows you to write customized scripts for a configuration or to
import existing scripts in the format “DataLog script” (*.dls).

For detailed instruction on codewriting for scripts please refer to the
CAETEC script manual.

11.1 Adding the Scripts-Interface

In order to work with scripts, you will first need to add the “Scripts” interface to your system.
To do so, select the system in the tree, click the “Components” button in the Ribbon and
then choose “Scripts”.

Changesanderrorsexcepted.

418

11.2 ADDINGASCRIPT

11.2 Adding a script

Once the “Scripts” interface has been added to your system, you can then add one or
multiple scripts. To do so, select the “Scripts” interface in the tree, click the “Components”
button in the Ribbon and then choose “Script”.

11.3 Importing a script

It is also possible to import previously written scripts of the format “DataLog script file
(*.dls)”. To do so, select the “Scripts” interface in the tree, click the “Import” button in the
Ribbon and then choose “DataLog script”.

The following window lets you choose the desired script file and import it by clicking
“open”.

Changesanderrorsexcepted.

419

11.4 TREEELEMENTSFORSCRIPTS

11.4 Tree elements for Scripts

After having added the “Scripts” interface to your system it will appear as a tree element
wit the name “Scripts”.

Once a script has been created or imported, it will apper as a child element to the
“Scripts” interface with two child elements of its own.
The two child elements labeled “Triggers” and “Signals” are non-interactive elements.
Their purpose is to show, how many triggers or signals have been defined by the script.

Changesanderrorsexcepted.

420

11.5 GRIDAREAFORSCRIPTS(COMPOSINGASCRIPT)

11.5 Grid area for Scripts (Composing a script)

The grid area for a script is where the actual composing of the script (writing the code)
happens. The grid area provides an editor for writing the code or composing it out of
prefabricated block of code, and also for checking for syntax errors of the code.
The functions of the editor will be explained in the following.

For detailed instructions on codewriting in scripts please refer to the CAETEC script
manual. This can be found in the Script editor toolbar next to the syntax check.

The functions of the editor, which can all be found in the toolbar at the top of the editor
window, are divided in three groups:

• Edit script code (→11.5.0.1)

• Prefabricated code blocks (→11.5.0.2)

• Syntax check (→11.5.0.3)

If either the “Triggers”, “Signals” or “Methods” element has been se-
lected in the tree, the grid area will provide you with extra fucntionalities.
These will be explained in the sections “Triggers in Scripts” (→11.5.1), “Sig-
nals in Scripts” (→11.5.2) and “Methods in Scripts” (→11.5.3) of this chap-
ter.

Changesanderrorsexcepted.

421

11.5 GRIDAREAFORSCRIPTS(COMPOSINGASCRIPT)

11.5.0.1 Edit script code

Here you can find the functions “Find & Replace” and “Comment”.

Find & Replace
The “Find & Replace” function allows you to search your code or a selection of it for
characters/words. It also allows you to directly replace the search result.

Comment
The “Comment” function allows you to comment or uncomment an entire line or a
selection. A line/selection, that is commented, is not part of the code.

Changesanderrorsexcepted.

422

11.5 GRIDAREAFORSCRIPTS(COMPOSINGASCRIPT)

11.5.0.2 Prefabricated code blocks

In the middle part of the editor’s toolbar you will find a number of dropdown menus that
offer prefabricated blocks of code. This allows you to completely compose your script of
these blocks instead of writing it manually.

Any code block that is selected in one of these menus will be added to the script at the
cursor’s current postition. For example choosing “Event->Timeout->Timeout: Bus type”,
like seen below

will insert the following line of code in the script.

If entering code manually, the editor offers an autocompletion of words.
However, this only completes words, but does not check whether the
result is an errorfree syntax.

Changesanderrorsexcepted.

423

11.5 GRIDAREAFORSCRIPTS(COMPOSINGASCRIPT)

11.5.0.3 Syntax check

The “Syntax check” function will check whether the syntax of the code is correct. The
result of the syntax check will be presented in a pop-up window.
As you can see in the picture below, this pop-up window also offers a line jump feature.
That means, if you click on an error in the pop-up window, the editor will automatically
jump to the corresponding line and highlight it, so it is easier to correct any errors.

11.5.0.4 Undo in scripts / Redo in scripts

The IPEmotion “Undo” button (Ctrl. + Z) and “Redo” button (Ctrl. + Y) do not work to
undo or redo actions or parts of scriptcode in the script editor.

In order to undo/redo an action or a part of scriptcode in the script editor, right click in
the script editor and choose “Undo” or “Redo” from the resulting context menu.

Changesanderrorsexcepted.

424

11.5 GRIDAREAFORSCRIPTS(COMPOSINGASCRIPT)

11.5.1 Triggers in Scripts

When the “Triggers” treeelement of a script is selected, the grid area will present you with
an overview of all the triggers, that have been defined by the script. You can also see,
whether a trigger is active or not, the description and type of the trigger.

11.5.2 Signals in Scripts

When the “Signals” treeelement of a script is selected, the grid area will present you with
an overview of all the Signals, that have been defined by the script. You can also see,
whether a signal is active or not and relevant settings, regarding the signal, such as Phy.
Min/Max or Sampling Rate. Some of these setting can be edited directly in the grid area.

Additional display settings regarding the signal can be accessed via the details area
“Display” tab.

• Displaying area

Shows the value range which will be shown on a display. It usually should match the
“Physical range” from the “Scaling” tab.

• Formatting

The dropdown menu “Decimal places” allows you to set how many decimal num-
bers of the value will be shown on a display.

Changesanderrorsexcepted.

425

11.6 DETAILSAREAFORSCRIPTS

• Name

Allows you to set a Name to be shown on a display.

11.5.3 Methods in Scripts (deprecated)

Defining methods for your configuration from within a script is no longer
supported, unless your logger is running in “Compatibility mode” for old
configurations.

It is therefore still possible to define methods from within a script but at
Check/Export this will cause a warning saying the method defined by
the script is no longer supported.

When the “Methods” treeelement of a script is selected, the grid area will present you
with an overview of all the methods, that have been defined by the script. You can also
see, whether a method is active or not, the description and type of the method as well
as the file type.

11.6 Details area for Scripts

The Details area provides settings for the script, that has been selected in the measure-
ment task tree.

General
Please refer to (→4.2.2).

Changesanderrorsexcepted.

426

11.7 EXPORTINGASCRIPT

11.7 Exporting a script

It is also possible to export a script and thus make it available for use in other configura-
tions. To do so, select the desired script in the measurement task tree, click the “Export”
button in the Ribbon and then select “DataLog script”.

The following window lets you choose the path, where to save the script file. Confirm with
“Save”.

Changesanderrorsexcepted.

427

12 INCLUDES

12 Includes

The “Includes” interface allows you to include partial configurations in your system. This
can be especially helpfull for components of a configuration that are likely to change
over time, such as Wifi accesspoints, and are used by a large number of loggers at the
same time.

12.1 Adding the Includes-Interface

In order to work with Includes, you will first need to add the “Includes” interface to your
system. To do so, select the system in the tree, click the “Components” button in the
Ribbon and then choose “Includes”.

Once the “Includes” interface has been added to your system, you can then add multiple
“Includes”. To do so, select the “Includes” interface in the tree, click the “Components”
button in the Ribbon and then choose “Include”.

Changesanderrorsexcepted.

428

12.2 TREEELEMENTSFORINCLUDES

12.2 Tree elements for Includes

After having added the “Includes” interface to your system it will appear as a tree
element wit the name “Includes”.

12.3 Grid area for Includes

If the “Includes” interface is selected in the tree, the Grid area will present you with an
overview of the Includes which have been added to your system so far.
Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

12.4 Details area for Includes

The Details area provides settings for the Include, that has been selected in the grid area.
General
Please refer to (→4.2.2).

Settings
This tab provides settings regarding the include file.

• Copy to dataset

Activating this setting will
traceability.

include a copy of this include file in the dataset for

Changesanderrorsexcepted.

429

12.4 DETAILSAREAFORINCLUDES

• Mode

Define, whether you want to include a specific file or the entire directory of the
include path.

If the mode is set to “Include a specific file”, the included file must be of
the type *.ccmi or *.cfginclude.

• Path

Define the cfginclude file path relative to “[cfgdir (see data transfer)]/includes/”.
The file path must end wit a slash (/). Further information regarding the path of the
configuration directory (cfgdir) can be found in the chapter “Transfer connections”
here (→16.3.1.1).

• Local

Marks this include file as a local include that is specific to this logger. For local includes
the Path must be relative to “[cfgdir (see data transfer)]/[frontnumber]/includes/”.

• Optional

This setting allows you to mark an include as “Optional”. An optional include will not
produce an error message upon export of the configuration if the corresponding
include file cannot be found.
Instead it only produces a warning message but
export will still happen.

Changesanderrorsexcepted.

430

13 EXTERNALFILES

13 External files

The function “External files” allows to include in the .ccmc a database file (DBC, AUTOSAR,
FIBEX etc.), that has been used to import signals into a signal channel (CAN, LIN, FlexRay or
ETH), as external file. When exporting your configuration, the external file will be included
in the .ccmc container and can thus be made available for later use in acquisition data
analysis or can be included in a dataset. All external files will be stored on the logger
alongside the configuration file.

The function “External files” is available for CAN, LIN, FlexRay and ETH.

13.1 Automatically add external files

In addition to manually adding a database as external file to your configuration, it is
possible to set up a configuration in such a way, that every signal database that gets
imported in any one signal channel will automatically be added as external file to that
signal channel.

To enable this setting, navigate to the “Options” window of IPEmotion.

Changesanderrorsexcepted.

431

13.1 AUTOMATICALLYADDEXTERNALFILES

In the following window navigate to the “PlugIns” tab of the sidebar and access the
plugin-specific settings for “CAETEC dataLog” by clicking the button with the blue screw
wrench symbol right next to “CAETEC dataLog”.

In the following window navigate to the “Options” tab and activate the tickbox for the
setting “Create and synchonize external files”. In this way, whenever you import a signal
database to a channel, it will be automatically be added as external file.

Changesanderrorsexcepted.

432

13.2 DATABASEEXTRACTIONFROMEXTERNALFILES

13.2 Database extraction from external files

In order to work with signals from a database, which has been attached as external file,
it is possible to extract databases from external files and thus make them available for
import.
Extracted databases will be saved in their original file format in the IPEmotion import
directory.

In order to automatically extract databases from external files navigate to the plugin
specific option as described above (→13.1) and choose the desired database extraction
mode from the dropdown menu.

Overviewofdatabaseextractionmodes

Extraction mode
No extraction of databases

Skip existing databases

Characteristics
Database files are not copied to the IPEmotion im-
port directory.
Database files are copied to the IPEmotion import
directory. If the file already exists, it is skipped.

Overwrite existing databases Database files are copied to the IPEmotion import
directory. If the file already exists, it is overwritten.
Database files are copied to the IPEmotion import
directory. If the file already exists, the extracted file
is saved with an index.

Extract
databases

existing

copy

of

Changesanderrorsexcepted.

433

13.3 ADDINGTHEEXTERNALFILESINTERFACE

13.3 Adding the External files interface

To add the “External files” interface to a signal channel, select the desired channel in the
measurement task tree, click the “Components” button in the Ribbon and then choose
“External files”.

13.4 Adding an external file

Once the interface has been added to the signal channel, you can then add one or mul-
tiple external files. To do so, select the resepective “External files” interface in the mea-
surement task tree, click the “Import” button in the Ribbon and then choose the desired
database type.

The available database types for external files depend on the type of
signal channel, to which they will be linked. So while an external file for a
CAN channel may be of the type CANdb, AUTOSAR or FIBEX, an external
file for an Ethernet channel can only be of the type AUTOSAR or FIBEX.

Changesanderrorsexcepted.

434

13.5 TREEELEMENTSFOREXTERNALFILES

In the following window you may then choose your database file and confirm with “OK”.

13.5 Tree elements for External files

Once the “External files” interface has been added to a signal channel it will appear as
a child element to the respective channel in the measurement task tree.

13.6 Grid area for External files

The grid area for “External files” will provide you with an overview of the added external
files for a signal channel.
It also provides information on the type of database and the
location of the original database file to be included.

Changesanderrorsexcepted.

435

13.7 DETAILSAREAFOREXTERNALFILES

13.7 Details area for External files

The details area for “External files” will provide you with settings regarding a single
database file that has been selected in the grid area.

General
Please refer to (→4.2.2).

File settings
This tab allows you to select the database file, you wish to include. To do so, click the
three dots at the right of the field.
In the following window navigate to the location of
your database file and confirm.

Changesanderrorsexcepted.

436

14 SURVEILLANCE

14 Surveillance

There are multiple functions for monitoring data acquisition and logger activity. This sec-
tion will give an overview of these functions and explain their functionality in detail.

14.1 Displays

You can connect a display to your logger in order to display certain displays, events,
video streams and messages. CAETEC dataloggers and the CAETEC dataLog PlugIn for
IPEmotion support two types of displays:

• CAETEC display (→14.1.3)

• third party openABK display (→14.1.4)

Configuration of these displays via the plugin will be explained in detail in the following.

14.1.1 Adding a display

In order to add a display to your system, you will first need to add the “Displays” interface.
To do so, select the system in the measurement task tree (the topmost element in the
tree,in this case ARCOS 1.5), click the “Components” button in the Ribbon and select
“Displays”.

Changesanderrorsexcepted.

437

14.1 DISPLAYS

In the next step you can add one of the two available display types to your system. To
do so, select the “Displays” interface in the tree, click the “Components” button in the
Ribbon and then select the display type you wish to add.

For instructions regarding the configuration of the single display types please refer to the
respective sections of this manual:

• CAETEC display (→14.1.3)

• third party openABK display (→14.1.4)

For instructions regarding the configuration of the entire “Displays” interface please keep
reading on below.

Changesanderrorsexcepted.

438

14.1 DISPLAYS

14.1.2 The “Displays” interface

In order to access the settings regarding the entire “Displays” interface including all addi-
tionally connected display types, select the tree element “Displays” and navigate to the
details area. The details area contains two tabs which will be explained here.

General
Please refer to (→4.2.2).

Settings
This tab contains settings specific for the “Displays” interface.

• Language

Choose the standard display language.

• Display trigger counter Set the behaviour of the display trigger counter. There are

three available settings.

Display trigger counter setting Characteristics
Reset at new configuration

Reset at system start

Never reset

The trigger counter will be reset, when the logger
receives a new configuration.
The trigger counter will be reset, whenever the log-
ger restarts.
The trigger counter will never be reset.

Changesanderrorsexcepted.

439

14.1 DISPLAYS

14.1.3 CAETEC Display-specific settings

This section will explain settings specific for the CAETEC Display. These settings are to be
found in the details area of the CAETEC Display.

Autoscroll
Settings regarding the display’s autoscroll function. Pressing the trigger button will interrupt
autoscroll for a defined time interval.

• Autoscroll

Activate or deactivate the autoscroll function.

• Interval

Time interval after which autoscroll will be reactivated. Setting this parameter to 0
will also deactivate the autoscroll function.

Changesanderrorsexcepted.

440

14.1 DISPLAYS

14.1.4 openABK Display-specific settings

This section will explain settings specific for the openABK Display. These settings are to be
found in the details area of the openABK Display.

Files
Define which display-configuration files will be included in the loggers configuration.

• Export IPEmotion APP

This setting allows you to export a display-configuration for the IPEmotion APP. The
display-configuration file will be included in the logger configuration. As soon as
a display gets connected to the logger, the display will check whether a corre-
If so, the display will
sponding display-configuration file is available on the logger.
automatically download the display-configuration and apply it.

For instructions on how to configure the IPEmotion APP as a display de-
vice, please refer to the IPEmotion documentation.

• Export EMBU-Chart

This setting allows you to export a display-configuration for an EMBU display device.
The display-configuration file will be included in the logger configuration. As soon
as a display gets connected to the logger, the display will check whether a corre-
If so, the display will
sponding display-configuration file is available on the logger.
automatically download the display-configuration and apply it.

Changesanderrorsexcepted.

441

14.1 DISPLAYS

Audio signal from Display
The openABK protocol allows to configure an audio signal coming from the openABK
display, provided that the display possesses a microphone. If that is the case, the logger
will automatically receive the audio signal from the display. This signal is set to inactive
by default, in order to activate it, select the “Microphone” tree element of your openABK
display, navigate to the grid area and set active the “Audio signal 01” as shown in the
figure below.

This figure also shows, that by default the openABK tree element possesses the “Micro-
phone” tree element which contains the “Audio signal 01”, independent of whether the
display actually possesses a microphone or not.

Storage
In order to store the audio signal use “WAV” as storage method. Please refer to (→ 15.13).

Settings
For details regarding the audio signal itself and the related settings please refer to the
chapter “Details area for audio recordings” (→8.21.4).

Changesanderrorsexcepted.

442

14.1 DISPLAYS

Priorities
Set the priorities for the “Violation” and the “Status” dialog. The dialog with the higher
priority will be shown if both dialogs appear at the same time.

DLUA Export (Create EMBU-Sys firmware dlua)
The “DLUA Export” function allows you to to create an EMBU-Sys firmware dlua for open-
ABK displays. The *.dlua container is necessary to install firmware updates of any kind on
your logger.
For more information on updating the firmware of your logger please refer to the chapter
“Updating licenses, firmware and web interface of the logger” (→4.5.5).

In order to create an EMBU-Sys firmware dlua you will first need to add an openABK
display to your configuration. For instructions on how to do so please refer to (→14.1.1).
Then navigate to the “DLUA Export” tab of the openABK display’s details area.

Click the button on the right end of the “Firmware file” field in order to select the firmware
file for your display. The file needs to be in the *.exe file format.

Changesanderrorsexcepted.

443

14.1 DISPLAYS

In the field labeled “Firmware version” fill in the version of the firmware as provided by the
manufacturer.

The firmware version number provided by EMBU-Sys conists of four parts
(e.g. 1.3.0.16) whereas the CTCPI for IPEmotion only allows you to fill in a
version number with tree parts (e.g. 1.3.16).
The third part of the EMBU-Sys version number is by default always a 0
and is ignored by the CTCPI for IPEmotion. So in order to convert the
EMBU-Sys version number to a CTCPI compatible format just leave out
the third part when typing it into the “Firmware version” field (e.g. 1.3.0.16
becomes 1.3.16).

In order to export the *.dlua container select the openABK display in the measurement
task tree, click the “Functions” button in the Ribbon and then choose “Create EMBU-Sys
firmware dlua”.

Changesanderrorsexcepted.

444

14.1 DISPLAYS

Finally choose a filename and path and save the file.

Changesanderrorsexcepted.

445

14.1 DISPLAYS

14.1.5 General Display settings

14.1.5.1 Tree elements for a Display

Adding the a to your system will add one new child element with the name
“CAETEC/openABK Display” to the “Displays” interface. The “CAETEC/openABK Display”
will again possess the three child elements: Signals, Buttons, Messages.

14.1.5.2 Grid area for a Display

In the “Grid area” you will be presented with an overview of the available Signals, Buttons
or Display messages, depending which tree element has been selected. Also you can
find here two important functions, which are the “Column chooser” (→4.2.5) and the
“Filter editor” (→4.2.6).

Changesanderrorsexcepted.

446

14.1 DISPLAYS

14.1.5.3 Details area for a Display

The details area for a display provides settings for the behaviour of the display.

General
Please refer to (→4.2.2).

Extended
Settings regarding the display of the selected signal.

• Export display name

Set checkbox to force export of the parameter display name to the connected dis-
play device.

• Add signals automatically

If set, all eligible signals will be automatically added to the display. Any signals that
have already been added will not be removed if they becom ineligible.

Changesanderrorsexcepted.

447

14.1 DISPLAYS

14.1.5.4 Signals for Display

The “Signals” element allows you to select one or more signals to be displayed on the
connected display-device. To do so, select the “Signals” element, click on the “Compo-
nents” button in the Ribbon and then choose “Signal”.

In the following window you will be presented with an overview of all the available signals
for display. Choose one or more signals that you wish to display and confirm with “OK”.

In order to access the settings regarding the signals to be displayed please proceed as
follows. Select the treeelement “Signals”, then select the desired signal in the grid area
and access the settings in the details area.

Changesanderrorsexcepted.

448

14.1 DISPLAYS

General
The description field allows you to give a user specific description. The Reference field
serves as the tree element’s unique identifier inside the measurement task tree. It cannot
be changed.

Display
Settings regarding the display of the selected signal.

• Display name

Define a name for the selected signal, which will be displayed if the function “Export
display name” has been enabled.

• Decimal places

Define the count of decimal places for the signal.

Changesanderrorsexcepted.

449

14.1 DISPLAYS

14.1.5.5 Buttons for Display

The CAETEC and openABK Displays possess one “Trigger button”, which will be shown in
the grid area when selecting the “Buttons” element in the measurement task tree.
To access settings regarding this “Trigger button”, select the treeelement “Buttons” and
then select the “Trigger button” in the grid area. The setting can be found in the “Trigger
button’s” details area.
General
The name field allows you to give a user specific name ot the trigger button and the
description field allows you to give a user specific description. The Reference field serves
as the tree element’s unique identifier inside the measurement task tree.
It cannot be
changed.

Trigger
The field “Fired trigger” tells you the trigger to be fired if the button is pressed.

Changesanderrorsexcepted.

450

14.1 DISPLAYS

14.1.5.6 Messages for Display

The “Messages” element allows you to set up one or more customized “Display messages”
which will be displayed when triggered. To do so, select the “Messages” element, click on
the “Components” button in the Ribbon and then choose “Display message”. Multiple
“Display messages” can be defined.
The content and trigger of the message may be defined in the message’s settings in the
details area.

To access a message’s settings, select it in the grid area and then navigate to the details
area.

General
This tab allows you to activate or deactivate a Display message by ticking/unticking the
checkbox.
It also allows you to give a user specific name if wished and add an additional description.
The Reference field serves as the unique identifier inside the measurement task tree.
It
cannot be changed.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

Changesanderrorsexcepted.

451

14.1 DISPLAYS

Trigger
In this tab you can define which trigger will cause the display of a “Display message”.

Settings
In the “Text” field you may type in the message you would like to be displayed.

• Title

Fill in the title of the message. You may use the Script expression editor (→8.27.2.2) to
compose a message using the available variables, operands and operators.

• Text type

Define whether the email text is plain text or contains a complete HTML document.

• Body
Fill
in the text, that will be contained in the message. You may use the Script
expression editor (→8.27.2.2) to compose a message using the available variables,
operands and operators.

In the field “Text” project parameters can be used as variables. For more
information please refer to (→5.6).

Changesanderrorsexcepted.

452

14.2 E-MAILS

14.2 E-mails

For surveillance-purposes it is possible to configure e-mails with user-specific content.
Sending of these e-mails will be triggered by user-defined events.

14.2.1 Setting up the E-mails interface

In order to set up the “E-mails” interface, you will first need to add it to your system and
then configure its SMTP settings. These steps will be explained in the following.

14.2.1.1 Adding the E-mails interface

In order to add the “E-mails” interface select your system in the measurement task tree
(the topmost elemenet of the tree), click the “Components” button in the Ribbon and
then select “E-mails”.

Changesanderrorsexcepted.

453

14.2 E-MAILS

14.2.1.2 Configure SMTP

In order for the logger to be able to send e-mails, the SMTP settings have to be correctly
set. To do so, fill in your e-mail provider’s SMTP server details as well as your user name,
password and sender.
To do so, select the “E-mails” interface in the measurement task tree, navigate to the
“SMTP” tab in the details area and fill in the fields.

Connection
The field connection allows you to set the connection you wish to use for this SMTP
configuration. Possible Connections are Ethernet and PPP connections.

In the field “Sender” project parameters can be used as variables. For
more information please refer to (→5.6).

Changesanderrorsexcepted.

454

14.2 E-MAILS

14.2.2 Composing e-mails

This section will explain how to compose new e-mails and how to define a trigger for send-
ing an e-mail.

14.2.2.1 Creating a new e-mail

In order to compose an e-mail, you will first need to create it. To do so, select the “E-mails”
interface in the measurement task tree, click on the “Components” button in the Ribbon
and choose “E-mail”:

14.2.2.2 Tree elements for E-mails

Each e-mail, that you have created in the “E-mails” interface will appear as a child ele-
ment to the “E-mails” interface in the tree.
Each of these e-mail elements will possess four child elements itself, that will allow you to
attach certain files to an e-mail. This will be explained in the chapter “E-mail attachments”
(→14.2.3).

Changesanderrorsexcepted.

455

14.2 E-MAILS

14.2.2.3 Grid area for E-mails

In the “Grid area” you will be presented with an overview of all the e-mails, that have been
created so far, as well as details regarding those e-mails, such as subject, recipient, trigger
etc. Also you can find here two important functions, which are the “Column chooser”
(→4.2.5) and the “Filter editor” (→4.2.6).

14.2.2.4 Details area for E-mails (Composing)

The Details area shows settings for “E-mails” allows you to compose an e-mail and set its
trigger, as well as general settings.

General
This tab allows you to activate or deactivate the e-mail by ticking/unticking the checkbox.
It also allows you to give a user specific name if wished and add an additional description.
The Reference field serves as the tree element’s unique identifier inside the measurement
task tree. It cannot be changed.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

Changesanderrorsexcepted.

456

14.2 E-MAILS

Trigger
This tab allows you to set the trigger which will cause an e-mail to be sent. For each e-mail
a trigger needs to be defined. And while each e-mail can only have one trigger defined,
the same trigger can be defined for multiple mails.

Settings
This is the tab, where the actual composing of the e-mail happens.

• Recipient

Fill in the e-mail addresse, that will receive the e-mail. Multiple recipients are possible.
They have to be separated by comma, semicolon or a white space.

• Subject

Fill in a subject for the e-mail. You may use the Script expression editor (→8.27.2.2)
to compose a dynamic message using the available variables, operands and
operators.

• Text type

Define whether the email text is plain text or contains a complete HTML document.

• Body

Fill in the text, that will be contained in the e-mail. You may use the Script expression
editor (→8.27.2.2) to compose a dynamic message using the available variables,
operands and operators.

Changesanderrorsexcepted.

457

14.2 E-MAILS

In the field “Body” project parameters can be used as variables. For
more information please refer to (→5.6).

14.2.3 E-mail attachments

It is possible to attach files to e-mails and therefore make some parts of the acquired
measurement data available for remote analysis on the fly. There are four different types
of attachments available, that will be explained in the following.

• Signals(→14.2.3.1)

• Datafiles(→14.2.3.2)

• Logfiles(→14.2.3.3)

• Datasets(→14.2.3.4)

14.2.3.1 Signal attachments

To attach signals to an e-mail, select the “Signals” child element of the e-mail, to which
you wish to attach signals, in the tree, click the “Components” button in the Ribbon and
then choose “Signal”.

Changesanderrorsexcepted.

458

14.2 E-MAILS

The following window allows you to choose all the signals you wish to attach to the e-mail.
Select all the signal you wish to attach and confirm with “OK”.

The grid area of the child element “Signals” will present you with an overview of all the
signals that have been selected for attachment.

Changesanderrorsexcepted.

459

14.2 E-MAILS

14.2.3.2 Datafile attachments

To attach datafiles to an e-mail, select the “Datafiles” child element of the e-mail, to
which you wish to attach signals, in the tree and navigate to the grid area. Here you
will be presented with an overview of all the datafiles that currently exist within your
configuration (if you havent added any datafile yet, the grid area will remain empty).
Select the datafiles you wish to attach via the tickbox labeled “Attach to mail”.

“Script file” datafiles are no longer available as e-mail attachments.

If you select any of the datafiles in the grid area and navigate to the details area, you
may access settings regarding the attached file.

General
Please refer to (→4.2.2).

Settings
Datafile attachment specific settings.

• Attach to mail.

Same functionality as in the grid area. Mark active to attach this file to mail.

• Number of data files

Define the maximum number of datafiles included in the attachment. Newer
datafiles take precedence over older ones if the maximum size has been reached.

Changesanderrorsexcepted.

460

14.2 E-MAILS

• Maximum size

Define the maximum total size of the attachment.
limit for all
included data files. If the “Maximum size” is set to 1 Mb and data file 1 has 900 Kb,
there will be only 100 Kb remaining for all the other data file attachments.

This size is a total

14.2.3.3 Logfile attachments

To attach logfiles to an e-mail, select the “Logfiles” child element of the e-mail, to which
you wish to attach signals, in the tree, click the “Components” button in the Ribbon and
then choose “Logfile”.

The grid area of the child element “Logfiles” will present you with an overview of all the
logfiles that have attached.

Changesanderrorsexcepted.

461

14.2 E-MAILS

If you select any of the logfiles in the grid area and navigate to the details area, you may
access settings regarding the attached file.

General
Please refer to (→4.2.2).

Settings
Logfile attachment specific settings.

• Logfile type

Define whether the logfile of the current run should be attached or a logfile from a
specific dataset.

• Dataset name

If the logfile type has been set to dataset, choose here the dataset from which you
wish to include the logfile.

• Maximum size

Define the maximum total size of the attachment.

14.2.3.4 Dataset attachments

To attach datasets to an e-mail, select the “Datasets” child element of the e-mail, to
which you wish to attach signals, in the tree and navigate to the grid area. Here you
will be presented with an overview of all the datasets that currently exist within your
configuration.
Select the datafiles you wish to attach via the tickbox labeled “Attach to mail”.

Changesanderrorsexcepted.

462

14.2 E-MAILS

If you select any of the datasets in the grid area and navigate to the details area, you
may access settings regarding the attached file.

General
Please refer to (→4.2.2).

Settings
Datafile attachment specific settings.

• Attach to mail

Same functionality as in the grid area. Mark active to attach this file to mail.

• Include running

If set, the running dataset is finished and included in the attachment.

• Number of data files

Define the maximum number of datafiles included in the attachment. Newer
datafiles take precedence over older ones if the maximum size has been reached.

• Maximum size

Define the maximum total size of the attachment.
included datasets.
there will be only 100 Kb remaining for all the other dataset attachments.

limit for all
If the “Maximum size” is set to 1 Mb and dataset 1 has 900 Kb,

This size is a total

Changesanderrorsexcepted.

463

14.3 LOGFILEMESSAGES

14.3 Log file messages

For surveillance-purposes it is possible to configure log file messages with user-specific con-
tent. These messages will be written into the log file when triggered by a user defined
trigger.

14.3.1 Adding the Log file messages interface

In order to create log file messages, you will first need to add the “Log file messages”
interface to your system. To do so, select the system in the measurement task tree (the
topmost element of the tree), click the “Components” button in the Ribbon and then
choose “Log file messages”.

14.3.2 Create a new Log file messages interface

Once the “Log file message” interface has been added to your system, you can now
create a new message. To do so, select the “Log file messages” interface in the mea-
surement task tree, click the “Components” button in the Ribbon and then choose “Log
file message”.

Composing and configuration of the message will be explained in the section “Details
area for Log file messages” (→14.3.3.2).

Changesanderrorsexcepted.

464

14.3 LOGFILEMESSAGES

14.3.3 Composing Log file messages

This section will explain how to compose log file messages and how to define a trigger for
writing the message to the log file.

14.3.3.1 Grid area for Log file messages

In the “Grid area” you will be presented with an overview of all the Log file messages, that
have been created so far, as well as details regarding those Log file messages, such as
the trigger and text of the message.
Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

Changesanderrorsexcepted.

465

14.3 LOGFILEMESSAGES

14.3.3.2 Details area for Log file messages (Composing)

The Details area for “Log file messages” allows you to compose the message and set its
trigger, as well as general settings.
To access the details area for a certain “Log file message”, select the message in the grid
area and then navigate to the grid area.

General
This tab allows you to activate or deactivate the Log file message by ticking/unticking the
checkbox.
It also allows you to give a user specific name if wished and add an additional description.
The Reference field serves as the tree element’s unique identifier inside the measurement
task tree. It cannot be changed.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

Trigger
This tab allows you to set the trigger which will cause a Log file message to be written to
the log file. For each Log file message a trigger needs to be defined. And while each
Log file message can only have one trigger defined, the same trigger can be defined for
multiple mails.

Changesanderrorsexcepted.

466

14.3 LOGFILEMESSAGES

Settings
This is the tab, where the actual composing of the Log file message happens. Write in any
text you wish in the field labeled “Text”. This text will then be written as a message to the
log file when triggered.

• Title

Fill in the title of the message. You may use the Script expression editor (→8.27.2.2)
to compose a dynamic title using the available variables, operands and operators.

• Text type

Define whether the email text is plain text or contains a complete HTML document.

• Body
Fill
in the text, that will be contained in the message. You may use the Script
expression editor (→8.27.2.2) to compose a dynamic message using the available
variables, operands and operators.

In the field “Text” project parameters can be used as variables. For more
information please refer to (→5.6).

Changesanderrorsexcepted.

467

14.4 MONITORING

14.4 Monitoring

The “Monitoring” interface allows you to define certain limit values or ranges for a signal or
channel and monitor if these limits are being violated. The result of monitoring operations
can be displayed live on any connected display.

In order to do so, you will first need to add the “Monitoring” interface to your system.
Select the system (the topmost element of the tree) in the measurement task tree, click
the “Components” button in the Ribbon and then choose “Monitoring”.

Next you will need add and configure either a “Limit value” or a “Range”. To do so
please refer to the respective sections of this chapter:

• Booleans (→14.4.2)

• Limit value (→14.4.3)

• Range (→14.4.4)

14.4.1 Tree elements for Monitoring

Once the “Monitoring” interface has been added to your system, it will apper as a new
tree element in the measurement task tree. It will also contain three child elements called
“Booleans”, “Limit value” and “Range”.
These child elements will contain all the “Booleans”, “Limit values” and “Ranges”, that you
later add to your system.

Changesanderrorsexcepted.

468

14.4 MONITORING

14.4.2 Booleans

The “Booleans” function in “Monitoring” allows you to define a boolean condition in con-
nection with a signal. If the boolean condition becomes true, a user-specific action will
be executed.

14.4.2.1 Adding Booleans

In order to add a boolean, select the tree element “Booleans”, click on the “Components”
button in the Ribbon and then choose “Boolean”.

14.4.2.2 Grid area for Booleans

In the “Grid area” you will be presented with an overview of all the Booleans, that
have been created so far, as well as details regarding those Booleanss, such as signal,
operation, etc..
Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

It is now also possible to display the Monitoring Reference values directly
in the grid area. To do so, use the “Column Chooser” in order to add the
“Reference value” column to the grid area. For instructions regarding
the column chooser please refer to (→4.2.5).

Changesanderrorsexcepted.

469

14.4 MONITORING

14.4.2.3 Details area for Booleans

The Details area contains settings regarding the Booleans.

General
Please refer to (→4.2.2).

Configuration
This tab allows you to define to which signal a boolean should apply.

• Signal

Choose the Signal to which the boolean will apply.

• Operation

This setting is by default set to boolean and cannot be changed.

• Reference value

The reference value is the boolean condition. It can be a fixed value, a signal or a
formula. For details on working with the formula editor please refer to (→8.27.1.4).

Actions
This tab allows you to define what action will be taken, should a boolean condition be-
come true.

• Display

If activated, a Display option will be used. The Display option comes with further
settings in extra tabs, that need to be set. These extra settings will be explained in
the sections concerning the “Display” tabsheet (→14.4.2.3) and the “Parameter x”
tabsheet (→14.4.2.3).

Changesanderrorsexcepted.

470

14.4 MONITORING

• Logfile

If set active, a logfile entry will be created upon limit violation or if a boolean condi-
tion becomes true.

• Trigger

If set, a trigger action will be used. You may further set the trigger mode to Posi-
tive/Negative Edge or Stateful.

• Eventlist

If set, an eventlist entry will be created, if either the “EVENT” or the “FEGER” header
is used in the dataset. Please refer to (→15.1.3).

• Trigger groups

If the above “Trigger” setting has been activated, and a trigger is defined, this setting
allows you to see how many trigger groups this trigger has been assigned to. The
“Assign” button opens a selection dialog which lets you change the trigger group
assignment of the trigger.

Display
Define the display output settings.

• HID dialog priority

Define the HID dialog priority. Higher priorities are ranked higher and will thus be
preferred if there is a multiple occurrence of display actions.

• HID dialog class

Define the HID dialog class, that will be displayed when a display action occurrs.

Changesanderrorsexcepted.

471

14.4 MONITORING

• Suppress startup warning

If this tickbox is marked active, no warning will be shown on the display, if the limit is
already exceeded at startup.

Changesanderrorsexcepted.

472

14.4 MONITORING

Parameter x
This tab allows you define the type fo parameter that should be displayed and its content.
Up to 5 parameters can be defined.

• Mode

Define whether no parameter, a static parameter or a dynamic parameter should
be displayed.

• Name

Define the parameter name.

• Static value

Define the parameter value for a static parameter.

• Dynamic value

Select a signal as the parameter value for a dynamic parameter.

Changesanderrorsexcepted.

473

14.4 MONITORING

14.4.3 Limit value

The “Limit value” function in “Monitoring” allows you to define a single value for a signal
and to compare the signal to this value. The result of this comparison will be put out to the
connected display.

14.4.3.1 Adding a limit value

In order to add a limit value, select the tree element “Limit value”, click on the “Compo-
nents” button in the Ribbon and then choose “Limit value”.

14.4.3.2 Grid area for Limit values

In the “Grid area” you will be presented with an overview of all the limit values, that have
been created so far, as well as details regarding those limit values, such as channel,
operation, output etc..
Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

It is now also possible to display the Monitoring Reference values directly
in the grid area. To do so, use the “Column Chooser” in order to add the
“Reference value” column to the grid area. For instructions regarding
the column chooser please refer to (→4.2.5).

Changesanderrorsexcepted.

474

14.4 MONITORING

14.4.3.3 Details area for Limit values

The Details area contains settings regarding the limit value.

General
This tab provides general settings for a limit value.

• Name

Give a user-defined Name to the selected Limit value.

• Description

Give a user-defined description to the selected Limit value.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

Configuration
This tab allows you to define to which signal a limit value should apply, as well as in what
way.

• Signal

Choose the Signal to which the limit value will apply.

Changesanderrorsexcepted.

475

14.4 MONITORING

• Operation

Select the boolean operator by which the signal will be compared to the limit value.
This will determine whether you will get a result when the signal hits the reference
value, exceeds it or falls below it.

• Reference value

The reference value is the value to which the signal will be compared. It can be a
fixed value, a channel or a formula. For details on working with the formula editor
please refer to (→8.27.1.4).

• Continuity

Define the required minimum duration of a limit violation or boolean true-value in
order to be put out .

• Repeat interval

Interval before reactivation of the event if the limit violation is still existent or the
boolean condition is still true.

Actions
This tab allows you to define what action will be taken, should a limit violation occurr.

• Display

If activated, a Display option will be used. The Display option comes with further
settings in extra tabs, that need to be set. These extra settings will be explained parts
of this section concerning the “Display” tabsheet (→14.4.3.3) and the “Parameter x”
tabsheet (→14.4.3.3).

• Logfile

If set active, a logfile entry will be created upon limit violation or if a boolean condi-
tion becomes true.

• Trigger

If set, a trigger action will be used. You may further set the trigger mode to Posi-
tive/Negative Edge or Stateful.

• Eventlist

If set, an eventlist entry will be created, if either the “EVENT” or the “FEGER” header
is used in the dataset. Please refer to (→15.1.3).

Changesanderrorsexcepted.

476

14.4 MONITORING

• Trigger groups

If the above “Trigger” setting has been activated, and a trigger is defined, this setting
allows you to see how many trigger groups this trigger has been assigned to. The
“Assign” button opens a selection dialog which lets you change the trigger group
assignment of the trigger.

Display
Define the display output settings.

• HID dialog priority

Define the HID dialog priority. Higher priorities are ranked higher and will thus be
preferred if there is a multiple occurrence of display actions.

• HID dialog class

Define the HID dialog class, that will be displayed when a display action occurrs.

• Suppress startup warning

If this tickbox is marked active, no warning will be shown on the display, if the limit is
already exceeded at startup.

Changesanderrorsexcepted.

477

14.4 MONITORING

Parameter x
This tab allows you define the type fo parameter that should be displayed and its content.
Up to 5 parameters can be defined.

• Mode

Define whether no parameter, a static parameter or a dynamic parameter should
be displayed.

• Name

Define the parameter name.

• Static value

Define the parameter value for a static parameter.

• Dynamic value

Select a signal as the parameter value for a dynamic parameter.

Changesanderrorsexcepted.

478

14.4 MONITORING

14.4.4 Range

The “Range” function in “Monitoring” allows you to define a double set of limit values.
You can thus create a Range of values to which to compare the signal. The result of this
comparison will be put out to the log file and can can additionally be displayed on a
connected display.

14.4.4.1 Adding a Range

In order to add a Range, select the tree element “Range”, click on the “Components”
button in the Ribbon and then choose “Range”.

14.4.4.2 Grid area for Ranges

In the “Grid area” you will be presented with an overview of all the Ranges, that have
been created so far, as well as details regarding those Ranges, such as channel, opera-
tion, output etc..
Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

It is now also possible to display the Monitoring Reference values directly
in the grid area. To do so, use the “Column Chooser” in order to add the
“Reference value” column to the grid area. For instructions regarding
the column chooser please refer to (→4.2.5).

Changesanderrorsexcepted.

479

14.4 MONITORING

14.4.4.3 Details area for Ranges

The Details area contains settings regarding the Range.

General
Please refer to (→4.2.2).

Configuration
This tab allows you to define to which signal a Range should apply, as well as in what way.

For a Range you need to define a top limit value and a bottom limit value. You can then
compare the signal to that range and see if it is inside or outside of the range.

• Signal

Choose the Signal to which the Range will apply.

• Operation

Select the boolean operator by which the signal will be compared to the Range.

• (Top/Bottom) Reference value

The reference value is the value to which the signal will be compared. It can be a
fixed value, a channel or a formula. For details on working with the formula editor
please refer to (→8.27.1.4).

• Continuity

Define the required minimum duration of a limit violation or boolean true-value in
order to be put out.

• Repeat interval

Interval before reactivation of the event if the limit violation is still existent or the
boolean condition is still true.

Changesanderrorsexcepted.

480

14.4 MONITORING

Actions
This tab allows you to define what action will be taken, should a limit violation occurr.

• Display

If activated, a Display option will be used. The Display option comes with further
settings in extra tabs, that need to be set. These extra settings will be explained parts
of this section concerning the “Display” tabsheet (→14.4.4.3) and the “Parameter x”
tabsheet (→14.4.4.3).

• Logfile

If set active, a logfile entry will be created upon limit violation or if a boolean condi-
tion becomes true.

• Trigger

If set, a trigger action will be used. You may further set the trigger mode to Posi-
tive/Negative Edge or Stateful.

• Eventlist

If set, an eventlist entry will be created, if either the “EVENT” or the “FEGER” header
is used in the dataset. Please refer to (→15.1.3).

Changesanderrorsexcepted.

481

14.4 MONITORING

• Trigger groups

If the above “Trigger” setting has been activated, and a trigger is defined, this setting
allows you to see how many trigger groups this trigger has been assigned to. The
“Assign” button opens a selection dialog which lets you change the trigger group
assignment of the trigger.

Changesanderrorsexcepted.

482

14.4 MONITORING

Display
Define the display output settings.

• HID dialog priority

Define the HID dialog priority. Higher priorities are ranked higher and will thus be
preferred if there is a multiple occurrence of display actions.

• HID dialog class

Define the HID dialog class, that will be displayed when a display action occurrs.

• Suppress startup warning

If this tickbox is marked active, no warning will be shown on the display, if the limit is
already exceeded at startup.

Parameter x
This tab allows you define the type fo parameter that should be displayed and its content.
Up to 5 parameters can be defined.

• Mode

Define whether no parameter, a static parameter or a dynamic parameter should
be displayed.

• Name

Define the parameter name.

• Static value

Define the parameter value for a static parameter.

• Dynamic value

Select a signal as the parameter value for a dynamic parameter.

Changesanderrorsexcepted.

483

14.5 XCPSLAVE

14.5 XCP slave

“XCP slave” allows you to connect the logger to a PC via ethernet and let the PC func-
tion as XCP master. That means, the PC will be requesting and receiving signals from the
logger.

14.5.1 Adding XCP slave

In order to add XCP slave, select the system in the measurement task tree (the topmost
element of the tree), click the “Components” button in the Ribbon and then choose “XCP
slave”.

14.5.2 Tree elements for XCP slave

Adding “XCP slave” to the system will add one new tree element called “XCP slave”.

14.5.3 Grid area for XCP slave

The Grid area provides you with an overview of the ethernet channels available for XCP
slave. Here you need to select the ethernet channel you wish to use by ticking the “Use
as XCP slave” tickbox.

It is possible to select multiple ethernet channels for XCP slave, but if you
choose more than one channel, all available channeles will be acti-
vated automatically.

Changesanderrorsexcepted.

484

14.5 XCPSLAVE

14.5.4 Details area for XCP slave

The details area for XCP slave contains all the important settings regarding the xcp slave
connection.

The important settings for XCP slave are located in the details area of the
tree element “XCP slave”, not in the details area of any of the ethernet
connections in the grid area.

General
Please refer to (→4.2.2).

A2L
This tab provides settings regarding the type and location of the A2L file provided to a PC
for establishing a connection with the ECU.

• Export to dataset

Activating this option will store the entire A2L file of the logger, including all bus-, ECU-
and logger-signals, inside the dataset. From there it can be copied to your PC and
used for XCP slave.

• Enable download

Activating this option will make the A2L file of the logger, including all bus-, ECU- and
logger-signals, available for download from the web interface. From there it can be
downloaded to your PC and used for XCP slave.

• Reduce data

If this option is activated, only a reduced file size A2L file will be available for copy-
ing/download. This A2L file will only contain the information necessary for the PC to
connect to the logger, from where it can then download the entire A2L file including
all bus-, ECU- and logger-signals.

Changesanderrorsexcepted.

485

14.5 XCPSLAVE

• Invert names

If this option is set, the measurement names will be written in reversed order. This
can be useful for working with some third-party tools.

Example

Regularorder: ’some’::’namespace’::’signalname’
Reversedorder: ’signalname’::’namespace’::’some’

Changesanderrorsexcepted.

486

15 DATASETS

15 Datasets

Data acquired throughout a measurement task will be stored in a dataset or a ring buffer
by the logger. This chapter will explain how to configure datasets and ring buffers.

15.1 Dataset

This section will explain how to configure a regular dataset.

15.1.1 Adding extra datasets

By default a system is configured with one dataset.
multiple datasets.
To do so, select the “Datasets” interface in the measurement task tree, click the “Compo-
nents” button in the Ribbon and then choose “Dataset”.

It is possible however, to configure

15.1.2 Tree elements for Datasets

The tree element “Datasets” will contain all the datasets you configure for your system.
The child element “Dataset” then contains the single components of your dataset.

Changesanderrorsexcepted.

487

15.1 DATASET

15.1.3 Details area for Datasets

This section contains settings regarding the overall behaviour of your dataset.
settings are global and will affect all components of your dataset.

These

In case the parent tree element “Dataset” selected, the details area will only show the
“General” tab. Please refer to (→4.2.2).

In case the child element “Dataset” is selected, the details area will contain additional
tabs which will be explained in the following.

General
Please refer to (→4.2.2).

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

File settings
This tab contains settings regarding filename and location.

Changesanderrorsexcepted.

488

15.1 DATASET

• Filename formatting

This field allows you to define the filename formatting of the final dataset file. Both
methods and protocols have to possible formatting options:

◦ Method/Protocol name with timestamp: protocol name with timestamp (date

and time)(default setting)

◦ Timestamp, trigger name and counter: Appends the name of the activating
trigger and its number/counter to the right of the timestamp in the file name.

• Log and configuration files This field allows you to set whether your dataset file wil be
stored externally or internally and what type of configuration to embed. There are
four types of configuration available:

◦ Complete, compressed CCMC container: Entire container is stored as is.
◦ Uncompressed contents of CCMC container: Content of the container is un-

packed and stored.

◦ Only CFG: Only the cfg is extracted.
◦ Complete, compressed CCMC container and uncompressed contents: Entire
container is stored as is and the unpacked content of the container is stored as
well.

Dataset settings
This tab allows for settings regarding the dataset itself.

• Dataset format

Define whether the directory structure of data within a dataset contains subdirecto-
ries or not.

• Dataset encoding

Set the type of encoding and compression level for the dataset.

Changesanderrorsexcepted.

489

15.1 DATASET

• Dataset name

This field allwos you to select, whether a timestamp will be appended to the dataset
name.

Also you can define an alias for this dataset. The alias can then be used to reference
the dataset in configuration includes. The alias has to be unique within all datasets.

• Storage target

This dropdown menu allows you to select, where the dataset shall be stored.

Storage target
Home partition
Partition with
datalog_extension_cfg
Left/Right drivebay slot

Custom storage label

Description
Dataset will be stored on the internal home partition
Dataset will be stored on an external drive with a dat-
alog_extension_cfg
Dataset will be stored on an extension disk installed in
the left/right drivebay slot
Dataset will be stored to a custom partition. Custom
partition can be created and managed via the log-
gers webinterface.

• Custom storage label

Here you can fill in the name of the custom partition if the option “Custom storage
label” has been selected.

Generate
Define settings regarding the creation of the dataset.

• Mode

Choose between continuous data acquisition or triggered data acquisition.

• Start- and Pause-trigger

This field allows you, to set triggers to start or pause dataset creation.

If you do

Changesanderrorsexcepted.

490

15.1 DATASET

not set a start trigger, then by default dataset creation is always active during
measurement.

• Completion

The dropdown menu “Condition” allows you to set a condition under which the
dataset should be closed and completed.
In case your condition for completion
requires a trigger, you may choose the trigger in the below field.
If you choose “Compress after completion”, the file will be compressed directly after
completion. If you do not choose this option, the dataset will be compressed before
transfer.

• Saving-mode

Select the saving-mode. The different options are listed below.

Saving-mode
Keep all datasets
Keep marked datasets

Characteristics
All datasets will be saved.
Choose a trigger to mark the dataset if the trigger is
fired. Only marked datasets will be saved, all other
datasets will be discarded.
Discard marked datasets Choose a trigger to mark the dataset if the trigger is
fired. All marked datasets will be discarded, all other
datasets will be saved.

• Mark-trigger

Select a trigger to mark a dataset.

Changesanderrorsexcepted.

491

15.1 DATASET

Header
When storing the data, the logger saves general
information about the measurement
(identification, comments, start, stop) and information about the data files (name, struc-
ture) in a header file. For additional functionality a various headers with specific options
can be attached. The options of each activated header-type will be accessible in a sep-
arate tab with the header-type’s name.
Multiple header-types can be activated at the same time.

• ATFX

• EVENT

• FEGER

Changesanderrorsexcepted.

492

15.1 DATASET

15.1.4 Setting up a dataset

A dataset can be set up using different filetypes, according to what information you
want it to contain. Each filetype you include in your dataset has specific functionalities
and for each included filetype will later be included a file in the exported dataset with its
preivously configured name and the according filetype extension.

In order to include a filetype in your dataset, select the tree element “Dataset”.

Changesanderrorsexcepted.

493

15.1 DATASET

Then click the “Components” button in the Ribbon and choose the desired filetype from
the resulting menu.

The following sections will explain in detail the different filetypes.

Changesanderrorsexcepted.

494

15.2 RINGBUFFER

15.2 Ring buffer

A ring buffer is a dataset, that can continuously store data from bus trace files and AVI
files. Once the defined maximum file size has been reached, old acquisition data from
the beginning of the dataset will be erased in order to store new acquisition data. In this
way, the ring buffer always keeps a specified amount of the most recent acquisition.
It is, however, possible to define certain triggers that will mark a certain datafile, that will
then not be deleted. Please refer to (→15.10.6.1).

15.2.1 Adding a ring buffer

To add a ring buffer to your configuration, select the “Datasets” interface in the mea-
surement task tree, click the “Components” button in the Ribbon and then choose “Ring
buffer”.

15.2.2 Setting up a ring buffer

The datafiles that will be included in a ring buffer can be set up in the same way as in a
dataset. Please refer to the chapter “Setting up a dataset” (→15.1.4).

Other than a dataset, a ring buffer can only contain the following filetypes:

• MDF 4.1 (Bus trace only) (→15.9)

• Vetor BLF / Vector ASCII / Vector ASCII compressed (→15.10)

• PCAP (→15.11)

• AVI (→15.12)

The sections of this manual for each of the three filetype mentioned above will contain a
part that will explain the specifics of that filetype when used in a ring buffer.

Changesanderrorsexcepted.

495

15.2 RINGBUFFER

15.2.3 Tree elements for ring buffer

Once a ring buffer has been added, it will appear as a child element to the “Dataset”
interface in the measurement task tree.

15.2.4 Grid area for ring buffer

In the “Grid area” you will be presented with an overview of all the datafiles, that have
been added to the ring buffer and you can activate or deactivate single filetypes for
storage in the ring buffer.
Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

15.2.5 Details area for Ring buffer

This section contains settings regarding the behaviour of your ring buffer.

General
Please refer to (→4.2.2).

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

Changesanderrorsexcepted.

496

15.2 RINGBUFFER

File settings
This tab contains settings regarding file name formatting.

• Filename formatting

This field allows you to define the filename formatting of the final ring buffer file. Both
methods and protocols have two possible formatting options:

◦ Method name/Protocol name with timestamp: protocol name with timestamp

(date and time)(default setting)

◦ Timestamp, trigger name and counter: Appends the name of the activating
trigger and its number/counter to the right of the timestamp in the file name.

Dataset settings
This tab allows for settings regarding the ring buffer itself.

• Dataset format

Define whether the directory structure of data within a ring buffer contains subdi-
rectories or not.

• Dataset encoding

Set the type of encoding and compression level for the ring buffer.

• Dataset name

This field allwos you to select, whether a timestamp will be appended to the ring
buffer name.

Changesanderrorsexcepted.

497

15.2 RINGBUFFER

Also you can define an alias for this ring buffer.
The alias can then be used to
reference the ring buffer in configuration includes. The alias has to be unique within
all ring buffers.

Generate
Define settings regarding the creation of the ring buffer.

• Mode

Choose between continuous data acquisition or triggered data acquisition.

• Start- and Pause-trigger

If you do
This field allows you, to set triggers to start or pause ring buffer creation.
not set a start trigger, then by default ring buffer creation is always active during
measurement.

Changesanderrorsexcepted.

498

15.3 DATASETPROJECTSETTINGS

15.3 Dataset Project settings

The “Project settings” filetype is meant for including Project information such as company
name, serial number, project name etc.
in your dataset. Multiple “Project settings” files
can be included in your dataset. The “Project settings” filetype for dataset creates a set of
project parameters that will be included only in the respective dataset. In order to define
“Project settings” that apply globally to the entire configuration and that get exported
with every dataset, please refer to (→5).

15.3.1 Adding project parameters

It is possible, to add user-specific project parameters in addition to the default project pa-
rameters. To do so, select the desired “Project settings xx” element in the measurement
task tree, select the “Components” button in the Ribbon and then choose “Project pa-
rameter”.

The new parameter will appear in the respective “Project settings xx” Grid area as cus-
tomizable parameter in the table.

Changesanderrorsexcepted.

499

15.3 DATASETPROJECTSETTINGS

15.3.2 Assigning a template of project parameters

It is also possible, to assign a template which contains a predefined set of user-specific
project parameters. To do so, right-click on the “Project settings xx” tree element and
then choose “Assign template”.

In the following window you may choose the template file and confirm wit “Open”. The
file type needs to be .xml.

15.3.3 Tree elements for Project settings

Including a “Project settings” file in your dataset will add one new child element per in-
cluded “Project settings” file to your tree element “Dataset”. The tree element is labeled
“Project settings xx”.

Changesanderrorsexcepted.

500

15.3 DATASETPROJECTSETTINGS

15.3.4 Grid area for Project settings

If a “Project settings xx” element is selected in the Measurement task tree, the grid area
will provide you with a table, that allows you to access all default or previously defined
user-specific projet parameters.

15.3.5 Details area for Project settings

If a “Project settings xx” element has been selected in the measurement task tree, addi-
tional settings are available in the details area.
General
This tab provides general settings for the selected Project settings file.

• Name

Give a user-defined Name to the selected formula/signal.

• Description

Give a user-defined description to the selected formula/signal.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Changesanderrorsexcepted.

501

15.3 DATASETPROJECTSETTINGS

Info
Tells you the type of template that has been assigned.

Changesanderrorsexcepted.

502

15.4 DATASETSPECIALSETTINGS

15.4 Dataset special settings

The “Dataset special settings” allow you to write an extra set of information regarding
bus channel aliases and XCP settings to the dataset file, similar to the “Dataset project
settings”. Unlike the “Dataset project settings” the “Dataset special settings” are no mere
set of information typed in in the form of a string, but they dynamically adapt to your
configuration.
Meaning that they only allow you to store settings and information to the dataset file, that
is relevant to your configuration.

15.4.1 Overview of available special settings

The following list gives an overview of the available “Dataset special settings”

• Bus channel settings

Allows you to write a bus channel’s alias information to the datset file.

• XCP A2L settings

Allows you to write the name of the A2L file corresponding to the selected XCP station
to the dataset file.

• XCP transport layer settings

Allows you to write the type of transport layer for the selected XCP station to the
dataset file.

• XCP version settings

Allows you to write the EPK version of the selected XCP station to the dataset file.

15.4.2 Adding Dataset special settings

In order to work with the “Dataset special settings” you will first need to add the “Dataset
To do so, select the desired dataset in the measurement
special settings” interface.
task tree, click the “Components” button in the Ribbon and choose “Dataset special
settings”.

Changesanderrorsexcepted.

503

15.4 DATASETSPECIALSETTINGS

Once the interface has been added you will now be able to add the individual special
settings. To do so, select the “Dataset special settings” interface in the measurement task
tree, click the “Components” button in the Ribbon and then choose the desired special
settings.
You may also add more than one setting at once, using the “Multiple selection” field.

15.4.3 Tree elements for Dataset special settings

After having added the “Dataset special settings” interface to your dataset it will appear
as a child element to the dataset with the name “Dataset special settings”.

Also each individual setting you add to the interface will appear as a child element to
the interface in the measurement task tree.

Changesanderrorsexcepted.

504

15.4 DATASETSPECIALSETTINGS

15.4.4 Grid area for Dataset special settings

The grid area will present you with an overview of available bus channels and XCP
stations whose information can be written to the dataset file in accordance with your
current configuration.
The column labeled “Select channel” allows you to individually select bus channels/XCP
stations whose information is to be written to the dataset file. Alternatively you can
choose to write all bus channels’/XCP stations’ information to the dataset file in the details
area for “Dataset special settings” (→15.4.5).

Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

Changesanderrorsexcepted.

505

15.4 DATASETSPECIALSETTINGS

15.4.5 Details area for Dataset special settings

The Details area provides settings for the individual special setting, that has been selected
in the measurement task tree.

General
Please refer to (→4.2.2).

Settings
The “Item selection” drop down menu in this tab allows you to set whether you wish
to write the information of all the bus channels/XCP stations, that are available for this
setting, to the dataset file or only the ones that have been selected in the grid area as
described here (→15.4.4).

Changesanderrorsexcepted.

506

15.5 INCLUDES

15.5 Includes

The “Includes” filetype allows you to include partial configurations in your dataset. This
can be especially helpfull for components of a configuration that are likely to change
over time, such as Wifi accesspoints, and are used by a large number of loggers at the
same time.

15.5.1 Adding the Includes-Interface

Adding the “Includes” filetype as described in the chapter “Setting up a dataset”
(→15.1.4), will add the “Includes” interface to your dataset.
Once the “Includes” interface has been added to your dataset, you can then add
multiple “Includes”. To do so, select the “Includes” interface in the tree, click the “Com-
ponents” button in the Ribbon and then choose “Include”.

15.5.2 Tree elements for Includes

After having added the “Includes” interface to your dataset it will appear as a child
element to the dataset with the name “Includes”.

Changesanderrorsexcepted.

507

15.5 INCLUDES

15.5.3 Grid area for Includes

If the “Includes” interface is selected in the tree, the Grid area will present you with an
overview of the Includes which have been added to your system so far.
Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

15.5.4 Details area for Includes

The Details area provides settings for the Include, that has been selected in the grid area.
General
Please refer to (→4.2.2).
Settings
This tab provides settings regarding the include file.

• Copy to dataset

Activating this setting will include a copy of this include file in the dataset for trace-
ability.

• Mode

Define, whether you want to include a specific file or the entire directory of the in-
clude path.

• Path

Define the cfginclude file path relative to “[cfgdir (see data transfer)]/includes/”. The
file path must end wit a slash (/).

• Optional

This setting allows you to mark an include as “Optional”. An optional include will not
produce an error message upon export of the configuration if the corresponding
include file cannot be found.
Instead it only produces a warning message but
export will still happen.

Changesanderrorsexcepted.

508

15.6 DATASETNETWORKDESTINATIONS

15.6 Dataset Network Destinations

The “Network Destinations” component allows you to define a set of network settings,
which will be written to a file, which is then stored parallel to a Dataset or Ring buffer. This
file in turn is then used by the readout station to transfer the data record after copying
from the logger to the readout station from the readout station to the defined path in the
company network.

SFTP may be used for this function.

15.6.1 Setting up Network Destinations

In order to set up a Network Destination you will first need to add the “Network Desti-
nations” interface to your Dataset/Ring buffer. To do so, select the Dataset/Ring buffer
in the measurement task tree, the click the “Components” button in the Ribbon and
choose “Network Destinations”.
The “Network Destinations” interface should appear as a child element to the corre-
sponding Dataset/Ring buffer in the measurement task tree.

Now that the “Network Destinations” interface has been added, select it, click the
“Components” button in the Ribbon and choose “Network Destination” to set up a
destination.
Multiple destinations may be defined per “Network Destinations” interface.

All “Network Destinations” that have been set up will appear in the Grid are when the
corresponding “Network Destinations” interface is selected in the measurement task tree.

Changesanderrorsexcepted.

509

15.6 DATASETNETWORKDESTINATIONS

15.6.2 Tree elements for Network Destinations

When the “Network Destinations” interface has been added to a Dataset/Ring buffe it will
appear as a child element to that Dataset/Ring buffer.

15.6.3 Grid area for Network Destinations

When selecting the “Network Destinations” interface in the measurement task tree, the
“Grid area” will present you with an overview of all “Network Destinations”, that have
been defined for that “Network Destinations” interface. The grid area also allows you to
directly access the individual destinations’ settings (Host, Port, Path, User name, Password),
which can also be found in the details area.
Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

Changesanderrorsexcepted.

510

15.6 DATASETNETWORKDESTINATIONS

15.6.4 Details area for Network Destinations

General
Please refer to (→4.2.2).

Settings
This tab allows you to set the network parameters for a selected destination.

• Host

Define the destination host IP address.

• Port

Define the SFTP port address.

• Path

Define the target file path on the host system. The path must be relative to the SFTP
path of the server.

• User name

Define the authentication user name on the host system.

• Password

Define the authentication password on the user system.

Changesanderrorsexcepted.

511

15.7 ATFX

15.7 ATFX

The “ATFX” filetype is meant for recording of signals. It is compatible with all signals that
produce values that can be represented on a 2-D graph. It is not compatible with video
or audio files.
The recorded signal values will be represented in a timelog.

15.7.1 Tree elements for ATFX

Including the “ATFX” filetype in your dataset will add three new child elements to your tree
element “Dataset”:

• ATFX xx

This element represents the ATFX file, which will later be included in your exported
dataset. You may add multiple files of the same filetype.

• Timelog

This element represents the timelog for recording signal values.

• Signal Group

The signal is a group of all the signals that the timelog will record and that will ulti-
mately be included in the exported dataset.

15.7.2 Grid area for ATFX

If the “Signal Group” is selected in the Measurement task tree, the grid area will show an
overview of the signals included in the “Signal Group”

Changesanderrorsexcepted.

512

15.7 ATFX

15.7.3 Details area for ATFX

The details area contains settings for the behaviour of your ATFX file, timelog or signal
group.

15.7.3.1 ATFX file

General
This tab provides general settings for the selected ATFX file.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected formula/signal.

• Description

Give a user-defined description to the selected formula/signal.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Changesanderrorsexcepted.

513

15.7 ATFX

File
This tab provides settings regarding the creation of the file.

• File type

Tells you the type of the created file.

• File create event

Define, when the ATFX file should be created. There are four possibilities:

File create event
On dataset begin
On recording start

On trigger

first
On
dataset)

trigger

(per

first
On
recording

trigger per

Characteristics
The file will be created once at logger start.
The file will be created everytime, recording via the
dataset is started or restarted after a pause. Starting
the recording may happen at the beginning of the
dataset (mode: Continuous acquisition) or via a trig-
ger (modes: Start and pause trigger; Stop is inverted
start). This may result in a splitting of the current dataset
file into multiple files, as a new file is created for each
time the dataset ist started.
The file will be created on a trigger and record for a
user defined duration. These settings can be defined
in the timelog settings (→ 15.7.3.2). This will result in a
splitting of the current ATFX file into multiple files, as a
new file is created for each timethe trigger is set.
The file will be created once, when the defined trigger
is set for the first time since the beginning of the dataset
and record for a user defined duration. These settings
can be defined in the timelog settings → 15.7.3.2). Each
following time the trigger is set, the data will be written
in the same previously created file. Therefore there will
only be one file.
The file will be created once, when the defined trig-
ger is set for the first time during a recording and save
data for a user defined duration. These settings can
be defined in the timelog settings → 15.7.3.2). Each fol-
lowing time the trigger is set during the same period of
recording, the data will be written in the same previ-
ously created file. Therefore there will only be one file
per recording.

Changesanderrorsexcepted.

514

15.7 ATFX

• Maximum file size

Define the maximum file size. It is recommended not to raise the maximum file size
above 2GB, as some third party analysis tools cannot handle files, that are larger.

• Create new file

If this box is marked active, a new file will be created, if the current file exceeds the
maximum file size.

• Data type

This dropdown menu allows you to switch the data type between float or double.

• Discard empty file

If this option is activated and the datafile is empty it will be discarded and not trans-
ferred.

Trigger
This tab allows you to define a span trigger for this dataset file. A span trigger will, upon
activation, cause the closure of the current and creation of a new ATFX file within the
existing dataset file.

To define a span trigger, click the “Select” button and choose anyone of the previously
configured triggers of your configuration. If no trigger suits the purpose, you will first need
to create one as described in the section “Triggers” (→10):

Changesanderrorsexcepted.

515

15.7 ATFX

15.7.3.2 ATFX Timelog

General
This tab provides general settings for the selected ATFX timelog.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

Changesanderrorsexcepted.

516

15.7 ATFX

Trigger
This tab provides settings regarding the trigger for the start and stop of the timelog. When
the timelog is started, all signals contained in the signal group will be stored to the ATFX
file according to their settings.
Furthermore will this trigger provoke the creation of the ATFX file, if you have choosen either
“On trigger” or “On first trigger” as “File create event”.

• Mode

Define whether you wish to continuously store data or if you want to start/stop data
storage via a trigger. There are two modes to control data storage via trigger:

Start and stop trigger allows you to set any previously defined trigger as start and/or
stop condition.

Stop is inverted start will store data as long as the start trigger condition is met. Once
it is no longer met and a possibly set Post-trigger duration has run out, data storage
will stop.

• Start-trigger

Define a trigger, that will start the timelog.

• Stop-trigger

Define a trigger, that will stop the timelog.

• Pre-trigger duration

Pre-trigger duration allows you to define, how long before the start trigger was set,
the timelog will start.

• Post-trigger duration

Post-trigger duration allows you to define, how long after the start trigger was set, the
timelog will stop.

Changesanderrorsexcepted.

517

15.7 ATFX

Extended
The field “Alias” allows you to give an alias to the method. The alias has to be unique
within the configuration.

An alias functions as a parameter that can later be referenced in includes/partial config-
urations.

User
The field “Identifier” allows you to give a user identifier to the timelog. It does not have any
effect other than helping the user identifiy a specific timelog.

Changesanderrorsexcepted.

518

15.7 ATFX

15.7.3.3 ATFX Signal Group

General
This tab provides general settings for the selected ATFX timelog.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected formula/signal.

• Description

Give a user-defined description to the selected formula/signal.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Storage
This tab allows for setting regarding the storage of the contained signals inside the ATFX
file.

• Storage mode

The storage mode in ATFX is fixed. It cannot be changed.

Changesanderrorsexcepted.

519

15.7 ATFX

• Storage rate

The storage rate defines how often the signals contained in this “Signal Group” will
be stored.

Storage rates with decimal places will be rounded to three decimal
places.

Changesanderrorsexcepted.

520

15.7 ATFX

15.7.4 Working with Signal Groups for ATFX

For filetypes intended for signal recording such as ATFX, MDF 4.0 and MDF 4.1, signals
need to be assigned to a “Signal Group” belonging to the timelog, in which you would
like the signal to be included. The signals, that are assigned to a “Signal Group” can then
be stored.

15.7.4.1 Assigning signals to Signal Groups

To assign a signal to a “Signal group”, select the “Signal group” in the “Measurement task
tree”, click the “Components” button in the Ribbon and choose “Signal”.

Changesanderrorsexcepted.

521

15.7 ATFX

In the following window you may choose all the available signals, that you wish to include
within this group and confirm by clicking “OK”.

ATFX can only contain one “Signal Group” and this “Signal Group” can
only have one storage rate. That means, all signals, that are contained
in the same “Signal Group”, will be stored with the same storag rate.

15.7.4.2 Cross reference, Storage group and Storage group reference

The functions “Cross reference”, “Storage group” and “Storage group reference” are
directly related to the “Signal group” function of timelogs in ATFX/MDF Dataset methods.
They all, with a different level of detail, aim to give a quick overview over the different
signal groups to which a signal has been assigned.

Cross reference
The “Cross reference” opens a separate window which will present you with an overview
of all the elements that reference a signal. Furthermore there are four descriptive columns
for each element.

Elementsthatwillbelistedin“Crossreference”:

• Timelog Signal groups

• Display Signal groups

• Email Signal groups

• Formulas

• Standard triggers

• Monitoring channels

Changesanderrorsexcepted.

522

15.7 ATFX

• Classings

To access the “Cross reference” function for any signal, right click on the desired signal
and choose “Cross reference” in the resulting context menu.

Changesanderrorsexcepted.

523

15.7 ATFX

Storage group
Through the “Column chooser” (→4.2.5) it possible to add the “Storage group” column
to the grid area. The “Storage group” column will list all Timelog Signal groups, to which
a signal has been assigned. Different “Signal groups” will be separated by comma and
each group’ storage rate is shown in parenthesis.

Storage group reference
Through the “Column chooser” (→4.2.5) it possible to add the “Storage group reference”
column to the grid area. The “Storage group reference” column will list all Timelog Signal
groups, to which a signal has been assigned, separated by comma. Additionally the
column will tell the name of the signal group, name of the timelog and name of the
method for each signal group, separated by slashes.

Changesanderrorsexcepted.

524

15.7 ATFX

15.7.5 Trigger groups for ATFX

A trigger group for ATFX allows to set up a group of triggers, whose activity will be stored to
the timelog. One ATFX file can only possess one trigger group with one fixed storage rate.
If you would like to store multiple groups of triggers with different storage rates, please refer
to MDF 4.0/4.1 (→15.8).

15.7.5.1 Adding a trigger group to timelog

In order to add a trigger group to a timelog, select the timelog in the measurement task
tree, click the “Components” button in the Ribbon and then select “Trigger group”.

Changesanderrorsexcepted.

525

15.7 ATFX

15.7.5.2 Assigning triggers to a group

In order to assign a trigger to a group, select the trigger group in the measurement task
tree and then navigate to the grid area. The grid area will present you with an overview
of all the available triggers. In order to store a trigger, select it and tick the box labeled
“Store trigger”.

In the grid area you can also set the storage rate.

As ATFX only supports one storage rate, this will affect the entire timelog
and all the signals and triggers that are stored within.

15.7.5.3 Details area for trigger groups

General
This tab provides general settings for the selected trigger group.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

Changesanderrorsexcepted.

526

15.7 ATFX

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Storage
This tab allows to set the storage rate.As ATFX only supports one storage rate, this will affect
the entire timelog and all the signals and triggers that are stored within.

Changesanderrorsexcepted.

527

15.8 MDF4.0

15.8 MDF 4.0

The “MDF 4.0” filetype is meant for recording of signals.
It is compatible with all signals
that produce values that can be represented on a 2-D graph. It is not compatible with
video or audio files.
The recorded signal values will be represented in a timelog.

MDF 4.0 and MDF 4.1 files can have (Other than ATFX) multiple “Signal
Groups” and some of those groups allow for include signals to be stored
in various rates.

15.8.1 Multiple timelogs in MDF 4.0

It is possible, to configure multiple timelogs within one MDF file. All timelogs that are
configured within one MDF file will later be stored in said MDF file.

To add another timelog in your MDF file, select the MDF file in the measurement task tree,
click the “Components” button in the Ribbon and then select “Timelog”.

Changesanderrorsexcepted.

528

15.8 MDF4.0

15.8.2 Bus trace in MDF 4.0/4.1

It is possible, to configure a bus trace within an MDF file. This bus trace will be stored
alongside other contained timelogs or bus traces within the MDF file. The bustrace for
MDF works the same as regular bus tracing methods, such as “Vector BLF” or “Vector
ASCII”, for details please refer to the chapter “Vector BLF/Vector ASCII/Vector ASCII
compressed” (→15.10).

To add a bus trace in your MDF file, select the MDF file in the measurement task tree, click
the “Components” button in the Ribbon and then select “Bus trace”.

It is possible to record star- and stop-triggger events in a bus trace. To
do so, navigate to the “Trigger” tab in the details area of the bus trace
and check the box for “Record start-/stop-trigger events”.

Changesanderrorsexcepted.

529

15.8 MDF4.0

15.8.3 Event writer in MDF 4.0

It is possible, to configure a an event writer within an MDF file. This event writer will record
all trigger events and monitoring events that are chosen to be stored. The event writer will
be stored alongside other contained timelogs or bus traces within the MDF file.

To add an event writer in your MDF file, select the MDF file in the measurement task tree,
click the “Components” button in the Ribbon and then select “Even writer”.

Changesanderrorsexcepted.

530

15.8 MDF4.0

15.8.4 Tree elements for MDF 4.0

Including the “MDF 4.0” filetype in your dataset will add multiple new child elements to
your tree element “Dataset”:

• MDF 4.0 xx

This element represents the MDF 4.0 file, which will later be included in your exported
dataset. You may add multiple files of the same filetype.

• Timelog

This element represents the timelog for recording signal values.

• Signal Group

The signal is a group of all the signals that the timelog will record and that will ulti-
mately be included in the exported dataset.

• Bus trace xx

This element represents a bus trace which will store all occurring traffic on a given
bus. All available buses will appear as child elements to this bus trace element.
This element only appears upon adding the Bus trace element to your MDF file.

• Event writer xx

This element represents an event writer which will store all occurring trigger events
which have been selected for storage.
This element only appears upon adding the Bus trace element to your MDF file.

Changesanderrorsexcepted.

531

15.8 MDF4.0

15.8.5 Grid area for MDF 4.0

15.8.5.1 Signal Group

If the “Signal Group” is selected in the Measurement task tree, the grid area will show an
overview of the signals included in the “Signal Group”.
Also you can access settings regarting the signals sampling rate and typ and storage rate.
If the signal group’s storage mode is is set to “Individual” (→15.8.6.4) the column “Sample
type” allows you to set each signal’s sample type.

15.8.5.2 Event writer

By clicking on the Event writer’s child element “Event group” in the measurement task
tree, the grid area will show an overview of all the available events, which can be chosen
to be recorded in the event writer.

In order to record an event in the event writer just activate the “Store event” checkbox in
the grid area for the given event.
Furthermore the grid area allows you to set the MDF 4.0/4.1 event type under which the
event will be stored. The available event types are:

• Trigger

• Marker point

• Marker range

Changesanderrorsexcepted.

532

15.8 MDF4.0

15.8.6 Details area for MDF 4.0

The details area contains settings for the behaviour of your MDF 4.0 file, timelog or signal
group.

15.8.6.1 MDF 4.0 File

General
This tab provides general settings for the selected MDF 4.0 file.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

File
This tab provides settings regarding the creation of the file.

• File type

Tells you the type of the created file.

Changesanderrorsexcepted.

533

15.8 MDF4.0

• File create event

Define, when the MDF 4.0 file should be created. There are four possibilities:

File create event
On dataset begin
On recording start

On trigger

On
first
dataset)

trigger

(per

On
first
recording

trigger per

Characteristics
The file will be created once at logger start.
The file will be created everytime, recording via the
dataset is started or restarted after a pause. Starting
the recording may happen at the beginning of the
dataset (mode: Continuous acqusisition) or via a trig-
ger (modes: Start and pause trigger; Stop is inverted
start). This may result in a splitting of the current dataset
file into multiple files, as a new file is created for each
time the dataset ist started.
The file will be created on a trigger and record for a
user defined duration. These settings can be defined
in the timelog settings (→ 15.8.6.2). This will result in a
splitting of the current ATFX file into multiple files, as a
new file is created for each timethe trigger is set.
The file will be created once, when the defined trigger
is set for the first time since the beginning of the dataset
and record for a user defined duration. These settings
can be defined in the timelog settings (→ 15.8.6.2).
Each following time the trigger is set, the data will be
written in the same previously created file. Therefore
there will only be one file.
The file will be created once, when the defined trig-
ger is set for the first time during a recording and save
data for a user defined duration. These settings can
be defined in the timelog settings (→ 15.8.6.2). Each
following time the trigger is set during the same period
of recording, the data will be written in the same pre-
viously created file. Therefore there will only be one file
per recording.

• Maximum file size

Define the maximum file size.
It is recommended not to raise the maximum file
size above 2GB, as some third party evaluation tools cannot handle files, that are
larger.

• Create new file

If this box is marked active, a new file will be created, if the current file exceeds the
maximum file size.

• Data type

This dropdown menu allows you to switch the data type between float or double.

• Discard empty file

If this option is activated and the datafile is empty it will be discarded and not trans-
ferred.

Changesanderrorsexcepted.

534

15.8 MDF4.0

Trigger
This tab allows you to define a span trigger for this dataset file. A span trigger will, upon
activation, cause the closure of the current and creation of a new MDF file within the
existing dataset file.

To define a span trigger, click the “Select” button and choose anyone of the previously
configured triggers of your configuration. If no trigger suits the purpose, you will first need
to create one as described in the section “Triggers” (→10):

15.8.6.2 MDF 4.0 Timelog

General
This tab provides general settings for the selected MDF 4.0 timelog.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

Changesanderrorsexcepted.

535

15.8 MDF4.0

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Trigger
This tab provides settings regarding the trigger for the start and stop of the timelog. When
the timelog is started, all signals contained in the signal group will be stored to the MDF
4.0 file according to their settings.
Furthermore will this trigger provoke the creation of the MDF 4.0 file, if you have choosen
either “On trigger” or “On first trigger” as “File create event”.

• Mode

Define whether you wish to continuously store data or if you want to start/stop data
storage via a trigger. There are two modes to control data storage via trigger:

Start and stop trigger allows you to set any previously defined trigger as start and/or
stop condition.

Stop is inverted start will store data as long as the start trigger condition is met. Once
it is no longer met and a possibly set Post-trigger duration has run out, data storage
will stop.

• Start-trigger

Define a trigger, that will start the timelog.

• Stop-trigger

Define a trigger, that will stop the timelog.

• Pre-trigger duration

Pre-trigger duration allows you to define, how long before the start trigger was set,
the timelog will start.

• Post-trigger duration

Post-trigger duration allows you to define, how long after the start trigger was set, the
timelog will stop.

• Record start-/stop-trigger

Activating this option will record start- and stop-trigger events in the timelog.

Changesanderrorsexcepted.

536

15.8 MDF4.0

Extended
The field “Alias” allows you to give an alias to the method. The alias has to be unique
within the configuration.

An alias functions as a parameter that can later be referenced in includes/partial config-
urations.

User
The field “Identifier” allows you to give a user identifier to the timelog. It does not have any
effect other than helping the user identifiy a specific timelog.

Changesanderrorsexcepted.

537

15.8 MDF4.0

15.8.6.3 MDF 4.0 Event writer

General
This tab provides general settings for the selected MDF 4.0 Event writer.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Changesanderrorsexcepted.

538

15.8 MDF4.0

Trigger
This tab provides settings regarding the trigger for the start and stop of the Event writer.
When the Event writer is started, all signals contained in the signal group will be stored to
the MDF 4.0 file according to their settings.
Furthermore will this trigger provoke the creation of the MDF 4.0 file, if you have choosen
either “On trigger” or “On first trigger” as “File create event”.

• Mode

Define whether you wish to continuously store data or if you want to start/stop data
storage via a trigger. There are two modes to control data storage via trigger:

Start and stop trigger allows you to set any previously defined trigger as start and/or
stop condition.

Stop is inverted start will store data as long as the start trigger condition is met. Once
it is no longer met and a possibly set Post-trigger duration has run out, data storage
will stop.

• Start-trigger

Define a trigger, that will start the Event writer.

• Stop-trigger

Define a trigger, that will stop the Event writer.

• Pre-trigger duration

Pre-trigger duration allows you to define, how long before the start trigger was set,
the Event writer will start.

• Post-trigger duration

Post-trigger duration allows you to define, how long after the start trigger was set, the
Event writer will stop.

• Record start-/stop-trigger

Activating this option will record start- and stop-trigger events in the Event writer.

Changesanderrorsexcepted.

539

15.8 MDF4.0

Extended
The field “Alias” allows you to give an alias to the method. The alias has to be unique
within the configuration.

An alias functions as a parameter that can later be referenced in includes/partial config-
urations.

User
The field “Identifier” allows you to give a user identifier to the Event writer. It does not have
any effect other than helping the user identifiy a specific Event writer.

Changesanderrorsexcepted.

540

15.8 MDF4.0

15.8.6.4 MDF 4.0 Signal Group

General
This tab provides general settings for the selected MDF 4.0 timelog.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected formula/signal.

• Description

Give a user-defined description to the selected formula/signal.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Changesanderrorsexcepted.

541

15.8 MDF4.0

Storage
This tab allows for settings regarding the storage of the contained signals inside the MDF
4.0 file.

• Storage mode

Storage mode
Fixed

From channel

Individual

On receive

On value change

Characteristics
The rate, at which the signals included in the “Signal
Group” will be stored, is the same for all included sig-
nals. You may set the rate below at “Storage Rate
The rate, at which the signals included in the “Signal
Group” will be stored, is the same as each signal’s
source channel. This may result in a “Signal Group” with
different storage rates for different signals, according
to their sourche channel’s sampling rate.
The rate, at which the signals included in the “Signal
Group” will be stored, can be individually set for each
signal. This may result in a “Signal Group” with different
storage rates for different signals. In “Individual” mode,
the sample type for the single signals can be set in the
grid area (→15.8.5).
A signal with the storage mode “On receive” will be
stored, whenever it is received by the logger. The set-
ting for the storage rate can be ignored.
A signal with the storage mode “On value change” will
be stored, whenever the incoming value of the signal
is different than the previous one. The setting for the
storage rate can be ignored.

• Storage rate

The storage rate defines how often the signals contained in this “Signal Group” will
be stored.

Storage rates with decimal places will be rounded to three decimal
places.

Changesanderrorsexcepted.

542

15.8 MDF4.0

15.8.7 Working with Signal Groups for MDF 4.0

For filetypes intended for signal recording such as ATFX, MDF 4.0 and MDF 4.1, signals
need to be assigned to a “Signal Group” belonging to the timelog, in which you would
like the signal to be included. The signals, that are assigned to a “Signal Group” can then
be stored.
Other than for ATFX files, MDF 4.0/4.1 files support multiple “Signal Groups” and storage
modes with different characteristics and therefore allow for a more flexible storage of
your data. For details on the different storage modes please refer to (→ 15.8.6.4).

This allows for example to create one “Signal Group” with a fixed storage rate of 10Hz,
one that stores signals according to their channel’s sampling rate and one that has an
individual storage rate for each signal.

15.8.7.1 Assigning signals to Signal Groups

To assign signals to a group, select the “Signal group” in the “Measurement task tree”,
click the “Components” button in the Ribbon and choose “Signal”.

Changesanderrorsexcepted.

543

15.8 MDF4.0

In the following window you may choose from all the available signals the ones, that you
wish to include within this group and confirm by clicking “OK”.

Even though the Plugin allows for different storage rates within one “Sig-
nal Group” in the case of the storage modes “From channel” and “In-
dividual”, technically each rate will be exported as a separate group in
the loggerconfig.
That means, if you have a “Signal Group” called “examplegroup” with
three different storage rates (1Hz, 10Hz, 100Hz), at export will be created
three groups named “examplegroup_1Hz”, “examplegroup_10Hz” and
“examplegroup_100Hz” (namemethod: signalgroup_storagerate).

15.8.7.2 Cross reference, Storage group and Storage group reference

The functions “Cross reference”, “Storage group” and “Storage group reference” are
directly related to the “Signal group” function of timelogs in ATFX/MDF Dataset methods.

These functions have been explained in detail previously, please refer to this chapter for
more information (→15.7.4.2).

Changesanderrorsexcepted.

544

15.8 MDF4.0

15.8.8 Trigger groups for MDF 4.0/4.1

A trigger group for MDF 4.0/4.1 allows to set up a group of triggers, whose activity will
be stored to the timelog. MDF timelogs support multiple storage rates and therefore it is
possible to create multiple trigger groups per timelog with an individual storage rate or
mode per trigger group.

15.8.8.1 Adding a trigger group to timelog

In order to add a trigger group to a timelog, select the timelog in the measurement task
tree, click the “Components” button in the Ribbon and then select “Trigger group”.

Changesanderrorsexcepted.

545

15.8 MDF4.0

15.8.8.2 Assigning triggers to a group

In order to assign a trigger to a group, select the trigger group in the measurement task
tree and then navigate to the grid area. The grid area will present you with an overview
of all the available triggers. In order to store a trigger, select it and tick the box labeled
“Store trigger”.

In the grid area you can also set the storage rate.

As MDF 4.0/4.1 supports multiple storage rates, this will affect only the
selected trigger group.

15.8.8.3 Details area for trigger groups

General
This tab provides general settings for the selected trigger group.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

Changesanderrorsexcepted.

546

15.8 MDF4.0

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Storage
This tab allows for settings regarding the storage of the triggers of the trigger group.

• Storage mode

Storage mode
Fixed

Individual

On value change

Characteristics
The rate, at which the triggers included in the “Trigger
group” will be stored, is the same for all included trig-
gers. You may set the rate below at “Storage Rate”
The rate, at which the triggers included in the “Trigger
group” will be stored, can be individually set for each
signal. This may result in a “Trigger group” with differ-
In “Individual”
ent storage rates for different triggers.
mode, the sample type for the single triggers can be
set in the grid area (→15.8.5).
A signal with the storage mode “On value change” will
be stored, whenever the incoming value of the signal
is different than the previous one. The setting for the
storage rate can be ignored.

• Storage rate

The storage rate defines how often the triggers contained in this “Trigger group” will
be stored.

Storage rates with decimal places will be rounded to three decimal
places.

Changesanderrorsexcepted.

547

15.9 MDF4.1

15.9 MDF 4.1

MDF 4.1 can largely be treated the same as MDF 4.0, with some differences, that will be
explained in the following.

15.9.1 File compression in MDF 4.1

MDF 4.1 files are compressed by default. The standard compression rate is set to 6 but
can be changed by the user in the “File” tab of the details area.

For further compression MDF 4.1 offers the option “Transpose data blocks”.

15.9.2 Header profiles in MDF 4.1

The dropdown menu “Header profile” in the “File” tab of your MDF 4.1 file allows you to
assign a header profile to the file. The available profiles are:

• Standard

• CANape

• MDA

• EDR

If an MDF 4.1 file, that has been created by a dataLog 2015.10.xx or 2015.14.xx, is being
read, the Header profile will be automatically set to EDR.

If the header profile is set to EDR and an EDR template has been assigned
in the project settings (→5.2), the EDR profile will autmatically fetch the
required information from the project settings.

Changesanderrorsexcepted.

548

15.9 MDF4.1

15.9.2.1 Comments reference

For the header profile Standard, CANape and MDR the option “Comments reference”
allows to reference comments and values from Project settings.
The pairs of names
and values contained in the Project settings will be written as header block common
properties. For more information regarding “Project settings” please refer to (→5).

To reference comments, select one of the three supported Header profiles, click the “Se-
lect” button next to the field “Comments reference” and select the “Project settings” file,
that you wish to reference.

15.9.2.2 Overview of header profiles and their differences

HD-Block

Field
hd_md_comments:
<com-
mon_properties>

CG-Block

Standard
Comments refer-
ence (→15.9.2.1)

CANape
Comments refer-
ence (→15.9.2.1)

MDA
Comments refer-
ence (→15.9.2.1)

EDR
-

Field
si_tx_name

Standard
-

CANape
-

MDA
-

si_tx_path
si_md_comment:
<com-
mon_properties>

-
-

-
-

-
-

1.5”

EDR
“CAETEC
AR-
COS” / “CAETEC
ARCOS
/
“CAETEC μCros”
/ “CAETEC μCros
1.1”
Frontnumber
“StorageGroup”,
“StorageRate”,
“TargetFile”

Changesanderrorsexcepted.

549

15.9 MDF4.1

CN-Block(timechannel)

Field
cn_tx_name
si_tx_name

Standard
“time”
-

CANape
“t”
-

si_tx_path

-

-

CN-Block(datachannel)

Field
cn_md_comment:
<names><display>

Standard
-

CANape
-

MDA
“time”
-

-

EDR
“time”
name of
group
Intervall

signal

“signal

MDA
Bus:
name/bus
name”
SOMEIP/OBD/
UDS/CCP/XCP:
“signal
name/station
name”
Namespace

EDR
-

ECU from source

Intervall

type,
Interface
PN, SN,
relative
channel number
Signal
type de-
scription accord-
ing to table “EDR
Use Cases Nam-
ing”
“CCP” / “XCP”
/ “KWP” / “UDS”
/ “FreeRunning” /
“NMEA”
Bus/OBD/UDS:
“file”,
“Mes-
sageID”; SomeIP:
“BusFileName”,
“Identifier”;
CCP/XCP: “file”,
“daq”

550

si_tx_name

si_tx_path

staion-/bus
name
“CAETEC
aLog
type]”
Namespace

or
dat-
[signal

si_md_comment:
<path><name>

si_md_comment:
<names> <descrip-
tion>

-

-

Namespace

staion-/bus
name
“CAETEC
aLog
type]”
-

or
dat-
[signal

staion-/bus
name
“CAETEC
aLog
type]”
-

or
dat-
[signal

-

-

si_md_comment:
<protocol>

“CCP” / “XCP” /
“KWP” / “UDS”

“CCP” / “XCP” /
“KWP” / “UDS”

“CCP” / “XCP” /
“KWP” / “UDS”

si_md_comment:
<com-
mon_properties>

-

-

-

Changesanderrorsexcepted.

15.9 MDF4.1

15.9.3 Video attachments in MDF 4.1

When working with an MDF 4.1 filesystem, you can attach “Video Streams” to your
timelog. As the video is only an attachment, it can not have its own triggers nor duration
settings. The video-file will be attached in the *.avi format and have the same filename
as the MDF file it belongs to. The MDF file knows about the existence and automatically
synchonizes the timelog and video.

15.9.3.1 Attaching a video

In order to attach a video, you will first need to add the “Video” component to your MDF
4.1 file.
Select the tree element “MDF 4.1 xx”, click the “Components” button in the Ribbon and
then choose “Video”.

Once the video component has been added to your MDF file, you can choose a video
signal, that you wish to attach.
Select the new tree element “Video stream”, click the “Components” button in the
Ribbon and then choose “Video signal”.

In the resulting window you will be presented with an overview of all the available video
signals. Choose the one, you wish to attach, and confirm with “OK”.

It is possible to attach multiple videos by adding an additinal “Video
Stream”. To do so, select the “Video” tree element, click on the “Com-
ponents” button in the ribbon and choose “Video Stream”.

Changesanderrorsexcepted.

551

15.9 MDF4.1

15.9.3.2 Details area for video in MDF 4.1

This section will explain the relevant settings for video attachments in MDF 4.1

Video xx General
The tab “General” for the tree element “Video xx” allows you to activate or deactivate
the video and give a user specific name.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

Changesanderrorsexcepted.

552

15.9 MDF4.1

Video xx Trigger
The tab “Trigger” for the tree element “Video xx” can mainly be neglected. The only
relevant field of this tabsheet is the “Mode”-field. It is read-only and shows you that your
video is an attachment to the MDF-file.

Video xx User
The tab “User” for the tree element “Video xx” allows you to define a user-specific
identifier to the video attachment. This identifier helps the user to later identify a specific
video attachment.

Video Stream Settings
The tab “Settings” for the tree element “Video Stream” allows you to set the framerate for
the video.

Changesanderrorsexcepted.

553

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

15.10 Vector BLF / Vector ASCII / Vector ASCII compressed

These three filetypes are equal in fuctionality and differ only in the final exported file.
The trace method records all the messages that arrive on the input bus (CAN, LIN,
FlexRay). Regardless of the signals defined, all the messages are recorded. Filter rules
can be defined to reduce the data volume. A typical trace application is the acquisition
of all raw data in order to later evaluate the total traffic on the channel. Unlike most of
the other methods, traces are event-oriented. This means the messages are not retrieved
from the channels according to a set time pattern, but are recorded as soon as they
arrive on the channel. This method accordingly has no parameter for sampling rate.

Including a bus tracing filetype in your datasete will produce a “Warning”
message, saying that “at least one channel must be set active”.

Please refer to the section “Bus trace” (→ 15.10.4.3), in order to activate
a channel for tracing.

The function trigger trace, which allows to trace all activity of a trigger,
is available for the following dataset methods:

• Vector ASCII

• Vector ASCII compressed

It is not available for:

• Vector BLF

15.10.1 Tree elements for bus/trigger tracing

Including a bus tracing filetype in your dataset will add various new child elements to your
tree element “Dataset”:

• Vector BLF / Vector ASCII / Vector ASCII compressed xx

This element represents the bus tracing file, which will later be included in your ex-
ported dataset. You may add multiple files of the same filetype.

Changesanderrorsexcepted.

554

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

• Trigger trace

This element represents the “Trigger trace” for recording trigger activity.

• Bus trace

This element represents the “Bus trace” for recording all the traffic on a selected bus
channel.

• Bus channels available for tracing

As child elements to the tree element “Bus trace” will appear all the Bus channels
which are currently available for tracing.

Changesanderrorsexcepted.

555

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

15.10.2 Grid area for trigger tracing

If the “Trigger trace” is selected in the Measurement task tree, the grid area will show an
overview of the triggers available for tracing.
At least one channel must be marked active for tracing, by setting active the setting
“Trace trigger”.

15.10.3 Grid area for bus tracing

If the “Bus trace” is selected in the Measurement task tree, the grid area will show an
overview of the Bus channels available for tracing.
At least one channel must be marked active for tracing, by setting active the setting
“Trace channel”.

The Storage channel number is an alternative channel number which can be written
into the datafile according to the user’s needs and which can differ from the physical
channel number.

The grid area will also show you the Physical channel number for each traceable channel.

If an ID Filter has been added for a Bus trace channel, selecting this Bus trace channel in
the tree will show an overview of the existing ID Filters in the grid area.
For information on working with ID Filters for Bus trace, please refer to the chapter Bus trace
ID Filter (→15.10.5).

Changesanderrorsexcepted.

556

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

15.10.4 Details area for bus/trigger tracing

The details area contains settings for the behaviour of your bus tracing file (Vector BLF /
Vector ASCII / Vector ASCII compressed), the “Bus trace” component or a traceable Bus
channel.

15.10.4.1 Bus tracing file

General
This tab provides general settings for the selected bus tracing file.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

Changesanderrorsexcepted.

557

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

File
This tab provides settings regarding the creation of the file.

• File type

Tells you the type of the created file.

• File create event

Define, when the bus tracing file should be created. There are four possibilities:

Changesanderrorsexcepted.

558

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

File create event
On dataset begin
On recording start

On trigger

On
first
dataset)

trigger

(per

On
first
recording

trigger per

Characteristics
The file will be created once at logger start.
The file will be created everytime, recording via the
dataset is started or restarted after a pause. Starting
the recording may happen at the beginning of the
dataset (mode: Continuous acqusisition) or via a trig-
ger (modes: Start and pause trigger; Stop is inverted
start). This may result in a splitting of the current dataset
file into multiple files, as a new file is created for each
time the dataset ist started.
The file will be created on a trigger and record for a
user defined duration. These settings can be defined
in the timelog settings (→ 15.10.4.3). This will result in a
splitting of the current ATFX file into multiple files, as a
new file is created for each timethe trigger is set.
The file will be created once, when the defined trigger
is set for the first time since the beginning of the dataset
and record for a user defined duration. These settings
can be defined in the timelog settings (→ 15.10.4.3).
Each following time the trigger is set, the data will be
written in the same previously created file. Therefore
there will only be one file.
The file will be created once, when the defined trig-
ger is set for the first time during a recording and save
data for a user defined duration. These settings can be
defined in the timelog settings (→ 15.10.4.3). Each fol-
lowing time the trigger is set during the same period of
recording, the data will be written in the same previ-
ously created file. Therefore there will only be one file
per recording.

• Maximum file size

Define the maximum file size.
It is recommended not to raise the maximum file
size above 2GB, as some third party evaluation tools cannot handle files, that are
larger.

• Create new file

If this box is marked active, a new file will be created, if the current file exceeds the
maximum file size.

• Timestamp

This dropdown menu allows you to set the format of the timestamp for the file.

• Discard empty file

If this option is activated and the datafile is empty it will be discarded and not trans-
ferred.

Changesanderrorsexcepted.

559

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

Trigger
This tab allows you to define a span trigger for this dataset file. A span trigger will, upon
activation, cause the closure of the current and creation of a new Vector BLF/Vector
ASCII/Vector ASCII Compressed file within the existing dataset file.

To define a span trigger, click the “Select” button and choose anyone of the previously
configured triggers of your configuration. If no trigger suits the purpose, you will first need
to create one as described in the section “Triggers” (→10):

15.10.4.2 Trigger trace

General
This tab provides general settings for the selected “Trigger trace”.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

Changesanderrorsexcepted.

560

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Settings
This tab provides settings for a trigger, that is selected in the grid area.

• Trace trigger

Set active in order to trace this trigger.

• Message mode

Select the type of message written to the trace file.

• Channel number

If the message mode has been set to “Virtual message”, this field allows you to
define the virtual channel number to identify the virtual message.

• CAN ID

If the message mode has been set to “Virtual message”, this field allows you to
define the virtual CAN ID to identify the trigger message.

Changesanderrorsexcepted.

561

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

15.10.4.3 Bus trace

General
This tab provides general settings for the selected “Bus trace”.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Trigger
This tab provides settings regarding the trigger for the start and stop of the “Bus trace”.
When the “Bus trace” is started, all traffic on the channel will be stored to the bus tracing
file.
Furthermore will this trigger provoke the creation of the bus tracing file, if you have choosen
either “On trigger” or “On first trigger” as “File create event”.

Changesanderrorsexcepted.

562

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

• Mode

Define whether you wish to continuously store data or if you want to start/stop data
storage via a trigger. There are two modes to control data storage via trigger:

Start and stop trigger allows you to set any previously defined trigger as start and/or
stop condition.

Stop is inverted start will store data as long as the start trigger condition is met. Once
it is no longer met and a possibly set Post-trigger duration has run out, data storage
will stop.

• Start-trigger

Define a trigger, that will start the “Bus trace”.

• Stop-trigger

Define a trigger, that will stop the “Bus trace”.

• Pre-trigger duration

Pre-trigger duration allows you to define, how long before the start trigger was set,
the “Bus trace” will start.

• Post-trigger duration

Post-trigger duration allows you to define, how long after the start trigger was set, the
“Bus trace” will stop.

Extended
This tab provides extended settings for “Bus trace”.

• Include internal events

Define whether the occurrance of internal events should be stored in the trace data.

• Include all trigger events

Define whether all trigger events should be stored in the trace data.

• Alias

The field “Alias” allows you to give an alias to the method. The alias has to be unique
within the configuration.

Changesanderrorsexcepted.

563

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

An alias functions as a parameter that can later be referenced in includes/partial
configurations.

User
The field ￿Identifier￿ allows you to give a user identifier to the Bus trace. It does not have
any effect other than helping the user identifiy a specific Bus trace.

Changesanderrorsexcepted.

564

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

15.10.4.4 Traceable Bus channel

Settings

• Trace channel

Mark this box activ in order to trace this channel.

• Default filter action

Define the default action for an ID Filter if it has been defined. For information on
working with ID Filters for Bus trace, please refer to the chapter Bus trace ID Filter
(→15.10.5).

• Channel number

Define an alternative channel number that will be written in the datafile instead of
the physical channel number.

Changesanderrorsexcepted.

565

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

15.10.5 Bus trace ID Filter

For “Bus trace” it is possible to specify one or more “ID Filters”. Such it is possible to specify
a singe ID or an ID range for a Bus and filter incoming traffic on that bus accrodingly.
It is possible to either block all traffic except the specified ID/ID range or to pass all traffic
except the specified ID/ID range.

In order to specify an “ID Filter”, you will first need to add the “ID Filter” component to the
desired Bus channel. To do so, select the desired Bus trace channel in the tree, click on
The new “ID Filter”
the “Components” button in the Ribbon and then choose “ID Filter”.

will appear in the grid area of the channel it belongs to. Select the filter and navigate to
the “Filter settings” tab in the details area. Here you will be able to specify the settings for
the filter.

• Mode

Specify whether a specific ID or a range of IDs should be used for the filter.

Changesanderrorsexcepted.

566

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

• CAN/LIN ID (For CAN and LIN channels only)

Allows you to define the specific/starting ID of your filter.

• Frame ID (For FlexRay channels only)

Allows you to define the specific/starting ID of your filter.

• Stopping ID

If using a range of IDs, this field allows you to define the stopping ID.

• Cycle repetition (For FlexRay channels only)

Allows you to define cycle repetition of the frame.

• Base cycle (For FlexRay channels only)

Allows you to define Base cycle of the frame.

All numbers in this tab can be entered in binary, decimal or hexadeci-
mal format. Furthermore can the ID mode for the CAN ID switched from
standard (0-7FF) to extended (0-1FFFFFFF).

Now the “ID Filter” has been specified and you will be able to define what the default
action for filters on the traced Bus channel should be. To do so, select the respective Bus
trace channel in the tree and navigate to the “Settings” tab in the details area. Here you
will be able to choose between to default actions for filters on this channel.

• Block all, except specified ID or ID range will block out and ignore all incoming traffic

on the channel except the specified ID/ID range.

• Pass all, except specified ID or ID range will store all incoming traffic on this channel

except the spdecified ID/ID range, which will be blocked and ignored.

It is possible to add and specify multiple ID Filters for one Bus trace chan-
nel.

Changesanderrorsexcepted.

567

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

15.10.6 Details area for bus tracing (Ring buffer)

The details area contains settings for the behaviour of your bus tracing file (Vector BLF /
Vector ASCII / Vector ASCII compressed) for Ring buffer, which will be explained here.

All subsequent settings (e.g. “Trigger trace”, “Bus trace” or traceable channels) are identi-
cal to regular bus tracing settings. Please refer to the chapter “Details area for bus tracing”
(→15.10.4).

15.10.6.1 Bus tracing file

General
This tab provides general settings for the selected bus tracing file.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

Changesanderrorsexcepted.

568

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

File
This tab provides settings regarding the creation of the file.

• File type

Tells you the type of the created file.

• File create event

Define, when the bus tracing file should be created. There are four possibilities:

File create event
On dataset begin
On recording start

On trigger

first
On
dataset)

trigger

(per

first
On
recording

trigger per

Characteristics
The file will be created once at logger start.
The file will be created everytime, recording via the
dataset is started or restarted after a pause. Starting
the recording may happen at the beginning of the
dataset (mode: Continuous acqusisition) or via a trig-
ger (modes: Start and pause trigger; Stop is inverted
start). This may result in a splitting of the current dataset
file into multiple files, as a new file is created for each
time the dataset ist started.
The file will be created on a trigger and record for a
user defined duration. These settings can be defined
in the Bus trace settings (→ 15.10.4.3). This will result in
a splitting of the current ATFX file into multiple files, as a
new file is created for each timethe trigger is set.
The file will be created once, when the defined trigger
is set for the first time since the beginning of the dataset
and record for a user defined duration. These settings
can be defined in the Bus trace settings (→ 15.10.4.3).
Each following time the trigger is set, the data will be
written in the same previously created file. Therefore
there will only be one file.
The file will be created once, when the defined trig-
ger is set for the first time during a recording and save
data for a user defined duration. These settings can be
defined in the Bus trace settings (→ 15.10.4.3). Each fol-
lowing time the trigger is set during the same period of
recording, the data will be written in the same previ-
ously created file. Therefore there will only be one file
per recording.

Changesanderrorsexcepted.

569

15.10 VECTORBLF/VECTORASCII/VECTORASCIICOMPRESSED

• Maximum file size

Define the maximum file size. It is recommended not to raise the maximum file size
above 2GB, as some third party evaluation tools cannot handle files, that are larger.

• Maximum file storage

Define the maximum file storage space. If the maximum file storage space has been
reached, older files will be deletet to make romm for newer files.

• File count

Tells you how many files can be hold with the current combination of “Maximum file
size” and “Maximum file storage”. You may also define here, how many files you wish
to be saved, and then the “Maximum file storage” will be filled in automatically.

• Protected snapshots

Define how many files before the trigger should be secured. The current and the
following file will be secured automatically.

• Snapshot trigger

It is possible to mark certain datafile via a trigger, in order for these files to be secured.
These files will not be deletet, when the “Maximum file storage” of the ring buffer is
reached.
This field allows you to select the trigger event, that will mark a datafile.

• Timestamp

This dropdown menu allows you to set the format of the timestamp for the file.

Changesanderrorsexcepted.

570

15.11 PCAP

15.11 PCAP

PCAP is a filetype for message orientated rawdate recordings on ethernet channels. The
trace method records all the messages that arrive on the ethernet channel. Regardless
of the signals defined, all the messages are recorded. Filter rules can be defined to
reduce the data volume. A typical trace application is the acquisition of all raw data in
order to later evaluate the total traffic on the channel. Unlike most of the other methods,
traces are event-oriented. This means the messages are not retrieved from the channels
according to a set time pattern, but are recorded as soon as they arrive on the channel.
This method accordingly has no parameter for sampling rate.

Including PCAP in your dataset will produce a “Warning” message, say-
ing that “at least one channel must be set active”.

Please refer to the section “ETH trace” (→ 15.11.3.2), in order to activate
a channel for tracing.

15.11.1 Tree elements for PCAP

Including PCAP in your dataset will add various new child elements to your tree element
“Dataset”:

• PCAP

This element represents the PCAP file, which will later be included in your exported
dataset. You may add multiple files of the same filetype.

• ETH trace

This element represents the “ETH trace” for recording all the traffic on a selected
ethernet channel.

Changesanderrorsexcepted.

571

15.11 PCAP

• ETH channels available for tracing

As child elements to the tree element “ETH trace” will appear all the ETH channels
which are currently available for tracing.

15.11.2 Grid area for PCAP

If the “ETH trace” is selected in the Measurement task tree, the grid area will show an
overview of the ethernet channels available for tracing.
At least one channel must be marked active for tracing, by ticking the checkbox labeled
“Trace channel”.

15.11.3 Details area for PCAP

The details area contains settings for the behaviour of your PCAP file or “ETH trace”.

15.11.3.1 PCAP file

General
This tab provides general settings for the selected Eth tracing file.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

Changesanderrorsexcepted.

572

15.11 PCAP

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

File
This tab provides settings regarding the creation of the file.

• File type

Tells you the type of the created file.

• File create event

Define, when the PCAP file should be created. There are four possibilities:

Changesanderrorsexcepted.

573

15.11 PCAP

File create event
On dataset begin
On recording start

On trigger

On
first
dataset)

trigger

(per

On
first
recording

trigger per

Characteristics
The file will be created once at logger start.
The file will be created everytime, recording via the
dataset is started or restarted after a pause. Starting
the recording may happen at the beginning of the
dataset (mode: Continuous acqusisition) or via a trig-
ger (modes: Start and pause trigger; Stop is inverted
start). This may result in a splitting of the current dataset
file into multiple files, as a new file is created for each
time the dataset ist started.
The file will be created on a trigger and record for a
user defined duration. These settings can be defined
in the timelog settings (→ 15.11.3.2). This will result in a
splitting of the current ATFX file into multiple files, as a
new file is created for each timethe trigger is set.
The file will be created once, when the defined trigger
is set for the first time since the beginning of the dataset
and record for a user defined duration. These settings
can be defined in the timelog settings (→ 15.11.3.2).
Each following time the trigger is set, the data will be
written in the same previously created file. Therefore
there will only be one file.
The file will be created once, when the defined trig-
ger is set for the first time during a recording and save
data for a user defined duration. These settings can be
defined in the timelog settings (→ 15.11.3.2). Each fol-
lowing time the trigger is set during the same period of
recording, the data will be written in the same previ-
ously created file. Therefore there will only be one file
per recording.

• Maximum file size

Define the maximum file size. It is recommended not to raise the maximum file size
above 2GB, as some third party analysis tools cannot handle files, that are larger.

• Create new file

If this box is marked active, a new file will be created, if the current file exceeds the
maximum file size.

• Timestamp

This dropdown menu allows you to set the format of the timestamp for the file.

• Discard empty file

If this option is activated and the datafile is empty it will be discarded and not trans-
ferred.

Changesanderrorsexcepted.

574

15.11 PCAP

Trigger
This tab allows you to define a span trigger for this dataset file. A span trigger will, upon
activation, cause the closure of the current and creation of a new PCAP file within the
existing dataset file.

To define a span trigger, click the “Select” button and choose anyone of the previously
configured triggers of your configuration. If no trigger suits the purpose, you will first need
to create one as described in the section “Triggers” (→10):

Changesanderrorsexcepted.

575

15.11 PCAP

15.11.3.2 Eth trace

General
This tab provides general settings for the selected “ETH trace”.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Trigger
This tab provides settings regarding the trigger for the start and stop of the “ETH trace”.
When the “ETH trace” is started, all traffic on the channel will be stored to the PCAP file.
Furthermore will this trigger provoke the creation of the PCAP file, if you have choosen
either “On trigger” or “On first trigger” as “File create event”.

Changesanderrorsexcepted.

576

15.11 PCAP

• Mode

Define whether you wish to continuously store data or if you want to start/stop data
storage via a trigger. There are two modes to control data storage via trigger:

Start and stop trigger allows you to set any previously defined trigger as start and/or
stop condition.

Stop is inverted start will store data as long as the start trigger condition is met. Once
it is no longer met and a possibly set Post-trigger duration has run out, data storage
will stop.

• Start-trigger

Define a trigger, that will start the “ETH trace”.

• Stop-trigger

Define a trigger, that will stop the “ETH trace”.

• Pre-trigger duration

Pre-trigger duration allows you to define, how long before the start trigger was set,
the “ETH trace” will start.

• Post-trigger duration

Post-trigger duration allows you to define, how long after the start trigger was set, the
“ETH trace” will stop.

Changesanderrorsexcepted.

577

15.11 PCAP

Extended
This tab provides extended settings for “ETH trace”.

• Include internal events

Define whether the occurrance of internal events should be stored in the trace data.

• Include all trigger events

Define whether all trigger events should be stored in the trace data.

• Alias

The field “Alias” allows you to give an alias to the method. The alias has to be unique
within the configuration.

An alias functions as a parameter that can later be referenced in includes/partial
configurations.

User
The field ￿Identifier￿ allows you to give a user identifier to the Bus trace. It does not have
any effect other than helping the user identifiy a specific Bus trace.

Changesanderrorsexcepted.

578

15.11 PCAP

15.11.4 Details area for PCAP (Ring buffer)

The details area contains settings for the behaviour of your PCAP file, the “ETH trace” com-
ponent or a traceable Bus channel.

15.11.4.1 PCAP file

General
This tab provides general settings for the selected PCAP file.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

Changesanderrorsexcepted.

579

15.11 PCAP

File
This tab provides settings regarding the creation of the file.

• File type

Tells you the type of the created file.

• File create event

Define, when the PCAP file should be created. There are four possibilities:

Changesanderrorsexcepted.

580

15.11 PCAP

File create event
On dataset begin
On recording start

On trigger

On
first
dataset)

trigger

(per

On
first
recording

trigger per

Characteristics
The file will be created once at logger start.
The file will be created everytime, recording via the
dataset is started or restarted after a pause. Starting
the recording may happen at the beginning of the
dataset (mode: Continuous acqusisition) or via a trig-
ger (modes: Start and pause trigger; Stop is inverted
start). This may result in a splitting of the current dataset
file into multiple files, as a new file is created for each
time the dataset ist started.
The file will be created on a trigger and record for a
user defined duration. These settings can be defined
in the ETH trace settings (→ 15.11.4.2). This will result in
a splitting of the current ATFX file into multiple files, as a
new file is created for each timethe trigger is set.
The file will be created once, when the defined trigger
is set for the first time since the beginning of the dataset
and record for a user defined duration. These settings
can be defined in the ETH trace settings (→ 15.11.4.2).
Each following time the trigger is set, the data will be
written in the same previously created file. Therefore
there will only be one file.
The file will be created once, when the defined trig-
ger is set for the first time during a recording and save
data for a user defined duration. These settings can be
defined in the ETH trace settings (→ 15.11.4.2). Each fol-
lowing time the trigger is set during the same period of
recording, the data will be written in the same previ-
ously created file. Therefore there will only be one file
per recording.

• Maximum file size

Define the maximum file size. It is recommended not to raise the maximum file size
above 2GB, as some third party evaluation tools cannot handle files, that are larger.

• Maximum file storage

Define the maximum file storage space. If the maximum file storage space has been
reached, older files will be deletet to make romm for newer files.

• File count

Tells you how many files can be hold with the current combination of “Maximum file
size” and “Maximum file storage”. You may also define here, how many files you wish
to be saved, and then the “Maximum file storage” will be filled in automatically.

• Protected snapshots

Define how many files before the trigger should be secured. The current and the
following file will be secured automatically.

• Snapshot trigger

Changesanderrorsexcepted.

581

15.11 PCAP

It is possible to mark certain datafile via a trigger, in order for these files to be secured.
These files will not be deletet, when the “Maximum file storage” of the ring buffer is
reached.
This field allows you to select the trigger event, that will mark a datafile.

15.11.4.2 ETH trace

General
This tab provides general settings for the selected “ETH trace”.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Trigger
This tab provides settings regarding the trigger for the start and stop of the “ETH trace”.
When the “ETH trace” is started, all traffic on the channel will be stored to the PCAP file.
Furthermore will this trigger provoke the creation of the PCAP file, if you have choosen
either “On trigger” or “On first trigger” as “File create event”.

• Mode

Define whether you wish to continuously store data or if you want to start/stop data
storage via a trigger. There are two modes to control data storage via trigger:

Changesanderrorsexcepted.

582

15.11 PCAP

Start and stop trigger allows you to set any previously defined trigger as start and/or
stop condition.

Stop is inverted start will store data as long as the start trigger condition is met. Once
it is no longer met and a possibly set Post-trigger duration has run out, data storage
will stop.

• Start-trigger

Define a trigger, that will start the “ETH trace”.

• Stop-trigger

Define a trigger, that will stop the “ETH trace”.

• Pre-trigger duration

Pre-trigger duration allows you to define, how long before the start trigger was set,
the “ETH trace” will start.

• Post-trigger duration

Post-trigger duration allows you to define, how long after the start trigger was set, the
“ETH trace” will stop.

• Master

Allows you to apply the trigger settings from another datafile of the current dataset.

15.11.4.3 Traceable ETH channel

Settings

Trace channel
Mark this box active in order to trace this channel.

Changesanderrorsexcepted.

583

15.12 AVI

15.12 AVI

The “AVI” filetype is meant for recording of video streams. For each AVI file, that you add
to your dataset you can only record one video stream.

15.12.1 Including a video signal in the Video Stream

In order to store a “Video Stream”, you will need to include a video signal in your “Video
Stream”.
To do so, select the tree element “Video Stream”, click the “Compontents” button in the
Ribbon and choose “Video Signal”.

Changesanderrorsexcepted.

584

15.12 AVI

In the resulting window you will be presented with an overview of all the available video
signals. You can chooe one signal and confirm by clicking “OK”.

15.12.2 Tree elements for AVI

Including the “AVI” filetype in your dataset will add three new child elements to your tree
element “Dataset”:

• AVI xx

This element represents the AVI file, which will
dataset. You may add multiple files of the same filetype.

later be included in your exported

• Video

Represents the video element in your AVI file. It tells you, that the type of signal, which
can be stored, is a video signal.

• Video Stream

This element represents the video signal which will be stored.

Changesanderrorsexcepted.

585

15.12 AVI

15.12.3 Grid area for AVI

If the “Video Stream” is selected in the Measurement task tree, and a video signal has
already been included in the “Video Stream”, the grid area will show the video signal
which has been included in the “Video Stream”.

15.12.4 Details area for AVI

The details area contains settings for the behaviour of your AVI file, Video element or Video
Stream.

15.12.4.1 AVI File

General
This tab provides general settings for the selected AVI file.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Changesanderrorsexcepted.

586

15.12 AVI

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

File
This tab provides settings regarding the creation of the file.

• File type

Tells you the type of the created file.

• File create event

Define, when the AVI file should be created. There are four possibilities:

Changesanderrorsexcepted.

587

15.12 AVI

File create event
On dataset begin
On recording start

On trigger

On
first
dataset)

trigger

(per

On
first
recording

trigger per

Characteristics
The file will be created once at logger start.
The file will be created everytime, recording via the
dataset is started or restarted after a pause. Starting
the recording may happen at the beginning of the
dataset (mode: Continuous acqusisition) or via a trig-
ger (modes: Start and pause trigger; Stop is inverted
start). This may result in a splitting of the current dataset
file into multiple files, as a new file is created for each
time the dataset ist started.
The file will be created on a trigger and record for a
user defined duration. These settings can be defined
in the timelog settings (→ 15.12.4.2). This will result in a
splitting of the current ATFX file into multiple files, as a
new file is created for each timethe trigger is set.
The file will be created once, when the defined trigger
is set for the first time since the beginning of the dataset
and record for a user defined duration. These settings
can be defined in the timelog settings (→ 15.12.4.2).
Each following time the trigger is set, the data will be
written in the same previously created file. Therefore
there will only be one file.
The file will be created once, when the defined trig-
ger is set for the first time during a recording and save
data for a user defined duration. These settings can be
defined in the timelog settings (→ 15.12.4.2). Each fol-
lowing time the trigger is set during the same period of
recording, the data will be written in the same previ-
ously created file. Therefore there will only be one file
per recording.

• Maximum file size

Define the maximum file size.
It is recommended not to raise the maximum file
size above 2GB, as some third party evaluation tools cannot handle files, that are
larger.

• Create new file

If this box is marked active, a new file will be created, if the current file exceeds the
maximum file size.

• Discard empty file

If this option is activated and the datafile is empty it will be discarded and not trans-
ferred.

Changesanderrorsexcepted.

588

15.12 AVI

Trigger
This tab allows you to define a span trigger for this dataset file. A span trigger will, upon
activation, cause the closure of the current and creation of a new AVI file within the
existing dataset file.

To define a span trigger, click the “Select” button and choose anyone of the previously
configured triggers of your configuration. If no trigger suits the purpose, you will first need
to create one as described in the section “Triggers” (→10):

Changesanderrorsexcepted.

589

15.12 AVI

15.12.4.2 Video

General
This tab provides general settings for the selected Video element.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Changesanderrorsexcepted.

590

15.12 AVI

Trigger
This tab provides settings regarding the trigger for the start and stop of the Video element.
When the Video element is started, the “Video Stream” will be stored to the AVI file.
Furthermore will this trigger provoke the creation of the AVI file, if you have choosen either
“On trigger” or “On first trigger” as “File create event”.

• Mode

Define whether you wish to continuously store data or if you want to start/stop data
storage via a trigger. There are two modes to control data storage via trigger:

Start and stop trigger allows you to set any previously defined trigger as start and/or
stop condition.

Stop is inverted start will store data as long as the start trigger condition is met. Once
it is no longer met and a possibly set Post-trigger duration has run out, data storage
will stop.

• Start-trigger

Define a trigger, that will start the Video element.

• Stop-trigger

Define a trigger, that will stop the Video element.

• Pre-trigger duration

Pre-trigger duration allows you to define, how long before the start trigger was set,
the Video element will start.

• Post-trigger duration

Post-trigger duration allows you to define, how long after the start trigger was set, the
Video element will stop.

Changesanderrorsexcepted.

591

15.12 AVI

Extended
The field “Alias” allows you to give an alias to the method. The alias has to be unique
within the configuration.

An alias functions as a parameter that can later be referenced in includes/partial config-
urations.

User
The field “Identifier” allows you to give a user identifier to the timelog. It does not have any
effect other than helping the user identifiy a specific timelog.

15.12.4.3 Video Stream

General
This tab provides general settings for the selected “Video Stream”.

Changesanderrorsexcepted.

592

15.12 AVI

• Active

Allows you to activate or deactivate the “Video Stream”.

• Name

Give a user-defined Name to the selected “Video Stream”.

• Description

Give a user-defined description to the selected “Video Stream”.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Settings
This tab allows you to set the frame rate of the video stream. Valid values range from
0.001...1000 fps.

15.12.5 Details area for AVI (Ring buffer)

The details area contains settings for the behaviour of your AVI file, Video element or Video
Stream.

15.12.5.1 AVI File

General
This tab provides general settings for the selected AVI file.

• Active

Allows you to activate or deactivate the selected file.

Changesanderrorsexcepted.

593

15.12 AVI

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

Changesanderrorsexcepted.

594

15.12 AVI

File
This tab provides settings regarding the creation of the file.

• File type

Tells you the type of the created file.

• File create event

Define, when the AVI file should be created. There are four possibilities:

File create event
On dataset begin
On recording start

On trigger

first
On
dataset)

trigger

(per

first
On
recording

trigger per

Characteristics
The file will be created once at logger start.
The file will be created everytime, recording via the
dataset is started or restarted after a pause. Starting
the recording may happen at the beginning of the
dataset (mode: Continuous acqusisition) or via a trig-
ger (modes: Start and pause trigger; Stop is inverted
start). This may result in a splitting of the current dataset
file into multiple files, as a new file is created for each
time the dataset ist started.
The file will be created on a trigger and record for a
user defined duration. These settings can be defined
in the Video settings (→ 15.12.5.2). This will result in a
splitting of the current ATFX file into multiple files, as a
new file is created for each timethe trigger is set.
The file will be created once, when the defined trigger
is set for the first time since the beginning of the dataset
and record for a user defined duration.
These set-
tings can be defined in the Video settings (→ 15.12.5.2).
Each following time the trigger is set, the data will be
written in the same previously created file. Therefore
there will only be one file.
The file will be created once, when the defined trig-
ger is set for the first time during a recording and save
data for a user defined duration. These settings can
be defined in the Video settings (→ 15.12.5.2). Each
following time the trigger is set during the same period
of recording, the data will be written in the same pre-
viously created file. Therefore there will only be one file
per recording.

Changesanderrorsexcepted.

595

15.12 AVI

• Maximum file size

Define the maximum file size. It is recommended not to raise the maximum file size
above 2GB, as some third party evaluation tools cannot handle files, that are larger.

• Maximum file storage

Define the maximum file storage space. If the maximum file storage space has been
reached, older files will be deletet to make romm for newer files.

• File count

Tells you how many files can be hold with the current combination of “Maximum file
size” and “Maximum file storage”. You may also define here, how many files you wish
to be saved, and then the “Maximum file storage” will be filled in automatically.

• Protected snapshots

Define how many files before the trigger should be secured. The current and the
following file will be secured automatically.

• Snapshot trigger

It is possible to mark certain datafile via a trigger, in order for these files to be secured.
These files will not be deletet, when the “Maximum file storage” of the ring buffer is
reached.
This field allows you to select the trigger event, that will mark a datafile.

15.12.5.2 Video

General
This tab provides general settings for the selected Video element.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

Changesanderrorsexcepted.

596

15.12 AVI

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Trigger
This tab provides settings regarding the trigger for the start and stop of the Video element.
When the Video element is started, the “Video Stream” will be stored to the AVI file.
Furthermore will this trigger provoke the creation of the AVI file, if you have choosen either
“On trigger” or “On first trigger” as “File create event”.

• Mode

Define whether you wish to continuously store data or if you want to start/stop data
storage via a trigger. There are two modes to control data storage via trigger:

Start and stop trigger allows you to set any previously defined trigger as start and/or
stop condition.

Stop is inverted start will store data as long as the start trigger condition is met. Once
it is no longer met and a possibly set Post-trigger duration has run out, data storage
will stop.

• Start-trigger

Define a trigger, that will start the Video element.

• Stop-trigger

Define a trigger, that will stop the Video element.

• Pre-trigger duration

Pre-trigger duration allows you to define, how long before the start trigger was set,
the Video element will start.

• Post-trigger duration

Post-trigger duration allows you to define, how long after the start trigger was set, the
Video element will stop.

Changesanderrorsexcepted.

597

15.12 AVI

User
The field “Identifier” allows you to give a user identifier to the timelog. It does not have any
effect other than helping the user identifiy a specific timelog.

15.12.5.3 Video Stream

General
This tab provides general settings for the selected “Video Stream”.

• Active

Allows you to activate or deactivate the “Video Stream”.

• Name

Give a user-defined Name to the selected “Video Stream”.

• Description

Give a user-defined description to the selected “Video Stream”.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Changesanderrorsexcepted.

598

15.13 WAV

15.13 WAV

The “WAV” filetype is meant for recording of audio streams. For each WAV file, that you
add to your dataset you can only record one audio stream.

15.13.1 Including an audio signal in the audio Stream

In order to store an “Audio Stream”, you will need to include a audio signal in your “Audio
Stream”.
To do so, select the tree element “Audio Stream”, click the “Compontents” button in the
Ribbon and choose “Audio Signal”.

Changesanderrorsexcepted.

599

15.13 WAV

In the resulting window you will be presented with an overview of all the available audio
signals. You can chooe one signal and confirm by clicking “OK”.

15.13.2 Tree elements for WAV

Including the “WAV” filetype in your dataset will add three new child elements to your tree
element “Dataset”:

• WAV xx

This element represents the WAV file, which will later be included in your exported
dataset. You may add multiple files of the same filetype.

• Audio

Represents the audio element in your WAV file.
which can be stored, is an audio signal.

It tells you, that the type of signal,

• Audio Stream

This element represents the audio signal which will be stored.

Changesanderrorsexcepted.

600

15.13 WAV

15.13.3 Grid area for WAV

If the “audio Stream” is selected in the Measurement task tree, and a audio signal has
already been included in the “audio Stream”, the grid area will show the audio signal
which has been included in the “audio Stream”.

15.13.4 Details area for WAV

The details area contains settings for the behaviour of your WAV file, the audio recording
or audio stream.

15.13.4.1 Wav selected

General
This tab provides general settings for the selected WAV file.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

Changesanderrorsexcepted.

601

15.13 WAV

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

File
This tab tells you the filetype of your file.

15.13.4.2 Audio xx selected

General
This tab provides general settings for the Audio xx element.

• Active

Allows you to activate or deactivate “GPS Tracking”.

Changesanderrorsexcepted.

602

15.13 WAV

• Name

Give a user-defined Name to your “GPS Tracking”.

• Description

Give a user-defined description to your “GPS Tracking”.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Trigger
This tab provides settings regarding the trigger for the start and stop of the audio recording.

• Mode

Define whether you wish to continuously store data or if you want to start/stop data
storage via a trigger. There are two modes to control data storage via trigger:

Start and stop trigger allows you to set any previously defined trigger as start and/or
stop condition.

Stop is inverted start will store data as long as the start trigger condition is met. Once
it is no longer met and a possibly set Post-trigger duration has run out, data storage
will stop.

• Start-trigger

Define a trigger, that will start “GPS Tracking”.

• Stop-trigger

Define a trigger, that will stop “GPS Tracking”.

Changesanderrorsexcepted.

603

15.13 WAV

Extended
The field “Alias” allows you to give an alias to the method. The alias has to be unique
within the configuration.

An alias functions as a parameter that can later be referenced in includes/partial config-
urations.

Changesanderrorsexcepted.

604

15.14 GPX

15.14 GPX

The “GPX” filetype is meant for GPS Tracking.

15.14.1 Assigning GPS signals

Other than for other filetypes, when working with GPX, you will not be able to choose the
signals you wish to store from a list of available signals, but you will need to assign a GPS
task (latitude, longitude or altitude) to a signal. That means, that technically any signal
can be used as GPS signal.

For instructions on assignig GPS tasks please refer to (→ 8.18.2.1).

One GPS task may only be assigned to one signal. Use the “Check”
button in the Ribbon to verify, that GPS tasks are uniquely assigned.
If
a GPS task is multiply assigned, navigate to the “Format” tab of the
wrongly assigned signal and deassign the GPS task.

Exporting a configuration will also check your system for validity and in-
form you, if you have multiply assigned GPS tasks.

15.14.2 Tree elements for GPX

Including the “GPX” filetype in your dataset will add two new child elements to your tree
element “Dataset”:

• GPX

This element represents the GPX file, which will later be included in your exported
dataset.

• GPS Tracking

Represents the GPS signals you are tracking

Changesanderrorsexcepted.

605

15.14 GPX

15.14.3 Grid area for GPX

The grid area is not used for configuration of GPX. Instead signal selection in this case works
via assignation of GPS tasks. Please refer to (→ 8.18.2.1).

15.14.4 Details area for GPX

The details area contains settings for the behaviour of your GPX file and “GPS Tracking”.

15.14.4.1 GPX File

General
This tab provides general settings for the selected GPX file.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

Changesanderrorsexcepted.

606

15.14 GPX

File
This tab tells you the filetype of your file.

15.14.4.2 GPS Tracking

General
This tab provides general settings for GPS Tracking.

• Active

Allows you to activate or deactivate “GPS Tracking”.

• Name

Give a user-defined Name to your “GPS Tracking”.

• Description

Give a user-defined description to your “GPS Tracking”.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Changesanderrorsexcepted.

607

15.14 GPX

Trigger
This tab provides settings regarding the trigger for the start and stop of the “GPS Tracking”.
When the “GPS Tracking” is started, all activated signals with GPS task will be stored to the
GPX file.

• Mode

Define whether you wish to continuously store data or if you want to start/stop data
storage via a trigger. There are two modes to control data storage via trigger:

Start and stop trigger allows you to set any previously defined trigger as start and/or
stop condition.

Stop is inverted start will store data as long as the start trigger condition is met. Once
it is no longer met and a possibly set Post-trigger duration has run out, data storage
will stop.

• Start-trigger

Define a trigger, that will start “GPS Tracking”.

• Stop-trigger

Define a trigger, that will stop “GPS Tracking”.

• Pre-trigger duration

Pre-trigger duration allows you to define, how long before the start trigger was set,
“GPS Tracking” will start.

• Post-trigger duration

Post-trigger duration allows you to define, how long after the start trigger was set,
“GPS Tracking” will stop.

Changesanderrorsexcepted.

608

15.14 GPX

Extended
The field “Alias” allows you to give an alias to the method. The alias has to be unique
within the configuration.

An alias functions as a parameter that can later be referenced in includes/partial config-
urations.

Storage
This tab allows you to set the storage rate for “GPS Tracking”

Storage rates with decimal places will be rounded to three decimal
places.

Changesanderrorsexcepted.

609

15.15 CAETECBINARY(CLASSINGS/MIN/MAXVALUES)

15.15 CAETEC binary (Classings / Min/Max Values)

The “CAETEC binary” filetype allows for classing of signals. Classings are processes for
counting values or sequences (such as cycles) of signals. The standard procedure is to
take the range in which the counted events are expected and divide this into so-called
classes. Any values lying above the highest or below the lowest class are generally ig-
nored (no open-border classes). Please refer to the chapter “Classing methods”(→15.17).

The methods fundamentally differ in their counting strategies (for example, when levels
are crossed, when a class is reached, cycle amplitudes and so on), and they are
standardized. Which particular standard was applied in the design of each method is
explained in the chapters on the different classing methods.

A signal can be used in several classing processes simultaneously.

Some methods can be applied with different numbers of signals. This is what is referred
to as the dimension of the particular classing. 1D, 2D, 3D specify how many signals are
joined in a class (joint classing). When joined, the classes of the signals form a matrix.
Counting is always performed in the matrix element in which the counting conditions for
all the involved signals are met by the same sampling instance.

15.15.1 Tree elements for CAETEC binary

Including a “CAETEC binary” file in your dataset will add one new child element called
“CAETEC binary xx” to your tree element “Dataset”.
Multiple “CAETEC binary” files can be added to your dataset. They will be labeled equally
and the counter will be raised by one for each new file. This may be necessary, if multiple
classings should be included in the dataset, as each “CAETEC binary” file can only contain
one classing.

Changesanderrorsexcepted.

610

15.15 CAETECBINARY(CLASSINGS/MIN/MAXVALUES)

15.15.2 Details area for CAETEC binary

The details area contains settings regarding the “CAETEC binary” file.
General
This tab provides general settings for the selected CAETEC binary file.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected formula/signal.

• Description

Give a user-defined description to the selected formula/signal.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

File
This tab provides settings regarding the creation of the file.

• File type

Tells you the type of the created file.

• Hold last value

Specify, for how long the last value of the signal will be hold.

Changesanderrorsexcepted.

611

15.15 CAETECBINARY(CLASSINGS/MIN/MAXVALUES)

15.15.3 Adding a classing

In order to add a classing, select the “CAETEC binary” or “CAETEC ASCII” file, which
should contain the classing, in the measurement task tree.

Then click the “Components” button in the Ribbon and choose the desired classing
method.

Changesanderrorsexcepted.

612

15.15 CAETECBINARY(CLASSINGS/MIN/MAXVALUES)

Once you have added a classing, you may now proceed to configure this classing. Please
refer to the chapter “Classing methods”(→15.17) for instructions.

15.15.4 Min/Max Values

The “Min/Max Values” function of the CAETEC binary method allows you to store the min-
imum and maximum incoming values of signals.

15.15.4.1 Adding Min/Max Values and selecting signals

In order to store the min/max values of a signal, you will first need to add a “Min/Max
Values” group to your CAETEC binary file. To do so, select the CAETEC binary file in the
measurement task tree, click the “Components” button in the Ribbon and then select
“Min/Max Values”.

Changesanderrorsexcepted.

613

15.15 CAETECBINARY(CLASSINGS/MIN/MAXVALUES)

Once the “Min/Max Values” group has been added, the signals whose min/max values
should be stored may be selected. To do so, select the tree element “Min/Max Values
xx”, click the “Components” button in the Ribbon and choose “Signal”.

The following window lets you choose one or multiple signals whose min/max values may
be stored.
Select the desired signals and confirm with “OK”. The selected signals will appear in the
grid area.

Changesanderrorsexcepted.

614

15.15 CAETECBINARY(CLASSINGS/MIN/MAXVALUES)

15.15.4.2 Tree elements for Min/Max Values

The “Min/Max Values” group will appear as a new child element of the CAETEC binary
method labeled “Min/Max Values xx”.

15.15.4.3 Grid area for Min/Max Values

The grid area shows an overview of all signals that have been selected for storing their
min/max values in this group. The grid area also shows related information such as unit
and sampling rate of the signal.

Changesanderrorsexcepted.

615

15.15 CAETECBINARY(CLASSINGS/MIN/MAXVALUES)

15.15.4.4 Details area for Min/Max Values

The details area shows settings regarding this “Min/Max Values” group.

General
This tab provides general settings for the selected “Min/Max Values xx” tree element.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Changesanderrorsexcepted.

616

15.15 CAETECBINARY(CLASSINGS/MIN/MAXVALUES)

Trigger
This tab provides settings regarding the trigger for the start and stop of the “Min/Max Val-
ues” storage. When the “Min/Max Values” storage is started, all traffic on the station will
be stored to the “Min/Max Values” file.
Furthermore will this trigger provoke the creation of the “Min/Max Values” file, if you have
choosen either “On trigger” or “On first trigger” as “File create event”.

• Mode

Define whether you wish to continuously store data or if you want to start/stop data
storage via a trigger. There are two modes to control data storage via trigger:

Start and stop trigger allows you to set any previously defined trigger as start and/or
stop condition.

Stop is inverted start will store data as long as the start trigger condition is met. Once
it is no longer met and a possibly set Post-trigger duration has run out, data storage
will stop.

• Start-trigger

Define a trigger, that will start the “Bus trace”.

• Stop-trigger

Define a trigger, that will stop the “Bus trace”.

• Pre-trigger duration

Pre-trigger duration allows you to define, how long before the start trigger was set,
the “Bus trace” will start.

• Post-trigger duration

Post-trigger duration allows you to define, how long after the start trigger was set, the
“Bus trace” will stop.

Changesanderrorsexcepted.

617

15.15 CAETECBINARY(CLASSINGS/MIN/MAXVALUES)

Extended
The field “Alias” allows you to give an alias to the method. The alias has to be unique
within the configuration.

An alias functions as a parameter that can later be referenced in includes/partial config-
urations.

Storage
The storage rate sets the rate at which the min/max values in this “Min/Max Values” group
will be stored.

The signals contained in one “Min/Max Values” may have different sam-
pling rates, but each “Min/Max Values” group may only have one stor-
age rate. It is therefore possible to add multiple “Min/Max Values” groups
per CAETEC binary file, so you can have different storage rates accord-
ing to the different sample rates of the signals, if necessary.

Changesanderrorsexcepted.

618

15.16 CAETECASCII(CLASSINGS/MIN/MAXVALUES)

15.16 CAETEC ASCII (Classings / Min/Max Values)

The “CAETEC ASCII” filetype allows for classing of signals. Classings are processes for
counting values or sequences (such as cycles) of signals. The standard procedure is to
take the range in which the counted events are expected and divide this into so-called
classes. Any values lying above the highest or below the lowest class are generally
ignored (no open-border classes).

The methods fundamentally differ in their counting strategies (for example, when levels
are crossed, when a class is reached, cycle amplitudes and so on), and they are
standardized. Which particular standard was applied in the design of each method is
explained in the chapters on the different classing methods. Please refer to the chapter
“Classing methods”(→15.17).

A signal can be used in several classing processes simultaneously.

Some methods can be applied with different numbers of signals. This is what is referred
to as the dimension of the particular classing. 1D, 2D, 3D specify how many signals are
joined in a class (joint classing). When joined, the classes of the signals form a matrix.
Counting is always performed in the matrix element in which the counting conditions for
all the involved signals are met by the same sampling instance.

15.16.1 Tree elements for CAETEC ASCII

Including a “CAETEC ASCII” file in your dataset will add one new child element called
“CAETEC ASCII xx” to your tree element “Dataset”.
Multiple “CAETEC ASCII” files can be added to your dataset. They will be labeled equally
and the counter will be raised by one for each new file. This may be necessary, if multiple
classings should be included in the dataset, as each “CAETEC ASCII” file can only contain
one classing.

Changesanderrorsexcepted.

619

15.16 CAETECASCII(CLASSINGS/MIN/MAXVALUES)

15.16.2 Details area for CAETEC ASCII

The details area contains settings regarding the “CAETEC ASCII” file.
General
This tab provides general settings for the selected CAETEC ASCII file.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected formula/signal.

• Description

Give a user-defined description to the selected formula/signal.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

File
This tab provides settings regarding the creation of the file.

• File type

Tells you the type of the created file.

• Hold last value

Specify, for how long the last value of the signal will be hold.

Changesanderrorsexcepted.

620

15.16 CAETECASCII(CLASSINGS/MIN/MAXVALUES)

15.16.3 Adding a classing

In order to add a classing, select the “CAETEC binary” or “CAETEC ASCII” file, which
should contain the classing, in the measurement task tree.

Then click the “Components” button in the Ribbon and choose the desired classing
method.

Changesanderrorsexcepted.

621

15.16 CAETECASCII(CLASSINGS/MIN/MAXVALUES)

Once you have added a classing, you may now proceed to configure this classing. Please
refer to the chapter “Classing methods”(→15.17) for instructions.

15.16.4 Min/Max Values

The “Min/Max Values” function of the CAETEC ASCII method allows you to store the min-
imum and maximum incoming values of signals.
It is identical to the “Min/Max Values”
function of the CAETEC binary method and has been described in the chapter “CAETEC
binary (Min/Max Values). Please refer to (→15.15.4).

Changesanderrorsexcepted.

622

15.17 CLASSINGMETHODS

15.17 Classing methods

This chapter will only explain the different classing methods. A classing is always a part of
either a CAETEC binary or a CAETEC ASCII file for your dataset. So in order to work with
a classing, you will need to add one of these filetypes for each classing, that you wish to
define.
For
dataset”(→15.1.4) and “CAETEC binary(→15.15) or ”CAETEC ASCII(→15.16).

instructions on how to do this, please refer

to the chapters “Setting up a

Changesanderrorsexcepted.

623

15.18 SCRIPTLOG

15.18 Script log

The “Script log” filetype is meant for recording script logging messages. The “Script log”
will only contain information if it is explicitely defined as a target by a script. Otherwise it
will remain empty.

15.18.1 Including a Script log as a target in a script

To include a “Script log” as a target in a script, you will first need to create a script. For
details on scripts please refer to (→11).
Then you will need to navigate to the tab labeled “Script” in the details area of the script.

The script you can see in the figure above will write a timecounter saying “Now it is x
seconds after start” in the “Scriptfile”, where the value x starts at 0 and increases by 1
every second.
It is crucial here, that the target, to which to print the value, equals the name of the
“Script log” to which the information should be written.

The first variable in parenthesis following the “printf” command defines the target. In this
case the target is ’Timecount’.

Changesanderrorsexcepted.

624

15.18 SCRIPTLOG

Now the last step is to navigate to the “General” tab in the details area of our “Script log”
and name it exactly as the target in the script, so the script can find the target to which it
is supposed to write.

If the target in the script and the “Script log” name are not equal, at
syntax check in the script you will get a syntax error looking like this.

Changesanderrorsexcepted.

625

15.18 SCRIPTLOG

15.18.2 Tree elements for Script log

Including the “Script log” filetype in your dataset will add one new child element labeled
“Script log xx” to your tree element “Dataset”.

15.18.3 Details area for Script log

The details area contains settings for the behaviour of your Script log.

General
This tab provides general settings for the selected Script log.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Changesanderrorsexcepted.

626

15.18 SCRIPTLOG

File
This tab provides settings regarding the creation of the file.

• File type

Tells you the type of the created file.

• File create event

Define, when the Script log file should be created. There are two possibilities:

File create event
At beginning of dataset
At start of recording

Characteristics
The file will be created once at logger start.
The file will be created everytime, recording via the
dataset is started or restarted after a pause. Starting
the recording may happen at the beginning of the
dataset (mode: Continuous acqusisition) or via a trig-
ger (modes: Start and pause trigger; Stop is inverted
start). This may result in a splitting of the current dataset
file into multiple files, as a new file is created for each
time the dataset ist started.

• Maximum file size

Define the maximum file size. It is recommended not to raise the maximum file size
above 2GB, as some third party analysis tools cannot handle files, that are larger.

• Create new file

If this box is marked active, a new file will be created, if the current file exceeds the
maximum file size.

• Extension

Define the filename extension without a leading dot.

• Discard empty file

If this option is activated and the datafile is empty it will be discarded and not trans-
ferred.

Changesanderrorsexcepted.

627

15.18 SCRIPTLOG

Trigger
This tab allows you to define a span trigger for this dataset file. A span trigger will, upon
activation, cause the closure of the current and creation of a new Script log file within
the existing dataset file.

To define a span trigger, click the “Select” button and choose anyone of the previously
configured triggers of your configuration. If no trigger suits the purpose, you will first need
to create one as described in the section “Triggers” (→10):

Changesanderrorsexcepted.

628

15.19 J1939DM1LOG

15.19 J1939 DM1 Log

The J1939 DM1 Log method is a trace method like bus trace or PCAP. It traces all the
incoming traffic on a J1939 station. Unlike most of the other methods, traces are event-
oriented. This means the messages are not retrieved from the channels according to a
set time pattern, but are recorded as soon as they arrive on the channel. This method
accordingly has no parameter for sampling rate.

15.19.1 Tree elements for J1939 DM1 Log

Including a J1939 DM1 Log filetype in your dataset will add various new child elements to
your tree element “Dataset”:

• J1939 DM1 Log xx

This element represents the J1939 DM1 Log file, which will later be included in your
exported dataset. You may add multiple files of the same filetype.

• J1939-Stations

This element contains all the traceable stations.

• J1939-stations available for tracing

As child elements to the tree element “J1939-Stations” will appear all the J1939-
Stations which are currently available for tracing.

15.19.2 Grid area for J1939 DM1 Log

If the “J1939-Stations” element is selected in the measurement task tree, the grid area will
show an overview of the J1939 stations available for tracing.
At least one station must be marked active for tracing, by setting active the setting “Log
station”.

Changesanderrorsexcepted.

629

15.19 J1939DM1LOG

15.19.3 Details area for J1939 DM1 Log

The details area contains settings for the behaviour of your J1939 DM1 Log xx file, the
“J1939-Stations” component or a traceable station.

15.19.3.1 J1939 DM1 Log xx file

General
This tab provides general settings for the selected bus tracing file.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

Changesanderrorsexcepted.

630

15.19 J1939DM1LOG

File
This tab provides settings regarding the creation of the file.

• File type

Tells you the type of the created file.

• File create event

Define, when the bus tracing file should be created. There are four possibilities:

Changesanderrorsexcepted.

631

15.19 J1939DM1LOG

File create event
On dataset begin
On recording start

On trigger

On
first
dataset)

trigger

(per

On
first
recording

trigger per

Characteristics
The file will be created once at logger start.
The file will be created everytime, recording via the
dataset is started or restarted after a pause. Starting
the recording may happen at the beginning of the
dataset (mode: Continuous acqusisition) or via a trig-
ger (modes: Start and pause trigger; Stop is inverted
start). This may result in a splitting of the current dataset
file into multiple files, as a new file is created for each
time the dataset ist started.
The file will be created on a trigger and record for a
user defined duration. These settings can be defined
in the timelog settings (→ 15.10.4.3). This will result in a
splitting of the current ATFX file into multiple files, as a
new file is created for each timethe trigger is set.
The file will be created once, when the defined trigger
is set for the first time since the beginning of the dataset
and record for a user defined duration. These settings
can be defined in the timelog settings (→ 15.10.4.3).
Each following time the trigger is set, the data will be
written in the same previously created file. Therefore
there will only be one file.
The file will be created once, when the defined trig-
ger is set for the first time during a recording and save
data for a user defined duration. These settings can be
defined in the timelog settings (→ 15.10.4.3). Each fol-
lowing time the trigger is set during the same period of
recording, the data will be written in the same previ-
ously created file. Therefore there will only be one file
per recording.

• Maximum file size

Define the maximum file size.
It is recommended not to raise the maximum file
size above 2GB, as some third party evaluation tools cannot handle files, that are
larger.

• Create new file

If this box is marked active, a new file will be created, if the current file exceeds the
maximum file size.

• Discard empty file

If this option is activated and the datafile is empty it will be discarded and not trans-
ferred.

Changesanderrorsexcepted.

632

15.19 J1939DM1LOG

Trigger
This tab allows you to define a span trigger for this dataset file. A span trigger will, upon
activation, cause the closure of the current and creation of a new J1939 DM1 Log file
within the existing dataset file.

To define a span trigger, click the “Select” button and choose anyone of the previously
configured triggers of your configuration. If no trigger suits the purpose, you will first need
to create one as described in the section “Triggers” (→10):

15.19.3.2 J1939-Stations component

General
This tab provides general settings for the selected “J1939-Stations” component.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

Changesanderrorsexcepted.

633

15.19 J1939DM1LOG

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Changesanderrorsexcepted.

634

15.19 J1939DM1LOG

Trigger
This tab provides settings regarding the trigger for the start and stop of the “J1939 DM1
Log”. When the “J1939 DM1 Log” is started, all traffic on the station will be stored to the
“J1939 DM1 Log” file.
Furthermore will this trigger provoke the creation of the“J1939 DM1 Log” file, if you have
choosen either “On trigger” or “On first trigger” as “File create event”.

• Mode

Define whether you wish to continuously store data or if you want to start/stop data
storage via a trigger. There are two modes to control data storage via trigger:

Start and stop trigger allows you to set any previously defined trigger as start and/or
stop condition.

Stop is inverted start will store data as long as the start trigger condition is met. Once
it is no longer met and a possibly set Post-trigger duration has run out, data storage
will stop.

• Start-trigger

Define a trigger, that will start the “Bus trace”.

• Stop-trigger

Define a trigger, that will stop the “Bus trace”.

• Pre-trigger duration

Pre-trigger duration allows you to define, how long before the start trigger was set,
the “Bus trace” will start.

• Post-trigger duration

Post-trigger duration allows you to define, how long after the start trigger was set, the
“Bus trace” will stop.

Changesanderrorsexcepted.

635

15.19 J1939DM1LOG

Extended
The field “Alias” allows you to give an alias to the method. The alias has to be unique
within the configuration.

An alias functions as a parameter that can later be referenced in includes/partial config-
urations.

Settings
This tab provide settings concerning all traceable J1939 stations.

• Min. trouble duration

Define the time, that a DM1 message must be active before it is written to the J1939
DM1 Logfile

• Write timestamp

If active, additional timestamps will be written to the logfile.

Changesanderrorsexcepted.

636

15.19 J1939DM1LOG

15.19.3.3 Traceable J1939 station

Station
When active, the station, that has been selected will be logged. This is the same setting
as selecting a station for logging in the grid area as described above.

Changesanderrorsexcepted.

637

15.20 DLT

15.20 DLT

The DLT filetype allows for data storage of data provided by DLT-Stations. For instructions
on setting up a DLT-Station please refer to the chapter “DLT (Diagnostic, Log and Trace)
on ETH” (→8.10.6).

Including a bus tracing filetype in your datasete will produce a “Warn-
ing” message, saying that “No DLT station selected for logging”.

Please refer to the section “Grid area for DLT” (→ 15.20.2), in order to
activate a station for logging.

15.20.1 Tree elements for DLT

Including a DLT file in your dataset will add various new child elements to your tree element
“Dataset”:

• DLT 01

This element represents the DLT file, which will
dataset. You may add multiple files of the same filetype.

later be included in your exported

• DLT-Station

This element represents the “DLT” interface under which all existing DLT-Stations are
joined and which serves for controlling the overall storage behaviour for all DLT-
Stations that are connected to this DLT file and activated for logging.

• DLT-Station xx

This element represents the individual DLT-Stations that are currently set up in your
configuration. Each “DLT-Station xx”, that you set up will appear here individually, so
the number of tree elements depends on the number of your DLT-Stations.

Changesanderrorsexcepted.

638

15.20 DLT

15.20.2 Grid area for DLT

If the “DLT-Stations” element is selected in the Measurement task tree, the grid area will
show an overview of the DLT-Stations available for logging.
Here you may activate and deactivate individual DLT-Stations for logging. To do so, mark
active the “Log station” box. At least one station must be activated for logging.
The “Active” box is read only and only shows whether a DLT-Station itself is set to active or
not.

15.20.3 Details area for DLT

The details area contains settings for the behaviour of your DLT file, the “DLT-Stations” in-
terface or an individual “DLT-Station xx”.

15.20.3.1 DLT file

General
This tab provides general settings for the selected DLT file.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

Changesanderrorsexcepted.

639

15.20 DLT

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

In the field “Name” project parameters can be used as variables. For
more information please refer to (→5.6).

File
This tab provides settings regarding the creation of the file.

• File type

Tells you the type of the created file.

• File creation event

Define, when the bus tracing file should be created. There are four possibilities:

Changesanderrorsexcepted.

640

15.20 DLT

File create event
At beginning of dataset
At start of recording

At trigger

At
first
dataset)

trigger

(per

At first trigger per record-
ing

Characteristics
The file will be created once at logger start.
The file will be created everytime, recording via the
dataset is started or restarted after a pause. Starting
the recording may happen at the beginning of the
dataset (mode: Continuous acqusisition) or via a trig-
ger (modes: Start and pause trigger; Stop is inverted
start). This may result in a splitting of the current dataset
file into multiple files, as a new file is created for each
time the dataset ist started.
The file will be created on a trigger and record for a
user defined duration. These settings can be defined
in the timelog settings (→ 15.10.4.3). This will result in a
splitting of the current ATFX file into multiple files, as a
new file is created for each timethe trigger is set.
The file will be created once, when the defined trigger
is set for the first time since the beginning of the dataset
and record for a user defined duration. These settings
can be defined in the timelog settings (→ 15.10.4.3).
Each following time the trigger is set, the data will be
written in the same previously created file. Therefore
there will only be one file.
The file will be created once, when the defined trig-
ger is set for the first time during a recording and save
data for a user defined duration. These settings can be
defined in the timelog settings (→ 15.10.4.3). Each fol-
lowing time the trigger is set during the same period of
recording, the data will be written in the same previ-
ously created file. Therefore there will only be one file
per recording.

• Maximum file size

Define the maximum file size.
It is recommended not to raise the maximum file
size above 2GB, as some third party evaluation tools cannot handle files, that are
larger.

• Create new file

If this box is marked active, a new file will be created, if the current file exceeds the
maximum file size.

Changesanderrorsexcepted.

641

15.20 DLT

Trigger
This tab allows you to define a span trigger for this dataset file. A span trigger will, upon
activation, cause the closure of the current and creation of a new DLT file within the
existing dataset file.

To define a span trigger, click the “Select” button and choose anyone of the previously
configured triggers of your configuration. If no trigger suits the purpose, you will first need
to create one as described in the section “Triggers” (→10):

Changesanderrorsexcepted.

642

15.20 DLT

15.20.3.2 DLT-Stations

General
This tab provides general settings for the “DLT-Stations” interface.

• Active

Allows you to activate or deactivate the selected file.

• Name

Give a user-defined Name to the selected file.

• Description

Give a user-defined description to the selected file.

• Reference

This field serves as the tree element’s unique identifier inside the measurement task
tree. It cannot be changed.

Trigger
This tab provides settings regarding the trigger for starting/stopping the storage of the “DLT-
Stations” and all the adjacent “DLT-Stations xx” that have been activated for logging.
Furthermore will this trigger provoke the creation of the bus tracing file, if you have choosen
either “At trigger” or “At first trigger” as “File creation event”.

Changesanderrorsexcepted.

643

15.20 DLT

• Mode

Define whether you wish to continuously store data or if you want to start/stop data
storage via a trigger. There are two modes to control data storage via trigger:

Start and stop trigger allows you to set any previously defined trigger as start and/or
stop condition.

Stop is inverted start will store data as long as the start trigger condition is met. Once
it is no longer met and a possibly set Post-trigger duration has run out, data storage
will stop.

• Start-trigger

Define a trigger, that will start the “Bus trace”.

• Stop-trigger

Define a trigger, that will stop the “Bus trace”.

• Pre-trigger duration

Pre-trigger duration allows you to define, how long before the start trigger was set,
the “Bus trace” will start.

• Post-trigger duration

Post-trigger duration allows you to define, how long after the start trigger was set, the
“Bus trace” will stop.

Extended
The field “Alias” allows you to give an alias to the method. The alias has to be unique
within the configuration.

An alias functions as a parameter that can later be referenced in includes/partial config-
urations.

Changesanderrorsexcepted.

644

15.20 DLT

15.20.3.3 DLT-Station xx

In the “Station” tab for each individual “DLT-Station xx” you can activate this station for
logging. This is the same setting as the “Log station” setting in the grid area, which has
earlier been described here (→15.20.2). Station

Changesanderrorsexcepted.

645

16 DATATRANSFER

16 Datatransfer

Stored measurement data can later be transferred from the logger and thus made
available for further analysis and processing. To do so, it is necessary, to configure one or
more “Transfer events”, that wilt trigger the transfer, and the desired connection method
used for the transfer. The first chapter of this section will explain “Transfer events” and in
the following chapter will be explained configuration of the transfer connection method.

Furthermore the logger will check whenever a data transfer is happening, if a newer
version of the current logger-configuration (datalog.ccmc) and firmware are available.
Instructions on how to set define the correct path will be explained for each type of
transfer connection in the respective chapter.

16.1 Transfer events

In order for data transfer to take place, it must be triggered by an event. These events
can be system events, such as starting or shutting down the logger; trigger events, i.e.
reactions to defined triggers; or time events, such as the arrival of a particular point in
time. Multiple events can also be defined, even of the same type.

In the event that data transfer limits have been defined, these can, if the need arises, be
over-ridden by specific transfer events.

Changesanderrorsexcepted.

646

16.1 TRANSFEREVENTS

16.1.1 General Information about transfer events

Multiple targets for transfer events
Each transfer event can use multiple connections to different targets, in order to ensure
successfull data transfer. In order to do so, activate every connection you want to use for
this transfer event in the transfer events grid area. For instructions on transfer connections
please refer to (→16.3).

By setting the priority you define, which connection will be used first, starting with priority 1.
As soon as data transfer via one connection has been successfully completed, the other
connections will be skipped and the dataset will be erased from the logger.

Ignore transfer limits
In the grid area of every transfer event you can choose to “Ignore transfer limits” for ev-
ery transfer connection. This means, it will ignore any defined restrictions for that transfer
connection. These restrictions can be set in the “Basic” settings tab in the details area of
each transfer connection. Please refer to (→16.3) and then to the respective connection
type’s section.

Default data transfer connection

Changesanderrorsexcepted.

647

16.1 TRANSFEREVENTS

In the grid area of every transfer event you can choose choose the default data transfer
connection for data transfer. This means, the connection, that has been defined as de-
fault data transfer connection will be used. This setting can be set in the “Basic” settings
tab in the details area of each transfer connection. Please refer to (→16.3) and then to
the respective connection type’s section.

16.1.2 Export order

The export order of a transfer event is a setting that applies only to the respective transfer
event and has no effect on other transfer events. The export order determines, for a given
transfer event, the order, in which the transfer event should try to use a certain connection
for data transfer.
If the defined default connection is set to USB and, for example, the set order is

1. Default

2. WIFI

3. USB

4. PPP

The logger will try to start a transfer for this event to Default (USB). If no USB device is con-
nected, it will then continue the list (WIFI,...) until the next available transfer connection
and start transfer using that connection.

16.1.3 Transfer priority

The transfer priority of a transfer event is, unlike the export order, a global setting. It regu-
lates the order of data transfer between all defined transfer events in your configuration.
Transfer priorities do not apply to only a transfer event (Trigger event or system event) but
they always apply to a combination of a transfer event and a transfer connection. The
following example will try to explain how that works.

Intheexample,therearethreetransferevents,the“Startup”eventandthe“Shutdown”
event and a trigger event. The “Startup” event in combination with the “PPP” transfer
connection has a priority of 100, so that as soon as the logger starts, it will, whenever
possible,startsendingdataviaUMTS.

Changesanderrorsexcepted.

648

16.1 TRANSFEREVENTS

The trigger event is also using a “PPP” transfer connection, because when the trigger
is fired, it should also start transferring data as soon as possible. However, it is not of the
highestprioritytostartsendingrightaway,soitissettoapriorityof80. Thatmeans,when
the trigger is fired, the combination of the trigger event has a lower priority than the
combination of the “Startup” event and the “PPP” connections and will therefore wait
forthe“Startup”eventtofinishtransferbeforeitcanstartanewdatatransfer.

Changesanderrorsexcepted.

649

16.1 TRANSFEREVENTS

However,assoonasthevehiclereturnstothegarageandisturnedoff,wemighthave
a quicker transfer connection available, such as WIFI or ETH, and want datatransfer to
happen using that connection. For that reason, the combination of the “Shutdown”
event and the WIFI connection have the hightest possible priority setting (255). That
means, as soon as a shutdown condition has occurred, all current data transfer will be
stopped, the logger will try to establish a WIFI connection and start datatransfer using
thatWIFIconnection.

16.1.4 Trigger events

A “Trigger event” will trigger data transfer whenever the selected trigger is set. Any
preivously configured trigger of your system can be used to trigger data transfer.

In order to configure a “Trigger event”, you will first need to add the “Trigger event” as a
“Transfer event”. To do so, select the tree element “Transfer events”, click on the “Com-
ponents” button in the Ribbon and choose “Trigger event”.

Changesanderrorsexcepted.

650

16.1 TRANSFEREVENTS

16.1.4.1 Tree elements for Trigger events

Adding a “Trigger event” for data transfer will add one new child element to the tree
element “Transfer events”, called “Trigger event”. Multiple “Trigger events” may be
added, which will each result in an extra tree element. The name of these elements can
be changed in the details area of each tree element.

Each “Trigger event” will also possess various child elements representing the possible tar-
gets (transfer connections) for this trigger event as well as child elements representing the
available datasets/ring buffers and file servers (only for WIFI and LAN connections) for
each target.

16.1.4.2 Grid area for Trigger events

The grid area for a “Trigger event” for data transfer will present you with an overview of
the available connections for data transfer.
You can choose the desired connection for data transfer by ticking the “Use for transfer”
tickbox, and you can override transfer limits by ticking the tickbox labeled “Ignore transfer
limits”.
You may also choose multiple connections for transfer and priorityze them.

Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

Changesanderrorsexcepted.

651

16.1 TRANSFEREVENTS

16.1.4.3 Details area for Trigger events

The Details area shows settings for the “Triggger event”, that has been selected in the
tree. The different tabs of the details area will be explained in the following.

General
Please refer to (→4.2.2).

Trigger
This tab contains only the setting “Event trigger”, which allows you to select which trigger
should be used to start data transfer.

Clicking the “Select” button will open a window, which allows you, to choose the desired
trigger. Confirm with “OK”.
Once a trigger has been chosen, the “Trigger event” will automatically named after this
event.

Changesanderrorsexcepted.

652

16.1 TRANSFEREVENTS

16.1.5 Time events

A “Time event” will trigger data transfer according to a set time intervall.

In order to configure a “Time event”, you will first need to add the “Time event” as a “Trans-
fer event”. To do so, select the tree element “Transfer events”, click on the “Components”
button in the Ribbon and choose the desired time intervall from the menu “Time event”.

16.1.5.1 Tree elements for Time events

Adding a “Time event” for data transfer will add one new child element to the tree
element “Transfer events”, called “Time event”. Multiple “Time events” may be added,
which will each result in an extra tree element. The name of these elements can be
changed in the details area of each tree element.

Each “Time event” will also possess various child elements representing the possible targets
(transfer connections) for this time event as well as child elements representing the avail-
able datasets/ring buffers and file servers (only for WIFI and LAN connections) for each
target.

Changesanderrorsexcepted.

653

16.1 TRANSFEREVENTS

16.1.5.2 Grid area for Time events

The grid area for a “Time event” for data transfer will present you with an overview of the
available connections for data transfer.
You can choose the desired connection for data transfer by ticking the “Use for transfer”
tickbox, and you can override transfer limits by ticking the tickbox labeled “Ignore transfer
limits”.
You may also choose multiple connections for transfer and priorityze them.

Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

16.1.5.3 Details area for Time events

The Details area shows settings for the “Time event”, that has been selected in the tree.
The different tabs of the details area will be explained in the following.

General
Please refer to (→4.2.2).

Time
This tab allows you to specify the time intervall for the transfer event.

Changesanderrorsexcepted.

654

16.1 TRANSFEREVENTS

16.1.6 System events

A “System event” will trigger according to a set “System event” such as “Startup”,
“Shutdown”, “Dataset closed” and others.

In order to configure a “System event”, you will first need to add the “System event” as a
“Transfer event”. To do so, select the tree element “Transfer events”, click on the “Compo-
nents” button in the Ribbon and choose the desired event from the menu “System event”.

Available System events

System event
Startup
Shutdown

Characteristics
Data transfer will start as soon as startup is finished.
Data transfer will start when shutdown is prompted. Shutdown
will not occur until data transfer has finished.

Start Measurement Data transfer will start as soon as measurement has started.
Stop Measurement Data transfer will start as soon as measurement has stoped.
Start Recording

Stop Recording

Dataset closed
USB plugged

Data transfer will start as soon as recording of measurement data
in a dataset has started.
Data transfer will start as soon as recording of measurement data
in a dataset has stoped.
Data transfer will start as soon as the current dataset is closed.
Data transfer will start as soon as a USB storage medium is
plugged in.

Changesanderrorsexcepted.

655

16.1 TRANSFEREVENTS

16.1.6.1 Tree elements for System events

Adding a “System event” for data transfer will add one new child element to the tree
element “Transfer events”, called according to the type of “System event” you have
chosen. Multiple “System events” may be added, which will each result in an extra tree
element.

Each “System event” will also possess various child elements representing the possible tar-
gets (transfer connections) for this system event as well as child elements representing
the available datasets/ring buffers and file servers (only for WIFI and LAN connections) for
each target.

16.1.6.2 Grid area for System events

The grid area for a “System event” for data transfer will present you with an overview of
the available connections for data transfer.
You can choose the desired connection for data transfer by ticking the “Use for transfer”
tickbox, and you can override transfer limits by ticking the tickbox labeled “Ignore transfer
limits”.
You may also choose multiple connections for transfer and priorityze them.

Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

16.1.6.3 Details area for System events

As “System events” are definite predefined events, there are no further settings for these
events available in the details area. It contains only the “General” tab, which will allow
you to give a user specific description to the event. Please refer to (→4.2.2).

Changesanderrorsexcepted.

656

16.2 TRANSFEREVENTTARGETS

16.2 Transfer event targets

Transfer events need to have at least one target defined, in order for transfer to happen.
Transfer event targets are transfer connections, which get asigned to a transfer event. For
instructions regarding the transfer connections pleaser refer to (→16.3).

16.2.1 Tree elements for transfer event targets

Each transfer event in the measurement task tree has a number of child elements,
corresponding to the transfer connections that have been configured so far. These are
the transfer event’s targets.

Furthermore will each target possess one or two (only for WIFI and LAN connections) child
elements:

• Dataset

The “Dataset” element is available for each transfer event target and contains all
datasets and ring buffers that can be chosen for transfer in the grid area.

• File server

The “File server” element is available for the WIFI and LAN transfer event targets and
contains all respective file servers that can be chosen for transfer in the grid area.

Changesanderrorsexcepted.

657

16.2 TRANSFEREVENTTARGETS

16.2.2 Grid area for transfer event targets

Depending whether you select the “Dataset” element or “File server” element for a given
transfer event target, the grid area will present you with an overview of all the currently
defined datasets or file servers, that can be set for datatransfer.
The tickbox “Transmit” allows you to set which datasets will be transmitted or which
fileserver will be used for transmission.

Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

Gridareafortransfereventtargetshowingtheavailabledatasets.

Gridareafortransfereventtargetshowingtheavailablefileservers.

Changesanderrorsexcepted.

658

16.2 TRANSFEREVENTTARGETS

16.2.3 Details area for transfer event targets

The details area for transfer event targets provides settings regarding the target. Different
settings can be found in the details area depending on whether the transfer connection
of the target (e.g. USB, WIFI, etc.) or the corresponding dataset element has been
selected in the tree.

16.2.3.1 Transfer event target settings

Settings
Transfer event target specific settings.

• Use for transfer

Set if you want to use this connection for datatransfer.

• Transfer priority

Set the transfer priority for this Transfer event/Transfer connection combination. For
further details please see (→16.1.3).

• Ignore transfer limits

Allows you to override transfer limits.

• Show dialog

If marked active, a dialog will inform the user about active datatransfer for this con-
nection on connected displays.

Changesanderrorsexcepted.

659

16.2 TRANSFEREVENTTARGETS

16.2.3.2 Transfer event target dataset selection

Transmit
Settings specific to dataset/ring buffer transmission for the corresponding transfer event
target.

• Configured datasets/ringbuffer

that have been
“Configured datasets/ringbuffers” are all datasets/ringbuffers,
logger configuration (as opposed to unconfigured
set up in your current
datasets/ringbuffers which are explained below;
for more detailed information
on configured and unconfigured datasets/ringbuffers please refer to the example
below →16.2.3.2). There are three options for transmission available.

Dataset/Ringbuffer
selection
All

Selected

None

Characteristics

All configured datasets/ringbuffers of the current logger
configuration will be transmitted.
Only the datasets/ringbuffers which have been set to trans-
mit in the grid area, using the tickbox “Transmit” as ex-
plained here (→16.2.2), will be transmitted.
None of the configured datasets/ringbuffers of the current
logger configuration will be transmitted.

It is possible to transmit a combination of configured and unconfigured
datasets/ringbuffers.

• Unconfigured datasets/ringbuffer

“Unconfigured datasets/ringbuffers” include all datasets/ringbuffers which have not
been set up as part of the current configuration but are still stored on the logger
(obsolete datasets/ringbuffers, stack trace and fallback files; for more detailed in-
formation on configured and unconfigured datasets/ringbuffers please refer to the
example below →16.2.3.2).
If this setting is active all unconfigured datasets/ringbuffers will be transmitted.

• Only protected (Ring buffer only)

If set, the ringbuffer datasets will only be transmitted if they are protected.

Changesanderrorsexcepted.

660

16.2 TRANSFEREVENTTARGETS

• Remove protection (Ringbuffer only)

If set, the ringbuffer datasets’ protection will be removed once transmitted.

Examplefortransmissionofacombinationofconfiguredand
unconfigureddatasets/ringbuffers

Unconfigured datasets/ringbuffers are obsolete datasets/ringbuffers,
stack traces and fallback files from previous configuration which are still
stored on the logger even though it is running a different configuration.
This may be the case if for any reason a dataset/ringbuffer could not be
transmitted (e.g. due to the lack of a fast enough transfer connection)
but a new configuration needs to be executed on the logger in order
to continue data acquisition.
In that case the datasets/ringbuffers
which have not been tranfered yet will stay stored on the logger as
“unconfigured” datasets/ringbuffers until they have been transfered
from the logger.

Once the vehicle returns to the garage and therefore possesses a fast
enough transfer connection it may therefore be necessary to transfer
both configured datasets/ringbuffers from the current logger configura-
tion as well as unconfigured datasets/ringbuffers from previous logger
configurations.

To do so on can for example set up a transfer event target using a PPP
connection and set the parameter for configured datasets/ringbuffers
to “Selected” and only transfer a selection of
the configured
datasets/ringbuffers while being on the road using this PPP connection.
All configured datasets/ringbuffers which have not been selected and
all unconfigured datasets/ringbuffers would still stay on the logger’s stor-
age.
Additionally one could set up a transfer event taret using a fast WIFI con-
nection and set the parameter for configured datasets/ringbuffers to
“All” while also activating the setting “Unconfigured datasets/ringbuffer”
and thus transfer all unconfigured datasets/ringbuffers. That way all the
in the logger’s storage (configured
datasets/ringbuffers remaining still
and unconfigured) will be transferred as soon as the faster WIFI connec-
tion in the garage is available.
Only once they have been transferred old datasets/ringbuffers will be
erased from the logger’s storage.

Changesanderrorsexcepted.

661

16.2 TRANSFEREVENTTARGETS

16.2.3.3 Transfer event target fileserver selection

Settings
When a fileserver from the list of available fileservers for a transfer event target is selected,
the “Transmit” setting in the details area allows you to define whether a fileserver should
be used for transmission.
The same setting can be accessed directly in the grid area showing the list ov available
fileservers for a transfer event targe as described here (→16.2.2).

Changesanderrorsexcepted.

662

16.3 TRANSFERCONNECTIONS

16.3 Transfer connections

In order for data to be transferred, a transfer connection has to be set up. There are four
different types of connections, that can be set up:

• USB (→16.3.1)

• WIFI (→16.3.2)

• LAN (→16.3.3)

• PPP/UMTS (→16.3.4)

16.3.1 Data transfer via USB

USB is the predefined default connection for data transfer and therefore it is included in
the measurement task tree by default. Via USB it is possible to transfer data to and from
an external storage device.
Configuration of a USB connection happens exclusively inside the details area of the tree
element “USB”.

16.3.1.1 Details area for USB

General
Please refer to (→4.2.2).

Basic
This tab contains basic settings for the connection.

• Check for update

Allows you to define, how often and when the logger should check for updated
configuration or firmware.
If the option “Interval” is selected, the time interval may be set in the field on the right
of the dropdown menu.

• Data transfer

Allows you to restrict, how often data transfer from the logger may occur.
If the option “Interval” is selected, the time interval may be set in the field on the right
of the dropdown menu.

Changesanderrorsexcepted.

663

16.3 TRANSFERCONNECTIONS

• Use as default

Tick or untick this box in order to make this your default connection for data transfer.

MD5
This tab provides settings regarding the MD5 check of transferred files.

Paths
This tab allows you to set the paths for data transfer.

• Measurement data

Define the path, where measurement data should be stored.

• Configuration (cfgdir)

Define the path, where the logger will check for a newer version of the current con-
figuration (datalog.ccmc) and firmware.
If there is a newer version, the logger will download it, append the current timestamp
in the filename, and apply/install it at the next possible moment.

• Configuration archive (optional)

Define the subpath for previous logger configurations and firmwares. If this subpath
has been defined, the logger will copy the previously used configuration/firmware
here, when he receives a newer version. If this subpath is not defined, the logger will
leave the file in the “Configuration” path, that has been defined before.

• Subconfiguration path

These fields allow you to define up to four paths under which the logger should check
for subconfigurations to transfer.

Changesanderrorsexcepted.

664

16.3 TRANSFERCONNECTIONS

In the field “Measurement data”, “Configuration” and “Subconfiguration
path” project parameters can be used as variables. For more informa-
tion please refer to (→5.6).

16.3.2 Data transfer via WIFI

In order to transfer data via WIFI, you will first need to add a WIFI connection to your system.
To do so, select the tree element “Connections”, click on the “Components” button in the
Ribbon and then choose “WIFI”.
After having set up the WIFI connection, you will need to set up a fileserver to which to
transfer data. For instructions on how to set up a fileserver please refer to the section
“Fileserver” (→16.3.6).

Changesanderrorsexcepted.

665

16.3 TRANSFERCONNECTIONS

16.3.2.1 Tree elements for WIFI connections

Adding a WIFI connection for data transfer will add two new child elements to the tree
element “Connections”:

• WIFI

Represents the WIFI connection itself.

• Access point xx

Represents the WIFI access point. A WIFI connection can have various access points,
in order to connect to different networks. To add a new access point, select the tree
element WIFI, then click the “Components” button in the Ribbon and select “Access
point”.

16.3.2.2 Grid area for WIFI connections

The grid area for a “WIFI connection” for data transfer will present you with an overview
of all the currently defined access points for WIFI connections.
It also allows to set the
“Export order” and “Connect priority” for each access point. For details regarding the
“Export order” and “Connect priority” please refer to (→16.3.2.3).

Using the “Column chooser” it is also possible to add the “Password” column to the grid
area for your WIFI connection. This allows you to set the password for each access point
with “WPA-EAP” authentication mode directily in the grid area.
Instructions on how to use the “Column chooser” can be found here (→4.2.5).

Another important function of the grid area is the “Filter editor” (→4.2.6).

Changesanderrorsexcepted.

666

16.3 TRANSFERCONNECTIONS

16.3.2.3 Details area for WIFI

The details area provides settings either for the WIFI connection in general or for a specific
access point, depending on which element has been selected in the tree.

WIFI Settings

General
Please refer to (→4.2.2).

Basic
This tab contains basic settings for the connection.

• Check for update

Allows you to define, how often and when the logger should check for updated
configuration or firmware.
If the option “Interval” is selected, the time interval may be set in the field on the right
of the dropdown menu.

• Data transfer

Allows you to restrict, how often data transfer from the logger may occur.
If the option “Interval” is selected, the time interval may be set in the field on the right
of the dropdown menu.

• Use as default

Tick or untick this box in order to make this your default connection for data transfer.

• Access point scan

If active, the logger will scan for access points in the environment.

The “AP scan” parameter cannot be set by the user anymore but will be
automatically set by the logger.

• Country code

Fill in the two letter WIFI country code for the vehicle’s location according to ISO
3166.

Changesanderrorsexcepted.

667

16.3 TRANSFERCONNECTIONS

MD5
This tab provides settings regarding the MD5 check of transferred files.

• Checks

Define how often the check should be executed.

• Delay between checks

Define the delay between two checks.

• Accepted failures

Define the number of accepted failures before aborting the data transfer.

Changesanderrorsexcepted.

668

16.3 TRANSFERCONNECTIONS

Access point Settings
Each WIFI connection can have multiple access points, in order to be able to connect
to different wireless networks. By setting the priority and export order of the access points
in the grid area, you define, which access point will be used first, starting with highest
priority (255) and export order 1. As soon as data transfer via one access point has been
successfully completed, the other access points will be skipped and the dataset will be
erased from the logger.

In order to add an extra access point, select the tree element “WIFI”, click on the
“Components” button in the Ribbon and the choose “Access point”.

Connect priority for access points
The “Connect priority” setting can be found in the grid area for WIFI connections.
It
allows you to set up a priority list for all your configured WIFI access points. This may be
necessary if the same configuration is being used on vehicles in different countries. For
example if a vehicle is being tested in Sweden, you can prioritize all the access points in
the Sweden testing facility, so that the logger will try to establish a connection with one
of these access points.

Values between 0 and 255 can be applied and the higher value has a higher priority.

Export order for access points
The export order can also be found in the grid area for WIFI connections and allows for
additional customization of the order, in which the the different access points will be
used for data transfer. It is applied after the “Connect priority” and therefore “Connect
priority” always outranks “Export order”.
Looking at the example mentioned above in regarding the “Connect priority”, this allows
to tell the logger to prioritize the access points in the Sweden testing facility, and then

Changesanderrorsexcepted.

669

16.3 TRANSFERCONNECTIONS

determine the order, in which the transfer event should try to connect to the available
access points with the same priority.
The logger will first try to establish a connection to the access point with the export order 1.
If a connection has successfully been established, the logger will start data transfer. If the
connection fails, the logger will attempt to connect to the next access point according
to the export order.

General
Please refer to (→4.2.2).

Network
This tab contains settings regarding the network to which the logger will connect.

• Network name

Define the name of the WIFI network (SSID).

• Get IP address automatically

Define whether the logger will expect the allocation of a valid IP address automati-
cally by a DHCP server, or whether you want to manually set an IP address.

• IP address

IF DHCP is disabled, this field allows you to manually enter an IP address.

• Network mode

Allows you to choose the mode of the network you wish to connect to.

Security
This tab provides security settings regarding the access point and the network you wish to
connect to.

• Authentication mode

Select the authentication mode of the network.

• Network key

Type in the authentication key of the network.

Changesanderrorsexcepted.

670

16.3 TRANSFERCONNECTIONS

• Login mode

If the authentication mode of the network is WPA-EAP, then you may here set whether
to login with a certificate or not.

• Security protocol

If the authentication mode of the network is WPA-EAP, then you may here set the
security protocol. The default setting “WPA/WPA2” will automatically choose the
correct protocol.

• Identity

If the authentication mode of the network is WPA-EAP, then you may here enter your
identity/username.

• Password

If the authentication mode of the network is WPA-EAP, then you may here enter your
password.

Changesanderrorsexcepted.

671

16.3 TRANSFERCONNECTIONS

16.3.3 Data transfer via LAN

In order to transfer data via LAN, you will first need to add a LAN connection to your system.
To do so, select the tree element “Connections”, click on the “Components” button in the
Ribbon and then choose “LAN”.
After you have set up the LAN connection, you will need to additionally set up a fileserver,
where the transferred data will be stored. Please refer to the section “Fileserver” (→16.3.6).

16.3.3.1 Tree elements for LAN connections

Adding a LAN connection for data transfer will add one new child element called “LAN”
to the tree element “Connections”

16.3.3.2 Details area for LAN

The details area provides settings for the LAN connection.

General
Please refer to (→4.2.2).

Changesanderrorsexcepted.

672

16.3 TRANSFERCONNECTIONS

Basic
This tab contains basic settings for the connection.

• Check for update

Allows you to define, how often and when the logger should check for updated
configuration or firmware.
If the option “Interval” is selected, the time interval may be set in the field on the right
of the dropdown menu.

• Data transfer

Allows you to restrict, how often data transfer from the logger may occur.
If the option “Interval” is selected, the time interval may be set in the field on the right
of the dropdown menu.

• Use as default

Tick or untick this box in order to make this your default connection for data transfer.

MD5
This tab provides settings regarding the MD5 check of transferred files.

• Checks

Define how often the check should be executed.

• Delay between checks

Define the delay between two checks.

• Accepted failures

Define the number of accepted failures before aborting the data transfer.

Changesanderrorsexcepted.

673

16.3 TRANSFERCONNECTIONS

16.3.4 Data transfer via PPP/UMTS

In order to transfer data via PPP/UMTS, you will first need to configure a PPP/UMTS con-
nection. To do so, please refer to (→16.3.4.1). Once a PPP/UMTS connection has been
set up, you will need so set the basic settings for PPP data transfer and you will also need
to set up a fileserver. This chapter treats the basic settings for data transfer via PPP.
For instructions on how to set up a fileserver please refer to the section “Fileserver”
(→16.3.6).

16.3.4.1 Setting up a PPP/UMTS connection

To set up a PPP/UMTS connection, select your system (Arcos, μCros, μCros XL) in the tree,
click the “Components” button in the Ribbon and choose “PPP”.

This will add two elements called “PPP” to the measurement task tree. One as a childele-
ment to the main system (Arcos, μCros, μCros XL) and one as a childelement to the tree
element “Connections”. Select the first of the two, navigate to the tab “Connection” in
the details area and fill in the access data. This data can be obtained from your simcard
provider.
The option “Persistent connection” allows you to maintain a connection not only during
data transfer but also during measurement.

Changesanderrorsexcepted.

674

16.3 TRANSFERCONNECTIONS

From V17.10.00 on it is possible to fill in a PIN code to unlock the SIM card.
It is therefore not longer necessary to remove the PIN code from the SIM
card.

16.3.4.2 Details area for PPP/UMTS

Configuration of a USB connection happens exclusively inside the details area of the tree
element “USB”.

General
Please refer to (→4.2.2).

Basic
This tab contains basic settings for the connection.

• Check for update

Allows you to define, how often and when the logger should check for updated
configuration or firmware.
If the option “Interval” is selected, the time interval may be set in the field on the right
of the dropdown menu.

• Data transfer

Allows you to restrict, how often data transfer from the logger may occur.
If the option “Interval” is selected, the time interval may be set in the field on the right
of the dropdown menu.

• Use as default

Tick or untick this box in order to make this your default connection for data transfer.

Changesanderrorsexcepted.

675

16.3 TRANSFERCONNECTIONS

MD5
This tab provides settings regarding the MD5 check of transferred files.

16.3.4.3 PPP status signals

The PPP module of the logger provides a list of status signals regarding the PPP connec-
tion. To access these signals, the “PPP status” component needs to be added to the
configuration. To do so, select the “PPP” interface in the tree, click the “Components”
button in the Ribbon and then choose “PPP status”.

The grid area of the new tree element “PPP status” provides you with an overview of
These signals are of the type “Internal signal”, for
the available “PPP status” signals.
further information regarding these signals please refer to the chapter “Internal signals
properties” (→8.26.3).

Changesanderrorsexcepted.

676

16.3 TRANSFERCONNECTIONS

OveviewofPPPstatussignals

Signal
Conncection status

Connection type

Network operator

Signal quality

Signal RSSI

Meaning
0 = not registered (not search-
ing)
1 = registered (home network)
2 = not registered (searching)
3 = registration denied
5 = registered (roaming)
1 = GSM
2 = UMTS
3 = GSM (with EDGE)
4 = UMTS (with HSDPA)
5 = UMTS (with HSUPA)
6 = UMTS (with HSDPA and
HSUPA)
7 = LTE
Information about your SIM
card’s network operator
Information about the quality
of the signals
Information
about
strength of the signals

the

Unit
-

-

-

%

dBm

Changesanderrorsexcepted.

677

16.3 TRANSFERCONNECTIONS

16.3.5 Wake on Call/Text

The two functions “Wake on Call” and “Wake on Text” are functions of the “PPP” interface
and both allow to wake up the logger remotely via a mobilephone.
In the case of “Wake on Call”, a phone number will be defined in the configuration and
if the logger receives a call from the configured number, it will wake up.
In the case of “Wake on Text” a passphrase will be defined in the configuration and if the
logger receives a text containing the configured passphrase, it will wake up.

To add “Wake on Call/Text” you will first need to add the “Wake on” interface. To do
so select the “PPP” element in the measurement task tree, click on the “Components”
button in the Ribbon and then select “Wake on”.

In the next step select the “Wake on” inteface in the measurement task tree, click the
“Components” button in the Ribbon and then choose “WakeOnCall” or “WakeOnText”.

Changesanderrorsexcepted.

678

16.3 TRANSFERCONNECTIONS

16.3.5.1 Tree elements for Wake on Call/Text

Adding the “Wake on” interface to your system will add one new element labeled “Wake
on” to your measurement task tree.

16.3.5.2 Grid area for Wake on Call/Text

The grid area for a “Wake on” will present you with an overview of all the currently defined
“Wake on Call/Text” modules.

Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

16.3.5.3 Details area for Wake on Call/Text

The details area provides settings for a “Wake on Call/Text” module. Choose the module
you wish to configure in the grid area and then navigate to the details area.

General
Please refer to (→4.2.2).

Settings
This tab contains settings for the connection.

In case of “Wake on Call” you can here define the phone number, that will wake up the
logger.

Changesanderrorsexcepted.

679

16.3 TRANSFERCONNECTIONS

In case of “Wake on Text” you can here define the passphrase, that will wake up the
logger.

Changesanderrorsexcepted.

680

16.3 TRANSFERCONNECTIONS

16.3.6 Setting up a Fileserver

Transferring data via WIFI/LAN/PPP/UMTS requires the configuration of a fileserver to which
the data will be transferred. To do so, select the tree element for the connection you wish
to configure: “PPP”, “LAN”, “Access point xx” (for WIFI connections the acccess point has
to be selected instead of the WIFI connection), click the “Components” button in the
Ribbon and choose “Fileserver”.

Changesanderrorsexcepted.

681

16.3 TRANSFERCONNECTIONS

16.3.6.1 Multiple File servers

Each data transfer connection can have multiple file servers, in order to ensure successfull
data transfer. By setting the priority of the file servers in the grid area, you define, which file
server will be used first, starting with priority 1. As soon as data transfer via one file server
has been successfully completed, the other file servers will be skipped and the dataset
will be erased from the logger.

16.3.6.2 Tree elements for File servers

Adding a Fileserver will add one new element called “Fileserver” to the tree. It is possible
to add multiple fileservers, to one connection, but they will all be found under the same
tree element. An overview of the fileservers can be seen in the grid area.

Changesanderrorsexcepted.

682

16.3 TRANSFERCONNECTIONS

16.3.6.3 Grid area for File servers

The grid area for a “Filserver” will present you with an overview of all the currently defined
added fileservers. It also allows you to prioritize the various fileservers.

Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

16.3.6.4 Details area for File servers

The details area provides settings for a file server. Choose the fileserver you wish to config-
ure in the grid area of the tree element “File server” and then navigate to the details area.

General
Please refer to (→4.2.2).

It is now possible to edit the “Name” field in a file server’s “General” tab.

Changesanderrorsexcepted.

683

16.3 TRANSFERCONNECTIONS

Connection
This tab contains settings for the connection.

• Protocol

Select the protocol used for data transfer to the file server.

• Single session

If set, the SFTP single session mode will be used.

• Hostname

Define the IP address or hostname of the SSH file server.

• Port

Define the port or hostname of the SSH file server.

• User name

Fill in the user name to access the SSH file server.

• Password

Fill in the password to access the SSH file server.

• Remember connection

If set, after a successfull transfer this server will be tried first in the future.
If at any point unsusccessfull, priority will be reset to 0.

In the field “User name” project parameters can be used as variables.
For more information please refer to (→5.6).

Changesanderrorsexcepted.

684

16.3 TRANSFERCONNECTIONS

Paths
This tab allows you to set the paths for data transfer.

• Measurement data

Define the path, where measurement data should be stored.

• Configuration

Define the path, where the logger will check for a newer version of the current con-
figuration (datalog.ccmc) and firmware.
If there is a newer version, the logger will download it, append the current timestamp
in the filename, and apply/install it at the next possible moment.

• Configuration archive (optional)

Define the subpath for previous logger configurations and firmwares. If this subpath
has been defined, the logger will copy the previously used configuration/firmware
here, when he receives a newer version. If this subpath is not defined, the logger will
leave the file in the “Configuration” path, that has been defined before.

In the fields “Measurement data” and “Configuration” project param-
eters can be used as variables. For more information please refer to
(→5.6).

Changesanderrorsexcepted.

685

17 SECOCCERTIFICATES

17 SecOC Certificates

SecOC stands for Secure Onboard Communication.
It allows you to set your logger up
with security certificates, which allow the logger to start an active communication on a
protected bus.

17.1 Adding SecOC certificates to the configuration

In order to work with SecOC certificates you will first need to add the “SecOC Certifi-
cates” interface to the measurement task tree. Subsequently there exist two different
ways which both allow you to add and configure a SecOC certificate. The difference in
both methods is exclusively in the process of adding/importing the certificate. The final
result is identical regardless of the method chosen to add/import the certificate.

In order to add the “SecOC Certificates” interface, select the system in the measurement
task tree, click the “Components” button in the Ribbon and then choose “SecOC Certifi-
cates”. This will add the “SecOC Certificates” interface to your measurement task tree.

Changesanderrorsexcepted.

686

17.1 ADDINGSECOCCERTIFICATESTOTHECONFIGURATION

17.1.1 Importing a SecOC certificate

The more direct way of setting up a SecOC certificate for your logger is by simply
importing the certificate into the “SecOC Certificates” interface. To do so select the
“SecOC Certificates” interface in the measurement task tree, click the “Import” button in
the Ribbon.

In the resulting window navigate to the file path of the desired certificate, select the
certificate and confirm with “Open”. All imported certificates can later be found in the
grid area (→17.3) of the “SecOC Certificates” interface.

Changesanderrorsexcepted.

687

17.1 ADDINGSECOCCERTIFICATESTOTHECONFIGURATION

17.1.2 Adding a SecOC certificate

Alternatively to directly importing the certificate file it is also possible to add an blank
certificate node to the “SecOC Certificates” interface and to define the underlying
certificate file for this certificate in a subsequent step.
This may be useful when one or more certificates need to be set up that for different
reasons should receive the corresponding certificate files at a later moment.

In order to add a certificate to the “SecOC Certificates” interface, select the interface
in the measurement task tree, click the “Components” button in the Ribbon and then
choose “Certificate”.
This will directly add a blank certificate node which can be found in the grid area
(→17.3) of the “SecOC Certificates” interface. To configure the certificate and define the
underlying certificate file, select the newly created certificate node in the grid area and
then navigate to the details area (→17.4).

Changesanderrorsexcepted.

688

17.2 TREEELEMENTSFORSECOCCERTIFICATES

17.2 Tree elements for SecOC Certificates

Adding the “SecOC Certificates” interface to your system will also add it as a tree element
to the measurement task tree. This tree element does not possess any child elements.

17.3 Grid area for SecOC Certificates

If the “SecOC Certificates” element is selected in the Measurement task tree, the grid
area will provide you with an overview of all available certificates and their most important
properties.
Also you can find here two important functions, which are the “Column chooser” (→4.2.5)
and the “Filter editor” (→4.2.6).

Changesanderrorsexcepted.

689

17.4 DETAILSAREAFORSECOCCERTIFICATES

17.4 Details area for SecOC Certificates

If a SecOC certificate has been selected in the grid area, you may access and configure
the certificate’s settings in the “Settings” tab of the details area.

Settings
This tab provides the settings that allow to configure the behaviour of a SecOC certificate.

• Certificate file

This field allows you to define the underlying certificate file for a SecOC certificate.
Click on the button on the right of the field to open an explorer window and choose
the desired certificate file.

• Password

Define a password for the SecOC certificate.

• Encryption mode

Choose the encryption mode which should be used to encrypt the certificate and
password on the logger There are three options available.

The corresponding private key file always has to be uploaded to the log-
ger using the web interface of the logger. For instructions consult the
web interface manual section “Encryption keys”.

Changesanderrorsexcepted.

690

17.4 DETAILSAREAFORSECOCCERTIFICATES

Encryption
mode
None
Default key

Custom key

Meaning

No encryption.
The standard IPEmotion GPG key will be used for encryption. For this
mode, the public GPG key needs to be deposited in the IPEmotion
“GPG keys” directory. Please note the “Important” box above this
table regarding the corresponding private key. Only one GPG key
pair may be deposited in this directory and this key pair will be used
as the default IPEmotion GPG key.
To find out or change the “GPG keys” directory access the “Op-
tions” menu via the “File” button and then navigate to “Directories”
in the lefthand sidebar of the menu. For more info please consult
the IPEmotion manual.
A custom public key, which can be specified in the “Custom key
file” field below, will be used for encryption. Please note the “Im-
portant” box above this table regarding the corresponding private
key.

• System key name

If a default GPG key is available in the “GPG keys” directory, this field will tell you the
name of the key.

• Custom key file

This field allows you to define a custom pubilc GPG key . Click on the button on the
right of the field to open an explorer window and choose the desired key file.

Changesanderrorsexcepted.

691

18 SETTINGUPATIMESERVER

18 Setting up a time server

In order for your logger to always have the correct time, you will need to set up a time
server to which the logger will connect and then synchronize its time with.

A time server can be configured for every LAN, WIFI or PPP/UMTS connection. To do so,
select the tree element for the connection you wish to configure: “PPP”, “LAN”, “Access
point xx” (for WIFI connections the acccess point has to be selected instead of the WIFI
connection), click the “Components” button in the Ribbon and choose “Time server”.

Then select the “Time server xx” in the grid area of the tree element “Time server xx” and
navigate to the “Connections” tab in the details area and set the hostname/IP address in
the field “Hostname”.

Changesanderrorsexcepted.

692

18 SETTINGUPATIMESERVER

It is now possible to edit the “Name” field in a time server’s “General” tab.

Changesanderrorsexcepted.

693

19 OBTAININGEXTENDEDSUPPORT

19 Obtaining extended support

support@caetec.de
+49 8142 501365

Changesanderrorsexcepted.

694


