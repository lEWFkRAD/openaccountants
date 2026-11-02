---
name: ca-estimated-tax-540es
description: Tier 2 California content skill for computing California estimated tax payments under Form 540-ES for full-year California residents who are sole proprietors or single-member LLCs disregarded for federal tax. Covers the California 30/40/0/30 installment schedule (NOT equal quarterly like federal), due dates (April 15, June 16, September 15 with no installment, January 15 for 2025), the 100% prior-year safe harbor (110% for high income), underpayment penalty computation on Form 5805 / 5805-F, required annual payment rules, interaction with federal estimated tax (separate payments to separate agencies), and withholding credits from W-2 or backup withholding. Defers income tax computation to ca-540-individual-return and SMLLC franchise tax to ca-smllc-form-568. MUST be loaded alongside us-tax-workflow-base v0.1 or later. California residents only. Tax year 2025.
version: 0.3
jurisdiction: US-CA
tier: 2
last_updated: 2026-11-02
---

# CA Estimated Tax 540-ES Skill v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is, and what it is not

**This file is a content skill that loads on top of `us-tax-workflow-base` v0.1.** It provides the California estimated tax payment rules for individual taxpayers who are full-year California residents with self-employment income for tax year 2025. California uses a unique 30/40/0/30 installment schedule that differs significantly from the federal equal-quarterly system.

**This skill does NOT compute California income tax** (handled by `ca-540-individual-return`). It takes the total CA tax liability as an input and determines the required estimated payments, safe harbor amounts, and any underpayment penalty.

**Critical distinction from federal.** Federal estimated tax uses equal 25% quarterly installments. California uses 30%/40%/0%/30%. Getting this wrong causes underpayment penalties. This is the single most important fact in this skill.

---

## Who this applies to

This skill covers California Form 540-ES and related underpayment penalty analysis for tax year 2025 for taxpayers who are:

- Full-year California residents
- Sole proprietors or single-member LLC owners with self-employment income
- Required to make estimated tax payments to the California Franchise Tax Board (FTB)

For the following kinds of work:

- Determining whether estimated tax payments are required
- Computing the required annual payment
- Allocating payments across the 30/40/0/30 installment schedule
- Computing underpayment penalties (Form 5805)
- Reconciling withholding credits against estimated tax obligations
- Producing the 2026 prospective estimated tax payment schedule

This skill does NOT cover:

- California income tax computation -- handled by `ca-540-individual-return`
- Federal estimated tax -- handled by `us-quarterly-estimated-tax`
- SMLLC $800 franchise tax or LLC fee payments -- handled by `ca-smllc-form-568`
- Corporate estimated tax (Form 100-ES)
- Nonresident estimated tax

---

## Section 2 -- Year coverage and currency

**Tax year covered:** 2025 (estimated payments made during 2025; return filed in 2026).

**Currency date:** April 2026.

**Legislation reflected:**
- R&TC section 19136 -- requirement to pay estimated tax
- R&TC section 19136.1 -- installment schedule (30/40/0/30)
- R&TC section 19136.5 -- exception for underpayments attributable to other states' credit-law changes (not the safe harbor rule)
- R&TC section 19142 -- underpayment penalty
- R&TC section 19144 -- exceptions to penalty
- FTB Form 540-ES Instructions (2025)
- FTB Form 5805 Instructions (2025) -- Underpayment of Estimated Tax by Individuals and Fiduciaries
- FTB Form 5805-F Instructions (2025) -- Underpayment of Estimated Tax by Farmers and Fishermen

---

## Rates, bands and thresholds

### Installment schedule

| Installment | Due date (calendar year) | Percentage of required annual payment | Cumulative |
|---|---|---|---|
| Q1 | April 15, 2025 | 30% | 30% |
| Q2 | June 16, 2025 | 40% | 70% |
| Q3 | September 15, 2025 | 0% (no installment is due for the 3rd required installment) | 70% |
| Q4 | January 15, 2026 | 30% | 100% |

**Note:** There is NO September 15 payment for California (the 3rd required installment is 0%; R&TC section 19136.1(a) as applied by FTB 2025 Form 540-ES). The 2nd 2025 installment date is June 16, 2025 because June 15 fell on a Sunday. This is the most common error. Taxpayers who autopay equal quarterly amounts overpay in Q1 and Q2 and skip Q3.

### Safe harbor rules

| Rule | Threshold | Source |
|---|---|---|
| Current-year safe harbor | Pay 90% of current year's CA tax liability | R&TC section 19136; FTB 2025 Form 540-ES Section B |
| Prior-year safe harbor | Pay 100% of prior year's CA tax liability (including AMT) | R&TC section 19136; FTB 2025 Form 540-ES Section B |
| Prior-year safe harbor (high income) | If prior-year (2024) CA AGI > $150,000 ($75,000 MFS): use the lesser of 90% of 2025 tax or 110% of 2024 tax | FTB 2025 Form 540-ES Section C |

**Note:** Confirmed: California does use 110% of prior-year tax for taxpayers whose prior-year CA AGI exceeds $150,000 ($75,000 if married/RDP filing separately); the rule does not apply to farmers or fishermen (FTB 2025 Form 540-ES Section C). R&TC section 19136.5 is NOT the safe harbor section -- it excepts underpayments attributable to other states' credit-law changes.

### Estimated tax payment threshold

| Figure | Value | Source |
|---|---|---|
| Estimated tax required if expected tax liability (after withholding and credits) exceeds | $500 ($250 if married/RDP filing separately) -- California has no $1,000 MFJ exception | R&TC section 19136(c); FTB 2025 Form 540-ES Section B |

### Underpayment penalty rate

| Figure | Value | Source |
|---|---|---|
| Underpayment (estimate) penalty rate | Set SEMIANNUALLY by FTB (rates determined each March and September): 8% for 01/01/2025-06/30/2025, then 7% for 07/01/2025-06/30/2026 and 07/01/2026-12/31/2026 | R&TC section 19521; FTB interest and estimate penalty rates page |

### Key payment logistics

| Item | Detail |
|---|---|
| Payment methods | FTB Web Pay (recommended), credit card (with fee), check with Form 540-ES voucher |
| Web Pay URL | https://webapp.ftb.ca.gov/webpay |
| Payee for checks | Franchise Tax Board |
| Mailing address | Varies by county; see Form 540-ES voucher |

---

## Section 4 -- Primary source library

| Source | Use |
|---|---|
| R&TC section 19136 | Requirement to make estimated tax payments; $500/$250 de minimis exception; withholding credited at the applicable percentage (19136(e)(2)(A)) |
| R&TC section 19136.1 | 30/40/0/30 installment allocation (modifies IRC 6654(d)(1)(A)) |
| R&TC section 19136.5 | Exception for underpayments attributable to other states' credit-law changes (NOT the safe harbor section) |
| R&TC section 19142 | Underpayment penalty computation |
| R&TC section 19144 | Exceptions to underpayment penalty |
| R&TC section 19521 | Interest rate determination |
| FTB Form 540-ES (2025) | Estimated tax vouchers and worksheet |
| FTB Form 5805 (2025) | Underpayment penalty computation |
| FTB Form 5805-F (2025) | Farmer/fisherman underpayment penalty |
| FTB Publication 1060 | Guide for Corporations Remitting Estimated Tax (reference for contrast) |

---

## The taxable base

### 5.1 -- General rule

A taxpayer must make estimated tax payments if:

1. They expect to owe at least $500 ($1,000 MFJ) in CA tax after subtracting withholding and credits (verify thresholds), AND
2. They expect their withholding and credits to be less than the LESSER of:
   - 90% of the current year's tax, OR
   - 100% of the prior year's tax (110% if high income -- verify CA rule)

### 5.2 -- Who typically must pay

- Self-employed individuals (Schedule C income)
- Taxpayers with significant investment income
- Taxpayers with income not subject to CA withholding
- Partners and S-corp shareholders (K-1 income)

### 5.3 -- Who may be exempt

- Taxpayers whose CA tax liability (after withholding and credits) is less than $500 ($250 if married/RDP filing separately) -- R&TC section 19136(c); there is no $1,000 MFJ exception in California
- New California residents (and nonresidents) with no California tax liability in the prior year -- no 2025 estimated tax payments required at all (FTB 2025 Form 540-ES Section B note; but see 5.4)
- Farmers and fishermen (special rules -- single installment due January 15, 2026, or file and pay by March 2, 2026; FTB 2025 Form 540-ES Section D and FTB 5805 instructions Section G)

### 5.4 -- First year in California

If the taxpayer had no CA tax liability in the prior year (e.g., new CA resident), FTB 2025 Form 540-ES Section B says no 2025 estimated tax payments are required at all: "You do not have to make estimated tax payments if you are a nonresident or new resident of California in 2025 and did not have a California tax liability in 2024." The prior-year-tax exception is not even needed. (The 90% current-year figure remains the general safe-harbor rate for taxpayers who DO owe estimated tax.)

---

## Deadlines and filing

### 6.1 -- How it works

California R&TC section 19136.1 prescribes the following allocation:

| Installment | Percentage | Due date | What to pay |
|---|---|---|---|
| 1st | 30% | April 15, 2025 | 30% of the required annual payment |
| 2nd | 40% | June 16, 2025 | 40% of the required annual payment |
| 3rd | 0% | September 15, 2025 | $0 (no installment is due for the 3rd required installment) |
| 4th | 30% | January 15, 2026 | 30% of the required annual payment |

### 6.2 -- Required annual payment

The "required annual payment" is the LESSER of:
- 90% of the 2025 CA tax liability, OR
- 100% of the 2024 CA tax liability including AMT (110% if 2024 CA AGI exceeded $150,000 / $75,000 MFS -- confirmed, FTB 2025 Form 540-ES Section C)

### 6.3 -- Example computation

Prior year CA tax = $10,000. Current year expected CA tax = $12,000.

Required annual payment = lesser of:
- 90% x $12,000 = $10,800
- 100% x $10,000 = $10,000

Required annual payment = $10,000.

| Installment | Amount |
|---|---|
| Q1 (April 15) | $10,000 x 30% = $3,000 |
| Q2 (June 16) | $10,000 x 40% = $4,000 |
| Q3 (September 15) | $0 |
| Q4 (January 15) | $10,000 x 30% = $3,000 |

### 6.4 -- Withholding credit application

If the taxpayer also has W-2 wages with CA withholding:
- California does NOT spread withholding evenly. R&TC section 19136(e)(2)(A) replaces the IRC 6654(g)(1) phrase "an equal part" with "the applicable percentage" -- withholding is credited at 30%/40%/0%/30% of the annual withholding for installments 1-4.
- FTB 2025 Form 540-ES worksheet method (lines 20-22): subtract TOTAL estimated withholding from the required annual payment FIRST, then multiply the balance by 30% (1st and 4th installments) and 40% (2nd). No 3rd installment. If the balance is under $500 ($250 MFS), no estimated payments are required.
- If total withholding meets the safe harbor, no estimated payments are needed.

### 6.5 -- Backup withholding

Backup withholding (7% on 1099 payments) is withholding and is credited the same way -- at the applicable percentage (30/40/0/30), not ratably. It reduces estimated tax obligations.

---

## Penalties and interest

### 7.1 -- When the penalty applies

A penalty applies if:
- The taxpayer underpaid any installment relative to its required amount, AND
- No exception applies (see 'Penalties and interest', 7.3)

The penalty is computed as INTEREST on each underpayment from the installment due date to the earlier of:
- The date the underpayment was cured (paid), or
- April 15, 2026 (the return due date)

### 7.2 -- Penalty computation steps

For each installment:

1. Determine the required payment (30% / 40% / 0% / 30% of required annual payment).
2. Subtract the withholding credit allocated to that installment at the applicable percentage -- 30%/40%/0%/30% of annual withholding (R&TC section 19136(e)(2)(A)), NOT 1/4 per quarter.
3. Subtract estimated payments actually made by the due date.
4. If the result is positive, that is the underpayment for that installment.
5. Compute interest on the underpayment at the FTB estimate-penalty rate (set semiannually: 8% for 01/01/2025-06/30/2025, 7% from 07/01/2025) from the due date to April 15, 2026 (or earlier payment date).

### 7.3 -- Exceptions to penalty

| Exception | Description |
|---|---|
| Tax liability under $500 ($250 MFS) | No penalty if total tax after withholding/credits < $500 ($250 if married/RDP filing separately) -- R&TC section 19136(c); no $1,000 MFJ exception in CA |
| No prior-year CA liability (new/nonresident) | No 2025 estimated tax payments required at all if you were a new resident (or nonresident) in 2025 with no 2024 CA tax liability (FTB 2025 Form 540-ES Section B) |
| Casualty/disaster | FTB may waive penalty for taxpayers in federally declared disaster areas |
| Annualized income method | Taxpayer can use Schedule AI on Form 5805 to demonstrate income was earned unevenly throughout the year and payments matched income timing |

### 7.4 -- Annualized income installment method

If income was earned unevenly (e.g., large contract paid in Q4), the taxpayer can use the annualized income installment method on Schedule AI (Form 5805):

1. Compute CA taxable income for each cumulative period (Jan-Mar, Jan-May, Jan-Aug, Jan-Dec).
2. Annualize each period's income.
3. Compute tax on the annualized income.
4. Determine the required installment based on annualized tax.
5. This may reduce or eliminate the penalty for early installments when income was low.

---

## Cross-border points

### 8.1 -- Separate systems

California estimated tax and federal estimated tax are completely independent:
- Separate computations
- Separate payment methods (FTB Web Pay vs. IRS EFTPS/Direct Pay)
- Separate safe harbors
- Different installment schedules (CA 30/40/0/30 vs. federal 25/25/25/25)

### 8.2 -- Common errors

| Error | Why it happens | Correct approach |
|---|---|---|
| Paying equal quarters to CA | Taxpayer assumes CA matches federal | Use 30/40/0/30 |
| Skipping CA Q1 because federal Q1 was paid | Confusing the two systems | Pay both on April 15 |
| Using federal safe harbor for CA | Different rules | Compute CA safe harbor separately |
| Sending CA payment to IRS | Wrong payee | CA goes to FTB; federal goes to IRS |

### 8.3 -- Consolidated payment calendar (for taxpayer action list)

| Date | Federal payment | CA payment |
|---|---|---|
| April 15, 2025 | 25% of federal required | 30% of CA required |
| June 15/16, 2025 | 25% of federal required (June 15) | 40% of CA required (June 16, 2025 -- June 15 was a Sunday) |
| September 15, 2025 | 25% of federal required | $0 |
| January 15, 2026 | 25% of federal required | 30% of CA required |

---

## Section 9 -- PROHIBITIONS

**P-ES-1.** NEVER use equal 25% quarterly installments for California estimated tax. California uses 30/40/0/30. This is the most critical prohibition in this skill.

**P-ES-2.** NEVER tell the taxpayer to make a California estimated tax payment on September 15. The Q3 California installment is $0.

**P-ES-3.** NEVER combine federal and California estimated tax into a single payment. They go to different agencies (IRS vs. FTB) with different methods.

**P-ES-4.** NEVER apply the wrong prior-year safe harbor percentage. California uses 100% of prior-year tax, but 110% if prior-year (2024) CA AGI exceeded $150,000 ($75,000 if married/RDP filing separately) -- confirmed, FTB 2025 Form 540-ES Section C. The 110% rule does not apply to farmers or fishermen.

**P-ES-5.** NEVER ignore withholding credits when computing estimated tax. W-2 withholding and backup withholding reduce the estimated tax obligation.

**P-ES-6.** NEVER assume the farmer/fisherman exception applies automatically. It requires that at least 2/3 of gross income comes from farming or fishing.

**P-ES-7.** NEVER confuse Form 540-ES (individual estimated tax) with Form 3522 (LLC franchise tax) or Form 3536 (LLC fee estimate). These are separate obligations with separate due dates.

**P-ES-8.** NEVER skip the underpayment penalty analysis. Even if the taxpayer paid some estimated tax, they may have underpaid specific installments under the 30/40/0/30 schedule.

---

## Worked examples

### EC-ES-1 -- Taxpayer pays equal quarters by mistake

**Situation:** Taxpayer's required annual payment is $20,000. They pay $5,000 on April 15, $5,000 on June 15, $5,000 on September 15, $5,000 on January 15.

**Resolution:**
- Required: Q1 = $6,000 (30%), Q2 = $8,000 (40%), Q3 = $0, Q4 = $6,000 (30%).
- Paid: Q1 = $5,000, Q2 = $5,000, Q3 = $5,000, Q4 = $5,000.
- Underpayment (cumulative basis, FTB 5805 Worksheet II -- overpayments carry forward): Q1 = $1,000 underpaid; Q2 cumulative required $14,000 vs paid $10,000 = $4,000 underpaid; Q3 = $0; Q4 cumulative required $20,000 vs paid $20,000 = $0 (the Q3 payment cures Q4).
- Penalty: interest computed on $1,000 from April 15 and on the cumulative underpayment from June 16, to April 15, 2026.
- **Note:** CA computes installments cumulatively -- the September $5,000 payment is not wasted; it cures the Q4 shortfall.

### EC-ES-2 -- New California resident, no prior-year CA tax

**Situation:** Taxpayer moved to California on January 1, 2025. No 2024 CA return. Expected 2025 CA tax = $15,000.

**Resolution:**
- No 2025 estimated tax payments are required at all: FTB 2025 Form 540-ES Section B says a new (or non) resident of California in 2025 with no California tax liability in 2024 does not have to make estimated tax payments.
- The old "must use the 90% current-year method" framing is wrong -- the taxpayer may simply pay the balance with the 2025 return.
- If the taxpayer WANTS to pay in (to reduce the April balance due), the 90% current-year figure (90% x $15,000 = $13,500, split 30/40/0/30) is the general rate -- but it is not mandatory in year one.
- **Flag for reviewer:** Confirm the taxpayer truly had zero 2024 CA liability (any 2024 CA tax, even small, ends the exemption).

### EC-ES-3 -- Income spike in Q4

**Situation:** Freelancer earns $30,000 in Q1-Q3 combined, then receives a $120,000 contract payment in November. Total 2025 CA tax is $18,000. Prior-year CA tax was $5,000.

**Resolution:**
- Prior-year safe harbor: 100% x $5,000 = $5,000. This is the required annual payment (less than 90% x $18,000 = $16,200).
- Q1 = $1,500, Q2 = $2,000, Q3 = $0, Q4 = $1,500.
- If the taxpayer paid $1,500 / $2,000 / $0 / $1,500, the safe harbor is met. No penalty even though actual tax is $18,000.
- Remaining $13,000 ($18,000 - $5,000) is due with the return on April 15, 2026.
- Alternatively, the taxpayer can use the annualized income method to reduce even the safe harbor amounts for early quarters.
- **Flag for reviewer:** 110% applies only if 2024 CA AGI exceeded $150,000 ($75,000 MFS) -- then the required annual payment is the lesser of 90% of 2025 tax ($16,200) or 110% of 2024 tax ($5,500).

### EC-ES-4 -- W-2 withholding covers most of the tax

**Situation:** Taxpayer has W-2 job (CA withholding $12,000 annually) and side Schedule C business. Total CA tax = $15,000.

**Resolution:**
- Required annual payment: lesser of 90% x $15,000 = $13,500 or 100% of prior year tax.
- Withholding is NOT spread $3,000 per quarter. FTB 2025 Form 540-ES worksheet (lines 20-22): subtract total withholding from the required annual payment first: $13,500 - $12,000 = $1,500 balance.
- Installments on the balance (30/40/0/30):
  - Q1: 30% x $1,500 = $450
  - Q2: 40% x $1,500 = $600
  - Q3: $0 (no 3rd installment; no negative withholding credit)
  - Q4: 30% x $1,500 = $450
- If withholding alone meets the safe harbor, no estimated payments needed (here withholding $12,000 < $13,500, so small payments are due).

### EC-ES-5 -- Farmer/fisherman exception

**Situation:** Taxpayer earns 70% of gross income from farming. Total CA tax = $8,000.

**Resolution:**
- Qualifies for farmer/fisherman exception (at least 2/3 of gross income from farming/fishing).
- Single installment due January 15, 2026 (100% of required payment; required annual payment for farmers/fishermen is 66 2/3% of 2025 tax -- 540-ES worksheet line 19a).
- OR file the 2025 return and pay full tax by March 2, 2026 -- no penalty (FTB 2025 Form 540-ES Section D; March 1, 2026 is a Sunday, so FTB prints March 2).
- The 30/40/0/30 schedule does NOT apply to qualifying farmers/fishermen.
- **Flag for reviewer:** Verify the 2/3 gross income test. If the taxpayer does not qualify, the regular 30/40/0/30 schedule applies.

### EC-ES-6 -- Disaster area relief

**Situation:** Taxpayer's home is in a county declared a disaster area by the Governor. FTB announces extended deadlines.

**Resolution:**
- Check FTB disaster relief announcements for the specific disaster.
- Estimated tax due dates may be extended (e.g., Q1 due April 15 extended to October 15).
- The penalty is waived or reduced for the extended period.
- **Flag for reviewer:** Verify the specific disaster relief provisions and extended dates.

### EC-ES-7 -- Taxpayer overpays Q1 and Q2

**Situation:** Taxpayer's required annual payment is $10,000. They pay $5,000 on April 15 and $5,000 on June 15 (total $10,000 by Q2). Nothing in Q3 or Q4.

**Resolution:**
- Required: Q1 = $3,000 (30%), Q2 = $4,000 (40%), Q3 = $0, Q4 = $3,000 (30%).
- Cumulative: After Q1 paid $5,000 (required $3,000 -- overpaid $2,000). After Q2 paid $10,000 cumulative (required $7,000 cumulative -- overpaid $3,000).
- Q4 required $3,000 -- but cumulative payments already exceed $10,000 total required. No underpayment.
- No penalty. The overpayment from Q1/Q2 carries forward to satisfy Q4.

### EC-ES-8 -- MFS with different income levels

**Situation:** Married couple filing separately for CA. Spouse A has CA tax of $20,000. Spouse B has CA tax of $3,000.

**Resolution:**
- Each spouse computes estimated tax independently.
- Spouse A: required annual payment based on Spouse A's tax. Apply 30/40/0/30.
- Spouse B: if tax after withholding and credits < $250 (the MFS de minimis threshold), no estimated payments required.
- Joint payments from prior years must be allocated between spouses.
- **Flag for reviewer:** Verify allocation of prior-year payments and withholding between spouses.

---

## Section 11 -- Test Suite

### Test ES-1 -- Basic 30/40/0/30 computation

**Input:** Prior year CA tax = $8,000. Current year CA tax = $10,000. No withholding.
**Expected:** Required annual payment = lesser of $9,000 (90% current) or $8,000 (100% prior) = $8,000. Q1 = $2,400, Q2 = $3,200, Q3 = $0, Q4 = $2,400.

### Test ES-2 -- Equal-quarter error detection

**Input:** Required annual payment = $12,000. Taxpayer paid $3,000 each quarter (April 15, June 16, September 15, January 15).
**Expected:** Required: Q1 $3,600, Q2 $4,800, Q3 $0, Q4 $3,600. Cumulative underpayment (FTB 5805 Worksheet II): Q1 $600, Q2 $2,400 ($8,400 cumulative required vs $6,000 paid), Q3 none, Q4 $0 (cumulative $12,000 required vs $12,000 paid -- prior over/underpayments carry forward). Penalty = interest on each installment's underpayment from its due date to April 15, 2026.

### Test ES-3 -- Withholding offsets estimated tax

**Input:** Total CA tax = $16,000. Prior year tax = $14,000. W-2 withholding = $14,000.
**Expected:** Required annual payment = lesser of $14,400 (90% current) or $14,000 (100% prior) = $14,000. Withholding $14,000 fully covers it: balance = $14,000 - $14,000 = $0, so NO estimated payments are required (540-ES worksheet: withholding is subtracted in total first, not spread per quarter).

### Test ES-4 -- No prior-year CA tax

**Input:** New CA resident. No 2024 CA tax. Expected 2025 CA tax = $20,000. No withholding.
**Expected:** No 2025 estimated tax payments required at all -- FTB 2025 Form 540-ES Section B exempts new/nonresidents with no 2024 CA tax liability. Pay the $20,000 with the 2025 return.

### Test ES-5 -- Prior-year safe harbor satisfied, current year much higher

**Input:** Prior year CA tax = $6,000. Current year CA tax = $25,000. Taxpayer paid: Q1 $1,800, Q2 $2,400, Q3 $0, Q4 $1,800. Total paid = $6,000.
**Expected:** Required annual payment = lesser of $22,500 (90% current) or $6,000 (100% prior) = $6,000. Q1 required $1,800 (30%), Q2 required $2,400 (40%), Q3 $0, Q4 $1,800 (30%). All installments met. No penalty. Balance due of $19,000 with return.

### Test ES-6 -- Consolidated federal + CA payment calendar

**Input:** Federal required estimated = $16,000. CA required estimated = $10,000.
**Expected:** Payment calendar:
- April 15: Federal $4,000 (25%) + CA $3,000 (30%) = $7,000 total
- June 15/16, 2025: Federal $4,000 (25%) + CA $4,000 (40%) = $8,000 total (CA date is June 16, 2025)
- September 15: Federal $4,000 (25%) + CA $0 (0%) = $4,000 total
- January 15: Federal $4,000 (25%) + CA $3,000 (30%) = $7,000 total

---

## Ask the client first

**Check 250 -- 30/40/0/30 schedule used.** Verify that California installment percentages are 30/40/0/30, not 25/25/25/25.

**Check 251 -- No September 15 CA payment.** Verify that the Q3 CA installment is $0 and no payment was scheduled or recommended for September 15.

**Check 252 -- Safe harbor computed correctly.** Verify that the required annual payment uses the lesser of 90% current-year or 100% (or 110%) prior-year.

**Check 253 -- Withholding credited at the applicable percentage.** If the taxpayer has W-2 withholding, verify it is credited at 30%/40%/0%/30% (R&TC section 19136(e)(2)(A)) -- or, per the 540-ES worksheet, subtracted in total from the required annual payment before applying the installment percentages -- NOT spread equally across 4 quarters.

**Check 254 -- Federal and CA payments are separate.** Verify the taxpayer action list shows separate payment amounts to IRS (EFTPS/Direct Pay) and FTB (Web Pay).

**Check 255 -- Underpayment penalty computed if applicable.** If any installment was underpaid, verify Form 5805 penalty computation.

**Check 256 -- Annualized income method considered.** If income was uneven across quarters, verify whether the annualized income method reduces or eliminates the penalty.

**Check 257 -- Farmer/fisherman exception evaluated.** If the taxpayer has farming/fishing income, verify whether the 2/3 gross income test is met.

**Check 258 -- 2026 prospective schedule produced.** Verify the output includes a 2026 estimated tax payment schedule using the 30/40/0/30 allocation.

**Check 259 -- Form 540-ES vs. Form 3522/3536 not confused.** Verify that 540-ES (personal estimated tax) is not conflated with Form 3522 (LLC $800) or Form 3536 (LLC fee estimate).

---

## Section 13 -- Cross-skill references

**Inputs from:**
- `ca-540-individual-return` -- total CA tax liability for safe harbor and required annual payment
- `us-quarterly-estimated-tax` -- federal estimated tax amounts for consolidated calendar
- Prior-year CA return -- prior-year CA tax for safe harbor

**Outputs to:**
- `us-ca-return-assembly` -- Form 540-ES payment schedule, Form 5805 penalty, 2026 prospective schedule, consolidated payment calendar

---

## Section 14 -- Known gaps

1. Disaster area deadline extensions are fact-specific and not embedded in this skill.
2. The annualized income installment method computation is outlined but not fully detailed step-by-step.
3. Part-year resident estimated tax allocation is not covered.

### Change log
- **v0.1 (April 2026):** Stub.
- **v0.2 (April 2026):** Full content skill with 30/40/0/30 schedule, safe harbor, underpayment penalty, edge cases, and test suite.
- **v0.3 (November 2026):** Deep-review corrections: 2025 Q2 date June 16; 110% high-income safe harbor confirmed ($150,000 / $75,000 MFS); $500/$250 de minimis (no $1,000 MFJ exception); withholding credited at the applicable percentage (30/40/0/30), not ratably; new/nonresidents with no 2024 CA liability owe no 2025 estimates; farmer/fisherman March 2, 2026 alternative and 66 2/3% required annual payment; cumulative carryforward on Form 5805; estimate penalty rates 8% then 7%; R&TC 19136.5 misattribution fixed.

## Sources
| Source | URL | Read on |
| --- | --- | --- |
| FTB 2025 Instructions for Form 540-ES | https://www.ftb.ca.gov/forms/2025/2025-540-es-instructions.pdf | 2026-10-31 |
| R&TC §19136 (estimated tax requirement) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136 | 2026-10-31 |
| R&TC §19136.1 (installment percentages) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.1 | 2026-10-31 |
| R&TC §19136.5 (other-state credit exception) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19136.5 | 2026-10-31 |
| FTB 2025 Instructions for Form 5805 | https://www.ftb.ca.gov/forms/2025/2025-5805-instructions.html | 2026-10-31 |
| FTB Interest and Estimate Penalty Rates page | https://www.ftb.ca.gov/pay/penalties-and-interest/interest-and-estimate-penalty-rates.html | 2026-10-31 |

Not yet confirmed: the statutory basis for the farmer/fisherman single-installment rule (the FTB instructions state the rule; the underlying R&TC section was not archived in this pack); R&TC sections 19142 and 19144 (penalty and exceptions) were not archived here and are cited from the skill's own prior text.

## End of skill

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Talk to a verified accountant
<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for California estimated-tax questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
