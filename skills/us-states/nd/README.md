---
jurisdiction: US-ND
applicable: [IT-IND, IT-CORP, VAT, PR, SC, TP, XB]
not_applicable: []
---

# North Dakota (US-ND): tax pack

North Dakota levies a graduated individual income tax — 0.00% to $48,475 (single), 1.95% to $244,825, 2.50% above, verified from the Tax Commissioner's individual page on 2026-10-25 — and a graduated corporate income tax (1.41% / 3.55% / 4.31% brackets, N.D.C.C. § 57-38-30 per the existing `nd-corporate-tax` skill) with **no separate franchise or gross-receipts tax** and **no PTET election**. State and local sales tax is administered by the Tax Commissioner; unemployment insurance is the **only** state-level social contribution and is employer-only, administered by Job Service ND under N.D.C.C. Ch. 52-8. There is no state disability insurance, no paid-family-leave payroll tax, and no state-level employee social contribution of any kind.

**Source status (2026-10-25):** tax.nd.gov (individual brackets, estimated-tax interest, credit-for-tax-paid and mobilized-military credit pages) and jobsnd.com (UI taxable-wage-base formula, new-employer/experience-rating mechanics, construction risk protection) all verified HTTP 200 with real content. **ndlegis.nd.gov failed DNS (getaddrinfo) for every request on 2026-10-25** and the Justia mirror returned 403 — so all Century Code section text (57-38-30, 57-38.1-09/-15/-18/-19, Ch. 52-8) is carried from the existing skills with their own [VERIFY] flags and is marked **needs-sources** for statute-text confirmation. Also **needs-sources:** the 2026 ND UI taxable wage base and rate schedules (2025 base $45,100 corroborated by `nd-payroll`), 2026 penalty/interest percentages, water's-edge election timing, and the ND-1 nonresident proration mechanics. (not yet confirmed)

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND | nd-income-tax, nd-estimated-tax, nd-return-assembly | existing |
| IT-CORP | nd-corporate-tax | existing |
| VAT / sales | nd-sales-tax | existing |
| PR, payroll withholding | nd-payroll | existing |
| SC, social contributions (employer-only UI; no employee levy) | nd-social-contributions | source-cited draft |
| TP, transfer pricing (combined reporting, water's edge, apportionment) | nd-transfer-pricing | source-cited draft |
| XB, cross-border (nonresidents, reciprocity, military, credits) | nd-cross-border-tax | source-cited draft |

## Official sources

- ND Office of State Tax Commissioner — individual income tax (brackets, estimates): <https://www.tax.nd.gov/individual-income-tax> — 200 with text, 2026-10-25.
- ND Tax Commissioner — credit for income tax paid to another state: <https://www.tax.nd.gov/credit-income-tax-paid-another-state-or-local-jurisdiction> — 200, 2026-10-25.
- ND Tax Commissioner — site root (tax-type index incl. mobilized-military credit): <https://www.tax.nd.gov/> — 200, 2026-10-25.
- Job Service ND — unemployment business tax, learn about taxes (wage-base formula = 70% of statewide average annual payroll; new-employer mechanics): <https://www.jobsnd.com/unemployment-business-tax/learn-about-taxes> — 200 with text, 2026-10-25.
- Job Service ND — root and file-reports hub: <https://www.jobsnd.com/> — 200, 2026-10-25.
- N.D.C.C. Ch. 52-8, 57-38, 57-38.1 (statute text): **needs-sources** — ndlegis.nd.gov DNS failure 2026-10-25; re-verify before publication.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
