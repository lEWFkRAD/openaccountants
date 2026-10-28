# Ledger US-NC — verified 2026-10-28 (lane/A-us-big)

## Evidence used (archived in oa-correction-evidence/sources/, retrieved 2026-10-28)
- US-NC-open-2.pdf — NCDOR 2025 Form D-401 Individual Income Tax Instructions (pdftotext OK): TY2025 rate 4.25%; standard deduction chart ($12,750 S/MFS, $25,500 MFJ/QSS, $19,125 HOH, MFS=0 if spouse itemizes); Child Deduction Table (MFJ $3,000 up to $40k → $0 over $140k; HOH up to $30k → $0 over $105k; S/MFS up to $20k → $0 over $70k); Schedule S Line 3 bonus depreciation 85% add-back + 20%/yr reversal from TY2026; Line 4 §179 NC limits $25,000/$200,000, 85% add-back; due date April 15, 2026; failure-to-file 5%/mo max 25%; failure-to-pay 5%; 90% rule with extension; underpayment interest if $1,000+ after credits/withholding (D-422); federal extension auto-grants state extension (circle on D-400) else D-410.
- US-NC-open-3.pdf — 2025 Form NC-40 instructions: $1,000 threshold; quarterly Apr15/Jun15/Sep15/Jan15; Jan-31 exception; farmers/fishermen 2/3 rule; safe harbor = 25% of lesser of 90% current (66⅔% farmers), 100% prior (12-mo), or 90% annualized; NO 110%/$150k tier in NC.
- US-NC-open.pdf — D-400 Schedule S web-fill instructions page (near-empty text layer; low value).
- US-NC-nc40.jsp.html — NC-40 form landing page (usable, corroborates online payments).
- US-NC-employers.html — DES employers hub (links only; no 2026 wage-base numbers → SUI 2026 stays needs-sources).
- US-NC-index.html / direct-pay / refunds / modernized-e-file — IRS/EFTPS generic pages, not NC-specific (no needles).
- US-NC-index-2.html — NCDOR home page (motor fuel suspension notice; no PIT needles).

## Corrections made
- nc-payroll.md v→0.2: TY2025 PIT rate 4.5% → **4.25%** (D-401: "the individual income tax rate is 4.25%") in §2.1 heading, rate table, supplemental rate, and 3 worked examples (recomputed: $1,668.13/yr, $64.16/pp; $3,315 back-withholding, $331.50 penalty).
- nc-income-tax.md 0.1→0.2: child-deduction table expanded to all filing statuses with archived quote; §179 limits $25,000/$200,000 + 85%/20% mechanics quoted; bonus depreciation 85% add-back + 20%/yr reversal quoted; estimated threshold quote added; Tier-1 rules NC-T1-04/05/06 updated.
- nc-estimated-tax.md v→0.2: safe harbor rewritten to archived NC-40 text (removed wrong 110%/$150k federal-style tier); Jan-31 exception and $1,000 threshold now carry archived quotes.
- nc-return-assembly.md v→0.2: [VERIFY:] flags on std deduction, child deduction, $1,000 threshold, bonus add-back resolved as VERIFIED with archived citations.

## Unverified / carried
- SUI 2026 wage base and rate range: still needs-sources (DES hub has no numbers).
- Underpayment interest 7% Jan–Jun 2026: no archived interest memo this run; carried.
- TY2026 3.99% rate: Session Law 2023-134 citation kept; no archived statute.

## Validators
check-examples exit 0; build-index exit 0; validate-guides exit 0.
