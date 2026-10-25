---
jurisdiction: US-GA
applicable: [IT-CORP, VAT, PR, TP, XB]
not_applicable:
  SC: "Georgia imposes no state-level social contributions on employees; FICA/FUTA are federal (skills/federal), and Georgia UI + Administrative Assessment are employer-only contributions covered by the `ga-payroll` skill (PR)."
---

# Georgia (US-GA): tax pack

Georgia levies a flat individual income tax (4.99% for tax years beginning on or after 1 January 2026, HB 463, signed 2026, reducing from 5.19% for 2025), a corporate income tax at the same flat rate, a separate graduated net worth tax (capped at $5,000), state sales tax (4% state rate plus local options), and employer withholding plus Georgia Unemployment Insurance administered by the Georgia Department of Labor (GDOL) — a different agency from the Department of Revenue (DOR). There is no state-level social-contribution regime for employees.

**Source status:** DOR booklets (IT-511, IT-611), HB 463 text, the DOR withholding page and the GDOL employer tax PDF all verified HTTP 200 on 2026-10-24. The 2026 GDOL rate notice (Form DOL-626: 2026 experience rates, wage-base confirmation, Administrative Assessment rate) did **not** resolve from the drafting environment — 2026 UI rate figures are **needs-sources**; the $9,500 wage base (unchanged since 2013) and 2.70% new-employer rate are corroborated by the GDOL employer PDF. The HB 111 (2025) signed-bill PDF link returned 404 on 2026-10-24; the 5.19% 2025 rate is corroborated by the 2025 IT-611 booklet and the 2026 withholding guide tables.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND | ga-income-tax, georgia-individual-tax-return-form-500 | existing |
| IT-CORP | ga-corporate-and-ptet, georgia-corporate-income-tax-returns-form-600, ga-net-worth-tax | existing |
| VAT / sales | ga-sales-tax, ga-contractor-and-manufacturing-sales-tax | existing |
| PR, payroll withholding | ga-payroll | existing |
| TP, transfer pricing (related-member addbacks) | ga-transfer-pricing-addbacks | source-cited draft |
| XB, cross-border (nonresidents, composite, P.L. 86-272) | ga-cross-border-tax | source-cited draft |
| SC, social contributions | not applicable — see frontmatter | — |

## Official sources

- 2025 IT-511 individual booklet: <https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download> — PDF 200 on 2026-10-24.
- 2025 IT-611 corporate booklet: <https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download> — PDF 200 on 2026-10-24.
- HB 463 (2026) enrolled text: <https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download> — PDF 200 on 2026-10-24.
- DOR withholding hub: <https://dor.georgia.gov/withholding> — 200 on 2026-10-24 (2026 Employer's Withholding Tax Guide, revised September 2026, is published from this hub).
- GDOL employer tax reporting PDF: <https://dol.georgia.gov/document/unemployment-tax/unemployment-insurance-tax-reporting-and-liability-information-employers/download> — PDF 200 on 2026-10-24.
- 2026 GDOL rate notice (Form DOL-626) — **needs-sources** (not reachable 2026-10-24).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
