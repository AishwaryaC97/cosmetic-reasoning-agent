import os
from dotenv import load_dotenv
from data_mocks import FABRIC_IQ_SEMANTIC_MODEL, FOUNDRY_IQ_KNOWLEDGE_BASE, WORK_IQ_CONTEXT

load_dotenv()

class CosmeticReasoningSystem:
    def __init__(self):
        self.endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
        self.model = os.getenv("AZURE_AI_MODEL_DEPLOYMENT", "gpt-4o")
        
        print("="*60)
        print("INITIALIZING COSMETIC ANALYSIS REASONING SYSTEM")
        print(f"Endpoint: {self.endpoint}")
        print(f"Deployment Model: {self.model}")
        print("="*60)

    def agent_ingredient_liaison(self, product_names: list) -> list:
        """Agent 1: Grounded Catalog Retrieval (Foundry IQ)"""
        print("\n[Agent 1: Ingredient Liaison] Querying Foundry IQ Knowledge Base...")
        extracted_products = []
        for p_name in product_names:
            matched = next((p for p in FOUNDRY_IQ_KNOWLEDGE_BASE if p["name"].lower() == p_name.lower()), None)
            if matched:
                extracted_products.append(matched)
                print(f" -> Found verified product: {matched['name']} (Source: FoundryIQ-KB)")
        return extracted_products

    def agent_dermal_semantic_layer(self, products: list, skin_profile_id: str) -> dict:
        """Agent 2: Contraindication Check (Fabric IQ)"""
        print(f"\n[Agent 2: Dermal Semantic Layer] Checking Fabric IQ Ontology for {skin_profile_id}...")
        profile = FABRIC_IQ_SEMANTIC_MODEL["skin_profiles"].get(skin_profile_id, {"type": "Unknown", "barriers": "Normal"})
        
        all_ingredients = []
        clashes_found = []
        for p in products:
            for ing in p["ingredients"]:
                all_ingredients.append(ing)

        for rule in FABRIC_IQ_SEMANTIC_MODEL["contraindications"]:
            if all(ing in all_ingredients for ing in rule["ingredients"]):
                clashes_found.append(rule)

        return {"skin_type": profile["type"], "detected_clashes": clashes_found}

    def agent_routine_orchestrator(self, analysis: dict, user_id: str) -> dict:
        """Agent 3: Context-Aware Scheduling (Work IQ)"""
        print(f"\n[Agent 3: Routine Orchestrator] Intersecting analysis with Work IQ context for {user_id}...")
        user_context = WORK_IQ_CONTEXT.get(user_id, {})
        schedule = {"AM": [], "PM": []}
        precautions = []

        if user_context.get("daily_sun_exposure_hours", 0) > 2:
            precautions.append("High daily sun exposure detected. Broad-spectrum SPF 50 is required.")

        if analysis["detected_clashes"]:
            print(" -> Conflict found! Splitting product placement into AM and PM blocks...")
            schedule["AM"].append("C-Bright Booster (Vitamin C)")
            schedule["PM"].append("Overnight Reset Serum (Retinol)")
            precautions.append("Split Application applied to prevent high skin irritation.")
        return {"tailored_schedule": schedule, "lifestyle_precautions": precautions}

    def run_pipeline(self, product_requests: list, skin_profile_id: str, user_id: str):
        products = self.agent_ingredient_liaison(product_requests)
        analysis = self.agent_dermal_semantic_layer(products, skin_profile_id)
        routine = self.agent_routine_orchestrator(analysis, user_id)
        
        print("\n" + "="*60)
        print("FINAL REASONING REPORT (COSMETIC ANALYSIS AGENT & PRODUCT ENABLEMENT)")
        print("="*60)
        print(f"Target Profile: {analysis['skin_type']}")
        print(f"AM Routine : {', '.join(routine['tailored_schedule']['AM'])}")
        print(f"PM Routine : {', '.join(routine['tailored_schedule']['PM'])}")
        print("\nSafety Advisories:")
        for prec in routine["lifestyle_precautions"]:
            print(f"{prec}")
        print("="*60)

if __name__ == "__main__":
    requested_products = ["Overnight Reset Serum", "C-Bright Booster"]
    
    orchestrator = CosmeticReasoningSystem()
    orchestrator.run_pipeline(
        product_requests=requested_products, 
        skin_profile_id="SKIN-001", 
        user_id="USER-001"
    )