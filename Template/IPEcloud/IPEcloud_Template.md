# [Test Case ID] - [Test Case Title]

## Description
[Brief description of what this test case validates for IPEcloud]

## Pre-Condition

### Required Licenses:

**IPEcloud2:**
- [License name or "Not applicable"]

**IPEmotionRT Logger:**
- [License name or "Not applicable"]

### Hardware Setup:

| IPEmotion | IPEmotion RT |
|-----------|--------------|
| [Hardware requirements for IPEmotion PC or "Not applicable"] | [Hardware requirements for IPEmotionRT Logger or "Not applicable"] |

### Software Setup:

| IPEmotion | IPEmotion RT |
|-----------|--------------|
| [Software requirements for IPEmotion PC or "Not applicable"] | [Software requirements for IPEmotionRT Logger or "Not applicable"] |

### IPEcloud2 Setup:

| Admin.UI | Client.UI |
|----------|-----------|
| **Browser:** [Chrome/Firefox/Edge latest version]<br><br>**Login:** Open browser → Navigate to Admin UI URL → Login with super admin credentials<br><br>**User Setup:**<br>Left panel → Users → Click on create user → Add user window:<br>- First name → Insert: [Username]<br>- Last name → Insert: [Last name]<br>- E-mail → Insert: [email@domain.com]<br>- Password → Insert: [password]<br>- Create<br><br>**Device Setup:**<br>Left panel → Devices → Click on create device → Create a new device window:<br>- Name → Insert: [Device name]<br>- Serial → Insert: [Serial number]<br>- Type → Open dropdown → Select: [Logger type]<br>- External ID → Insert: [External ID]<br>- License → Open dropdown → Select: [License type]<br>- Automatic File upload → [check/uncheck]<br>- Create<br><br>**Organization Setup:**<br>Left panel → Select Landlord → Organization overview page → Click on create organization:<br>- Name field → Insert: [Organization name]<br>- Deployment region → Open dropdown → Select: [Region]<br>- Description → Insert: [Description]<br>- Enable Log File Analysis → Active: [check/uncheck]<br>- External ID → Insert: [External ID]<br>- Click on create<br><br>**Assign User to Organization:**<br>Organization overview page → Click on [Organization name] → Tab users → Click on '+' icon → Assign user to organization window:<br>- Email field → Insert: [email@domain.com]<br>- Role → Open dropdown → Select: [Admin/Write/Read/None]<br>- Assign<br><br>**Assign Device to Organization:**<br>Landlord → Organization overview page → Click on [Organization name] → Devices tab → Click on add device:<br>- Insert: [Serial number of logger]<br>- Assign | **Browser:** [Chrome/Firefox/Edge latest version]<br><br>**Login:** Open browser → Navigate to Client UI URL → Click on SSO Login → Sign in to your account window:<br>- Username or email → Insert: [email@domain.com]<br>- Password → Insert: [password]<br>- Sign in<br><br>[Additional client UI setup steps if needed] |

## Test Steps

| Step | Client.UI Steps / Input Data | Expected Result |
|------|------------------------------|-----------------|
| 1 | [Navigation path → Action → Input data] | [Specific expected outcome with details] |
| 2 | [Navigation path → Action → Input data] | [Specific expected outcome with details] |
| 3 | [Navigation path → Action → Input data] | [Specific expected outcome with details] |
| 4 | [Navigation path → Action → Input data] | [Specific expected outcome with details] |

**Note:** Use `→` to separate navigation steps. For Admin.UI actions, prefix with "Admin UI →". For Client.UI actions, prefix with "Client UI →".

**Example formats:**
- Admin UI → Left panel → Users → Click on create user
- Client UI → Dashboard → IPEstatus → Click on logger [serial number]
- Tab users → [email] → Click: Edit → Role → Open dropdown → Select: [Role] → Save

## Notes
- [Any additional notes or references]
- [User credentials and test data details]
- [Device serial numbers and configurations]
- [Organization setup requirements]
- [Clean-up instructions if needed]
- Reference: [IPEcloud User Manual Chapter or section]
- KD Item: [Item number if applicable]

## Priority
[High / Medium / Low]

## Coverage
- [ ] Positive Testing
- [ ] Negative Testing
- [ ] Performance Testing
- [ ] Functional Testing
