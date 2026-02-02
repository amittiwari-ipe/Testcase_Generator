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
4. Review generated scenarios and provide feedback
5. Approve scenarios to generate individual test cases

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
│   └── prompts/
│       └── Manual_TC.prompt.md       # GitHub Copilot test case generation prompt
├── .vscode/
│   ├── settings.json                 # VS Code workspace settings
│   ├── extensions.json               # Recommended extensions
│   └── tasks.json                    # Automated tasks
├── Template/                         # Official test case templates
│   ├── XPI/
│   ├── IPEmotion/
│   ├── IPEmotionRT/
│   └── IPE891/
├── help_document/                    # Reference documentation (104 markdown files, ~825 MB total)
│   ├── General/                      # Common documentation for ALL projects
│   │   └── product_highlights.md    # Product overview (9.5 MB)
│   ├── IPE891/                       # IPE891 documentation (19 MB)
│   │   ├── IPE891_Specification_COPYstation2_Product_Requirement_Specification.md
│   │   └── IPE891_Specification_COPYstation2_TRS.md
│   ├── IPEmotion/                    # IPEmotion documentation (267 MB)
│   │   ├── IPEmotion/                # 46 main chapters (Chapter_01 to Chapter_46)
│   │   │   ├── Chapter_01_1_Introduction.md
│   │   │   ├── Chapter_13_13_SIGNALS_work_space.md
│   │   │   ├── Chapter_16_16_Measurements_on_CAN_FD_LIN_ETH_FlexRay_interfaces.md
│   │   │   ├── Chapter_20_20_VIEW_work_space.md
│   │   │   ├── Chapter_21_21_Data_Manager_Work_Space.md
│   │   │   └── ... (all 46 chapters)
│   │   ├── IPEmotion_ETHERNET_Protocols.md
│   │   ├── IPEmotion_PlugIn_CAETEC_dataLog.md
│   │   ├── IPEmotion_PlugIn_CAETEC_dataLog_Script.md
│   │   ├── IPEmotion_PlugIn_CAN_Protocols.md
│   │   ├── IPEmotion_PlugIn_Video.md
│   │   ├── IPEmotion_Settings.md
│   │   ├── IPEmotion_Specification_Erweiterung.md
│   │   └── IPEmotion_Specification_Lastenheft.md
│   ├── IPEmotionRT/                  # IPEmotion RT documentation (218 MB)
│   │   ├── IPEmotion/                # 46 IPEmotion chapters (shared with IPEmotion project)
│   │   │   ├── Chapter_01_1_Introduction.md
│   │   │   ├── Chapter_05_5_IPEmotion_RT_data_logger_Quick_Start_Guide.md
│   │   │   ├── Chapter_26_26_IPEmotion_RT_Data_Logger_Software.md
│   │   │   └── ... (all 46 chapters)
│   │   ├── IPEmotionRT_Axis_IP_Cameras.md
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
│   └── XPI/                          # X-Plugin documentation (312 MB)
│       ├── IPEmotion/                # 46 IPEmotion chapters (shared with IPEmotion project)
│       │   ├── Chapter_01_1_Introduction.md
│       │   ├── Chapter_15_15_X-PlugIn_Option.md
│       │   └── ... (all 46 chapters)
│       ├── IPEmotion_PlugIn_IPETRONIK_X/  # Organized by chapters and sections
│       │   ├── 1_Introduction.md
│       │   ├── 2_Safety_Instructions_and_General_Information.md
│       │   ├── 3_Abbreviations.md
│       │   ├── 4_X-PlugIn_Overview.md
│       │   ├── 5_PlugIn_Options.md
│       │   ├── 6_ Hardware Integration/  # 7 sub-sections
│       │   ├── 7_Software Interface/     # 7 sub-sections
│       │   ├── 8_X-PlugIn Interface Configuration/  # 7 sub-sections + Section 8.5 split
│       │   ├── 9_Technical_Data.md
│       │   └── 10_Appendix.md
│       ├── XPI_IPEmotion_PlugIn_IPETRONIK_X.md
│       └── XPI_Testing_Documentation.md
├── Testcases/                        # All test case files organized by project and requirement
│   ├── XPI/                          # X-Plugin test cases
│   │   └── [TICKET-ID]/              # Requirement folder (e.g., XPI-17015/)
│   │       ├── Transcript.md         # Original requirement document
│   │       ├── Scenarios.md          # Test scenarios for approval
│   │       └── Scenario_N_*.md       # Individual test case files
│   ├── IPEmotion/                    # IPEmotion test cases
│   │   └── [TICKET-ID]/              # Requirement folder (e.g., IM-2436/)
│   ├── IPEmotionRT/                  # IPEmotion RT test cases
│   │   └── [TICKET-ID]/              # Requirement folder (e.g., TD4-16395/)
│   └── IPE891/                       # IPE891 test cases
│       └── [TICKET-ID]/              # Requirement folder (e.g., vvHLP-2475/)
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

- **Python 3.14** with **PyMuPDF (fitz)** - For PDF to markdown conversion with embedded images
- **GitHub Copilot** - AI-assisted test case generation

## PDF Documentation Features

All PDF documentation has been converted to markdown with:
- ✅ **Embedded base64 images** - View images directly in VS Code preview (Ctrl+Shift+V)
- ✅ **Chapter-wise organization** - Large documents split into manageable chapters
- ✅ **Sub-section splitting** - Complex chapters further divided for easy navigation
- ✅ **Original formatting** - Text and structure preserved from PDFs

### Viewing Documentation

1. Open any `.md` file in the `help_document/` folder
2. Press `Ctrl+Shift+V` to open Markdown preview
3. All images will display inline (no separate image files needed)

### Documentation Organization

- **General**: Product highlights and overview
- **IPE891**: Specification and TRS documents
- **IPEmotion**: 46 chapters covering all features (SIGNALS, ACQUISITION, VIEW, Data Manager, ANALYSIS, etc.)
- **IPEmotionRT**: RT Logger documentation, hardware setup, communication protocols
  - **IPEmotion/ folder**: 46 shared IPEmotion chapters for RT-specific guidance
- **XPI**: Complete IPETRONIK X plugin documentation with 10 main chapters and detailed sub-sections
  - **IPEmotion/ folder**: 46 shared IPEmotion chapters for X-Plugin integration reference

**Note**: IPEmotion help files (46 chapters) are available in both IPEmotionRT and XPI project folders for comprehensive test case creation.

## Test Case Organization

### Requirement-Based Folder Structure

Each requirement has its own dedicated folder:

```
Testcases/[Project]/[TICKET-ID]/
  ├── Transcript.md (or original format like .pdf)
  ├── Scenarios.md
  ├── Scenario_1_[Feature_Name]_Test.md
  ├── Scenario_2_[Feature_Name]_Test.md
  └── ...
```

### Workflow

1. **Create requirement folder**: `Testcases/[Project]/[TICKET-ID]/`
2. **Save transcript**: Store user-provided requirement document
3. **Generate scenarios**: Create `Scenarios.md` with all test scenarios
4. **Review & approve**: User reviews and approves scenarios
5. **Create test cases**: Generate individual test case files (one per scenario)

### File Naming Conventions

- **Requirement Folder**: `[TICKET-ID]` (e.g., `IM-2436`, `XPI-17015`)
- **Transcript File**: `Transcript.md` (or keep original format like `.pdf`)
- **Scenarios File**: `Scenarios.md`
- **Test Case Files**: `Scenario_[N]_[Feature_Description]_Test.md`

### Examples

**XPI Project:**
```
Testcases/XPI/XPI-17015/
  ├── Transcript.md
  ├── Scenarios.md
  ├── Scenario_1_M-THERMO3_16_Offset_Adjustment_Test.md
  └── Scenario_2_Reset_Offset_Channel_Grid_Test.md
```

**IPEmotion Project:**
```
Testcases/IPEmotion/IM-2436/
  ├── Transcript.md
  ├── Scenarios.md
  ├── Scenario_1_Detection_Functionality_Test.md
  └── Scenario_2_Error_Handling_Test.md
```

## Configuration

- VS Code settings: `.vscode/settings.json`
- Copilot prompt: `.github/prompts/Manual_TC.prompt.md`
- Test case templates: `Template/[ProjectName]/[ProjectName]_Template.md`
- Reference docs: `help_document/[ProjectName]/` (104 markdown files, ~825 MB with embedded images)
