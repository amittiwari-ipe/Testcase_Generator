# CS2_License_Management_WebUI_Test

## Description
COPYstation2 shall provide an option to add, delete, and list licenses via the Web UI:
1. COPYstation2 shall provide an option to add, delete, and list licenses via the Web UI. #1
2. COPYstation2 shall display a proper error message when an invalid license is added. #2
3. All licenses added via Web UI shall be persisted in the loggerinfo file at /etc/cs2/. #3

## Pre-Condition

### Hardware Setup:

| COPYstation2 |
|--------------|
| Copystation2 should be up and running. |

### Software Setup:

| COPYstation2 |
|--------------|
| Install the latest CS2 web interface and Backend dlua |

## Test Steps

| Step | RT Steps / Input Data | Expected Result |
|------|----------------------|-----------------|
| 1 | On your PC, open a browser and enter the Copystation2 IP address | |
| 2 | Log in using Admin credentials | |
| 3 | Settings | LICENSES section is available with the "Add New+" option |
| 4 | Licenses → Add New + | "Add New Key" pop-up is displayed with License Key field, Save, and Cancel button |
| 5 | Save without entering a license key | Inline error message is displayed:<br>**A license key is required.** |
| 6 | Cancel | Pop-up is closed, and no error message remains |
| 7 | Licenses → Add New+ → Enter the following invalid license keys one by one, clicking Save each time:<br>- 12345<br>- qwertyu<br>- !@#$%^&<br>- QWER@#$123qwer | Toast message is displayed for each attempt:<br><br>**Error**<br>Failed to add license.<br><br>No licenses are added or listed |
| 8 | Logs → Device Logs | Following error messages will be recorded:<br><br>SYSTEM; WEBINTERFACE;ERROR;License validation failed. key: 12345<br><br>SYSTEM;WEBINTERFACE;ERROR;License validation failed. key: qwertyu<br><br>SYSTEM;WEBINTERFACE;ERROR;License validation failed. key: !@#$%^&<br><br>SYSTEM;WEBINTERFACE;ERROR;License validation failed. key: QWER@#$123qwer |
| 9 | Logs → Web UI Logs | Following error messages will be recorded:<br><br>[Settings] Failed to add license.<br>[Settings] Failed to add license.<br>[Settings] Failed to add license.<br>[Settings] Failed to add license. |
| 10 | Licenses → Add New+ → Insert a valid CS2_01 license key in the license field → Save | Toast message is displayed:<br><br>**Success**<br>License added successfully.<br><br>The license will be added successfully with the following columns:<br><br>**License Type:** CS2_01<br>**Valid Until:** unlimited<br>**Actions:** delete |
| 11 | Logs → Device Logs | Following entry is recorded:<br><br>SYSTEM;INFO;installed license CS2_01 |
| 12 | Logs → Web UI Logs | Following entries are recorded:<br><br>[Settings] License added successfully.<br>[Settings] Attempting to add new license. |
| 13 | Open the loggerinfo file using terminal:<br>`cat /etc/cs2/loggerinfo` | Imported CS2_01 license key is present in the file |
| 14 | Add the same CS2_01 license key again | Toast message is displayed:<br><br>**Success**<br>License added successfully.<br><br>Again, the same license will not be displayed multiple times. |
| 15 | Restart the Copystation2 | |
| 16 | Log in as Admin → Settings → LICENSES | Previously added license is still listed |
| 17 | Repeat all the above steps using valid license keys for the following license types:<br>- CS2_SFTP<br>- CS2_API | |
| 18 | IPE-admin → Sign Out | |
| 19 | Log in again as Admin → Settings → Licenses | All imported licenses will be available. |

## Notes
- Test verifies Web UI functionality for license management
- Validates error handling for invalid license keys
- Confirms license persistence in /etc/cs2/loggerinfo
- License types tested: CS2_01, CS2_SFTP, CS2_API

## Priority
High

## Coverage
- [x] Positive Testing
- [x] Negative Testing
- [ ] Performance Testing
- [x] Functional Testing
