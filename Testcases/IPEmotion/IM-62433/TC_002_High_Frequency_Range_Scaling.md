# TC_002 - Frequency to Flow Rate with High Frequency Range

## Description
Verify frequency-to-flow-rate scaling configuration with a higher frequency range (10 kHz) and verify calculation accuracy across the range.

## Pre-Condition

### Software Setup:

#### Windows
- IPEmotion 2024 R2 or later installed
- X-PlugIn license activated
- M-CNT3 4 hardware module connected or simulation mode
- Function generator capable of 0-10 kHz output (for hardware testing)
- Create test folder: `C:\TestData\IM-62433\TC_002\`
- Document scaling parameters: SensorMax = 10000 Hz, PhysMax = 500 l/min

#### Linux
- IPEmotion installed via Docker or native installation
- X-PlugIn license activated
- M-CNT3 4 hardware module connected or simulation mode
- Function generator capable of 0-10 kHz output
- Create test folder: `/home/testuser/TestData/IM-62433/TC_002/`
- Ensure read/write permissions on test folder

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| 1 | Launch IPEmotion application | IPEmotion opens successfully |
| 2 | Navigate to GInterface Configuration workspace | GInterface workspace is displayed |
| 3 | Right-click on M-CNT3 4 device → Add Channel | Channel creation dialog opens |
| 4 | Enter channel name: "FlowSensor_HighFreq" | Channel name set |
| 5 | Select "Frequency" from SensorMode dropdown | SensorMode set to "Frequency" |
| 6 | Verify scaling configuration section is visible | Frequency-to-flow-rate fields displayed |
| 7 | Enter Maximum Frequency (SensorMax): 10000 Hz | Value "10000" entered |
| 8 | Select physical unit: "l/min" from dropdown | Unit "l/min" selected |
| 9 | Enter Maximum Flow Rate (PhysMax): 500 l/min | Value "500" entered |
| 10 | Verify minimum values: SensorMin = 0 Hz, PhysMin = 0 l/min | Default minimums displayed automatically |
| 11 | Click "OK" to save configuration | Configuration saved, channel created |
| 12 | Navigate to SIGNALS workspace | SIGNALS workspace opens |
| 13 | Verify "FlowSensor_HighFreq" signal appears in signal tree | Signal visible with unit "l/min" |
| 14 | Right-click signal → Properties | Signal properties dialog opens |
| 15 | Verify signal properties:<br>- Unit: l/min<br>- Scaling: Frequency to Flow Rate<br>- Max: 500 l/min | Properties match configuration |
| 16 | Close properties dialog | Dialog closes |
| 17 | Navigate to ACQUISITION workspace | ACQUISITION workspace opens |
| 18 | Start measurement acquisition | Acquisition starts, status shows "Running" |
| 19 | Set frequency input to 0 Hz (if using hardware) | Frequency generator set to 0 Hz |
| 20 | Verify signal displays 0.0 l/min | Flow rate = 0.0 l/min (correct) |
| 21 | Set frequency input to 2500 Hz | Frequency generator set to 2500 Hz |
| 22 | Verify signal displays 125.0 l/min | Flow rate = 125.0 l/min (calculation: 2500/10000*500) |
| 23 | Set frequency input to 5000 Hz | Frequency generator set to 5000 Hz |
| 24 | Verify signal displays 250.0 l/min | Flow rate = 250.0 l/min (calculation: 5000/10000*500) |
| 25 | Set frequency input to 7500 Hz | Frequency generator set to 7500 Hz |
| 26 | Verify signal displays 375.0 l/min | Flow rate = 375.0 l/min (calculation: 7500/10000*500) |
| 27 | Set frequency input to 10000 Hz (maximum) | Frequency generator set to 10000 Hz |
| 28 | Verify signal displays 500.0 l/min | Flow rate = 500.0 l/min (at maximum) |
| 29 | Stop measurement acquisition | Acquisition stops successfully |
| 30 | Verify all displayed values matched expected calculations (±0.5% tolerance) | All values within acceptable tolerance |

## Notes
- This test validates higher frequency range (10 kHz) with proportionally higher flow rate
- Scaling formula: Flow Rate = (Frequency / 10000) * 500 l/min
- Expected values at test points:
  - 0 Hz → 0 l/min
  - 2500 Hz → 125 l/min
  - 5000 Hz → 250 l/min
  - 7500 Hz → 375 l/min
  - 10000 Hz → 500 l/min
- Tolerance: ±0.5% or ±2.5 l/min (whichever is greater)
- For software-only testing without hardware, use simulation mode with configurable frequency input
- Reference: IPEmotion User Manual Chapter 17 (ACQUISITION workspace)
- Reference: XPI M-CNT3 specifications for maximum frequency support
- KD Item: IM-62433

## Priority
High

## Coverage
- [x] Positive Testing
- [ ] Negative Testing
- [ ] Performance Testing
- [x] Functional Testing
