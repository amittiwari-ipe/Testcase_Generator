# Test Scenarios for IM-62433
## M-CNT3 4: Channel-Wizard: Frequency to Flow Rate Scaling

**Project:** IPEmotion
**Requirement:** IM-62433
**Priority:** High
**Date:** February 1, 2026

---

## Scenario Overview

This document outlines the test scenarios for validating the frequency-to-flow-rate scaling configuration feature in IPEmotion Channel Wizard for M-CNT3 4 counter module. Each scenario will be converted into detailed test cases upon approval.

---

## Scenario 1: Basic Frequency to Flow Rate Scaling Configuration
**Type:** Positive Testing - Functional
**Objective:** Verify that users can configure basic frequency-to-flow-rate scaling with default minimum values

**Description:**
- Open Channel Wizard for M-CNT3 4 channel
- Select SensorMode: "Frequency"
- Configure scaling: SensorMax = 1000 Hz, PhysMax = 75 l/min
- Verify minimum values automatically set to 0
- Save configuration and verify persistence
- Verify real-time frequency values are converted correctly

**Expected Test Cases:** 2-3 test cases covering different frequency ranges

**Status:** ⏳ Pending Approval

---

## Scenario 2: Multiple Volume Flow Units Selection
**Type:** Positive Testing - Functional
**Objective:** Verify that all supported volume flow units work correctly in scaling configuration

**Description:**
- Configure scaling with different volume flow units from dropdown
- Test units: l/min, l/s, m³/s, m³/h, m³/min, gal/min, gal/s
- Verify unit conversion calculations are accurate
- Verify unit display in signal properties
- Test switching between units with existing configuration

**Expected Test Cases:** 3-4 test cases covering different unit combinations

**Status:** ⏳ Pending Approval

---

## Scenario 3: Custom Minimum Frequency and Flow Rate
**Type:** Positive Testing - Functional
**Objective:** Verify that users can manually configure non-zero minimum values

**Description:**
- Configure scaling with custom minimum values
- Example: SensorMin = 100 Hz, PhysMin = 10 l/min, SensorMax = 1000 Hz, PhysMax = 100 l/min
- Verify linear scaling calculation with offset
- Verify behavior at boundary values (exactly at min/max)
- Test negative direction detection (if applicable)

**Expected Test Cases:** 2-3 test cases with different minimum value configurations

**Status:** ⏳ Pending Approval

---

## Scenario 4: Frequency with Direction Detection Mode
**Type:** Positive Testing - Functional
**Objective:** Verify scaling configuration works correctly with bidirectional frequency sensors

**Description:**
- Select SensorMode: "Frequency with Direction Detection"
- Configure frequency-to-flow-rate scaling
- Test forward direction frequency → positive flow rate
- Test reverse direction frequency → negative flow rate
- Verify direction indication in signal data
- Verify scaling formula applies correctly in both directions

**Expected Test Cases:** 2-3 test cases covering bidirectional scenarios

**Status:** ⏳ Pending Approval

---

## Scenario 5: Real-Time Data Conversion and Display
**Type:** Integration Testing
**Objective:** Verify that real-time frequency measurements are correctly converted to flow rate

**Description:**
- Configure scaling in Channel Wizard
- Connect to M-CNT3 4 hardware with frequency input
- Start measurement acquisition
- Apply known frequency input (e.g., 500 Hz from function generator)
- Verify displayed flow rate matches expected calculation
- Verify signal updates in real-time
- Check signal properties show correct unit

**Expected Test Cases:** 2-3 test cases with different frequency inputs

**Status:** ⏳ Pending Approval

---

## Scenario 6: Configuration Persistence in IPEmotion Model
**Type:** Functional Testing
**Objective:** Verify that scaling configuration is saved and restored correctly

**Description:**
- Configure frequency-to-flow-rate scaling with specific parameters
- Save IPEmotion project
- Close and reopen IPEmotion
- Open Channel Wizard for same channel
- Verify all scaling parameters are restored correctly
- Verify measurements continue to use correct scaling after reload

**Expected Test Cases:** 2 test cases (save/reload, export/import model)

**Status:** ⏳ Pending Approval

---

## Scenario 7: Boundary Value Testing
**Type:** Boundary Testing
**Objective:** Verify system handles minimum, maximum, and edge-case values correctly

**Description:**
- Test with very small frequency (0.001 Hz) and flow rate (0.001 l/min)
- Test with very large frequency (100 kHz) and flow rate (10000 l/min)
- Test with SensorMax = 0 (should show validation error)
- Test with PhysMax = 0 (should show validation error or warning)
- Test frequency input exactly at SensorMax
- Test frequency input exceeding SensorMax (extrapolation behavior)

**Expected Test Cases:** 4-5 test cases covering boundary conditions

**Status:** ⏳ Pending Approval

---

## Scenario 8: Invalid Input Validation
**Type:** Negative Testing
**Objective:** Verify proper validation and error handling for invalid inputs

**Description:**
- Enter non-numeric values in frequency/flow rate fields
- Enter negative frequency values
- Enter SensorMin > SensorMax (should show error)
- Enter PhysMin > PhysMax (should show error)
- Test very large numbers exceeding field limits
- Leave required fields empty and attempt to save
- Verify appropriate error messages guide user

**Expected Test Cases:** 4-5 test cases covering different validation scenarios

**Status:** ⏳ Pending Approval

---

## Scenario 9: Scaling Calculation Accuracy
**Type:** Functional Testing
**Objective:** Verify mathematical accuracy of frequency-to-flow-rate conversion

**Description:**
- Configure known scaling parameters (e.g., 1000 Hz → 100 l/min)
- Test conversion at multiple frequency points: 0, 250, 500, 750, 1000 Hz
- Calculate expected flow rates and compare with actual
- Verify linear interpolation accuracy (tolerance ±0.1%)
- Test with non-round numbers (e.g., 723 Hz, 87.5 l/min)
- Verify floating-point precision handling

**Expected Test Cases:** 3-4 test cases with different calculation scenarios

**Status:** ⏳ Pending Approval

---

## Scenario 10: UI Usability and Field Behavior
**Type:** UI Testing
**Objective:** Verify user interface behavior, field enabling/disabling, and user experience

**Description:**
- Verify scaling fields appear only when SensorMode = "Frequency" or "Frequency with Direction Detection"
- Test field enabling/disabling based on sensor mode selection
- Verify physical unit dropdown contains all supported volume flow units
- Test tab order and keyboard navigation
- Verify field tooltips and help text
- Test undo/cancel functionality
- Verify field formatting (decimal places, separators)

**Expected Test Cases:** 3-4 test cases covering UI behavior

**Status:** ⏳ Pending Approval

---

## Scenario 11: Integration with Existing Scaling Methods
**Type:** Integration Testing
**Objective:** Verify frequency-to-flow-rate scaling coexists with other scaling methods

**Description:**
- Configure channel with frequency-to-flow-rate scaling
- Verify other channels can use different scaling methods simultaneously
- Test switching from frequency-to-flow-rate to other scaling methods
- Test switching from other scaling methods to frequency-to-flow-rate
- Verify no interference between different scaling configurations
- Test copy/paste channel configuration between channels

**Expected Test Cases:** 2-3 test cases covering scaling method interactions

**Status:** ⏳ Pending Approval

---

## Scenario 12: Documentation and User Guidance
**Type:** Usability Testing
**Objective:** Verify that users can understand and use the feature with available documentation

**Description:**
- Follow user manual instructions to configure scaling
- Verify example values from documentation work correctly
- Test calculation formula provided in documentation
- Verify help text and tooltips match documentation
- Check for any missing or unclear instructions

**Expected Test Cases:** 1-2 test cases validating documentation accuracy

**Status:** ⏳ Pending Approval

---

## Summary

**Total Scenarios:** 12
**Estimated Test Cases:** 30-40 individual test cases

**Coverage Breakdown:**
- Positive/Functional Testing: 6 scenarios (15-19 test cases)
- Integration Testing: 3 scenarios (6-8 test cases)
- Negative Testing: 1 scenario (4-5 test cases)
- Boundary Testing: 1 scenario (4-5 test cases)
- UI Testing: 1 scenario (3-4 test cases)

---

## Known Limitations (Not to be Tested)
- ❌ Sensor database save functionality (not implemented)
- ❌ Sensor database selection (not implemented)
- ❌ Free-text physical unit entry (only dropdown selection supported)

---

## Next Steps

1. **Review and approve** specific scenarios to implement
2. **Prioritize** which scenarios are most critical
3. **Provide feedback** on scenario coverage
4. Once approved, detailed test cases will be created for selected scenarios

---

## Notes

- All test cases will reference IPEmotion documentation:
  - Chapter 14: GInterface Configuration
  - Chapter 15: X-PlugIn Option
  - XPI M-CNT3 specifications
- Hardware testing requires M-CNT3 4 module and frequency source
- Software-only testing possible using simulation mode
