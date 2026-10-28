---
name: gi-property-stamp-duty
description: Prepare an ordinary Gibraltar property conveyance stamp-duty calculation, separating the whole-property value test from consideration bands and excluding unverified relief eligibility.
version: "0.2"
jurisdiction: GI
tax_year: 2026
last_updated: 2026-10-28
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Gibraltar ordinary property conveyance stamp duty

**Source-cited draft. Independent review pending.** Scope: ordinary conveyances, without buyer relief or special duty. This is not a complete property-tax Guide.

## Statutory calculation

Schedule 1 distinguishes whole-property value from consideration. For ordinary conveyances:

| Whole-property value | Duty on consideration |
|---|---|
| Up to £200,000 | Zero |
| Above £200,000 through £350,000 | 2% on first £250,000; 5.5% on excess |
| Above £350,000 | 3% on first £350,000; 3.5% on next £450,000; 4.5% above £800,000 |

These are alternative schedules, not one continuous marginal table. First/second-buyer treatment has separate eligibility and bands. Special duty and affordable-housing exemptions require separate examination. [Stamp Duties Act 2005, ss19A–19C and Schedule 1, pp28–29; accessed 22 October 2026](https://www.gibraltarlaws.gov.gi/legislations/stamp-duties-act-2005-1262/download).

## Worked boundary checks

Assume value equals consideration, with no relief or special duty:

- £200,000: £0.
- £250,000: £5,000.
- £350,000: £5,000 + £5,500 = £10,500.
- £400,000: £10,500 + £1,750 = £12,250.
- £900,000: £10,500 + £15,750 + £4,500 = £30,750.

The £200,000 exemption is not a universal deductible slice.

## Working-paper evidence

Record the instrument date, parties, consideration, independently supported whole-property value and legal character of the transaction. Ask the reviewer to confirm the chosen Schedule 1 category before using the arithmetic. Do not substitute the cash paid at completion for the entire consideration without examining the contract.

Attach a copy of the executed instrument or proposed execution version to the calculation. Keep valuation support separate from financing documents. Reconcile the calculation's consideration to the contract and explain any difference from the valuation. This is our preparation workflow, not an assertion that every listed document is a prescribed filing attachment.

## Scope remaining

Relief eligibility, mortgages, leases, indirect property investments, gifts, exemptions, electronic filing, payment timing and penalties are not computed here. Do not reuse this table for those transactions. A reviewer must check current amendments and the actual facts before filing or paying. No accountant attestation is claimed.

> Contributed by Ryan Duguid.

## Recomputing examples

```oa-check
name: GI SD on 300,000 GBP: 2% first 250,000 + 5.5% excess
inputs:
  price: 300000
steps:
  - b1: min(price, 250000) * 0.02
  - b2: max(min(price, 350000) - 250000, 0) * 0.055
  - duty: b1 + b2
expected:
  b1: 5000.00
  b2: 2750.00
  duty: 7750.00
```
```oa-check
name: GI SD on 900,000 GBP: 3% first 350,000 + 3.5% next 450,000 + 4.5% above 800,000
inputs:
  price: 900000
steps:
  - b1: min(price, 350000) * 0.03
  - b2: (min(price, 800000) - 350000) * 0.035
  - b3: max(price - 800000, 0) * 0.045
  - duty: b1 + b2 + b3
expected:
  b1: 10500.00
  b2: 15750.00
  b3: 4500.00
  duty: 30750.00
```

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Sources

- Stamp Duties Act 2005 (Gibraltar), ss19A-19C and Schedule 1

_Sources listed from citations already present in the guide; as_of: 2026-10-28; unverified against archived evidence._
