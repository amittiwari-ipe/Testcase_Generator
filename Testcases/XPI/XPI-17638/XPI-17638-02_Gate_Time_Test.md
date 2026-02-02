# XPI-17638-02 - Gate Time Test for Period Duration Measurement

## Description
Testing the gate time functionality during period duration measurement, including timeout behavior when signal is disconnected and reconnected.

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
| **Test with Gate Time 2s** | | |
| Display | | 542xxxxx_1 shows about 10ms<br>Status channel LED is green, LED on device is off |
| Disconnect the input cable | | |
| Wait 2s | | 542xxxxx_1 shows NoValue<br>Status channel LED is red, LED on device is magenta<br>WARNING 542xxxxx_1 Status detected: Input signal timeout |
| Reconnect the input cable | | 542xxxxx_1 shows about 10ms<br>Status channel LED is green, LED on device is off<br>INFORMATION 542xxxxx_1 Status reset: Input signal timeout |
| Stop | | |
| **Test with Gate Time 5s** | | |
| 542xxxxx_1 → Tab Input Signal → Gate time → 5s | | |
| Reset | | |
| Display | | 542xxxxx_1 shows about 10ms<br>Status channel LED is green, LED on device is off |
| Disconnect the input cable | | |
| Wait 5s | | 542xxxxx_1 shows NoValue<br>Status channel LED is red, LED on device is magenta<br>WARNING 542xxxxx_1 Status detected: Input signal timeout |
| Reconnect the input cable | | 542xxxxx_1 shows about 10ms<br>Status channel LED is green, LED on device is off<br>INFORMATION 542xxxxx_1 Status reset: Input signal timeout |
| Stop | | |
| **Test with Gate Time 10s** | | |
| 542xxxxx_1 → Tab Input Signal → Gate time → 10s | | |
| Reset | | |
| Display | | 542xxxxx_1 shows about 10ms<br>Status channel LED is green, LED on device is off |
| Disconnect the input cable | | |
| Wait 10s | | 542xxxxx_1 shows NoValue<br>Status channel LED is red, LED on device is magenta<br>WARNING 542xxxxx_1 Status detected: Input signal timeout |
| Reconnect the input cable | | 542xxxxx_1 shows about 10ms<br>Status channel LED is green, LED on device is off<br>INFORMATION 542xxxxx_1 Status reset: Input signal timeout |
| Stop | | |
| **Test with Gate Time 0.5s** | | |
| 542xxxxx_1 → Tab Input Signal → Gate time → 0.5s | | |
| Reset | | |
| Display | | 542xxxxx_1 shows about 10ms<br>Status channel LED is green, LED on device is off |
| Disconnect the input cable | | |
| Wait 0.5s | | 542xxxxx_1 shows NoValue<br>Status channel LED is red, LED on device is magenta<br>WARNING 542xxxxx_1 Status detected: Input signal timeout |
| Reconnect the input cable | | 542xxxxx_1 shows about 10ms<br>Status channel LED is green, LED on device is off<br>INFORMATION 542xxxxx_1 Status reset: Input signal timeout |
| Stop | | |

## Notes
- Wiring of input according to MCNT3_4-259 - HW-IF: Kanal-Steckverbinder-Typ 1
- Pin 2 and Pin 3 must be short-circuited
- Test different gate time values (0.5s, 2s, 5s, 10s) to verify timeout mechanism
- Timeout should trigger after gate time expires without valid signal
- Connection restoration should automatically resume measurement
- Status indicators: Channel LED (green/red), Device LED (off/magenta)
- Expected messages: WARNING for timeout detection, INFORMATION for timeout reset

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
- Cover Positive test cases (normal signal connection with various gate times)
- Cover Negative test cases (timeout scenarios with disconnected signal)
- Cover Functional test cases (gate time accuracy, timeout detection, recovery behavior)
- Verify status indicators and error messaging
