# Guadeloupe tax pack — domain applicability

Jurisdiction: GP (Guadeloupe, French overseas department, EU outermost region).
As of 2026-10-22. Guadeloupe applies the French Code général des impôts with
overseas adaptations (CGI Art. 197 B income-tax reduction, DOM VAT rates,
octroi de mer, DOM social scales). The parent France pack
(`skills/international/france/`) carries the shared mechanics; this pack
carries the Guadeloupe-specific layer.

applicable:
  - Income tax, individuals (gp-income-tax-individuals.md) — CGI barème plus the Art. 197 B overseas reduction
  - Income tax, companies (gp-income-tax-companies.md) — IS 25%/15% plus overseas investment incentives
  - VAT (gp-value-added-tax.md) — 8.5% standard DOM rate, territoriality rules
  - Octroi de mer (gp-producer-octroi-compliance.md, already drafted) — import and internal goods tax
  - Social contributions (gp-social-contributions.md) — DOM URSSAF scales
  - Payroll withholding (gp-payroll-withholding.md) — PAS with the Guadeloupe grid
  - Transfer pricing (gp-transfer-pricing.md) — CGI Art. 57, LPF L.13 AA
  - Cross-border (gp-cross-border.md) — EU ORA customs/VAT interface, exit tax

not_applicable:
  - Departure/exit tax as a separate GP regime: the French exit tax (CGI Art. 167 bis) applies to French tax residents wherever they live, including Guadeloupe; there is no separate Guadeloupe exit charge (reason: single French fiscal territory; as_of 2026-10-22)

Source status: legifrance.gouv.fr and impots.gouv.fr returned 403/maintenance to
this host on 2026-10-22; figures are carried from the France pack (official
pages read 19 Sep–19 Oct 2026) and douane.gouv.fr / service-public.fr pages
read 2026-10-22. The Art. 197 B reduction rate and cap need re-verification
against Legifrance before tier-1 promotion.
