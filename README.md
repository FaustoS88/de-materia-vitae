<p align="center">
  <img src="assets/logo.png" alt="De Materia Vitae" width="200" />
</p>

<h1 align="center">De Materia Vitae</h1>

<p align="center">
  Ancient practice × Modern evidence — an open-source, evidence-graded guide for healthspan and longevity.<br/>
  <a href="https://demateriavitae.duckdns.org">demateriavitae.duckdns.org</a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License" /></a>
  <img src="https://img.shields.io/badge/evidence-graded-4a6741" alt="Evidence Graded" />
  <img src="https://img.shields.io/badge/protocols-6-c4722f" alt="6 Protocols" />
  <img src="https://img.shields.io/badge/languages-4-3a6b8c" alt="4 Languages" />
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome" />
</p>

<p align="center">
  <em>Six practices, each graded against the trials that tested it. The classical claims that didn't survive them aren't here.</em>
</p>

---

## How the evidence is checked

Every line in a protocol that cites a study carries a PMID. `tools/check-citations.py` queries PubMed for each one and exits non-zero when the first author, the year or the journal doesn't match the record, or when a line quotes a title that differs from it. The same run fails when a translation doesn't cite every PMID its English original cites. It runs on every pull request, including the ones the translation workflow opens, where a model drafts the Spanish and Italian and this script is what decides.

The classical sources are catalogued apart, in `evidence/ancient-sources/`, with the edition and the translation used, so a reference points to a book and a page rather than to "tradition".

---

## What Is This?

An open-source, evidence-graded, living document for maintaining a human body.

Not a diet book. Not a biohacking blog. Not a medical textbook. Something between all three: **a practical operating manual** that starts from what the classical texts recommended and keeps only what the evidence after them supports.

1. **The classical texts as leads, not evidence** — Dioscorides' *De Materia Medica* (60 AD), Hippocrates' *Regimen*, Avicenna's *Canon of Medicine* (1025), the *Shennong Bencao Jing* (200 AD), the *Charaka Samhita* (400 BC). These record what people used for centuries, which is a reason to look and not a reason to believe: bloodletting has the same pedigree. Every practice taken from them is graded on the trials that came later.
2. **Modern evidence standards** — PubMed-indexed research, Cochrane reviews, WHO guidelines, meta-analyses. Each claim carries a grade and a PMID you can open.

A claim needs at least one classical source and one peer-reviewed one, and the grade comes from the second.

---

## Philosophy

- **Compounding, not perfection.** Small daily practices, stacked over decades. That's the entire game.
- **Ancient + modern, not either/or.** Traditional use says where to look; a trial says whether to believe it. When the two disagree, the trial wins and the practice loses its place here.
- **Transparent uncertainty.** We tell you exactly what's proven, what's plausible, and what's traditional. No hype.
- **Accessible to everyone.** Three budget tiers with PPP-adjusted pricing so whether you're in Mumbai, Milan, or Minneapolis, you know what this costs in your reality.
- **Action over reading.** This is a decision tree, not a bibliography. You open it, answer a few questions, and get a protocol.

---

## Start Here: Decision Tree

```
What do you want to optimize for?
│
├── A. "I want to live longer and healthier" → HEALTHSPAN FOUNDATION
│   Start with: Nutrition (1-8) + Movement (9-10) + Sleep (13)
│   Add after 30 days: Stress (14) + Fasting (15) + Environment (11-12)
│   Deworming (16): only where worms are common or after a positive stool test
│   → See protocols/01-nutrition.md through protocols/06-systemic-maintenance.md
│
├── B. "I feel like shit right now" → SYMPTOM PATH
│   │
│   ├── Chronic fatigue?
│   │   1. Check: sleep quality, iron/B12/ferritin (blood test)
│   │   2. If normal → try: microbiome reset, blue light glasses
│   │   3. If persists → physician (thyroid, sleep apnea, depression screening)
│   │   → See protocols/03-sleep-circadian.md + protocols/06-systemic-maintenance.md (testing schedule)
│   │
│   ├── Can't sleep / poor sleep?
│   │   1. Start: blue light glasses (red lens 2-3h before bed), no caffeine after 2pm
│   │   2. Add: 10-min breathwork, consistent sleep/wake time
│   │   3. Check: room temperature (18-20°C), darkness, noise
│   │   → See protocols/03-sleep-circadian.md
│   │
│   ├── Brain fog / can't focus?
│   │   1. Start: sleep protocol (above), omega-3 (fatty fish or algal oil)
│   │   2. Add: green tea (EGCG + L-theanine), daily walking
│   │   3. If persists → physician; a stool test if you have been where worms are common
│   │   → See protocols/01-nutrition.md + protocols/03-sleep-circadian.md
│   │
│   ├── Digestive issues (bloating, irregularity)?
│   │   1. Start: fermented foods daily, 30g+ fiber, eliminate ultra-processed food
│   │   2. Add: probiotic (50B CFU), L-glutamine, identify food intolerances
│   │   3. If persists → physician and a stool test; deworming only if it is positive
│   │   → See protocols/06-systemic-maintenance.md
│   │
│   └── Joint pain / low energy / body feels old?
│       1. Start: resistance training (2-3×/week), omega-3, daily walking
│       2. Add: EVOO as primary fat, berries daily, vitamin D check
│       3. If persists → physician (inflammatory markers, CRP, ESR)
│       → See protocols/02-movement.md + protocols/01-nutrition.md
│
├── C. "I want to be systematic about this" → FULL STACK
│   Month 1: Nutrition (all 8 items) + Movement (walking daily)
│   Month 2: Add resistance training + blue light glasses
│   Month 3: Add fasting window + meditation
│   Month 4: Add water filter + sunscreen
│   Month 6: Blood work, adjust based on biomarkers
│   → See all protocols/ files, use trackers/ for logging
│
└── D. "I just want the checklist" → QUICK REFERENCE
    See the Quick Reference section at the bottom of each protocol file.

```

---

## Budget Tiers

Every protocol includes three cost tiers. We use **PPP-adjusted pricing** (Purchasing Power Parity) so the cost is fair regardless of where you live.

| Tier | Concept | What's included |
|------|---------|-----------------|
| **Foundation** | Free | Walking, sunlight, meditation, meal timing, bodyweight exercise, sleep hygiene |
| **Essential** | ~$30-60/mo (US PPP baseline) | Adds EVOO, green tea, basic supplements, water filter, blue light glasses |
| **Complete** | ~$150-300/mo (US PPP baseline) | Adds comprehensive testing, premium supplements, lab work, advanced protocols |

Your local cost = US baseline × your country's PPP factor (inverse). We provide a calculator: `tools/budget-planner.py`

**Example:** If the Essential tier is $50/mo in the US:
- 🇮🇹 Italy (PPP ~0.75): ~$38/mo equivalent
- 🇮🇳 India (PPP ~0.30): ~$15/mo equivalent
- 🇨🇭 Switzerland (PPP ~1.40): ~$70/mo equivalent

Everyone pays roughly the same *proportion* of their local purchasing power.

---

## Repository Structure

```
de-materia-vitae/
├── README.md                    ← You are here
├── CONTRIBUTING.md              ← How to add protocols, evidence standards
├── CODE_OF_CONDUCT.md
│
├── protocols/
│   ├── 01-nutrition.md          ← Olive oil, greens, fish, nuts, tea, fermented, grains, berries
│   ├── 02-movement.md           ← Resistance training, walking
│   ├── 03-sleep-circadian.md    ← Blue light glasses, sleep optimization
│   ├── 04-stress-recovery.md    ← Meditation, breathwork
│   ├── 05-environment.md        ← Water filter, sunscreen, air quality
│   ├── 06-systemic-maintenance.md ← Deworming, testing schedule
│   └── _template.md             ← Template for new protocols
│
├── evidence/
│   ├── sources.json             ← Structured evidence database (PubMed + ancient sources)
│   ├── interactions.json        ← Drug/herb/supplement interaction matrix
│   └── ancient-sources/         ← Translated excerpts from classical texts
│       ├── dioscorides-de-materia-medica.md
│       ├── hippocrates-regimen.md
│       ├── avicenna-canon-of-medicine.md
│       └── README.md
│
├── trackers/
│   ├── daily-log.csv            ← Daily health/symptom tracking
│   ├── protocol-comparison.csv  ← Before/after protocol comparison
│   └── biomarker-trends.csv     ← Blood work over time
│
├── tools/
│   ├── dose-calculator.py       ← Bodyweight-based dosing
│   ├── interaction-checker.py   ← Safe combination validator
│   └── budget-planner.py        ← PPP-adjusted cost estimator
│
├── translations/
│   ├── es/                      ← Spanish
│   ├── it/                      ← Italian
│   └── fr/                      ← French
│
└── n-of-1/
    └── README.md                ← How to submit your self-experiment results
```

---

## Evidence Grading

Every claim in this repo carries an evidence grade:

| Grade | Meaning | Example |
|-------|---------|---------|
| ★★★★★ | Multiple RCTs, meta-analyses, WHO/medical guidelines | Albendazole for parasites, EVOO for cardiovascular health |
| ★★★★☆ | At least one RCT + strong mechanistic evidence | Green tea/EGCG for metabolic health |
| ★★★☆☆ | Small human studies + consistent observational data | Garlic/allicin for Giardia clearance |
| ★★☆☆☆ | Traditional use + in vitro/animal evidence | Pumpkin seeds for helminth paralysis |
| ★☆☆☆☆ | Traditional use only, mechanistic plausibility | Black walnut hull for parasites |
| ☆☆☆☆☆ | Anecdotal only — **not included in this repo** | — |

We require **minimum ★★☆☆☆** for inclusion, AND an ancient source reference.

---

## Important Disclaimers

**This is not medical advice.** This is information. Share it with your doctor. If you have symptoms, see a physician. If you take medications, check interactions (we provide a tool: `tools/interaction-checker.py`). If you are pregnant, nursing, or have a chronic condition, consult a specialist before starting any protocol.

**We are not responsible for what you do with this information.** That's standard open-source license language, but it's also real: your body is yours, we're just sharing what we've found useful.

---

## License

[MIT License](LICENSE) — free to use, share, modify, build upon. We only ask that you credit this project and share your improvements back.

---

*"Let food be thy medicine and medicine be thy food."* — Hippocrates, ~400 BC

*"For it is the body that we must attend to first."* — The Canon of Medicine, Avicenna, 1025 AD

We're still attending to the same body. The tools just got better.
