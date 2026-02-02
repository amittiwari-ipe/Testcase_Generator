# TC_006 - MDF4 Selective Signal Import with Filter

## Description
Verify that users can selectively import specific signals from MDF4 traffic file using the "Select signals..." feature in ARXML import dialog.

## Pre-Condition

### Software Setup:

#### Windows
- IPEmotion 2024 R2 or later installed
- Traffic-to-Signal converter license activated
- Activated plugins: None
- Test data location: M:\Testmanagement\DUS\01_Projekte\00_IPEmotion\03_Testdaten\Allgemein\IPEmotion\Traffic-Konvertierung\ETH\IM-44385\
- Required files:
  - ETH_Traffic_MDF4_Large.MF4 (contains traffic for 50+ signals)
  - ETH_Complete_SignalSet.arxml (ARXML with 50+ signal definitions)
- Hardware requirements: None
- License requirements: IPEmotion Standard + Traffic-to-Signal converter

#### Linux
- IPEmotion 2024 R2 or later installed (Docker/native)
- Traffic-to-Signal converter license activated
- Activated plugins: None
- Test data location: /home/testuser/testdata/IPEmotion/Traffic-Konvertierung/ETH/IM-44385/
- Required files:
  - ETH_Traffic_MDF4_Large.MF4
  - ETH_Complete_SignalSet.arxml
- Hardware requirements: None
- License requirements: IPEmotion Standard + Traffic-to-Signal converter

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| 1 | Start IPEmotion<br>Activated plugins:<br>None | IPEmotion starts successfully |
| 2 | File → Administration → Reset → Yes | IPEmotion resets to default state |
| 3 | File → Options → Data manager → Tree display style: → File / Group / Signal → OK | Tree display style configured |
| 4 | Data manager → Files → Load: Open dropdown list → Load → ETH_Traffic_MDF4_Large.MF4 → Open<br><br>M:\Testmanagement\DUS\01_Projekte\00_IPEmotion\03_Testdaten\Allgemein\IPEmotion\Traffic-Konvertierung\ETH\IM-44385\ | ETH_Traffic_MDF4_Large.MF4 loaded successfully |
| 5 | ETH_Traffic_MDF4_Large.MF4 → Speichergruppe-1 → ETH / ETH1 Traffic-Kanal → Context menu → Convert traffic ... | "Assignation traffic description file" window turns up with the following data: [#1]<br><br>Traffic type: ETH SignalPDU<br>Interface: All<br>Filter: Unchecked<br>Description file: &lt;empty&gt; |
| 6 | "Assignation traffic description file" window → Description file → … → Select ETH_Complete_SignalSet.arxml → Open<br><br>M:\Testmanagement\DUS\01_Projekte\00_IPEmotion\03_Testdaten\Allgemein\IPEmotion\Traffic-Konvertierung\ETH\IM-44385\ | Description file: ETH_Complete_SignalSet.arxml |
| 7 | "Assignation traffic description file" window → Description file → "Select signals..." - Button | "AUTOSAR import" window opens with signal grid<br><br>Grid displays all available signals from ARXML (50+ signals listed) |
| 8 | "AUTOSAR import" window → Grid → Scroll to locate signals:<br><br>CriticalTemperature_Sensor_1_Rx<br>CriticalPressure_HydraulicSystem_Rx<br>EmergencyStop_Status_Rx | Signals visible in grid |
| 9 | "AUTOSAR import" window → Grid → Select:<br><br>CriticalTemperature_Sensor_1_Rx<br>CriticalPressure_HydraulicSystem_Rx<br>EmergencyStop_Status_Rx<br><br>→ column Selection: Checked | 3 signals selected<br><br>Checkboxes in Selection column: Checked<br>Other signals remain: Unchecked |
| 10 | "AUTOSAR import" window → Verify selection count in status bar | Status shows: "3 of 52 signals selected" [#2] |
| 11 | "AUTOSAR import" window → OK | "AUTOSAR import" window closes<br><br>Returns to "Assignation traffic description file" window |
| 12 | "Assignation traffic description file" window → Verify description shows | Description file: ETH_Complete_SignalSet.arxml<br>Selected signals: 3 |
| 13 | "Assignation traffic description file" window → OK | Traffic conversion starts for 3 selected signals only |
| 14 | Wait for conversion to complete | Conversion completes successfully |
| 15 | ETH_Traffic_MDF4_Large.MF4 → Speichergruppe-1 → Properties → General → Channel count | Channel Count: 4 [#3]<br><br>(1 traffic channel + 3 extracted signals) |
| 16 | ETH_Traffic_MDF4_Large.MF4 → Speichergruppe-1 | The following sub-nodes are available now: [#4]<br><br>ETH / ETH1 Traffic-Kanal<br>CriticalTemperature_Sensor_1_Rx<br>CriticalPressure_HydraulicSystem_Rx<br>EmergencyStop_Status_Rx<br><br>Other signals NOT present (correctly filtered) |
| 17 | ETH_Traffic_MDF4_Large.MF4 → Speichergruppe-1 → ETH / ETH1 Traffic-Kanal → CriticalTemperature_Sensor_1_Rx → Properties → General | The following data is available:<br><br>General<br>Type: Signal<br>Name: CriticalTemperature_Sensor_1_Rx<br>Description: Critical temperature sensor monitoring<br>Reference: CriticalTemperature_Sensor_1_Rx/TempMonitor_PDU/5001/TempSensorECU/192.168.1.20:40100/ETH_Complete_SignalSet/ETH-1/TrafficToSignalSystem |
| 18 | CriticalTemperature_Sensor_1_Rx → Properties → Values | The following data is available:<br><br>Values<br>Value count: 8923<br>Unit: °C<br>Data type: 16-Bit integer signed<br>Physical Min: -40<br>Physical Max: 200<br>Display Min: -40<br>Display Max: 200<br>Decimal places: 1<br>Implicit: Unchecked<br>Task: Default<br>Transformation mode: FactorOffset<br>NoValue defined: Unchecked |
| 19 | ETH_Traffic_MDF4_Large.MF4 → Grid → column CriticalTemperature_Sensor_1_Rx Speichergruppe-1 | Index 0: 22<br>Index 1: 22<br>Index 2: 23<br>Index 3: 24<br>...<br>Index 8921: 87<br>Index 8922: 88 |
| 20 | ETH_Traffic_MDF4_Large.MF4 → Speichergruppe-1 → ETH / ETH1 Traffic-Kanal → CriticalPressure_HydraulicSystem_Rx → Properties → Values | The following data is available:<br><br>Values<br>Value count: 8923<br>Unit: bar<br>Data type: 16-Bit integer unsigned<br>Physical Min: 0<br>Physical Max: 500<br>Display Min: 0<br>Display Max: 500<br>Decimal places: 2<br>Implicit: Unchecked<br>Task: Default<br>Transformation mode: FactorOffset<br>NoValue defined: Unchecked |
| 21 | ETH_Traffic_MDF4_Large.MF4 → Speichergruppe-1 → ETH / ETH1 Traffic-Kanal → EmergencyStop_Status_Rx → Properties → Values | The following data is available:<br><br>Values<br>Value count: 8923<br>Unit: &lt;empty&gt;<br>Data type: 8-Bit integer unsigned<br>Physical Min: 0<br>Physical Max: 3<br>Display Min: 0<br>Display Max: 3<br>Decimal places: 0<br>Implicit: Unchecked<br>Task: Default<br>Transformation mode: FactorOffset<br>NoValue defined: Unchecked |
| 22 | ETH_Traffic_MDF4_Large.MF4 → Grid → column EmergencyStop_Status_Rx Speichergruppe-1 | Index 0: 0<br>Index 1: 0<br>Index 2: 0<br>Index 3: 0<br>...<br>Index 8921: 1<br>Index 8922: 1 |
| 23 | Files → Remove → No | File unloaded from Data Manager |

## Notes
- [#1] Dialog allows selective signal import via "Select signals..." button
- [#2] Total signal count in ARXML is 52, user selects 3 specific signals
- [#3] Channel count = 1 traffic channel + 3 selected signals (not 52)
- [#4] Only selected signals extracted, others correctly filtered out
- Test validates selective import reduces memory usage and processing time
- Useful when ARXML contains many signals but only subset needed
- Signal properties and values extracted correctly despite filtering
- All three selected signals have same sample count (synchronized)
- Different data types validated: signed int16, unsigned int16, uint8
- Different units validated: °C, bar, empty
- Status enumeration (EmergencyStop) values: 0=Normal, 1=Active, 2=Error, 3=Unknown
- KD Item: IM-44385
- Reference: IPEmotion User Manual Chapter 21.3 (Signal Selection)

## Priority
High

## Coverage
- [x] Positive Testing
- [ ] Negative Testing
- [ ] Performance Testing
- [x] Functional Testing
