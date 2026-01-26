# XPI-17015 - M-THERMO3 16 Offset Adjustment

## Description
Implement offset compensation for M-THERMO3 16 device:
- Enable offset compensation for M-THERMO 16
- Support relative measurement capability
- Compensate for accuracy losses during break detection with long, thin cables
- Feature should operate similarly to SENS devices (offset adjust dialog, function menu on channel/device/system nodes)
- Support triggering all or certain offset groups and resetting adjustments
- Automatic reset of current offset and reference value on parameter changes
- Only available for temperature channels (not for Cold Junction Temperature or Thermal Voltage in raw mode)

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
| Connect thermocouples to all channels | Connect thermocouples to all channels |
| Set reference temperature value (e.g., 15 °C) | Set reference temperature value (e.g., 15 °C) |

### Software Setup:

| IPEmotion | IPEmotion RT |
|-----------|--------------|
| Activated Plugin: IPETRONIK X | Start IPEmotionRT |
| Add columns "Offset value" and "Reference value" | Add columns "Offset value" and "Reference value" |

### Software Version / Firmware:
- X-Plugin version: [Latest version with offset adjustment support]
- M-THERMO3 16 firmware version: [Firmware supporting offset adjustment]
- PC OS version: [Windows/Linux version]

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| 1 | Start IPEmotion<br>Activated Plugin: IPETRONIK X | Start IPEmotionRT |
| 2 | Detect | Detect and Synchronize | M-THERMO3 16 device is detected successfully |
| 3 | Reset | Reset devices | All devices are reset successfully |
| 4 | M-THERMO3 16 (540xxxxx) → Context menu → Adjust → Offset | Offset adjust dialog opens<br>Result is OK for every channel<br>Dialog structure similar to SENS devices |
| 5 | Select all channels → Set Reference value → 20 °C | Reference value field accepts the value |
| 6 | Selection → All → Start | Offset adjust starts<br>Result is OK for every channel<br>Offset adjustment completes successfully |
| 7 | Close Offset adjust dialog | Dialog closes without errors |
| 8 | Verify Display | All temperature channels show approximately 20 °C<br><br>**Reference value column:**<br>All channels show 20 °C<br><br>**Offset value column:**<br>All channels show calculated offset (e.g., ~5 °C if actual was 15 °C) |
| 9 | 540xxxxx_1 → Context menu → Function → Reset channel adjustment | **Offset value column:**<br>540xxxxx_1: 0<br>All other channels retain their offset<br><br>**Message window:**<br>INFORMATION M-THERMO3 16<br>The offset reset was successful.<br>INFORMATION 540xxxxx_1<br>The offset reset was successful. |
| 10 | 540xxxxx → Function → Reset channel adjustment | **Offset value column:**<br>All channels show 0 °C<br><br>**Message window:**<br>INFORMATION M-THERMO3 16<br>The offset reset was successful.<br>INFORMATION 540xxxxx_1 ... 540xxxxx_16<br>The offset reset was successful for all channels. |
| 11 | 540xxxxx → Function → Adjust all channels<br>Reference value: 25 °C | **Offset value:**<br>All channels show new calculated offset<br><br>**Reference value column:**<br>All channels show 25 °C |
| 12 | Change physical range for 540xxxxx_1 (e.g., modify sensor range) | **Auto-reset verification:**<br>Offset value for 540xxxxx_1 is automatically reset to 0<br>Reference value is reset according to rules:<br>- If range contains 0: Reference = 0<br>- If range doesn't contain 0: Reference = (min + max) / 2 |
| 13 | Change SensorMode for 540xxxxx_2 | **Auto-reset verification:**<br>Offset value for 540xxxxx_2 is automatically reset to 0<br>Reference value is reset to default |
| 14 | Change Adjustment group for 540xxxxx_3 | **Auto-reset verification:**<br>Offset value for 540xxxxx_3 is automatically reset to 0<br>Reference value is reset to default |
| 15 | Manually change Reference value for 540xxxxx_4 | **Auto-reset verification:**<br>Latest offset value for 540xxxxx_4 is reset<br>New reference value is accepted |
| 16 | Try to set Reference value outside physical range | **Validation:**<br>System prevents setting reference value outside physical range<br>Error message displayed |
| 17 | 540xxxxx → Adjust → Offset<br>Create different adjustment groups | Multiple offset groups can be created<br>Each group can be triggered independently |
| 18 | Function menu → Trigger specific offset group | Only channels in selected group perform adjustment<br>Other channels remain unchanged |
| 19 | Stop measurement | |
| 20 | Save configuration with offset and reference values | Configuration saves successfully |
| 21 | Close and reopen configuration | Offset and reference values are persisted correctly |
| 22 | Reset | Reset devices | Offset value and Reference value are set to zero for all channels |
| 23 | **Test with older firmware (if applicable):** Load device with older firmware not supporting offset adjustment | **Expected behavior:**<br>Offset adjustment command returns error<br>Error message displayed: "Adjustment failed"<br>System handles gracefully without escalation |
| 24 | **Test measurement mode:** Verify offset adjustment only available for temperature channels | **Verification:**<br>- Temperature channels: Offset adjustment available<br>- Cold Junction Temperature: Offset adjustment NOT available<br>- Thermal Voltage (Raw mode): Offset adjustment NOT available |

## Notes
- Feature implemented similarly to SENS devices for consistent user experience
- Automatic reset occurs on parameter changes: physical/sensor range, unit, SensorMode, Reference value, Adjustment group
- Reference value rules:
  - If physical range contains "0": Reference value = 0
  - If physical range does NOT contain "0": Reference value = (min + max) / 2
  - Reference value cannot be set outside physical range
- Offset adjustment only supported for temperature channels
- Cold Junction Temperature and Thermal Voltage (in raw mode) do NOT support offset adjustment
- Device XML files should include function ID information to distinguish offset compensation availability
- M-THERMO3 16 term cable references: 623-500 (IPEmotion), 623-501 (IPEmotion RT)

## Priority
High

## Coverage
- [x] Positive Testing
- [x] Negative Testing
- [ ] Performance Testing
- [x] Functional Testing

## Related Issues
- Offset compensation feature parity with SENS devices
- Firmware version compatibility handling
- Auto-reset on parameter changes
- Reference value validation and constraints
- Adjustment group functionality
