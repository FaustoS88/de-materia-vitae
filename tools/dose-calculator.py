#!/usr/bin/env python3
"""
De Materia Vitae — Dose Calculator

Bodyweight-based dosing for supplements and substances mentioned in protocols.
Always consult a physician before starting any supplementation.

Usage:
    python dose-calculator.py
"""

import json

# Dosing database: substance → { per_kg_mg, min_mg, max_mg, notes }
DOSES = {
    "L-Glutamine": {
        "per_kg_mg": 70,
        "min_mg": 3000,
        "max_mg": 10000,
        "notes": "Gut lining repair. Take on empty stomach."
    },
    "Omega-3 (EPA+DHA combined)": {
        "per_kg_mg": None,  # Fixed dose
        "min_mg": 1000,
        "max_mg": 3000,
        "notes": "General health: 1-2g/day. Therapeutic: 2-3g/day. Take with food."
    },
    "Vitamin D3": {
        "per_kg_mg": None,
        "min_mg": 1000,  # IU
        "max_mg": 5000,  # IU
        "notes": "Dose depends on baseline blood level. Target: 40-60 ng/mL. Take with fat."
    },
    "Magnesium (glycinate/bisglycinate)": {
        "per_kg_mg": 5,
        "min_mg": 200,
        "max_mg": 400,
        "notes": "Sleep and relaxation. Take 1-2 hours before bed. Avoid oxide form."
    },
    "Probiotic (CFU)": {
        "per_kg_mg": None,
        "min_mg": 10_000_000_000,   # 10B
        "max_mg": 100_000_000_000,  # 100B
        "notes": "Maintenance: 10-50B CFU. Post-antibiotic/post-cleanse: 50-100B CFU."
    },
    "Allicin (stabilized)": {
        "per_kg_mg": 6,
        "min_mg": 450,
        "max_mg": 1350,
        "notes": "Antiparasitic. 450mg up to 3x daily during cleanse. Take on empty stomach."
    },
    "Berberine": {
        "per_kg_mg": 7,
        "min_mg": 500,
        "max_mg": 1500,
        "notes": "Take with meals. Monitor blood glucose if diabetic. Avoid with CYP450 drugs."
    },
    "NAC (N-Acetyl Cysteine)": {
        "per_kg_mg": 8,
        "min_mg": 600,
        "max_mg": 1800,
        "notes": "Antioxidant, liver support, detox support. Take between meals."
    },
    "Zinc Carnosine": {
        "per_kg_mg": None,
        "min_mg": 37,
        "max_mg": 75,
        "notes": "Gut lining healing. 75mg daily. Take on empty stomach."
    },
    "Activated Charcoal": {
        "per_kg_mg": 15,
        "min_mg": 500,
        "max_mg": 2000,
        "notes": "Binds toxins during die-off. Take 2+ hours away from ALL medications/supplements."
    }
}


def format_number(n):
    """Format large numbers with commas or scientific notation."""
    if n >= 1_000_000_000:
        return f"{n / 1_000_000_000:.1f}B"
    elif n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n:,.0f}"
    return f"{n:.0f}"


def calculate_dose(weight_kg: float):
    """Calculate doses for all substances based on bodyweight."""
    results = {}

    for substance, info in DOSES.items():
        if info["per_kg_mg"] is not None:
            dose = info["per_kg_mg"] * weight_kg
            # Clamp to min/max
            dose = max(info["min_mg"], min(dose, info["max_mg"]))
        else:
            # Fixed dose — return range
            dose = (info["min_mg"], info["max_mg"])

        results[substance] = {
            "dose": dose,
            "notes": info["notes"]
        }

    return results


def main():
    print("=" * 60)
    print("  De Materia Vitae — Dose Calculator")
    print("=" * 60)
    print()

    # Get bodyweight
    while True:
        try:
            unit = input("Weight unit [kg/lbs]: ").strip().lower()
            if unit in ("kg", "lbs", "lb"):
                break
            print("Please enter 'kg' or 'lbs'")
        except EOFError:
            return

    while True:
        try:
            weight = float(input(f"Your weight ({unit}): "))
            if weight <= 0 or weight > 500:
                print("Please enter a realistic weight.")
                continue
            break
        except ValueError:
            print("Please enter a number.")
        except EOFError:
            return

    if unit in ("lbs", "lb"):
        weight_kg = weight * 0.453592
    else:
        weight_kg = weight

    print(f"\nBodyweight: {weight_kg:.1f} kg ({weight_kg * 2.20462:.1f} lbs)")
    print()

    # Calculate doses
    results = calculate_dose(weight_kg)

    print(f"{'Substance':<35} {'Dose':<20} Notes")
    print("-" * 90)

    for substance, info in results.items():
        dose = info["dose"]
        if isinstance(dose, tuple):
            dose_str = f"{format_number(dose[0])}–{format_number(dose[1])}"
        else:
            dose_str = format_number(dose)

        # Truncate notes for display
        notes = info["notes"][:50] + "..." if len(info["notes"]) > 50 else info["notes"]
        print(f"{substance:<35} {dose_str:<20} {notes}")

    print()
    print("=" * 60)
    print("  DISCLAIMER: This is not medical advice.")
    print("  Consult a physician before starting any supplementation.")
    print("=" * 60)


if __name__ == "__main__":
    main()
