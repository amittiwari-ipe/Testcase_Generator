# IPETRONIK Test Case Generation - Quick Reference

**Efficient test case generation for IPETRONIK products. Full details in `TESTCASE_CREATION_WORKFLOW.md`**

---

## SCOPE VALIDATION

**SUPPORTED:** XPI (XPI-*) | IPEmotion (IM-*) | IPEmotionRT (TD4-*) | IPE891 (vvHLP-*) | IPEcloud (FLEET-*)

**If out of scope:** "Sorry, support is not available for this request. This assistant is for IPETRONIK test case generation only."

---

## PROJECT QUICK REFERENCE

| Prefix | Project | Template Path | Doc Path |
|--------|---------|---------------|----------|
| **XPI-** | X-Plugin (Hardware) | `Template/XPI/` | `help_document/XPI/` |
| **IM-** | IPEmotion (Software) | `Template/IPEmotion/` | `help_document/IPEmotion/` |
| **TD4-** | IPEmotionRT (Logger) | `Template/IPEmotionRT/` | `help_document/IPEmotionRT/` |
| **vvHLP-** | IPE891 (COPYstation2) | `Template/IPE891/` | `help_document/IPE891/` |
| **FLEET-** | IPEcloud (Cloud) | `Template/IPEcloud/` | `help_document/IPEcloud/` |

**Doc TOC:** See `HELP_DOCUMENT_TOC.md` for chapter references.

---

## SCENARIO TEMPLATE (Phase 1)

**File:** `01_Scenarios_[TICKET-ID].md` - **Create this FIRST, wait for approval**

```markdown
# Test Scenarios for [TICKET-ID] - [Title]

## Requirement Summary
[2-3 sentences]

## Test Scenarios
### Scenario 1: [Name]
**Description:** [What to test]
**Estimated Test Cases:** [N]
**Coverage:** Positive, Negative, Functional

[Repeat for each scenario]

## Total: [N] test cases across [X] scenarios
```

---

## FILE NAMING & FOLDER STRUCTURE

| Project | Test Case Format |
|---------|------------------|
| XPI | `XPI-[ID]-[##]_Description.md` |
| IPEmotion/RT/cloud | `TC_[###]_Description.md` |
| IPE891 | `IPE891-[ID]_Description.md` |

**Folder:**
```
Testcases/[Project]/[TICKET-ID]/
  ├── 01_Scenarios_[TICKET-ID].md ⚠️ CREATE FIRST
  ├── [TC-ID]_Description.md  (after approval)
```

---

## ⚡ MANDATORY WORKFLOW

### Phase 1: CREATE SCENARIOS FIRST ⚠️
1. **Validate scope** → Identify project → Load template
2. **Create** `01_Scenarios_[TICKET-ID].md`
3. **STOP** → Show message:
   ```
   ✅ Created test scenarios for [TICKET-ID]
   Location: Testcases/[Project]/[TICKET-ID]/01_Scenarios_[TICKET-ID].md
   
   Scenarios: [list]
   Total: [N] test cases estimated
   
   ⏸️ Please review and reply "approved" to proceed with test cases.
   ```

### Phase 2: CREATE TEST CASES (ONLY AFTER APPROVAL)
4. **Wait** for explicit user approval
5. **Generate** detailed test cases
6. **Deliver** to `Testcases/[Project]/[TICKET-ID]/`

**⚠️ NEVER skip Phase 1. NEVER create test cases without approval.**

---

## EFFICIENCY RULES

### DO:
✅ Create all test cases in batch (multi-file creation)
✅ Use templates from `Template/[Project]/` folders
✅ Be specific with values and expectations
✅ Check ticket prefix to identify project first
✅ Reference documentation from `help_document/[Project]/`

### DON'T:
❌ Skip scenario creation and approval step
❌ Use vague language or approximations
❌ Miss hardware part numbers (for XPI)
❌ Answer questions about non-IPETRONIK projects

---

## 📚 DETAILED REFERENCES

**For complete information:**
- **Templates & Examples:** `Template/[Project]/` folders
- **Step-by-Step Workflow:** `TESTCASE_CREATION_WORKFLOW.md`
- **Documentation Index:** `HELP_DOCUMENT_TOC.md`
- **Project Best Practices:** See TESTCASE_CREATION_WORKFLOW.md sections 4-7
- **Quality Standards:** TESTCASE_CREATION_WORKFLOW.md section 8

**Key Quality Rules:**
- Navigation: Use → separator (File → Import → PCAP)  
- Expected Results: Be specific, measurable (not "correct" or "works")
- Part Numbers: Always include for hardware (623-500, 542xxxxx format)
- References: Cite doc chapters/sections

---

**This file is streamlined for performance. Full details, examples, and patterns are in referenced documents:**
- `TESTCASE_CREATION_WORKFLOW.md` - Complete workflow with examples
- `HELP_DOCUMENT_TOC.md` - Documentation chapter index
- `Template/[Project]/` - Project-specific templates and formats

