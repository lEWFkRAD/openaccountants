---
name: fl-cross-border
description: >
  Use this skill whenever asked about Florida cross-border taxation
  for tax year 2026 — the corporate nexus standard under Ch. 220
  ("doing business, earning or receiving income in this state"),
  Public Law 86-272 solicitation protection (15 U.S.C. s.381), the
  absence of a Florida individual income tax and what that means for
  nonresidents and departing residents, credits for taxes paid to
  other states under s. 220.13, and reemployment-tax nexus for
  remote employers. Trigger on "Florida nexus", "Florida corporate
  income tax other state", "PL 86-272 Florida", "Florida
  nonresident", "moving to Florida taxes", "Florida credit for taxes
  paid". Source-cited draft; Ch. 220 statute text read 2026-10-27.
jurisdiction: US-FL
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - fl-corporate-income-tax
---

# Florida cross-border (nexus, non-residents, other-state taxes) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Florida's cross-border profile is unusual among US states: because there is **no individual income tax**, "non-resident" questions for individuals collapse to corporate and payroll questions. The corporate tax reaches every "taxpayer" by, among other things, "conducting business, earning or receiving income in this state" (s. 220.11(1), statute text read 2026-10-27). This skill covers corporate nexus, PL 86-272, the other-state-tax addback/credit interplay in s. 220.13, and the reemployment-tax side of remote work. **Source status:** ss. 220.11, 220.13 statute text read 2026-10-27 (flsenate.gov, 200); DOR nexus guidance pages not fetched this run — flagged **needs-sources** where cited.

## 2. Who applies

- **Out-of-state C-corporations** with Florida nexus: Florida's statutory hook is broad — "doing business, earning or receiving income in this state" (s. 220.11(1)). There is no bright-line economic-nexus dollar threshold in the statute text read this run; DOR applies facts-and-circumstances plus factor-based apportionment (confirm current DOR nexus guidance: **needs-sources**).
- **Foreign (non-US) corporations**: same Ch. 220 reach; federal ECI rules gate the treaty analysis, Florida conforms to federal starting point (s. 220.13).
- **Individuals moving to/from Florida**: no Florida income tax follows the mover in either direction — the old residence state may still tax for part-years; Florida itself imposes none (see `fl-moving-to-florida-domicile`).
- **Remote employers**: Florida reemployment tax attaches to Florida employment regardless of where the employer sits (see `fl-social-contributions`).

## 3. Rates and base

| Item | Amount / rule | Source |
|---|---|---|
| Corporate rate on Florida-apportioned net income | 5.5% (s. 220.11(2)(a)) | flsenate.gov, read 2026-10-27 |
| Apportionment to Florida | 50% sales / 25% property / 25% payroll (s. 220.15(1)) | flsenate.gov, read 2026-10-27 |
| Individual nonresident income tax | none — Florida has no individual income tax | structural; no FL PIT statute exists |
| Credit for taxes paid to other states | interplay via s. 220.13(1)(a)1.a.-b. addback/credit mechanics | flsenate.gov, read 2026-10-27 |
| PL 86-272 protection | federal bar on net-income tax for pure order-solicitation of tangible goods | 15 U.S.C. §381 |

Base: only Florida-apportioned adjusted federal income is taxed; a nexus-but-no-Florida-factor company can land at a zero or near-zero apportionment percentage.

## 4. Deadlines

- F-1120 (or F-1120-N) follows the federal return due date; e-filing is mandatory where the federal return must be e-filed (s. 220.21(2), read 2026-10-27).
- No Florida part-year or nonresident individual return exists (no PIT).
- Reemployment quarterly RT-6 for employers with Florida employees (see `fl-social-contributions`).

## 5. Penalties and interest

Ch. 220 penalties/interest (ss. 220.25–220.27): section text not extracted this run — **needs-sources** for percentages. Common failure modes: (1) an out-of-state company assuming no Florida exposure while its sales factor grows — Florida nexus is statutory-conduct based, not threshold based; (2) claiming PL 86-272 for services, digital, or in-state fulfillment, which exceed "solicitation of orders of tangible personal property"; (3) departing residents assuming their old state's tax disappears automatically — it does not; (4) remote employers missing Florida reemployment duty for Florida-based staff.

## 6. Cross-border interactions

- **PL 86-272** (15 U.S.C. §381) protects only solicitation of orders for tangible personal property shipped from outside Florida; it does not shield services, digital goods, or in-state inventory fulfillment.
- **Other-state PTE taxes:** where an entity pays another state's pass-through entity tax, Florida resident members have no Florida credit to claim (no FL PIT); the federal §164 deduction/SALT-cap analysis governs instead.
- **Foreign parents:** no Florida-specific treaty or ECI provisions beyond federal conformity; treaty relief is federal-level only.
- **Combined-reporting states:** a group combined elsewhere still files Florida on the entity/statutory-fraction basis unless it elects Florida consolidation (s. 220.131).

## 7. Worked examples

A Texas corporation (no Florida property or payroll) has $3,000,000 of Florida-apportioned adjusted federal income for 2026:

```oa-check
name: FL corporate tax on apportioned income
inputs:
  apportioned: 3000000
  rate: 0.055
steps:
  - tax: apportioned * rate
expected:
  tax: 165000.00
```

The same company's only Florida activity is soliciting tangible-goods orders shipped from Texas (PL 86-272 protected):

```oa-check
name: PL 86-272 protected
inputs:
  apportioned: 3000000
  rate: 0.055
  protected: 1
steps:
  - tax: apportioned * rate * (1 - protected)
expected:
  tax: 0.00
```

## 8. Ask the client

- What Florida contacts exist — employees, agents, inventory, fulfillment, trade shows — and do they cross "doing business / earning income in this state"?
- Is the activity pure tangible-goods solicitation (PL 86-272) or services/digital/fulfillment?
- For inbound movers: has the old state been formally exited (domicile, statutory-day rules), since Florida itself will not tax them?
- For remote employers: are Florida-based employees registered for Florida reemployment tax?

## Sources

1. s. 220.11 Fla. Stat. (tax imposed; nexus language): https://www.flsenate.gov/Laws/Statutes/2025/220.11 (200, statute text read 2026-10-27)
2. s. 220.13 Fla. Stat. (adjusted federal income; other-state tax addback/credit): https://www.flsenate.gov/Laws/Statutes/2025/220.13 (200, statute text read 2026-10-27)
3. s. 220.15 Fla. Stat. (apportionment): https://www.flsenate.gov/Laws/Statutes/2025/220.15 (200, statute text read 2026-10-27)
4. s. 220.21 Fla. Stat. (returns; e-file mandate): https://www.flsenate.gov/Laws/Statutes/2025/220.21 (200, statute text read 2026-10-27)
5. 15 U.S.C. §381 (Public Law 86-272): https://www.law.cornell.edu/uscode/text/15/381 (200 with text, 2026-10-27)
6. FL DOR nexus guidance: not fetched this run — **needs-sources**

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Florida nexus and cross-border questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
