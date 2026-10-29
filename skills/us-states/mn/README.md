---
jurisdiction: US-MN
applicable: [IT-IND, IT-CORP, VAT, PR, SC, TP, XB]
not_applicable: []
---

# Minnesota — OpenAccountants Tax Skills

**Source status (2026-10-25):** revisor.mn.gov statute pages for 268B.14 (PFML premiums), 290.17 (combined reporting), 289A.08 subd. 7 (composite returns) and 290.92 (nonresident withholding) verified HTTP 200 with statute text. Rate text of 290A.03 (MinnesotaCare) and penalty section 289A.21 render via JavaScript and carry **needs-sources** caveats; figures are corroborated by the existing `mn-corporate-and-pte`, `mn-income-tax`, and `mn-payroll` skills.

## Official sources

- M.S. 268B.14 (PFML premiums): <https://www.revisor.mn.gov/statutes/cite/268B.14> — 200 with text, 2026-10-25.
- M.S. 290.17 (combined reporting): <https://www.revisor.mn.gov/statutes/cite/290.17> — 200 with text, 2026-10-25.
- M.S. 289A.08 (composite returns): <https://www.revisor.mn.gov/statutes/cite/289A.08> — 200 with text, 2026-10-25.
- M.S. 290.92 (nonresident withholding): <https://www.revisor.mn.gov/statutes/cite/290.92> — 200 with text, 2026-10-25.
- M.S. 290A.03 (MinnesotaCare): <https://www.revisor.mn.gov/statutes/cite/290A.03> — 200, 2026-10-25; rate text JS-rendered, **needs-sources**.

| Field | Value |
|---|---|
| State | Minnesota |
| Code | US-MN |
| Income tax | Yes |
| Sales tax | Yes |
| Franchise / gross receipts tax | No |
| Tax authority | [Minnesota Department of Revenue](https://www.revenue.state.mn.us) |
| Quality tier | Q3 — AI-drafted, not independently verified |

## Files in this folder

| File | What it covers |
|---|---|
| `mn-income-tax.md` | Individual income tax for self-employed / sole proprietors (Form M1) |
| `mn-sales-tax.md` | Sales and use tax obligations and rates |
| `mn-social-contributions.md` | PFML premiums (M.S. 268B.14, 2026: 0.7% both programs; small-employer relief) + MinnesotaCare overlay |
| `mn-transfer-pricing-combined-reporting.md` | Combined reporting / unitary business principle (M.S. 290.17) as Minnesota's connected-party regime |
| `mn-cross-border-tax.md` | Schedule M1NR, composite returns (289A.08 subd. 7), nonresident-partner withholding (290.92, $1,000 exception) |

## What's NOT covered

- Corporate franchise tax (Form M4)
- Estate tax (Form M706)
- Part-year and non-resident returns (Schedule M1NR)
- Partnership / S-corp pass-through (Schedule KPI / KS)
- MinnesotaCare tax (health care provider tax)
- Property tax (administered at county level)

## How to use

Upload all `.md` files in this folder PLUS the federal skills from `skills/foundation/` and `skills/federal/` to your LLM.
