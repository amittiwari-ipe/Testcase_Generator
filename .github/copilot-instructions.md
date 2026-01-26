# GitHub Copilot Instructions for IPETRONIK Test Case Creation

## Project Context

This workspace is for creating and managing test cases for IPETRONIK products:
- XPI (X-Plugin)
- IPEmotion
- IPEmotion RT
- IPE891

## Test Case Creation Guidelines

### Automatic Project Detection

Requirements with ticket IDs automatically detect the project:
- **XPI-** prefix → X-Plugin
- **IM-** prefix → IPEmotion  
- **TD4-** prefix → IPEmotion RT
- **vvHLP-** prefix → IPE891

### File Location
- All test cases MUST be created in `testcases/` folder
- Use naming convention:
  - With ticket: `[TICKET-ID]_[Feature]_Test.md` (e.g., `XPI-11839_M-THERMO3_Test.md`)
  - Without ticket: `[Module]_[Feature]_Test.md` (e.g., `Sx-STG_IEPE_Mode_Test.md`)

### Test Case Format
Follow the official templates in `Template/` folder:
- `Template/XPI/XPI_Template.md` - X-Plugin test case template
- `Template/IPEmotion/IPEmotion_Template.md` - IPEmotion test case template
- `Template/IPEmotionRT/IPEmotionRT_Template.md` - IPEmotion RT test case template
- `Template/IPE891/IPE891_Template.md` - IPE891 test case template

Standard test case sections:
- Test Case Title
- Preconditions (Licenses, Hardware Setup, Software/Firmware)
- Test Steps Table (Step | RT Steps / Input Data | Expected Result)
- Priority (High/Medium/Low)
- Coverage Expectations (Positive, Negative, Performance, Functional)

### Reference Documentation
Use markdown files in `help_document/` folder organized by product:

**XPI (X-Plugin) Documentation** (`help_document/XPI/`):
- `X-Plugin.md` - X-Plugin documentation
- `X-PlugIn_Testing_Documentation.md` - Testing standards
- `XPI_IPEmotion.md` - XPI IPEmotion integration
- `XPI_IPEmotion_PlugIn_IPETRONIK_X.md` - Technical specifications
- `XPI_Testing_Documentation.md` - XPI testing documentation

**IPEmotion Documentation** (`help_document/IPEmotion/`):
- `IPEmotion.md` - IPEmotion documentation
- `IPEmotion_Main.md` - Main documentation
- `IPEmotion_PlugIn_IPETRONIK_X.md` - Plugin specifications
- `IPEmotion_PlugIn_CAN_Protocols.md` - CAN protocol documentation
- `IPEmotion_PlugIn_Video.md` - Video plugin documentation
- `IPEmotion_Settings.md` - Settings and configuration
- `IPEmotion_Specification_Erweiterung.md` - Extension specifications
- `IPEmotion_Specification_Lastenheft.md` - Requirements specification

**IPEmotion RT Documentation** (`help_document/IPEmotionRT/`):
- `IPEmotionRT_IPEmotion.md` - RT Logger documentation
- `IPEmotionRT_Gateway_Use_Cases.md` - Gateway use cases
- `IPEmotionRT_M_Gateway3.md` - M-Gateway3 documentation
- `IPEmotionRT_Settings.md` - RT settings
- `IPEmotionRT_Video.md` - RT video features
- `IPEmotionRT_ETHERNET_Protocols.md` - Ethernet protocols
- Additional RT-specific documentation

**IPE891 Documentation** (`help_document/IPE891/`):
- `IPE891_Product_Requirement_Specification.md` - Product requirements
- `IPE891_Specification_COPYstation2_Product_Requirement_Specification.md` - COPYstation2 specs
- `IPE891_Specification_COPYstation2_TRS.md` - Technical requirements

**General Documentation** (`help_document/General/`) - Common reference for ALL projects:
- `product_highlights.md` - Product features and highlights across all IPETRONIK products

### Existing Test Cases Reference
Learn from existing test cases in:
- `Testcases/XPI/` - X-Plugin test cases
- `Testcases/IPEmotion/` - IPEmotion test cases
- `Testcases/IPEmotionRT/` - IPEmotion RT test cases
- `Testcases/IPE891/` - IPE891 test cases

## Test Coverage Best Practices

### Positive Testing
- Test normal/expected use cases with valid inputs
- Verify all documented features work as specified
- Test default configurations and standard workflows
- Validate successful completion messages and states

### Negative Testing
- **Invalid Inputs**: Wrong data types, out-of-range values, null/empty values
- **Boundary Conditions**: Min/max values, edge cases, limit testing
- **Error Scenarios**: Missing hardware, invalid configurations, connection failures
- **Permission Issues**: Unauthorized access, missing licenses, restricted operations
- **Data Validation**: Malformed data, special characters, encoding issues

### Edge Case Testing
- **Boundary Values**: Test at min, max, and just outside valid ranges
- **Special Values**: Zero, negative numbers, very large numbers
- **Empty States**: No devices detected, empty configurations, zero channels
- **Maximum Load**: Maximum number of channels/devices/connections
- **Timeout Scenarios**: Long-running operations, network delays

### Performance Testing
- Response time for device detection and synchronization
- Data acquisition rates and throughput
- Memory usage with maximum configurations
- CPU utilization during heavy operations
- Startup and initialization times

### Functional Testing
- Feature completeness per requirement
- Integration between modules and components
- Data flow and transformation accuracy
- UI/UX functionality and responsiveness
- Configuration persistence and loading

### Security Testing (IPE891, WebUI)
- Authentication and authorization
- Session management
- Input validation and sanitization
- Secure communication protocols
- Access control and permissions

### Regression Testing
- Verify existing features still work after changes
- Test backward compatibility with older firmware/software
- Validate configuration migration scenarios
- Check for side effects on related features

## Test Data Guidelines

### Specify Concrete Values
- Use specific numbers, not placeholders: "20 °C" not "[temperature value]"
- Define actual device IDs: "540123456" not "[device ID]"
- Include real version numbers: "v2.5.1" not "[version]"
- Provide measurable thresholds: "< 100ms" not "[acceptable time]"

### Include Test Variations
- Multiple valid input combinations
- Common error scenarios
- Typical production configurations
- Known problematic cases from past issues

### Module-Specific Testing Patterns

**M-THERMO Modules:**
- Test all thermocouple types (K, J, T, etc.)
- Verify temperature ranges and accuracy
- Test offset adjustment and calibration
- Validate cold junction compensation
- Check channel configuration options

**Sx-STG Modules:**
- Test IEPE sensor modes and excitation currents
- Verify bridge configurations (full/half/quarter)
- Test different voltage ranges
- Validate filter settings
- Check sampling rates

**CAN Interfaces:**
- Test different baud rates
- Verify message filtering
- Test error frame handling
- Validate network management features
- Check bus load scenarios

**License Management:**
- Test with valid licenses
- Test with expired licenses
- Test with missing licenses
- Verify license transfer/migration
- Check license limit enforcement

### Code Style
When suggesting code or scripts:
- Use clear, descriptive variable names
- Add comments for complex logic
- Follow Python PEP 8 style guidelines
- Use type hints where applicable

### Markdown Files
- Use proper heading hierarchy
- Format tables correctly
- Include code blocks with language identifiers
- Keep lines under 120 characters when possible

## Workflow

When generating test cases:
1. **Detect project** from ticket prefix or manual specification
2. **Read** appropriate template from `Template/` folder
3. **Reference** existing test cases in `Testcases/[Project]/` for formatting examples
4. **Reference** project-specific documentation from `help_document/[Project]/` folder
5. **Create test scenarios FIRST** - Before writing the test case:
   - Break down the requirement into testable scenarios
   - Identify all features/functions to be tested
   - List positive scenarios (happy paths)
   - List negative scenarios (error conditions, invalid inputs)
   - List edge cases (boundary values, limits, special conditions)
   - List performance scenarios (timing, throughput, resource usage)
   - List integration scenarios (component interactions)
   - Present scenarios to user for confirmation/feedback
6. **Analyze requirement** for all testing aspects:
   - Identify positive test scenarios
   - Determine negative test scenarios and error conditions
   - Consider edge cases and boundary values
   - Assess performance requirements
   - Review security implications (if applicable)
7. **Generate comprehensive test case** based on approved scenarios:
   - Include specific, measurable values (not placeholders)
   - Cover all test types: positive, negative, edge cases, performance
   - Add detailed expected results for each step
   - Include error messages and validation criteria
   - Specify hardware/software versions and configurations
8. **Validate completeness**:
   - All preconditions clearly defined
   - Test steps are actionable and unambiguous
   - Expected results are specific and measurable
   - Coverage includes multiple test types
   - Related issues and notes documented
9. **Save** in `Testcases/[Project]/` folder with proper naming

## Important Rules
- Never expose or reference internal file paths in user-facing content
- Always validate technical details against reference documentation
- **ALWAYS create test scenarios FIRST before writing test cases**
- Present scenarios to user for review before generating the full test case
- Ensure test cases are comprehensive and actionable
- Include specific values and measurable expected results (NO PLACEHOLDERS)
- Use ticket ID in filename when available
- Filter documentation based on detected project type
- Generate test steps for BOTH positive and negative scenarios
- Include boundary value testing where applicable
- Specify exact error messages expected in negative tests
- Add performance metrics when testing speed/throughput
- Cross-reference related test cases or known issues
