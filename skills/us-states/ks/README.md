---
pack: US-KS
jurisdiction: US-KS
applicable:
  - IT-IND
  - IT-CORP
  - VAT
  - SC
  - PR
  - TP
  - XB
not_applicable: {}
as_of: 2026-10-28
---

# Kansas (US-KS) — pack map

Kansas taxes individuals on a **two-bracket progressive rate** (5.20%–5.58% per the pre-existing skill, 2024+ rate structure — confirm against K.S.A. 79-32-110: needs-sources), corporations on a flat rate on Kansas-source income (Form K-120; the KDOR Corporate Income page confirms filing duty, S-corp auto-status, bank privilege-tax carve-out, and that the franchise tax is repealed for tax year 2011+), and sales at 6.5% state plus local. Employer social contributions are UI-only (KDOR Labor Services); there is no state disability or paid-leave program. Withholding follows the federal duty: any payor who must withhold federal tax from payments to Kansas residents must also withhold Kansas tax.

## Domain map

| Domain | Status | File | Notes |
|---|---|---|---|
| IT-IND individual income | drafted (pre-existing) | `ks-income-tax.md` | K-40, two-bracket, sole-proprietor focus |
| IT-CORP corporate income | drafted 2026-10-28 | `ks-corporate-income-tax.md` | K-120 duty + S/bank rules verified from KDOR; rate + combined-report form needs-sources |
| VAT sales/use | drafted (pre-existing) | `ks-sales-tax.md` | 6.5% state + local |
| SC social contributions | drafted 2026-10-28 | `ks-social-contributions.md` | UI-only; wage base/rates needs-sources (dol.ks.gov 403 to plain HTTP) |
| PR payroll withholding | drafted 2026-10-28 | `ks-payroll.md` | K-4 + KW-3 verified as live PDFs; rate-schedule mechanics needs-sources |
| TP transfer pricing | drafted 2026-10-28 | `ks-transfer-pricing.md` | no standalone TP documentation regime; related-party/combined mechanics needs-sources |
| XB cross-border | drafted 2026-10-28 | `ks-cross-border.md` | K-40PN/Schedule S routing; no reciprocity, no exit tax — needs-sources |

All seven domains apply to Kansas — no not_applicable entries (franchise tax repealed 2011 is noted in the corporate skill, not a domain).

## Key sources (read 2026-10-28)

- KDOR Corporate Income page: https://www.ksrevenue.gov/bustaxtypescorp.html (filing duty; S auto-status; banks file privilege tax; federal extension honored, 90% must be paid by due date to avoid late-payment penalty)
- KDOR Franchise page: https://www.ksrevenue.gov/bustaxtypesfranchise.html (no franchise tax for tax year 2011 and after; SOS $55 annual-report fee)
- KDOR Withholding page: https://www.ksrevenue.gov/bustaxtypeswh.html (withhold for KS residents wherever working and nonresidents working in KS; federal-payor rule extends to Kansas)
- K-4 form PDF: https://www.ksrevenue.gov/pdf/k-4.pdf (verified PDF, 2026-10-28)
- KW-3 e-file specs: https://www.ksrevenue.gov/pdf/KW-3ECSV.pdf (verified link on KDOR withholding page)
- K.S.A. 79-32-110 (corporate rates) / 79-32-150 (nonresident returns) / 79-27-105 (UI rates): https://www.kslegislature.org/li/b2025_26/statutes/2025_79-32-110/ — **page returns a JS shell with no server-side statute text to plain HTTP; all statute figures carried as needs-sources**
- KDOR UI (dol.ks.gov): 403 Forbidden to plain HTTP this run — UI figures needs-sources

## Open items for reviewer

- 2026 corporate rate and brackets (K.S.A. 79-32-110) and the combined-report requirement/form (K-120M).
- 2026 UI taxable wage base, contribution-rate ranges, new-employer rate (K.S.A. 79-27-105; dol.ks.gov blocked).
- Withholding percentage-schedule mechanics; KW-3 due date (last day of January per practice — verify).
- Nonresident allocation detail (Schedule S Part B) and K-40PN form ID.
- Related-party addback / combined-report statutory basis (K.S.A. 79-32.140 series — verify numbering).

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Kansas questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
