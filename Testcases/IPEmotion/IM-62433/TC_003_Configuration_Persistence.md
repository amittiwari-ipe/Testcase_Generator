# TC_003 - Configuration Persistence and Project Reload

## Description
Verify that frequency-to-flow-rate scaling configuration is saved persistently in IPEmotion model and correctly restored after closing and reopening the project.

## Pre-Condition

### Software Setup:

#### Windows
- IPEmotion 2024 R2 or later installed
- X-PlugIn license activated
- M-CNT3 4 hardware module connected or simulation mode
- Create test folder: `C:\TestData\IM-62433\TC_003\`
- Prepare test configuration: SensorMax = 5000 Hz, PhysMax = 250 l/min
- Ensure sufficient disk space for project save

#### Linux
- IPEmotion installed via Docker or native installation
- X-PlugIn license activated
- M-CNT3 4 hardware module connected or simulation mode
- Create test folder: `/home/testuser/TestData/IM-62433/TC_003/`
- Ensure read/write permissions on test folder
- Ensure sufficient disk space for project save

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| 1 | Launch IPEmotion application | IPEmotion opens successfully |
| 2 | Create new project: File → New Project | New empty project created |
| 3 | Navigate to GInterface Configuration workspace | GInterface workspace displayed |
| 4 | Add M-CNT3 4 device (if not already present) | M-CNT3 4 device visible in device tree |
| 5 | Right-click M-CNT3 4 → Add Channel | Channel creation dialog opens |
| 6 | Configure channel:<br>- Name: "FlowSensor_Persist"<br>- SensorMode: "Frequency" | Channel name and mode set |
| 7 | Configure scaling parameters:<br>- SensorMax: 5000 Hz<br>- PhysMax: 250 l/min<br>- Unit: l/min | All scaling parameters entered |
| 8 | Verify minimum values auto-set to 0 | SensorMin = 0 Hz, PhysMin = 0 l/min |
| 9 | Click "OK" to save channel configuration | Channel created successfully |
| 10 | Verify channel appears in device tree | "FlowSensor_Persist" visible under M-CNT3 4 |
| 11 | Save project: File → Save Project As | Save dialog opens |
| 12 | Save as: "TC_003_Persistence_Test.ipep" in test folder | Project saved successfully, confirmation shown |
| 13 | Verify project file exists in test folder | File "TC_003_Persistence_Test.ipep" created |
| 14 | Note file size and timestamp | File size recorded (e.g., ~150 KB) |
| 15 | Close IPEmotion: File → Exit | IPEmotion closes completely |
| 16 | Wait 5 seconds | Ensure complete shutdown |
| 17 | Relaunch IPEmotion application | IPEmotion opens to start screen |
| 18 | Open saved project: File → Open Project | File browser opens |
| 19 | Navigate to test folder and select "TC_003_Persistence_Test.ipep" | File selected |
| 20 | Click "Open" | Project loads successfully |
| 21 | Verify project loads without errors | No error messages, project fully loaded |
| 22 | Navigate to GInterface Configuration workspace | GInterface workspace displayed with configured device |
| 23 | Locate M-CNT3 4 device in device tree | M-CNT3 4 device visible |
| 24 | Verify "FlowSensor_Persist" channel is present | Channel visible in device tree |
| 25 | Right-click "FlowSensor_Persist" → Properties | Channel properties dialog opens |
| 26 | Navigate to Scaling configuration tab | Scaling settings displayed |
| 27 | Verify all parameters restored correctly:<br>- SensorMode: Frequency<br>- SensorMax: 5000 Hz<br>- PhysMax: 250 l/min<br>- Unit: l/min<br>- SensorMin: 0 Hz<br>- PhysMin: 0 l/min | All values match original configuration exactly |
| 28 | Close properties dialog | Dialog closes |
| 29 | Navigate to SIGNALS workspace | SIGNALS workspace opens |
| 30 | Verify signal "FlowSensor_Persist" exists with unit "l/min" | Signal present with correct unit |
| 31 | Right-click signal → Properties | Signal properties open |
| 32 | Verify signal scaling type is "Frequency to Flow Rate" | Scaling type preserved correctly |
| 33 | Close signal properties | Dialog closes |
| 34 | Start measurement acquisition | Acquisition starts |
| 35 | Apply test frequency: 2500 Hz (if hardware available) | Frequency input set |
| 36 | Verify displayed flow rate: 125.0 l/min (2500/5000*250) | Correct flow rate displayed (scaling works after reload) |
| 37 | Stop acquisition | Acquisition stopped |
| 38 | Close project without saving additional changes | Project closed |

## Notes
- This test validates persistent storage of frequency-to-flow-rate configuration in IPEmotion model
- Configuration must survive complete application restart
- All parameters must be restored exactly as configured
- Scaling calculation must work correctly after project reload
- Expected calculation at 2500 Hz: 2500/5000*250 = 125.0 l/min
- Project file format: .ipep (IPEmotion Project)
- Configuration stored in XML format within project file
- Test validates data serialization/deserialization
- Reference: IPEmotion User Manual Chapter 8 (Application Menu - File operations)
- Reference: IPEmotion User Manual Chapter 12 (PROJECT workspace)
- KD Item: IM-62433

## Priority
High

## Coverage
- [x] Positive Testing
- [ ] Negative Testing
- [ ] Performance Testing
- [x] Functional Testing
