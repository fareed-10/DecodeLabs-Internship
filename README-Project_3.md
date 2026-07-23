# DecodeLabs
# Project 3: Phishing Awareness Analysis
### DecodeLabs Industrial Training | Batch 2026

## 📌 Overview
This project focuses on the **detection phase** of cybersecurity — analyzing sample messages to identify phishing attempts, listing red flags, and explaining why each message is unsafe. It also includes a non-expert triage checklist and decision tree for handling suspicious messages.

**Key Skills:** Threat analysis, awareness of cyber attacks, security thinking

---

## 🎣 Sample Message Analysis

### Sample 1 — Mass Phishing (Fake Account Alert)

**From:** Amazon Security `<security@amaz0n-support.com>`
**Subject:** Your account has been suspended — action required

> Dear Customer, we detected unusual sign-in activity on your account. Your account will be permanently suspended in 24 hours unless you verify your identity. Click here to verify: `hxxp://amaz0n-account-verify.com/login`

**Suspicious links/keywords:** `amaz0n-support.com`, `amaz0n-account-verify.com` (lookalike domains)

| # | Red Flag | Detail |
|---|----------|--------|
| 1 | Typosquatted domain | "amaz0n" uses a zero instead of "o" |
| 2 | Urgency/fear trigger | "24 hours", "permanent suspension" |
| 3 | Generic greeting | "Dear Customer" instead of real name |
| 4 | Sender-domain mismatch | Not a real amazon.com address |

**Why unsafe:** Classic typosquat + false deadline built to trigger a click before the user thinks it through — a mass-phishing credential-harvesting attempt.

---

### Sample 2 — Spear Phishing (Internal IT Impersonation)

**From:** IT Support `<it-helpdesk@decodelabs-tech.support.com>`
**Subject:** FW: Mandatory — Password expires in 24 hrs

> All employee passwords must be reset today. Reset now: `hxxp://decodelabs.tech.password-reset.io/reset`

**Suspicious links/keywords:** `decodelabs.tech.password-reset.io` — true root domain is `password-reset.io`, with `decodelabs.tech` used as a fake subdomain

| # | Red Flag | Detail |
|---|----------|--------|
| 1 | Subdomain trap | Real domain buried as a subdomain of an unrelated root |
| 2 | Sender-domain mismatch | Sent from an external lookalike domain |
| 3 | Urgency | "before it expires" |
| 4 | No personalization | Addressed to "Team" |

**Why unsafe:** Reading the URL right-to-left reveals it's owned by an external party, not the real company — a spear-phishing credential-harvesting attempt.

---

### Sample 3 — Whaling / BEC (Executive Wire Transfer)

**From:** CEO – Strictly Confidential `<ceo.urgent@executive-update.com>`
**Subject:** IMMEDIATE ACTION REQUIRED: Transfer Authorization

> Please process the attached wire transfer instructions immediately and bypass standard procedure. Strictly confidential — do not discuss with anyone.

| # | Red Flag | Detail |
|---|----------|--------|
| 1 | Authority impersonation | Poses as the CEO |
| 2 | Secrecy demand | "Strictly confidential," "don't discuss" |
| 3 | Bypass request | Skip normal finance procedure |
| 4 | Unavailability excuse | "Can't take calls" prevents verification |
| 5 | Sender-domain mismatch | Random external domain, not the real company |

**Why unsafe:** A Business Email Compromise (BEC)/whaling attempt combining authority, urgency, and secrecy to bypass verification and authorize a fraudulent wire transfer.

---

## ✅ Non-Expert Triage Checklist

**Step 1 — Sender Check**
- [ ] Does the display name match the actual email address?
- [ ] Is the domain spelled exactly right?

**Step 2 — Content Check**
- [ ] False urgency ("act now," "24 hours," "account locked")?
- [ ] Asked to bypass a process or keep something secret?
- [ ] Requests passwords, MFA codes, or payment changes?

**Step 3 — Link/Attachment Check**
- [ ] Does the hovered link match the visible text?
- [ ] Unusual file types (.iso, .js, .scr)?
- [ ] Unexpected QR code?

**Step 4 — Verification**
- [ ] Can the request be confirmed via a separate, known channel?

**Step 5 — Decision**
- No flags → **Close**
- 1–2 flags → **Warn User / Verify Further**
- 3+ flags or direct credential/money request → **Block & Escalate**

---

## 🌳 Decision Tree

Incoming Suspicious Message
                          │
    ┌─────────────────────┼─────────────────────┐
    │                     │                     │
 SAFE                SUSPICIOUS              MALICIOUS
    │                     │                     │
    ▼                     ▼                     ▼
 CLOSE               WARN USER              BLOCK DOMAIN
                    (verify via a           & ESCALATE
                     separate channel)      (report, don't
                                              just delete)

---

## 🔑 Key Takeaway

Phishing succeeds by exploiting the gap between a technical control and a human reaction. All red flags covered above exist to short-circuit normal verification instincts. The fix is always the same:

**Pause → Verify (via a separate channel) → Report**

---
*Submitted as part of DecodeLabs Cyber Security Industrial Training — Project 3*                                              
