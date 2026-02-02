# Requirement: IM-62433

## Title
M-CNT3 4: Implementation UI: Channel-Wizard: (Leaded) Scaling configuration: Frequency (Hz) to Flow rate (m³/s)

## Project
IPEmotion

## Type
Feature Implementation - UI Enhancement

## Description
Implement a scaling function in the IPEmotion Channel Wizard that allows direct conversion from frequency (Hz) to flow rate for M-CNT3 4 channels configured in "Frequency" or "Frequency with Direction Detection" sensor modes.

### Key Features:
1. **Frequency to Flow Rate Conversion**: Direct scaling from Hz to volume flow units (l/min, m³/s, etc.)
2. **Input Parameters**:
   - Maximum frequency (SensorMax) - Hz
   - Maximum flow rate (PhysMax) - l/min or other volume flow unit
   - Minimum frequency (SensorMin) - Hz (automatic: 0Hz)
   - Minimum flow rate (PhysMin) - l/min (automatic: 0)
3. **Physical Unit Selection**: Dropdown list of supported volume flow units (not free text)
4. **Persistent Storage**: Input parameters stored in IPEmotion model

### Example Configuration:
- Maximum frequency (SensorMax): 1000 Hz
- Maximum flow rate (PhysMax): 75 l/min
- Minimum frequency (SensorMin): 0 Hz (automatic)
- Minimum flow rate (PhysMin): 0 l/min (automatic)

**Scaling Formula**: Flow rate = (Frequency / SensorMax) * PhysMax

## Scope and Limitations
✅ **Included:**
- UI implementation in IPEmotion Channel Wizard
- Scaling calculator with frequency to flow rate conversion
- Support for multiple volume flow units (l/min, m³/s, m³/h, gal/min, etc.)
- Persistent storage of parameters in IPEmotion model
- Applicable to SensorMode: "Frequency" and "Frequency with Direction Detection"

❌ **Not Included (Current Limitations):**
- Saving channel settings to sensor database
- Loading sensor from sensor database (sensor selection not supported)
- Free-text physical unit configuration (only predefined units from dropdown)

## Applicable Hardware
- M-CNT3 4 (Counter Module with 4 channels)
- SensorMode: Frequency OR Frequency with Direction Detection

## Expected Behavior
1. User opens Channel Wizard for M-CNT3 4 channel
2. User selects SensorMode: "Frequency" or "Frequency with Direction Detection"
3. Scaling configuration section displays frequency-to-flow-rate fields
4. User enters Maximum frequency (SensorMax) in Hz
5. User selects physical unit from dropdown (e.g., l/min)
6. User enters Maximum flow rate (PhysMax) in selected unit
7. System automatically sets Minimum values to 0 (if not manually changed)
8. System calculates scaling: Physical value = (Frequency / SensorMax) * PhysMax
9. Configuration is saved persistently in IPEmotion model
10. Real-time frequency measurements are automatically converted to flow rate

## Test Coverage Requirements
- Positive testing: Valid configurations with different units and ranges
- Boundary testing: Min/Max frequency values, extreme flow rates
- Negative testing: Invalid inputs, out-of-range values
- Functional testing: Scaling calculation accuracy, unit conversions
- Integration testing: Real-time data conversion, model persistence
- UI testing: Dropdown selection, field validation, user experience

## Priority
High

## Related Documentation
- IPEmotion User Manual Chapter 14: GInterface Configuration
- IPEmotion User Manual Chapter 15: X-PlugIn Option
- XPI Documentation: M-CNT3 Counter Module specifications
- IPEmotion Settings and Configuration

## Hardware/Software Requirements
- IPEmotion 2024 R2 or later
- X-PlugIn license
- M-CNT3 4 hardware module (for hardware testing)
- Frequency sensor/simulator for testing

## Date Created
February 1, 2026
