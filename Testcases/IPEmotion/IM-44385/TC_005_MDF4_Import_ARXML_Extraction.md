# TC_005 - MDF4 Traffic File Import with ARXML Signal Extraction

## Description
Verify that IPEmotion can successfully import an MDF4 file containing Ethernet traffic and extract signals using ARXML definitions for SOME/IP PDUs.

## Pre-Condition

### Software Setup:

#### Windows
- IPEmotion 2024 R2 or later installed
- Traffic-to-Signal converter license activated
- Activated plugins: None
- Test data location: M:\Testmanagement\DUS\01_Projekte\00_IPEmotion\03_Testdaten\Allgemein\IPEmotion\Traffic-Konvertierung\ETH\IM-44385\
- Required files:
  - ETH_Traffic_MDF4_001.MF4 (Ethernet traffic recording)
  - ETH_Signals_SOMEIP.arxml (ARXML signal definitions)
- Hardware requirements: None (file-based testing)
- License requirements: IPEmotion Standard + Traffic-to-Signal converter

#### Linux
- IPEmotion 2024 R2 or later installed (Docker/native)
- Traffic-to-Signal converter license activated
- Activated plugins: None
- Test data location: /home/testuser/testdata/IPEmotion/Traffic-Konvertierung/ETH/IM-44385/
- Required files:
  - ETH_Traffic_MDF4_001.MF4
  - ETH_Signals_SOMEIP.arxml
- Hardware requirements: None
- License requirements: IPEmotion Standard + Traffic-to-Signal converter

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| 1 | Start IPEmotion<br>Activated plugins:<br>None | IPEmotion starts successfully |
| 2 | File → Administration → Reset → Yes | IPEmotion resets to default state |
| 3 | File → Options → Data manager → Tree display style: → File / Group / Signal → OK | Tree display style set to hierarchical view |
| 4 | Data manager → Files → Load: Open dropdown list → Load → ETH_Traffic_MDF4_001.MF4 → Open<br><br>M:\Testmanagement\DUS\01_Projekte\00_IPEmotion\03_Testdaten\Allgemein\IPEmotion\Traffic-Konvertierung\ETH\IM-44385\ | File loads successfully<br><br>ETH_Traffic_MDF4_001.MF4 appears in Files tree |
| 5 | ETH_Traffic_MDF4_001.MF4 → Speichergruppe-1 → ETH / ETH1 Traffic-Kanal → Context menu → Convert traffic ... | "Assignation traffic description file" window turns up with the following data: [#1]<br><br>Traffic type: ETH SignalPDU<br>Interface: All<br>Filter: Unchecked<br>Description file: &lt;empty&gt; |
| 6 | "Assignation traffic description file" window → Description file → … → Select ETH_Signals_SOMEIP.arxml → Open<br><br>M:\Testmanagement\DUS\01_Projekte\00_IPEmotion\03_Testdaten\Allgemein\IPEmotion\Traffic-Konvertierung\ETH\IM-44385\ | "Assignation traffic description file" window updated:<br><br>Description file: ETH_Signals_SOMEIP.arxml |
| 7 | "Assignation traffic description file" window → OK | Traffic conversion starts<br><br>Progress indicator visible |
| 8 | Wait for conversion to complete | Conversion completes successfully<br><br>No error messages displayed |
| 9 | ETH_Traffic_MDF4_001.MF4 → Speichergruppe-1 → Properties → General → Channel count | Channel Count: 1847 [#2] |
| 10 | ETH_Traffic_MDF4_001.MF4 → Speichergruppe-1 | The following sub-nodes are available now: [#3]<br><br>ETH / ETH1 Traffic-Kanal<br>VehicleSpeed_SOMEIP_Service_Rx<br>EngineRPM_SOMEIP_Service_Rx<br>BatteryVoltage_SOMEIP_Service_Rx<br>DiagnosticStatus_SOMEIP_Service_Rx |
| 11 | ETH_Traffic_MDF4_001.MF4 → Speichergruppe-1 → ETH / ETH1 Traffic-Kanal → VehicleSpeed_SOMEIP_Service_Rx → Properties → General | The following data is available:<br><br>General<br>Type: Signal<br>Name: VehicleSpeed_SOMEIP_Service_Rx<br>Description: &lt;empty&gt;<br>Reference: VehicleSpeed_SOMEIP_Service_Rx/VehicleData_PDU/1234/VehicleECU/192.168.1.10:30501/ETH_Signals_SOMEIP/ETH-1/TrafficToSignalSystem |
| 12 | VehicleSpeed_SOMEIP_Service_Rx → Properties → Values | The following data is available:<br><br>Values<br>Value count: 5420<br>Unit: km/h<br>Data type: 16-Bit integer unsigned<br>Physical Min: 0<br>Physical Max: 300<br>Display Min: 0<br>Display Max: 300<br>Decimal places: Automatic<br>Implicit: Unchecked<br>Task: Default<br>Transformation mode: FactorOffset<br>NoValue defined: Unchecked |
| 13 | VehicleSpeed_SOMEIP_Service_Rx → Properties → User-defined parameters | The following data is available:<br><br>User-defined parameters<br>ref:sourceType: ECU<br>ref:busType: ETHERNET<br>ref:typeName: EthSignalPdu<br>ref:messageName: VehicleData_PDU<br>ref:sourceFile: ETH_Signals_SOMEIP<br>ref:interface: ETH-1<br>ref:system: TrafficToSignalSystem<br>ref:messageId: 1234<br>ref:senderName: VehicleECU |
| 14 | ETH_Traffic_MDF4_001.MF4 → Grid → column VehicleSpeed_SOMEIP_Service_Rx Speichergruppe-1 | Index 0: 0<br>Index 1: 0<br>Index 2: 15<br>Index 3: 32<br>...<br>Index 5418: 87<br>Index 5419: 85 |
| 15 | ETH_Traffic_MDF4_001.MF4 → Speichergruppe-1 → ETH / ETH1 Traffic-Kanal → EngineRPM_SOMEIP_Service_Rx → Properties → General | The following data is available:<br><br>General<br>Type: Signal<br>Name: EngineRPM_SOMEIP_Service_Rx<br>Description: &lt;empty&gt;<br>Reference: EngineRPM_SOMEIP_Service_Rx/VehicleData_PDU/1234/VehicleECU/192.168.1.10:30501/ETH_Signals_SOMEIP/ETH-1/TrafficToSignalSystem |
| 16 | EngineRPM_SOMEIP_Service_Rx → Properties → Values | The following data is available:<br><br>Values<br>Value count: 5420<br>Unit: rpm<br>Data type: 16-Bit integer unsigned<br>Physical Min: 0<br>Physical Max: 8000<br>Display Min: 0<br>Display Max: 8000<br>Decimal places: Automatic<br>Implicit: Unchecked<br>Task: Default<br>Transformation mode: FactorOffset<br>NoValue defined: Unchecked |
| 17 | ETH_Traffic_MDF4_001.MF4 → Grid → column EngineRPM_SOMEIP_Service_Rx Speichergruppe-1 | Index 0: 850<br>Index 1: 850<br>Index 2: 875<br>Index 3: 920<br>...<br>Index 5418: 2450<br>Index 5419: 2420 |
| 18 | ETH_Traffic_MDF4_001.MF4 → Speichergruppe-1 → ETH / ETH1 Traffic-Kanal → BatteryVoltage_SOMEIP_Service_Rx → Properties → Values | The following data is available:<br><br>Values<br>Value count: 5420<br>Unit: V<br>Data type: 32-Bit floating point<br>Physical Min: -3.4028234663852886E+38<br>Physical Max: 3.4028234663852886E+38<br>Display Min: 0<br>Display Max: 20<br>Decimal places: Automatic<br>Implicit: Unchecked<br>Task: Default<br>Transformation mode: FactorOffset<br>NoValue defined: Checked<br>Value for invalid acquisition values: NaN |
| 19 | ETH_Traffic_MDF4_001.MF4 → Grid → column BatteryVoltage_SOMEIP_Service_Rx Speichergruppe-1 | Index 0: 13.8<br>Index 1: 13.8<br>Index 2: 13.7<br>Index 3: 13.9<br>...<br>Index 5418: 14.2<br>Index 5419: 14.1 |
| 20 | ETH_Traffic_MDF4_001.MF4 → Speichergruppe-1 → ETH / ETH1 Traffic-Kanal → Convert traffic ... | "Assignation traffic description file" window turns up with the following data: [#1] [#4]<br><br>Traffic type: ETH SignalPDU<br>Interface: All<br>Filter: Unchecked<br>Description file: ETH_Signals_SOMEIP.arxml |
| 21 | "Assignation traffic description file" window → Cancel | Dialog closes<br><br>No changes to signals |

## Notes
- [#1] First-time traffic conversion dialog shows empty description file
- [#2] Channel count includes original traffic channel plus extracted signals
- [#3] Extracted signals are added as sub-nodes under storage group
- [#4] Previously configured ARXML file is remembered for subsequent conversions
- Test validates MDF4 format support for Ethernet traffic recordings
- SOME/IP protocol decoding validation
- Signal extraction with proper units, data types, and ranges
- Value count verification ensures all PDU instances were processed
- Index validation confirms actual signal values extracted correctly
- Float signal (BatteryVoltage) validates NaN handling for invalid values
- KD Item: IM-44385
- Reference: IPEmotion User Manual Chapter 21 (DATA MANAGER workspace)
- Reference: IPEmotion User Manual Chapter 25.8.12 (MDF4 Import)

## Priority
High

## Coverage
- [x] Positive Testing
- [ ] Negative Testing
- [ ] Performance Testing
- [x] Functional Testing
