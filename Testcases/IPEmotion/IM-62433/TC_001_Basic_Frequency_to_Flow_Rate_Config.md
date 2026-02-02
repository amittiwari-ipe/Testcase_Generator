# TC_001 - Basic Frequency to Flow Rate Configuration with Default Units

## Description
Verify that users can configure basic frequency-to-flow-rate scaling in Channel Wizard for M-CNT3 4 channel with default minimum values and l/min unit.

## Pre-Condition

### Software Setup:

#### Windows
- IPEmotion 2024 R2 or later installed
- X-PlugIn license activated
- M-CNT3 4 hardware module connected (or simulation mode available)
- Create test folder: `C:\TestData\IM-62433\TC_001\`
- Document scaling parameters: SensorMax = 1000 Hz, PhysMax = 75 l/min

#### Linux
- IPEmotion installed via Docker or native installation
- X-PlugIn license activated
- M-CNT3 4 hardware module connected (or simulation mode available)
- Create test folder: `/home/testuser/TestData/IM-62433/TC_001/`
- Ensure read/write permissions on test folder

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| 1 | Launch IPEmotion application | IPEmotion opens successfully |
| 2 | Navigate to GInterface Configuration workspace | GInterface workspace is displayed |
| 3 | Right-click on M-CNT3 4 device → Add Channel | Channel creation dialog opens |
| 4 | Select "Frequency" from SensorMode dropdown | SensorMode set to "Frequency" |
| 5 | Verify that scaling configuration section appears | Frequency-to-flow-rate scaling fields are visible |
| 6 | Verify default minimum values displayed:<br>- SensorMin: 0 Hz<br>- PhysMin: 0 l/min | Both minimum fields show "0" automatically |
| 7 | Click on "Maximum Frequency (SensorMax)" field | Field is active and ready for input |
| 8 | Enter value: 1000 | Value "1000" displayed in SensorMax field |
| 9 | Verify unit "Hz" is shown next to SensorMax field | Unit "Hz" displayed correctly |
| 10 | Click on "Physical Unit" dropdown | Dropdown list opens showing volume flow units |
| 11 | Verify "l/min" is available in the list | "l/min" is present in dropdown options |
| 12 | Select "l/min" from dropdown | "l/min" is selected and displayed |
| 13 | Click on "Maximum Flow Rate (PhysMax)" field | Field is active and ready for input |
| 14 | Enter value: 75 | Value "75" displayed in PhysMax field |
| 15 | Verify unit "l/min" is shown next to PhysMax field | Unit "l/min" displayed correctly |
| 16 | Review complete configuration:<br>- SensorMin: 0 Hz<br>- SensorMax: 1000 Hz<br>- PhysMin: 0 l/min<br>- PhysMax: 75 l/min | All values displayed correctly |
| 17 | Click "Apply" or "OK" to save configuration | Configuration saved successfully, dialog closes |
| 18 | Verify new channel appears in GInterface tree | Channel visible with configured name |
| 19 | Right-click channel → Properties | Channel properties dialog opens |
| 20 | Navigate to "Scaling" tab | Scaling configuration is displayed |
| 21 | Verify scaling type shows "Frequency to Flow Rate" | Scaling type correctly identified |
| 22 | Verify all parameters match entered values:<br>- SensorMax: 1000 Hz<br>- PhysMax: 75 l/min<br>- Unit: l/min | All parameters preserved correctly |
| 23 | Close properties dialog | Dialog closes |
| 24 | Save IPEmotion project as "TC_001_FreqToFlow.ipep" | Project saved successfully |

## Notes
- This test validates the basic configuration workflow for frequency-to-flow-rate scaling
- Default minimum values (0 Hz, 0 l/min) are automatically populated
- Scaling formula: Flow Rate = (Frequency / 1000) * 75 l/min
- At 500 Hz frequency input, expected output = 37.5 l/min
- At 1000 Hz frequency input, expected output = 75 l/min
- Reference: IPEmotion User Manual Chapter 14 (GInterface Configuration)
- Reference: IPEmotion User Manual Chapter 15 (X-PlugIn Option)
- Reference: XPI Documentation - M-CNT3 Counter Module
- KD Item: IM-62433

## Priority
High

## Coverage
- [x] Positive Testing
- [ ] Negative Testing
- [ ] Performance Testing
- [x] Functional Testing
