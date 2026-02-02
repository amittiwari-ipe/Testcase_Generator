# TC_003 - PCAP Import with Complex PDU Structure

## Description
Verify that IPEmotion can extract signals from a complex PDU structure containing nested data types, arrays, and different byte orders using ARXML definitions.

## Pre-Condition

### Software Setup:

#### Windows
- IPEmotion 2024 R2 or later installed
- Traffic-to-Signal converter license activated
- Test PCAP file: `eth_traffic_complex_pdu.pcap` (available in test data folder)
- ARXML file: `complex_pdu_definition.arxml` (contains complex data structures)
- Create test folder: `C:\TestData\IM-44385\TC_003\`
- Copy PCAP and ARXML files to test folder

#### Linux
- IPEmotion installed via Docker or native installation
- Traffic-to-Signal converter license activated
- Test PCAP file: `eth_traffic_complex_pdu.pcap`
- ARXML file: `complex_pdu_definition.arxml`
- Create test folder: `/home/testuser/TestData/IM-44385/TC_003/`
- Ensure read/write permissions on test folder

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| 1 | Launch IPEmotion application | IPEmotion opens successfully |
| 2 | Navigate to DATA MANAGER workspace | DATA MANAGER workspace is displayed |
| 3 | Click Import → Traffic Files → PCAP | PCAP import dialog opens |
| 4 | Browse and select `eth_traffic_complex_pdu.pcap` | File is selected and path displayed |
| 5 | Click "Load ARXML Configuration" button | ARXML file selection dialog opens |
| 6 | Browse and select `complex_pdu_definition.arxml` | ARXML file loaded successfully |
| 7 | Verify signal preview shows: VehicleSpeed, WheelSpeed[4], EngineData.RPM, EngineData.Torque, StatusFlags | Complex structure displayed with nested elements |
| 8 | Expand "WheelSpeed" array signal | Shows 4 elements: WheelSpeed[0], WheelSpeed[1], WheelSpeed[2], WheelSpeed[3] |
| 9 | Expand "EngineData" structure | Shows nested signals: EngineData.RPM, EngineData.Torque, EngineData.Temp |
| 10 | Select all signals for extraction | All checkboxes checked including array elements and nested signals |
| 11 | Verify byte order configuration: VehicleSpeed=Big-endian, WheelSpeed=Little-endian, EngineData=Mixed | Byte order indicators shown correctly for each signal group |
| 12 | Click "Import" to start conversion | Progress bar shows conversion in progress |
| 13 | Wait for conversion to complete | "Import completed successfully" message, shows "9 signals extracted" (1+4+3+1) |
| 14 | Navigate to SIGNALS workspace | SIGNALS workspace opens |
| 15 | Verify signal hierarchy in tree: VehicleSpeed, WheelSpeed folder with [0]-[3], EngineData folder with RPM/Torque/Temp | Signal tree shows hierarchical structure correctly |
| 16 | Select WheelSpeed[0] → View values | Values displayed, range: 0-100 km/h |
| 17 | Select WheelSpeed[3] → View values | Values displayed, range: 0-100 km/h |
| 18 | Compare WheelSpeed[0] vs WheelSpeed[3] for sample #100 | Values are different (expected: front vs rear wheel speeds) |
| 19 | Select EngineData.RPM → View Properties | Unit: rpm, Type: uint16, Byte order: Big-endian |
| 20 | Select EngineData.Torque → View Properties | Unit: Nm, Type: int16, Byte order: Little-endian, Scale: 0.1 |
| 21 | Verify StatusFlags signal (bitfield) | Individual bits displayed: bit0=EngineRunning, bit1=CruiseActive, etc. |
| 22 | Create VIEW chart with VehicleSpeed and all 4 WheelSpeed signals | Chart displays 5 curves with different colors |
| 23 | Verify array signal values correlate logically | Front wheels (0,1) show similar values, rear wheels (2,3) show similar values |
| 24 | Export one signal to CSV and verify data integrity | CSV file created, values match display, timestamps correct |

## Notes
- Test PCAP file contains 500 Ethernet frames with complex SOME/IP PDU
- PDU structure includes:
  - Simple scalar: VehicleSpeed (uint16, Big-endian)
  - Array: WheelSpeed[4] (uint16, Little-endian)
  - Nested struct: EngineData { RPM (uint16, BE), Torque (int16, LE, scale 0.1), Temp (int8) }
  - Bitfield: StatusFlags (uint8, 8 boolean flags)
- Total PDU size: 18 bytes
- Mixed byte order tests correct parsing implementation
- Reference: IPEmotion User Manual Chapter 16.3.4 (Complex SOME/IP structures)
- Reference: IPEmotion User Manual Chapter 13 (SIGNALS workspace)
- Reference: ARXML specification for complex data types
- KD Item: IM-44385

## Priority
High

## Coverage
- [x] Positive Testing
- [ ] Negative Testing
- [ ] Performance Testing
- [x] Functional Testing
