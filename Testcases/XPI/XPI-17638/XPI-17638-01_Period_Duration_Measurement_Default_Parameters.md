# XPI-17638-01 - Period Duration Measurement with Default Parameters

## Description
Testing the period duration measurement functionality with default parameters for M-CNT3 4 device, including corner cases according to MCNT3_4-334 - SENSOR_MODE: Periodendauer.

## Pre-Condition

| IPEmotion PC | IPEmotion RT |
|--------------|--------------|
| Power supply between 9,3V and 36V | Power supply between 9,3V and 36V |
| Connect any CAN Interface to PC via USB | Connect any Logger |
| Connect M-CNT3 4 device with CAN interface and power supply via M3-CAN/PWR term cable 623-500 | Connect M-CNT3 4 to M-CAN port via LOG M3-CAN Term Kabel cable 623-502 or to CAN port and power supply via M3-CAN/PWR term 623-500 |
| Connect input cable SIM-CNT-IN BANANA (600-402 or 600-561) to 1. channel | Connect input cable SIM-CNT-IN BANANA (600-402 or 600-561) to 1. channel |
| Pin 2 and pin 3 have to be short-circuited | Pin 2 and pin 3 have to be short-circuited |

**Frequency Generator:**
- Function: Pulse
- Frequency: 100Hz
- Output menu → Load impedance → High Z
- Amplitude → High Level → 5V → Low Level 0V

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| Start IPEmotion<br>Activated plugins: IPETRONIK X | Start IPEmotionRT | |
| Detect | Detect and Synchronize | |
| Reset | | |
| 542xxxxx_1 → Tab Scaling → Sensor mode → Period duration | | |
| 542xxxxx_1 → Tab Filter → Hardware filter → Off | | |
| 542xxxxx_1 → Tab Input Signal →<br>DC compensation → Uncheck →<br>Trigger → Signal A → Rising edge →<br>Gate time → 2s<br>Threshold on → 3V<br>Threshold off → 1V | | |
| Frequency generator:<br>Function: Pulse<br>Frequency: 100Hz<br>Output menu → Load impedance → High Z<br>Amplitude → High Level → 5V → Low Level 0V | | |
| Display | | 542xxxxx_1 shows about 10ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Frequency: 1Hz | | 542xxxxx_1 shows about 1000ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Frequency: 10Hz | | 542xxxxx_1 shows about 100ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Frequency: 50Hz | | 542xxxxx_1 shows about 20ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Frequency: 100Hz | | 542xxxxx_1 shows about 10ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Frequency: 500Hz | | 542xxxxx_1 shows about 2ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Frequency: 1kHz | | 542xxxxx_1 shows about 1ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Frequency: 5kHz | | 542xxxxx_1 shows about 0.2ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Frequency: 10kHz | | 542xxxxx_1 shows about 0.1ms<br>Status channel LED is green, LED on device is off |
| **Corner case testing according to MCNT3_4-334** | | |
| Frequency generator:<br>Minimum frequency per specification | | 542xxxxx_1 shows correct period duration<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Maximum frequency per specification | | 542xxxxx_1 shows correct period duration<br>Status channel LED is green, LED on device is off |
| Stop | | |

## Notes
- Individual parameters can be tested in parallel with all channels
- Wiring of input according to MCNT3_4-259 - HW-IF: Kanal-Steckverbinder-Typ 1
- Pin 2 and Pin 3 must be short-circuited
- Corner cases should be tested according to MCNT3_4-334 - SENSOR_MODE: Periodendauer
- Start condition after reset: Signal A = Rising edge, Gate Time = 2s
- Expected period duration = 1 / Frequency (e.g., 100Hz → 10ms)

## Priority
High

## Coverage
- [x] Positive Testing
- [x] Negative Testing
- [ ] Performance Testing
- [x] Functional Testing

---

**Priority**: High

**Coverage Expectations**:
- Cover Positive test cases (normal frequency range)
- Cover Negative test cases (corner cases - min/max frequencies)
- Cover Functional test cases (period duration measurement accuracy)
- Verify multi-channel parallel operation
