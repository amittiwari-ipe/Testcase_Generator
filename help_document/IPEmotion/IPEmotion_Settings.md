IPEmotionSettings COM Reference

Version: 2026 R1 RC Build 96992

January 2026

Table of contents

1

2

3

4

5

6

7

Important and general information

1.1
1.2

Important information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
General information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

IPEmotionSettings

2.1

IPEmotionSettings Interfaces Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

IPEmotionSettings Namespace Index

3.1

IPEmotionSettings Namespace List . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

IPEmotionSettings Hierarchical Index

4.1

IPEmotionSettings Interface Hierarchy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

IPEmotionSettings Interface Index
IPEmotionSettings Interface List

5.1

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

IPEmotionSettings Namespace Documentation

6.1

IPEmotionSettings Namespace Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

IPEmotionSettings Interface Documentation

ICloudDrive Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.1
ICloudDrives Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.2
IDataPlugIn Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.3
IDataPlugIns Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.4
IDataServiceObservedDirectories Interface Reference . . . . . . . . . . . . . . . . . . . . . .
7.5
IDataServiceObservedDirectory Interface Reference . . . . . . . . . . . . . . . . . . . . . . .
7.6
IInstrumentPlugIn Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.7
IInstrumentPlugIns Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.8
7.9
IMapProvider Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.10 IMapProviders Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.11 InstrumentPlugInProxy Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.12 InstrumentPlugInsEnum Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.13 InstrumentPlugInsProxy Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.14 IOperationPlugIn Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.15 IOperationPlugIns Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.16 IPlugIn Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.17 IPlugInOption Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.18 IPlugInOptions Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.19 IPlugIns Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.20 IReferenceObject Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.21 IReferenceObjects Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.22 ISettingsHandler Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.23 IUserAccount Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.24 IUserAccounts Interface Reference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

1
1
5

7
7

9
9

11
11

13
13

15
15

29
29
31
33
35
36
38
39
41
43
44
45
47
48
50
51
52
54
55
56
57
58
59
79
81

Chapter 1

Important and general information

1.1 Important information

Please follow these instructions before and during the use and application on any IPETRONIK product!

1.1.1 Safety and Warning instructions

Please follow the instructions and information as contained in the user manual!

1. The user can influence an electronic system by applying the IPETRONIK product. This might cause

risk of personal injury or property damages.

2. The use and application of the IPETRONIK product is permitted only to qualified professional

staff, as well as, only in appropriate manner and in the designated use.

3. Before using an IPETRONIK measurement system in the vehicle it has to be verified that no func-

tion of the vehicle, which is relevant for secure operation, might be influenced:

• by the installation of the IPETRONIK measurement system in the vehicle,

• by an potential malfunction of the IPETRONIK system during the test drive.

In order to avoid possible danger or personal injury and property damages, appropriate actions are to
be taken; such actions have to bring the entire system into a secured condition (e.g. by using a system
for emergency stop, an emergency operation, monitoring of critical values). Please check the following
points to avoid errors:

• Adaption of sensors to components of the electrical system / electronics, brake system, engine and

transmission control, chassis, body.

• Tap of one or several bus systems (CAN, LIN, ETHERNET) including the required electrical con-

nection(s) for data acquisition.

• Communication with the vehicle´s control units (ECUs), especially with such of the brake system

and/or of the engine and transmission control (power train control system).

• Installation of components for remote data transmission (mobiles, GSM/GPRS modems, WiFi and

Bluetooth components).

4. Before directly or indirectly using the data acquired by an IPETRONIK measurement system to

calibrate control units, please review the data regarding to plausibility.

5. With regard to the application of IPETRONIK products in vehicles during use on public roads the man-
ufacturer and/or registered user of the vehicle has to ensure that all changes/modifications have no
influence concerning the license of the vehicle or its license of operation.

6. User does agree to the instructions and regulations as mentioned above. In case the user does
not agree with the instructions and regulations as mentioned above, he has to notify this expressly and
immediately in writing to IPETRONIK before confirming the sales contract.

Important and general information

1.1.2 Liability, Warranty, Copyright, License agreement

Limitation of liability
Any liability of IPETRONIK, its representatives, agents and the like, especially with regard to personal injury
or damage to property of any kind, shall be excluded (within the legally admissible framework), as far as, the
instructions and warnings, as mentioned below, have not been followed.

Warranty
Products, accessories and services have a 24 months warranty.
All product data, specifications, drawings, etc., correspond to the current condition of the indicated creation
date. For the purpose of optimizing technical processes and production, some details of our modules and
accessory components may be modified at any time without prior notification.
Although the present document has been prepared with the utmost attention to detail, it may not be exempt of
misprints, typing or transcription errors. These errors are not covered by any warranty.

Copyright and Duplication
All rights reserved to IPETRONIK GmbH & Co. KG, in particular those of property, copyright and trademarks.
The rights related to any third party trademarks mentioned in the present document remain unaffected.
This document may not be duplicated, partially or entirely without the prior approval from IPETRONIK GmbH
& Co. KG. All graphics and explanations are copyright protected. Any use beyond the scope of the document
is prohibited.

Software license agreement
This software is property of IPETRONIK GmbH & Co. KG, and is protected by copyright laws.
partial reproduction is strictly forbidden.
A valid software license is required to use the software.

Its total or

IMPORTANT - READ CAREFULLY! THIS IS A LEGAL AGREEMENT BETWEEN YOU, LICENSEE, AND
IPETRONIK GMBH & CO. KG/IPETRONIK INC. ("IPETRONIK"). BY CHECKING “I ACCEPT ALL OF THE
TERMS CONTAINED IN THE ABOVE AGREEMENT” DURING INSTALLATION, COPYING OR USING THIS
PRODUCT IN ANY WAY YOU ACKNOWLEDGE THAT YOU HAVE READ THIS LICENSE AND THAT YOU
UNDERSTAND AND EXPRESSLY AGREE TO BE BOUND BY THE TERMS AND CONDITIONS SET FORTH
BELOW.

1. Definitions

a. SOFTWARE is defined as computer program in object code or machine-readable format, together
with any and all modifications, enhancements, updates, and improvements provided by IPETRONIK
as well as any subsequent versions, corrections, bug fixes, enhancements, updates or other modi-
fications, regardless of the source. The term “Licensed Software” shall not include the source code
version of the Licensed Software.

b. EQUIPMENT is defined as automotive measuring equipment produced by IPETRONIK as well as

other parties.

c. LICENSEE is defined as the recipient of this SOFTWARE and any of its employees, agents or repre-

sentatives.

d. MODIFY or MODIFICATION is defined as change to the SOFTWARE by LICENSEE in order to

customize the SOFTWARE for use solely by LICENSEE.

2. License Terms

a. As long as LICENSEE complies with all terms in this Software License Agreement IPETRONIK grants
LICENSEE a non-exclusive, non-transferable license to load and use the SOFTWARE upon the terms
and conditions set forth below.

b. LICENSEE has the right to load the SOFTWARE for use on any internal computer or piece of EQUIP-

MENT, as long as it is only on one computer or piece of EQUIPMENT at any given time.

c. LICENSEE will notify all of its employees, agents or representatives permitted access to the SOFT-

WARE of the duties and obligations under this Software License Agreement.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

2 / 88

Important and general information

d. LICENSEE has the right to MODIFY the SOFTWARE for use on any internal computer or of EQUIP-

MENT, as long as it is only on one computer or piece of EQUIPMENT at any given time.

e. Any MODIFICATION(S) to the SOFTWARE are subject to the terms and conditions of this Agreement.

f. LICENSEE may not:

i. Loan, rent, lease, give, sublicense, distribute, transmit or otherwise transfer the SOFTWARE, or
otherwise exercise any of IPETRONIK´s legal rights in and to the SOFTWARE, or any deriva-
tive works of the SOFTWARE, in whole or in part, except with the prior written agreement of
IPETRONIK.

ii. Copy, translate, reverse engineer, decompile, disassemble the SOFTWARE, in whole or in part.
iii. Except as provided is Section 2(d), create derivative works based on the SOFTWARE, in whole

or in part.

iv. Remove, modify or cause not to be displayed any copyright or trademark notices, license agree-

ments, or startup messages contained in the programs or documentation.

v. Transmit or otherwise export outside of the Unites States any of the SOFTWARE or technology

in violation of United States or other applicable laws or regulations.

3. Ownership of Intellectual Property

LICENSEE agrees and acknowledges that the SOFTWARE is being provided to it only for use in
EQUIPMENT in the ordinary course of business and that LICENSEE agrees and acknowledges that
IPETRONIK is the owner of all title and proprietary rights in the SOFTWARE, including, without limita-
tion, any and all patents, copyrights, trademarks or any other intellectual property rights associated with
it under the laws of the United States or any jurisdiction throughout the world. No right, title or interest in
the SOFTWARE or any IPETRONIK patent, copyright, trademark, or any other intellectual property right
is transferred to LICENSEE or any other party through this Software License Agreement.

4. Disclaimer of Warranties; Liability Limitations

a. THE SOFTWARE IS PROVIDED TO YOU "AS IS". THERE ARE NO WARRANTIES OF ANY KIND,
WHETHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND COMPATIBILITY, AND TITLE.

b. LICENSEE ASSUMES ALL RISK AS TO THE SELECTION, USE, PERFORMANCE AND QUALITY
OF THE SOFTWARE. IN NO EVENT WILL IPETRONIK OR ANY OTHER PARTY WHO HAS BEEN
INVOLVED IN THE CREATION, PRODUCTION OR DELIVERY OF THE SOFTWARE BE LIABLE
FOR SPECIAL, DIRECT, INDIRECT, INCIDENTAL OR CONSEQUENTIAL DAMAGES, INCLUDING
LOSS OF PROFITS OR INABILITY TO USE THE LICENSED MATERIAL. IN NO EVENT SHALL
IPETRONIK´S LIABILITY FOR ANY DAMAGES OR LOSS TO LICENSEE OR TO ANY THIRD
PARTY EXCEED ANY LICENSE FEE ACTUALLY PAID BY THE LICENSEE TO IPETRONIK FOR
THE SOFTWARE.

c. Since some states or jurisdictions do not permit the exclusion of implied warranties or limitation of
liability for consequential damages, in such states or jurisdictions, the liability is limited to the fullest
extent permitted by law.

5. Intellectual Property Infringement Indemnification

a. IPETRONIK shall defend, indemnify, and hold LICENSEE harmless from and against any claims and
fees (including attorneys´ fees), damage awards arising in connection with a claim that the licensed
SOFTWARE or documentation, when properly used, infringes upon any presently existing, valid and
enforceable United States patent, trademark, or other intellectual property right, provided that:

i. such claim of infringement is not based on any Modification or action taken or suffered by LI-
CENSEE other than the use of the licensed SOFTWARE and documentation in accordance with
the terms and conditions of this agreement;

ii. such claim of infringement is not based on any action by LICENSEE in modifying the SOFTWARE

pursuant to the terms of Section 2(d).

iii. LICENSEE promptly notifies IPETRONIK of such claim in writing at support@ipetronik.com, and

gives IPETRONIK exclusive control over the defense and settlement of such claim;

iv. LICENSEE provides such cooperation and assistance, at IPETRONIK´S expense, as IPETRONIK

may reasonably request to settle or oppose any such claim; and

v. such claim of infringement is based only on the licensed SOFTWARE and documentation as

provided to LICENSEE.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

3 / 88

Important and general information

b. In the event of any infringement claim for which IPETRONIK is liable pursuant to section 5 (a),

IPETRONIK may, at its sole option and expense:

i. procure for LICENSEE the right to continue using the licensed SOFTWARE or documentation;
ii. modify or amend the licensed SOFTWARE or documentation so that it becomes non-infringing;
iii. replace the licensed SOFTWARE or documentation with a non-infringing substitute; or
iv. recover the infringing licensed software and documentation from LICENSEE and repay to LI-
CENSEE all license fees paid to IPETRONIK in connection therewith, less a reasonable amount
based on LICENSEE´s use prior to such recovery and refund.

c. This Article 5 sets forth IPETRONIK´s sole obligations and liability for intellectual property infringe-
ment. These indemnity provisions only apply to the SOFTWARE as originally licensed to LICENSEE
and do not cover any MODIFICATIONS made by LICENSEE or any other third party.

6. Limitation of Liability

a. EXCEPT WITH RESPECT TO ITS INTELLECTUAL PROPERTY INDEMNIFICATION OBLIGA-
TIONS, AS SET FORTH IN ARTICLE 5, IN NO EVENT SHALL IPETRONIK BE LIABLE FOR SPE-
CIAL, INDIRECT OR CONSEQUENTIAL DAMAGES (INCLUDING, WITHOUT LIMITATION, LOST
PROFITS, LOST DATA, OR LOST SAVINGS), EVEN IF IPETRONIK WAS ADVISED OF THE POS-
SIBILITY OF SUCH DAMAGES. FURTHERMORE, IPETRONIK´S LIABILITY (WHETHER IN CON-
TRACT, TORT, OR OTHERWISE) ARISING OUT OF, OR CONNECTED WITH, THIS AGREEMENT
OR THE LICENSED SOFTWARE OR DOCUMENTATION SHALL IN NO CASE EXCEED THE PAY-
MENTS RECEIVED BY IPETRONIK FROM LICENSEE FOR THE LICENSED SOFTWARE AND
DOCUMENTATION.

b. EXCEPT IN CONNECTION WITH ITS OBLIGATIONS UNDER ARTICLE 5:

i. IN NO EVENT SHALL LICENSEE BE LIABLE FOR SPECIAL, INDIRECT OR CONSEQUEN-
TIAL DAMAGES (INCLUDING, WITHOUT LIMITATION, LOST PROFITS, LOST DATA, OR LOST
SAVINGS), EVEN IF LICENSEE WAS ADVISED OF THE POSSIBILITY OF SUCH DAMAGES;
AND

ii. LICENSEE´S LIABILITY (WHETHER IN CONTRACT, TORT, OR OTHERWISE) ARISING OUT
OF, OR CONNECTED WITH, THIS AGREEMENT OR THE LICENSED SOFTWARE OR DOCU-
MENTATION SHALL IN NO CASE EXCEED THE PAYMENTS OWED TO LICENSOR FOR THE
LICENSED SOFTWARE AND DOCUMENTATION.

7. Indemnification Obligations of LICENSEE

a. LICENSEE shall defend, indemnify, and hold IPETRONIK harmless from any claims, losses, ex-
penses, fees (including attorneys´ fees), costs or damages arising in connection with a MODIFICA-
TION or LICENSEE´S unauthorized use of the Licensed Software or Documentation.

8. Merger Clause

a. LICENSEE agrees that this Software License Agreement is the complete and exclusive agreement
between LICENSEE and IPETRONIK governing the SOFTWARE. This Software License Agreement
supersedes and merges all prior agreements with IPETRONIK concerning the SOFTWARE and can
only be modified by a subsequent written agreement signed by IPETRONIK. To the extent that there
is any conflict between this Software License Agreement and any IPETRONIK purchase order or
other written agreement for the purchase of IPETRONIK parts or products, the terms of the purchase
order or written agreement control.

9. General

a. If any provision or portion of a provision of this Software License Agreement is determined to be
invalid or unenforceable, it shall be deemed omitted and the remaining provisions of this Software
License Agreement shall remain in full force and effect to the fullest extent permitted by law.

b. LICENSEE may not assign or transfer all or part of this Software License Agreement to any third party

without the express written approval of IPETRONIK.

c. This Software License Agreement will be governed by the laws of the State of Michigan without regard

to its conflict of laws provisions.

d. All disputes arising out of, or in connection with, the present contract shall be finally settled under the
Rules of Arbitration of the International Chamber of Commerce by one or more arbitrators appointed
in accordance with the said Rules.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

4 / 88

Important and general information

1.2 General information

1.2.1 About this manual

This manual describes the COM interface provided by the software IPEmotionSettings.

1.2.2 Version

This manual has the version number 2026 R1 RC Build 96992, released January 2026 © All rights reserved
!

1.2.3 Support

Headquarter:

IPETRONIK GmbH & Co. KG
Im Rollfeld 28

76532 Baden-Baden, Germany

Phone +49 7221 9922 0
Fax +49 7221 9922 100

info@ipetronik.com
www.ipetronik.com

Limited commercial partnership with its head office in Baden-Baden, registry court Mannheim HRA No.
201313
IPETRONIK Verwaltungs-GmbH Baden-Baden is an individually liable society, registry court Mannheim HRB
No. 202089

CEOs: Dr. Wassiou Sitou, Andreas Wocke

Technical support and product information

www.ipetronik.com
e-mail: support@ipetronik.com

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

5 / 88

Important and general information

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

6 / 88

Chapter 2

IPEmotionSettings

This document describes the COM interfaces of the IPEmotionSettings program.

The IPEmotionSettings program is meant to be used to modify the IPEmotion options.

The program can only be used, while no instance of IPEmotion is running. Only one instance of this program
can be run simultaneously. It will only change the options of the latest installed version of IPEmotion.

To change the IPEmotion options, you need to write a script or program, that uses the COM interface, provided
by the IPEmotionSettings program.

The actual options are loaded at program startup and will be changed only if the interface function SaveSet-
tings() is called.

The IPEmotionSettings program must be terminated by calling the interface function Quit(), before IPEmotion
will be started.

2.1 IPEmotionSettings Interfaces Overview

Namespace IPETRONIK.IPEmotionSettingsISettingsHandlerIPlugInsIUserAccountsIDataPlugInsICloudDrivesIMapProvidersIInstrumentPlugInsIOperationPlugInsIPlugInIReferenceObjectsIPlugInOptionsIReferenceObjectIPlugInOptionIUserAccountIDataPlugInIPlugInOptionsIPlugInOptionICloudDriveIMapProviderIInstrumentPlugInIOperationPlugInIPEmotionSettings

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

8 / 88

Chapter 3

IPEmotionSettings Namespace Index

3.1 IPEmotionSettings Namespace List

The following chapter lists all namespaces with brief descriptions:

IPEmotionSettings (Namespace of the IPEmotion settings interface) . . . . . . . . . . . . . . . . . .

15

IPEmotionSettings Namespace Index

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

10 / 88

Chapter 4

IPEmotionSettings Hierarchical Index

4.1 IPEmotionSettings Interface Hierarchy

This inheritance list is sorted roughly, but not completely, alphabetically:

IInstrumentPlugIns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

ICloudDrive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
ICloudDrives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IDataPlugIn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IDataPlugIns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IDataServiceObservedDirectories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IDataServiceObservedDirectory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IInstrumentPlugIn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

29
31
33
35
36
38
39
InstrumentPlugInProxy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
41
InstrumentPlugInsProxy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
43
44
47
50
51
52
54
55
56
57
58
59
79
81

IMapProvider . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IMapProviders . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
InstrumentPlugInsEnum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IOperationPlugIn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IOperationPlugIns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IPlugIn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IPlugInOption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IPlugInOptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IPlugIns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IReferenceObject . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IReferenceObjects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
ISettingsHandler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IUserAccount . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IUserAccounts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

IPEmotionSettings Hierarchical Index

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

12 / 88

Chapter 5

IPEmotionSettings Interface Index

5.1 IPEmotionSettings Interface List

The following chapter lists all interfaces with brief descriptions:

ICloudDrive (Cloud drive interface) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
ICloudDrives (Cloud drive list interface)
IDataPlugIn (Data plug-in interface)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IDataPlugIns (Data plug-in list interface) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IDataServiceObservedDirectories (Observed directories list interface)
. . . . . . . . . . . . . . . . .
IDataServiceObservedDirectory (Observed directories interface) . . . . . . . . . . . . . . . . . . . .
IInstrumentPlugIn (Instrument plug-in interface) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IInstrumentPlugIns (Instrument plug-in list interface)
. . . . . . . . . . . . . . . . . . . . . . . . . . .
IMapProvider (Map provider interface) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IMapProviders (Map provider list interface)
InstrumentPlugInProxy (Anzeige-PlugIn-Proxy ) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
InstrumentPlugInsEnum (Anzeige-PlugIn-List-Enumerator ) . . . . . . . . . . . . . . . . . . . . . . .
InstrumentPlugInsProxy (Anzeige-PlugIn-Listen-Proxy )
. . . . . . . . . . . . . . . . . . . . . . . . .
IOperationPlugIn (Operation plug-in interface) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IOperationPlugIns (Operation plug-in list interface) . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IPlugIn (Plug-in interface)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IPlugInOption (Plug-in options interface) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IPlugInOptions (Plug-in options list interface)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IPlugIns (Plug-in list interface)
IReferenceObject (Reference object interface)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IReferenceObjects (Reference object list interface) . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . .
ISettingsHandler (IPEmotion settings handler interface)
IUserAccount (User account interface) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
IUserAccounts (User account list interface)

29
31
33
35
36
38
39
41
43
44
45
47
48
50
51
52
54
55
56
57
58
59
79
81

IPEmotionSettings Interface Index

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

14 / 88

Chapter 6

IPEmotionSettings Namespace
Documentation

6.1 IPEmotionSettings Namespace Reference

Namespace of the IPEmotion settings interface.

Interfaces

• interface ICloudDrive

Cloud drive interface.

• interface ICloudDrives

Cloud drive list interface.

• interface IDataPlugIn

Data plug-in interface.

• interface IDataPlugIns

Data plug-in list interface.

• interface IDataServiceObservedDirectory

Observed directories interface.

• interface IDataServiceObservedDirectories

Observed directories list interface.

• interface IInstrumentPlugIn

Instrument plug-in interface.

• interface IInstrumentPlugIns

Instrument plug-in list interface.

• interface IMapProvider

Map provider interface.

• interface IMapProviders

Map provider list interface.

• class InstrumentPlugInProxy

IPEmotionSettings Namespace Documentation

Anzeige-PlugIn-Proxy.

• class InstrumentPlugInsProxy

Anzeige-PlugIn-Listen-Proxy.

• class InstrumentPlugInsEnum

Anzeige-PlugIn-List-Enumerator.

• interface IOperationPlugIn

Operation plug-in interface.

• interface IOperationPlugIns

Operation plug-in list interface.

• interface IPlugIn

Plug-in interface.

• interface IPlugIns

Plug-in list interface.

• interface IPlugInOption

Plug-in options interface.

• interface IPlugInOptions

Plug-in options list interface.

• interface IReferenceObject

Reference object interface.

• interface IReferenceObjects

Reference object list interface.

• interface ISettingsHandler

IPEmotion settings handler interface.

• interface IUserAccount

User account interface.

• interface IUserAccounts

User account list interface.

Enumerations

• enum SupportedViewType

Enumeration of all view types that can be supported by display instrument plug-ins.

• enum ConfigurationPriority

Enumeration of available usage priorities.

• enum HardwareDetectionAction

Enumeration of available actions to be performed after the automatic hardware detection.

• enum SignalConfigurationMode

Enumeration of available configuration modes.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

16 / 88

IPEmotionSettings Namespace Documentation

• enum PhysicalDimensionTypes

Enumeration of supported physical dimension types.

• enum UiCommand

Enumeration of available shortcut commands.

• enum TimeZoneDisplayType

Enumeration of supported time zones used to diaplay absolute times in the analysis.

• enum SelectedPlotHighlightType

Enumeration of supported highlightning types used to highlight selected curves in yt-charts.

• enum CharacteristicSupport

Enumeration of available characteristic support types.

• enum MapImagerySource

Enumeration of supported sources of map imagery.

• enum AnalysisDiagramAbsoluteTimeFormat

Enumeration of supported absolute time axis modes in the analysis.

• enum DataTreeDisplayMode

Enumeration of supported data tree display styles.

• enum ThermocoupleColorCoding

Enumeration of supported color coding of thermocouples.

• enum UserLevel

Enumeration of available access levels.

6.1.1 Detailed Description

Namespace of the IPEmotion settings interface.

6.1.2 Enumeration Type Documentation

6.1.2.1 enum SupportedViewType

Enumeration of all view types that can be supported by display instrument plug-ins.

Remarks:

The following enumeration values are available:

• 1: OnlineView Instrument plug-in contains only online instruments

• 2: AnalysisView Instrument plug-in contains only analysis instruments

• 3: OnlineAndAnalysisView Instrument plug-in contains online and analysis instruments

6.1.2.2 enum ConfigurationPriority

Enumeration of available usage priorities.

Remarks:

The following enumeration values are available:

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

17 / 88

IPEmotionSettings Namespace Documentation

• 0: High - Use this setting for your preferred hardware

• 1: Standard - The default setting

• 2: Low - Use this for hardware you own but don’t want to be used

• 3: NotUsed - Removes this type of hardware from the list of available hardware

6.1.2.3 enum HardwareDetectionAction

Enumeration of available actions to be performed after the automatic hardware detection.

Remarks:

The following enumeration values are available:

• 0: ACTION_USER_GUIDANCE - Guided configuration

• 1: ACTION_AUTO_CONFIGURATION - Automatic creation of a default configuration

• 2: ACTION_MANUAL_CONFIGURATION - Manual configuration

6.1.2.4 enum SignalConfigurationMode

Enumeration of available configuration modes.

Remarks:

The following enumeration values are available:

• 0: CONFIGURATION_MODE_HARDWARE - Hardware centric configuration

• 1: CONFIGURATION_MODE_MEASURE_POINT - Configuration based on a measurement point plan

6.1.2.5 enum PhysicalDimensionTypes

Enumeration of supported physical dimension types.

Remarks:

The following enumeration values are available:

• 0: NONE - Used for values without a physical dimension

• 1: Length

• 2: Mass

• 3: Time

• 4: Current

• 5: Temperature

• 6: MolarAmount

• 7: LuminousIntensity

• 8: Voltage

• 9: Resistance

• 10: Frequency

• 11: Force

• 12: Energy

• 13: Power

• 14: Pressure

• 15: Speed

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

18 / 88

IPEmotionSettings Namespace Documentation

• 16: Rpm

• 17: MassFlowRate

• 18: Angle

• 19: Strain

• 20: BaudeRate

• 21: Percent

• 22: ByteSpace

• 23: Acceleration

• 24: Torque

• 25: VolumetricFlowRate

• 26: SpecificEnthalpy

• 27: EnergyFluxDensity

• 28: BridgeDetuning

• 29: Density

• 30: RelativeHumidity

• 31: FrameRate

• 32: TransferRate

6.1.2.6 enum UiCommand

Enumeration of available shortcut commands.

Remarks:

The following enumeration values are available:

• 0: COMMAND_FILE_NEW

• 1: COMMAND_FILE_SAVE

• 2: COMMAND_FILE_SAVE_AS

• 3: COMMAND_FILE_OPEN

• 4: COMMAND_PRINT

• 5: COMMAND_EDIT_CUT

• 6: COMMAND_EDIT_COPY

• 7: COMMAND_EDIT_PASTE

• 8: COMMAND_EDIT_UNDO

• 9: COMMAND_EDIT_REDO

• 10: COMMAND_SCRIPTING_NEW_SCRIPT

• 11: COMMAND_SCRIPTING_IMPORT

• 12: COMMAND_ABOUT

• 13: COMMAND_NEW_SCRIPT_GROUP

• 14: COMMAND_PRINT_ONCE

• 15: COMMAND_PRINT_AS_PDF

• 16: COMMAND_PRINT_PREVIEW

• 17: COMMAND_CREATE_RUNTIME_VERSION

• 18: COMMAND_PRINT_EXPORT_EXCEL

• 19: COMMAND_PRINT_EXPORT_HTML

• 20: COMMAND_PRINT_EXPORT_RTF

• 21: COMMAND_PRINT_EXPORT_IMAGE

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

19 / 88

IPEmotionSettings Namespace Documentation

• 22: COMMAND_PRINT_EXPORTV

• 23: COMMAND_SHOW_MESSAGE_WINDOW

• 24: COMMAND_RESET_USER_SETTINGS

• 25: COMMAND_SHOW_OPTIONS_DIALOG

• 26: COMMAND_CREATE_SUPPORT_FILE

• 27: COMMAND_QUIT_PROGRAM

• 28: COMMAND_EDIT_DELETE

• 29: COMMAND_EDIT_CLEAR

• 30: COMMAND_SHOW_ITEM_PROPERTIES

• 31: COMMAND_SHOW_HELP

• 32: COMMAND_BUILD_CONFIGURATION

• 33: COMMAND_USE_USER_GUIDE

• 34: COMMAND_ADJUST_WITH_SENSORDATABASE

• 35: COMMAND_DETECT_HARDWARE

• 36: COMMAND_INIT_HARDWARE

• 37: COMMAND_RESET_HARDWARE

• 38: COMMAND_SYNC_HARDWARE

• 39: COMMAND_SHOW_HARDWARE_DETAILS

• 40: COMMAND_ADD_CALCULATION

• 41: COMMAND_ADD_STORAGE_GROUP

• 42: COMMAND_ADD_LIMIT

• 43: COMMAND_SHOW_AQUISITION_DETAILS

• 44: COMMAND_START_AQUISITION

• 45: COMMAND_START_RECORD_DATA

• 46: COMMAND_PAUSE_AQUISITION

• 47: COMMAND_ONLINEVIEW_ADD_SCREEN

• 48: COMMAND_ONLINEVIEW_ADD_GROUP

• 49: COMMAND_ONLINEVIEW_LAYOUT_FIXED

• 50: COMMAND_ONLINEVIEW_LAYOUT_FREE

• 51: COMMAND_ONLINEVIEW_LAYOUT_1_1

• 52: COMMAND_ONLINEVIEW_LAYOUT_2_1

• 53: COMMAND_ONLINEVIEW_LAYOUT_3_1

• 54: COMMAND_ONLINEVIEW_LAYOUT_2_2_1

• 55: COMMAND_SHOW_SCREEN_LIST

• 56: COMMAND_ONLINEVIEW_ADD_TRACKING_DIAGRAM

• 57: COMMAND_ONLINEVIEW_ADD_XY_DIAGRAM

• 58: COMMAND_ONLINEVIEW_ADD_YT_OSCILOSCOPE

• 59: COMMAND_ONLINEVIEW_ADD_ALPHANUMERIC_DISPLAY

• 60: COMMAND_ONLINEVIEW_ADD_BAR_INSTRUMENT

• 61: COMMAND_ONLINEVIEW_ADD_TACHO_INSTRUMENT

• 62: COMMAND_ONLINEVIEW_ADD_POINTER_INSTRUMENT

• 63: COMMAND_ONLINEVIEW_ADD_SLIDER_INSTRUMENT

• 64: COMMAND_ONLINEVIEW_ADD_DIGITAL_INSTRUMENT

• 65: COMMAND_ONLINEVIEW_ADD_SWITCH_INSTRUMENT

• 66: COMMAND_ONLINEVIEW_ADD_VIDEO_DISPLAY

• 67: COMMAND_LOAD_DATA_FILE

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

20 / 88

IPEmotionSettings Namespace Documentation

• 68: COMMAND_CLEAR_DATA_POOL

• 69: COMMAND_EXPORT_DATA_FILE

• 70: COMMAND_ANALYZE_IN_EXCEL

• 71: COMMAND_SHOW_DATA_FILES

• 72: COMMAND_ANALYSIS_ADD_SCREEN

• 73: COMMAND_ANALYSIS_ADD_GROUP

• 74: COMMAND_ANALYSIS_LAYOUT_FIXED

• 75: COMMAND_ANALYSIS_LAYOUT_FREE

• 76: COMMAND_ANALYSIS_LAYOUT_1_1

• 77: COMMAND_ANALYSIS_LAYOUT_2_1

• 78: COMMAND_ANALYSIS_LAYOUT_3_1

• 79: COMMAND_ANALYSIS_LAYOUT_2_2_1

• 80: COMMAND_ANALYSIS_ADD_LINE_DIAGRAM

• 81: COMMAND_ANALYSIS_ADD_VIDEO_DISPLAY

• 82: COMMAND_ANALYSIS_ZOOM_TYPE_PANNING

• 83: COMMAND_ANALYSIS_ZOOM_TYPE_STRETCHING

• 84: COMMAND_ANALYSIS_ZOOM_TYPE_RUBBERBAND

• 85: COMMAND_ANALYSIS_ZOOM_UNDO

• 86: COMMAND_ANALYSIS_SYNCHRONIZED_ZOOM

• 87: COMMAND_ANALYSIS_OPTIMAL_RANGE

• 88: COMMAND_ANALYSIS_ORIGINAL_RANGE

• 89: COMMAND_ANALYSIS_FIRST_CURSOR

• 90: COMMAND_ANALYSIS_SECOND_CURSOR

• 91: COMMAND_ANALYSIS_START_REPLAY

• 92: COMMAND_ANALYSIS_STOP_REPLAY

• 93: COMMAND_ANALYSIS_SHOW_DATA_FILES

• 94: COMMAND_SCRIPTING_EXPORT

• 95: COMMAND_SCRIPTING_START_RECORDING

• 96: COMMAND_SCRIPTING_STOP_RECORDING

• 97: COMMAND_SCRIPTING_SHOW_SCRIPT_LIBRARY

• 98: COMMAND_SCRIPTING_SHOW_SCRIPT_DETAILS

• 99: COMMAND_ADD_FFT

• 100: COMMAND_ADD_VARIABLE_DOUBLE

• 101: COMMAND_ADD_VARIABLE_STATUS

• 102: COMMAND_ADD_VARIABLE_TEXT

• 103: COMMAND_ADD_FUNCTION_GENERATOR_FILE

• 104: COMMAND_ADD_FUNCTION_GENERATOR_RAMP

• 105: COMMAND_ADD_FUNCTION_GENERATOR_RECTANGLE

• 106: COMMAND_ADD_FUNCTION_GENERATOR_SAWTOOTH

• 107: COMMAND_ADD_FUNCTION_GENERATOR_SINE

• 108: COMMAND_ADD_PID_CONTROLLER

• 109: COMMAND_ONLINEVIEW_ADD_FFT_OSCILOSCOPE

• 110: COMMAND_ONLINEVIEW_ADD_BUTTON

• 111: COMMAND_ANALYSIS_ADD_XY_DIAGRAM

• 112: COMMAND_ONLINEVIEW_ADD_LOG_PH_DIAGRAM

• 113: COMMAND_ANALYSIS_ADD_LOG_PH_DIAGRAM

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

21 / 88

IPEmotionSettings Namespace Documentation

• 114: COMMAND_FULLSCREEN_MODE

• 115: COMMAND_PRINT_REPORT

• 116: COMMAND_PRINT_REPORT_ONCE

• 117: COMMAND_EXPORT_REPORT_AS_PDF

• 118: COMMAND_EXPORT_REPORT_AS_HTML

• 119: COMMAND_EXPORT_REPORT_AS_IMAGE

• 120: COMMAND_EXPORT_REPORT_AS_EXCEL

• 121: COMMAND_ZOOM_REPORT_800

• 122: COMMAND_ZOOM_REPORT_400

• 123: COMMAND_ZOOM_REPORT_300

• 124: COMMAND_ZOOM_REPORT_200

• 125: COMMAND_ZOOM_REPORT_150

• 126: COMMAND_ZOOM_REPORT_100

• 127: COMMAND_ZOOM_REPORT_50

• 128: COMMAND_ADD_REPORT_ELEMENT_ARROW

• 129: COMMAND_ADD_REPORT_ELEMENT_LINE

• 130: COMMAND_ADD_REPORT_ELEMENT_PICTURE

• 131: COMMAND_ADD_REPORT_ELEMENT_TEXT

• 132: COMMAND_ADD_REPORT_ELEMENT_RICH_TEXT

• 133: COMMAND_CHECK_CONFIGURATION

• 134: COMMAND_MAP_HARDWARE

• 135: COMMAND_ADD_RANGE

• 136: COMMAND_ADD_SEQUENCE_CONTROL

• 137: COMMAND_ADD_SEQUENCE_CONTROL_BLOCK

• 138: COMMAND_ADJUST_WITH_TEDS

• 139: COMMAND_ADJUST_OFFSETS

• 140: COMMAND_REPORTING_ELEMENT_LINE_BACK

• 141: COMMAND_REPORTING_ELEMENT_LINE_VERT

• 142: COMMAND_REPORTING_ELEMENT_LINE_HORZ

• 143: COMMAND_REPORTING_ELEMENT_ELLIPSE

• 144: COMMAND_REPORTING_ELEMENT_RECTANGLE

• 145: COMMAND_REPORTING_LAYOUT_DESIGNER

• 146: COMMAND_REPORTING_ZOOM_WHOLE_PAGE

• 147: COMMAND_COMPARE_CONFIGURATIONS

• 148: COMMAND_SHOW_HARDWARE_STATUS_WINDOW

• 149: COMMAND_SHOW_PC_STATUS_WINDOW

• 150: COMMAND_SHOW_STORAGE_STATUS_WINDOW

• 151: COMMAND_SHOW_OUTPUT_WINDOW

• 152: COMMAND_RESET_TEMPLATES

• 153: COMMAND_RESET_FORMULA_POOL

• 154: COMMAND_LOGIN

• 155: COMMAND_LOGOUT

• 156: COMMAND_SIGNALS_SHUNT_CHECK

• 157: COMMAND_MEASUREMENT_ADD_CLASSIFICATION_SAMPLE_COUNT

• 158: COMMAND_MEASUREMENT_ADD_CLASSIFICATION_TIME_AT_LEVEL

• 159: COMMAND_MEASUREMENT_ADD_CLASSIFICATION_FROM_TO_COUNT

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

22 / 88

IPEmotionSettings Namespace Documentation

• 160: COMMAND_MEASUREMENT_ADD_CLASSIFICATION_LEVEL_CROSSING

• 161: COMMAND_MEASUREMENT_ADD_CLASSIFICATION_TRANSITION_MATRIX

• 162: COMMAND_MEASUREMENT_ADD_CLASSIFICATION_RAINFLOW

• 163: COMMAND_MEASUREMENT_ADD_CLASSIFICATION_SAMPLE_COUNT_COMPOUND

• 164: COMMAND_MEASUREMENT_ADD_CLASSIFICATION_TIME_AT_LEVEL_COMPOUND

• 165: COMMAND_MEASUREMENT_ADD_ROUTER

• 166: COMMAND_ONLINEVIEW_ADD_HISTOGRAM

• 167: COMMAND_ONLINEVIEW_ADD_TABLE

• 168: COMMAND_ONLINEVIEW_ADD_MAP

• 169: COMMAND_ANALYSIS_ADD_MAP

• 170: COMMAND_REPORTING_ADD_ARROW_BACK

• 171: COMMAND_REPORTING_ADD_ARROW_HORIZONTAL

• 172: COMMAND_REPORTING_ADD_ARROW_VERTICAL

• 173: COMMAND_REPORTING_ADD_ARROW_START

• 174: COMMAND_REPORTING_ADD_ARROW_BACK_START

• 175: COMMAND_REPORTING_ADD_ARROW_VERTICAL_START

• 176: COMMAND_REPORTING_ADD_ARROW_HORIZONTAL_START

• 177: COMMAND_REPORTING_ADD_TABLE

• 178: COMMAND_EDIT_PASTE_BEHIND

• 179: COMMAND_EDIT_COPY_TO_FILE

• 180: COMMAND_EDIT_PASTE_FROM_FILE

• 181: COMMAND_GENERAL_IMPORT_WORKING_ENVIRONMENT

• 182: COMMAND_GENERAL_EXPORT_WORKING_ENVIRONMENT

• 183: COMMAND_MEASUREMENT_ADD_SCALING

• 184: COMMAND_ANALYSIS_CURSORS_FREE

• 185: COMMAND_GENERAL_RESET_OBJECT_POOL

• 186: COMMAND_GENERAL_EMPTY_MAP_CACHE

• 187: COMMAND_ANALYSIS_OPTIMAL_X_RANGE

• 188: COMMAND_ONLINEVIEW_ADD_TRAFFIC_ANALYSER

• 189: COMMAND_ONLINEVIEW_ADD_CHANNEL_TABLE

• 191: COMMAND_MEASUREMENT_ADD_TRAFFIC_SIMULATION

• 192: COMMAND_ANALYSIS_ADD_BUTTON

• 193: COMMAND_DATA_MANAGER_FILES_DETAILED_EXPORT

• 194: COMMAND_DATA_MANAGER_ADD_SEQUENCE

• 195: COMMAND_DATA_MANAGER_ADD_FORMULA

• 196: COMMAND_DATA_MANAGER_ADD_FORMULA_FROM_POOL

• 197: COMMAND_DATA_MANAGER_ADD_FFT

• 198: COMMAND_DATA_MANAGER_ADD_CLASSIFICATION_SAMPLE_COUNT

• 199: COMMAND_DATA_MANAGER_ADD_CLASSIFICATION_TIME_AT_LEVEL

• 200: COMMAND_DATA_MANAGER_ADD_CLASSIFICATION_LEVEL_CROSSING

• 201: COMMAND_DATA_MANAGER_ADD_FILTER_LOW_PASS

• 202: COMMAND_DATA_MANAGER_ADD_FILTER_HIGH_PASS

• 203: COMMAND_DATA_MANAGER_ADD_FILTER_BAND_PASS

• 204: COMMAND_DATA_MANAGER_ADD_FILTER_BAND_STOP

• 205: COMMAND_DATA_MANAGER_ADD_SEGMENT

• 206: COMMAND_DATA_MANAGER_ADD_SCRIPT

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

23 / 88

IPEmotionSettings Namespace Documentation

• 207: COMMAND_ANALYSIS_ADD_HISTOGRAM

• 208: COMMAND_ANALYSIS_ADD_ALPHANUMERIC_DISPLAY

• 209: COMMAND_ANALYSIS_ADD_TRAFFIC_ANALYSER

• 210: COMMAND_ANALYSIS_ADD_TABLE

• 212: COMMAND_ONLINEVIEW_ADD_TRAFFIC_GENERATOR

• 213: COMMAND_ANALYSIS_OPERATION_ADD_SEGMENT_BY_INDEX

• 214: COMMAND_ANALYSIS_OPERATION_ADD_SEGMENT_BY_TIME

• 215: COMMAND_ANALYSIS_OPERATION_FIND_INDEX_OF_CONDITION

• 216: COMMAND_ANALYSIS_OPERATION_FIND_TIME_OF_CONDITION

• 217: COMMAND_ANALYSIS_OPERATION_ADD_STATISTIC

• 218: COMMAND_ANALYSIS_ADD_3D_VIEW

• 219: COMMAND_DATA_MANAGER_OPERATION_ADD_CLASSIFICATION_FROM_TO_COUNT

• 220: COMMAND_DATA_MANAGER_OPERATION_ADD_CLASSIFICATION_TRANSITION_MATRIX

• 221: COMMAND_DATA_MANAGER_OPERATION_ADD_CLASSIFICATION_RAINFLOW

• 222: COMMAND_DATA_MANAGER_OPERATION_ADD_CLASSIFICATION_COMPOUND_SAMPLE_COUNT

• 223: COMMAND_DATA_MANAGER_OPERATION_ADD_CLASSIFICATION_COMPOUND_TIME_AT_LEVEL

• 224: COMMAND_ANALYSIS_ADD_POLAR_DIAGAM

• 225: COMMAND_ANALYSIS_ADD_CLASSIFICATION_TABLE

• 226: COMMAND_ANALYSIS_ADD_CAMPBELL_DIAGRAM

• 227: COMMAND_ANALYSIS_ADD_CLASSIFICATION_GRID

• 228: COMMAND_DATA_MANAGER_OPERATION_ADD_CAMPBELL

• 229: COMMAND_ANALYSIS_AXIS_SYNC_DISABLED

• 230: COMMAND_ANALYSIS_AXIS_SYNC_BY_TIME

• 231: COMMAND_ANALYSIS_AXIS_SYNC_MULTI

• 232: COMMAND_ONLINEVIEW_ADD_PROFILE_DIAGRAM

• 233: COMMAND_MEASUREMENT_ADD_PROFILE

• 234: COMMAND_ANALYSIS_OPTIMAL_Z_RANGE

• 235: COMMAND_ONLINEVIEW_ADD_PROFILE_DIAGRAM_FROM_FILE

• 236: COMMAND_DATA_MANAGER_OPERATION_ADD_OVERALL_LEVEL

• 237: COMMAND_DATA_MANAGER_OPERATION_ADD_ORDER_FILTER

• 238: COMMAND_ADD_CIRCULAR_STORAGE_GROUP

• 239: COMMAND_DATA_MANAGER_FILES_DATABASE_SEARCH

• 240: COMMAND_MEASUREMENT_ADD_XCP_SLAVE

• 241: COMMAND_GENERAL_RESET_PERSISTENT_DATA

• 242: COMMAND_DATA_MANAGER_FILES_CONVERSION

• 243: COMMAND_COMMAND_MEASUREMENT_ADD_CAN_SEND

• 244: COMMAND_COMMAND_MEASUREMENT_ADD_MAIL_GROUP

• 245: COMMAND_SUB_CONFIG_CREATE

• 246: COMMAND_SUB_CONFIGR_REMOVE

• 247: COMMAND_SUB_CONFIG_OPTIONS

• 248: COMMAND_SUB_CONFIG_ENCRYPT

• 249: COMMAND_SUB_CONFIG_DECRYPT

• 250: COMMAND_COMMAND_MEASUREMENT_ADD_STATISTIC_GROUP

• 251: COMMAND_RUN_SHUNT_CHECK

• 252: COMMAND_TEST_AQUISITION

• 253: COMMAND_RESET_DEVICES

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

24 / 88

IPEmotionSettings Namespace Documentation

• 254: COMMAND_ADD_HV_OPERATION
• 255: COMMAND_GENERAL_APP_A2L_TO_ARXML
• 256: COMMAND_DATA_MANAGER_DECRYPT_FILES
• 257: COMMAND_ONLINEVIEW_LAYOUT_4_1
• 258: COMMAND_ONLINEVIEW_LAYOUT_5_1
• 259: COMMAND_ANALYSIS_LAYOUT_4_1
• 260: COMMAND_ANALYSIS_LAYOUT_5_1

The following commands need a parameter:

• 666666: COMMAND_SCRIPTING_RUN_SCRIPT
• 666667: COMMAND_SHOW_SCREEN
• 666668: COMMAND_USER_BUTTON
• 666669: COMMAND_ANALYSIS_SHOW_SCREEN
• 666670: COMMAND_MARKER
• 666671: COMMAND_ONLINE_CONTROL_SWITCH
• 666672: COMMAND_ONLINE_CONTROL_ACTION_BUTTON
• 666673: COMMAND_ANALYSIS_CONTROL_ACTION_BUTTON
• 666674: COMMAND_CUSTOM_PAGE_BUTTON
• 666675: COMMAND_RUN_OFFSET_ADJUST

6.1.2.7 enum TimeZoneDisplayType

Enumeration of supported time zones used to diaplay absolute times in the analysis.

Remarks:

The following enumeration values are available:

• 0: Utc - UTC
• 1: Local - local time zone of the analysis PC
• 2: Source - local time zone of the measurement file

6.1.2.8 enum SelectedPlotHighlightType

Enumeration of supported highlightning types used to highlight selected curves in yt-charts.

Remarks:

The following enumeration values are available:

• 0: NoHighlightning - no highlightning
• 1: Bold - the curve is drawn with an increased line width
• 2: Flash - the seelcted curve is flashing

6.1.2.9 enum CharacteristicSupport

Enumeration of available characteristic support types.

Remarks:

The following enumeration values are available:

• 0: AsCharacteristic - import as characteristic
• 1: AsMeasurement - conversion to measurement
• 2: Ignore - no import at all

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

25 / 88

IPEmotionSettings Namespace Documentation

6.1.2.10 enum MapImagerySource

Enumeration of supported sources of map imagery.

Remarks:

The following enumeration values are available:

• 0x00010001: InternalCacheWithInternet - Tiles are retrieved from the internal cache if contained
within, otherwise loaded from the internet. Tiles loaded from the internet are stored in the cache.

• 0x00020001: LocalDatabaseWithInternet - Tiles are retrieved from the specified local database if
contained within, otherwise loaded from the internet. Tiles loaded from the internet are not stored.

• 0x00020000: LocalDatabase - Tiles are retrieved from the specified local database only. Map re-

gions requiring imagery which is not contained in the database are not displayed.

6.1.2.11 enum AnalysisDiagramAbsoluteTimeFormat

Enumeration of supported absolute time axis modes in the analysis.

Remarks:

The following enumeration values are available:

• 0: TimeOrDate - time axis with time or date

• 1: TimeWithDate - time axis with time and date

• 2: TimeWithDateAndYear - time axis with time, date and year.

6.1.2.12 enum DataTreeDisplayMode

Enumeration of supported data tree display styles.

Remarks:

The following enumeration values are available:

• 0: Legacy - display in the same way as in IPEmotion 2019R1 and earlier

• 1: FileGroupSignal - grouped by file, group and signal, where files are only available when the

measurement file supports groups

• 2: NoGroups - grouped by file and signal, groups are not displayed

6.1.2.13 enum ThermocoupleColorCoding

Enumeration of supported color coding of thermocouples.

Remarks:

The following enumeration values are available:

• 0: Iec - displays color of thermocouple information in IEC 584-3 code

• 1: Ansi - displays color of thermocouple information in ANSI MC 96.1 code

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

26 / 88

IPEmotionSettings Namespace Documentation

6.1.2.14 enum UserLevel

Enumeration of available access levels.

Remarks:

The following enumeration values are available:

• 1: Level1 - Access level with the least privileges

• 2: Level2

• 3: Level3 - Access level with the highest privileges

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

27 / 88

IPEmotionSettings Namespace Documentation

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

28 / 88

Chapter 7

IPEmotionSettings Interface
Documentation

7.1 ICloudDrive Interface Reference

Cloud drive interface.

Properties

• string Name [get, set]

Returns or sets the name of the cloud drive.

• string Url [get, set]

Returns or sets the URL of the cloud drive.

• string LoginName [get, set]

Returns or sets the login name needed to access the cloud drive.

• string Password [get, set]

Returns or sets the password.

• bool Active [get, set]

Specifies whether the cloud drive will be connected.

• string MappedDrive [get, set]

Returns or sets the drive letter that should be assigned to the cloud drive.

7.1.1 Detailed Description

Cloud drive interface.

7.1.2 Property Documentation

7.1.2.1 string Name [get, set]

Returns or sets the name of the cloud drive.

The name should be unique.

IPEmotionSettings Interface Documentation

7.1.2.2 string Url [get, set]

Returns or sets the URL of the cloud drive.

7.1.2.3 string LoginName [get, set]

Returns or sets the login name needed to access the cloud drive.

7.1.2.4 string Password [get, set]

Returns or sets the password.

7.1.2.5 bool Active [get, set]

Specifies whether the cloud drive will be connected.

7.1.2.6 string MappedDrive [get, set]

Returns or sets the drive letter that should be assigned to the cloud drive.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

30 / 88

IPEmotionSettings Interface Documentation

7.2 ICloudDrives Interface Reference

Cloud drive list interface.

Public Member Functions

• IEnumerator GetEnumerator ()

Enumerator for the cloud drives list.

• ICloudDrive AddCloudDrive (string nameOfCloudDrive, string url, string loginName, string password,

bool activate, string driveLetter)

Adds a new cloud drive to the cloud drives list.

• void RemoveCloudDrive (ICloudDrive cloudDriveToRemove)

Removes a cloud drive from the cloud drives list.

Properties

• int Count [get]

Count of cloud drives in this list.

• ICloudDrive Item [int index] [get]

Returns the cloud drive with the given (zero based) index from this list.

7.2.1 Detailed Description

Cloud drive list interface.

7.2.2 Member Function Documentation

7.2.2.1 IEnumerator GetEnumerator ()

Enumerator for the cloud drives list.

Returns:

Interface of the cloud drives list enumerator

7.2.2.2 ICloudDrive AddCloudDrive (string nameOfCloudDrive, string url, string loginName, string

password, bool activate, string driveLetter)

Adds a new cloud drive to the cloud drives list.

Parameters:

nameOfCloudDrive Name of the new cloud drive.

url URL of the new cloud drive.

loginName Log-in name of the new cloud drive.

password Password of the new cloud drive.

activate Connect cloud drive.
IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

31 / 88

IPEmotionSettings Interface Documentation

driveLetter Drive letter that should be assigned to the cloud drive.

The name, the URL and the log-in name are required parameters.

Using an empty password is not recommended.

In case the drive letter is not specified the operating system will choose a drive letter when connecting the
cloud drive.

Returns:

Interface of the new cloud drive

7.2.2.3 void RemoveCloudDrive (ICloudDrive cloudDriveToRemove)

Removes a cloud drive from the cloud drives list.

Parameters:

cloudDriveToRemove Interface of the cloud drive to be removed from the list.

7.2.3 Property Documentation

7.2.3.1 int Count [get]

Count of cloud drives in this list.

7.2.3.2 ICloudDrive Item[int index] [get]

Returns the cloud drive with the given (zero based) index from this list.

Parameters:

index Index of the cloud drive in this list.

Returns:

Interface of the cloud drive.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

32 / 88

IPEmotionSettings Interface Documentation

7.3 IDataPlugIn Interface Reference

Data plug-in interface.

Public Member Functions

• object GetOptionValue (string optionName)

Returns the value assigned to the named data plug-in option.

• void SetOptionValue (string optionName, object valueToSet)

Sets the value of the named data plug-in option.

Properties

• string FormatId [get]

Returns the data plug-in format identifier.

• IPlugInOptions Options [get]

Returns the options list of the data plug-in.

7.3.1 Detailed Description

Data plug-in interface.

7.3.2 Member Function Documentation

7.3.2.1 object GetOptionValue (string optionName)

Returns the value assigned to the named data plug-in option.

Parameters:

optionName Name of the data plug-in option.

7.3.2.2 void SetOptionValue (string optionName, object valueToSet)

Sets the value of the named data plug-in option.

Parameters:

optionName Name of the data plug-in option

valueToSet Value to be set for the named data plug-in option.

7.3.3 Property Documentation

7.3.3.1 string FormatId [get]

Returns the data plug-in format identifier.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

33 / 88

IPEmotionSettings Interface Documentation

7.3.3.2 IPlugInOptions Options [get]

Returns the options list of the data plug-in.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

34 / 88

IPEmotionSettings Interface Documentation

7.4 IDataPlugIns Interface Reference

Data plug-in list interface.

Public Member Functions

• IEnumerator GetEnumerator ()

Enumerator for the data plug-in list.

Properties

• int Count [get]

Count of data plug-ins in this list.

• IDataPlugIn Item [int index] [get]

Returns the data plug-in with the given (zero based) index from this list.

7.4.1 Detailed Description

Data plug-in list interface.

7.4.2 Member Function Documentation

7.4.2.1 IEnumerator GetEnumerator ()

Enumerator for the data plug-in list.

Returns:

Interface of the data plug-in list enumerator.

7.4.3 Property Documentation

7.4.3.1 int Count [get]

Count of data plug-ins in this list.

7.4.3.2 IDataPlugIn Item[int index] [get]

Returns the data plug-in with the given (zero based) index from this list.

Parameters:

index Index of the data plug-in in this list.

Returns:

Interface of the data plug-in.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

35 / 88

IPEmotionSettings Interface Documentation

7.5 IDataServiceObservedDirectories Interface Reference

Observed directories list interface.

Public Member Functions

• IEnumerator GetEnumerator ()

Enumerator for the observed directories list.

• IDataServiceObservedDirectory AddDirectory (string nameOfDirectory, bool activateObservation, string

fullPathOfDirectory, bool includeAllSubdirectories)

Adds a new observed directory to the list.

• void RemoveDirectory (IDataServiceObservedDirectory observedDirectoryToRemove)

Removes an observed directory from the list.

Properties

• int Count [get]

Count of observed directories in this list.

• IDataServiceObservedDirectory Item [int index] [get]

Returns the observed directory with the given (zero based) index from this list.

7.5.1 Detailed Description

Observed directories list interface.

7.5.2 Member Function Documentation

7.5.2.1 IEnumerator GetEnumerator ()

Enumerator for the observed directories list.

Returns:

Interface of the observed directories list enumerator

7.5.2.2 IDataServiceObservedDirectory AddDirectory (string nameOfDirectory, bool

activateObservation, string fullPathOfDirectory, bool includeAllSubdirectories)

Adds a new observed directory to the list.

Parameters:

nameOfDirectory Name of new the observed directory.

activateObservation Activate observation.

fullPathOfDirectory Complete path of the new observed directory.

includeAllSubdirectories Enable observation of subdirectories.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

36 / 88

IPEmotionSettings Interface Documentation

The path is a required parameter. It can be local or UNC.

Name of the directory is not recommended. It should help to differ between the directories.

Returns:

Interface of the new observed directory

7.5.2.3 void RemoveDirectory (IDataServiceObservedDirectory observedDirectoryToRemove)

Removes an observed directory from the list.

Parameters:

observedDirectoryToRemove Interface of the observed directory to be removed from the list.

7.5.3 Property Documentation

7.5.3.1 int Count [get]

Count of observed directories in this list.

7.5.3.2 IDataServiceObservedDirectory Item[int index] [get]

Returns the observed directory with the given (zero based) index from this list.

Parameters:

index Index of the observed directories in this list.

Returns:

Interface of the observed directory.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

37 / 88

IPEmotionSettings Interface Documentation

7.6 IDataServiceObservedDirectory Interface Reference

Observed directories interface.

Properties

• string Name [get, set]

Returns or sets the name of the observed directory.

• bool Active [get, set]

Returns or sets whether the directory will be observed.

• string Path [get, set]

Returns or sets the path of the directory.

• bool IncludeSubdirectories [get, set]

Returns or sets whether subdirectories will be included.

7.6.1 Detailed Description

Observed directories interface.

7.6.2 Property Documentation

7.6.2.1 string Name [get, set]

Returns or sets the name of the observed directory.

The name should be unique.

7.6.2.2 bool Active [get, set]

Returns or sets whether the directory will be observed.

7.6.2.3 string Path [get, set]

Returns or sets the path of the directory.

7.6.2.4 bool IncludeSubdirectories [get, set]

Returns or sets whether subdirectories will be included.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

38 / 88

IPEmotionSettings Interface Documentation

7.7 IInstrumentPlugIn Interface Reference

Instrument plug-in interface.

Inherited by InstrumentPlugInProxy.

Properties

• string TypeName [get]

Returns the instrument plug-in type name.

• bool Active [get, set]

Specifies whether the instrument plug-in is active.

• string PreferredVersion [get, set]

Specifies the preferred instrument plug-in version.

• string Manufacturer [get]

Returns the name of the plug-in manufacturer.

• string Description [get]

Returns the description of the plug-in.

• SupportedViewType SupportedViewType [get]

Returns the supported view type(s) of the plug-in.

7.7.1 Detailed Description

Instrument plug-in interface.

7.7.2 Property Documentation

7.7.2.1 string TypeName [get]

Returns the instrument plug-in type name.

Implemented in InstrumentPlugInProxy.

7.7.2.2 bool Active [get, set]

Specifies whether the instrument plug-in is active.

Implemented in InstrumentPlugInProxy.

7.7.2.3 string PreferredVersion [get, set]

Specifies the preferred instrument plug-in version.

Remarks:

In case the latest installed instrument plug-in version should be used an empty string should be set.

Implemented in InstrumentPlugInProxy.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

39 / 88

IPEmotionSettings Interface Documentation

7.7.2.4 string Manufacturer [get]

Returns the name of the plug-in manufacturer.

Implemented in InstrumentPlugInProxy.

7.7.2.5 string Description [get]

Returns the description of the plug-in.

Implemented in InstrumentPlugInProxy.

7.7.2.6 SupportedViewType SupportedViewType [get]

Returns the supported view type(s) of the plug-in.

Implemented in InstrumentPlugInProxy.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

40 / 88

IPEmotionSettings Interface Documentation

7.8 IInstrumentPlugIns Interface Reference

Instrument plug-in list interface.

Inherited by InstrumentPlugInsProxy.

Public Member Functions

• IEnumerator GetEnumerator ()

Enumerator for the instrument plug-in list.

Properties

• int Count [get]

Count of instrument plug-ins in this list.

• IInstrumentPlugIn Item [int index] [get]

Returns the instrument plug-in with the given (zero based) index from this list.

7.8.1 Detailed Description

Instrument plug-in list interface.

7.8.2 Member Function Documentation

7.8.2.1 IEnumerator GetEnumerator ()

Enumerator for the instrument plug-in list.

Returns:

Interface of the instrument plug-in list enumerator.

Implemented in InstrumentPlugInsProxy.

7.8.3 Property Documentation

7.8.3.1 int Count [get]

Count of instrument plug-ins in this list.

Implemented in InstrumentPlugInsProxy.

7.8.3.2 IInstrumentPlugIn Item[int index] [get]

Returns the instrument plug-in with the given (zero based) index from this list.

Parameters:

index Index of the instrument plug-in in this list.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

41 / 88

IPEmotionSettings Interface Documentation

Returns:

Interface of the instrument plug-in.

Implemented in InstrumentPlugInsProxy.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

42 / 88

IPEmotionSettings Interface Documentation

7.9 IMapProvider Interface Reference

Map provider interface.

Properties

• string MapProviderKey [get]

Returns the key of the map provider.

• string MapProviderName [get]

Returns the name of the map provider.

7.9.1 Detailed Description

Map provider interface.

7.9.2 Property Documentation

7.9.2.1 string MapProviderKey [get]

Returns the key of the map provider.

7.9.2.2 string MapProviderName [get]

Returns the name of the map provider.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

43 / 88

IPEmotionSettings Interface Documentation

7.10 IMapProviders Interface Reference

Map provider list interface.

Public Member Functions

• IEnumerator GetEnumerator ()

Enumerator for the map provider list.

Properties

• int Count [get]

Count of map providers in this list.

• IMapProvider Item [int index] [get]

Returns the map provider with the given (zero based) index from this list.

7.10.1 Detailed Description

Map provider list interface.

7.10.2 Member Function Documentation

7.10.2.1 IEnumerator GetEnumerator ()

Enumerator for the map provider list.

Returns:

Interface of the map provider list enumerator

7.10.3 Property Documentation

7.10.3.1 int Count [get]

Count of map providers in this list.

7.10.3.2 IMapProvider Item[int index] [get]

Returns the map provider with the given (zero based) index from this list.

Parameters:

index Index of the map provider in this list.

Returns:

Interface of the map provider.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

44 / 88

IPEmotionSettings Interface Documentation

7.11 InstrumentPlugInProxy Interface Reference

Anzeige-PlugIn-Proxy.

Inherits IInstrumentPlugIn.

Properties

• string TypeName [get]

Returns the instrument plug-in type name.

• bool Active [get, set]

Specifies whether the instrument plug-in is active.

• string PreferredVersion [get, set]

Specifies the preferred instrument plug-in version.

• string Manufacturer [get]

Returns the name of the plug-in manufacturer.

• string Description [get]

Returns the description of the plug-in.

• SupportedViewType SupportedViewType [get]

Returns the supported view type(s) of the plug-in.

7.11.1 Detailed Description

Anzeige-PlugIn-Proxy.

7.11.2 Property Documentation

7.11.2.1 string TypeName [get]

Returns the instrument plug-in type name.

Implements IInstrumentPlugIn.

7.11.2.2 bool Active [get, set]

Specifies whether the instrument plug-in is active.

Implements IInstrumentPlugIn.

7.11.2.3 string PreferredVersion [get, set]

Specifies the preferred instrument plug-in version.

Remarks:

In case the latest installed instrument plug-in version should be used an empty string should be set.

Implements IInstrumentPlugIn.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

45 / 88

IPEmotionSettings Interface Documentation

7.11.2.4 string Manufacturer [get]

Returns the name of the plug-in manufacturer.

Implements IInstrumentPlugIn.

7.11.2.5 string Description [get]

Returns the description of the plug-in.

Implements IInstrumentPlugIn.

7.11.2.6 SupportedViewType SupportedViewType [get]

Returns the supported view type(s) of the plug-in.

Implements IInstrumentPlugIn.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

46 / 88

IPEmotionSettings Interface Documentation

7.12 InstrumentPlugInsEnum Interface Reference

Anzeige-PlugIn-List-Enumerator.

7.12.1 Detailed Description

Anzeige-PlugIn-List-Enumerator.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

47 / 88

IPEmotionSettings Interface Documentation

7.13 InstrumentPlugInsProxy Interface Reference

Anzeige-PlugIn-Listen-Proxy.

Inherits IInstrumentPlugIns.

Public Member Functions

• IEnumerator GetEnumerator ()

Enumerator for the instrument plug-in list.

Properties

• int Count [get]

Count of instrument plug-ins in this list.

• IInstrumentPlugIn Item [int index] [get]

Returns the instrument plug-in with the given (zero based) index from this list.

7.13.1 Detailed Description

Anzeige-PlugIn-Listen-Proxy.

7.13.2 Member Function Documentation

7.13.2.1 IEnumerator GetEnumerator ()

Enumerator for the instrument plug-in list.

Returns:

Interface of the instrument plug-in list enumerator.

Implements IInstrumentPlugIns.

7.13.3 Property Documentation

7.13.3.1 int Count [get]

Count of instrument plug-ins in this list.

Implements IInstrumentPlugIns.

7.13.3.2 IInstrumentPlugIn Item[int index] [get]

Returns the instrument plug-in with the given (zero based) index from this list.

Parameters:

index Index of the instrument plug-in in this list.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

48 / 88

IPEmotionSettings Interface Documentation

Returns:

Interface of the instrument plug-in.

Implements IInstrumentPlugIns.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

49 / 88

IPEmotionSettings Interface Documentation

7.14 IOperationPlugIn Interface Reference

Operation plug-in interface.

Properties

• string TypeName [get]

Returns the operation plug-in type name.

• bool Active [get, set]

Specifies whether the operation plug-in is active.

• string PreferredVersion [get, set]

Specifies the preferred operation plug-in version.

• string Manufacturer [get]

Returns the name of the plug-in manufacturer.

• string Description [get]

Returns the description of the plug-in.

7.14.1 Detailed Description

Operation plug-in interface.

7.14.2 Property Documentation

7.14.2.1 string TypeName [get]

Returns the operation plug-in type name.

7.14.2.2 bool Active [get, set]

Specifies whether the operation plug-in is active.

7.14.2.3 string PreferredVersion [get, set]

Specifies the preferred operation plug-in version.

Remarks:

In case the latest installed operation plug-in version should be used an empty string should be set.

7.14.2.4 string Manufacturer [get]

Returns the name of the plug-in manufacturer.

7.14.2.5 string Description [get]

Returns the description of the plug-in.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

50 / 88

IPEmotionSettings Interface Documentation

7.15 IOperationPlugIns Interface Reference

Operation plug-in list interface.

Public Member Functions

• IEnumerator GetEnumerator ()

Enumerator for the operation plug-in list.

Properties

• int Count [get]

Count of operation plug-ins in this list.

• IOperationPlugIn Item [int index] [get]

Returns the operation plug-in with the given (zero based) index from this list.

7.15.1 Detailed Description

Operation plug-in list interface.

7.15.2 Member Function Documentation

7.15.2.1 IEnumerator GetEnumerator ()

Enumerator for the operation plug-in list.

Returns:

Interface of the operation plug-in list enumerator.

7.15.3 Property Documentation

7.15.3.1 int Count [get]

Count of operation plug-ins in this list.

7.15.3.2 IOperationPlugIn Item[int index] [get]

Returns the operation plug-in with the given (zero based) index from this list.

Parameters:

index Index of the operation plug-in in this list.

Returns:

Interface of the operation plug-in.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

51 / 88

IPEmotionSettings Interface Documentation

7.16 IPlugIn Interface Reference

Plug-in interface.

Public Member Functions

• object GetOptionValue (string optionName)

Returns the value assigned to the named plug-in option.

• void SetOptionValue (string optionName, object valueToSet)

Sets the value of the named plug-in option.

Properties

• string TypeName [get]

Returns the plug-in type name.

• bool Active [get, set]

Specifies whether the plug-in is active.

• string PreferredVersion [get, set]

Specifies the preferred plug-in version.

• IReferenceObjects ReferenceObjectList [get]

Returns the reference object list of the plug-in.

• IPlugInOptions Options [get]

Returns the options list of the plug-in.

• string Manufacturer [get]

Returns the name of the plug-in manufacturer.

• string Description [get]

Returns the description of the plug-in.

7.16.1 Detailed Description

Plug-in interface.

7.16.2 Member Function Documentation

7.16.2.1 object GetOptionValue (string optionName)

Returns the value assigned to the named plug-in option.

Parameters:

optionName Name of the plug-in option.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

52 / 88

IPEmotionSettings Interface Documentation

7.16.2.2 void SetOptionValue (string optionName, object valueToSet)

Sets the value of the named plug-in option.

Parameters:

optionName Name of the plug-in option

valueToSet Value to be set for the named plug-in option.

7.16.3 Property Documentation

7.16.3.1 string TypeName [get]

Returns the plug-in type name.

7.16.3.2 bool Active [get, set]

Specifies whether the plug-in is active.

7.16.3.3 string PreferredVersion [get, set]

Specifies the preferred plug-in version.

Remarks:

In case the latest installed plug-in version should be used an empty string should be set.

7.16.3.4 IReferenceObjects ReferenceObjectList [get]

Returns the reference object list of the plug-in.

7.16.3.5 IPlugInOptions Options [get]

Returns the options list of the plug-in.

7.16.3.6 string Manufacturer [get]

Returns the name of the plug-in manufacturer.

7.16.3.7 string Description [get]

Returns the description of the plug-in.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

53 / 88

IPEmotionSettings Interface Documentation

7.17 IPlugInOption Interface Reference

Plug-in options interface.

Properties

• string Name [get]

Name of the plug-in option.

• object Value [get, set]

Value of the plug-in option.

7.17.1 Detailed Description

Plug-in options interface.

7.17.2 Property Documentation

7.17.2.1 string Name [get]

Name of the plug-in option.

7.17.2.2 object Value [get, set]

Value of the plug-in option.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

54 / 88

IPEmotionSettings Interface Documentation

7.18 IPlugInOptions Interface Reference

Plug-in options list interface.

Public Member Functions

• IEnumerator GetEnumerator ()

Enumerator for the plug-in-option list.

Properties

• int Count [get]

Count of plug-in-options in this list.

• IPlugInOption Item [int index] [get]

Returns the plug-in-option with the given (zero based) index from this list.

7.18.1 Detailed Description

Plug-in options list interface.

7.18.2 Member Function Documentation

7.18.2.1 IEnumerator GetEnumerator ()

Enumerator for the plug-in-option list.

Returns:

Interface of the plug-in-option list enumerator.

7.18.3 Property Documentation

7.18.3.1 int Count [get]

Count of plug-in-options in this list.

7.18.3.2 IPlugInOption Item[int index] [get]

Returns the plug-in-option with the given (zero based) index from this list.

Parameters:

index Index of the plug-in-option in this list.

Returns:

Interface of the plug-in-option.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

55 / 88

IPEmotionSettings Interface Documentation

7.19 IPlugIns Interface Reference

Plug-in list interface.

Public Member Functions

• IEnumerator GetEnumerator ()

Enumerator for the plug-in list.

Properties

• int Count [get]

Count of plug-ins in this list.

• IPlugIn Item [int index] [get]

Returns the plug-in with the given (zero based) index from this list.

7.19.1 Detailed Description

Plug-in list interface.

7.19.2 Member Function Documentation

7.19.2.1 IEnumerator GetEnumerator ()

Enumerator for the plug-in list.

Returns:

Interface of the plug-in list enumerator.

7.19.3 Property Documentation

7.19.3.1 int Count [get]

Count of plug-ins in this list.

7.19.3.2 IPlugIn Item[int index] [get]

Returns the plug-in with the given (zero based) index from this list.

Parameters:

index Index of the plug-in in this list.

Returns:

Interface of the plug-in.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

56 / 88

IPEmotionSettings Interface Documentation

7.20 IReferenceObject Interface Reference

Reference object interface.

Properties

• string TypeName [get]

Reference object type name.

• bool IsReferencePart [get, set]

Specifies whether the object will be used in the reference.

• ConfigurationPriority Priority [get, set]

Specifies the usage priority of the object.

7.20.1 Detailed Description

Reference object interface.

7.20.2 Property Documentation

7.20.2.1 string TypeName [get]

Reference object type name.

7.20.2.2 bool IsReferencePart [get, set]

Specifies whether the object will be used in the reference.

7.20.2.3 ConfigurationPriority Priority [get, set]

Specifies the usage priority of the object.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

57 / 88

IPEmotionSettings Interface Documentation

7.21 IReferenceObjects Interface Reference

Reference object list interface.

Public Member Functions

• IEnumerator GetEnumerator ()

Enumerator for the reference object list.

Properties

• int Count [get]

Count of reference objects in this list.

• IReferenceObject Item [int index] [get]

Returns the reference object with the given (zero based) index from this list.

7.21.1 Detailed Description

Reference object list interface.

7.21.2 Member Function Documentation

7.21.2.1 IEnumerator GetEnumerator ()

Enumerator for the reference object list.

Returns:

Interface of the reference object list enumerator.

7.21.3 Property Documentation

7.21.3.1 int Count [get]

Count of reference objects in this list.

7.21.3.2 IReferenceObject Item[int index] [get]

Returns the reference object with the given (zero based) index from this list.

Parameters:

index Index of the reference object in this list.

Returns:

Interface of the reference object.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

58 / 88

IPEmotionSettings Interface Documentation

7.22 ISettingsHandler Interface Reference

IPEmotion settings handler interface.

Public Member Functions

• void SaveSettings ()

Saves the modified settings.

• void Quit ()

Terminates the program.

• void SetPreferredUnit (PhysicalDimensionTypes physicalDimension, string preferredUnit)

Sets the preferred Unit for a given physical dimension.

• string GetPreferredUnit (PhysicalDimensionTypes physicalDimension)

Returns the preferred unit for a given physical dimension.

• void AddHotKey (UiCommand commandId, Keys key, int parameter)

Adds a hot key to a command.

• void RemoveHotKey (UiCommand commandId, int parameter)

Removes a hot key from a command.

• void EnableUserAdministration (string newAdminPassword)

Enables the user administration and sets the administrator password.

• void DisableUserAdministration (string adminPassword)

Disables the user administration.

• IUserAccounts GetUserAccounts (string adminPassword)

Returns the list of registered user accounts in the user administration.

• bool ChangeAdminPassword (string oldAdminPassword, string newAdminPassword)

Changes the password of the adminiatrator account.

• void ActivatePlugIn (string pluginName)

Activates a specific plug-in.

• void ActivatePlugInVersion (string pluginName, string pluginVersion)

Activates a specific plug-in version.

• void DeactivatePlugIn (string pluginName)

Deactivates a plug-in.

• void ImportEnvironment (string fileName)

Imports a working environment file, overwriting the actual settings.

• void ExportEnvironment (string fileName)

Creates a working environment file using the actual settings.

• void ActivateInstrumentPlugIn (string pluginName)

Activates a specific instrument plug-in.

• void ActivateInstrumentPlugInVersion (string pluginName, string pluginVersion)

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

59 / 88

IPEmotionSettings Interface Documentation

Activates a specific instrument plug-in version.

• void DeactivateInstrumentPlugIn (string pluginName)

Deactivates a instrument plug-in.

• void ActivateOperationPlugIn (string pluginName)

Activates a specific operation plug-in.

• void ActivateOperationPlugInVersion (string pluginName, string pluginVersion)

Activates a specific operation plug-in version.

• void DeactivateOperationPlugIn (string pluginName)

Deactivates an operation plug-in.

• void AssignLicenseKey (string licenseKey)

Assign a license key.

Properties

• bool LoadLastConfigurationOnStart [get, set]

Returns or sets whether IPEmotion loads the last used configuration on start.

• bool HardwareDetectionOnStart [get, set]

Returns or sets whether IPEmotion starts a hardware detection on start.

• bool UseHardwareDetectionAction [get, set]

Returns or sets if a specific configuration action should be performed after a succesfull automatic hardware
detection on IPEmotion start.

• HardwareDetectionAction HardwareDetectionAction [get, set]

Returns or sets which kind of configuration action should be performed after a succesfull automatic hardware
detection on IPEmotion start.

• bool IncludeExternalFilesInConfiguration [get, set]

Returns or sets whether external files are added to the configuration file.

• bool IncludeOptionsInConfiguration [get, set]

Returns or sets whether option settings that influence the configuration are saved in the configuration file.

• SignalConfigurationMode SignalConfigurationMode [get, set]

Returns or sets the configuration mode.

• bool ErrorFreeMeasurementChainAtInit [get, set]

Returns or sets whether an error free configuration is required before any hardware initialization can be done.

• bool ExpertMode [get, set]

Returns or sets the expert mode.

• bool AutoAdministration [get, set]

Returns or sets whether the autotomatic service administration is used.

• bool EnableAdditionalWarnings [get, set]

Returns or sets whether additional warnings are displayed in popup-windows when expert mode is active.

• bool EnableVariableConfiguration [get, set]

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

60 / 88

IPEmotionSettings Interface Documentation

Returns or sets whether variable channels are available when the expert mode is active.

• bool DisplayExtendedTabs [get, set]

Returns or sets whether extended dialog tabs like the format tab of channels are displayed.

• int SplitFileSize [get, set]

Returns or sets the maximum size of an acquisition file before it is split.

• double NoValueTimeout [get, set]

Returns or sets the NoValue timeout in seconds.

• double LimitMessageDisplayTime [get, set]

Returns or sets the display time of limit excceded messages in seconds.

• bool EnableProtocolConfiguration [get, set]

Returns or sets whether protocol nodes are visible in the hardware tree when the expert mode is active.

• bool EnableProtocolChannelConfiguration [get, set]

Returns or sets whether the scaling of channels, imported from a description file, can be edited.

• bool JobConfiguration [get, set]

Returns or sets whether diagnostic job sequences are displayed in the IPEmotion setup tree and diagnostic jobs
in the grid.

• bool IgnoreVerbalTable [get, set]

Returns or sets whether verbal tables are ignored during import of description files.

• int MaxPollingListCount [get, set]

Returns or sets the number of polling lists that should be created when importing CCP/XCP signals.

• CharacteristicSupport CharacteristicSupport [get, set]

Returns or sets the way characteristics are handled during import.

• bool EnableImporterLogging [get, set]

Returns or sets whether warnings and errors appearing during import are written to a log file.

• int SupportJ1939 [get, set]

Determines if a real J1939 protocol is imported from a CANbd file if it contains the necessary J1939 protocol
parameters or the appropriate messages are imported as normal CAN messages.

• bool SynchronizeSignalsByName [get, set]

Returns whether signal of message based protcols are synchronized by their names or by their name and the
name of the message they are part of.

• bool EnableReferenceConfiguration [get, set]

Returns or sets whether the channel references can be configured in the plug-in options when expert mode is
active.

• string Culture [get, set]

Returns or sets the localization of the IPEmotion UI.

• string Skin [get, set]

Returns or sets the name of the skin to be used by the IPEmotion UI.

• bool ShowToolTips [get, set]

Returns or sets whether tool tips are shown.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

61 / 88

IPEmotionSettings Interface Documentation

• int FontSize [get, set]

Returns or sets the font size used by the display elements.

• double HudTransparency [get, set]

Returns or sets the transparency used by the HUD dialogs.

• bool UseStandardDialogs [get, set]

Specifies whether the Windows standard file open/save dialog is user or the IPEmotion specific variant.

• bool TimeChannelIsAbsolut [get, set]

Specifies whether the IPEmotion time channels are displayed in relative time or absolute time.

• bool PerformanceOptimization [get, set]

Specifies whether the performance of the display elements should be optimized at the expense of the design.

• bool UseDisplayNames [get, set]

Specifies whether the display instruments use the display name instead of the channel name.

• int OnlineYtDiagramHistoryBufferDepth [get, set]

Specifies the online yt charts history buffer depth.

• int OnlineYtDiagramHistoryBufferResolution [get, set]

Specifies the online yt charts history buffer resolution factor.

• bool InitViewPagesAtFirstVisibility [get, set]

Specifies whether the online view pages are initialized during configuration loading or delayed until the page is
made visible for the first time.

• bool HideInactiveChannels [get, set]

Specifies whether inactive channels are hidden from the channel list, the channel selection dialog and the
overview page.

• bool ResetTimeOnStorage [get, set]

Specifies if the online time will reset after switch from displaying mode in storage mode.

• bool SharedTimeChannel [get, set]

Indicates whether cyclical time channels, that have the same sampling rate and the same data set, should be
combined in the display and while they are exported.

• bool MergeDataFilesOnImport [get, set]

Specifies whether data files are to be connected when loading a data set.

• TimeZoneDisplayType TimeZoneDisplayType [get, set]

Specifies whether absolute times are displayed referring to the local time zone of the analysys system, the local
time zone of the measurement system or as UTC time.

• bool EnableMapCache [get, set]

Specifies whether caching of map tiles is enabled.

• int MapCacheSize [get, set]

Specifies the maximum size of the cache for map tiles in MByte.

• int MapTilesProxyTcpPortNumber [get, set]

Specifies the TCP port number used by the map imagery processing unit.

• MapImagerySource MapImagerySource [get, set]

Specifies the data source from which to load map imagery.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

62 / 88

IPEmotionSettings Interface Documentation

• string MapProvider [get, set]

Specifies the map provider from where the map imagery is loaded.

• IMapProviders MapProviders [get]

Returns the list of available map providers.

• IDataPlugIns DataImportPlugInList [get]

Returns the list of available data import plug-ins.

• IDataPlugIns DataExportPlugInList [get]

Returns the list of available data export plug-ins.

• int AnalysisDiagramCurveQuality [get, set]

Specifies whether the analysis diagrams uses all measured values or only samples when drawing the curves.

• bool UseExtendedCursorValues [get, set]

Specifies whether the values of the cursors should be displayed in a separate window instead of directly beside
the crosshair.

• SelectedPlotHighlightType SelectedPlotHighlightType [get, set]

Specifies the highlightning type of selected curves in yt-charts.

• string ConfigDefaultDirectory [get, set]

Specifies the default directory for loading and saving configuration files.

• string ProjectDataDefaultDirectory [get, set]

Specifies the default directory for loading and saving project data files.

• string ImportDefaultDirectory [get, set]

Specifies the default directory where import description files can be found.

• string ExportDefaultDirectory [get, set]

Specifies the default directory where description files should be exported to.

• string StorageDataDefaultDirectory [get, set]

Specifies the default directory where measurement data files can be loaded from.

• string RawDataDefaultDirectory [get, set]

Specifies the default directory where temporary measurement data files will be saved.

• string ScriptingDefaultDirectory [get, set]

Specifies the default directory where IPEmotion loads and stores script files.

• string CustomDataDefaultDirectory [get, set]

Specifies the default directory where user specific data is loaded from and stored to.

• string LayoutDefaultDirectory [get, set]

Specifies the default directory for report layout files.

• string DatabaseDefaultDirectory [get, set]

Specifies the default directory for database files.

• string RefPropDirectory [get, set]

Specifies the directory where the REFPROP library file can be found.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

63 / 88

IPEmotionSettings Interface Documentation

• bool IsUserAdministrationActive [get]

Returns true in case the user administration is active.

• ICloudDrives CloudDrives [get]

Returns the list of registered cloud drives.

• IPlugIns PlugInList [get]

Returns the list of available plug-ins.

• bool CreateContinousTimeSignalOnMerge [get, set]

Specifies whether a continous time signal is generated when data files are merged.

• IInstrumentPlugIns InstrumentPlugInList [get]

Returns the list of available instrument plug-ins.

• IOperationPlugIns OperationPlugInList [get]

Returns the list of available operation plug-ins.

• string DataServiceDatabasePath [get, set]

Specifies the default directory for data service’s database.

• bool DataServiceActive [get, set]
• IDataServiceObservedDirectories DataServiceDirectories [get]
• bool UseConnectionBasedView [get, set]

Specifies whether hardware interfaces are grouped by type in the selection list.

• bool AllowFilesOfNewerVersions [get, set]

Returns whether IPEmotion will load configurations that were created with a newer version of IPEmotion.

• AnalysisDiagramAbsoluteTimeFormat AnalysisDiagramAbsoluteTimeFormat [get, set]

Returns or sets the mode of the absolute time axis in the analysis.

• int FreeGridSize [get, set]

Returns the free grid size in online and analysis view. The value 0 means the free grid size is disabled.

• bool AutomaticSavingSubConfigs [get, set]

Returns or sets whether the automatic saving of sub-configs is used.

• DataTreeDisplayMode DataTreeDisplayMode [get, set]

Returns or sets the way IPEmotion will display the entries in the measurement data tree.

• bool LoadLinkedSubConfigs [get, set]

Returns or sets whether the linked sub-configs will be loaded when opening a configuration.

• bool UseShortLabelInsteadOfVerbalTableText [get, set]

Returns or sets whether verbal table names uses short names.

• bool AutoscaleYAxisAfterLoadNewFile [get, set]

Defines whether the y-axis should be autoscaled after loading a new measurement file or keeps the old zoom
state.

• long SplitFileSizeEx [get, set]

Returns the maximum size of an acquisition file before it is split.

• bool AllowDaqListOverfill [get, set]

Specifies whether the DAQ lists may be overfilled without automatically deactivating signals after the import.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

64 / 88

IPEmotionSettings Interface Documentation

• ThermocoupleColorCoding ThermoCoupleColorCoding [get, set]

Specifies which color coding IPEmotion should use for thermocouple information.

• bool PakServiceEnabled [get, set]

Activates/deactivates the Pak service.

• ushort PakServicePort [get, set]

Returns or sets the port number of the PAK-service.

• bool PreventNegativeTimestamps [get, set]

Specifies whether the time stamps of a storage group are changed if it has a pre-trigger to avoid negative time
stamps.

• string TempDirectory [get, set]

Specifies the directory where the temporary files are created.

7.22.1 Detailed Description

IPEmotion settings handler interface.

7.22.2 Member Function Documentation

7.22.2.1 void SaveSettings ()

Saves the modified settings.

7.22.2.2 void Quit ()

Terminates the program.

Remarks:

Modified settings will not be saved automatically. Call SaveSettings to save the modifications.

7.22.2.3 void SetPreferredUnit (PhysicalDimensionTypes physicalDimension, string preferredUnit)

Sets the preferred Unit for a given physical dimension.

Parameters:

physicalDimension Type of the physical dimension

preferredUnit Symbol of the preferred unit

7.22.2.4 string GetPreferredUnit (PhysicalDimensionTypes physicalDimension)

Returns the preferred unit for a given physical dimension.

Parameters:

physicalDimension Typ of the physical dimension

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

65 / 88

IPEmotionSettings Interface Documentation

7.22.2.5 void AddHotKey (UiCommand commandId, Keys key, int parameter)

Adds a hot key to a command.

Parameters:

commandId Command id

key Hotkeys key code

parameter Optional parameter (index of script, screen, ...)

Remarks:

In case the command does not support a parameter the parameter value must be set to -1.

7.22.2.6 void RemoveHotKey (UiCommand commandId, int parameter)

Removes a hot key from a command.

Parameters:

commandId Command id

parameter Optional parameter (index of script, screen, ...)

Remarks:

In case the command does not support a parameter the parameter value must be set to -1.

7.22.2.7 void EnableUserAdministration (string newAdminPassword)

Enables the user administration and sets the administrator password.

Parameters:

newAdminPassword Password to be set for the adminiatrator account

Remarks:

It is recomended to assign a non-empty password for the administrator account.

7.22.2.8 void DisableUserAdministration (string adminPassword)

Disables the user administration.

Parameters:

adminPassword Password of the adminiatrator account

Remarks:

The password must match the password of the administrator account, otherwise no change will happen.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

66 / 88

IPEmotionSettings Interface Documentation

7.22.2.9 IUserAccounts GetUserAccounts (string adminPassword)

Returns the list of registered user accounts in the user administration.

Parameters:

adminPassword Password of the adminiatrator account

Remarks:

The password must match the password of the administrator account, otherwise no user account list will
be returned.

7.22.2.10 bool ChangeAdminPassword (string oldAdminPassword, string newAdminPassword)

Changes the password of the adminiatrator account.

Parameters:

oldAdminPassword Old password of the adminiatrator account
newAdminPassword New password of the adminiatrator account

Remarks:

The old password must match the password of the administrator account, otherwise no change will hap-
pen.
It is recomended to assign a non-empty password for the administrator account.

Returns:

True in case the password was changed, otherwise false.

7.22.2.11 void ActivatePlugIn (string pluginName)

Activates a specific plug-in.

Parameters:

pluginName Name of the plug-in to be activated

7.22.2.12 void ActivatePlugInVersion (string pluginName, string pluginVersion)

Activates a specific plug-in version.

Parameters:

pluginName Name of the plug-in to be activated
pluginVersion Version of the plug-in to be activated

Remarks:

In case no version is given the default version will be used.

7.22.2.13 void DeactivatePlugIn (string pluginName)

Deactivates a plug-in.

Parameters:

pluginName Name of the plug-in to be deactivated

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

67 / 88

IPEmotionSettings Interface Documentation

7.22.2.14 void ImportEnvironment (string fileName)

Imports a working environment file, overwriting the actual settings.

Parameters:

fileName Name of the working environment file to be imported (∗.ief)

7.22.2.15 void ExportEnvironment (string fileName)

Creates a working environment file using the actual settings.

Parameters:

fileName Name of the working environment file to be saved (∗.ief)

Remarks:

The actual settings are automatically saved before the environment file is created.

7.22.2.16 void ActivateInstrumentPlugIn (string pluginName)

Activates a specific instrument plug-in.

Parameters:

pluginName Name of the instrument plug-in to be activated

7.22.2.17 void ActivateInstrumentPlugInVersion (string pluginName, string pluginVersion)

Activates a specific instrument plug-in version.

Parameters:

pluginName Name of the instrument plug-in to be activated
pluginVersion Version of the instrument plug-in to be activated

Remarks:

In case no version is given the default version will be used.

7.22.2.18 void DeactivateInstrumentPlugIn (string pluginName)

Deactivates a instrument plug-in.

Parameters:

pluginName Name of the instrument plug-in to be deactivated

7.22.2.19 void ActivateOperationPlugIn (string pluginName)

Activates a specific operation plug-in.

Parameters:

pluginName Name of the operation plug-in to be activated

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

68 / 88

IPEmotionSettings Interface Documentation

7.22.2.20 void ActivateOperationPlugInVersion (string pluginName, string pluginVersion)

Activates a specific operation plug-in version.

Parameters:

pluginName Name of the operation plug-in to be activated

pluginVersion Version of the operation plug-in to be activated

Remarks:

In case no version is given the default version will be used.

7.22.2.21 void DeactivateOperationPlugIn (string pluginName)

Deactivates an operation plug-in.

Parameters:

pluginName Name of the operation plug-in to be deactivated

7.22.2.22 void AssignLicenseKey (string licenseKey)

Assign a license key.

Parameters:

licenseKey Lizense key to be assigned. IPEmotion will use this license when it’s started.

7.22.3 Property Documentation

7.22.3.1 bool LoadLastConfigurationOnStart [get, set]

Returns or sets whether IPEmotion loads the last used configuration on start.

7.22.3.2 bool HardwareDetectionOnStart [get, set]

Returns or sets whether IPEmotion starts a hardware detection on start.

7.22.3.3 bool UseHardwareDetectionAction [get, set]

Returns or sets if a specific configuration action should be performed after a succesfull automatic hardware
detection on IPEmotion start.

7.22.3.4 HardwareDetectionAction HardwareDetectionAction [get, set]

Returns or sets which kind of configuration action should be performed after a succesfull automatic hardware
detection on IPEmotion start.

7.22.3.5 bool IncludeExternalFilesInConfiguration [get, set]

Returns or sets whether external files are added to the configuration file.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

69 / 88

IPEmotionSettings Interface Documentation

7.22.3.6 bool IncludeOptionsInConfiguration [get, set]

Returns or sets whether option settings that influence the configuration are saved in the configuration file.

7.22.3.7 SignalConfigurationMode SignalConfigurationMode [get, set]

Returns or sets the configuration mode.

7.22.3.8 bool ErrorFreeMeasurementChainAtInit [get, set]

Returns or sets whether an error free configuration is required before any hardware initialization can be done.

7.22.3.9 bool ExpertMode [get, set]

Returns or sets the expert mode.

7.22.3.10 bool AutoAdministration [get, set]

Returns or sets whether the autotomatic service administration is used.

7.22.3.11 bool EnableAdditionalWarnings [get, set]

Returns or sets whether additional warnings are displayed in popup-windows when expert mode is active.

7.22.3.12 bool EnableVariableConfiguration [get, set]

Returns or sets whether variable channels are available when the expert mode is active.

7.22.3.13 bool DisplayExtendedTabs [get, set]

Returns or sets whether extended dialog tabs like the format tab of channels are displayed.

7.22.3.14 int SplitFileSize [get, set]

Returns or sets the maximum size of an acquisition file before it is split.

Remarks:

Only values from 1048576 (1 MByte) up to 1073741824 (1 GByte) are allowed.
This property is deprecated and should no longer be used. Instead the SplitFileSizeEx property should
be used.

7.22.3.15 double NoValueTimeout [get, set]

Returns or sets the NoValue timeout in seconds.

Remarks:

Only values from 0 up to 5.0 are allowed.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

70 / 88

IPEmotionSettings Interface Documentation

7.22.3.16 double LimitMessageDisplayTime [get, set]

Returns or sets the display time of limit excceded messages in seconds.

Remarks:

Only positive values are allowed. In case 0 is set the messages stay visible until closed by the user.

7.22.3.17 bool EnableProtocolConfiguration [get, set]

Returns or sets whether protocol nodes are visible in the hardware tree when the expert mode is active.

7.22.3.18 bool EnableProtocolChannelConfiguration [get, set]

Returns or sets whether the scaling of channels, imported from a description file, can be edited.

7.22.3.19 bool JobConfiguration [get, set]

Returns or sets whether diagnostic job sequences are displayed in the IPEmotion setup tree and diagnostic
jobs in the grid.

7.22.3.20 bool IgnoreVerbalTable [get, set]

Returns or sets whether verbal tables are ignored during import of description files.

7.22.3.21 int MaxPollingListCount [get, set]

Returns or sets the number of polling lists that should be created when importing CCP/XCP signals.

Remarks:

Values between 0 and 4 are supported, which means the support of polling lists can be disabled or up to
4 polling lists can be used. The usage of multiple DAQ lists requires a plug-in that supports this feature.

7.22.3.22 CharacteristicSupport CharacteristicSupport [get, set]

Returns or sets the way characteristics are handled during import.

7.22.3.23 bool EnableImporterLogging [get, set]

Returns or sets whether warnings and errors appearing during import are written to a log file.

7.22.3.24 int SupportJ1939 [get, set]

Determines if a real J1939 protocol is imported from a CANbd file if it contains the necessary J1939 protocol
parameters or the appropriate messages are imported as normal CAN messages.

Remarks:

With a value of 1 the real J1939 protocol is used, with 0 normal CAN messages are created.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

71 / 88

IPEmotionSettings Interface Documentation

7.22.3.25 bool SynchronizeSignalsByName [get, set]

Returns whether signal of message based protcols are synchronized by their names or by their name and the
name of the message they are part of.

7.22.3.26 bool EnableReferenceConfiguration [get, set]

Returns or sets whether the channel references can be configured in the plug-in options when expert mode is
active.

Remarks:

No longer supported.

7.22.3.27 string Culture [get, set]

Returns or sets the localization of the IPEmotion UI.

Remarks:

The localization is specified by a language tag that conforms to IETF RFC 3066. The language part is a
two letter subtag according to ISO standard 639 and the country part is a two letter subtag according to
the country code specified in ISO 3166.

7.22.3.28 string Skin [get, set]

Returns or sets the name of the skin to be used by the IPEmotion UI.

Remarks:

The following skins are available:

• "IPETRONIK2": Blue

• "IPETRONIK-DarkBlue-Skin": Dark blue

• "IPETRONIK-Black-Skin": Black

• "IPETRONIK-LightBlue-Skin": Light blue

• "IPETRONIK-Grey-Skin": Grey

• "IPETRONIK-Bright-Skin": Bright

7.22.3.29 bool ShowToolTips [get, set]

Returns or sets whether tool tips are shown.

7.22.3.30 int FontSize [get, set]

Returns or sets the font size used by the display elements.

Remarks:

The font size can be set to 7 (S), 9 (M), 11 (L) or 13 (XL) point.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

72 / 88

IPEmotionSettings Interface Documentation

7.22.3.31 double HudTransparency [get, set]

Returns or sets the transparency used by the HUD dialogs.

Remarks:

The transparency can be set to values between 0 % (totaly opaque) and 30 %.

7.22.3.32 bool UseStandardDialogs [get, set]

Specifies whether the Windows standard file open/save dialog is user or the IPEmotion specific variant.

7.22.3.33 bool TimeChannelIsAbsolut [get, set]

Specifies whether the IPEmotion time channels are displayed in relative time or absolute time.

7.22.3.34 bool PerformanceOptimization [get, set]

Specifies whether the performance of the display elements should be optimized at the expense of the design.

7.22.3.35 bool UseDisplayNames [get, set]

Specifies whether the display instruments use the display name instead of the channel name.

7.22.3.36 int OnlineYtDiagramHistoryBufferDepth [get, set]

Specifies the online yt charts history buffer depth.

Remarks:

Allowed values are in the range from 1 to 50.

7.22.3.37 int OnlineYtDiagramHistoryBufferResolution [get, set]

Specifies the online yt charts history buffer resolution factor.

Remarks:

Allowed values are in the range from 1 to 10.

7.22.3.38 bool InitViewPagesAtFirstVisibility [get, set]

Specifies whether the online view pages are initialized during configuration loading or delayed until the page
is made visible for the first time.

7.22.3.39 bool HideInactiveChannels [get, set]

Specifies whether inactive channels are hidden from the channel list, the channel selection dialog and the
overview page.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

73 / 88

IPEmotionSettings Interface Documentation

7.22.3.40 bool ResetTimeOnStorage [get, set]

Specifies if the online time will reset after switch from displaying mode in storage mode.

7.22.3.41 bool SharedTimeChannel [get, set]

Indicates whether cyclical time channels, that have the same sampling rate and the same data set, should be
combined in the display and while they are exported.

7.22.3.42 bool MergeDataFilesOnImport [get, set]

Specifies whether data files are to be connected when loading a data set.

7.22.3.43 TimeZoneDisplayType TimeZoneDisplayType [get, set]

Specifies whether absolute times are displayed referring to the local time zone of the analysys system, the
local time zone of the measurement system or as UTC time.

Remarks:

This setting affects the display of absolute times only if the loaded data contains the necessary informa-
tions.

7.22.3.44 bool EnableMapCache [get, set]

Specifies whether caching of map tiles is enabled.

Remarks:

Obsolete. This configuration option is no longer available. Please use property ’MapImagerySource’ if
applicable.

7.22.3.45 int MapCacheSize [get, set]

Specifies the maximum size of the cache for map tiles in MByte.

Remarks:

Obsolete. This configuration option is no longer available.

7.22.3.46 int MapTilesProxyTcpPortNumber [get, set]

Specifies the TCP port number used by the map imagery processing unit.

Remarks:

Obsolete. This configuration option is no longer available.

7.22.3.47 MapImagerySource MapImagerySource [get, set]

Specifies the data source from which to load map imagery.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

74 / 88

IPEmotionSettings Interface Documentation

7.22.3.48 string MapProvider [get, set]

Specifies the map provider from where the map imagery is loaded.

Remarks:

The parameter must be a map provider key from the MapProviders list.

7.22.3.49 IMapProviders MapProviders [get]

Returns the list of available map providers.

7.22.3.50 IDataPlugIns DataImportPlugInList [get]

Returns the list of available data import plug-ins.

7.22.3.51 IDataPlugIns DataExportPlugInList [get]

Returns the list of available data export plug-ins.

7.22.3.52 int AnalysisDiagramCurveQuality [get, set]

Specifies whether the analysis diagrams uses all measured values or only samples when drawing the curves.

Remarks:

Only values from 0 up to 100 are allowed.
The value 100 means that all measured values are used to draw the curves.
A value of 0 specifies that only a minimum number of samples is used.

7.22.3.53 bool UseExtendedCursorValues [get, set]

Specifies whether the values of the cursors should be displayed in a separate window instead of directly beside
the crosshair.

7.22.3.54 SelectedPlotHighlightType SelectedPlotHighlightType [get, set]

Specifies the highlightning type of selected curves in yt-charts.

7.22.3.55 string ConfigDefaultDirectory [get, set]

Specifies the default directory for loading and saving configuration files.

7.22.3.56 string ProjectDataDefaultDirectory [get, set]

Specifies the default directory for loading and saving project data files.

7.22.3.57 string ImportDefaultDirectory [get, set]

Specifies the default directory where import description files can be found.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

75 / 88

IPEmotionSettings Interface Documentation

7.22.3.58 string ExportDefaultDirectory [get, set]

Specifies the default directory where description files should be exported to.

7.22.3.59 string StorageDataDefaultDirectory [get, set]

Specifies the default directory where measurement data files can be loaded from.

7.22.3.60 string RawDataDefaultDirectory [get, set]

Specifies the default directory where temporary measurement data files will be saved.

7.22.3.61 string ScriptingDefaultDirectory [get, set]

Specifies the default directory where IPEmotion loads and stores script files.

7.22.3.62 string CustomDataDefaultDirectory [get, set]

Specifies the default directory where user specific data is loaded from and stored to.

7.22.3.63 string LayoutDefaultDirectory [get, set]

Specifies the default directory for report layout files.

7.22.3.64 string DatabaseDefaultDirectory [get, set]

Specifies the default directory for database files.

7.22.3.65 string RefPropDirectory [get, set]

Specifies the directory where the REFPROP library file can be found.

7.22.3.66 bool IsUserAdministrationActive [get]

Returns true in case the user administration is active.

7.22.3.67 ICloudDrives CloudDrives [get]

Returns the list of registered cloud drives.

7.22.3.68 IPlugIns PlugInList [get]

Returns the list of available plug-ins.

7.22.3.69 bool CreateContinousTimeSignalOnMerge [get, set]

Specifies whether a continous time signal is generated when data files are merged.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

76 / 88

IPEmotionSettings Interface Documentation

7.22.3.70 IInstrumentPlugIns InstrumentPlugInList [get]

Returns the list of available instrument plug-ins.

7.22.3.71 IOperationPlugIns OperationPlugInList [get]

Returns the list of available operation plug-ins.

7.22.3.72 string DataServiceDatabasePath [get, set]

Specifies the default directory for data service’s database.

7.22.3.73 bool DataServiceActive [get, set]

7.22.3.74 IDataServiceObservedDirectories DataServiceDirectories [get]

7.22.3.75 bool UseConnectionBasedView [get, set]

Specifies whether hardware interfaces are grouped by type in the selection list.

7.22.3.76 bool AllowFilesOfNewerVersions [get, set]

Returns whether IPEmotion will load configurations that were created with a newer version of IPEmotion.

7.22.3.77 AnalysisDiagramAbsoluteTimeFormat AnalysisDiagramAbsoluteTimeFormat [get, set]

Returns or sets the mode of the absolute time axis in the analysis.

7.22.3.78 int FreeGridSize [get, set]

Returns the free grid size in online and analysis view. The value 0 means the free grid size is disabled.

7.22.3.79 bool AutomaticSavingSubConfigs [get, set]

Returns or sets whether the automatic saving of sub-configs is used.

7.22.3.80 DataTreeDisplayMode DataTreeDisplayMode [get, set]

Returns or sets the way IPEmotion will display the entries in the measurement data tree.

7.22.3.81 bool LoadLinkedSubConfigs [get, set]

Returns or sets whether the linked sub-configs will be loaded when opening a configuration.

7.22.3.82 bool UseShortLabelInsteadOfVerbalTableText [get, set]

Returns or sets whether verbal table names uses short names.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

77 / 88

IPEmotionSettings Interface Documentation

7.22.3.83 bool AutoscaleYAxisAfterLoadNewFile [get, set]

Defines whether the y-axis should be autoscaled after loading a new measurement file or keeps the old zoom
state.

7.22.3.84 long SplitFileSizeEx [get, set]

Returns the maximum size of an acquisition file before it is split.

Remarks:

For IPEmotion only values from 1048576 (1 MByte) up to 1073741824 (1 GByte) are allowed.
For IPEmotionRT.UI the value is fixed to 68719476736 (64 GByte) and can not be changed.

7.22.3.85 bool AllowDaqListOverfill [get, set]

Specifies whether the DAQ lists may be overfilled without automatically deactivating signals after the import.

7.22.3.86 ThermocoupleColorCoding ThermoCoupleColorCoding [get, set]

Specifies which color coding IPEmotion should use for thermocouple information.

7.22.3.87 bool PakServiceEnabled [get, set]

Activates/deactivates the Pak service.

7.22.3.88 ushort PakServicePort [get, set]

Returns or sets the port number of the PAK-service.

7.22.3.89 bool PreventNegativeTimestamps [get, set]

Specifies whether the time stamps of a storage group are changed if it has a pre-trigger to avoid negative time
stamps.

Remarks:

Does not correct timestamps of data aquired via Quickstart or NML.

7.22.3.90 string TempDirectory [get, set]

Specifies the directory where the temporary files are created.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

78 / 88

IPEmotionSettings Interface Documentation

7.23 IUserAccount Interface Reference

User account interface.

Properties

• string Username [get]

Returns the name of the user.

• string Password [get, set]

Returns or sets the user password.

• bool CanConfigurate [get, set]

Specifies whether the user can change the configuration.

• bool CanModifyStatus [get, set]

Specifies whether the user can modify the IPEmotion status.

• UserLevel UserLevel [get, set]

Specifies the access level of the user.

• bool Active [get, set]

Specifies whether the user can log in.

• bool CanConfigurateView [get, set]

Specifies whether the user can change the view configuration.

7.23.1 Detailed Description

User account interface.

7.23.2 Property Documentation

7.23.2.1 string Username [get]

Returns the name of the user.

7.23.2.2 string Password [get, set]

Returns or sets the user password.

7.23.2.3 bool CanConfigurate [get, set]

Specifies whether the user can change the configuration.

7.23.2.4 bool CanModifyStatus [get, set]

Specifies whether the user can modify the IPEmotion status.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

79 / 88

IPEmotionSettings Interface Documentation

7.23.2.5 UserLevel UserLevel [get, set]

Specifies the access level of the user.

7.23.2.6 bool Active [get, set]

Specifies whether the user can log in.

7.23.2.7 bool CanConfigurateView [get, set]

Specifies whether the user can change the view configuration.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

80 / 88

IPEmotionSettings Interface Documentation

7.24 IUserAccounts Interface Reference

User account list interface.

Public Member Functions

• IEnumerator GetEnumerator ()

Enumerator for the user account list.

• IUserAccount AddUser (string nameOfUser, string userPassword, UserLevel accessLevel, bool enab-

bleConfig, bool enabbleStatusModification)

Adds a new user to the user account list.

• void RemoveUser (string nameOfUser)

Removes a user from the user account list.

Properties

• int Count [get]

Count of user accounts in this list.

• IUserAccount Item [int index] [get]

Returns the user account with the given (zero based) index from this list.

7.24.1 Detailed Description

User account list interface.

7.24.2 Member Function Documentation

7.24.2.1 IEnumerator GetEnumerator ()

Enumerator for the user account list.

Returns:

Interface of the user account list enumerator

7.24.2.2 IUserAccount AddUser (string nameOfUser, string userPassword, UserLevel accessLevel,

bool enabbleConfig, bool enabbleStatusModification)

Adds a new user to the user account list.

Parameters:

nameOfUser Name of the new user.

userPassword Password of the new user.

accessLevel Access level of the new user.

enabbleConfig Specifies whether the new user may modify configurations.

enabbleStatusModification Specifies whether the new user may change the IPEmotion satus.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

81 / 88

IPEmotionSettings Interface Documentation

Returns:

Interface of the new user account

7.24.2.3 void RemoveUser (string nameOfUser)

Removes a user from the user account list.

Parameters:

nameOfUser Name of the user.

7.24.3 Property Documentation

7.24.3.1 int Count [get]

Count of user accounts in this list.

7.24.3.2 IUserAccount Item[int index] [get]

Returns the user account with the given (zero based) index from this list.

Parameters:

index Index of the user account in this list.

Returns:

Interface of the user account.

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

82 / 88

Index

ActivateInstrumentPlugIn
ISettingsHandler, 68

ActivateInstrumentPlugInVersion

ISettingsHandler, 68
ActivateOperationPlugIn
ISettingsHandler, 68
ActivateOperationPlugInVersion
ISettingsHandler, 68

ActivatePlugIn

ISettingsHandler, 67

ActivatePlugInVersion

ISettingsHandler, 67

Active

ICloudDrive, 30
IDataServiceObservedDirectory, 38
IInstrumentPlugIn, 39
InstrumentPlugInProxy, 45
IOperationPlugIn, 50
IPlugIn, 53
IUserAccount, 80

AddCloudDrive

ICloudDrives, 31

AddDirectory

ChangeAdminPassword
ISettingsHandler, 67

CharacteristicSupport

IPEmotionSettings, 25
ISettingsHandler, 71

CloudDrives

ISettingsHandler, 76

ConfigDefaultDirectory

ISettingsHandler, 75

ConfigurationPriority

IPEmotionSettings, 17

Count

ICloudDrives, 32
IDataPlugIns, 35
IDataServiceObservedDirectories, 37
IInstrumentPlugIns, 41
IMapProviders, 44
InstrumentPlugInsProxy, 48
IOperationPlugIns, 51
IPlugInOptions, 55
IPlugIns, 56
IReferenceObjects, 58
IUserAccounts, 82

IDataServiceObservedDirectories, 36

CreateContinousTimeSignalOnMerge

AddHotKey

ISettingsHandler, 65

AddUser

IUserAccounts, 81

AllowDaqListOverfill

ISettingsHandler, 78
AllowFilesOfNewerVersions
ISettingsHandler, 77

AnalysisDiagramAbsoluteTimeFormat

IPEmotionSettings, 26
ISettingsHandler, 77
AnalysisDiagramCurveQuality
ISettingsHandler, 75

AssignLicenseKey

ISettingsHandler, 69

AutoAdministration

ISettingsHandler, 70
AutomaticSavingSubConfigs
ISettingsHandler, 77

AutoscaleYAxisAfterLoadNewFile

ISettingsHandler, 77

CanConfigurate

IUserAccount, 79

CanConfigurateView

IUserAccount, 80

CanModifyStatus

IUserAccount, 79

ISettingsHandler, 76

Culture

ISettingsHandler, 72
CustomDataDefaultDirectory
ISettingsHandler, 76

DatabaseDefaultDirectory
ISettingsHandler, 76

DataExportPlugInList

ISettingsHandler, 75

DataImportPlugInList

ISettingsHandler, 75

DataServiceActive

ISettingsHandler, 77

DataServiceDatabasePath

ISettingsHandler, 77

DataServiceDirectories

ISettingsHandler, 77

DataTreeDisplayMode

IPEmotionSettings, 26
ISettingsHandler, 77
DeactivateInstrumentPlugIn
ISettingsHandler, 68

DeactivateOperationPlugIn

ISettingsHandler, 69

DeactivatePlugIn

ISettingsHandler, 67

Description

INDEX

IInstrumentPlugIn, 40
InstrumentPlugInProxy, 46
IOperationPlugIn, 50
IPlugIn, 53

DisableUserAdministration

ISettingsHandler, 66

DisplayExtendedTabs

ISettingsHandler, 70

EnableAdditionalWarnings

ISettingsHandler, 70

EnableImporterLogging

ISettingsHandler, 71

EnableMapCache

ISettingsHandler, 74

EnableProtocolChannelConfiguration

ISettingsHandler, 71
EnableProtocolConfiguration
ISettingsHandler, 71
EnableReferenceConfiguration
ISettingsHandler, 72
EnableUserAdministration
ISettingsHandler, 66
EnableVariableConfiguration
ISettingsHandler, 70

ErrorFreeMeasurementChainAtInit

ISettingsHandler, 70

ExpertMode

ISettingsHandler, 70

ExportDefaultDirectory

ISettingsHandler, 75

ExportEnvironment

ISettingsHandler, 68

FontSize

ISettingsHandler, 72

FormatId

IDataPlugIn, 33

FreeGridSize

ISettingsHandler, 77

GetEnumerator

ICloudDrives, 31
IDataPlugIns, 35
IDataServiceObservedDirectories, 36
IInstrumentPlugIns, 41
IMapProviders, 44
InstrumentPlugInsProxy, 48
IOperationPlugIns, 51
IPlugInOptions, 55
IPlugIns, 56
IReferenceObjects, 58
IUserAccounts, 81

GetOptionValue

IDataPlugIn, 33
IPlugIn, 52

GetPreferredUnit

ISettingsHandler, 65

GetUserAccounts

ISettingsHandler, 66

HardwareDetectionAction

IPEmotionSettings, 18
ISettingsHandler, 69

HardwareDetectionOnStart

ISettingsHandler, 69

HideInactiveChannels

ISettingsHandler, 73

HudTransparency

ISettingsHandler, 72

ICloudDrive, 29

Active, 30
LoginName, 30
MappedDrive, 30
Name, 29
Password, 30
Url, 29
ICloudDrives, 31

AddCloudDrive, 31
Count, 32
GetEnumerator, 31
Item, 32
RemoveCloudDrive, 32

IDataPlugIn, 33

FormatId, 33
GetOptionValue, 33
Options, 33
SetOptionValue, 33

IDataPlugIns, 35
Count, 35
GetEnumerator, 35
Item, 35

IDataServiceObservedDirectories, 36

AddDirectory, 36
Count, 37
GetEnumerator, 36
Item, 37
RemoveDirectory, 37

IDataServiceObservedDirectory, 38

Active, 38
IncludeSubdirectories, 38
Name, 38
Path, 38
IgnoreVerbalTable

ISettingsHandler, 71

IInstrumentPlugIn, 39

Active, 39
Description, 40
Manufacturer, 39
PreferredVersion, 39
SupportedViewType, 40
TypeName, 39
IInstrumentPlugIns, 41

Count, 41
GetEnumerator, 41
Item, 41
IMapProvider, 43

MapProviderKey, 43
MapProviderName, 43

IMapProviders, 44
Count, 44
GetEnumerator, 44

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

84 / 88

INDEX

Item, 44

ImportDefaultDirectory

ISettingsHandler, 75

ImportEnvironment

ISettingsHandler, 67

IncludeExternalFilesInConfiguration

ISettingsHandler, 69
IncludeOptionsInConfiguration
ISettingsHandler, 69

IncludeSubdirectories

IDataServiceObservedDirectory, 38

InitViewPagesAtFirstVisibility
ISettingsHandler, 73

InstrumentPlugInList

ISettingsHandler, 76

InstrumentPlugInProxy, 45

Active, 45
Description, 46
Manufacturer, 45
PreferredVersion, 45
SupportedViewType, 46
TypeName, 45

InstrumentPlugInsEnum, 47
InstrumentPlugInsProxy, 48

Count, 48
GetEnumerator, 48
Item, 48

IOperationPlugIn, 50
Active, 50
Description, 50
Manufacturer, 50
PreferredVersion, 50
TypeName, 50
IOperationPlugIns, 51

Count, 51
GetEnumerator, 51
Item, 51

IPEmotionSettings, 15

AnalysisDiagramAbsoluteTimeFormat, 26
CharacteristicSupport, 25
ConfigurationPriority, 17
DataTreeDisplayMode, 26
HardwareDetectionAction, 18
MapImagerySource, 25
PhysicalDimensionTypes, 18
SelectedPlotHighlightType, 25
SignalConfigurationMode, 18
SupportedViewType, 17
ThermocoupleColorCoding, 26
TimeZoneDisplayType, 25
UiCommand, 19
UserLevel, 26

IPlugIn, 52

Active, 53
Description, 53
GetOptionValue, 52
Manufacturer, 53
Options, 53
PreferredVersion, 53
ReferenceObjectList, 53

SetOptionValue, 52
TypeName, 53

IPlugInOption, 54
Name, 54
Value, 54
IPlugInOptions, 55
Count, 55
GetEnumerator, 55
Item, 55
IPlugIns, 56

Count, 56
GetEnumerator, 56
Item, 56

IReferenceObject, 57

IsReferencePart, 57
Priority, 57
TypeName, 57
IReferenceObjects, 58

Count, 58
GetEnumerator, 58
Item, 58

ISettingsHandler, 59

ActivateInstrumentPlugIn, 68
ActivateInstrumentPlugInVersion, 68
ActivateOperationPlugIn, 68
ActivateOperationPlugInVersion, 68
ActivatePlugIn, 67
ActivatePlugInVersion, 67
AddHotKey, 65
AllowDaqListOverfill, 78
AllowFilesOfNewerVersions, 77
AnalysisDiagramAbsoluteTimeFormat, 77
AnalysisDiagramCurveQuality, 75
AssignLicenseKey, 69
AutoAdministration, 70
AutomaticSavingSubConfigs, 77
AutoscaleYAxisAfterLoadNewFile, 77
ChangeAdminPassword, 67
CharacteristicSupport, 71
CloudDrives, 76
ConfigDefaultDirectory, 75
CreateContinousTimeSignalOnMerge, 76
Culture, 72
CustomDataDefaultDirectory, 76
DatabaseDefaultDirectory, 76
DataExportPlugInList, 75
DataImportPlugInList, 75
DataServiceActive, 77
DataServiceDatabasePath, 77
DataServiceDirectories, 77
DataTreeDisplayMode, 77
DeactivateInstrumentPlugIn, 68
DeactivateOperationPlugIn, 69
DeactivatePlugIn, 67
DisableUserAdministration, 66
DisplayExtendedTabs, 70
EnableAdditionalWarnings, 70
EnableImporterLogging, 71
EnableMapCache, 74
EnableProtocolChannelConfiguration, 71

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

85 / 88

INDEX

EnableProtocolConfiguration, 71
EnableReferenceConfiguration, 72
EnableUserAdministration, 66
EnableVariableConfiguration, 70
ErrorFreeMeasurementChainAtInit, 70
ExpertMode, 70
ExportDefaultDirectory, 75
ExportEnvironment, 68
FontSize, 72
FreeGridSize, 77
GetPreferredUnit, 65
GetUserAccounts, 66
HardwareDetectionAction, 69
HardwareDetectionOnStart, 69
HideInactiveChannels, 73
HudTransparency, 72
IgnoreVerbalTable, 71
ImportDefaultDirectory, 75
ImportEnvironment, 67
IncludeExternalFilesInConfiguration, 69
IncludeOptionsInConfiguration, 69
InitViewPagesAtFirstVisibility, 73
InstrumentPlugInList, 76
IsUserAdministrationActive, 76
JobConfiguration, 71
LayoutDefaultDirectory, 76
LimitMessageDisplayTime, 70
LoadLastConfigurationOnStart, 69
LoadLinkedSubConfigs, 77
MapCacheSize, 74
MapImagerySource, 74
MapProvider, 74
MapProviders, 75
MapTilesProxyTcpPortNumber, 74
MaxPollingListCount, 71
MergeDataFilesOnImport, 74
NoValueTimeout, 70
OnlineYtDiagramHistoryBufferDepth, 73
OnlineYtDiagramHistoryBufferResolution, 73
OperationPlugInList, 77
PakServiceEnabled, 78
PakServicePort, 78
PerformanceOptimization, 73
PlugInList, 76
PreventNegativeTimestamps, 78
ProjectDataDefaultDirectory, 75
Quit, 65
RawDataDefaultDirectory, 76
RefPropDirectory, 76
RemoveHotKey, 66
ResetTimeOnStorage, 73
SaveSettings, 65
ScriptingDefaultDirectory, 76
SelectedPlotHighlightType, 75
SetPreferredUnit, 65
SharedTimeChannel, 74
ShowToolTips, 72
SignalConfigurationMode, 70
Skin, 72
SplitFileSize, 70

SplitFileSizeEx, 78
StorageDataDefaultDirectory, 76
SupportJ1939, 71
SynchronizeSignalsByName, 71
TempDirectory, 78
ThermoCoupleColorCoding, 78
TimeChannelIsAbsolut, 73
TimeZoneDisplayType, 74
UseConnectionBasedView, 77
UseDisplayNames, 73
UseExtendedCursorValues, 75
UseHardwareDetectionAction, 69
UseShortLabelInsteadOfVerbalTableText, 77
UseStandardDialogs, 73

IsReferencePart

IReferenceObject, 57
IsUserAdministrationActive

ISettingsHandler, 76

Item

ICloudDrives, 32
IDataPlugIns, 35
IDataServiceObservedDirectories, 37
IInstrumentPlugIns, 41
IMapProviders, 44
InstrumentPlugInsProxy, 48
IOperationPlugIns, 51
IPlugInOptions, 55
IPlugIns, 56
IReferenceObjects, 58
IUserAccounts, 82

IUserAccount, 79
Active, 80
CanConfigurate, 79
CanConfigurateView, 80
CanModifyStatus, 79
Password, 79
UserLevel, 79
Username, 79
IUserAccounts, 81

AddUser, 81
Count, 82
GetEnumerator, 81
Item, 82
RemoveUser, 82

JobConfiguration

ISettingsHandler, 71

LayoutDefaultDirectory

ISettingsHandler, 76

LimitMessageDisplayTime

ISettingsHandler, 70
LoadLastConfigurationOnStart
ISettingsHandler, 69

LoadLinkedSubConfigs

ISettingsHandler, 77

LoginName

ICloudDrive, 30

Manufacturer

IInstrumentPlugIn, 39

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

86 / 88

INDEX

InstrumentPlugInProxy, 45
IOperationPlugIn, 50
IPlugIn, 53
MapCacheSize

ISettingsHandler, 74

MapImagerySource

IPEmotionSettings, 25
ISettingsHandler, 74

MappedDrive

ICloudDrive, 30

MapProvider

ISettingsHandler, 74

MapProviderKey

IMapProvider, 43

MapProviderName

IMapProvider, 43

MapProviders

ISettingsHandler, 75
MapTilesProxyTcpPortNumber
ISettingsHandler, 74

MaxPollingListCount

ISettingsHandler, 71
MergeDataFilesOnImport
ISettingsHandler, 74

Name

ICloudDrive, 29
IDataServiceObservedDirectory, 38
IPlugInOption, 54

NoValueTimeout

ISettingsHandler, 70

OnlineYtDiagramHistoryBufferDepth

ISettingsHandler, 73

OnlineYtDiagramHistoryBufferResolution

ISettingsHandler, 73

OperationPlugInList

ISettingsHandler, 77

Options

IDataPlugIn, 33
IPlugIn, 53

PakServiceEnabled

ISettingsHandler, 78

PakServicePort

ISettingsHandler, 78

Password

ICloudDrive, 30
IUserAccount, 79

Path

IDataServiceObservedDirectory, 38

PerformanceOptimization
ISettingsHandler, 73
PhysicalDimensionTypes

IPEmotionSettings, 18

PlugInList

ISettingsHandler, 76

PreferredVersion

IInstrumentPlugIn, 39
InstrumentPlugInProxy, 45
IOperationPlugIn, 50

IPlugIn, 53

PreventNegativeTimestamps
ISettingsHandler, 78

Priority

IReferenceObject, 57

ProjectDataDefaultDirectory
ISettingsHandler, 75

Quit

ISettingsHandler, 65

RawDataDefaultDirectory
ISettingsHandler, 76

ReferenceObjectList
IPlugIn, 53

RefPropDirectory

ISettingsHandler, 76

RemoveCloudDrive

ICloudDrives, 32

RemoveDirectory

IDataServiceObservedDirectories, 37

RemoveHotKey

ISettingsHandler, 66

RemoveUser

IUserAccounts, 82

ResetTimeOnStorage

ISettingsHandler, 73

SaveSettings

ISettingsHandler, 65
ScriptingDefaultDirectory
ISettingsHandler, 76

SelectedPlotHighlightType
IPEmotionSettings, 25
ISettingsHandler, 75

SetOptionValue

IDataPlugIn, 33
IPlugIn, 52

SetPreferredUnit

ISettingsHandler, 65

SharedTimeChannel

ISettingsHandler, 74

ShowToolTips

ISettingsHandler, 72
SignalConfigurationMode

IPEmotionSettings, 18
ISettingsHandler, 70

Skin

ISettingsHandler, 72

SplitFileSize

ISettingsHandler, 70

SplitFileSizeEx

ISettingsHandler, 78
StorageDataDefaultDirectory
ISettingsHandler, 76

SupportedViewType

IInstrumentPlugIn, 40
InstrumentPlugInProxy, 46
IPEmotionSettings, 17

SupportJ1939

ISettingsHandler, 71

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

87 / 88

INDEX

SynchronizeSignalsByName
ISettingsHandler, 71

TempDirectory

ISettingsHandler, 78
ThermoCoupleColorCoding
ISettingsHandler, 78

ThermocoupleColorCoding
IPEmotionSettings, 26

TimeChannelIsAbsolut

ISettingsHandler, 73

TimeZoneDisplayType

IPEmotionSettings, 25
ISettingsHandler, 74

TypeName

IInstrumentPlugIn, 39
InstrumentPlugInProxy, 45
IOperationPlugIn, 50
IPlugIn, 53
IReferenceObject, 57

UiCommand

IPEmotionSettings, 19

Url

ICloudDrive, 29
UseConnectionBasedView

ISettingsHandler, 77

UseDisplayNames

ISettingsHandler, 73

UseExtendedCursorValues

ISettingsHandler, 75
UseHardwareDetectionAction
ISettingsHandler, 69

UserLevel

IPEmotionSettings, 26
IUserAccount, 79

Username

IUserAccount, 79

UseShortLabelInsteadOfVerbalTableText

ISettingsHandler, 77

UseStandardDialogs

ISettingsHandler, 73

Value

IPlugInOption, 54

IPEmotionSettings COM Reference

IPETRONIK GmbH & Co. KG

88 / 88


