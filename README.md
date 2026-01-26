# IPETRONIK Test Case Management

Test case creation and management for IPETRONIK products.

## Supported Products

- **XPI** - X-Plugin for IPEmotion
- **IPEmotion** - IPEmotion software platform
- **IPEmotion RT** - IPEmotion RT Logger
- **IPE891** - IPE891 product line

## Quick Start

### Creating a Test Case

1. Open GitHub Copilot Chat
2. Use prompt: `@workspace /Manual_TC`
3. Paste your requirement with ticket ID (auto-detects project)

### Automatic Project Detection

Ticket prefixes automatically determine the project:

| Prefix | Project | Example |
|--------|---------|---------|
| **XPI-** | X-Plugin | XPI-11839 |
| **IM-** | IPEmotion | IM-61740 |
| **TD4-** | IPEmotion RT | TD4-14432 |
| **vvHLP-** | IPE891 | vvHLP-2475 |

### Examples

**Example 1 - With Ticket (Auto-detection):**
```
XPI-11839 - Anbindung M-THERMO3 16
Basis-Parameter wie M-THERMO2...
Senderate für jeden Kanal einzeln einstellbar
```

**Example 2 - Manual Project Specification:**
```
Project ID: XPI
Type: Feature
Requirement: Test Sx-STG module IEPE sensor configuration with different excitation current levels (2mA, 4mA, 8mA)
```

## Folder Structure

```
├── .github/
│   └── copilot-instructions.md       # GitHub Copilot workspace configuration
├── .vscode/
│   ├── settings.json                 # VS Code workspace settings
│   ├── extensions.json               # Recommended extensions
│   └── tasks.json                    # Automated tasks
├── Template/                         # Official test case templates
│   ├── XPI/
│   ├── IPEmotion/
│   ├── IPEmotionRT/
│   └── IPE891/
├── help_document/                    # Reference documentation (organized by product)
│   ├── XPI/                          # X-Plugin documentation
│   │   ├── X-Plugin.md
│   │   ├── X-PlugIn_Testing_Documentation.md
│   │   ├── XPI_IPEmotion.md
│   │   ├── XPI_IPEmotion_PlugIn_IPETRONIK_X.md
│   │   └── XPI_Testing_Documentation.md
│   ├── IPEmotion/                    # IPEmotion documentation
│   │   ├── IPEmotion.md
│   │   ├── IPEmotion_Main.md
│   │   ├── IPEmotion_PlugIn_CAETEC_dataLog.md
│   │   ├── IPEmotion_PlugIn_CAETEC_dataLog_Script.md
│   │   ├── IPEmotion_PlugIn_CAN_Protocols.md
│   │   ├── IPEmotion_PlugIn_IPETRONIK_X.md
│   │   ├── IPEmotion_PlugIn_Video.md
│   │   ├── IPEmotion_Settings.md
│   │   ├── IPEmotion_Specification_Erweiterung.md
│   │   └── IPEmotion_Specification_Lastenheft.md
│   ├── IPEmotionRT/                  # IPEmotion RT documentation
│   │   ├── IPEmotionRT_Axis_IP_Cameras.md
│   │   ├── IPEmotionRT_ETHERNET_Protocols.md
│   │   ├── IPEmotionRT_Gateway_Use_Cases.md
│   │   ├── IPEmotionRT_IPE833.md
│   │   ├── IPEmotionRT_IPEcloud_Sales.md
│   │   ├── IPEmotionRT_IPElog2_XCP_Slave.md
│   │   ├── IPEmotionRT_IPEmotion.md
│   │   ├── IPEmotionRT_J1939.md
│   │   ├── IPEmotionRT_M_Gateway3.md
│   │   ├── IPEmotionRT_OBD_II.md
│   │   ├── IPEmotionRT_Settings.md
│   │   ├── IPEmotionRT_Traffic_Values_Developer_Check.md
│   │   └── IPEmotionRT_Video.md
│   ├── IPE891/                       # IPE891 documentation
│   │   ├── IPE891_Product_Requirement_Specification.md
│   │   ├── IPE891_Specification_COPYstation2_Product_Requirement_Specification.md
│   │   └── IPE891_Specification_COPYstation2_TRS.md
│   └── General/                      # Common documentation for ALL projects
│       └── product_highlights.md     # Shared across all products
├── Testcases/                        # All test case files organized by project
│   ├── XPI/                          # X-Plugin test cases
│   ├── IPEmotion/                    # IPEmotion test cases
│   ├── IPEmotionRT/                  # IPEmotion RT test cases
│   └── IPE891/                       # IPE891 test cases
├── convert_pdfs.py                   # PDF to markdown conversion script
├── .gitignore                        # Git ignore configuration
└── README.md                         # This file
```

## Test Case Format

All test cases follow this structure:

- **Test Case Title**: Clear, descriptive title
- **Preconditions**:
  - Required Licenses
  - Hardware Setup (IPEmotion and/or IPEmotion RT)
  - Software Version / Firmware
- **Test Steps Table**: Step | RT Steps / Input Data | Expected Result
- **Priority**: High / Medium / Low
- **Coverage Expectations**: Positive, Negative, Performance, Functional

## Tools

- **uvx** (v0.9.26) - For PDF to markdown conversion
- **markitdown** - Microsoft's document conversion tool
- **GitHub Copilot** - AI-assisted test case generation

## Adding New Reference Documentation

1. Place PDFs in `.ref-docs/` folder
2. Convert to markdown:
   ```bash
   export PYTHONIOENCODING=utf-8
   uvx --python 3.14 markitdown ".ref-docs/your-file.pdf" > "help_document/[Product]/output.md"
   ```
3. Update documentation references in `.github/copilot-instructions.md` if needed

## Test Case Naming Convention

Test cases are organized in project-specific folders:

- **Location**: `Testcases/[ProjectName]/`
  - XPI test cases → `Testcases/XPI/`
  - IPEmotion test cases → `Testcases/IPEmotion/`
  - IPEmotion RT test cases → `Testcases/IPEmotionRT/`
  - IPE891 test cases → `Testcases/IPE891/`

- **File naming**:
  - With ticket: `[TICKET-ID]_[Feature]_Test.md`
    - Example: `Testcases/XPI/XPI-11839_M-THERMO3_Integration_Test.md`
  - Without ticket: `[Module]_[Feature]_Test.md`
    - Example: `Testcases/XPI/Sx-STG_IEPE_Mode_Test.md`

## Configuration

- VS Code settings: `.vscode/settings.json`
- Copilot instructions: `.github/copilot-instructions.md`
- Test case templates: `Template/[ProjectName]/[ProjectName]_Template.md`
