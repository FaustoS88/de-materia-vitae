#!/usr/bin/env python3
"""
De Materia Vitae — PPP-Adjusted Budget Planner

Calculates the local purchasing-power-equivalent cost for each budget tier
based on the user's country. Uses World Bank PPP conversion factors.

Usage:
    python budget-planner.py
"""

# PPP conversion factors (inverse): local currency units per int'l dollar
# Source: World Bank, IMF World Economic Outlook
# Lower number = cheaper to live there; Higher = more expensive
# Data is approximate PPP conversion factor for private consumption (LCU per USD)
# Normalized so US = 1.0
PPP_FACTORS = {
    # North America
    "US": 1.0,
    "Canada": 1.1,

    # Europe
    "UK": 0.85,
    "Germany": 0.85,
    "France": 0.85,
    "Italy": 0.75,
    "Spain": 0.7,
    "Portugal": 0.65,
    "Netherlands": 0.95,
    "Switzerland": 1.4,
    "Austria": 0.9,
    "Sweden": 0.9,
    "Norway": 1.2,
    "Denmark": 1.1,
    "Poland": 0.5,
    "Czech Republic": 0.55,
    "Romania": 0.4,
    "Greece": 0.65,
    "Croatia": 0.6,
    "Ireland": 1.0,
    "Belgium": 0.9,
    "Finland": 0.95,

    # Asia
    "India": 0.3,
    "China": 0.4,
    "Japan": 1.0,
    "South Korea": 0.7,
    "Thailand": 0.35,
    "Vietnam": 0.25,
    "Philippines": 0.3,
    "Indonesia": 0.3,
    "Malaysia": 0.35,
    "Singapore": 0.9,
    "Pakistan": 0.2,
    "Bangladesh": 0.2,
    "Sri Lanka": 0.25,

    # Latin America
    "Brazil": 0.35,
    "Mexico": 0.4,
    "Argentina": 0.3,
    "Colombia": 0.35,
    "Chile": 0.5,
    "Peru": 0.35,
    "Ecuador": 0.35,
    "Costa Rica": 0.4,

    # Africa
    "South Africa": 0.35,
    "Nigeria": 0.15,
    "Kenya": 0.25,
    "Egypt": 0.2,
    "Morocco": 0.3,
    "Ethiopia": 0.15,
    "Ghana": 0.25,
    "Tanzania": 0.2,

    # Middle East
    "Turkey": 0.3,
    "Israel": 1.1,
    "UAE": 0.8,
    "Saudi Arabia": 0.6,

    # Oceania
    "Australia": 1.15,
    "New Zealand": 1.05,

    # Eastern Europe / Central Asia
    "Russia": 0.3,
    "Ukraine": 0.25,
    "Kazakhstan": 0.3,
}

# Budget tiers (US baseline per month)
TIERS = {
    "Foundation (Free)": {
        "nutrition": 0,
        "supplements": 0,
        "equipment": 0,
        "testing": 0,
        "total": 0,
        "includes": "Walking, sunlight, meditation, meal timing, bodyweight exercise, sleep hygiene"
    },
    "Essential": {
        "nutrition": 25,  # EVOO, green tea, berries, nuts
        "supplements": 15,  # Basic: vitamin D, omega-3, probiotic
        "equipment": 5,  # Amortized: water filter, blue light glasses
        "testing": 5,  # Amortized: annual blood work
        "total": 50,
        "includes": "Adds EVOO, green tea, basic supplements, water filter, blue light glasses"
    },
    "Complete": {
        "nutrition": 60,  # Premium: wild fish, organic, berries, variety
        "supplements": 40,  # Full stack: allicin, berberine, NAC, etc.
        "equipment": 30,  # Amortized: RO filter, premium glasses, gym
        "testing": 70,  # Amortized: comprehensive testing, GI-MAP, Dexa
        "total": 200,
        "includes": "Adds comprehensive testing, premium supplements, lab work, advanced protocols"
    }
}


def get_ppp_factor(country_code):
    """Get the PPP factor for a country."""
    # Try exact match
    if country_code in PPP_FACTORS:
        return PPP_FACTORS[country_code]

    # Try case-insensitive partial match
    country_lower = country_code.lower()
    for key, value in PPP_FACTORS.items():
        if country_lower in key.lower() or key.lower() in country_lower:
            return value

    return None


def main():
    print("=" * 70)
    print("  De Materia Vitae — PPP-Adjusted Budget Planner")
    print("=" * 70)
    print()

    # Get country
    print("Available countries:")
    for i, country in enumerate(sorted(PPP_FACTORS.keys()), 1):
        end = ", " if i % 6 != 0 else "\n"
        print(f"  {country:<15}", end=end)
    print()

    while True:
        try:
            country = input("\nYour country (name or code): ").strip()
            if not country:
                print("Please enter a country name.")
                continue
            break
        except EOFError:
            return

    ppp = get_ppp_factor(country)

    if ppp is None:
        print(f"\nCountry '{country}' not found in database.")
        print("Using US baseline (1.0) as fallback.")
        ppp = 1.0
        country = "US (fallback)"

    print(f"\nCountry: {country}")
    print(f"PPP Factor: {ppp:.2f} (relative to US)")
    print()

    # Calculate adjusted costs
    print(f"{'Tier':<25} {'US $/mo':<12} {'Your $/mo (PPP-adjusted)':<30} Includes")
    print("-" * 100)

    for tier_name, tier_data in TIERS.items():
        if tier_data["total"] == 0:
            print(f"{tier_name:<25} {'$0':<12} {'$0':<30} {tier_data['includes']}")
        else:
            adjusted = round(tier_data["total"] * ppp)
            print(f"{tier_name:<25} ${tier_data['total']:<11} ${adjusted:<29} {tier_data['includes']}")

    print()
    print("=" * 70)

    # Breakdown for Essential tier
    print("\nDetailed breakdown — Essential tier:")
    print(f"  {'Category':<20} {'US $':<10} {'Your $':<10}")
    print(f"  {'-'*40}")
    for category in ["nutrition", "supplements", "equipment", "testing"]:
        us_val = TIERS["Essential"][category]
        local_val = round(us_val * ppp)
        print(f"  {category.capitalize():<20} ${us_val:<9} ${local_val:<9}")

    print()
    print("=" * 70)
    print("  Note: These are estimates. Actual costs vary by location,")
    print("  brand, season, and availability. Use as a rough guide.")
    print("=" * 70)


if __name__ == "__main__":
    main()
