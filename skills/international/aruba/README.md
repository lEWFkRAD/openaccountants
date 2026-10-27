---
jurisdiction: AW
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
covered_by:
  VAT: aw-turnover-taxes
  SC: aw-social-contributions
  IT-IND: aw-individual-income-tax
---

# Aruba (AW): tax pack

Aruba (country of the Kingdom of the Netherlands) levies a **22% corporate income tax** (winstbelasting; reduced from 25% effective 1 January 2023, AB 2022 no. 161), a progressive individual/wage tax on "table income" (21%/42%/52% bands over a tax-free amount of at most Afl. 30,000 for 2026), **dividend withholding tax** on distributions by Aruba-registered bodies, and monthly turnover taxes **BBO 2.5% + BAVP 1.5% + BAZV 3% = 7%** with a small-business relief at Afl. 50,000 annual turnover. There is no general VAT; BBO/BAVP/BAZV and import taxes do the work. Social contributions run through SVB (AOV/AWW, AZV, ZV/OV, Cessantia) and are withheld with wage tax (loonbelasting) by the employer.

**Source status (2026-10-27):** impuesto.aw (Departamento di Impuesto, DIMP) pages verified HTTP 200 with real content this run: winstbelasting, dividendbelasting-home, belastingplan_2023 (22% rate text, DGA deemed-dividend rule, dividend-rate changes), bbo, hoeveel-bbo-en-bavp-moet-u-betalen (rate timeline to 7%), wanneer-moet-u-aangifte-doen-en-betalen (BBO monthly 15th deadline, cash regime), loonbelasting-en-premies, hoeveel-loonbelasting-houdt-u-in-en-draagt-u-af (withholding mechanics, 3% cost deduction cap Afl. 1,500), aangifte-buitenlandse-belastingplichtigen (non-resident filing), wanneer-moet-u-betalen (2-month assessment term, holiday shift), internationaal/beps (BEPS/CbC/MAP). The existing `aw-individual-income-tax`, `aw-social-contributions` and `aw-turnover-taxes` skills carry the 2026 DIMP table and SVB 2026 schedule (verified 22 Oct 2026). **needs-sources:** the current dividendbelasting headline rate (the /dividendbelasting page 404s; only the home page resolves — 5% listed-company and 0% IPC rates confirmed abolished by belastingplan_2023), the statutory winstbelasting Landsverordening article numbers, the monthly loonbelasting payment deadline (15th asserted by pattern, not verified this run), late-payment surcharge/interest percentages, and the treaty position (Aruba applies Kingdom treaties only for the Netherlands European part — confirm per treaty).

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND (loonbelasting/inkomstenbelasting table) | aw-individual-income-tax | existing (mapped via covered_by) |
| IT-CORP (winstbelasting 22%) | aw-corporate-tax | source-cited draft |
| VAT / turnover taxes (BBO/BAVP/BAZV 7%) | aw-turnover-taxes | existing (mapped via covered_by) |
| SC (AOV/AWW, AZV, ZV/OV, Cessantia) | aw-social-contributions | existing (mapped via covered_by) |
| PR (loonbelasting withholding, VZL/VOD) | aw-payroll-withholding | source-cited draft |
| TP (arm's length, BEPS/CbC/MAP) | aw-transfer-pricing | source-cited draft |
| XB (non-resident filing, part-year, DGA) | aw-cross-border-tax | source-cited draft |

## Official sources

- Departamento di Impuesto (DIMP): <https://www.impuesto.aw/> — all pages listed above verified 200 with text 2026-10-27.
- AB 2022 no. 161 (BBO/BAVP/BAZV rates) and Landsverordening loonbelasting — PDFs linked from DIMP wetgeving pages (verified 200 as links this run).
- SVB (Sociale Verzekeringsbank Aruba) 2026 tariff schedule: <https://www.svbaruba.org/employer/summary-of-tariffs/summary-of-tariffs-2026/?lang=en> — verified 22 Oct 2026 (carried from `aw-social-contributions`).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
