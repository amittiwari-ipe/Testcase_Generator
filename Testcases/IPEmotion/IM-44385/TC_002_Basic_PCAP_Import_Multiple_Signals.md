# TC_002 - Basic PCAP Import with Multiple Signals

## Description
Verify that IPEmotion can successfully import a PCAP file containing Ethernet traffic and extract multiple signals from the same PDU using ARXML signal definitions.

## Pre-Condition

### Software Setup:

#### Windows
- IPEmotion 2024 R2 or later installed
- Traffic-to-Signal converter license activated
- Test PCAP file: `eth_traffic_multi_signal.pcap` (available in test data folder)
- ARXML file: `multi_signal_definition.arxml` (contains 5 signal definitions in one PDU)
- Create test folder: `C:\TestData\IM-44385\TC_002\`
- Copy PCAP and ARXML files to test folder

#### Linux
- IPEmotion installed via Docker or native installation
- Traffic-to-Signal converter license activated
- Test PCAP file: `eth_traffic_multi_signal.pcap`
- ARXML file: `multi_signal_definition.arxml`
- Create test folder: `/home/testuser/TestData/IM-44385/TC_002/`
- Ensure read/write permissions on test folder

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| 1 | Launch IPEmotion application | IPEmotion opens successfully |
| 2 | Navigate to DATA MANAGER workspace | DATA MANAGER workspace is displayed |
| 3 | Click Import → Traffic Files → PCAP | PCAP import dialog opens |
| 4 | Browse and select `eth_traffic_multi_signal.pcap` | File is selected and path displayed |
| 5 | Click "Load ARXML Configuration" button | ARXML file selection dialog opens |
| 6 | Browse and select `multi_signal_definition.arxml` | ARXML file loaded successfully |
| 7 | Verify all 5 signals appear in preview: SpeedSignal, RPMSignal, TempSignal, PressureSignal, StatusSignal | All 5 signals listed with correct types and units |
| 8 | Enable all signals for extraction (checkboxes) | All signal checkboxes are checked |
| 9 | Click "Import" to start Traffic-to-Signal conversion | Progress bar shows conversion in progress |
| 10 | Wait for conversion to complete | "Import completed successfully" message, shows "5 signals extracted" |
| 11 | Navigate to SIGNALS workspace | SIGNALS workspace opens |
| 12 | Verify all 5 signals appear in signal tree | All signals visible: SpeedSignal, RPMSignal, TempSignal, PressureSignal, StatusSignal |
| 13 | Select SpeedSignal → View Properties | Unit: km/h, Type: uint16, Range: 0-250 |
| 14 | Select RPMSignal → View Properties | Unit: rpm, Type: uint16, Range: 0-8000 |
| 15 | Select TempSignal → View Properties | Unit: °C, Type: int8, Range: -40 to 150 |
| 16 | Select PressureSignal → View Properties | Unit: bar, Type: uint16, Range: 0-10 |
| 17 | Select StatusSignal → View Properties | Type: uint8, Enum: {0=Off, 1=On, 2=Error} |
| 18 | Verify all signals have same sample count | All signals show identical sample count (1000 samples) |
| 19 | Verify signals are time-synchronized | All signals share same timestamp for sample #1 |
| 20 | Navigate to VIEW workspace | VIEW workspace opens |
| 21 | Drag SpeedSignal and RPMSignal to Chart 1 | Both signals displayed in chart with different Y-axes |
| 22 | Verify signal curves are displayed correctly | Curves show expected value patterns without gaps |

## Notes
- Test PCAP file contains 1000 Ethernet frames with SOME/IP messages
- All signals are extracted from the same PDU (Service ID: 0x1234, Method ID: 0x5678)
- Signal layout in PDU: Speed(0-15), RPM(16-31), Temp(32-39), Pressure(40-55), Status(56-63)
- Byte order: Big-endian (network byte order)
- Reference: IPEmotion User Manual Chapter 16.3 (Ethernet SOME/IP)
- Reference: IPEmotion User Manual Chapter 21 (DATA MANAGER)
- Reference: IPEmotion User Manual Chapter 20 (VIEW workspace)
- KD Item: IM-44385

## Priority
High

## Coverage
- [x] Positive Testing
- [ ] Negative Testing
- [ ] Performance Testing
- [x] Functional Testing
