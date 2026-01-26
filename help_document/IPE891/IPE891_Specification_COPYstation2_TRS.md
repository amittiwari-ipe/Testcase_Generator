COPYstation2 Technical Requirement Specification
1 Introduction ................................................................................................................................................................................................... 2
1.1 Purpose .................................................................................................................................................................................................. 2
1.2 Scope .................................................................................................................................................................................................... 2
1.3 Definitions and Attributes ..................................................................................................................................................................................... 2
1.3.1 OpState attribute ........................................................................................................................................................................................ 2
1.4 Glossary .................................................................................................................................................................................................. 2
1.5 Applicable documents ........................................................................................................................................................................................ 2
1.6 Related documents .......................................................................................................................................................................................... 2
2 System Overview ............................................................................................................................................................................................... 2
3 Requirements ................................................................................................................................................................................................. 2
3.1 System level interfaces ....................................................................................................................................................................................... 2
3.2 Hardware-Software interfaces .................................................................................................................................................................................. 2
```
3.3 Operational States (internal) ................................................................................................................................................................................... 3
```
3.4 Accessories ............................................................................................................................................................................................... 3
3.4.1 Cover for cartridge slots ................................................................................................................................................................................... 3
3.4.1.1 Dimensions and Material ............................................................................................................................................................................... 3
3.4.1.2 Usability ........................................................................................................................................................................................... 3
3.5 Hardware ................................................................................................................................................................................................. 3
3.5.1 Mechanics ............................................................................................................................................................................................. 3
3.5.1.1 General provisions ................................................................................................................................................................................... 3
3.5.1.2 Dimensions ......................................................................................................................................................................................... 3
3.5.1.3 Weight ............................................................................................................................................................................................ 3
3.5.1.4 Thermal concept ..................................................................................................................................................................................... 3
3.5.1.5 Interlocking mechanism ................................................................................................................................................................................ 3
3.5.1.6 Controls ........................................................................................................................................................................................... 4
3.5.1.7 Safety ............................................................................................................................................................................................. 4
3.5.1.8 Testing ............................................................................................................................................................................................ 4
3.5.2 Electronics ............................................................................................................................................................................................. 4
3.5.2.1 General provisions ................................................................................................................................................................................... 4
3.5.2.2 Purchased hardware .................................................................................................................................................................................. 4
3.5.2.2.1 Case .......................................................................................................................................................................................... 4
3.5.2.2.2 Power Supply .................................................................................................................................................................................... 5
3.5.2.2.3 Main board and RAM .............................................................................................................................................................................. 5
3.5.2.2.4 CPU ........................................................................................................................................................................................... 5
3.5.2.2.5 Cooler ......................................................................................................................................................................................... 6
```
3.5.2.2.6 100 GbE Intel(R) Network Adapter E810 ............................................................................................................................................................... 6
```
3.5.2.2.7 M2.0 System storage .............................................................................................................................................................................. 6
3.5.2.2.8 Local buffer storage ............................................................................................................................................................................... 6
3.5.2.2.9 Display ......................................................................................................................................................................................... 6
3.5.2.2.10 Lifting magnet .................................................................................................................................................................................. 7
3.5.2.3 Engineered Hardware ................................................................................................................................................................................. 7
3.5.2.3.1 ControlBoard Baseboard ........................................................................................................................................................................... 7
3.5.2.3.2 Cartridge controller board ........................................................................................................................................................................... 8
3.6 Software functions / blocks .................................................................................................................................................................................... 9
3.6.1 Operating system ........................................................................................................................................................................................ 9
3.6.1.1 Functional Requirements .............................................................................................................................................................................. 9
3.6.1.2 Non-functional requirements ............................................................................................................................................................................ 9
3.6.2 HW Platform control ...................................................................................................................................................................................... 9
3.6.2.1 Functional Requirements .............................................................................................................................................................................. 9
3.6.2.1.1 Cartridge detection to mounting ...................................................................................................................................................................... 9
3.6.2.2 Non-functional requirements ............................................................................................................................................................................ 10
3.6.3 Configuration ........................................................................................................................................................................................... 10
3.6.4 Update ................................................................................................................................................................................................ 11
3.6.5 Data enumeration and Job management ...................................................................................................................................................................... 11
3.6.5.1 Functional Requirements .............................................................................................................................................................................. 11
3.6.5.1.1 Dataset enumeration .............................................................................................................................................................................. 11
3.6.5.1.2 JSON Parsing ................................................................................................................................................................................... 11
3.6.5.1.3 Job management ................................................................................................................................................................................. 13
3.6.5.1.4 Local Buffer ..................................................................................................................................................................................... 14
3.6.5.1.5 Logging ........................................................................................................................................................................................ 15
3.6.5.2 Non-functional requirements ............................................................................................................................................................................ 15
3.6.6 Data transfer ........................................................................................................................................................................................... 15
3.6.6.1 Functional Requirements .............................................................................................................................................................................. 15
3.6.6.1.1 Network Connection check .......................................................................................................................................................................... 15
3.6.6.1.2 Create connection to target ......................................................................................................................................................................... 16
3.6.6.1.3 Data transfer to target server ........................................................................................................................................................................ 16
3.6.6.1.4 Target servers ................................................................................................................................................................................... 17
3.6.6.2 Non-functional requirements ............................................................................................................................................................................ 17
3.6.7 API ................................................................................................................................................................................................... 17
3.6.7.1 Functional Requirements .............................................................................................................................................................................. 17
3.6.7.2 Non-functional requirements ............................................................................................................................................................................ 18
3.6.7.3 API Documentation ................................................................................................................................................................................... 18
3.6.8 Web interface ........................................................................................................................................................................................... 18
3.6.8.1 Functional Requirements .............................................................................................................................................................................. 18
3.6.8.2 Non-functional requirements ............................................................................................................................................................................ 20
3.6.9 Testing ................................................................................................................................................................................................ 20
3.6.9.1 Data source for testing ................................................................................................................................................................................ 20
3.6.9.2 Data sinks for testing .................................................................................................................................................................................. 20
3.7 Production Tools ............................................................................................................................................................................................ 21
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 1of 31
1 Introduction
1.1 Purpose
```
This is the Technical Requirements Specification for COPYStation2 (CS2_TRS). It provides specifies the top level technical requirements derived from the product requirements.
```
1.2 Scope
The requirements herein specify high level technical details required to implement the product specified in [CS2_PRS]. Low-level design decisions may be included in this document to aid development, but are not explicitly within the intended scope of the document.
1.3 Definitions and Attributes
1.3.1 OpState attribute
The Requirements defined in this document may start with the following Text block before the actual requirement text:
[OpState: <state1>, <state2> ...]
```
Examples:
```
[OpState: Auto_Idle, Auto_Working, API_Idle][OpState: Auto]
[OpState: API_Working][OpState: API]
If the OpState attribute is present, the requirement shall only be applicable when the COPYstation2 is in the specified operation states, i.e. it can be considered an extension of the requirements condition clause such as "COPYstation2 shall ... if its current operating stateis API_Working"
If the attribute is not present, by default the requirement is applicable in any normal operation state. The states "Update" and "EndOfLine" shall be specified explicitly in the requirement or in the OpState attribute.
1.4 Glossary
Term Definition
PRS Product Requirement Specification, this document
TRS Technical Requirement Specification, a document derived from this PRS that specifies the technical requirements needed to implement the described system.
JSON JavaScript Object Notation, an open standard file format and data interchange format that uses human-readable text to store and transmit data objects
API Application Programming Interface, an interface that allows two separate programs or systems to communicate with each other to provide information or execute actions.
hot-plugging Inserting, accessing and extracting devices, especially storage devices, while the host system is up and running, without having to power it off.
```
dataset A set of related files, including at least JSON (.json) file which describes the dataset. The rest of the files can be any combination of .zip, .log, .m5sum, ....The definition of the file format for the JSON description files can be found in [JSONInfo]
```
```
cartridge A data storage device made by IPETRONIK which can be hot-plugged into and unplugged from a logger (starting with the IPE891) and COPYstation2
```
```
logger Any IPETRONIK data logger (e.g. IPE891), typically mounted in vehicles and connected to various communication busses.
```
1.5 Applicable documents
Applicable documents are documents with which this document claims compliance.
Reference Document name Description
```
SysDH System Development Handbook (TODO!) Process description for the development of a device/system, including a specification for product requirements (TODO!)
```
[CS2_PRS] COPYstation2_Product_Requirement_Specification Technical Requirement Specification for the COPYstation2 project. Includes system, hardware and software level requirements
1.6 Related documents
Related documents are documents referenced by, but not covered by the scope of this document.
Reference Document name Description
[JSONInfo] LoggerDatasetInformation_Schema_v02.json Definition of the structure for dataset JSON files. Path: http://gitlab.caetec:8929/ASO/loggerdatasetinformationformat
2 System Overview
The COPYstation2 is a simple-to-use adapter from IPETRONIK cartridges to Customer IT infrastructure using high speed Ethernet connections.
<Image: 2024-07-01_14_34_19-COPY2_Display.pptx_-_PowerPoint.png>Figure 1 COPYstation2 enclosure concept
It is meant to be mounted on a server rack, physically attached to a customer's IT infrastructure, and provides slots for hot-plugging cartridges, as well as a display and LEDs for status presentation and buttons for headless control, i.e. control without any external display.
<Image: 2024-07-18_14_05_10-.png>
```
COPYstation2 is used to connect a IPETRONIK cartridge that has been filled with datasets from a vehicle test. Alternatively, the logger can directly transfer the datasets to the COPYstation2 via a wireless link. The datasets are processed and transferred to a Server(Azure, SFTP or other). The progress of the transfer and the state of the system can be viewed with a PC/Laptop connected directly to the COPYstation2 using the COPYstation2's WebUI.
```
<Image: Screenshot_2024-07-17_153527.png>
COPYstation2 can be used in a customer environment where multiple COPYstation2 and possibly other similar systems from other manufacturers are handled automatically by an external control system. The COPYstation2 has the functionality to be controlled via an APIwhich follows the specification required by the external control system.
3 Requirements
3.1 System level interfaces
3.2 Hardware-Software interfaces
vvHLP-2291 - Cold boot with inserted cartridgesThe COPYstation2 must not boot the computer hardware before the two cartridges are inserted. If the two cartridges are not inserted the display shall inform the user and request both cartridges to insert.
```
Rationale: This is part of the preliminary solution in order to have the PCIe root complex initialized as long as the BIOS does not support the hot-plug feature on the pcie slots.
```
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 2of 31
Status Draft
Linked Work Items has parent: vvHLP-1144 - Hardware-Software interfaces
```
3.3 Operational States (internal)
```
3.4 Accessories
3.4.1 Cover for cartridge slots
3.4.1.1 Dimensions and Material
vvHLP-2285 - DimensionThe cartridge slot cover shall have the dimension of the cartridge front.
Status Draft
Linked Work Items has parent: vvHLP-2277 - Dimensions and Material ,is derived from: vvHLP-2276 - Cartridge slot cover
vvHLP-2282 - DesignThe cover shall have no air vents.
Status Draft
Linked Work Items has parent: vvHLP-2277 - Dimensions and Material ,is derived from: vvHLP-2276 - Cartridge slot cover
vvHLP-2281 - MaterialThe material used can be plastic or metal. The overall appearance must fit to the overall look.
Status Draft
Linked Work Items has parent: vvHLP-2277 - Dimensions and Material ,is derived from: vvHLP-2276 - Cartridge slot cover
3.4.1.2 Usability
vvHLP-2283 - RemovableThe cartridge slot cover shall be removable manually and without pressing the eject button.
Status Draft
Linked Work Items has parent: vvHLP-2279 - Usability ,is derived from: vvHLP-2276 - Cartridge slot cover
vvHLP-2284 - HandleThe cartridge slots cover shall have a handle with a hole which can be used to fix the cover to the device.
```
Note: The minimum force necessary for removing the cover must be as high that the cover is firmly secured in the slot. Underno circumstances shall the cover fall out unintentionally.
```
Status Draft
Linked Work Items has parent: vvHLP-2279 - Usability ,is derived from: vvHLP-2276 - Cartridge slot cover
3.5 Hardware
3.5.1 Mechanics
3.5.1.1 General provisions
The COPYstation2 is an adapter from cartridges to Customer IT infrastructure using 100 Gbit Ethernet connections via E810 network adapter.
3.5.1.2 Dimensions
```
COS2-54 - SizeThe base unit will (WxLxH). (Reference 19" 4 Units)
```
```
Dimensions (h/w/d): 177.8 x 485 x 445 mm
```
Status Draft
Linked Work Items
3.5.1.3 Weight
COS2-56 - WeightThe COPYstation2 will weight under 10 kg.
Status Draft
Linked Work Items
3.5.1.4 Thermal concept
COS2-67 - Thermal conceptFor cooling, the interior of the logger is blown through with internal air. The direction of the fan airflow is to vent the housing to the front. The fresh air should be sucked in from the back.
```
Fans will be used in combination with high air flow and air pressure. An over pressure in the housing should be created. The fans are controlled individually. The final number and the specific fan types are determined in the course of further thermal simulations (noise, backpressure, etc.).
```
For the ventilation concept, fans with a diameter of 60, 80 or 100 mm are used. The air flow of the fans must be sufficiently high.
0 ~ 40 °C/ 32 ~ 104 °F ambient operating temperature range.
Status Draft
Linked Work Items
3.5.1.5 Interlocking mechanism
COS2-68 - Interlocking mechanismMechanical fixation:
When plugged in, the memory cassette is held in position by spring-loaded ball thrust pieces so that no vibrations act on the plug.Locking:
A bolt similar to a door lock is provided. So you can plug in a new memory cartridge at any time and then the latch snaps shut.Eject:
```
To start ejecting a cassette, you have to press a dedicated button on the front of the device. After approval by the PC (complete the writing process if necessary), the latch is released for about 10s (similar to an electronic door opener). After this time the process may haveto be completed, can be restarted.
```
Emergency ReleaseThere is a possibility to open the bolt even when the power is de-energized, e.g. by moving the bolt through the front with a paper clip.
Status Draft
Linked Work Items
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 3of 31
3.5.1.6 Controls
COS2-70 - ControlsThe device has two buttons. One for each cartridge. Three LEDs per bay provide information about the condition of the cartridge.
Status Draft
Linked Work Items
3.5.1.7 Safety
COS2-69 - SafetyThe fans are designed to be inaccessible to fingers and hands by cover plates. Any edges and corners are rounded off accordingly if necessary. Grab handles are provided and enable safe handling of the device.
Status Draft
Linked Work Items
3.5.1.8 Testing
COS2-71 - Hardware considerations for HIL testingIn order to ensure an automated test environment, it is necessary to take into account all the necessary parameters. Depending on the function, the signals must be tapped by means of a test point or jumpers and resistors must be separable.
The following signals are affected
```
Separable:* 4x Detect pin cartridge (MODINSTALLED)
```
```
Accessible (Testpad):* 1x Power button (NO)
```
- 1x Reset button (NO)* 2x Cartridge eject button (NO and NC)
Status Draft
Linked Work Items is derived from: vvHLP-1446 - Testing - HIL tests
3.5.2 Electronics
3.5.2.1 General provisions
Block diagram for requirement specificationBlock diagram for requirement specification.
Define of the required parts and components.
3.5.2.2 Purchased hardware
3.5.2.2.1 Case
COS2-63 - CaseThe case used for the CopyStation2 is a standard 19" server rack. The front panel is replaced by an in-house development. The two cartridges are installed in the two 5.25" drive bays.
The existing USB sockets, power and reset buttons are used in the functions mentioned.
Inter-Tech: IPC 4U-40240Form factor: ATX
```
max. Motherboard size: 305 x 208 mmHeight CPU cooler (max.) 150 mm
```
```
Dimensions (h/w/d): 177.8 x 485 x 445 mm
```
The buttons are processed by the MSP and output to the motherboard. The USB 3 Type A sockets are connected directly to the USB3_34 of the motherboard.
Status Draft
Linked Work Items is derived by: COS2-30 - Evaluate Housing and integration of the cartridges into the system
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 4of 31
3.5.2.2.2 Power Supply
COS2-64 - Power supplyIn order to provide sufficient power, a power supply with a nominal output of 850 watts is used.
be quite!Straight Power 12
```
850 Watt (80 plus platinum)Temperature range is 0°C to 40°C.
```
```
A suitable solution is to use the Delta GPS-1000EB A. The temperature range is 0°C to 50°C (derating from 40°C). 800W are still available at 50°C.
```
Status Draft
Linked Work Items
3.5.2.2.3 Main board and RAM
Which longterm available plattform do we use for our COPY2?
COS2-59 - Server main boardThe mainboard must provide the following functionality:
```
Formactor: ATX or eATX if it fits below the cartridge slots1.At least 3 PCIe x16 slots Gen. 4 (2 for the DATAdrive2, 1 100GBe network card)2.
```
At least 2 PCIe x16 slots providing x4x4x4x4 with HotPlug / Surprise HotPlug3.PCIe Gen. 4 for internal buffer storrage4.
```
1x SSDs for OS and application5.USB 3.2 (20-pin header)6.
```
```
Sleep mode (ACPI S3)7.
```
```
ADVANTECH ASMB-830LGA 4094 AMD® EPYC™ 7002/7003 ATX Server Board with 8x DDR4, 5x PCIe 4.0 x16 + 2x PCIe 4.0 x8, 9x SATA 3, 5x USB 3.2 (Gen1), Dual 10GbE, and IPMI
```
```
LGA 4094 (Socket SP3) ATX server board with AMD EPYC™ 7002/7003 processorDDR4 3200 MHz RDIMM up to 128GB per DIMM
```
Features 5x PCIe 4.0 x16, 2x PCIe 4.0 x8Intel® X550 dual 10GbE ports
```
Eight (via SFF-8643 connector) + one SATA 3 and two M.2 connectors (SATA/PCIe 4.0 compatible)0 ~ 60 °C/ 32 ~ 140 °F ambient operating temperature range
```
RAMTotal 192GByte RAM
6x ASMB-830T2-00A1SQRRD4N32G3K2SRB
Status Draft
Linked Work Items is derived from: COS2-27 - Evaluate CPU scaling Options and RAM size for COPY2
3.5.2.2.4 CPU
How much RAM is needed and why?How many Cores should our CPU have to optimally transfer data between ETH <-> RAM <-> Cartridges <-> Internal Buffer storage?
What are our scaling options?How pricy are those options?
COS2-57 - CPUAchieve exceptional performance and energy efficiency with AMD EPYC™ 7003 series processors for servers.
Name AMD EPYC™ 7443PFamily EPYC
Series EPYC 7003 SeriesForm Factor Servers
# of CPU Cores 24# of Threads 48
Max. Boost Clock Up to 4 GHz
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 5of 31
Base Clock 2.85 GHzL3 Cache 128 MB
1kU Pricing 1337 USDDefault TDP 200W
```
AMD Configurable TDP (cTDP) 165-200WCPU Socket SP3
```
Socket Count 1PLaunch Date 03/15/2021
Status Draft
Linked Work Items is derived from: COS2-27 - Evaluate CPU scaling Options and RAM size for COPY2
3.5.2.2.5 Cooler
COS2-58 - CPU CoolerThe CPU cooler must have enough cooling capacity for the 200W TDP of the CPU used. It must be compatible with socket SP3.
The fan included in the Glyn bundle is used for the CPU.
An alternative is:ARCTIC: Freezer 4U-M Rev. 2
Multicompatible 4U Single Tower CPU CoolerSocket SP3
Status Draft
Linked Work Items
```
3.5.2.2.6 100 GbE Intel(R) Network Adapter E810
```
Which Upload interfaces should we consider?
```
COS2-60 - Network adapterIntel(R) Ethernet Network Adapter E810
```
Port Configuration DualData Rate Per Port
100/50/25/10GbESpeed & Slot Width
16 GT/s x16 lanesController
Intel Ethernet Controller E810
Status Draft
Linked Work Items
3.5.2.2.7 M2.0 System storage
COS2-61 - System storageHardware has not yet been defined!
Status Draft
Linked Work Items
3.5.2.2.8 Local buffer storage
COS2-93 - PCEe 16x Adapter to 4x4 M.2The internal buffer storage is just an option for a future bundle!
```
In order to create a sufficiently large buffer memory, an adapter board from PCIe to M.2 is required. DELOCK offers an adapter with PCIe 4.0 and bifurcation functionality (DELOCK89017 or DELOCK 90090).
```
Status Draft
Linked Work Items
COS2-62 - Local buffer storageThe memory is yet to be determined!
More options are wanted! 16TByte, 32TByte an 64Byte!
A size of 15TByte with lower write rates exist on market at the moment. Sequential data rates of 3500 MB/s.Full speed with 7500 MB/s is just possible with smaller devices of 6-8 TByte size!
Status Draft
Linked Work Items
3.5.2.2.9 Display
COS2-55 - DisplayMatrix Orbital: MOP-AL404C
High quality 40x4 LCD HD44780 compatible controller. Sunlight readable LCD, transflective display. Available as a Serial , I2C or USB 40x4 LCD as the LK404-25 Intelligent 40x4 LCD
Status Draft
Linked Work Items is derived from: COS2-26 - Evaluate which display could be used for the COPY2
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 6of 31
3.5.2.2.10 Lifting magnet
COS2-65 - Lifting magnetsTwo magnets are needed for the locking system of the cartridge. A magnet per cartridge.
With an adapted winding ratio of 5 volts, a current of about 400 mA can be expected. In total, that's about one ampere of current consumption.The magnets are a 6V variant. They are briefly supplied with 12V to generate a sufficiently high starting torque. The voltage is then reduced to a holding voltage of 6V to prevent thermal overload.
Each magnet has a current consumption of about 150 mA at 12 volts supply voltage with the regular winding ratio. So 2 watts.
Status Draft
Linked Work Items is derived from: COS2-30 - Evaluate Housing and integration of the cartridges into the system
3.5.2.3 Engineered Hardware
3.5.2.3.1 ControlBoard Baseboard
COS2-72 - ControlBoard size Board dimensionsThe circuit board for the STM32 is in the middle area of the server case. The assembly will not extend over the entire height. There must be space in the lower part of the case for 80mm, at least 60mm fans.
Status Draft
Linked Work Items
COS2-75 - ControlBoard Connector PowerPower Connector 24 pin for ATX standard is fitted in duplicate, as it is necessary to tap the control signals and standby voltage. Important signals can be monitored or switched by the STM32. The detection of Wake on LAN or Wake on USB is therefore possible.
Key signals are: 5VSB, PS-ON and PG
Status Draft
Linked Work Items
COS2-86 - ControlBoard Connector CartridgeEach cartridge controller is connected with a sufficiently large connector to ensure the following functions:
- 12V power supply and 3.3V* SPI-BUS for communication with EEPROMs and port expanders
- Necessary IO signals that require direct control
Status Draft
Linked Work Items
COS2-87 - ControlBoard Connector DisplayThe display is plugged directly onto the STM32 board.
Status Draft
Linked Work Items
COS2-88 - ControlerBoard Connector ButtomEach button has a separate connector
Status Draft
Linked Work Items
COS2-89 - ControlBoard Connector USB/UART communicationA USB Typ B connector is provided to ensure communication via UART with the STM32. The counterpart is a suitable USB3_5 interface on the motherboard.
There are six LEDs available. POWER, RESET, HDD, NIC1, NIC2 NIC3 and ALARM. It is not yet clear whether all LEDs will be used.
Status Draft
Linked Work Items
COS2-90 - ControlBoard Connector CASE front panel interfaceThe front panel interface for POWER and RESET is routed through the ControlBoard PCB. The signals must be able to be switched by the STM32.
The signals are passed from the STM32 to the motherboard via a second connector.
Status Draft
Linked Work Items
COS2-91 - Controlboard Connector FANSix connections for fans are provided.
Status Draft
Linked Work Items
COS2-92 - ControlBoard Connectors MagnetEach lifting magnet has a separate connector.
Status Draft
Linked Work Items
COS2-77 - STM32 deviceAnalog: STM32U595ZJT6Q
The same STM serves as the microcontroller as in the IPE891 logger system. It will also be used as the code base.In addition to various control pins, the following interfaces are used:
- SPI for communication with EEPROMS and HI side switches.* UART is used for the connection to the motherboard.
- I2C to control the display and FAN controller (possibly also via UART)
Status Draft
Linked Work Items
COS2-78 - USB/UART converterAn RS-232 serial interface from FTDI is used to convert USB to UART.
As an option, USB can be used directly from the integrated USB interface of the STM32.
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 7of 31
Status Draft
Linked Work Items
COS2-79 - ControlBoard display converterThe display is controlled by a serial to parallel converter. A decision between I2C and SPI has yet to be made. For I2C the PCF8574 would be used, for SPI the MCP23S09 or similar.
In addition, two chip select pin signals are required to address two row blocks each. A possibility to dim the intensity of the display backlight is implemented.
Status Draft
Linked Work Items
COS2-80 - ControlBoard FAN controllerA FAN controller is used. A total of six fans can be controlled. All six fans have a tachometer signal. Communication takes place via I2C. The circuit is the same as the fan control in the IPE891. A circuit with MAX31790ATI+ is preferred. Reference circuit below.
It is possible to switch the fan supply of 12 Volt to 24 Volt. A 24 Volt modul is not integrated jet.
Status Draft
Linked Work Items
COS2-76 - ControlBoard cartridge status LEDsThree LEDs are provided for each cartridge to display the status and modes. They are located directly on the pcb. The concept is similar to the scheme of the IPE891 logger system. Optical fiber to the front panel are required.
The LEDs are controlled by an LED driver, such as the PCA9959 or similar. Communication is realized via SPI.
Status Draft
Linked Work Items
COS2-81 - ControlBoard lifting magnet high-side switchThe solenoids are switched using a high-side switch. The switch is designed for the required current strength. A current measurement is provided to detect a fault. An INA241A or a component with comparable properties.
Status Draft
Linked Work Items
COS2-82 - ControlBoard power supply filterThe voltage provided by the power supply is further smoothed by PI filters to ensure a stable, constant voltage. 3V3, 5VSB, 5V and 12V
Status Draft
Linked Work Items
COS2-83 - ControlerBoard FusesThe power supply already has over voltage and over current protection.
Status Draft
Linked Work Items
3.5.2.3.2 Cartridge controller board
COS2-73 - PCB size cartridgecontrolThe control of the data lines, signals, clock and voltage levels must find space on this circuit board.
The adapter board must have contour cutouts that allow ventilation of the cartridge! It must be narrow enough to ensure easy installation and removal, as it must be replaceable as a wearing part.
Status Draft
Linked Work Items
COS2-94 - CartridgeAdapter RedriverTI's DS160PR810 is used as the redriver of the PCEe lanes. This is PCIe 4.0 capable. Two rerivers are required per cartridge. The circuit is based on the circuit diagram of the evaluation module DS160PR810EVM-RSC.
Status Draft
Linked Work Items
COS2-96 - CartridgeAdapter HS-SwitchThe TI LM74910 is used as a high-side switch for controlling the cartridge's memory cards. Mosfet is still to be designed according to the required current peak. The assumption is 4 cards with 15W peak power consumption each, which results in a current of 18 amps by
3.3 volt.
Status Draft
Linked Work Items
COS2-84 - Cartridge PCB EEPROMThe cartridges are equipped with an EEPROM. Information such as serial number and mating cycles should be able to be queried.
Status Draft
Linked Work Items
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 8of 31
3.6 Software functions / blocks
3.6.1 Operating system
3.6.1.1 Functional Requirements
vvHLP-1542 - Software component initializationCOPYstation2 software must initialize all of its components on system start-up.
```
Rationale: Initialization need to perform to start all supporting functions.
```
Status Implemented
Linked Work Items
has parent: vvHLP-1153 - Functional Requirements ,is implemented by: vvHLP-1557 - datalog init understanding and code walkthrough ,
is implemented by: vvHLP-1748 - cs2 rework ,is implemented by: vvHLP-1749 - cs2 integration task and wrapping injectors ,
is related to: vvHLP-1558 - Initial placeholder for cs2 init ,is related to: vvHLP-1564 - di injector for cs2 block device manager and use in cs2 init ,
is related to: vvHLP-1565 - cs2 executable cmake changes, mock script file to run cs2 executable in container ,is related to: vvHLP-1669 - cs2 default folders code improvements and cmake changes ,
is related to: vvHLP-1705 - Default location for logging and config for cs2, ccs2block device manager changes
3.6.1.2 Non-functional requirements
3.6.2 HW Platform control
3.6.2.1 Functional Requirements
vvHLP-2328 - HW Platform control - Communication with the PowerControllerThe COPYstation2 software must open a connection to the PowerController on the system over UART. The used application protocol to access the PowerController's functions over this connection is defined in http://gitlab.caetec:8929/logger-
firmware/powercontroller/ipe891/ipe891_powercontroller_stm32_common
```
Note: This allows the COPYstation2 software to detect hardware events (e.g. cartridge hot-plug) and control certain aspects of the embedded system (e.g. cartridge state, watchdog, etc.)
```
Status Draft
Linked Work Items
has parent: vvHLP-1159 - Functional Requirements ,is derived from: vvHLP-1078 - Cartridge hotplug detection - mounting ,
is derived from: vvHLP-1247 - Display network parameters on the integrated display ,is derived from: vvHLP-1248 - Display transfer status on the integrated display ,
is implemented by: vvHLP-2329 - Integration of the COPYstation2 SW and HW
3.6.2.1.1 Cartridge detection to mounting
vvHLP-1329 - Cartridge - Detect the inserted cartridgesCOPYstation2 shall monitor block device hot plug events and set the state of newly added storage to detected
Status Implemented
Linked Work Items
has parent: vvHLP-1338 - Cartridge detection to mounting ,is derived from: vvHLP-1078 - Cartridge hotplug detection - mounting ,
is implemented by: vvHLP-1838 - Cartridge hotplug detection - mounting ,is implemented by: vvHLP-1503 - Enable automount for USB
vvHLP-1328 - Cartridge - Mount on detectionCOPYstation2 shall attempt to mount the detected storage.
Status Implemented
Linked Work Items
has parent: vvHLP-1338 - Cartridge detection to mounting ,is derived from: vvHLP-1078 - Cartridge hotplug detection - mounting ,
is implemented by: vvHLP-1838 - Cartridge hotplug detection - mounting ,is implemented by: vvHLP-1503 - Enable automount for USB ,
is implemented by: vvHLP-1523 - Revert automount USB
vvHLP-1339 - Read cartridge Health statusCOPYstation2 shall read SMART data of each individual drives in cartridge when it is detected state.
Status Approved
Linked Work Itemshas parent: vvHLP-1338 - Cartridge detection to mounting ,is derived from: vvHLP-1351 - Track the health status of the Cartridge. ,is implemented by: vvHLP-1778 - Track the health status of the Cartridge and Log warnings
vvHLP-1289 - Cartridge - Update mount stateCOPYstation2 shall set the storage to mounted state on completion of the mount operation.
Status Implemented
has parent: vvHLP-1338 - Cartridge detection to mounting ,
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 9of 31
Linked Work Itemsis derived from: vvHLP-1078 - Cartridge hotplug detection - mounting ,is implemented by: vvHLP-1838 - Cartridge hotplug detection - mounting ,is implemented by: vvHLP-1522 - Set the USB storage to mounted ,
is implemented by: vvHLP-1544 - Implementation of vvHLP-1289 - Cartridge - Update mount state
vvHLP-1483 - Cartridge - Mount failureCOPYstation2 shall set the storage state to hardware error state if the mounting operation is not completed within 30 seconds.
```
Rationale: Healthy disk should ideally be mounted < 30 secs.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1338 - Cartridge detection to mounting ,is derived from: vvHLP-1078 - Cartridge hotplug detection - mounting ,is implemented by: vvHLP-1838 - Cartridge hotplug detection - mounting
vvHLP-1297 - Cartridge unlockCOPYstation2 shall initiate unlock cartridge via power controller upon cartridge state change to unmounted.
Status Implemented
Linked Work Itemshas parent: vvHLP-1338 - Cartridge detection to mounting ,is derived from: vvHLP-1132 - Cartridge hotplug - unlock ,is implemented by: vvHLP-2182 - API function to request cartridge eject
vvHLP-1310 - Cartridge Hotplug - UnmountCOPYstation2 shall attempt to unmount the storage upon unmount request.
Status Implemented
Linked Work Items
has parent: vvHLP-1338 - Cartridge detection to mounting ,is derived from: vvHLP-1133 - Cartridge hotplug - unmount request ,
```
is implemented by: vvHLP-1547 - Mock the CS2 power controller ,is implemented by: vvHLP-1548 - Implementation of USB Hotplug - Unmount (vvHLP-1310) ,
```
```
is implemented by: vvHLP-1549 - Implementation of Cartridge Hotplug - Unmount(vvHLP-1310)
```
vvHLP-1493 - Cartridge Eject request from webUICOPYstation2 shall have Cartrige Eject button option on webUI.
Status Implemented
Linked Work Itemshas parent: vvHLP-1338 - Cartridge detection to mounting ,is derived from: vvHLP-1133 - Cartridge hotplug - unmount request ,is implemented by: vvHLP-2160 - Cartridge Eject request from webUI
vvHLP-1492 - Cartridge Hotplug - Unmount request on unlock button via power controllerCOPYstation2 shall raise a unmount request on press of unlock button via power controller
Status Rejected
Linked Work Itemshas parent: vvHLP-1338 - Cartridge detection to mounting ,is derived from: vvHLP-1133 - Cartridge hotplug - unmount request ,is implemented by: vvHLP-2176 - Cartridge Hotplug - Unmount request on unlock button via power controller
vvHLP-1486 - Cartridge Hotplug - Unmount failureCOPYstation2 shall set the storage to failed state if the unmounting operation is not completed within 30 seconds.
```
Note:Possible failure cases
```
```
Drive is busy(Process is still accessing file or folder)Drive is failing and final flushing of buffers is not possible.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1338 - Cartridge detection to mounting ,is derived from: vvHLP-1133 - Cartridge hotplug - unmount request ,is implemented by: vvHLP-1707 - Cartridge Hotplug - Unmount failure
vvHLP-1485 - Cartridge Hotplug - Update unmounted stateCOPYstation2 shall set the storage to unmounted state on completion of the unmount operation.
Status Implemented
Linked Work Items has parent: vvHLP-1338 - Cartridge detection to mounting ,is derived from: vvHLP-1133 - Cartridge hotplug - unmount request
vvHLP-1484 - Cartridge Hotplug - Abort all jobs on unmount requestCOPYstation2 must set all transfer jobs to "Cancelled" state before the unmount process is initiated.
Status Implemented
Linked Work Items
has parent: vvHLP-1338 - Cartridge detection to mounting ,is derived from: vvHLP-1133 - Cartridge hotplug - unmount request ,
is implemented by: vvHLP-1702 - Cartridge Hotplug - Notify the unmount request to other components to abort all jobs ,is implemented by: vvHLP-1722 - Cartridge Hotplug - Implement the cancelled state for job in transfer module ,
is implemented by: vvHLP-1732 - Cartridge Hotplug - Discard parsing the event when unmount action is received ,is related to: vvHLP-1782 - Crash observed on ejecting the Storage Device ,
is related to: vvHLP-1547 - Mock the CS2 power controller
vvHLP-1385 - Operation mode settingCOPYstation2 shall change the operation mode from Automatic to API and vice versa.
Licensing error should be logged with correct error code and relevant error message.
Status Implemented
Linked Work Items
has parent: vvHLP-1338 - Cartridge detection to mounting ,is derived from: vvHLP-1463 - Switching between API and Automatic mode ,
is implemented by: vvHLP-1768 - Validate the API License availability on request to switch from Auto to API mode ,is implemented by: vvHLP-1956 - Operation mode setting
3.6.2.2 Non-functional requirements
3.6.3 Configuration
vvHLP-1506 - Configuration JSON schema validation on importCOPYstation2 shall validate the JSON schema for the configuration on settings import.
Status Rejected
Linked Work Itemshas parent: vvHLP-1505 - Configuration ,is derived from: vvHLP-1439 - Import configuration settings on COPYstation2 via WebUI ,is implemented by: vvHLP-2161 - Configuration JSON schema validation on import
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 10of 31
3.6.4 Update
vvHLP-1476 - Update installation information webUICOPYstation2 must provide the information about the status of the installation of update package. Prompt user for the restart option with restart now and restart later on the webUI
```
Status: In Progress, Success or FailurePossible failure conditions:
```
Downgrading the versionsDULA file corruption.
Invalid file.missing dependencies
File upload failure when using DLUA upload.Download failure when using server option.
```
Note: More failure condition can be added during the development.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1475 - Update ,is derived from: vvHLP-1433 - Update installation information on webUI ,is implemented by: vvHLP-2158 - Update installation information webUI
vvHLP-1479 - Update software package via DLUA uploadCOPYstation2 shall initiate the software update from the uploaded DLUA file upon validation of the file uploaded.
Status Implemented
Linked Work Items
has parent: vvHLP-1475 - Update ,is derived from: vvHLP-1432 - Update software package using DLUA file upload via webUI ,
is implemented by: vvHLP-1900 - Update software package via DLUA upload ,is implemented by: vvHLP-1973 - CS2 Update Manager 'Implementation analysis'
vvHLP-1478 - web UI option to update software package from the serverCOPYstation2 must provide option to user to update software package from the server on webUI.
Status Implemented
Linked Work Itemshas parent: vvHLP-1475 - Update ,is derived from: vvHLP-1425 - Update software package using remote server ,is implemented by: vvHLP-2159 - web UI option to update software package from the server
vvHLP-1477 - Update software package from USBCOPYstation2 should install the software package based on the user selection.
Status In Progress
Linked Work Itemshas parent: vvHLP-1475 - Update ,is derived from: vvHLP-1426 - Update software package using the local storage or USB ,is implemented by: vvHLP-1899 - Update software package from USB
3.6.5 Data enumeration and Job management
3.6.5.1 Functional Requirements
3.6.5.1.1 Dataset enumeration
```
vvHLP-1292 - Dataset enumeration - Enumerate of datasets on the cartridgeCOPYstation2 shall enumerate the files available on the cartridge, on cartridge state changed to mounted for dataset information file(<datasetName>.JSON).
```
Status Implemented
Linked Work Items
has parent: vvHLP-1349 - Dataset enumeration ,is derived from: vvHLP-1334 - Automatic data processing on cartridge insertion ,
is implemented by: vvHLP-1837 - Automatic data processing on cartridge insertion ,is implemented by: vvHLP-1520 - Enumeration to be done folder by folder for Peripheral Storage ,
is implemented by: vvHLP-1556 - Enumerate the files in the block device ,is implemented by: vvHLP-1728 - Send Relative path of dataLocation and only filenames to JsonParser
vvHLP-1487 - Dataset enumeration - Update the cartridge state as busyCOPYstation2 shall update the cartridge state busy before initiating the dataset enumeration.
** Transition between Idle state to busy state conditions:1. When Enumeration of file is running
2. When one or more JSON file is pending for parse or parsing is in progress3. When one or more transfer job is in enqueued, paused or running state
Status Implemented
Linked Work Items
has parent: vvHLP-1349 - Dataset enumeration ,is derived from: vvHLP-1334 - Automatic data processing on cartridge insertion ,
is implemented by: vvHLP-1837 - Automatic data processing on cartridge insertion ,is implemented by: vvHLP-1704 - Dataset enumeration - Update the cartridge state as busy
```
vvHLP-1489 - Create transfer job descriptionCOPYstation2 must create a transfer job description based on the parsed JSON(dataset information file) data.
```
Status Implemented
Linked Work Items
has parent: vvHLP-1349 - Dataset enumeration ,is derived from: vvHLP-1334 - Automatic data processing on cartridge insertion ,
is implemented by: vvHLP-1837 - Automatic data processing on cartridge insertion ,is implemented by: vvHLP-1684 - Create job description for validated JSON files
3.6.5.1.2 JSON Parsing
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 11of 31
JSON parsing includes:
Dataset Definition JSON schema version support check1.JSON schema validation2.
JSON file parsing3.Reading the metadata from JSON4.
```
Decrypting the encrypted JSON5.As in dataLog the GPG ascii file is being saved encrypted, so need to save here as well. (TBD)6.
```
vvHLP-1314 - JSON Schema Validation for dataset definition fileCOPYstation2 shall validate the dataset definition JSON files against current dataset definition JSON schema [JSONInfo]
Status Implemented
Linked Work Items
has parent: vvHLP-1348 - JSON Parsing ,is derived from: vvHLP-1181 - JSON File processing ,
```
is implemented by: vvHLP-1836 - JSON File processing ,is implemented by: vvHLP-1551 - Implementation of JSON Schema Validation for dataset definition file( vvHLP-1314) ,
```
is related to: vvHLP-1563 - dataset json validation understanding and initial boiler plate code
vvHLP-1312 - Dataset definition JSON File parsingCOPYstation2 shall parse dataset definition JSON file to extract all information required to create a transfer job after successful validation of the JSON file schema.
Status Implemented
Linked Work Items
has parent: vvHLP-1348 - JSON Parsing ,is derived from: vvHLP-1181 - JSON File processing ,
```
is implemented by: vvHLP-1836 - JSON File processing ,is implemented by: vvHLP-1550 - Implementation of Dataset definition JSON File parsing (vvHLP-1312)
```
vvHLP-1331 - Dataset completenessCOPYstation2 must verify that all files listed in the JSON are available and complete.
Status Implemented
Linked Work Items
has parent: vvHLP-1348 - JSON Parsing ,is derived from: vvHLP-1181 - JSON File processing ,
```
is implemented by: vvHLP-1836 - JSON File processing ,is implemented by: vvHLP-1552 - Implement Dataset verification (vvHLP-1331)
```
vvHLP-1313 - Decrypting the encrypted JSONCOPYstation2 shall decrypt the encrypted JSON files using available private gpg keys report if there is error during decryption in logs.
```
Constraint:
```
The decrypted JSON file must not be stored on any local or removable drive.1.Only root user should have access to /var/copystation2_cache/cfg/keys2.
Status Implemented
Linked Work Itemshas parent: vvHLP-1348 - JSON Parsing ,is derived from: vvHLP-1177 - Decrypt JSON File processing ,is implemented by: vvHLP-1766 - Decrypt JSON File processing
3.6.5.1.3 Job management
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 12of 31
Figure 2 JobStatesvvHLP-1347 - Creating jobs for enumerated datasets
COPYstation2 shall create job on enumerated datasets.
```
Job can only be created once enumeration data is available. (vvHLP-1292)Jobs will be created by scheduler and will have initial state as 'Created'.
```
If job creation failed then it should be reported with error "JOB_CREATION_FAILED" and its reason.
Status Rejected
Linked Work Items has parent: vvHLP-1350 - Job management
vvHLP-1319 - Abort transfer jobs of a storage/cartridgeCOPYstation2 shall abort current transfer jobs for a selected cartridge on request from webUI/API. Internally if the current job state is enqueued, running or paused then it should be stopped and then to the cancelled state. Prompt should be shown with a warning message
to the user that "All the running jobs will be aborted. Aborted jobs can not be restarted". proceed on user inputPlease refer transfer job states 3.6.5.1.3 - Job management
Status Implemented
Linked Work Itemshas parent: vvHLP-1350 - Job management ,is derived from: vvHLP-1182 - Actions on the cartridge slot ,is implemented by: vvHLP-1858 - Abort transfer jobs of a storage/cartridge
vvHLP-1363 - Stop transfer jobs of a storage/cartridgeCOPYstation2 shall stop running and enqueued transfer jobs for a selected storage/cartridge. Prompt should be shown with a warning message to the user that "All the running jobs will be stopped". proceed on user input
Please refer transfer job states 3.6.5.1.3 - Job management
Status Implemented
Linked Work Items
has parent: vvHLP-1350 - Job management ,is derived from: vvHLP-1182 - Actions on the cartridge slot ,
is implemented by: vvHLP-1857 - Restart Transfer Jobs of a storage/cartridge ,is implemented by: vvHLP-1897 - Stop transfer jobs of a storage/cartridge
vvHLP-1318 - Restart Transfer Jobs of a storage/cartridgeCOPYstation2 shall restart current transfer jobs for a selected cartridge. Prompt should be shown with a warning message to the user that "All the running jobs will be stopped before restarting". if at least one job is in running state proceed on user choice.
Please refer transfer job states 3.6.5.1.3 - Job management
Status Implemented
Linked Work Itemshas parent: vvHLP-1350 - Job management ,is derived from: vvHLP-1182 - Actions on the cartridge slot ,is implemented by: vvHLP-1857 - Restart Transfer Jobs of a storage/cartridge
vvHLP-1322 - Abort a selected transfer job
COPYstation2 shall abort a selected transfer job based on the request from webUI/API. Prompt should be shown with a warning message to the user that "Job will be aborted and can only be restarted by cartridge reinsertion". Set the job state to "Cancelled".Please refer transfer job states 3.6.5.1.3 - Job management
Status Verified
Linked Work Itemshas parent: vvHLP-1350 - Job management ,is derived from: vvHLP-1183 - Actions on the transfer job ,is implemented by: vvHLP-1896 - Abort a selected transfer job
vvHLP-1364 - Stop a selected transfer jobCOPYstation2 shall stop the selected transfer job based on the request from the webUI/API. Prompt should be shown with a warning message to the user that "Job will be stopped "and proceed on user choice.
Please refer transfer job states 3.6.5.1.3 - Job management
Status Verified
Linked Work Itemshas parent: vvHLP-1350 - Job management ,is derived from: vvHLP-1183 - Actions on the transfer job ,is implemented by: vvHLP-1896 - Abort a selected transfer job
vvHLP-1320 - Restart a selected transfer jobCOPYstation2 shall restart the selected transfer job based on the request from webUI/API
Please refer transfer job states 3.6.5.1.3 - Job management
Status Implemented
Linked Work Itemshas parent: vvHLP-1350 - Job management ,is derived from: vvHLP-1183 - Actions on the transfer job ,is implemented by: vvHLP-1894 - Restart a selected transfer job
vvHLP-1324 - Pause a selected transfer jobCOPYstation2 shall pause a selected transfer job based on the request from webUI/API. Set the job status as "Paused"
Please refer transfer job states 3.6.5.1.3 - Job management
Status Implemented
Linked Work Itemshas parent: vvHLP-1350 - Job management ,is derived from: vvHLP-1183 - Actions on the transfer job ,is implemented by: vvHLP-1852 - Pause and resume a selected transfer job
vvHLP-1323 - Resume a job with specific job IdCOPYstation2 shall Resume a selected transfer job based on the request from webUI/API. Set the job status as "Running".
Please refer transfer job states 3.6.5.1.3 - Job management
Status Implemented
Linked Work Itemshas parent: vvHLP-1350 - Job management ,is derived from: vvHLP-1183 - Actions on the transfer job ,
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 13of 31
is implemented by: vvHLP-1852 - Pause and resume a selected transfer job
vvHLP-1327 - Implementation to change the transfer job order
COPYstation2 shall do transfer job ordering on various conditions.
Transfer job ordering options to support:
Options for custom prioritizing the transfer job/jobs1.Dataset creation time ascending/descending2.
Dataset size ascending/descending3.Dataset name A-Z / Z-A4.
Job source A-Z / Z-A5.Job destination A-Z / Z-A6.
Ordering operation should do:
The order of job can be changed on any one of the above parameter.1.Order can only be changed when the jobs are enqueued/stopped state.2.
On change of the options selected by the user transfer job under the enqueued jobs will reorder the jobs that are in the running queue is not affected by the changes.3.If user intends to change the order of the running jobs the jobs must be stopped before reordering.4.
Custom priority can be achieved by a drag and drop similar feature in webUI.5.Custom priorities for the transfer job/jobs can be achieved by selection of one or more jobs in the enqueued job list and with move up, move down, move last or move top options6.
Default order:Dataset creation time in ascending order
Status Implemented
Linked Work Items
has parent: vvHLP-1350 - Job management ,is derived from: vvHLP-1184 - Allow to change the transfer job order ,
is implemented by: vvHLP-1963 - API function to support prioritization of transfer jobs and Implementation to change the transfer job order ,is related to: vvHLP-1928 - Design for prioritization of transfer jobs
3.6.5.1.4 Local Buffer
```
vvHLP-1356 - Function to check the available storage spaceCOPYstation2 shall check the available disk space in a specific storage path (Local), the available storage should be calculate based on the storage + the storage required by the enqueued jobs with the path as destination.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1355 - Local Buffer ,is derived from: vvHLP-1178 - Offload the data from the cartridge ,is implemented by: vvHLP-1760 - Offload the data from the cartridge excluding UI option
vvHLP-1299 - Offloading of cartridge datasets to Local BufferCOPYstation2 shall create the transfer job with the destination as local buffer path if the offloading option is configured by the user and if the storage space available at the local buffer path.
Status Implemented
Linked Work Items
has parent: vvHLP-1355 - Local Buffer ,is derived from: vvHLP-1098 - Automatic dataset uploads- Offload the cartridge data ,
is derived from: vvHLP-1178 - Offload the data from the cartridge ,is implemented by: vvHLP-1760 - Offload the data from the cartridge excluding UI option
```
vvHLP-1298 - Upload to remote target from Local Buffer(retry on failure)COPYstation2 shall track the failed transfer job for the dataset with source as the Local storage and destination as the remote server and retry failed transfer jobs periodically (every 30 minutes).
```
```
Rationale: Files that belong to a failed transfer job does not get deleted which could lead to storage consumption on the local storage.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1355 - Local Buffer ,is derived from: vvHLP-1178 - Offload the data from the cartridge ,is implemented by: vvHLP-1760 - Offload the data from the cartridge excluding UI option
vvHLP-1361 - Clear all data on storageCOPYstation2 shall clear the data on any storage.
The storage mount point should be the identification for storage.If required a filter of data can be applied to select the data which need to be deleted. Or the data that need to be skipped for clear.
The error during clear should be logged.
Status Rejected
Linked Work Items has parent: vvHLP-1355 - Local Buffer ,is derived from: vvHLP-1178 - Offload the data from the cartridge
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 14of 31
3.6.5.1.5 Logging
vvHLP-1302 - Logging system for COPYstation2COPYstation2 shall reuse the logging mechanism of dataLog.
Status Implemented
Linked Work Items
has parent: vvHLP-1362 - Logging ,is derived from: vvHLP-1070 - Download log files ,
is derived from: vvHLP-1199 - Display log messages ,is derived from: vvHLP-1242 - Log files download option ,
```
is implemented by: vvHLP-1546 - Implementation of Logging system for COPYstation2 (vvHLP-1302)
```
vvHLP-1305 - Information to be logged in COPYstation2COPYstation2 shall capture below information, while discarding duplicate messages to avoid excessive logging, but not limited to:
Entry and exit points of COPYstation2.1.Errors with error codes2.
Exceptions with its its reason3.Log the action with details such as timestamp, user initiating the abort, and affected jobs.4.
COPYstation2 must not log the sensitive information such as:
Default target server sensitive information like SFTP user password, Azure SAS token etc.1.Primary target authentication information mentioned in JSON.2.
GPG key details.3.
```
Note: This can also be achieved by masking the critical data before printing it to the log.Log format should be similar to dataLog.
```
Status Implemented
Linked Work Items
has parent: vvHLP-1362 - Logging ,is derived from: vvHLP-1070 - Download log files ,
is derived from: vvHLP-1199 - Display log messages ,is derived from: vvHLP-1242 - Log files download option
vvHLP-1527 - Display log messages on webUICOPYstation2 shall display the log messages on webUI.
Status Implemented
Linked Work Itemshas parent: vvHLP-1362 - Logging ,is derived from: vvHLP-1199 - Display log messages ,is implemented by: vvHLP-2014 - Display log messages on webUI
3.6.5.2 Non-functional requirements
3.6.6 Data transfer
3.6.6.1 Functional Requirements
The dataset should be transferred to target server.1.If previous target server failed then transfer job server detail should be updated with next target server details in the list.2.
```
Start the transfer job with updated target server details.3.The target server list should have default server entry at last,( if default server information is available).4.
```
Target servers to support:
SFTP1.Azure2.
AWS3.SMB4.
Local File system5.
```
Errors:
```
```
TRANSFER_ABORT_FAILED : Abort transfer jobs of a storage/cartridge failedTRANSFER_STOP_FAILED : Stop transfer jobs of a storage/cartridge failed
```
```
TRANSFR_RESTART_FAILED : Restart Transfer Jobs of a storage/cartridge failedJOB_ABORT_FAILED : Abort a selected transfer job faild
```
```
JOB_STOP_FAILED : Stop a selected transfer job failedJOB_RESTART_FAILED : Restart a selected transfer job failed
```
```
PAUSE_PAUSE_FAILED : Pause a selected transfer job failedJOB_RESUME_FAILED : Resume a job with specific job Id failed
```
```
CONNECTION_TIMEOUT : Connection to target server take more than 2 seconds.NETWORK_ERROR: not able to connect due to network unavailability
```
```
SERVER_UNAVAILABLE: the target Server is not available(no response for the request)
```
3.6.6.1.1 Network Connection check
vvHLP-1368 - Validate the private gpg keys during upload via APICOPYstation2 shall validate if the gpg key is private and not password protected on the attempt upload via API.
Status Implemented
Linked Work Items
has parent: vvHLP-1374 - Network Connection check ,is derived from: vvHLP-1177 - Decrypt JSON File processing ,
is implemented by: vvHLP-1859 - Option to upload GPG private key in API and Import the GPG key information uploaded from webUI/API. ,is implemented by: vvHLP-1898 - Validate the private gpg keys during upload via API
vvHLP-1378 - Limit maximum parallel job transfersCOPYstation2 shall limit the amount of running transfer jobs to the configured values for maximum parallel running job count in total and maximum parallel running transfer per target.
```
Note:Default Configuration:
```
Maximum number of parallel running transfer jobs in the system: 64Maximum number of parallel running transfer jobs per target: 32
Lower limit: 1Upper limit: 64
```
Limitation:The change/update of this value should not be allowed while transfer is in progress.
```
During development, Configured values should be checked and if other values provide a better performance, the default values should be changed accordingly.
Status Implemented
Linked Work Itemshas parent: vvHLP-1374 - Network Connection check ,is derived from: vvHLP-1256 - Maximum parallel file transfers ,is implemented by: vvHLP-1826 - Maximum parallel file transfer
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 15of 31
3.6.6.1.2 Create connection to target
vvHLP-1370 - Choose next available target server for dataset upload if the primary target server failsCOPYstation2 shall choose next available target server from the destination list in case of transfer failure to the current target server.
Status Implemented
Linked Work Items
has parent: vvHLP-1371 - Create connection to target ,is derived from: vvHLP-1197 - Use additional target servers if primary target failed ,
is implemented by: vvHLP-1835 - Use additional target servers if primary target failed ,is implemented by: vvHLP-1683 - Tests to check uploading for next target server if primary target server fails
vvHLP-1369 - Choose default server for dataset uploadCOPYstation2 shall choose default server to upload the datasets.
If the connection to all target servers in the list are failed then the upload should happen with default server, which will be at last in the list.
Status Rejected
Linked Work Items has parent: vvHLP-1371 - Create connection to target
vvHLP-1366 - Create transfer job based on job descriptionCOPYstation2 shall create a transfer job based on the created Job description.
Status Implemented
Linked Work Itemshas parent: vvHLP-1371 - Create connection to target ,is derived from: vvHLP-1239 - Transfer module reuse ,is related to: vvHLP-1521 - Request to add job to group using the created job id
vvHLP-1496 - Manage the transfer job group
COPYstation2 shall manage the job group based on storage state change create/delete transfer job group.
Status Implemented
Linked Work Items
has parent: vvHLP-1371 - Create connection to target ,is derived from: vvHLP-1239 - Transfer module reuse ,
is related to: vvHLP-1534 - Create transfer job group based on storage ,is related to: vvHLP-1535 - Delete transfer job group when storage is unavailable
vvHLP-1495 - Transfer the files that is listed in the transfer job
COPYstation2 shall attempt to transfer the files listed in the Job description to the first destination on the destinations list.NOTE: Attempt to transfer to additional targets is cover by vvHLP-1197
Status Implemented
Linked Work Items has parent: vvHLP-1371 - Create connection to target ,is derived from: vvHLP-1239 - Transfer module reuse
3.6.6.1.3 Data transfer to target server
vvHLP-1367 - Update the transfer job stateCOPYstation2 shall update the transfer job status upon a change of the job state.
Refer to: L3 - Transfer module - job state diagram
Status Implemented
Linked Work Items
has parent: vvHLP-1372 - Data transfer to target server ,is derived from: vvHLP-1239 - Transfer module reuse ,
is implemented by: vvHLP-1681 - Update Transfer job state ,is related to: vvHLP-1562 - Pending unit tests for cTargetWorker
```
vvHLP-1499 - Update the transfer job progressCOPYstation2 shall update the transfer job progess in percentage(%) with respect to the total size of all the files in the job.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1372 - Data transfer to target server ,is derived from: vvHLP-1239 - Transfer module reuse ,is related to: vvHLP-1667 - Update transfer progress for each job
vvHLP-1524 - Display the Job progress under the cartridgeCOPYstation2 shall display the job progress under the cartridge.
Possible Information:Upload %
```
File/Job/dataset countFile progress count (API)
```
Upload speedETA
Status Implemented
Linked Work Items
has parent: vvHLP-1372 - Data transfer to target server ,is derived from: vvHLP-1110 - CopyStation2 must display the cartridge state for the user ,
is implemented by: vvHLP-2013 - Display the Job progress under the cartridge ,is related to: vvHLP-1525 - Request to create job group ,
is related to: vvHLP-1526 - Request to delete the job group
```
vvHLP-1498 - Update the transfer job group progressCOPYstation2 shall update the group(cartridge, Local storage) progress based on the job progress changes.
```
Information to maintain based on compilation of all the jobs for the group:
```
Upload rate (Size in Bytes/sec)1.Percentage (based on size) [Cancelled job will also be included as part of the calculation]2.
```
```
Number of jobs processed [Running, Finished, Cancelled]/Total number of jobs (As a Percentage)3.
```
Status Implemented
Linked Work Items
has parent: vvHLP-1372 - Data transfer to target server ,is derived from: vvHLP-1110 - CopyStation2 must display the cartridge state for the user ,
is implemented by: vvHLP-1685 - Update the number of Jobs Processed ,is related to: vvHLP-1700 - Upload rate Implementation ,
is related to: vvHLP-1723 - Percentage in Jobs
vvHLP-1500 - Maintain the transfer job state change infoCOPYstation2 shall maintain the list of transfer job state changes, possibly including user readable explanation messages.
```
Note: This can be implemented using regular system log.
```
Status Implemented
Linked Work Items has parent: vvHLP-1372 - Data transfer to target server ,is derived from: vvHLP-1239 - Transfer module reuse
vvHLP-1296 - Add default target details from config to job descriptionCOPYstation2 must append the configured default target to the destination list of each job description before creating the corresponding transfer job.
Status Implemented
Linked Work Items
has parent: vvHLP-1372 - Data transfer to target server ,is derived from: vvHLP-1180 - Default target for transfer jobs ,
is derived from: vvHLP-1701 - Testing upload ,
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 16of 31
```
is implemented by: vvHLP-1545 - Implementation of Add default target details from config to job description (vvHLP-1296)
```
vvHLP-1373 - Delete the successfully transferred dataCOPYstation2 shall delete the successfully transferred datasets.
Delete should only happen when all the files of the transfer job are uploaded. The system should delete all files of datasets.Dataset integrity need to be maintained.
Status Implemented
Linked Work Items
has parent: vvHLP-1372 - Data transfer to target server ,is derived from: vvHLP-1198 - Delete successfully transferred files ,
```
is implemented by: vvHLP-1834 - Delete successfully transferred files ,is related to: vvHLP-1765 - Deletion of dataset file(json) failing after successful upload ,
```
is related to: vvHLP-1533 - Add post job run hook to delete the datasets after successful upload
3.6.6.1.4 Target servers
vvHLP-1375 - Support for SFTP serverCOPYstation2 shall support the SFTP target server.
Transfer job must be able to connect to the with configured SFTP server. vvHLP-1366Transfer job must be able to authenticate the user credential with configured SFTP server.
Transfer job must be able to initiate a session for the data transfer with configured SFTP server.System must be able handle the SFTP protocol related errors.
Status Implemented
Linked Work Items
has parent: vvHLP-1376 - Target servers ,is derived from: vvHLP-1219 - Support for SFTP server as transfer target ,
is implemented by: vvHLP-1833 - Support for SFTP server as transfer target ,is implemented by: vvHLP-1510 - SFTP cpp Implementation
3.6.6.2 Non-functional requirements
3.6.7 API
3.6.7.1 Functional Requirements
vvHLP-1315 - Option to upload GPG private key in APICOPYstation2 shall provide an API function to the user for uploading the private GPG key.
Status Implemented
Linked Work Itemshas parent: vvHLP-1166 - Functional Requirements ,is derived from: vvHLP-1177 - Decrypt JSON File processing ,is implemented by: vvHLP-1859 - Option to upload GPG private key in API and Import the GPG key information uploaded from webUI/API.
vvHLP-1317 - Option to Abort/Stop/Restart all transfer jobs of specific slot through APICOPYstation2 shall provide an API function to Abort/Stop/Restart of current ongoing transfer job of a specific slot.
```
Note:Single API function for all type of request and single API function for all type of response. User need to pass the action as parameter in request API.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1166 - Functional Requirements ,is derived from: vvHLP-1182 - Actions on the cartridge slot ,is implemented by: vvHLP-1957 - Option to Abort/Stop/Restart all transfer jobs of specific slot through API
vvHLP-1321 - Actions to perform on a selected transfer job through API
COPYstation2 shall provide an API function to Enqueue, Pause, Resume, Stop, Cancel and Restart a selected transfer job.Enqueue a job with specific job Id
User must be able enqueue a job using the API function with Job Id as the parameter.1.Set the job status as Enqueued.2.
Pause a job with specific job Id
User must be able pause a running job using the API function with Job Id as the parameter.1.Set the job status as Paused.2.
```
Note: try to keep the seek for the file being transferred so that we can resume from the point where it was paused.
```
Resume a job with specific job Id
User must be able resume a paused job using the API function with Job Id as the parameter.1.Set the job status as enqueued.2.
```
Note: Use the seek, if available for the file being transferred so that we can resume from the point where it was paused.
```
Stop a job with specific job Id
User must be able to stop only Running or Paused job using the API function with Job Id as the parameter.1.Set the job status as stopped.2.
Restart a job with specific job Id
User must be able restart only stopped job using the API function with Job Id as the parameter.1.Set the job status as enqueued.2.
Cancel a job with specific job Id
User must be able cancel an enqueued, paused or running job using the cancel function of the API using the Job Id as the parameter.1.Set the job status as cancelled.2.
```
Note:Single API function for all type of request and single API function for all type of response. User need to pass the action as parameter in request API.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1166 - Functional Requirements ,is derived from: vvHLP-1183 - Actions on the transfer job ,is implemented by: vvHLP-1895 - Actions to perform on a selected transfer job through API
vvHLP-1326 - API function to support prioritization of transfer jobsCOPYstation2 shall provide API functions for prioritizing the transfer jobs.
```
Suggesion:Custom prioritization:
```
first parameter list of Job IDssecond parameter could be MoveUp, MoveDown, MoveToTop, MoveToBottom.
Pre-defined prioritization:first parameter list of Job IDs
second parameter could be one from belowDataset creation time ascending/descending
Dataset size ascending/descendingDataset name A-Z / Z-A
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 17of 31
Job source A-Z / Z-AJob destination A-Z / Z-A
Status Implemented
Linked Work Items
has parent: vvHLP-1166 - Functional Requirements ,is derived from: vvHLP-1184 - Allow to change the transfer job order ,
is implemented by: vvHLP-1963 - API function to support prioritization of transfer jobs and Implementation to change the transfer job order ,is related to: vvHLP-1928 - Design for prioritization of transfer jobs
vvHLP-1379 - API function to set maximum parallel transfer jobs per systemCOPYstation2 shall provide API function to set/edit and view the maximum parallel jobs in the system.
Status Rejected
Linked Work Items has parent: vvHLP-1166 - Functional Requirements
vvHLP-1384 - API function to change Operation ModeCOPYstation2 shall provide an API function to change the operation mode from Automatic to API and vice versa.
Status Implemented
Linked Work Itemshas parent: vvHLP-1166 - Functional Requirements ,is derived from: vvHLP-1463 - Switching between API and Automatic mode ,is implemented by: vvHLP-1851 - API function to change Operation Mode
3.6.7.2 Non-functional requirements
3.6.7.3 API Documentation
vvHLP-1380 - API documentation for internal dev teamCOPYstation2 development tool chain shall create automatic development API documentation.
Tool to use for automatic documentation: Doxygen, every declared API functions needs to provided with detailed comment about in standard Doxygen format of c++.
Status Verified
Linked Work Items has parent: vvHLP-1381 - API Documentation ,is derived from: vvHLP-1201 - Documentation- API documentation
vvHLP-1502 - API documentation for customer/external use[OpState:API]
```
COPYstation2 shall provide APIs defined and described in a structured, machine readable description format very similar to OpenAPI ( https://swagger.io/resources/open-api/ ). It should provide a similar feature set, allow for automation and documentation generation.Suggestion:
```
```
If API is developed as REST API for customer, then better to use Swagger(Swagger Editor).If API is developed as JSONRPC API for customer, then better to use OpenRPC playground(OPEN-RPC Playground).
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1381 - API Documentation ,is derived from: vvHLP-1201 - Documentation- API documentation ,is implemented by: vvHLP-2178 - API documentation for customer/external use
3.6.8 Web interface
3.6.8.1 Functional Requirements
vvHLP-1382 - General UI description for the webUINote: A UI/UX designer is currently working on a UX design.
```
TBD: Waiting for the new design draft from new UX designer initially to be reviewed by product management team.
```
```
The main view in the webUI must show the current upload rates, the status of the cartridges, the status of the system (including status API/automatic mode) and the list of upload jobs.The user can switch to a different page, when they are interested in the log messages.
```
A third page is used for the settings of the COPYstation2.The current license and the active options are displayed in the webUI. The user can add/modify/delete licenses in this screen.
Status Verified
Linked Work Itemshas parent: vvHLP-1169 - Functional Requirements ,is derived from: vvHLP-1203 - General UI description for the webUI ,is implemented by: vvHLP-2117 - General UI description for the webUI
vvHLP-1307 - webUI option to configure default targetCOPYstation2 must provide an option in the webUI that allows users to add, edit, and remove default target for upload operations, user should be able to configure multiple default servers.
Supported target types:The system should support various target types including but not limited to:
```
SFTP: Secure File Transfer Protocol1.AWS: Amazon Web Services2.
```
```
Azure: Microsoft Azure Blob Storage3.SMB: Microsoft SMB4.
```
Status Implemented
Linked Work Items
has parent: vvHLP-1169 - Functional Requirements ,is derived from: vvHLP-1179 - Default target if primary target failed ,
is derived from: vvHLP-1180 - Default target for transfer jobs ,is implemented by: vvHLP-2023 - webUI option to configure default target
vvHLP-1311 - Network Status Display in WebUICOPYstation2 shall display the network state information for all connection available on the system on the webUI.
Details to be captured for for each connection:
Connection Type: ethernet1.Connection State: Indicate whether the connection is active, inactive, or in an error state.2.
```
Bandwidth: Show the bandwidth of connection.3.IP Address V4: Display the IP V4 address of connection.4.
```
IP Address V6: Display the IP V6 address of connection.5.Subnet Mask: Display the subnet mask of connection.6.
```
Gateway: Display the gateway address of connection.7.MAC Address: Display the MAC address of connection.8.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1169 - Functional Requirements ,is derived from: vvHLP-1108 - CopyStation2 must display the network state for the user ,is implemented by: vvHLP-2053 - Network Status Display in WebUI
vvHLP-1309 - COPYstation2 state display in webUICOPYstation2 shall display the application running state to the user via a green round LED in webUI.
Status Implemented
Linked Work Itemshas parent: vvHLP-1169 - Functional Requirements ,is derived from: vvHLP-1109 - CopyStation2 must display the application state for the user ,
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 18of 31
is implemented by: vvHLP-1993 - COPYstation2 state display in webUI
```
vvHLP-1497 - Update the transfer job group stateCOPYstation2 shall Update the group(cartridge, Local storage,) state based on the job state changes.
```
state as BUSY if at least 1 transfer job is runningstate as IDLE if No transfer job is running
Status Implemented
Linked Work Items
has parent: vvHLP-1169 - Functional Requirements ,is derived from: vvHLP-1110 - CopyStation2 must display the cartridge state for the user ,
is related to: vvHLP-1696 - Initial Header / Cpp design ,is related to: vvHLP-1698 - Logic Implementation ,
is related to: vvHLP-1699 - Unit tests
vvHLP-1308 - Cartridge Status Display in WebUICOPYstation2 shall display the cartridge status to the user in webUI which should include the below
cartridge state - please refer Cartridge statetransfer status
transfer progress %number of jobs running/scheduled
upload rate Bites/Secupload ETA
Status Rejected
Linked Work Items has parent: vvHLP-1169 - Functional Requirements ,is derived from: vvHLP-1110 - CopyStation2 must display the cartridge state for the user
vvHLP-1316 - Option to upload GPG private key in webUICOPYstation2 shall have option to upload the private GPG key in webUI.
Status Implemented
Linked Work Itemshas parent: vvHLP-1169 - Functional Requirements ,is derived from: vvHLP-1177 - Decrypt JSON File processing ,is implemented by: vvHLP-2054 - Option to upload GPG private key in webUI
vvHLP-1295 - WebUI option for cartridge datasets offloading to Local BufferCOPYstation2 must provide an option to user to configure the offloading cartridge data to the local storage via webUI
Status Implemented
Linked Work Itemshas parent: vvHLP-1169 - Functional Requirements ,is derived from: vvHLP-1178 - Offload the data from the cartridge ,is implemented by: vvHLP-1761 - UI option for Offload the data from the cartridge
vvHLP-1325 - Option for user to change the priority of transfer jobs in webUICOPYstation2 shall provide a user interface to prioritize the transfer jobs.
Transfer job ordering options to support:
Options for custom prioritizing the transfer job1.Dataset creation time ascending/descending2.
Dataset size ascending/descending3.Dataset name A-Z / Z-A4.
Job source A-Z / Z-A5.Job destination A-Z / Z-A6.
User must be able to change the order of the any job in the enqueued list by just drag and drop the job from one position to other in the list from the WebUI.webUI shall provide option to user to select one or more job and perform MoveUp, MoveDown, MoveToTop, MoveToBottom.
Ordering operation should do:
The order of job can be changed on any one of the above parameter.1.Order can only be changed when the jobs are enqueued/stopped state.2.
On change of the options selected by the user transfer job under the enqueued jobs will reorder the jobs that are in the running queue is not affected by the changes.3.If user intends to change the order of the running jobs the jobs must be stopped before reordering.4.
Custom priority can be achieved by a drag and drop similar feature in webUI.5.Custom priority can be achieved by selection of one or more job and perform MoveUp, MoveDown, MoveToTop, MoveToBottom.6.
Default order:Dataset creation time in ascending order
Status Implemented
Linked Work Itemshas parent: vvHLP-1169 - Functional Requirements ,is derived from: vvHLP-1184 - Allow to change the transfer job order ,is implemented by: vvHLP-2157 - Option for user to change the priority of transfer jobs in webUI
vvHLP-1377 - User option to set/edit the maximum parallel Transfer jobCOPYstation2 shall provide option to set/edit the maximum parallel transfer jobs in total on the system via webUI.
Status Rejected
Linked Work Items has parent: vvHLP-1169 - Functional Requirements
```
vvHLP-1488 - User option to set/edit the maximum parallel Transfer job per transfer targetCOPYstation2 shall provide option to set/edit the maximum parallel transfer jobs of each transfer target(destination) via webUI.
```
Status Rejected
Linked Work Items has parent: vvHLP-1169 - Functional Requirements
vvHLP-1383 - Operation mode change optionCOPYstation2 shall provide an option in webUI to change the operation mode from Automatic to API and vice versa.
Status Implemented
Linked Work Itemshas parent: vvHLP-1169 - Functional Requirements ,is derived from: vvHLP-1463 - Switching between API and Automatic mode ,is implemented by: vvHLP-2063 - Operation mode change option
vvHLP-1387 - Display the list of running transfer jobs on webUICOPYstation2 shall display the list of running transfer jobs for the whole station via webUI.
Status Implemented
Linked Work Itemshas parent: vvHLP-1169 - Functional Requirements ,is derived from: vvHLP-1200 - Display current upload jobs ,is implemented by: vvHLP-1854 - Display list of running transfer jobs
```
vvHLP-1386 - Display of current upload rate via webUICOPYstation2 shall display the current upload rate for both cartridges and the internal buffer (if used) via webUI additionally some (short term) historical data, e.g. the last 60 seconds.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1169 - Functional Requirements ,
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 19of 31
Linked Work Items is derived from: vvHLP-1208 - Current upload rate of the storage ,is implemented by: vvHLP-1865 - Display of current upload rate via webUI
3.6.8.2 Non-functional requirements
3.6.9 Testing
3.6.9.1 Data source for testing
```
vvHLP-1539 - Support script: creating a dummy datasetThe COPYstation2 SW test setup must contain a mk-dataset.sh script to create one dataset, including dummy data files (mf4, pcap) containing pseudo-random data and a valid JSON dataset definition file listing all data files and any passed transfer targets. Each call to the
```
script with the same parameters must generate the same result
The following parameters should be accepted:
Seed for pseudo-random generation.Target folder
Dataset nameNumber of data files
Minimum size per datafileMaximum size per datafile
```
Target definition (path to a file containing the targets definition as json)
```
Rationale for the stable pseudo-random generation: In order to have repeatable tests, the source data should always be the same for any given test.
Status Implemented
Linked Work Items has parent: vvHLP-1540 - Data source for testing ,is derived from: vvHLP-1202 - Testing - API test automation
vvHLP-1555 - Support script: Script for creating multiple datasetsThe COPYstation2 SW test setup must contain a mk-datasets.sh script to create multiple datasets by calling mk-dataset.sh multiple times with pseudo-random parameters. Each call to the script with the same parameters must generate the same result.
The following parameters should be accepted:
Seed for pseudo-random generation.Target folder
```
Datasets in subfolders? (boolean: 0 or 1)Number of datasets
```
Minimum number of datafiles per datasetMaximum number of datafiles per dataset
Minimum size per datafileMaximum size per datafile
```
Target definition (path to a file containing the targets definition as json)
```
Status Implemented
Linked Work Items
has parent: vvHLP-1540 - Data source for testing ,is derived from: vvHLP-1202 - Testing - API test automation ,
is implemented by: vvHLP-1686 - Script for creating multiple datasets ,is implemented by: vvHLP-1807 - File should remain on the target server
```
vvHLP-1554 - Test case script: CS2 uploads from cartridge to an SFTP server (positive case, all datasets are valid)The COPYstation2 SW test setup must contain a test-sftp-upload.sh script to:
```
create a target definition json file from the passed target sftp server1.create multiple datasets by calling mk-datasets.sh2.
calculate and store the checksums of all datafiles3.run the COPYstation2 SW4.
```
wait for transfers to finish (check whether the original folder is empty or timeout)5.check the checksums on the target server against the original checksums (if the target server is localhost, run the checksums locally, otherwise use ssh to run the checksums)6.
```
stop the COPYstation2 SW7.remove all files in the target sftp server folder8.
remove any remaining datasets inside the source folder on the CS29.
The following parameters should be accepted:
```
Seed for pseudo-random generation.Source folder on the CS2 (where the datasets will be created)
```
```
Minumum transfer speed in bits per seconds (to calculate the timeout value)target sftp server
```
target sftp server usertarget sftp server password
target sftp server folder
Status Implemented
Linked Work Items
has parent: vvHLP-1540 - Data source for testing ,is derived from: vvHLP-1202 - Testing - API test automation ,
is implemented by: vvHLP-1706 - sftp test script cs2 ,is implemented by: vvHLP-1726 - sftp test script improvements and review all scripts ,
is implemented by: vvHLP-1807 - File should remain on the target server
3.6.9.2 Data sinks for testing
vvHLP-1474 - SFTP server setup for testingSetup the SFTP server on the local network to testing the data transfer functionality to SFTP server from COPYstation2.
Status Verified
Linked Work Items has parent: vvHLP-1470 - Data sinks for testing ,is derived from: vvHLP-1447 - Testing - Data sinks
vvHLP-1471 - SMB server for testingSetup the SMB server on the local network to testing the data transfer functionality to SMB server from COPYstation2.
Status Approved
Linked Work Items has parent: vvHLP-1470 - Data sinks for testing ,is derived from: vvHLP-1447 - Testing - Data sinks
vvHLP-1472 - Azure blob storage server for testingSetup the Azure blob storage server on the local network to testing the data transfer functionality to Azure blob storage server from COPYstation2.
Status Verified
Linked Work Items has parent: vvHLP-1470 - Data sinks for testing ,is derived from: vvHLP-1447 - Testing - Data sinks
vvHLP-1473 - AWS S3 server for testingSetup the AWS S3 server on the local network to testing the data transfer functionality to AWS S3 server from COPYstation2.
Status Verified
Linked Work Items has parent: vvHLP-1470 - Data sinks for testing ,is derived from: vvHLP-1447 - Testing - Data sinks
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 20of 31
3.7 Production Tools
vvHLP-1513 - Loading of configuration from JSON file on start-upCOPYstation2 must load the configuration from JSON in Local configuration storage path on start-up.
```
Note: Possible storage path for the current config /home/cs2/config
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1243 - COPYstation2 settings page in the WebUI ,is implemented by: vvHLP-1703 - code changes for loading default json during software component initialization
vvHLP-1514 - Configuration schema validationCOPYstation2 shall do configuration schema validation.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1243 - COPYstation2 settings page in the WebUI ,is related to: vvHLP-1515 - Defining configuration schema
vvHLP-1516 - Saving default target server configuration in JSON on modificationCOPYstation2 shall store the default target connection parameters in JSON file in Local configuration storage path.
Status Rejected
Linked Work Items has parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1243 - COPYstation2 settings page in the WebUI
vvHLP-1543 - Add job to transfer jobsCOPYstation2 shall add/remove the transfer job to respective group.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,specifies: vvHLP-1239 - Transfer module reuse ,is related to: vvHLP-1536 - Add a job to an existing transfer job group
vvHLP-1511 - COPYstation2 default valuesCOPYstation2 shall use default values for any unset user configuration option.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1243 - COPYstation2 settings page in the WebUI ,is implemented by: vvHLP-1771 - COPYstation2 default values and Store configuration changes in local as JSON file
vvHLP-1512 - Store configuration changes in local as JSON fileCOPYstation2 shall store the configuration as a JSON file in Local configuration storage path, on any option change.
```
Note: Possible storage path for the current config /home/cs2/config
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1243 - COPYstation2 settings page in the WebUI ,is implemented by: vvHLP-1771 - COPYstation2 default values and Store configuration changes in local as JSON file
vvHLP-1517 - Default operation modeCOPYstation2 shall have default operation mode as Auto and initially on first time setup it should start with auto mode.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1463 - Switching between API and Automatic mode ,is related to: vvHLP-1519 - Initialize CS2 with Auto controller mode as default
vvHLP-1566 - Configure local SFTP server on CS2COPYstation2 must configure the Local SFTP server to allow uploads to the SFTP offloading area.
```
Note: Configuration need to be done in /etc/ssh/sshd_config file.
```
Status Verified
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1073 - SFTP server ,is implemented by: vvHLP-2179 - Configure local SFTP server on CS2
vvHLP-1567 - Use common local sftp root pathCOPYstation2 shall use a common Local SFTP root path.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1073 - SFTP server ,is implemented by: vvHLP-2094 - Implementation to support a common upload root directory for SFTP user
```
vvHLP-1568 - Mapping of local sftp root path to UUID or Label in /etc/fstab(Production)COPYstation2 shall do one time mapping of Local SFTP storage UUID or Label to its path in /etc/fstab file of the system.
```
Status Approved
Linked Work Items has parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1073 - SFTP server
vvHLP-1569 - add/delete local sftp server user on request from webUICOPYstation2 shall add a new user or delete an existing user based on the request from the webUI.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1074 - SFTP server - Authentication ,is implemented by: vvHLP-1901 - Add/delete local sftp server user on request from webUI
vvHLP-1570 - API function to change local sftp user passwordCOPYstation2 shall provide an API function to change the password of the existing local SFTP user.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1074 - SFTP server - Authentication ,is implemented by: vvHLP-1902 - API function to change local sftp user password
vvHLP-1571 - Authenticate using user/password before granting access via SFTPCOPYstation2 shall authenticate the access grant using username and password.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1074 - SFTP server - Authentication ,is implemented by: vvHLP-1903 - Authenticate using user/password before granting access via SFTP
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 21of 31
vvHLP-1572 - WebUI option for SFTP user to define a upload directory.COPYstation2 must provide webUI option for each SFTP users to define its own custom upload path which will have priority over user home path.
```
Note: The custom path name should be unique in chroot path.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1282 - SFTP server - Directories in SFTP root ,is implemented by: vvHLP-2062 - WebUI option for SFTP user to define a upload directory.
vvHLP-1573 - Create transfer job for newly uploaded complete dataset within 6 minutesCOPYstation2 must create a transfer job for the complete datasets uploaded on the local sftp server path within 6 minutes.
```
Ref: http://intranet.caetec/mediawiki/index.php/Entwicklung/Team_Logger/Projekte/dataLog/Technische_Dokumentation/AblaufAllgemein
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1103 - SFTP server - automatic transfer ,is implemented by: vvHLP-1767 - Monitor and Create transfer job for newly uploaded complete dataset within 6 minutes for SFTP server
vvHLP-1574 - Check for the "SFTP" license option before starting local SFTP server.COPYstation2 must validate the availability of the SFTP license before starting the Local SFTP server.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1352 - License check - SFTP license option ,is implemented by: vvHLP-1855 - Check for the "SFTP" license option before starting local SFTP server.
vvHLP-1575 - Validate the minimum password for user credential input on config importCOPYstation2 shall check if the password fulfills the minimal password requirements on config import
Minimal password requirement: At least 8 characters long. Contains at least one lowercase letter and one uppercase letter and one number.
Status Rejected
Linked Work Items has parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1084 - Password requirements
vvHLP-1576 - Validate the minimum password for user credential input from APICOPYstation2 shall check if the password fulfills the minimal password requirements when a password change request is received via API
Minimal password requirement: At least 8 characters long. Contains at least one lowercase letter and one uppercase letter and one number.
Status Implemented
Linked Work Items
has parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1084 - Password requirements ,
is implemented by: vvHLP-1904 - Validate the minimum password for user credential input from API ,is implemented by: vvHLP-1933 - Validate the minimum password for user credential input on web ui.
vvHLP-1577 - Validate the minimum password for user credential input on web ui.COPYstation2 shall check if the password fulfills the minimal password requirements when a password change request is received via webUI.
Minimal password requirement: At least 8 characters long. Contains at least one lowercase letter and one uppercase letter and one number.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1084 - Password requirements ,is implemented by: vvHLP-1933 - Validate the minimum password for user credential input on web ui.
vvHLP-1578 - Read the plugin cycles from EEPROM of the cartridge and slot connectorsCOPYstation2 should read the number of plugin cycles from the EEPROM of the cartridge and slot connectors
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1104 - Track the Plugin Cycles of the cartridge and slot connectors ,is implemented by: vvHLP-1988 - Read the cartridge plugin cycles from power controller and Maintain plugin cycles at runtime infomanager
vvHLP-1579 - Maintain plugin cycles at runtime infomanagerCOPYstation2 should maintain the plugin cycles in runtime info manager.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1104 - Track the Plugin Cycles of the cartridge and slot connectors ,is implemented by: vvHLP-1988 - Read the cartridge plugin cycles from power controller and Maintain plugin cycles at runtime infomanager
vvHLP-1580 - Display the information on the usage of the cartridge and slot connectors to the user on the webUICOPYstation2 should read the number of plugin cycles for each cartridge and slot connectors on the system.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1104 - Track the Plugin Cycles of the cartridge and slot connectors ,is implemented by: vvHLP-2116 - Display the information on the usage of the cartridge and slot connectors to the user on the webUI
```
vvHLP-1581 - The health status of internal storage should be maintained in runtime infomanager.COPYstation2 shall read SMART data of internal storage in a periodic manner (every 500ms).
```
Refinments disccussed and approved- Although the original interval was set to 500 ms, it has been adjusted to a more suitable 5-minute interval due to the nature of SMART data.
- The retrieved health status is stored in a dedicated structure, which is returned when requested via the API.- Logging occurs only when the health status indicates a problem, preventing log flooding during normal operation.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1105 - Track the health status of the internal storage. ,is implemented by: vvHLP-1780 - The health status of internal storage should be read in a periodic manner and log the health status check on failure
vvHLP-1582 - Display the healh status of internal storage on webUI.COPYstation2 shall display the health status of the internal storage on the webUI
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1105 - Track the health status of the internal storage. ,is implemented by: vvHLP-2119 - Display the health status of internal storage and Cartridge on webUI.
vvHLP-1583 - Information to be displayed under health status of internal storage.COPYstation2 shall display the below information as part of health information.
Model numberSerial number
Firmware versionOperating hours
Number of connectionsFaulty sectors
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 22of 31
SMART overall health assessment test result
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1105 - Track the health status of the internal storage. ,is implemented by: vvHLP-1780 - The health status of internal storage should be read in a periodic manner and log the health status check on failure
vvHLP-1584 - On health status check failure of of internal storageCOPYstation2 shall log the health status check failure and should proceed with enumeration.
```
Note: should not block further processing and log the warning message.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1105 - Track the health status of the internal storage. ,is implemented by: vvHLP-1780 - The health status of internal storage should be read in a periodic manner and log the health status check on failure
vvHLP-1585 - Poll for the network info every 500ms and maintain in runtime infomanager.COPYstation2 should poll the network information for the available connection every 500ms and maintain the latest information in the runtime info manager.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1108 - CopyStation2 must display the network state for the user ,is implemented by: vvHLP-1989 - Poll for the network info every 500ms and maintain in runtime infomanager.
vvHLP-1586 - Display the systemtime via webUI.COPYstation2 shall display the system time on the webUI.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1111 - CopyStation2 must display the system time for the user ,is implemented by: vvHLP-1935 - vvHLP-1586 - Display the systemtime via webUI
vvHLP-1587 - Provide the systemtime via API.COPYstation2 shall provide an API function for user to get the system time.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1111 - CopyStation2 must display the system time for the user ,is implemented by: vvHLP-2102 - Provide API function for user to get and set the system time.
```
vvHLP-1588 - Provide option to set system time in webUI. (UI)COPYstation2 shall provide webUI option to user for setting system time.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1175 - Set system time manually ,is implemented by: vvHLP-2118 - Provide option to set system time in webUI.
```
vvHLP-1589 - Provide option to set system time through API. (API)COPYstation2 shall provide API function for setting system time.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1175 - Set system time manually ,is implemented by: vvHLP-2102 - Provide API function for user to get and set the system time.
vvHLP-1590 - Update the webUI/API requested time internally in the systemCOPYstation2 shall update the system time from the time set via webUI/ API.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1175 - Set system time manually ,is implemented by: vvHLP-2103 - Update the webUI/API requested time internally in the system.
vvHLP-1591 - Provide option to set NTP server in webUI by admin user only.COPYstation2 should have an option available to set NTP server information.
Status Rejected
Linked Work Items has parent: vvHLP-1160 - Production Tools
vvHLP-1592 - On NTP server update Sync the system internal time with NTP time.COPYstation2 shall synchronize the time with configured NTP server, if the NTP server is update on the configuration.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1176 - Set time from NTP server ,is implemented by: vvHLP-1781 - On NTP server update Sync the system internal time with NTP time.
vvHLP-1593 - Import the GPG key information uploaded from webUI/API.COPYstation2 should import the uploaded private gpg key by the user on the key ring.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1177 - Decrypt JSON File processing ,is implemented by: vvHLP-1859 - Option to upload GPG private key in API and Import the GPG key information uploaded from webUI/API.
vvHLP-1594 - Display the available GPG keys in CS2 system on webUI.COPYstation2 should provide the list of available gpg keys on the system with minimum ID, fingerprint and expiry date details on the webUI.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1177 - Decrypt JSON File processing ,is implemented by: vvHLP-2050 - Display the available GPG keys in CS2 system on webUI.
vvHLP-1595 - API function to list the available GPG keys in CS2 system.COPYstation2 should provide the list of available gpg keys on the system with minimum ID, fingerprint and expiry date details via API function.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1177 - Decrypt JSON File processing ,is implemented by: vvHLP-1905 - API function to list the available GPG keys in CS2 system.
vvHLP-1596 - Option to Abort/Stop/Restart all transfer jobs of specific slot through webUICOPYstation2 must provide option to stop, restart and abort all transfer jobs on a specific cartridge.
```
Button to Restart( ) all the jobs on the cartridge should be available on the WebUI and visible only when at least one job is in running, enqueued or stopped state. Prompt should be shown with a warning message to the user that "All the running jobs will be stopped andrestarted ". user consent is necessary for further processing.
```
```
Button to Stop( ) all the jobs on the cartridge should be available on the WebUI and visible only when one or more job is in running or enqueued state. Prompt should be shown with a warning message to the user that "All the running jobs will be stopped ". user consentis necessary for further processing.
```
```
Button to Abort(×) all the jobs on the cartridge should be available on the WebUI and visible only when the at least one job is in either of created, enqueued, running, pause and stopped states. Prompt should be shown with a warning message to the user that "Allthe running jobs will be aborted ". user consent is necessary for further processing.
```
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 23of 31
```
Note: Stop and restart button should be toggle buttons
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1182 - Actions on the cartridge slot ,is implemented by: vvHLP-1995 - Option to Abort/Stop/Restart all transfer jobs of specific slot through webUI
vvHLP-1597 - Actions to perform on a selected transfer job through webUICOPYstation2 must provide option to stop, restart, pause, resume and abort a specific transfer job.
```
Buttons in the Running job queueButton to Stop( ) the job should be available on the WebUI and visible only when the job is in running or enqueued state. Prompt should be shown with a warning message to the user that "Transfer job will be stopped ". user consent is necessary for further processing.
```
```
Button to Abort(×) the job should be available on the WebUI and visible only when the job is in either of created, enqueued, running, pause and stopped state. Prompt should be shown with a warning message to the user that "Transfer job will be aborted ". userconsent is necessary for further processing.
```
```
Button to Pause( ) the job should be available on the WebUI and visible only when the job is in running state.Button to Resume( ) the job should be available on the WebUI and visible only when the job is in paused state.
```
```
Buttons available for each job in the Enqueued job queueButton to Restart( ) the job should be available on the WebUI and visible only when the job is in stopped state.
```
```
Button to Abort(×) the job should be available on the WebUI and visible only when the job is in either of created, enqueued, running, pause and stopped state. Prompt should be shown with a warning message to the user that "Transfer job will be aborted ". userconsent is necessary for further processing.
```
```
Note:Pause and resume button should be toggle buttons
```
Please refer transfer job states 3.6.5.1.3 - Job management
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1183 - Actions on the transfer job ,is implemented by: vvHLP-2052 - Actions to perform on a selected transfer job through webUI
```
vvHLP-1598 - Creation of system manual for user. (Documentation team)The Documentation Team shall create a comprehensive System User Manual covering system overview, installation, configuration, user roles, and step-by-step operational guidance. The manual should include troubleshooting tips, FAQs, and visual aids
```
```
(screenshots/diagrams) for clarity. It must follow project documentation standards, be reviewed by SMEs, and delivered in both PDF and printable formats. Final approval will be required before sharing with the customer.
```
Status Approved
Linked Work Items has parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1204 - Documentation - Manual
vvHLP-1599 - Support for Amazon S3:COPYstation2 shall support the Amazon S3 server.
Transfer job must be able to connect to the with configured Amazon S3 server. vvHLP-1366Transfer job must be able to authenticate the user credential with configured Amazon S3 server.
Transfer job must be able to initiate a session for the data transfer with configured Amazon S3 server.System must be able handle the Amazon S3 protocol related errors.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1216 - Support for Amazon S3 Cloud Storage as transfer target ,is implemented by: vvHLP-1773 - Support for Amazon S3 Cloud Storage as transfer target
vvHLP-1600 - Support for Microsoft Azure Blob Storage:COPYstation2 shall support the Azure blob storage server.
Transfer job must be able to connect to the with configured Azure blob storage server. vvHLP-1366Transfer job must be able to authenticate the user credential with configured Azure blob storage server.
Transfer job must be able to initiate a session for the data transfer with configured Azure blob storage server.System must be able handle the Azure blob storage protocol related errors.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1217 - Support for Microsoft Azure Blob Storage as transfer target ,is implemented by: vvHLP-1774 - Support for Microsoft Azure Blob Storage as transfer target
vvHLP-1601 - Support for Microsoft SMB:COPYstation2 shall support the Microsoft SMB server.
Transfer job must be able to connect to the with configured Microsoft SMB server. vvHLP-1366Transfer job must be able to authenticate the user credential with configured Microsoft SMB server.
Transfer job must be able to initiate a session for the data transfer with configured Microsoft SMB server.System must be able handle the Microsoft SMB protocol related errors.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1218 - Support for Microsoft SMB as transfer target ,is implemented by: vvHLP-2129 - Support for Microsoft SMB
vvHLP-1602 - Function implementation to identifiy the untracked files.COPYstation2 shall track the files on the cartridge that does not belong to any dataset.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1240 - Upload untracked files to default server ,is implemented by: vvHLP-1775 - Implementation to identifiy and delete files from internal buffer which is not modified more than 1 day.
vvHLP-1603 - API function to request for upload the untracked files.COPYstation2 must provide an option to start a transfer job containing all files that are not part of any datasets to the default server via API.
Status In Progress
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1240 - Upload untracked files to default server ,is implemented by: vvHLP-1863 - API function to request for upload the untracked files.
vvHLP-1604 - webUI option to request for upload the untracked files.COPYstation2 must provide an option to start a transfer job containing all files that are not part of any datasets to the default server via the WebUI.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1240 - Upload untracked files to default server ,is implemented by: vvHLP-2011 - WebUI option to request for upload the untracked files
vvHLP-1605 - Create transfer job for the untracked files.COPYstation2 shall create transfer job containing all files that are not part of any datasets to the default server on request from webUI/API.
Status In Progress
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1240 - Upload untracked files to default server ,is implemented by: vvHLP-1958 - Create transfer job for the untracked files.
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 24of 31
vvHLP-1606 - Function implementation to format the cartridge.COPYstation2 shall format the cartridge upon the request from WebUI and API.
```
Note: Format functionality of the datalog could be reused to implement this functionality, currently datalog provide the option to format in ext4 and ext4 transfer target
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1241 - Formatting the cartridge ,is implemented by: vvHLP-1959 - Function implementation to format the cartridge and API function to request for format the cartridge.
vvHLP-1607 - API function to request for format the cartridge.COPYstation2 shall provide an API function format a specific cartridge.
```
Note: Possible parameter to the API function could be the slot number1
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1241 - Formatting the cartridge ,is implemented by: vvHLP-1959 - Function implementation to format the cartridge and API function to request for format the cartridge.
vvHLP-1608 - webUI option to request for format the cartridge.COPYstation2 shall provide an option to user on the webUI to format a specific cartridge.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1241 - Formatting the cartridge ,is implemented by: vvHLP-2181 - webUI option to request for format the cartridge.
```
vvHLP-1609 - Option to add, delete or modify users with its type(webUI, API & SFTP).COPYstation2 must provide an option to the user to add, delete or modify users of the following types for the COPYstation2 via the web interface:
```
admin WebUI users that can configure the COPYstation2 via the web interfaceSFTP users that can transfer data to and from the COPYstation2 via SFTP
API users that can use the API
This includes setting the users' passwords
```
Note: User information can be stored in the path - /var/copystation2/userfiles
```
Status Implemented
```
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1249 - Manage users as admin ,is implemented by: vvHLP-2045 - Option to add, delete or modify users with its type(webUI, API & SFTP).
```
vvHLP-1610 - WebUI option to export the current configuration of COPYstation2.COPYstation2 shall provide the webUI option to user for exporting the current user configuration in the JSON format.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1250 - Export configuration file from copystation ,is implemented by: vvHLP-2162 - WebUI option to export the current configuration of COPYstation2.
vvHLP-1611 - Export the current configuration information.COPYstation2 shall export the current user configuration in the JSON format.
Status Implemented
Linked Work Items
has parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1250 - Export configuration file from copystation ,
is implemented by: vvHLP-1906 - Export the current configuration information. ,is implemented by: vvHLP-1969 - Export/Import implementation analysis and design
vvHLP-1612 - Automatic troubleshoot for memory leaks.COPYstation2 shall track the memory leaks if any.
Status Draft
Linked Work Items has parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1251 - Automatic troubleshooting and resolving
vvHLP-1613 - Reuse datalog memory usage warningsCOPYstation2 shall reuse the memory usage warnings from the datalog.
```
Suggestion: Additionally, reboot could be performed when the threshold is crossed
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1251 - Automatic troubleshooting and resolving ,is implemented by: vvHLP-1772 - Reuse datalog memory usage warnings.
vvHLP-1614 - Reuse datalog supervisor and watchdogCOPYstation2 shall reuse the supervisor and watchdog implementation from the datalog.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1251 - Automatic troubleshooting and resolving ,is implemented by: vvHLP-2257 - Reuse datalog supervisor and watchdog
vvHLP-1615 - Validate the API License availability on request to switch from Auto to API modeCOPYstation2 must validate if the API license is available before switch from Auto mode to API mode. Notify the user with appropriate message upon unavailability of the license.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1258 - License check - API license option ,is implemented by: vvHLP-1768 - Validate the API License availability on request to switch from Auto to API mode
vvHLP-1616 - Validate the Basic license availability during system startup.COPYstation2 must validate if the basic license is available on the system startup.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1259 - License check - basic license ,is implemented by: vvHLP-1769 - Validate the Basic license availability during system startup, and Set the operation mode and state
vvHLP-1617 - Set the operation mode and state based on validation of basic licenseCOPYstation2 must check if a valid license for the currently installed version is available only on successful validation the states must be set to <opmode>_working <opmode>_Idle.
On basic license validation failure operation state must not switch into the "Auto_Working" or "API_Working" state, but should stay in the "Auto_Idle" or "API_Idle" state during normal operation.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1259 - License check - basic license ,is implemented by: vvHLP-1769 - Validate the Basic license availability during system startup, and Set the operation mode and state
```
vvHLP-1618 - Implementation to identifiy files from internal buffer which is not modified > 1 day.COPYstation2 must identify files that don't belong to any recognized dataset and have not been modified for 1 day from its internal buffer in a periodic manner (30 mins).
```
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 25of 31
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1336 - Delete untracked files from the internal buffer ,is implemented by: vvHLP-1775 - Implementation to identifiy and delete files from internal buffer which is not modified more than 1 day.
vvHLP-1619 - Implementation to delete the identified untracked files.COPYstation2 must delete all files that don't belong to any recognized dataset and have not been modified for 1 day from its internal buffer.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1336 - Delete untracked files from the internal buffer ,is implemented by: vvHLP-1775 - Implementation to identifiy and delete files from internal buffer which is not modified more than 1 day.
vvHLP-1620 - webUI option to configure internal buffer cleanup.COPYstation2 shall provide an option to the user on webUI for configuring the internal buffer clean up by deleting the untracked files.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1336 - Delete untracked files from the internal buffer ,is implemented by: vvHLP-2163 - webUI option to configure internal buffer cleanup.
vvHLP-1621 - Authentiate the user credentials before providing the access to API user.COPYstation2 must require authentication using username and password before granting access via API.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1341 - API Authentication ,is implemented by: vvHLP-2164 - Authentiate the user credentials before providing the access to API user.
vvHLP-1622 - Authenticate the user credentials before providing the access to SSH user.COPYstation2 must require authentication using SSH key before granting access via SSH.
```
Note: SSH access keys are configured during production to provide access for IPETRONIK support engineers.
```
Status Approved
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1342 - SSH Authentication ,is implemented by: vvHLP-1964 - Authentiate the user credentials before providing the access to SSH user.
vvHLP-1623 - Authentiate the user credentials before providing the access to webUI user.COPYstation2 must require authentication using username and password before granting access to the WebUI.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1343 - Web UI Authentication ,is implemented by: vvHLP-1934 - Authentiate the user credentials before providing the access to webUI user.
```
vvHLP-1624 - Create transfer job for newly offloaded complete datasetCreate transfer job for newly offloaded complete dataset(re use similar logic as local sftp monitor)
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1345 - Transfer the offloaded datasets to target server ,is implemented by: vvHLP-1770 - Create transfer job for newly offloaded complete dataset
vvHLP-1625 - Function to fetch the serial number of system.COPYstation2 must fetch the serial number of the hardware on the system start up and maintain in runtimeInfoManager.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1346 - Fetch the serial number to the user ,is implemented by: vvHLP-1960 - Function to fetch the serial number of system and API function to request for the serial number.
vvHLP-1626 - Display of serial number on webUI.COPYstation2 must display the system serial number on the webUI.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1346 - Fetch the serial number to the user ,is implemented by: vvHLP-2044 - Display of serial number on webUI.
vvHLP-1627 - API function to request for the serial number.COPYstation2 must provide API function to user to fetch the system serial number.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1346 - Fetch the serial number to the user ,is implemented by: vvHLP-1960 - Function to fetch the serial number of system and API function to request for the serial number.
vvHLP-1628 - Consolidate the health status of four SSD available in IPE891 cartridgeCOPYstation2 shall consolidate the health status of all four SSD's of the cartridge to provide the health status of the whole cartridge.
Status Rejected
Linked Work Items has parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1351 - Track the health status of the Cartridge.
vvHLP-1629 - Display the healh status of Cartridge on webUI.COPYstation2 shall display the health status of the whole cartridge on the webUI
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1351 - Track the health status of the Cartridge. ,is implemented by: vvHLP-2119 - Display the health status of internal storage and Cartridge on webUI.
vvHLP-1630 - Information to be displayed under health status of Cartridge.COPYstation2 shall display the health status and detailed below information for each cartridge
Model number,serial number,
```
Plugin cycles,SMART overall health assessment test result(Consolidate for all 4 drives))
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1351 - Track the health status of the Cartridge. ,is implemented by: vvHLP-1779 - Information to be displayed under health status of Cartridge.
vvHLP-1631 - Warning on health check failureCOPYstation2 shall log the health status check failure and should proceed with enumeration.
```
Note: should not block further processing and log the warning message.
```
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 26of 31
Status Approved
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1351 - Track the health status of the Cartridge. ,is implemented by: vvHLP-1778 - Track the health status of the Cartridge and Log warnings
vvHLP-1632 - webUI option to set NTP server.COPYstation2 should have an option available on webUI to set NTP server information.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1445 - Set NTP server details ,is implemented by: vvHLP-2049 - webUI option to set NTP server.
vvHLP-1633 - API function to set NTP server.COPYstation2 should an API function to set NTP server information.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1445 - Set NTP server details ,is implemented by: vvHLP-2104 - API function to set NTP server.
```
vvHLP-1634 - Puts system to sleep mode if <OP mode>_idle state > 30 minutesCOPYstation2 shall monitor the operation mode states(Auto_idle, Auto_working, API_idle, API_working), if the state remains idle for more than 30 mins system should be put on sleep (power saving) mode.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1449 - Sleep mode due to inactivity ,is implemented by: vvHLP-2066 - Implement Power Saving Mode Based on Operation Mode Idle Time in COPYstation2
vvHLP-1635 - Puts system to sleep mode if last wakeup from sleep time > 30 minutes and <OP mode>_idle.COPYstation2 shall update the operation mode state to <opmode>_working on system wake up.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1449 - Sleep mode due to inactivity ,is implemented by: vvHLP-2066 - Implement Power Saving Mode Based on Operation Mode Idle Time in COPYstation2
vvHLP-1636 - Implementation the wake up on for cartridgeCOPYstation2 shall update the operation mode state to <opmode>_working on detection or removal of the cartridge.
Status In Progress
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1450 - Sleep mode - Wake up on cartridge activity ,is implemented by: vvHLP-1907 - Implementation Wake up via Wake-on-LAN
vvHLP-1637 - Implementation Wake up via Wake-on-LANCOPYstation2 shall update the operation mode state to <opmode>_working on any data exchange over the LAN.
Status In Progress
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1451 - Sleep mode - Wake up via Wake-on-LAN ,is implemented by: vvHLP-1907 - Implementation Wake up via Wake-on-LAN
vvHLP-1638 - Implementation Wake up on press of power buttonCOPYstation2 shall update the operation mode state to <opmode>_working on power button press.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1452 - Sleep mode - Wake up on press of power button ,is implemented by: vvHLP-1907 - Implementation Wake up via Wake-on-LAN
vvHLP-1639 - Track the activity of the systemCOPYstation2 must determine the time since the last of the following items occurs as inactivity time:
active data uploadincoming SFTP connections
```
Physical cartridge operation (insertion/extraction)WebUI accesses
```
API request
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1453 - Activity detection ,is implemented by: vvHLP-2068 - Track the activity of the system
vvHLP-1640 - If no activity is detected, set the OP state to <OP mode>_idle.COPYstation2 shall set the operation state idle, if No activity was detected for more than 1mins.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1453 - Activity detection ,is implemented by: vvHLP-2069 - Set OP State Based on Activity Detection
vvHLP-1641 - If activity is detected, set the op state to <OP mode>_working.COPYstation2 shall set the operation state working, when the tracked activity is detected.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1453 - Activity detection ,is implemented by: vvHLP-2069 - Set OP State Based on Activity Detection
vvHLP-1642 - Encrypt all user passwords with the key is hard-coded in the COPYstation2 binary.COPYstation2 shall store all users' passwords encrypted with a current symmetric encryption algorithm for which the key is hard-coded in the COPYstation2 binary.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1462 - Password encryption ,is implemented by: vvHLP-1908 - Hash all user passwords
vvHLP-1643 - Display the current operation mode on the webUICOPYstation2 shall display the current operation mode to user on the webUI
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1244 - Operation mode information to user ,is implemented by: vvHLP-1993 - COPYstation2 state display in webUI
vvHLP-1644 - webUI option to configure the maximum parallel transfer for systemCOPYstation2 shall provide option to set/edit the maximum parallel transfer jobs in total on the system via webUI.
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 27of 31
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1468 - Set maximum parallel transfers ,is implemented by: vvHLP-2048 - webUI option to configure the maximum parallel transfer for system and for each targets
```
vvHLP-1645 - webUI option to configure the maximum parallel transfer for each targetsCOPYstation2 shall provide option to set/edit the maximum parallel transfer jobs of each transfer target(destination) via webUI.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1468 - Set maximum parallel transfers ,is implemented by: vvHLP-2048 - webUI option to configure the maximum parallel transfer for system and for each targets
vvHLP-1646 - API option to configure the maximum parallel transfer for systemCOPYstation2 shall provide API function to set/edit and view the maximum parallel jobs in the system.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1468 - Set maximum parallel transfers ,is implemented by: vvHLP-1856 - API option to configure the maximum parallel transfer for system and maximum parallel transfer for each targets
vvHLP-1647 - API option to configure the maximum parallel transfer for each targetsCOPYstation2 shall provide API function to set/edit and view the maximum parallel jobs in the system.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1468 - Set maximum parallel transfers ,is implemented by: vvHLP-1856 - API option to configure the maximum parallel transfer for system and maximum parallel transfer for each targets
vvHLP-1648 - Provide network state information via APICOPYstation2 shall provide the network state information for all connection available on the system via API function.
Details to be captured for for each connection:
Connection Type: ethernet1.Connection State: Indicate whether the connection is active, inactive, or in an error state.2.
```
Bandwidth: Show the bandwidth of connection.3.IP Address V4: Display the IP V4 address of connection.4.
```
IP Address V6: Display the IP V6 address of connection.5.Subnet Mask: Display the subnet mask of connection.6.
```
Gateway: Display the gateway address of connection.7.MAC Address: Display the MAC address of connection.8.
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1108 - CopyStation2 must display the network state for the user ,is implemented by: vvHLP-2065 - Provide network state information via API
vvHLP-1649 - Get the systemtime and maintain in the runtine infomanager
Status Rejected
Linked Work Items has parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1111 - CopyStation2 must display the system time for the user
vvHLP-1650 - Network status via integrated displayCOPYstation2 must display the status of the network status on the LCD/LED display on the system.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1247 - Display network parameters on the integrated display ,is implemented by: vvHLP-2132 - Network status via integrated display
vvHLP-1651 - Transfer job group upload status display via integrated displayCOPYstation2 shall display the transfer job group upload progress status on integrated display.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1248 - Display transfer status on the integrated display ,is implemented by: vvHLP-2133 - Transfer job group upload status display via integrated display
vvHLP-1695 - Update software package using remote serverCOPYstation2 should download the selected update file and start software package installation.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1425 - Update software package using remote server ,is implemented by: vvHLP-2183 - Install selected dlua package from update server, local or USB
vvHLP-1694 - Display the dlua update files as list from the update serverCOPYstation2 should display the list of dlua update files available in the configured server and user should be able to select the specific version for installation., if there is only single update file available on the configured server then that should be considered as the
selection.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1425 - Update software package using remote server ,is implemented by: vvHLP-2170 - Display the update file list from the update server
vvHLP-1693 - Import configuration settings on COPYstation2COPYstation2 shall import the configuration JSON as the current configuration upon the validation of the schema
Status Implemented
Linked Work Items
has parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1439 - Import configuration settings on COPYstation2 via WebUI ,
is implemented by: vvHLP-1912 - Import configuration settings on COPYstation2 ,is implemented by: vvHLP-2204 - API implementation to import the config file
```
vvHLP-1690 - List the available update file on USB on webUICOPYstation2 should list the (.dlua)update file available in the USB connected and user should be able to select the specific version for installation, if there is only single (.dlua)update file available on the USB then that should be considered as the selection.
```
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 28of 31
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1426 - Update software package using the local storage or USB ,is implemented by: vvHLP-2169 - List the available update file in USB and UpdateServer on webUI
vvHLP-1689 - Filesystem access authorized directory for userCOPYstation2 must constrain filesystem access to a subtree dedicated to dataset uploads for users only authorized for dataset uploads.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1089 - STFP server - Filesystem access ,is implemented by: vvHLP-2070 - Filesystem access authorized directory for Local SFTP user
vvHLP-1688 - API option for SFTP user to define a upload directory.COPYstation2 must provide API function to define upload directory for SFTP users.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1282 - SFTP server - Directories in SFTP root ,is implemented by: vvHLP-1955 - API option for SFTP user to define a upload directory.
vvHLP-1687 - Export configuration file from copystation via APICOPYstation2 shall provide the API function to user for exporting the current user configuration in the JSON format.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1250 - Export configuration file from copystation ,is implemented by: vvHLP-2071 - Export configuration file from copystation via API
vvHLP-1680 - Change local sftp user password on webUI requestCOPYstation2 shall change the password of the existing local SFTP user on request from webUI.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1074 - SFTP server - Authentication ,is implemented by: vvHLP-1931 - Change local sftp user password on webUI request
vvHLP-1679 - API function to add/delete local sftp server userCOPYstation2 shall provide an API function to add a new user or delete an existing.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1074 - SFTP server - Authentication ,is implemented by: vvHLP-1911 - API function to add/delete local sftp server user
```
vvHLP-1678 - Provide current upload rate via APICOPYstation2 shall provide the current upload rate for the requested storage via API function with storage as parameter (slot1, slot2, internal buffer, LocalSFTP)
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1208 - Current upload rate of the storage ,is implemented by: vvHLP-1862 - Provide current upload rate via API
vvHLP-1677 - Provide the list of running transfer jobs via APICOPYstation2 shall provide the list of running transfer jobs for the whole station via API.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1200 - Display current upload jobs ,is implemented by: vvHLP-1861 - Provide the list of running transfer jobs via API
vvHLP-1676 - Provide the list of enqueued transfer jobs via APICOPYstation2 shall provide the list of enqueued transfer jobs for the whole station via API.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1200 - Display current upload jobs ,is implemented by: vvHLP-1860 - Provide the list of enqueued transfer jobs via API
vvHLP-1675 - Information to display on webUI for each job on running and enqueued job listCOPYstation2 shall display the below information for each job in the running and enqueued list.
```
Information:
```
JobIDSource
Source pathDestination
Destination pathProgress
```
StateAction buttons [ Stop ( ) toggle Restart ( )], [ Resume ( ) toggle Pause ( )], Abort (×)
```
```
Note: Action button pause/resume, stop/restart shall not be available in enqueued state i.e In the Enqueued job list only Abort will be available
```
Example Job list:
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1200 - Display current upload jobs ,is implemented by: vvHLP-1996 - Information to display on webUI for each job on running and enqueued job list
vvHLP-1674 - Display the list of enqueued transfer jobs on webUICOPYstation2 shall display the list of enqueued transfer jobs for the whole station via webUI.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1200 - Display current upload jobs ,is implemented by: vvHLP-2015 - Display the list of enqueued transfer jobs on webUI
vvHLP-1673 - API function to request cartridge ejectCOPYstation2 shall provide API function to request cartridge eject.
Status Implemented
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 29of 31
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1133 - Cartridge hotplug - unmount request ,is implemented by: vvHLP-2182 - API function to request cartridge eject
vvHLP-1672 - WebUI option to Import configuration on COPYstation2COPYstation2 must provide an option to the admin user to upload and import a settings file in the system settings page of the WebUI.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1439 - Import configuration settings on COPYstation2 via WebUI ,is implemented by: vvHLP-2168 - WebUI option to Import configuration on COPYstation2
vvHLP-1670 - Validate the private gpg keys during upload via webUICOPYstation2 shall validate if the gpg key is private and not password protected on the attempt upload via webUI
Status Rejected
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1177 - Decrypt JSON File processing ,is implemented by: vvHLP-2051 - Validate the private gpg keys during upload via webUI
vvHLP-1666 - Remove job from transfer groupCOPYstation2 shall remove the job from transfer job group on some condition for Local SFTP and Local Buffer only.
```
Note: job remove is not valid for cartridge.
```
Status Implemented
Linked Work Items
has parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1110 - CopyStation2 must display the cartridge state for the user ,
is derived from: vvHLP-1239 - Transfer module reuse ,is implemented by: vvHLP-1990 - Remove the finished job from transfer job group for internal storage ,
is related to: vvHLP-1537 - Remove a job from an existing transfer job group
vvHLP-1665 - Implement log file rotation for each dayCOPYstation2 shall rename the current log file by appending the timestamp at the end of the day, create a new log and log the information on newly created file.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1242 - Log files download option ,is implemented by: vvHLP-1909 - Implement log file rotation for each day
vvHLP-1664 - Keep logs from last 14 days onlyCOPYstation2 should keep the log files for not more than 14 days.
```
Rationale: older log files are deleted to maintain the storage space
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1242 - Log files download option ,is implemented by: vvHLP-1777 - Implementation for zipping of log files and Keep logs from last 14 days only
vvHLP-1663 - Reset the COPYstation2 software via USBCOPYstation2 must support USB keyboard input and a display output and be able to boot from a USB drive on request during startup.
Status Implemented
Linked Work Items has parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1252 - Reset the COPYstation2 software via USB drive with a keyboard and display
vvHLP-1662 - Implementation for zipping of log filesCOPYstation2 shall zip all available log file for on the request from the user to download log files.
Possible log file:
logs of last 14 dayswebUI logs
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1242 - Log files download option ,is implemented by: vvHLP-1777 - Implementation for zipping of log files and Keep logs from last 14 days only
vvHLP-1661 - Log files download option from APICOPYstation2 shall provide an option for the user to download logs via API
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1242 - Log files download option ,is implemented by: vvHLP-2107 - Log files download option from API
vvHLP-1660 - Log files download option in webUICOPYstation2 shall provide an option for the user to download logs via webUI
Status Implemented
Linked Work Items
has parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1242 - Log files download option ,
is implemented by: vvHLP-2047 - Log files download option in webUI ,is implemented by: vvHLP-2232 - Download webUI logs
vvHLP-1659 - webUI option to list the SFTP userCOPYstation2 should have an option available for listing the existing SFTP users
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1074 - SFTP server - Authentication ,is implemented by: vvHLP-1994 - webUI option to list the SFTP user
vvHLP-1658 - webUI option to register/modify SFTP userCOPYstation2 should have an option available for add/delete users and change password for existing users.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1074 - SFTP server - Authentication ,is implemented by: vvHLP-1866 - webUI option to register/modify SFTP user
vvHLP-1657 - Provide the current operation mode info to user via APICOPYstation2 shall provide the current operation mode info to user via API function.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1244 - Operation mode information to user ,is implemented by: vvHLP-1961 - Provide the current operation mode info to user via API
vvHLP-1656 - webUI option to upload DLUA file for updating software packageCOPYstation2 shall provide an option to the user for upload the DLUA files for updating the software pacakges
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 30of 31
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1432 - Update software package using DLUA file upload via webUI ,is implemented by: vvHLP-2167 - webUI option to upload DLUA file for updating software package
vvHLP-1655 - webUI option to update software package via USBCOPYstation2 must provide option to user to update software package from the USB on webUI.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1426 - Update software package using the local storage or USB ,is implemented by: vvHLP-2166 - webUI option to update software package via USB
vvHLP-1654 - webUI option to configure remote server for software package updateCOPYstation2 must provide option to the user on webUI to configure a server of any of the following type SFTP, AZURE, AWS, SMB specifically for updates.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1425 - Update software package using remote server ,is implemented by: vvHLP-2165 - webUI option to configure remote server for software package update
vvHLP-1653 - Monitor the Local SFTP path for new filesCOPYstaion2 shall monitor the local storage paths for file changes and track if the file belongs to datasets.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1103 - SFTP server - automatic transfer ,is implemented by: vvHLP-1767 - Monitor and Create transfer job for newly uploaded complete dataset within 6 minutes for SFTP server
```
vvHLP-1652 - Provide the information about slot and cartridge connectors plugin cycle over APICOPYstation2 shall send slot and cartridge connectors plugin cycle information over API with parameters (cartidge1, cartidge2, slot1 & slot2).
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,specifies: vvHLP-1104 - Track the Plugin Cycles of the cartridge and slot connectors ,is implemented by: vvHLP-2106 - Provide the information about slot and cartridge connectors plugin cycle over API
vvHLP-1710 - API function to delete untracked files from the internal bufferCOPYstation2 shall provide an API function to the user for configuring the internal buffer clean up by deleting the untracked files.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,specifies: vvHLP-1336 - Delete untracked files from the internal buffer ,is implemented by: vvHLP-1962 - API function to get/set internal storage cleanup
vvHLP-1711 - LED state display for the cartridge stateCOPYstation2 must display the information on the cartridge status of the cartridge slots to the user via the LEDs for each cartridge.
```
Hint: The LED colors/codes must be the same as with the IPE891.
```
```
ref: vvHLP-1553 - LEDs DATAdrive 2 Status
```
Status In Progress
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1110 - CopyStation2 must display the cartridge state for the user ,is implemented by: vvHLP-2184 - LED state display for the cartridge state
```
vvHLP-1714 - Network interface configuration option from webUICOPYstation2 webUI shall provide option to the user for the network configuration, User should be able to select IP seetting DHCP or Manual and for manual setting should be able to set IPV4 or IPV6 informations(IP address, subnet prefix, gateway, preffered DNS
```
```
alternate DNS).
```
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1128 - Production - Network interface configuration ,is implemented by: vvHLP-2046 - Network interface configuration option from webUI
vvHLP-1715 - Network interface configuration option from APICOPYstation2 shall provide an API function to set the network interface configuration.
Status Verified
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1128 - Production - Network interface configuration ,is implemented by: vvHLP-2105 - Network interface configuration option from API
vvHLP-1716 - set the network interface configuration for the systemCOPYstation2 shall set the network interface configuration upon the request from webUI or API.
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is derived from: vvHLP-1128 - Production - Network interface configuration ,is implemented by: vvHLP-1776 - Set the network interface configuration for the system
vvHLP-1717 - Display current upload status for Local Buffer and Local SFTPCOPYstation2 shall display the current progress of jobs for local buffer and local sftp
Number of Jobs completed/hrUpload rate
Historic data for graph
Status Implemented
Linked Work Itemshas parent: vvHLP-1160 - Production Tools ,is branched from: vvHLP-1200 - Display current upload jobs ,is implemented by: vvHLP-2043 - Display current upload status for Local Buffer and Local SFTP
```
COPYstation2_TRS(rev. 1917962)
```
IPE891 - COPYstation2_TRS © IPETRONIK GmbH & Co. KG AuthorGonzalez, JuanUpdated2025-11-24 08:37Page 31of 31