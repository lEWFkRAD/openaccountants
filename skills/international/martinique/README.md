# Martinique tax pack — domain applicability

Jurisdiction: MQ (Martinique, French overseas department, EU outermost region).
As of 2026-10-22. Martinique applies the French Code général des impôts with
overseas adaptations (CGI Art. 197 B income-tax reduction, 8.5% DOM VAT,
octroi de mer with a Martinique-specific internal-rate deliberation, DOM
social scales). The parent France pack (`skills/international/france/`)
carries the shared mechanics; this pack carries the Martinique layer.
Martinique and Guadeloupe form one Antilles fiscal territory for octroi de
mer goods movements — see `mq-antilles-goods-movements.md`.

applicable:
  - Income tax, individuals (mq-income-tax-individuals.md) — CGI barème plus the Art. 197 B overseas reduction
  - Income tax, companies (mq-income-tax-companies.md) — IS 25%/15% plus overseas investment incentives
  - VAT (mq-value-added-tax.md) — 8.5% standard DOM rate, territoriality rules
  - Octroi de mer (mq-antilles-goods-movements.md, already drafted) — import/internal goods tax and inter-island movements
  - Social contributions (mq-social-contributions.md) — DOM URSSAF scales
  - Payroll withholding (mq-payroll-withholding.md) — PAS with the Martinique grid
  - Transfer pricing (mq-transfer-pricing.md) — CGI Art. 57, LPF L.13 AA
  - Cross-border (mq-cross-border.md) — EU ORA customs/VAT interface, CARICOM proximity, exit tax

not_applicable:
  - Departure/exit tax as a separate MQ regime: the French exit tax (CGI Art. 167 bis) applies to French tax residents wherever they live, including Martinique; there is no separate Martinique exit charge (reason: single French fiscal territory; as_of 2026-10-22)

Source status: legifrance.gouv.fr and impots.gouv.fr returned 403/maintenance to
this host on 2026-10-22; figures are carried from the France pack (official
pages read 19 Sep–19 Oct 2026) and douane.gouv.fr / service-public.fr pages
read 2026-10-22. The Art. 197 B reduction rate and cap need re-verification
against Legifrance before tier-1 promotion.
