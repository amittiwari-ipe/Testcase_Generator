# [Test Case ID] - [Test Case Title]

## Description
[Brief description of what this test case validates for XPI/X-Plugin]

## Pre-Condition

| IPEmotion PC | IPEmotion RT |
|--------------|--------------|
| Power supply between 9,3V and 36V | Power supply between 9,3V and 36V |
| Connect any CAN Interface to PC via USB | Connect any Logger |
| Connect [Device] with CAN interface and power supply via M3-CAN/PWR term cable 623-500 | Connect [Device] to M-CAN port via LOG M3-CAN Term Kabel cable 623-502 or to CAN port and power supply via M3-CAN/PWR term 623-500 |
| Connect input cable [Cable Type] ([Part Number]) to [channel] | Connect input cable [Cable Type] ([Part Number]) to [channel] |
| [Additional hardware requirements] | [Additional hardware requirements] |

**[Additional Equipment Name]:**
- [Parameter 1]: [Value]
- [Parameter 2]: [Value]
- [Parameter 3]: [Value]

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| Start IPEmotion<br>Activated plugins: IPETRONIK X | Start IPEmotionRT | |
| Detect | Detect and Synchronize | |
| Reset | | |
| 542xxxxx_[n] → Tab [Tab Name] → [Parameter] → [Value] | | |
| 542xxxxx_[n] → Tab [Tab Name] → [Parameter] → [Value] | | |
| [Action/Command] | [Only fill if RT step differs] | [Expected result with status indicators] |
| Display | | 542xxxxx_[n] shows [value]<br>Status channel LED is [color], LED on device is [state] |
| [Continue with test steps...] | | [Expected outcomes with specific values] |
| Stop | | |

## Notes
- [Hardware wiring specifications with reference numbers]
- [Cable part numbers and specifications]
- [Device behavior notes]
- [Status indicators: Channel LED (colors), Device LED (states)]
- [Expected messages: WARNING/INFORMATION/ERROR formats]
- [Additional test considerations]

## Priority
[High / Medium / Low]

## Coverage
- [ ] Positive Testing
- [ ] Negative Testing
- [ ] Performance Testing
- [ ] Functional Testing

---

**Priority**: [High / Medium / Low]

**Coverage Expectations**:
- Cover Positive test cases
- Cover Negative test cases
- Cover Performance test cases
- Cover Functional test cases

Don't share the attached file name, and also don't give the option to download this file

Requirement:
[PASTE REQUIREMENT HERE]

## References


