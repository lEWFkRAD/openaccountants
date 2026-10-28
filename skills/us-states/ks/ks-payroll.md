---
name: ks-payroll
description: >
  Use this skill whenever asked about Kansas payroll withholding for tax
  year 2026 — Form K-4 employee withholding allowance certificate, KW-3
  annual withholding reconciliation (due January 31), KW-5 deposit reports
  with the five statutory filing frequencies ($200/$1,200/$8,000/$100,000
  thresholds), the KDOR rule that any payor who must withhold federal tax
  from payments to Kansas residents must also withhold Kansas tax, and
  default withholding when no K-4 is on file. Trigger on "Kansas
  withholding", "K-4", "KW-3", "KW-5", "KDOR withholding", "Kansas W-2".
  Corrected 2026-10-28 against archived KDOR FAQ, Pub. KW-100 (full text
  incl. percentage tables), and KW-3 e-file specs.
jurisdiction: US-KS
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - ks-income-tax
---

# Kansas payroll withholding v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Covers Kansas income-tax withholding by employers and other payors. **Source status:** corrected 2026-10-28 against archived KDOR documents: the Withholding FAQ statutory frequency table (`SRC-US-KS-DORE-faqs-withholding.html`), **Pub. KW-100 Kansas Withholding Tax Guide** (`SRC-US-KS-DORE-kw100-guide.pdf`, pdftotext-verified incl. percentage tables), **KW-3 e-file specs** (`SRC-US-KS-DORE-kw3especs.pdf`: "All 2025 KW-3Es must be filed by January 31, 2026"), KW-110 duty notice (`SRC-US-KS-DORE-kw110.pdf`), and the K-4 info page (`SRC-US-KS-DORE-k4info.html`). Governing act: **K.S.A. 79-3294 et seq.** (Kansas Withholding and Declaration of Estimated Tax Act, per KW-110).

## 2. Who applies

- **Employers must withhold Kansas tax** for (a) Kansas residents, whether services are performed inside or outside Kansas, and (b) nonresidents performing services in Kansas (KDOR Withholding page + KW-110 duty notice, archived).
- **Non-wage payors**: "Any employer or payor who must withhold Federal Income Tax from payments other than wages made to Kansas residents must also withhold Kansas Tax" (KDOR Withholding page, verified quote) — this sweeps in 1099 backup-type withholding, pensions/annuities/deferred income, interest and dividends, and lottery/gambling winnings when federal withholding applies (KW-100, archived).
- **Registration**: withhold employers must file the Kansas business tax application **CR-16** before the first wage payment (KW-110, archived).
- **No K-4 on file**: employer must withhold **at the single rate with no allowances** (K-4 info page, archived).
- **No reciprocity**: Kansas has no withholding reciprocity agreement with neighboring states (structural; needs-sources for a citation).

## 3. Mechanics and rates

| Item | Rule | Source |
|---|---|---|
| Employee certificate | Kansas Form K-4 (allowances; "married" allowance optional — spouses may claim "single" for two-earner joint accuracy; dependents counted once; extra flat-dollar withholding allowed) | archived `SRC-US-KS-DORE-k4info.html` |
| Default | single, zero allowances, if no K-4 | verified |
| Computation methods | **percentage formula** (rate tables on net wage after allowances) or **wage-bracket tables**; above the last bracket of a wage table the percentage formula is mandatory | Pub. KW-100, archived PDF text verified |
| Allowance value (TY2025+ tables) | withholding allowance tied to K.S.A. 79-32,121 exemptions: **$2,320/allowance**, $9,160 single / $18,320 married equivalent | KW-100 text + `SRC-US-KS-79-32121.html` |
| Deposit frequency (KW-5) | **Annual** ≤ $200/yr (due Jan 25); **Quarterly** $200.01–$1,200 (25th after quarter close); **Monthly** $1,200.01–$8,000 (15th of following month); **Semi-Monthly** $8,000.01–$100,000 (1st–15th due 25th; 16th–end due 10th next month); **Quad-Monthly** ≥ $100,000.01 (within 3 banking days of the 7th/15th/21st/last day; EFT required). Frequency changes effective Jan 1 | KDOR Withholding FAQ statutory table, archived |
| KW-5 | required for **every** period even with zero withholding; annual filers still file an annual KW-5 (KW-3 does not replace it); file + pay electronically | KW-100, archived |
| E-filing mandate | W-2/KW-3 magnetic media no longer accepted; **51+ employees/payees must e-file** | `SRC-US-KS-DORE-kw3especs.pdf` |
| Annual reconciliation | **KW-3** annual withholding return + W-2s/1099s | verified |

## 4. Deadlines

- K-4: complete at hire or when taxable payments begin; review annually and on marital/allowance changes (k4info page, archived).
- Periodic deposits (KW-5): per the frequency table above (archived FAQ).
- **KW-3 + W-2/1099 annual reconciliation: January 31** of the following year ("The annual return, W-2s and 1099s are due by January 31 of the following year" — KW-100; "All 2025 KW-3Es must be filed by January 31, 2026" — KW-3 e-file specs).

## 5. Penalties and interest

- Failure to withhold/pay over: employer liable for the tax plus penalties under the withholding act (K.S.A. 79-3294 et seq.) — specific tier percentages **needs-sources** (the old 79-32,173 was repealed in 1988; current penalty sections not yet archived).
- **Worker misclassification**: "Penalties may be imposed on persons who knowingly and intentionally mis-classify an employee as an independent contractor and fail to report state income tax withholding or unemployment insurance contributions" (KW-100, archived quote).
- Employment-tax delinquency program: KDOR maintains an Employment Tax Delinquencies page (verified in KDOR navigation); enforcement detail **needs-sources**.

## 6. Cross-border interactions

- Resident-employee rule means Kansas withholding follows the **employee's residence** even for work performed out of state — multi-state employers must not net this against other states' nonresident withholding without credit analysis (see `ks-cross-border`).
- Nonresident employees working in Kansas: withhold Kansas; their home state may credit Kansas tax.
- W-2 state box reporting: single-state reporting per wage-source rules; e-file specs verified.

## 7. Worked examples

**Example 1 — deposit frequency band check:** employer withholds $9,500 annually; margin above the monthly band's $8,000 cap and below the semi-monthly $100,000 cap (semi-monthly band applies; Jan 1–15 deposit due January 25, Jan 16–31 due February 10 — archived KDOR FAQ table).

```oa-check
name: KS withholding frequency band
inputs:
  annual_wh: 9500
  m_top: 8000
  sm_top: 100000
steps:
  - over_monthly_band: annual_wh - m_top
  - headroom_under_semimonthly_cap: sm_top - annual_wh
expected:
  over_monthly_band: 1500
  headroom_under_semimonthly_cap: 90500
```

**Example 2 — percentage-formula allowance credit:** employee claims 2 allowances on K-4; monthly payroll period. What allowance amount is deducted from gross before applying the rate tables?

```oa-check
name: KS K-4 allowance deduction
inputs:
  allowances: 2
  per_allowance: 2320
steps:
  - annual_credit: per_allowance * allowances
  - monthly_credit: annual_credit / 12
expected:
  annual_credit: 4640
  monthly_credit: 386.6666666666667
```

## 8. Ask the client

- Are K-4s on file for every Kansas-withholding employee (default single-zero surprises are common)?
- Resident employees working remotely from other states — Kansas withholding still required on residents.
- Non-wage payors (contractor payments to Kansas residents) — Kansas withholding duty mirrors federal.
- E-file readiness: KCSC portal, KW-3E/W-2 spec formats.

## 9. Sources

1. **KDOR Withholding FAQ — statutory filing-frequency table** (annual/quarterly/monthly/semi-monthly/quad-monthly thresholds and due dates): https://www.ksrevenue.gov/faqs-withholding.html — archived `SRC-US-KS-DORE-faqs-withholding.html`, fetched 2026-10-28.
2. **Pub. KW-100 Kansas Withholding Tax Guide** (KW-3/W-2/1099 due Jan 31, KW-5 every period, percentage formula vs wage-bracket tables, $2,320 allowance, misclassification penalty quote, EFT/e-file rules): https://ksrevenue.gov/pdf/kw100.pdf — archived `SRC-US-KS-DORE-kw100-guide.pdf`, pdftotext verified.
3. **KW-3/W-2 e-file specifications** ("All 2025 KW-3Es must be filed by January 31, 2026"; 51+ e-file mandate; no magnetic media): https://www.ksrevenue.gov/pdf/KW-3ECSV.pdf — archived `SRC-US-KS-DORE-kw3especs.pdf`.
4. **KW-110 withholding duty notice** (resident/services-in-Kansas rule, CR-16 registration, K.S.A. 79-3294 et seq.): https://www.ksrevenue.gov/pdf/kw-110.pdf — archived `SRC-US-KS-DORE-kw110.pdf`.
5. **K.S.A. 79-32,121** (personal exemptions $9,160/$18,320/$2,320 feeding the tables): archived `SRC-US-KS-79-32121.html`.
6. KDOR Withholding (duty, non-wage payor rule): https://www.ksrevenue.gov/bustaxtypeswh.html — archived `SRC-US-KS-DORE-withholding-page.html`.
7. KDOR K-4 information (allowance design, single-zero default, exempt-status verification): https://www.ksrevenue.gov/k4info.html — archived `SRC-US-KS-DORE-k4info.html`.

**Needs-sources:** current withholding penalty tier percentages (79-32,173 repealed 1988; successor sections not yet archived), reciprocity citation, exact K.A.R. frequency-assignment regulation.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Kansas payroll questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
