---
pack: US-NE
jurisdiction: US-NE
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

# Nebraska (US-NE) -- pack map

Nebraska taxes individuals and corporations under Revenue Act Chapter 77 (Nebraska Legislature statutes, structure verified), runs employer income-tax withholding through the Department of Revenue with an annual **Income Tax Withholding Circular (Circular EN -- the 2026 and 2027 editions exist as official PDFs, verified)**, and offers a **pass-through entity (PTE) tax election** (official tax-credit page verified). Sales tax is state + local (pre-existing `ne-sales-tax.md`). Unemployment is administered by the Department of Labor (site returned 403 to this run's fetcher -- figures needs-sources).

## Domain map

| Domain | Status | File | Notes |
|---|---|---|---|
| IT-IND individual income | drafted (pre-existing) | `ne-income-tax.md` | 1040N |
| IT-CORP corporate income | drafted 2026-10-28 | `ne-corporate-income-tax.md` | Ch. 77 structure verified; rate table + Form 4-1120C needs-sources |
| VAT sales/use | drafted (pre-existing) | `ne-sales-tax.md` | state + local |
| SC social contributions | drafted 2026-10-28 | `ne-social-contributions.md` | NDOL administers; wage base/rates needs-sources (403 this run) |
| PR payroll withholding | drafted 2026-10-28 | `ne-payroll.md` | withholding page + Circular EN 2026/2027 verified; form IDs/frequencies needs-sources |
| TP transfer pricing | drafted 2026-10-28 | `ne-transfer-pricing.md` | PTE election verified; combined/addback posture needs-sources |
| XB cross-border | drafted 2026-10-28 | `ne-cross-border.md` | PTE rails verified; nonresident mechanics needs-sources |

All seven domains apply -- no not_applicable entries.

## Key sources (read 2026-10-28)

- DOR Income Tax Withholding: https://revenue.nebraska.gov/businesses/income-tax-withholding -- resolves (200), fetched; withholding rails and Circular EN reference verified
- Circular EN PDFs: https://revenue.nebraska.gov/sites/default/files/doc/forms/2026cir_en_whole.pdf and .../2027cir_en_whole.pdf -- official 2026/2027 withholding circulars (existence verified; text not parsed this run)
- DOR withholding forms index: https://revenue.nebraska.gov/about/forms/income-tax-withholding-forms -- resolves (200); form-number extraction needs-sources
- PTE tax: https://revenue.nebraska.gov/tax-credits/nebraska-pass-through-entity-tax-ptet -- official page verified (election exists)
- Revenue Act Chapter 77: https://nebraskalegislature.gov/laws/browse-chapters.php?chapter=77 -- fetched; §77-3513 (withholding) verified reachable
- NDOL (UI): https://nebraska.gov/labor -- portal resolves; employer UI pages returned 403 to this run's fetcher -- **needs-sources**

## Open items for reviewer

- Corporate rate table (the commonly cited two-band table) and Form 4-1120C identity; filing deadlines and estimate thresholds.
- Withholding form ID (941-N commonly cited) and deposit frequencies -- inside Circular EN, not parsed.
- UI wage base/rates (NDOL 403).
- Combined reporting posture (Nebraska is separate-company with addback provisions -- confirm) and nonresident mechanics.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for Nebraska questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
