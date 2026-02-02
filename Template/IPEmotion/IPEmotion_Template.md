# [Test Case ID] - [Test Case Title]

## Description
[Brief description of what this test case validates]

## Pre-Condition

### Software Setup:

#### Windows
- IPEmotion [version] installed
- Required plugins: [List activated plugins or "None"]
- Test data location: [Exact path with drive letter, e.g., M:\Testmanagement\DUS\01_Projekte\...]
- Required files: [List specific files with extensions]
- Hardware requirements: [Specific hardware modules if needed]
- License requirements: [Specific licenses needed]

#### Linux
- IPEmotion [version] installed (Docker/native)
- Required plugins: [List activated plugins or "None"]
- Test data location: [Exact path, e.g., /home/testuser/testdata/...]
- Required files: [List specific files with extensions]
- Hardware requirements: [Specific hardware modules if needed]
- License requirements: [Specific licenses needed]

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| 1 | Start IPEmotion<br>Activated plugins:<br>[List or "None"] | [IPEmotion starts successfully] |
| 2 | File → [Menu path using →] | [Exact dialog/window name in quotes with exact fields and values shown]<br><br>Example format:<br>"Dialog Name" window turns up with the following data: [#1]<br><br>Field 1: [exact value]<br>Field 2: [exact value]<br>Checkbox: [Checked/Unchecked]<br>Dropdown: [selected value] |
| 3 | [Action] → [Sub-action] → [Specific button/field] | [Exact result with specific values]<br><br>Example:<br>The following data is available:<br><br>Property 1: [exact value]<br>Property 2: [exact value]<br>Count: [exact number] |
| 4 | [Navigation path] → Grid → column [Signal Name] | [Exact values at specific indices]<br><br>Index 0: [exact value]<br>Index 1: [exact value]<br>...<br>Index [n-1]: [exact value]<br>Index [n]: [exact value] |
| 5 | [Item] → Properties → [Tab name] | The following data is available:<br><br>[Complete property list with exact values]<br>Type: [value]<br>Name: [value]<br>Unit: [value or <empty>]<br>Data type: [exact type]<br>Min: [exact value]<br>Max: [exact value]<br>[All other properties...] |

## Notes
- [Reference markers like [#1], [#2] for cross-referencing]
- [Exact file paths with full directory structure]
- [Specific test data files and their locations]
- [Expected calculations or formulas]
- [Tolerance values for numeric comparisons]
- KD Item: [Item number]
- Reference: [IPEmotion User Manual Chapter X]

## Priority
[High / Medium / Low]

## Coverage
- [ ] Positive Testing
- [ ] Negative Testing
- [ ] Performance Testing
- [ ] Functional Testing
