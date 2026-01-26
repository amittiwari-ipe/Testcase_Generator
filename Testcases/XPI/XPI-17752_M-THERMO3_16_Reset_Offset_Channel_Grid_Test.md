# XPI-17752 - M-THERMO3 16: Reset Offset Value and Channel Grid Values

## Description
Reset offset value, values in the channel grid for M-THERMO3 16 device. Validate that offset adjustments can be performed, displayed correctly in channel grid columns, and reset individually or for all channels.

## Pre-Condition

### Required Licenses:
- IPEmotion
- IPEmotion RT Logger
- X-Plugin license

### Hardware Setup:

| IPEmotion | IPEmotion RT |
|-----------|--------------|
| Connect IPEcanFD or IPEcanPro FD to PC via USB | Connect logger to PC and start logger |
| Connect the M-THERMO3 16 to any CAN interface and to the power supplier via M3-CAN/PWR term cable 623-500 | Connect the M-THERMO3 16 to CAN1 port of logger and the power supplier via M3-CAN/PWR term cable 623-501 |
| Connect the thermocouple to all channels | Connect thermocouple to all channel |
| Set the digistant value to 15 °C | Set the digistant value to 15 °C |

### Software Setup:

| IPEmotion | IPEmotion RT |
|-----------|--------------|
| Activated Plugin: IPETRONIK X | |

### Software Version / Firmware:
- X-Plugin version: V02.24.00
- M-THERMO3 16 firmware version: [Latest]
- PC OS version: Windows 64-bit

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| Start IPEmotion<br>Activated Plugin: IPETRONIK X | Start IPEmotionRT | |
| Add columns "Offset value" and "Reference value" | | |
| Detect | Detect and Synchronize | |
| Reset | Reset devices | |
| X-1 → Adjust → Offset | | Offset adjust dialog opens<br>Result is OK for every channel |
| Select all channels → Reference value → 10 | | |
| Selection → All → Start | | Offset adjust starts...<br>Result is OK for every channel |
| Close Offset adjust dialog | | |
| Display | | All channels show about 10 °C<br><br>**Reference value in column:**<br>All channels show about 10 °C<br><br>**Offset value in column:**<br>All channels show about -5 °C |
| Stop | | |
| 540xxxxx_1 → Context menu → Function → Reset channel adjustment | | **Offset value in column:**<br><br>540xxxxx_1: 0<br><br>All other channels show about -5 °C<br><br>**Message window:**<br>INFORMATION X-1<br>The offset reset was successful.<br><br>INFORMATION 540xxxxx_1<br>The offset reset was successful. |
| 540xxxxx → Function → Reset channel adjustment | | **Offset value in column:**<br><br>All channels show about 0 °C<br><br>**Message window:**<br>INFORMATION X-1 The offset reset was successful.<br>INFORMATION 540xxxxx_1 The offset reset was successful.<br>.<br>.<br>.<br>INFORMATION 540xxxxx_16 The offset reset was successful. |
| 540xxxxx → Function → Adjust all channels | | **Offset value:**<br><br>All channels show about -5 °C<br><br>**Reference value in column:**<br><br>All channels show about 10 °C |
| Display | | All channels show about 10 °C |
| Stop | | |
| Reset | Reset devices | Offset value and Reference value is set to zero for all channels |

## Notes
- M-THERMO3 16 device used for testing (540xxxxx)
- Term cable references: 623-500 (IPEmotion), 623-501 (IPEmotion RT)
- Digistant value: 15 °C
- Reference temperature for offset: 10 °C
- Test validates offset adjustment and reset functionality for individual channels and all channels
- Verifies proper display in channel grid columns

## Priority
Prio 3 Should [50.0]

## Coverage
- [x] Positive Testing
- [x] Negative Testing
- [ ] Performance Testing
- [x] Functional Testing

## Test Metadata
- **Test Type:** Functional Test
- **Categories:** Testing CAN
- **Platform:** IPEmotion 64bit FW, IPEmotion RT
- **Area:** X-PI, FW
- **Feature:** Offset adjust
- **Hardware:** M-THERMO3 16, any CAN Interface
- **Automatable:** PC&RT
- **Test Object:** M-THERMO3 16
- **Release Creation:** X-PI V02.24.00
