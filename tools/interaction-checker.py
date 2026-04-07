#!/usr/bin/env python3
"""
De Materia Vitae — Interaction Checker

Checks if a list of substances/medications have known interactions
based on the interactions database in evidence/interactions.json.

Usage:
    python interaction-checker.py
    python interaction-checker.py "warfarin" "garlic" "green tea"
"""

import json
import os
import sys


def load_interactions():
    """Load the interactions database."""
    # Find the interactions.json relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "..", "evidence", "interactions.json")

    if not os.path.exists(json_path):
        print(f"Error: interactions.json not found at {json_path}")
        sys.exit(1)

    with open(json_path, "r") as f:
        data = json.load(f)

    return data["interactions"]


def check_interactions(substances):
    """Check for interactions between the given substances."""
    interactions = load_interactions()
    found = []

    # Normalize input
    substances_lower = [s.lower() for s in substances]

    for interaction in interactions:
        substance_match = interaction["substance"].lower()
        interacts_match = interaction["interacts_with"].lower()

        for s in substances_lower:
            # Check if any input substance matches the interaction
            if s in substance_match or substance_match in s:
                # Check if any OTHER input substance matches what it interacts with
                for other in substances_lower:
                    if other == s:
                        continue
                    if other in interacts_match or interacts_match in other:
                        found.append(interaction)

    return found


def severity_icon(severity):
    """Return emoji based on severity."""
    icons = {
        "Contraindicated": "🚫",
        "Severe": "⛔",
        "Moderate": "⚠️",
        "Mild": "ℹ️"
    }
    return icons.get(severity, "")


def main():
    print("=" * 70)
    print("  De Materia Vitae — Interaction Checker")
    print("=" * 70)
    print()

    # Get substances from command line or prompt
    if len(sys.argv) > 1:
        substances = sys.argv[1:]
    else:
        print("Enter substances/supplements/medications (one per line, empty line to finish):")
        substances = []
        while True:
            try:
                line = input("  > ").strip()
                if not line:
                    break
                substances.append(line)
            except EOFError:
                break

    if not substances:
        print("No substances provided.")
        return

    print(f"\nChecking interactions for: {', '.join(substances)}")
    print()

    # Check interactions
    found = check_interactions(substances)

    if found:
        print(f"Found {len(found)} interaction(s):\n")

        # Sort by severity
        severity_order = {"Contraindicated": 0, "Severe": 1, "Moderate": 2, "Mild": 3}
        found.sort(key=lambda x: severity_order.get(x["severity"], 4))

        for i, interaction in enumerate(found, 1):
            icon = severity_icon(interaction["severity"])
            print(f"{icon} {i}. {interaction['substance']} ↔ {interaction['interacts_with']}")
            print(f"   Severity: {interaction['severity']}")
            print(f"   Effect: {interaction['effect']}")
            print(f"   Recommendation: {interaction['recommendation']}")
            print()
    else:
        print("✅ No known interactions found between these substances.")
        print()
        print("Note: This does NOT guarantee safety. The database may not be exhaustive.")
        print("Always consult a pharmacist or physician for your specific medication list.")

    print("=" * 70)
    print("  DISCLAIMER: This is not medical advice.")
    print("  Always consult a healthcare professional.")
    print("=" * 70)


if __name__ == "__main__":
    main()
