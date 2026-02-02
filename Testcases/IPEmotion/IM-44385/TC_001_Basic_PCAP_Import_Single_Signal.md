# TC_001 - Basic PCAP Import with Single Signal

## Description
Verify that IPEmotion can successfully import a PCAP file containing Ethernet traffic and extract a single signal using ARXML signal definitions.

## Pre-Condition

### Software Setup:

#### Windows
- IPEmotion 2024 R2 or later installed
- Traffic-to-Signal converter license activated
- Test PCAP file: `eth_traffic_single_signal.pcap` (available in test data folder)
- ARXML file: `single_signal_definition.arxml` (contains one signal definition)
- Create test folder: `C:\TestData\IM-44385\TC_001\`
- Copy PCAP and ARXML files to test folder

#### Linux
- IPEmotion installed via Docker or native installation
- Traffic-to-Signal converter license activated
- Test PCAP file: `eth_traffic_single_signal.pcap`
- ARXML file: `single_signal_definition.arxml`
- Create test folder: `/home/testuser/TestData/IM-44385/TC_001/`
- Ensure read/write permissions on test folder

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| 1 | Launch IPEmotion application | IPEmotion opens successfully |
| 2 | Navigate to DATA MANAGER workspace | DATA MANAGER workspace is displayed |
| 3 | Click Import → Traffic Files → PCAP | PCAP import dialog opens |
| 4 | Browse and select `eth_traffic_single_signal.pcap` | File is selected and path displayed |
| 5 | Click "Load ARXML Configuration" button | ARXML file selection dialog opens |
| 6 | Browse and select `single_signal_definition.arxml` | ARXML file loaded, signal definition preview shown |
| 7 | Verify signal name "SpeedSignal" appears in preview | Signal "SpeedSignal" is listed with type: uint16, unit: km/h |
| 8 | Click "Import" to start Traffic-to-Signal conversion | Progress bar shows conversion in progress |
| 9 | Wait for conversion to complete | "Import completed successfully" message displayed |
| 10 | Navigate to SIGNALS workspace | SIGNALS workspace opens |
| 11 | Verify "SpeedSignal" appears in signal list | Signal "SpeedSignal" is visible in SIGNALS tree |
| 12 | Right-click signal → Properties | Signal properties dialog opens |
| 13 | Verify signal properties: Unit = km/h, Type = uint16 | All properties match ARXML definition |
| 14 | Double-click signal to view values | Signal values are displayed (range: 0-120 km/h) |
| 15 | Verify signal sample count matches PCAP frame count | Sample count = expected frame count from PCAP |

## Notes
- Test PCAP file contains 1000 Ethernet frames with SOME/IP messages
- Signal "SpeedSignal" is located at PDU offset 0, length 16 bits
- Expected signal value range: 0-120 km/h
- Reference: IPEmotion User Manual Chapter 16 (Ethernet Interfaces)
- Reference: IPEmotion User Manual Chapter 21 (DATA MANAGER)
- KD Item: IM-44385

## Priority
High

## Coverage
- [x] Positive Testing
- [ ] Negative Testing
- [ ] Performance Testing
- [x] Functional Testing
