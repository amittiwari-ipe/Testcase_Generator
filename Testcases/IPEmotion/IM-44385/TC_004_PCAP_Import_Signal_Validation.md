# TC_004 - PCAP Import Signal Value Validation

## Description
Verify that signal values extracted from PCAP file match expected values by comparing with known reference data, validating data accuracy, scaling, and offset calculations.

## Pre-Condition

### Software Setup:

#### Windows
- IPEmotion 2024 R2 or later installed
- Traffic-to-Signal converter license activated
- Test PCAP file: `eth_traffic_validation.pcap` (available in test data folder)
- ARXML file: `validation_signal_definition.arxml` (contains signals with scaling and offset)
- Reference data file: `expected_values.csv` (contains expected signal values for validation)
- Create test folder: `C:\TestData\IM-44385\TC_004\`
- Copy all test files to test folder

#### Linux
- IPEmotion installed via Docker or native installation
- Traffic-to-Signal converter license activated
- Test PCAP file: `eth_traffic_validation.pcap`
- ARXML file: `validation_signal_definition.arxml`
- Reference data file: `expected_values.csv`
- Create test folder: `/home/testuser/TestData/IM-44385/TC_004/`
- Ensure read/write permissions on test folder

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| 1 | Launch IPEmotion application | IPEmotion opens successfully |
| 2 | Navigate to DATA MANAGER workspace | DATA MANAGER workspace is displayed |
| 3 | Click Import → Traffic Files → PCAP | PCAP import dialog opens |
| 4 | Browse and select `eth_traffic_validation.pcap` | File is selected (contains 100 frames with known values) |
| 5 | Click "Load ARXML Configuration" button | ARXML file selection dialog opens |
| 6 | Browse and select `validation_signal_definition.arxml` | ARXML loaded with 3 signals: RawSignal, ScaledSignal, OffsetSignal |
| 7 | Verify signal definitions in preview:<br>- RawSignal: uint16, no scaling<br>- ScaledSignal: uint16, scale=0.01<br>- OffsetSignal: uint16, scale=0.1, offset=-100 | All signal parameters displayed correctly |
| 8 | Click "Import" to start conversion | Progress bar shows conversion in progress |
| 9 | Wait for conversion to complete | "Import completed successfully", 3 signals extracted, 100 samples each |
| 10 | Navigate to SIGNALS workspace | SIGNALS workspace opens |
| 11 | Select RawSignal → View data table | Data table opens showing all 100 samples |
| 12 | Check sample #1 value: Expected raw value = 1000 | Sample #1: RawSignal = 1000 (exact match) |
| 13 | Check sample #50 value: Expected raw value = 5000 | Sample #50: RawSignal = 5000 (exact match) |
| 14 | Check sample #100 value: Expected raw value = 10000 | Sample #100: RawSignal = 10000 (exact match) |
| 15 | Select ScaledSignal → View data table | Data table opens showing scaled values |
| 16 | Check sample #1 scaled value: Raw=1000, Expected=10.00 (1000 * 0.01) | Sample #1: ScaledSignal = 10.00 (correct scaling) |
| 17 | Check sample #50 scaled value: Raw=5000, Expected=50.00 (5000 * 0.01) | Sample #50: ScaledSignal = 50.00 (correct scaling) |
| 18 | Check sample #100 scaled value: Raw=10000, Expected=100.00 (10000 * 0.01) | Sample #100: ScaledSignal = 100.00 (correct scaling) |
| 19 | Select OffsetSignal → View data table | Data table opens showing scaled+offset values |
| 20 | Check sample #1 offset value: Raw=1000, Expected=0.0 (1000*0.1-100) | Sample #1: OffsetSignal = 0.0 (correct scale+offset) |
| 21 | Check sample #50 offset value: Raw=1500, Expected=50.0 (1500*0.1-100) | Sample #50: OffsetSignal = 50.0 (correct scale+offset) |
| 22 | Check sample #100 offset value: Raw=2000, Expected=100.0 (2000*0.1-100) | Sample #100: OffsetSignal = 100.0 (correct scale+offset) |
| 23 | Export all signals to CSV | CSV export dialog opens |
| 24 | Save as `extracted_values.csv` | File saved successfully |
| 25 | Compare `extracted_values.csv` with `expected_values.csv` using diff tool | Files are identical (or differences within tolerance of 0.01%) |
| 26 | Verify timestamp accuracy: Sample #1 should be at t=0.0s, Sample #100 at t=0.99s (10ms intervals) | Timestamps match expected values exactly |
| 27 | Select RawSignal → Statistics view | Statistics panel shows: Min=1000, Max=10000, Avg=5500, Count=100 |
| 28 | Verify statistics match expected calculations | All statistical values correct (tolerance ±1 for floating point) |

## Notes
- Test PCAP file contains synthetic data with known values for validation
- Frame timing: 10ms intervals (100 frames = 1 second total duration)
- RawSignal increments by 100 each frame (1000, 1100, 1200, ..., 10000)
- ScaledSignal = RawSignal * 0.01
- OffsetSignal = RawSignal * 0.1 - 100
- Expected values calculated and stored in `expected_values.csv`
- Validation tolerance: ±0.01% for floating point comparisons
- This test validates correct implementation of:
  - Byte order conversion
  - Scaling factor application
  - Offset calculation
  - Timestamp extraction
  - Data integrity through entire pipeline
- Reference: IPEmotion User Manual Chapter 21.5 (Data Import Validation)
- Reference: ARXML specification for signal physical representation
- KD Item: IM-44385

## Priority
High

## Coverage
- [x] Positive Testing
- [ ] Negative Testing
- [ ] Performance Testing
- [x] Functional Testing
