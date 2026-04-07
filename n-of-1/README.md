# N-of-1 Self-Experiments

> Your body is your laboratory.

This directory is for community-submitted self-experiment results. Not anecdotes — structured, measured, honest reports of what happened when you tried a protocol.

---

## Why N-of-1?

Clinical trials tell you what works *on average*. They don't tell you what works *for you*. N-of-1 experiments bridge the gap between population evidence and personal optimization.

**Caveat:** N-of-1 data is hypothesis-generating, not hypothesis-confirming. It tells us what's worth studying, not what's proven.

---

## How to Submit

1. Copy `n-of-1-template.csv` (below) and fill in your data
2. Name the file: `YYYY-MM-DD_protocol-name_initials.csv` (e.g., `2026-04-06_deworming-natural_FS.csv`)
3. Place in this directory
4. Submit a PR

---

## Template

```csv
# HEADER
date_started,date_ended,age,sex,weight_kg,height_cm,country,baseline_issues

# PROTOCOL
protocol_name,protocol_source,dose,frequency,duration,compliance_pct

# DAILY TRACKING (one row per day)
date,sleep_hrs,sleep_quality_1_10,energy_1_10,mood_1_10,focus_1_10,digestion_1_10,pain_1_10,notes

# OUTCOMES
outcome_metric,baseline_value,end_value,change,change_pct,subjective_impression

# ADVERSE EFFECTS
effect,severity_1_10,onset_day,resolved_day,notes

# REFLECTION
would_repeat,confidence_1_10,what_surprised_you,what_would_you_change,advice_for_others
```

---

## Submission Guidelines

### Minimum Requirements
- **Duration:** At least 14 days (longer is better — most protocols need 2+ weeks to show effects)
- **Baseline:** At least 3 days of tracking BEFORE starting the protocol
- **Honesty:** Report adverse effects. Report if it didn't work. Negative results are valuable.
- **Anonymity:** Use initials only. No full names, emails, or identifiable information.

### Good to Have
- Blood work before and after (if applicable)
- Photos (if visible changes)
- Specific measurements (weight, waist, HRV, resting heart rate)
- What else was happening during this period (travel, illness, stress, medication changes)

### Red Flags (will be rejected)
- No baseline measurements
- Duration less than 7 days
- Claims of miraculous cures
- Promoting unlisted substances or protocols
- Identifiable personal information

---

## How to Read N-of-1 Submissions

1. **Check the baseline:** Were they actually symptomatic before? If baseline was already good, room for improvement is limited.
2. **Check the duration:** 2 weeks is barely enough. 4+ weeks is more meaningful.
3. **Check confounders:** Did they change 5 things at once? Then you can't attribute the change to any one thing.
4. **Look for adverse effects:** If there are none listed, either nothing happened or they didn't report honestly.
5. **Consider the person:** Age, sex, weight, baseline health status all matter. Their results may not apply to you.

---

## Example (Abbreviated)

```csv
# HEADER
date_started,date_ended,age,sex,weight_kg,height_cm,country,baseline_issues
2026-01-15,2026-02-15,38,M,75,178,IT,fatigue,brain_fog,bloating

# PROTOCOL
protocol_name,protocol_source,dose,frequency,duration,compliance_pct
Natural Deworming,de-materia-vitae protocols/06,garlic+pumpkin+papaya+herbs,daily,14 days,93%

# DAILY TRACKING (sample)
date,sleep_hrs,sleep_quality_1_10,energy_1_10,mood_1_10,focus_1_10,digestion_1_10,pain_1_10,notes
2026-01-12,7,5,4,6,5,4,0,Baseline day 1
2026-01-13,7.5,5,5,6,5,5,0,Baseline day 2
2026-01-15,7,5,5,6,5,5,0,Started protocol. Felt normal.
2026-01-17,6.5,4,3,5,4,3,1,Day 3: mild headache, bloating. Die-off?
2026-01-20,7.5,7,7,7,7,7,0,Day 6: feeling noticeably better
2026-01-29,8,8,8,8,8,8,0,Day 15: best I've felt in months

# OUTCOMES
outcome_metric,baseline_value,end_value,change,change_pct,subjective_impression
energy_1_10,4.3,7.8,3.5,81%,Substantial improvement
digestion_1_10,4.7,8.2,3.5,74%,Much less bloating
brain_fog_1_10,6,3,-3,-50%,Noticeable clarity improvement

# ADVERSE EFFECTS
effect,severity_1_10,onset_day,resolved_day,notes
headache,3,3,5,Mild, resolved with extra water
loose_stool,4,3,6,Expected during die-off

# REFLECTION
would_repeat,confidence_1_10,what_surprised_you,what_would_you_change,advice_for_others
yes,8,How quickly I felt better (day 5-6),Start with lower herbal doses,Drink more water than you think
```

---

## Contributing Analysis

If you want to aggregate N-of-1 data (e.g., "10 people tried the deworming protocol, here's the average result"), that's even more valuable. Submit analysis as a separate file: `analysis_protocol-name_YYYY-MM-DD.md`

**Minimum for analysis:**
- At least 5 individual submissions
- Standardized outcome measures
- Statistical summary (mean, median, range)
- Adverse effect frequency
- Confounder analysis

---

*Your data belongs here. Even if it didn't work. Especially if it didn't work.*
