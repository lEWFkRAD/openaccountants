# Illinois (US-IL) pack

Jurisdiction: Illinois, United States. Tax year 2026. Pack drafted 2026-10-27 (source-cited drafts, tier 2).

Illinois taxes individuals and corporations under the Income Tax Act (35 ILCS 5), imposes a
corporate replacement tax, runs its own withholding regime, and administers unemployment
through IDES. Sales tax is administered by IDOR with a state rate plus local distributions.

## applicable

- `IT-IND` — individual income tax (flat 4.95% + surtax tiers) — present: `il-income-tax.md`
- `IT-CORP` — corporate income tax + replacement tax — drafted: `il-corporate-income-tax.md`
- `VAT` — sales tax (state + local) — present: `il-sales-tax.md`
- `SC` — social contributions (IDES unemployment, workers' comp) — drafted: `il-social-contributions.md`
- `PR` — payroll withholding — present: `il-payroll.md`
- `TP` — transfer pricing / unitary combined reporting — drafted: `il-transfer-pricing.md`
- `XB` — cross-border / nexus — drafted: `il-cross-border.md`

## not_applicable

- none — Illinois has income, corporate, sales, payroll, and social-contribution regimes; all
  pilot domains apply.

## Source status

- Form IL-1120 (R-12/25), IL-1120-V, and the 24-page IL-1120 instructions PDF: verified 2026-10-27
  (tax.illinois.gov, PDF text read — filing dates, estimated-tax $400 threshold, unitary/Finnigan
  notes, IL-2220 penalty form all read from the instructions).
- sources/US-IL-ides-ui-rates-2026.pdf PDF (`UI_tax_rates_2026.pdf`): verified 2026-10-27 — 2026 wage base
  wage base and rate schedule per the archived IDES chart (figures not machine-readable in the archived copy — not yet confirmed);
  small-employer flat rate under the gross-wage threshold; minimum penalty (figures: not yet confirmed).
- ILCS statute pages (35 ILCS 5) render article text via JavaScript; direct section URLs did not
  resolve to text this run — statutory rate citations carry not-yet-confirmed flags pending a
  readable ILCS fetch.
