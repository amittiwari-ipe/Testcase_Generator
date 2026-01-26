# TD4-16395 - RT License Flags Support for 2026

## Description
As PO of IPEmotionRT I expect that new license flags for RT licenses are supported in 2026:
- **IPEcloud2** → subscription → definition for future use, but not used in 26 R1 → will set the logger in R1 always to error status if set
- **CMP streaming** → stream CMP via ETHERNET CMP traffic → data format CMP_TRAFFIC with direction output is checked
- **WiFi, Bluetooth** → to prevent wireless connections in general → error status for active AP or Bluetooth if not set
- **IPEcal Pay for Calibration** → use with IPEmotion CE → available via COM interface as handled there

## Pre-Condition

### Required Licenses:
**IPEmotionRT Logger:**
- Basic license
- WLAN + Communication package
- WLAN + Communication + Wireless access package

### Hardware Setup:

| IPEmotion | IPEmotion RT |
|-----------|--------------|
| Connect logger to PC and Power supply | Connect logger to PC and Power supply |
| Connect Wifi antenna to logger | Connect Wifi antenna to logger |

### Software Setup:

| IPEmotion | IPEmotion RT |
|-----------|--------------|
| Start RT.UI → Signals → Detect | Start RT.UI → Signals → Detect |
| Initialize an empty configuration to the Logger | Initialize an empty configuration to the Logger |
| About → Licensing → assign the Basic license to the Logger → OK | About → Licensing → assign the Basic license to the Logger → OK |
| Reboot the Logger | Reboot the Logger |

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| 1 | when logger is ON → RT.UI → Message window | Following errors are available:<br><br>**Type:** Error<br>**Source:** License<br>**Message:** License insufficient<br><br>**Type:** Error<br>**Source:** License<br>**Message:** License missing: Wireless access<br><br>**Type:** Error<br>**Source:** License<br>**Message:** License insufficient |
| 2 | Status window | Following errors are available:<br><br>**Type:** Error<br>**Source:** IPElog2<br>**Message:** License insufficient |
| 3 | Open any browser and navigate to http://192.168.236.1/ → Syslog | Following error messages should be available:<br><br>License: License missing: Wireless access<br>License: License insufficient<br>Datalogger Init failed, can't start measurement |
| 4 | Use now any mobile device or a laptop → go to WiFi setup and check available networks | SSID with connected logger type should not available |
| 5 | RT.UI → Signals → Logger → Tab Access point → Active: unchecked | |
| 6 | Initialize | |
| 7 | Message window | There are no error messages regarding insufficient licenses |
| 8 | RT.UI → About → Licensing → assign the license with WLAN + Communication package → Close | |
| 9 | Reboot the Logger | |
| 10 | File → Open → TD4-16392.rwf → Open<br><br>**Path:**<br>M:\Testmanagement\DUS\01_Projekte\25_IPEmotion_RT\03_Testdaten\V16.00.00\TD4-16395 | |
| 11 | Signals → Change the logger type and front number if required | |
| 12 | Communication → Wifi → Wifi-1 → Change the Wifi credentials if required | |
| 13 | Initialize | |
| 14 | Message window | Following errors are available:<br><br>**Type:** Error<br>**Source:** License<br>**Message:** License insufficient<br><br>**Type:** Error<br>**Source:** License<br>**Message:** License missing: Wireless access<br><br>**Type:** Error<br>**Source:** License<br>**Message:** License insufficient |
| 15 | Status window | Following errors are available:<br><br>**Type:** Error<br>**Source:** IPElog2<br>**Message:** License insufficient |
| 16 | Browser → Check Syslog message | Following error messages should be available:<br><br>License: License missing: Wireless access<br>License: License insufficient<br>Datalogger Init failed, can't start measurement |
| 17 | Laptop → go to WiFi setup and check available networks | SSID with connected logger type should not available |
| 18 | RT.UI → Signals → Logger → Tab Access point → Active: unchecked | |
| 19 | Initialize | |
| 20 | Message window | There are no error messages regarding insufficient licenses |
| 21 | wait until Wifi connection is established on the logger | |
| 22 | Browser → Check syslog messages | You will see "Start data transfer"<br>and "Data transfer finished" |
| 23 | RT.UI → About → Licensing → assign the license with WLAN + Communication + Wireless access package → Close | |
| 24 | Reboot the Logger | |
| 25 | RT.UI → Signals → Logger → Tab Access point → Active: checked | |
| 26 | Initialize | |
| 27 | Message window | There are no error messages regarding insufficient licenses |
| 28 | wait until Wifi connection is established on the logger | |
| 29 | Browser → Check syslog messages | You will see "Start data transfer"<br>and "Data transfer finished" |
| 30 | Disconnect logger from PC | |
| 31 | Laptop → go to WiFi setup and check available networks | SSID with connected logger type should be available |
| 32 | Connect to the SSID with connected logger type | |
| 33 | RT.UI → Detect | Logger should be detected |
| 34 | Signals → Initialize empty config to logger | |

## Notes
- Test data file: TD4-16392.rwf
- Location: M:\Testmanagement\DUS\01_Projekte\25_IPEmotion_RT\03_Testdaten\V16.00.00\TD4-16395
- Syslog access: http://192.168.236.1/

## Priority
High

## Coverage
- [x] Positive Testing
- [x] Negative Testing
- [ ] Performance Testing
- [x] Functional Testing
