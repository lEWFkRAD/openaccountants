---
name: wi-transfer-pricing
description: >
  Use this skill whenever asked about Wisconsin combined reporting and
  transfer pricing for tax year 2026 — the three combined-group tests
  (commonly controlled group with the >50% voting-power test, unitary
  business, water's edge), the designated agent filing Form 6 instead of
  separate Forms 4, entities that can never join a combined group (S corps,
  REITs, RICs, REMICs, FASITs), intercompany transaction elimination inside
  the group, and the 80%-active-foreign-business-income water's edge rule.
  Trigger on "Wisconsin combined return", "Wisconsin Form 6", "WI unitary",
  "commonly controlled group Wisconsin", "water's edge Wisconsin",
  "Wisconsin designated agent", "Wisconsin combined reporting".
  Source-cited draft; 2025 Form 4 instructions (IC-100, R. 10-25) PDF read
  2026-10-27 — combined-group sections quoted; Wis. Stat. § 71.255 and Tax
  2.61 cited as summarized in IC-100.
jurisdiction: US-WI
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - wi-corporate-income-tax
---

# Wisconsin combined reporting / transfer pricing v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows. Not reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified Wisconsin professional.

## Who this applies to

Wisconsin is a **mandatory combined-reporting** state: a corporation that meets the three tests does **not** file its own Form 4 — the group's **designated agent files Form 6** for the whole combined group. Intercompany transactions vanish inside the group, which resolves most transfer-pricing friction but pulls losses, credits and foreign affiliates into scope.

**Source status (as_of 2026-10-27):** [2025 Form 4 instructions IC-100 (R. 10-25)](https://www.revenue.wi.gov/TaxForms2025/2025-Form4-inst.pdf) fetched as PDF and read — the three tests, the 50% test, unitary-business indicators, water's edge, and excluded entities are quoted from it. It summarizes **Wis. Stat. § 71.255(1)(c)** and **Wis. Admin. Code Tax 2.61(3)**; the underlying statute text was not separately fetched this run — flagged where relied on. Form 6 instructions not read — **not yet confirmed** for election-consistency and combined-schedule mechanics.

### 2. Who applies

A corporation is in a **combined group** if it meets **all three tests**:

1. **Test 1 — commonly controlled group** (§ 71.255(1)(c), Tax 2.61(3)): parent-subsidiary chains, common-owner corporations, family-owned corporations, or stapled entities, meeting the **50% test** — common ownership of stock representing **more than 50% of voting power**, direct or indirect (IRC § 318 attribution for indirect).
2. **Test 2 — unitary business**: integrated, interdependent enterprises contributing to one another's operations — IC-100 indicators: centralized purchasing/marketing/advertising/accounting/R&D; intercorporate sales or leases; intercorporate services (admin, data, HR, insurance, tax, legal, financial).
3. **Test 3 — water's edge**: the corporation is not excluded by the water's edge rules.

**Never in a combined group** (must file separate returns): **S corporations, REITs, RICs, REMICs, FASITs.**

## 3. Rates and base

| Item | Amount / rule | Source |
|---|---|---|
| Combined tax rate | **7.9%** on the group's combined apportioned base (Form 6) | IC-100, read 2026-10-27 |
| ED surcharge | 3% of combined tax, min $25 / max $9,800 (per group) | IC-100, read 2026-10-27 |
| Filing | Designated agent files **Form 6**; members do not file separate Forms 4 | IC-100, read 2026-10-27 |
| 50% test | >50% voting power, direct or indirect (§ 318 attribution) | IC-100 summarizing Tax 2.61(3)(d), read 2026-10-27 |
| Water's edge | Applies where a company derives **80%+ of worldwide gross income from active foreign business income** (subchapter N sources, active trade/business abroad); subsidiary = ≥50% voting **and** ≥50% value | IC-100, read 2026-10-27 |
| Intercompany | Dividends, interest, rents, royalties, service fees eliminated inside the group | combined-return mechanics — Form 6 instructions **not yet confirmed** |
| Apportionment | Single sales factor at group level (schedules A-01…A-09) | IC-100, read 2026-10-27 |

### 4. Deadlines

| Filing | Due |
|---|---|
| Form 6 | Federal due date; WI extension = 30 days after federal extended date (automatic) |
| Designated agent designation | With the Form 6 for the year — Form 6 instructions not yet confirmed |
| Combined member additions/departures | Year of change — not yet confirmed |

### 5. Penalties and interest

- Same corporate regime as Form 4: **18% per year interest**, civil penalties up to 100% of unreported tax, criminal exposure for false returns (IC-100, read 2026-10-27).
- **AUDIT FLASH POINT**: failing to combine when the three tests are met — family groups and stapled structures routinely miss Test 1's indirect/attribution rules; DOR re-billing plus 18% interest is the standard assessment pattern. (not yet confirmed)

### 6. Cross-border

- **Water's edge** is the group's foreign boundary: the 80%-active-foreign-income company and its foreign subsidiaries sit outside the combined group; their dividends/royalties then become **intercompany payments to non-members** — elimination stops and DOR scrutiny starts. (not yet confirmed)
- US subsidiaries of foreign parents combine normally unless the water's edge test pulls the parent chain out.
- Compare Pennsylvania (elective combined + § 7337 addback, `pa-transfer-pricing`) and Ohio (CAT consolidated/affiliated choice, `oh-transfer-pricing`).

### 7. Worked examples

**Example A — combined group nets a member loss.**

```oa-check
name: Form 6 combined base with loss member
inputs:
  member_a_wi_income: 900000
  member_b_wi_income: -250000
  rate: 0.079
steps:
  - combined_base: member_a_wi_income + member_b_wi_income
  - tax: combined_base * rate
  - ed: min(max(tax * 0.03, 25), 9800)
  - total: tax + ed
expected:
  combined_base: 650000
  tax: 51350.00
  ed: 1540.50
  total: 52890.50
```

Separate Forms 4 would have paid 71,100 + surcharge on A alone and banked a B loss — combining is usually the win when a member runs a loss.

**Example B — water's edge flips a royalty from eliminated to deductible-scrutiny.**

```oa-check
name: Royalty to foreign affiliate after water's edge exclusion
inputs:
  combined_base_before: 650000
  royalty_to_excluded_affiliate: 120000
  rate: 0.079
steps:
  - base_if_deducted: combined_base_before - royalty_to_excluded_affiliate
  - tax_if_deducted: base_if_deducted * rate
expected:
  base_if_deducted: 530000
  tax_if_deducted: 41870.00
```

Once the affiliate is outside the water's edge, the royalty leaves the group — DOR then tests the pricing against arm's-length standards (the 9,480.00 swing shown is exactly what that audit targets).

### 8. Ask the client

- Map ownership with § 318 attribution — family groups miss the >50% voting test constantly.
- Unitary indicators: shared services, intercompany leases/sales — document both directions.
- Any member with 80%+ active foreign business income? That's the water's edge line. (not yet confirmed)
- S corps/REITs in the structure: they file separately no matter what.
- Who is the designated agent, and is the designation consistent year to year?

### 9. Sources

- [2025 Form 4 instructions IC-100 (R. 10-25)](https://www.revenue.wi.gov/TaxForms2025/2025-Form4-inst.pdf) — PDF read 2026-10-27 (three tests, 50% test, unitary indicators, water's edge, excluded entities, penalties)
- Wis. Stat. § 71.255; Wis. Admin. Code Tax 2.61 — cited as summarized in IC-100 (statute text not separately fetched 2026-10-27) (not yet confirmed)
- `wi-corporate-income-tax` (this pack) — rate/surcharge; `pa-transfer-pricing`, `oh-transfer-pricing` — state contrasts
- **not yet confirmed:** Form 6 instructions (designation, consistency, combined schedules M-W); § 71.255 full text; combined NOL/credit rules.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Wisconsin combined-return and unitary-group questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

## Rates, bands and thresholds

Not yet confirmed against archived sources.

## The taxable base

Not yet confirmed against archived sources.

## Deadlines and filing

Not yet confirmed against archived sources.

## Penalties and interest

Not yet confirmed against archived sources.

## Cross-border points

Not yet confirmed against archived sources.

## Worked examples

Not yet confirmed against archived sources.

## Ask the client first

Not yet confirmed against archived sources.

## Sources

Not yet confirmed: figures in this skill lack archived line-citations.


| Source | URL | Read on |
| --- | --- | --- |
| (see Not yet confirmed) | — | 2026-10-28 |

Not yet confirmed against archived sources.

## Talk to a verified accountant

Not yet confirmed against archived sources.
