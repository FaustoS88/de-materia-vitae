# Contributing to De Materia Vitae

Thank you for wanting to contribute. This project lives on the quality of its evidence and the integrity of its contributors.

---

## Core Rules for Contributions

### 1. Every Claim Needs Sources
- **Minimum:** 1 ancient source + 1 modern peer-reviewed source
- **Ancient sources:** Dioscorides, Hippocrates, Galen, Avicenna, Shennong Bencao Jing, Charaka Samhita, or other documented classical texts with citations
- **Modern sources:** PubMed-indexed journals, Cochrane reviews, WHO guidelines, meta-analyses, or systematic reviews
- **Format:** Provide the PubMed ID (PMID), DOI, or direct URL. Ancient sources should include book/chapter reference.

### 2. Evidence Grade Is Mandatory
Every protocol and claim must carry an evidence grade (see README grading system). If you're unsure, grade it lower. **Overstating evidence is the only unforgivable sin here.**

### 3. No Biohacking Hype
- No "miracle," "reverses aging," "cures," or "detox" (unless referring to actual hepatic/renal detox pathways)
- No N=1 anecdotes presented as general truth
- If it works in mice but not humans yet, say so explicitly
- If the effect size is small, report it honestly

### 4. Protocol Format
All protocols must follow the structure in `protocols/_template.md`. This ensures consistency across the repo.

### 5. Interactions Must Be Documented
If a protocol involves any substance (herb, supplement, drug) that interacts with medications, the interaction must be:
- Documented in the protocol file
- Added to `evidence/interactions.json`

### 6. Cultural Sensitivity
- No condescension toward traditional medicine
- No claiming Western science "discovered" what other cultures have known for millennia
- Frame ancient → modern as "confirmation," not "discovery"

### 7. Pricing Must Be PPP-Adjusted
When suggesting costs, provide the US baseline and note that local costs vary by PPP. Don't present US prices as universal.

---

## How to Add a New Protocol

1. Copy `protocols/_template.md` to a new file
2. Fill in all sections
3. Add sources to `evidence/sources.json`
4. If there are interactions, add to `evidence/interactions.json`
5. If referencing ancient texts, add excerpt to `evidence/ancient-sources/` (or reference existing)
6. Submit PR with a description of what the protocol covers and why it matters

---

## How to Add Ancient Source Material

1. Place file in `evidence/ancient-sources/`
2. Format:
   - Title: `[Author] - [Work] - [Topic]`
   - Include: original text (translated), source edition, book/chapter reference
   - Add a "Relevance" section connecting to modern protocols
3. Only include excerpts directly relevant to protocols in this repo

---

## How to Submit N-of-1 Data

1. Follow the template in `n-of-1/README.md`
2. Anonymize all personal identifiers
3. Include: baseline measurements, protocol details, duration, results, adverse effects
4. Submit to `n-of-1/` directory

---

## Pull Request Checklist

Before submitting, verify:
- [ ] All claims have sources (ancient + modern)
- [ ] Evidence grade is assigned
- [ ] No medical advice language ("you should," "you must" → use "evidence suggests")
- [ ] Interactions documented
- [ ] Follows protocol template
- [ ] Pricing is PPP-referenced, not absolute
- [ ] No hype language
- [ ] Spell-checked and readable

---

## Communication

- Be kind. Be precise. Disagree with ideas, not people.
- If you think a protocol is wrong, argue with evidence — not opinion.
- If you don't know the evidence grade, ask. Don't guess.

---

## Thank You

This project exists because people care about sharing reliable health information. Your contributions make it better.
