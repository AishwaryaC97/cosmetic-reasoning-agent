# SYNTHETIC DATASET: Fabric IQ
FABRIC_IQ_SEMANTIC_MODEL = {
    "skin_profiles": {
        "SKIN-001": {"type": "Sensitive", "barriers": "Weakened"},
        "SKIN-002": {"type": "Oily/Acne-Prone", "barriers": "Resilient"}
    },
    "ingredients": {
        "ING-101": {"name": "Retinol", "category": "Retinoid", "vegan": True, "target": "Aging/Acne"},
        "ING-102": {"name": "L-Ascorbic Acid", "category": "Vitamin C", "vegan": True, "target": "Brightening"},
        "ING-103": {"name": "Snail Mucin", "category": "Hydration", "vegan": False, "target": "Barrier Repair"}
    },
    "contraindications": [
        {"ingredients": ["Retinol", "L-Ascorbic Acid"], "risk": "High Irritation", "resolution": "Split AM/PM"}
    ]
}

# SYNTHETIC DATASET: Foundry IQ 
FOUNDRY_IQ_KNOWLEDGE_BASE = [
    {
        "product_id": "PRODBETA",
        "brand": "GlowSyntheticIQ",
        "name": "Overnight Reset Serum",
        "ingredients": ["Retinol", "Niacinamide"],
        "claims": ["Cruelty-Free", "Vegan"]
    },
    {
        "product_id": "PROD-BETA",
        "brand": "DermaMock",
        "name": "C-Bright Booster",
        "ingredients": ["L-Ascorbic Acid", "Vitamin E"],
        "claims": ["Vegan"]
    }
]

# SYNTHETIC DATASET: Work IQ 
WORK_IQ_CONTEXT = {
    "USER-001": {
        "daily_sun_exposure_hours": 4,
        "climate": "Sunny",
        "routine_complexity_preference": "Minimalist"
    }
}