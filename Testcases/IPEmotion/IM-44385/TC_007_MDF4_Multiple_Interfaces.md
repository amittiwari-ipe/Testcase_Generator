# TC_007 - MDF4 Import with Multiple Ethernet Interfaces

## Description
Verify that IPEmotion correctly handles MDF4 files containing traffic from multiple Ethernet interfaces and can extract signals per interface with proper segregation.

## Pre-Condition

### Software Setup:

#### Windows
- IPEmotion 2024 R2 or later installed
- Traffic-to-Signal converter license activated
- Activated plugins: None
- Test data location: M:\Testmanagement\DUS\01_Projekte\00_IPEmotion\03_Testdaten\Allgemein\IPEmotion\Traffic-Konvertierung\ETH\IM-44385\
- Required files:
  - ETH_MultiInterface_Recording.MF4 (contains ETH1 and ETH2 traffic)
  - ETH_Interface1_Signals.arxml (signals for ETH1)
  - ETH_Interface2_Signals.arxml (signals for ETH2)
- Hardware requirements: None
- License requirements: IPEmotion Standard + Traffic-to-Signal converter

#### Linux
- IPEmotion 2024 R2 or later installed (Docker/native)
- Traffic-to-Signal converter license activated
- Activated plugins: None
- Test data location: /home/testuser/testdata/IPEmotion/Traffic-Konvertierung/ETH/IM-44385/
- Required files:
  - ETH_MultiInterface_Recording.MF4
  - ETH_Interface1_Signals.arxml
  - ETH_Interface2_Signals.arxml
- Hardware requirements: None
- License requirements: IPEmotion Standard + Traffic-to-Signal converter

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| 1 | Start IPEmotion<br>Activated plugins:<br>None | IPEmotion starts successfully |
| 2 | File → Administration → Reset → Yes | IPEmotion resets to default state |
| 3 | File → Options → Data manager → Tree display style: → File / Group / Signal → OK | Tree display configured |
| 4 | Data manager → Files → Load: Open dropdown list → Load → ETH_MultiInterface_Recording.MF4 → Open<br><br>M:\Testmanagement\DUS\01_Projekte\00_IPEmotion\03_Testdaten\Allgemein\IPEmotion\Traffic-Konvertierung\ETH\IM-44385\ | ETH_MultiInterface_Recording.MF4 loaded |
| 5 | ETH_MultiInterface_Recording.MF4 → Speichergruppe-1 | The following sub-nodes are visible: [#1]<br><br>ETH / ETH1 Traffic-Kanal<br>ETH / ETH2 Traffic-Kanal |
| 6 | ETH_MultiInterface_Recording.MF4 → Speichergruppe-1 → ETH / ETH1 Traffic-Kanal → Context menu → Convert traffic ... | "Assignation traffic description file" window turns up with the following data: [#2]<br><br>Traffic type: ETH SignalPDU<br>Interface: ETH1 [#3]<br>Filter: Unchecked<br>Description file: &lt;empty&gt; |
| 7 | "Assignation traffic description file" window → Description file → … → Select ETH_Interface1_Signals.arxml → Open<br><br>M:\Testmanagement\DUS\01_Projekte\00_IPEmotion\03_Testdaten\Allgemein\IPEmotion\Traffic-Konvertierung\ETH\IM-44385\ | Description file: ETH_Interface1_Signals.arxml |
| 8 | "Assignation traffic description file" window → OK | Conversion starts for ETH1 interface |
| 9 | Wait for ETH1 conversion to complete | Conversion completes successfully |
| 10 | ETH_MultiInterface_Recording.MF4 → Speichergruppe-1 → ETH / ETH1 Traffic-Kanal | The following sub-nodes are now available under ETH1: [#4]<br><br>PowertrainData_ETH1_Rx<br>ChassisData_ETH1_Rx<br>DiagnosticInfo_ETH1_Rx |
| 11 | ETH_MultiInterface_Recording.MF4 → Speichergruppe-1 → ETH / ETH2 Traffic-Kanal → Context menu → Convert traffic ... | "Assignation traffic description file" window turns up with the following data:<br><br>Traffic type: ETH SignalPDU<br>Interface: ETH2 [#5]<br>Filter: Unchecked<br>Description file: &lt;empty&gt; |
| 12 | "Assignation traffic description file" window → Description file → … → Select ETH_Interface2_Signals.arxml → Open<br><br>M:\Testmanagement\DUS\01_Projekte\00_IPEmotion\03_Testdaten\Allgemein\IPEmotion\Traffic-Konvertierung\ETH\IM-44385\ | Description file: ETH_Interface2_Signals.arxml |
| 13 | "Assignation traffic description file" window → OK | Conversion starts for ETH2 interface |
| 14 | Wait for ETH2 conversion to complete | Conversion completes successfully |
| 15 | ETH_MultiInterface_Recording.MF4 → Speichergruppe-1 → ETH / ETH2 Traffic-Kanal | The following sub-nodes are now available under ETH2: [#6]<br><br>BodyElectronics_ETH2_Rx<br>Infotainment_ETH2_Rx<br>ADAS_Data_ETH2_Rx |
| 16 | ETH_MultiInterface_Recording.MF4 → Speichergruppe-1 → Properties → General → Channel count | Channel Count: 8 [#7]<br><br>(2 traffic channels + 3 ETH1 signals + 3 ETH2 signals) |
| 17 | ETH_MultiInterface_Recording.MF4 → Speichergruppe-1 → ETH / ETH1 Traffic-Kanal → PowertrainData_ETH1_Rx → Properties → General | The following data is available:<br><br>General<br>Type: Signal<br>Name: PowertrainData_ETH1_Rx<br>Description: &lt;empty&gt;<br>Reference: PowertrainData_ETH1_Rx/Powertrain_PDU/2001/PowertrainECU/192.168.1.10:30500/ETH_Interface1_Signals/ETH-1/TrafficToSignalSystem |
| 18 | PowertrainData_ETH1_Rx → Properties → Values | The following data is available:<br><br>Values<br>Value count: 12450<br>Unit: &lt;empty&gt;<br>Data type: 32-Bit integer unsigned<br>Physical Min: 0<br>Physical Max: 4294967295<br>Display Min: 0<br>Display Max: 100000<br>Decimal places: 0<br>Implicit: Unchecked<br>Task: Default<br>Transformation mode: FactorOffset<br>NoValue defined: Unchecked |
| 19 | PowertrainData_ETH1_Rx → Properties → User-defined parameters | The following data is available:<br><br>User-defined parameters<br>ref:sourceType: ECU<br>ref:busType: ETHERNET<br>ref:typeName: EthSignalPdu<br>ref:messageName: Powertrain_PDU<br>ref:sourceFile: ETH_Interface1_Signals<br>ref:interface: ETH-1 [#8]<br>ref:system: TrafficToSignalSystem<br>ref:messageId: 2001<br>ref:senderName: PowertrainECU |
| 20 | ETH_MultiInterface_Recording.MF4 → Grid → column PowertrainData_ETH1_Rx Speichergruppe-1 | Index 0: 1000<br>Index 1: 1025<br>Index 2: 1050<br>...<br>Index 12448: 45820<br>Index 12449: 45900 |
| 21 | ETH_MultiInterface_Recording.MF4 → Speichergruppe-1 → ETH / ETH2 Traffic-Kanal → BodyElectronics_ETH2_Rx → Properties → General | The following data is available:<br><br>General<br>Type: Signal<br>Name: BodyElectronics_ETH2_Rx<br>Description: &lt;empty&gt;<br>Reference: BodyElectronics_ETH2_Rx/Body_PDU/3001/BodyECU/192.168.2.20:40100/ETH_Interface2_Signals/ETH-2/TrafficToSignalSystem |
| 22 | BodyElectronics_ETH2_Rx → Properties → Values | The following data is available:<br><br>Values<br>Value count: 8734<br>Unit: &lt;empty&gt;<br>Data type: 16-Bit integer unsigned<br>Physical Min: 0<br>Physical Max: 65535<br>Display Min: 0<br>Display Max: 10000<br>Decimal places: 0<br>Implicit: Unchecked<br>Task: Default<br>Transformation mode: FactorOffset<br>NoValue defined: Unchecked |
| 23 | BodyElectronics_ETH2_Rx → Properties → User-defined parameters | The following data is available:<br><br>User-defined parameters<br>ref:sourceType: ECU<br>ref:busType: ETHERNET<br>ref:typeName: EthSignalPdu<br>ref:messageName: Body_PDU<br>ref:sourceFile: ETH_Interface2_Signals<br>ref:interface: ETH-2 [#9]<br>ref:system: TrafficToSignalSystem<br>ref:messageId: 3001<br>ref:senderName: BodyECU |
| 24 | ETH_MultiInterface_Recording.MF4 → Grid → column BodyElectronics_ETH2_Rx Speichergruppe-1 | Index 0: 500<br>Index 1: 510<br>Index 2: 515<br>...<br>Index 8732: 2340<br>Index 8733: 2355 |
| 25 | Verify signal segregation: PowertrainData_ETH1_Rx appears only under ETH1, BodyElectronics_ETH2_Rx appears only under ETH2 | Signals correctly segregated by source interface<br><br>No cross-contamination between ETH1 and ETH2 signals |

## Notes
- [#1] MDF4 file contains traffic from two separate Ethernet interfaces
- [#2] Conversion dialog automatically detects interface ETH1 when converting ETH1 traffic
- [#3] Interface field shows specific interface, not "All"
- [#4] Extracted signals appear as sub-nodes under their source traffic channel
- [#5] Converting ETH2 separately shows interface ETH2 in dialog
- [#6] ETH2 signals extracted independently from ETH1
- [#7] Total channels = 2 traffic + 6 extracted signals (3 per interface)
- [#8] User-defined parameter "ref:interface" confirms signal from ETH-1
- [#9] User-defined parameter "ref:interface" confirms signal from ETH-2
- Different sample counts (12450 vs 8734) indicate independent recording rates per interface
- Different IP addresses (192.168.1.x vs 192.168.2.x) indicate separate networks
- Different ports and message IDs confirm distinct SOME/IP services
- Test validates multi-interface support in single MDF4 file
- Each interface processes independently with separate ARXML files
- Signals correctly tagged with source interface in properties
- KD Item: IM-44385
- Reference: IPEmotion User Manual Chapter 16.4 (Multiple Ethernet Interfaces)
- Reference: MDF4 specification for multi-bus recordings

## Priority
High

## Coverage
- [x] Positive Testing
- [ ] Negative Testing
- [ ] Performance Testing
- [x] Functional Testing
