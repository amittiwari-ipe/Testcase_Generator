# XPI-17638-03 - Trigger Edge Selection Test for Period Duration Measurement

## Description
Testing the trigger edge selection functionality (rising/falling edge) during period duration measurement to verify that edge selection affects the measured period duration correctly.

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
- Duty: 50%
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
| Frequency generator:<br>Function: Pulse<br>Frequency: 100Hz<br>Duty: 50%<br>Output menu → Load impedance → High Z<br>Amplitude → High Level → 5V → Low Level 0V | | |
| Display | | 542xxxxx_1 shows about 10ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Duty: 30% | | 542xxxxx_1 shows about 10ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Duty: 50% | | 542xxxxx_1 shows about 10ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Duty: 70% | | 542xxxxx_1 shows about 10ms<br>Status channel LED is green, LED on device is off |
| Stop | | |
| 542xxxxx_1 → Tab Input Signal →<br>Trigger → Signal A → Falling edge | | |
| Reset | | |
| Display | | 542xxxxx_1 shows about 10ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Duty: 30% | | 542xxxxx_1 shows about 7ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Duty: 50% | | 542xxxxx_1 shows about 10ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Duty: 70% | | 542xxxxx_1 shows about 13ms<br>Status channel LED is green, LED on device is off |
| Stop | | |
| **Test with 1kHz Frequency** | | |
| 542xxxxx_1 → Tab Input Signal →<br>Trigger → Signal A → Rising edge | | |
| Reset | | |
| Frequency generator:<br>Frequency: 1kHz<br>Duty: 50% | | |
| Display | | 542xxxxx_1 shows about 1ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Duty: 25% | | 542xxxxx_1 shows about 1ms<br>Status channel LED is green, LED on device is off |
| Stop | | |
| 542xxxxx_1 → Tab Input Signal →<br>Trigger → Signal A → Falling edge | | |
| Reset | | |
| Display | | 542xxxxx_1 shows about 0.75ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Duty: 50% | | 542xxxxx_1 shows about 1ms<br>Status channel LED is green, LED on device is off |
| Stop | | |
| **Test with 10Hz Frequency** | | |
| 542xxxxx_1 → Tab Input Signal →<br>Trigger → Signal A → Rising edge | | |
| Reset | | |
| Frequency generator:<br>Frequency: 10Hz<br>Duty: 50% | | |
| Display | | 542xxxxx_1 shows about 100ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Duty: 75% | | 542xxxxx_1 shows about 100ms<br>Status channel LED is green, LED on device is off |
| Stop | | |
| 542xxxxx_1 → Tab Input Signal →<br>Trigger → Signal A → Falling edge | | |
| Reset | | |
| Display | | 542xxxxx_1 shows about 125ms<br>Status channel LED is green, LED on device is off |
| Frequency generator:<br>Duty: 50% | | 542xxxxx_1 shows about 100ms<br>Status channel LED is green, LED on device is off |
| Stop | | |

## Notes
- Wiring of input according to MCNT3_4-259 - HW-IF: Kanal-Steckverbinder-Typ 1
- Pin 2 and Pin 3 must be short-circuited
- Rising edge trigger measures time between consecutive rising edges (constant period regardless of duty cycle)
- Falling edge trigger measures time between consecutive falling edges (period varies with duty cycle changes)
- Status indicators: Channel LED (green), Device LED (off after measurement mode signaling)
- Individual parameters can be tested in parallel with all channels
- Test demonstrates edge selection impact on period duration measurement
- Period duration calculation:
  - Rising edge: Always 1/Frequency
  - Falling edge: Varies with duty cycle when duty ≠ 50%

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
- Cover Positive test cases (both rising and falling edge configurations)
- Cover Functional test cases (edge selection impact on period duration measurement)
- Verify measurement stability with consistent edge detection
- Validate measurement variation when duty cycle affects edge-to-edge timing
