---
jurisdiction: US-MA
applicable: [IT-IND, IT-CORP, VAT, PR, SC, TP, XB]
not_applicable: []
---

# Massachusetts — OpenAccountants Tax Skills

**Source status (2026-10-25):** the DFML PFML contribution-rate page verified HTTP 200 with live content (0.88% total; family 0.18%, medical 0.70%, 40/60 split on medical). mass.gov regulation/guide/form pages and malegislature.gov statute pages returned 404 site-wide from the drafting environment on 2026-10-25 — the SC/TP/XB drafts carry **needs-sources** caveats on those citations; figures are corroborated by the existing `ma-corporate-excise` and `ma-income-tax` skills.

**Open question:** `maine-sales-tax.md` and `maryland-sales-tax.md` sit in this folder — likely misfiled; flagged for separate cleanup, not touched by this pack.

## Official sources

- DFML PFML contribution rates: <https://www.mass.gov/info-details/family-and-medical-leave-contribution-rates-for-employers> — 200 with content, 2026-10-25.
- M.G.L. c.63 §33A: <https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXIV/Chapter63/Section33A> — **needs-sources** (404 site-wide 2026-10-25).
- 830 CMR 63.03: <https://www.mass.gov/regulations/830-cmr-6303-unitary-combined-reporting> — **needs-sources** (404 2026-10-25).
- Form 1-NR/PY: <https://www.mass.gov/forms/massachusetts-nonresident-or-part-year-resident-income-tax-return-form-1-nrpy> — **needs-sources** (404 2026-10-25).
- DOR PTE election: <https://www.mass.gov/info-details/passthrough-entity-tax-election> — **needs-sources** (404 2026-10-25).

| Field | Value |
|---|---|
| State | Massachusetts |
| Code | US-MA |
| Income tax | Yes |
| Sales tax | Yes |
| Franchise / gross receipts tax | No |
| Tax authority | [Massachusetts Department of Revenue (DOR)](https://www.mass.gov/orgs/massachusetts-department-of-revenue) |
| Quality tier | Q3 — AI-drafted, not independently verified |

## Files in this folder
| File | What it covers |
|---|---|
| `ma-income-tax.md` | Massachusetts individual income tax (flat 5% + 4% surtax over ~$1M) for self-employed / sole proprietors. Form 1. |
| `ma-sales-tax.md` | Massachusetts sales and use tax — 6.25% state rate. |
| `ma-social-contributions.md` | PFML paid family and medical leave contributions (2026: 0.88% total; split rules; small-employer relief). |
| `ma-transfer-pricing-combined-reporting.md` | Combined unitary reporting (M.G.L. c.63 §33A / 830 CMR 63.03) as Massachusetts' connected-party regime. |
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
