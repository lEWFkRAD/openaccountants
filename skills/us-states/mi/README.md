---
jurisdiction: US-MI
applicable: [IT-IND, IT-CORP, VAT, PR, SC, TP, XB]
not_applicable: []
---

# Michigan — OpenAccountants Tax Skills

**Source status (2026-10-25):** Treasury CIT unitary-business-groups page and the resident/non-resident FAQ hub verified HTTP 200 with live content; 2022 PA 1 (MI PFML) enrolled-act URL 200 but its premium sections were not machine-readable from the text layer — PFML premium figures are **needs-sources**. legislature.mi.gov MCL section pages render via JavaScript; statute text carries **needs-sources** caveats. Figures are corroborated by the existing `mi-corporate-income-tax`, `mi-income-tax`, and `mi-payroll` skills.

## Official sources

- Treasury CIT unitary business groups: <https://www.michigan.gov/taxes/business-taxes/cit/detail/unitary-business-groups> — 200 with content, 2026-10-25.
- MCL 208.1401 (UBG): <https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-208-1401> — 200, 2026-10-25 (JS-rendered text).
- MCL 206.131 (composite): <https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-206-131> — 200, 2026-10-25 (JS-rendered text, **needs-sources**).
- Treasury non-resident FAQ hub: <https://www.michigan.gov/taxes/iit/file-your-income-taxes/resident-and-non-resident-income-faqs> — 200 with content, 2026-10-25.
- 2022 PA 1 (MI PFML, enrolled): <https://www.legislature.mi.gov/documents/2021-2022/publicact/htm/2022-PA-0001.htm> — 200, 2026-10-25; premium schedule **needs-sources**.

| Field | Value |
|---|---|
| State | Michigan |
| Code | US-MI |
| Income tax | Yes |
| Sales tax | Yes |
| Franchise / gross receipts tax | No |
| Tax authority | [Michigan Department of Treasury](https://www.michigan.gov/treasury) |
| Quality tier | Q3 — AI-drafted, not independently verified |

## Files in this folder

| File | What it covers |
|---|---|
| `mi-income-tax.md` | Individual income tax for self-employed / sole proprietors (Form MI-1040) |
| `mi-sales-tax.md` | Sales and use tax obligations and rates |
mi-social-contributions.md | UI employer-only structure (wage base not yet confirmed) + PFML program
| `mi-transfer-pricing-unitary-combined.md` | Unitary combined reporting (MCL 208.1401) as Michigan's connected-party regime |
| `mi-cross-border-tax.md` | Schedule NR, reciprocity, composite (needs-sources), P.L. 86-272 |

## What's NOT covered

- Corporate income tax (CIT)
- Michigan Business Tax (MBT) — repealed, replaced by CIT
- Estate tax (Michigan has no estate tax)
- Part-year and non-resident returns (Schedule NR)
- City income taxes (Detroit, Grand Rapids, etc.) — separate filing
- Property tax (administered at local level)

## How to use

Upload all `.md` files in this folder PLUS the federal skills from `skills/foundation/` and `skills/federal/` to your LLM.
