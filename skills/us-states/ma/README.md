---
jurisdiction: US-MA
applicable: [IT-IND, IT-CORP, VAT, PR, SC, TP, XB]
not_applicable: []
---

# Massachusetts -- OpenAccountants Tax Skills

**Source status (2026-10-29):** the DFML PFML contribution-rate page and the DOR Elective Pass-through Entity Excise page were re-fetched and archived with content on 2026-10-28/29; the combined-reporting statute (M.G.L. c.63 §32B), the S-corp net-income measure (§32D), the excise rate section (§39) and 830 CMR 63.00 (Secretary of the Commonwealth regulation PDF) were archived from malegislature.gov / sec.state.ma.us. mass.gov form/guide pages (Form 1-NR/PY) and the malegislature.gov c.63D chapter page remained 403/404 from this environment; those items sit on each skill's "Not yet confirmed" line.

**Open question:** `maine-sales-tax.md` and `maryland-sales-tax.md` sit in this folder -- likely misfiled; flagged for separate cleanup, not touched by this pack.

## Official sources

- DFML PFML contribution rates: <https://www.mass.gov/info-details/family-and-medical-leave-contribution-rates-for-employers> -- archived with content 2026-10-28.
- M.G.L. c.63 §32B (combined reporting): <https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter63/Section32B> -- archived 2026-10-28.
- 830 CMR 63.00 incl. 63.32B.2 Combined Reporting: <https://www.sec.state.ma.us/reg_pub/pdf/800/830063.pdf> -- archived 2026-10-28.
- Form 1-NR/PY: <https://www.mass.gov/forms/massachusetts-nonresident-or-part-year-resident-income-tax-return-form-1-nrpy> -- not yet archived (403/404 from this environment 2026-10-25 through 2026-10-29).
- DOR PTE election: <https://www.mass.gov/info-details/elective-pass-through-entity-excise> -- archived with content 2026-10-28.

| Field | Value |
|---|---|
| State | Massachusetts |
| Code | US-MA |
| Income tax | Yes |
| Sales tax | Yes |
| Franchise / gross receipts tax | No |
| Tax authority | [Massachusetts Department of Revenue (DOR)](https://www.mass.gov/orgs/massachusetts-department-of-revenue) |
| Quality tier | Q3 -- AI-drafted, not independently verified |

## Files in this folder
| File | What it covers |
|---|---|
| `ma-income-tax.md` | Massachusetts individual income tax (flat 5% + 4% surtax over ~$1M) for self-employed / sole proprietors. Form 1. |
| `ma-sales-tax.md` | Massachusetts sales and use tax -- 6.25% state rate. |
| `ma-social-contributions.md` | PFML paid family and medical leave contributions (2026: 0.88% total; split rules; small-employer relief). |
| `ma-transfer-pricing-combined-reporting.md` | Combined unitary reporting (M.G.L. c.63 §32B / 830 CMR 63.32B.2) as Massachusetts' connected-party regime. |
| `ma-cross-border-tax.md` | Nonresidents (Form 1-NR/PY), sourcing, PTE election (c.63D) as the composite alternative. |

## What's NOT covered
- Corporate excise tax (Form 355)
- Partnership returns (Form 3)
- S-corp returns
- Part-year and nonresident returns (Form 1-NR/PY)
- Estate tax (Form M-706)
- Room occupancy tax
- Meals tax (local option)
- Cannabis tax
- Amended returns

## How to use
Upload all `.md` files in this folder PLUS the federal skills from `skills/foundation/` and `skills/federal/` to your LLM.
