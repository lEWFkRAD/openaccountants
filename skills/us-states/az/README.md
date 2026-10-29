---
jurisdiction: US-AZ
applicable: [IT-IND, IT-CORP, VAT, PR, SC, TP, XB]
not_applicable: []
covered_by:
  IT-IND: az-income-tax
  VAT: az-transaction-privilege-tax
  PR: az-payroll
---

# Arizona (US-AZ): tax pack

Arizona runs a flat **2.5%** individual income tax (A.R.S. Title 43) and a flat **4.9%** corporate income tax with a **$50 minimum** (A.R.S. §43-1111, text read 2026-10-27). There is no state franchise or gross-receipts tax on top of income tax; the sales-tax equivalent is the **Transaction Privilege Tax (TPT)**, a tax on the seller's privilege, plus local city/county TPT licenses. Corporate multistate income is apportioned under a Uniform Division of Income Tax Act structure (§§43-1131 to 43-1149) with property, payroll and sales factors (§§43-1141/43-1143/43-1145 read 2026-10-27); unitary groups file combined and affiliated groups may consolidate (§43-947, cited in §43-1132(D)). Employer social contributions centre on Arizona unemployment insurance (wage base and rates per the existing `az-payroll` skill). Returns are due the **15th day of the 4th month** after year-end; estimates due the 15th of the 4th, 6th, 9th and 12th months (ADOR corporate page, read 2026-10-27). Interest on under/overpayments tracks IRC §6621 (federal short-term + 3%), compounded annually (ADOR interest-rate page, read 2026-10-27).

**Source status (2026-10-27):** azdor.gov corporate-income-tax page, azdor.gov interest-rates page, and azleg.gov §§43-1111, 43-1126, 43-1131, 43-1132, 43-1133, 43-1134, 43-1141, 43-1143, 43-1145, 43-1146, 43-1151, 43-1201, 43-1231, 43-1361, 43-1362 all verified HTTP 200 with real content. **needs-sources:** the §43-1142 property-factor exception text and §43-1144 sales-factor exceptions (azleg 404 on those paths this run), §43-941/43-947 combined/consolidated statute text, the current AZ UI wage-base/rate schedule (des.az.gov SSL-timed-out), the §43-323 e-file mandate text, and the current penalty schedule (late-filing percentage).

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | az-income-tax | existing |
| IT-CORP, corporate income tax | az-corporate-income-tax | source-cited draft |
| VAT / sales (TPT) | az-sales-tax, az-transaction-privilege-tax | existing |
| PR, payroll withholding | az-payroll | existing |
| SC, social contributions (AZ UI, comp-insurance overlay) | az-social-contributions | source-cited draft |
| TP, transfer pricing (unitary combined, factors, consolidation) | az-transfer-pricing | source-cited draft |
| XB, cross-border (nonresidents, PTE, tax clearance) | az-cross-border | source-cited draft |

## Official sources

- AZDOR — Corporate Income Tax (forms, due dates, estimates, e-file): <https://azdor.gov/business/corporate-income-tax> — 200 with text, 2026-10-27.
- AZDOR — Corporate Tax Forms hub: <https://azdor.gov/forms/corporate-tax-forms> — 200 with text, 2026-10-27.
- AZDOR — Interest Rates (IRC §6621 + 3%, annual compounding, 2026 quarterly table): <https://azdor.gov/business/interest-rates> — 200 with text, 2026-10-27.
- A.R.S. §43-1111 — Tax rates for corporations (4.9%, $50 minimum): <https://www.azleg.gov/ars/43/01111.htm> — 200 with text, 2026-10-27.
- A.R.S. §43-1126 — S-corporation treatment and return: <https://www.azleg.gov/ars/43/01126.htm> — 200 with text, 2026-10-27.
- A.R.S. §43-1131 — Definitions (UDITA): <https://www.azleg.gov/ars/43/01131.htm> — 200 with text, 2026-10-27.
- A.R.S. §43-1132 — Taxpayers liable; allocation/apportionment; §43-947 affiliated groups: <https://www.azleg.gov/ars/43/01132.htm> — 200 with text, 2026-10-27.
- A.R.S. §43-1133 — Taxability in another state: <https://www.azleg.gov/ars/43/01133.htm> — 200 with text, 2026-10-27.
- A.R.S. §43-1134 — Allocation of nonbusiness income: <https://www.azleg.gov/ars/43/01134.htm> — 200 with text, 2026-10-27.
- A.R.S. §43-1141 — Property factor (cost; rented at 8× net annual rent): <https://www.azleg.gov/ars/43/01141.htm> — 200 with text, 2026-10-27.
- A.R.S. §43-1143 — Payroll factor: <https://www.azleg.gov/ars/43/01143.htm> — 200 with text, 2026-10-27.
- A.R.S. §43-1145 — Sales factor: <https://www.azleg.gov/ars/43/01145.htm> — 200 with text, 2026-10-27.
- A.R.S. §43-1146 — Situs of tangible-personal-property sales (delivery test): <https://www.azleg.gov/ars/43/01146.htm> — 200 with text, 2026-10-27.
- A.R.S. §43-1151 — Tax clearance on cessation of corporate activities: <https://www.azleg.gov/ars/43/01151.htm> — 200 with text, 2026-10-27.
- A.R.S. §43-1201 — Organizations exempt from tax: <https://www.azleg.gov/ars/43/01201.htm> — 200 with text, 2026-10-27.
- A.R.S. §43-1231 — Unrelated business income taxed under §43-1111: <https://www.azleg.gov/ars/43/01231.htm> — 200 with text, 2026-10-27.
- A.R.S. §43-1361/§43-1362 — Estate tax-clearance certificate: <https://www.azleg.gov/ars/43/01361.htm>, <https://www.azleg.gov/ars/43/01362.htm> — 200 with text, 2026-10-27.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
