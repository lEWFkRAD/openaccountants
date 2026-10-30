---
name: nc-transfer-pricing
description: >-
  Use when a North Carolina corporate group has related-party interest,
  royalty, or intangible flows and needs the 2026 answer: the mandatory net
  interest addback to a related member under N.C.G.S. § 105-130.5(25), the
  royalty reporting option under § 105-130.7A, single-sales-factor
  apportionment with the alternative-apportionment escape hatch under
  § 105-130.4(t1), and combined reporting on Form CD-405. Trigger on North
  Carolina addback, related member interest, 105-130.5, royalty option
  105-130.7A, NC combined return CD-405, NC intangibles. Source-cited
  draft; 130.5(25), 130.7A and 130.4(t1) text verified 2026-10-25.
jurisdiction: US-NC
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-25
version: 0.1
---

# North Carolina transfer pricing (addbacks, royalty option, combined reporting)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

C corporations filing North Carolina Form CD-405 that are members of a controlled group with intercompany interest, royalty, or intangible flows -- especially structures routing IP or financing through a low- or no-tax state or a foreign affiliate. North Carolina polices connected-party income three ways: (1) a **mandatory addback** of net interest expense paid to related members, (2) an **election-based royalty regime**, and (3) **combined reporting** for affiliated groups on Form CD-405. S corporations are outside the corporate income tax (G.S. 105-130.3) but remain in franchise-tax scope.

## Rates, bands and thresholds

## Core rules and rates

- **Net interest addback (mandatory).** State net income adds back "the amount of net interest expense to a related member" to the extent deducted for federal purposes -- N.C.G.S. § 105-130.5(25), statute text verified 2026-10-25. There is no "same unitary combination" exception written into (25) itself; back-to-back and conduit analysis follows NCDOR administrative practice. _(§ 105-130.5(25))_
- **Royalty reporting option.** § 105-130.7A gives taxpayers an option concerning the method by which royalty payments to related members are reported; § 105-130.5 cross-references "royalty payments required to be added by G.S. 105-130.7A, to the extent deducted in calculating federal taxable income." Electing the option changes whether royalties are added back or the underlying income is included. _(§ 105-130.7A; § 105-130.5)_
- **Corporate rate for 2026: 2%.** G.S. 105-130.3 schedule, verified 2026-10-25: 2025 → 2.25%; 2026 → 2%; 2028 → 1%; after 2029 → 0%. Addback income is taxed at these rates, so the dollar bite shrinks each year of the phase-out. _(§ 105-130.3)_
- **Single-sales-factor apportionment** with market-based sourcing; the **alternative apportionment** escape hatch (§ 105-130.4(t1)) lets the Secretary modify the factor when the standard factor does not fairly reflect NC activity -- the tool NCDOR uses against engineered IP/servicing footprints. _(§ 105-130.4, text verified 2026-10-25)_
- **Combined reporting.** Affiliated groups file the combined return (Form CD-405 combined) -- corroborated by the `nc-corporate-tax` skill; the controlling combined-reporting statute section was **not located on ncleg.gov on 2026-10-25: not yet confirmed**.

## The taxable base

## Base and adjustments

Start from federal taxable income (after the corporate rate applies to state net income):

1. **Add** § 105-130.5(25) net interest expense to related members (mandatory).
2. **Add or re-scope** royalties per § 105-130.7A election status.
3. **Apportion** by the single sales factor (§ 105-130.4), subject to (t1) modification.
4. Franchise tax runs on the apportioned capital base in parallel (§ 105-122, $1.50 per $1,000) -- addbacks do not change the franchise base.

## Deadlines and filing

## Deadlines

- CD-405 combined income and franchise return: 15th day of the 4th month after year end (Apr 15 calendar filers); extension to Nov 15 by timely application.
- CD-429 estimated payments: four installments (Apr 15, Jun 15, Sep 15, Dec 15) -- installment mechanics verified in § 105-163.15 text, 2026-10-25.
- Fiscal-year filers blend the rate by days in each calendar year (NCDOR proration table).

## Penalties and interest

- Underpayment of estimated installments: interest runs from each installment due date to the earlier of payment or Apr 15 of the following year (§ 105-163.15(c) mechanics, verified 2026-10-25).
- Late filing/failure to file: standard Chapter 105 penalties (5% per month up to 5%, plus interest) -- exact current schedule in NCDOR bulletin; **not yet confirmed** for the 2026 published rate.
- Addback positions are a named NCDOR audit focus; documentation of the related-member's state of residence and its inclusion in another state's combined report is the standard defense file.

## Cross-border points

## Cross-border and federal overlay

- Foreign related members: the (25) addback applies to interest to related members regardless of residence; treaty analysis is federal (see federal skills).
- Double-taxation relief: if the related member included the interest in another state's combined or separate report, NCDOR recognizes offsetting inclusion in practice -- keep both states' returns in the file.
- Federal §163(j) limits shrink the federal deduction and therefore the addback amount (the addback is "to the extent deducted").

## Worked examples

**Example 1 -- mandatory interest + royalty addback, 2026.** NC C-corp pays $400,000 royalties and $100,000 net interest to a related member in a no-income-tax state. Both are deducted federally. 2026 rate 2%.

```oa-check
name: nc addback 2026
inputs:
  royalty: 400000
  interest: 100000
  rate: 0.02
steps:
  - addback: royalty + interest
  - tax: addback * rate
expected:
  addback: 500000
  tax: 10000.00
```

(Interest addback is mandatory under (25); the royalty treatment depends on the 130.7A election -- this example assumes the addback branch.)

**Example 2 -- fiscal-year blended rate.** FY Jul 1 2025 – Jun 30 2026, $500,000 state net income after addbacks. 184 days in 2025 (2.25%), 181 days in 2026 (2%).

```oa-check
name: nc fiscal-year blended rate
inputs:
  income: 500000
  days2025: 184
  days2026: 181
  r2025: 0.0225
  r2026: 0.02
steps:
  - blend: (r2025 * days2025 + r2026 * days2026) / (days2025 + days2026)
  - tax: round(income * blend, 2)
expected:
  blend: 0.0213
  tax: 10630.14
```

## Ask the client first

1. Who is the related member, where is it taxed, and is it in another state's combined report?
2. Is the debt thin or excessive relative to the operating entity's equity (conduit/debt-equity recharacterization risk)?
3. Has the group made (or does it want) the § 105-130.7A royalty election?
4. Where are the IP, the financing, and the employees -- will § 105-130.4(t1) alternative apportionment be triggered?
5. Fiscal-year filers: is the blended-rate proration table applied?

## Sources

| Source | URL | Read on |
|---|---|---|
| N.C.G.S. § 105-130.5 (State net income; (25) related-member net interest addback) : | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.5A.html | 2026-10-25 |
| N.C.G.S. § 105-130.7A (royalty income reporting option): | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.7A.html | 2026-10-25 |
| N.C.G.S. § 105-130.3 (corporate rate schedule): | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.3.html | 2026-10-25 |
| N.C.G.S. § 105-130.4 (apportionment; (t1) alternative): | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-130.4.html | 2026-10-25 |
| N.C.G.S. § 105-163.15 (estimated installments): | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html | 2026-10-25 |

Not yet confirmed: Combined-reporting statutory authority (Form CD-405 combined): not located on ncleg.gov 2026-10-25; corroborated by `nc-corporate-tax` skill (read 2026-10-25) 2026 NCDOR penalty-rate schedule

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
