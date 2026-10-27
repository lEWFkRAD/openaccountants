---
name: gd-payroll-withholding
description: >
  Grenada payroll withholding (PAYE) reference for 2026. Covers employer
  registration under Income Tax Act Cap. 149 Fourth Schedule, the 30% deduction
  rate with the EC$60,000 accumulation trigger, Comptroller-directed rates for
  multi-employment and non-resident employees, net-of-tax gross-up, the 7-day
  monthly remittance deadline, employer personal liability for failed
  deductions, and 2% monthly interest on unpaid deductions. Use for Grenada
  payroll compliance and employer exposure reviews. Independent accountant
  review pending.
jurisdiction: GD
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Grenada payroll withholding (PAYE) v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows; not reviewed for any specific person's facts. Do not file, pay, or take a position on it without review by a qualified Grenadian professional.

## 1. Scope and sources

PAYE is administered under the Income Tax Act Cap. 149, s.54 and the Fourth Schedule ("Deduction of Tax by Employers"), consolidated PDF read 2026-10-27 ([Grenada Parliament](https://grenadaparliament.gd/wp-content/uploads/2021/08/Cap149-INCOME-TAX-ACT.pdf); chapter page [laws.gov.gd](https://laws.gov.gd/index.php/chapters/i-144-155/425-chapter-149-income-tax-act)). This skill is the employer-side duty map; the employee's annual charge is `gd-income-tax`; NIS contributions are `gd-social-contributions`; non-resident employment payments under s.51 are `gd-cross-border`.

**Source status caveat:** consolidated text to Act No. 2 of 2010; 2011–2026 amendments not retrievable in consolidated form on 2026-10-27. The Fourth Schedule in the consolidated text uses a flat 30% deduction (para 2(1)) — **needs-sources:** confirm no amendment replaced it with graduated PAYE bands; the IRD G-TAX FAQ (read 2026-10-27) confirms PAYE is one of the three monthly G-TAX taxes and cites an EC$3,000 monthly / EC$36,000 annual individual benchmark.

## 2. Who applies

- **Every employer except the Government of Grenada** paying remuneration must deduct tax (s.54(1)) and must **register as an employer within 30 days** of becoming one (Fourth Schedule para 1(2)); address changes and cessation also within 30 days (para 1(3)).
- **Representative employers** (agents paying on behalf of non-resident employers, estates, etc.) carry the same duties (para 10; s.2 definition read 2026-10-27).
- **Employees** are jointly exposed: where the employer failed to deduct, the employer is personally liable (para 6(1)) and may recover from the employee (para 6(3)).

## 3. Rates and base

| Item | Amount | Source |
|---|---|---|
| PAYE deduction | **30%** of chargeable remuneration | Fourth Schedule para 2(1), consolidated PDF read 2026-10-27 |
| Accumulation trigger | once accumulated remuneration reaches **EC$60,000** in the basis period, the excess is deducted at 30% for the remainder of the period | para 2(2) |
| Multi-employment or non-resident employee | amount **directed by the Comptroller** | paras 2(4)–(5) |
| Any other case | Comptroller-directed | para 2(6) |

**Base:** "remuneration" as defined in the Fourth Schedule (para 12) — wages, salaries, allowances, perquisites; NIS employee contributions are a separate charge (`gd-social-contributions`). Net-of-tax contracts are grossed-up under para 4 (see Example 2 in `gd-income-tax`).

## 4. Deadlines

- **Remit deducted PAYE within 7 days after the end of the month** in which it was deductible (s.96(a)/(e), consolidated PDF read 2026-10-27).
- **Monthly return** of deductions and remittances (para 8) and **annual return within 2 months after the calendar year end** (para 9); deficiencies must be accounted for (para 9(3)).
- **Certificates** of remuneration and tax deducted on request within 7 days (para 5(2)).
- G-TAX is the filing/payment channel for PAYE from the 2024 tax year ([IRD G-TAX FAQ](https://www.ird.gd/gtax/index.html), read 2026-10-27).

## 5. Penalties and interest

- **2% per month or part-month** interest on deducted-or-deductible PAYE not paid within the s.96 time (s.97(1)); that interest is the employer's own debt and **cannot be recovered from the employee** (s.97(2)).
- **Failure to deduct:** employer personally liable for the amount plus any penalty (para 6(1)); Comptroller may absolve where earlier/later deductions covered the tax (para 6(4)).
- **Recovery:** Crown debt routes under ss.98–105; unpaid deducted tax is a debt due to Government (para 3(b)).
- Late/incorrect returns: ss.111–112 penalties with s.114 notice.

## 6. Cross-border

- **Non-resident employees:** where a Grenada business pays employment income to a non-resident that it deducts in computing business income, s.51 requires withholding at the Third Schedule rate (15%) within 7 days — this sits beside, not inside, Fourth Schedule PAYE; Comptroller-directed PAYE (para 2(5)) applies where the non-resident is instead within the employment charge. Flag both paths to the reviewer. **needs-sources:** which route governs which non-resident employment fact pattern post-2010.
- **Accrued-but-unpaid** non-resident employment income: advance payment of the withholding when the business return is filed (s.51(2)).
- Foreign-address payees are presumed non-resident (s.50(4) analogue for payments; apply the same evidence discipline to payroll).

## 7. Worked examples

**Example 1 — monthly PAYE deduction.** Employee monthly remuneration EC$4,000, single Grenada employment.

```oa-check
name: monthly PAYE at 30 percent
inputs:
  remuneration: 4000
  rate: 0.30
steps:
  - paye: remuneration * rate
expected:
  paye: 1200
```

Remit 1,200 within 7 days after month-end via G-TAX; issue the para 5 certificate on request.

**Example 2 — failed deduction, employer exposure.** Employer paid EC$6,000 monthly remuneration for one month without deducting; the failure is discovered one month late.

```oa-check
name: employer liability plus one month interest
inputs:
  remuneration: 6000
  rate: 0.30
  interest_monthly: 0.02
steps:
  - failed_tax: remuneration * rate
  - interest_1m: failed_tax * interest_monthly
expected:
  failed_tax: 1800
  interest_1m: 36
```

The employer owes 1,800 plus 36 interest (recoverable from the employee only for the tax, not the interest — s.97(2)).

## 8. Ask the client

- Are all employers registered and are G-TAX monthly PAYE returns reconciled to payroll registers (para 8)?
- Any employees with second jobs or non-resident status — has a Comptroller direction been obtained?
- Any net-of-tax salary promises — gross-up exposure quantified?
- Accumulated-remuneration tracking for anyone approaching EC$60,000 in the year.
- Certificate issuance practice (para 5) — employees must attach certificates to any return.

## 9. Sources

- [Income Tax Act Cap. 149 consolidated PDF — s.54, ss.51, 96–98, Fourth Schedule paras 1–12](https://grenadaparliament.gd/wp-content/uploads/2021/08/Cap149-INCOME-TAX-ACT.pdf) — read 2026-10-27
- [Cap. 149 chapter page, laws.gov.gd](https://laws.gov.gd/index.php/chapters/i-144-155/425-chapter-149-income-tax-act) — read 2026-10-27
- [IRD G-TAX FAQ (PAYE on G-TAX, thresholds)](https://www.ird.gd/gtax/index.html) — read 2026-10-27
- [IRD filing-deadline extension press release, 31 March 2026 (PDF)](https://www.finance.gd/docs/2026/PRESS_RELEASE-IRD_Extension.pdf) — read 2026-10-27

<!-- openaccountants-cta-block -->

**Talk to a verified accountant** — this skill is a source-cited draft (tier 2). For Grenada payroll compliance under professional review, book time with an OpenAccountants verified accountant: [Calendly](https://www.openaccountants.com).
