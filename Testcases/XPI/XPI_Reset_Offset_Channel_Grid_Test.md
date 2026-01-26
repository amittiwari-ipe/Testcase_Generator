# XPI_Reset_Offset_Channel_Grid_Test

## Description
Reset offset value, values in the channel grid

## Pre-Condition

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

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| 1 | Start IPEmotion<br>Activated Plugin: IPETRONIK X | Start IPEmotionRT |
| 2 | Add columns "Offset value" and "Reference value" | |
| 3 | Detect | Detect and Synchronize |
| 4 | Reset | Reset devices |
| 5 | X-1 → Adjust → Offset | Offset adjust dialog opens<br>Result is OK for every channel |
| 6 | Select all channels → Reference value → 10 | |
| 7 | Selection → All → Start | Offset adjust starts...<br>Result is OK for every channel |
| 8 | Close Offset adjust dialog | |
| 9 | Display | All channels show about 10 °C<br><br>**Reference value in column:**<br>All channels show about 10 °C<br><br>**Offset value in column:**<br>All channels show about -5 °C |
| 10 | Stop | |
| 11 | 540xxxxx_1 → Context menu → Function → Reset channel adjustment | **Offset value in column:**<br><br>540xxxxx_1: 0<br><br>All other channels show about -5 °C<br><br>**Message window:**<br>INFORMATION X-1<br>The offset reset was successful.<br><br>INFORMATION 540xxxxx_1<br>The offset reset was successful. |
| 12 | 540xxxxx → Function → Reset channel adjustment | **Offset value in column:**<br><br>All channels show about 0 °C<br><br>**Message window:**<br>INFORMATION X-1 The offset reset was successful.<br>INFORMATION 540xxxxx_1 The offset reset was successful.<br>.<br>.<br>.<br>INFORMATION 540xxxxx_16 The offset reset was successful. |
| 13 | 540xxxxx → Function → Adjust all channels | **Offset value:**<br><br>All channels show about -5 °C<br><br>**Reference value in column:**<br><br>All channels show about 10 °C |
| 14 | Display | All channels show about 10 °C |
| 15 | Stop | |
| 16 | Reset | Reset devices | Offset value and Reference value is set to zero for all channels |

## Notes
- M-THERMO3 16 device used for testing
- Term cable references: 623-500 (IPEmotion), 623-501 (IPEmotion RT)
- Digistant value: 15 °C
- Test validates offset adjustment and reset functionality

## Priority
Medium

## Coverage
- [x] Positive Testing
- [ ] Negative Testing
- [ ] Performance Testing
- [x] Functional Testing
