---
jurisdiction: US-NY
applicable: [IT-IND, IT-CORP, VAT, PR, SC, TP, XB]
not_applicable: []
---

# New York (US-NY): tax pack

New York levies a graduated individual income tax (4%–10.9%), an Article 9-A corporate franchise tax on the **highest of three bases** with a top business-income rate of **7.25%** (rate factor 0.0725 verified in the CT-3-A instructions PDF, 2026-10-25) and **combined filing on Form CT-3-A** for related corporations, state+local sales tax, and the MCTMT payroll tax inside the 12-county MCTD. It is one of the few states with **employee-side** social contributions: mandatory Paid Family Leave contributions (2025: 0.388% of gross wages, annual cap $354.53, NYSAWW $1,757.19 — verified on paidfamilyleave.ny.gov) and statutory disability insurance (SDI). Cross-border rules are unusually aggressive: the 183-day statutory-residency test plus the convenience-of-the-employer rule (20 NYCRR §132.18(a), cited in the existing `ny-income-tax` skill) tax nonresidents' remote-work wages.

**Source status (2026-10-25):** tax.ny.gov Article 9-A page (three bases, CT-3-A combined filing), CT-3/CT-3-A PDFs (0.0725 rate factor), paidfamilyleave.ny.gov/cost (PFL 2025 rate/cap/SAWW, waiver rules), tax.ny.gov IT-203 instructions PDF (convenience-of-the-employer test section) all verified HTTP 200 with real content. **needs-sources:** 2026 PFL rate/cap/SAWW (2026 calculator live but 2026 figures not yet in page text), SDI contribution figures (0.5%/$300/$1.50 — DFS/DOL/WFTC pages 404 or DNS-failed), 2026 UI schedule, NYS-45 instructions (404), Article 9-A statute text (Tax Law §§ 210-A/210-B/210-C/251), CT-4 installment percentages, and the 2026 penalty/interest schedule.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND | ny-income-tax, ny-estimated-tax | existing |
| IT-CORP | orchestrator `ny-corporate-franchise-article-9a` + this pack's ny-transfer-pricing; also nyc-ubt, ny-llc-filing-fee | existing |
| VAT / sales | ny-sales-tax, new-york-sales-tax | existing |
| PR, payroll withholding | orchestrator `ny-payroll`, `ny-pte-tax-ptet`; ny-mctmt in this folder | existing |
| XB, cross-border | ny-residency-leaving-new-york (+ residency content in ny-income-tax) | existing |
| SC, social contributions (PFL, SDI, UI, MCTMT overlay) | ny-social-contributions | source-cited draft |
| TP, transfer pricing (Article 9-A combined, receipts, intangibles) | ny-transfer-pricing | source-cited draft |

## Official sources

- NYS DTF — Article 9-A (three bases, CT-3-A combined filing): <https://www.tax.ny.gov/bus/ct/article9a.htm> — 200 with text, 2026-10-25.
- NYS DTF — CT-3-A instructions (7.25% factor): <https://www.tax.ny.gov/pdf/current_forms/ct/ct3ai.pdf> — 200 PDF, 2026-10-25.
- NYS DTF — CT-3-A form: <https://www.tax.ny.gov/pdf/current_forms/ct/ct3a.pdf> — 200 PDF, 2026-10-25.
- NYS DTF — combined group receipts: <https://www.tax.ny.gov/bus/ct/article9a_deriving_receipts.htm> — linked from Article 9-A page, 2026-10-25.
- NYS DTF — MCTMT hub: <https://www.tax.ny.gov/bus/mctmt/> — 200 with text, 2026-10-25.
- NY Paid Family Leave — Cost (2025 rate 0.388%, cap $354.53, NYSAWW $1,757.19): <https://paidfamilyleave.ny.gov/cost> — 200 with text, 2026-10-25.
- NYS DTF — IT-203 instructions (convenience of the employer): <https://www.tax.ny.gov/pdf/current_forms/it/it203i.pdf> — 200 PDF, 2026-10-25.
- NYS DTF — nonresident FAQs: <https://www.tax.ny.gov/pit/file/nonresident-faqs.htm> — 200, 2026-10-25.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
