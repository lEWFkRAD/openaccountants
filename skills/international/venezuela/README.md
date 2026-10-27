---
jurisdiction: VE
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
covered_by:
  VAT: venezuela-iva
---

# Venezuela (VE): tax pack

Venezuela taxes worldwide income of residents under the ISLR Law (Ley de ISLR, G.O. 6.079 E. 22 Dec 2015, as amended): individuals on the progressive Tarifa No. 1 (6%–34%), companies on Tarifa No. 2 (22% band / 34% top) with special flat rates of **40%** (banks, financial institutions, insurers) and **50%** (oil exploitation), with **34% withholding** on dividends, interest and royalties paid to non-residents and a 34% flat rate on non-resident Venezuelan-source income, and a 1:1 related-party debt/equity limit (Art. 38). All statutory amounts are expressed in Tax Units (UT; VES 43.00/UT since 2 June 2025, Providencia SNAT/2025/0048) and the environment is hyperinflationary — every figure must be re-confirmed at filing time.

**Source status (2026-10-27):** the existing `venezuela-income-tax`, `venezuela-payroll`, `venezuela-social-contributions`, `venezuela-iva` and `venezuela-tax-optimization` skills carry the ISLR Law article citations (Arts. 31, 36, 146, 155, 171, 235, 289, 311, 331, 333, 346, 351, 352, 361, 362, 363, 364, 365, 366, 367, 368, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700) and PwC citations (reviewed Jan 2026); those figures are carried into the new drafts with their citations. **seniat.gob.ve returned HTTP 403 to every request on 2026-10-26 and taxsummaries.pwc.com began rate-limiting (HTTP 429/503) mid-run on 2026-10-27** — the PwC pages verified earlier this run (corporate incomes, tax administration, individual residence-and-source, corporate deductibility, transfer pricing) are cited with their earlier as_of. **needs-sources:** the ISLR article number for the transfer-pricing/arm's-length rule and the SPAR special-regime article, current UT value at filing date, and the 2026 filing-calendar resolutions.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND | venezuela-income-tax, venezuela-payroll | existing |
| IT-CORP | venezuela-corporate-tax | source-cited draft |
| VAT / consumption | venezuela-iva | existing (mapped via covered_by) |
| SC, social contributions | venezuela-social-contributions, venezuela-payroll | existing |
| PR, withholding | venezuela-payroll | existing |
| TP, transfer pricing | venezuela-transfer-pricing | source-cited draft |
| XB, cross-border | venezuela-cross-border-tax | source-cited draft |

## Official sources

- SENIAT (Servicio Nacional Integrador de Administración Tributaria): <https://www.seniat.gob.ve/> — 403 to direct requests 2026-10-26; cited as authority of record only.
- Ley de ISLR, Gaceta Oficial 6.079 Especial, 22 December 2015 (as amended) — article citations carried from the existing skills.
- Providencia Administrativa SNAT/2025/0048, Gaceta Oficial No. 43,140 (UT = VES 43.00 from 2 June 2025) — carried from `venezuela-payroll`.
- PwC Worldwide Tax Summaries — Venezuela (corporate incomes, tax administration, individual residence-and-source, deductibility, transfer pricing): <https://taxsummaries.pwc.com/venezuela/corporate/incomes> — 200 with text, 2026-10-27 (rate-limited after).
