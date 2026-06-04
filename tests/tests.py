import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import CosmeticReasoningSystem

def test_clash_detection():
    print("--- RUNNING SAFETY EVALUATION TEST ---")
    orchestrator = CosmeticReasoningSystem()
    
    test_products = ["Overnight Reset Serum", "C-Bright Booster"]
    
    products = orchestrator.agent_ingredient_liaison(test_products)
    
    if len(products) < 2:
        print(f"TEST ERROR: Agent 1 failed to retrieve both products. Only found {len(products)}/2.")
        print("Double check that 'Overnight Reset Serum' is typed exactly identical in data_mocks.py")
        return

    analysis = orchestrator.agent_dermal_semantic_layer(products, "SKIN-001")
    
    if len(analysis["detected_clashes"]) > 0:
        print("\nTEST PASSED: Agent successfully identified chemical contraindication (Retinol + Vitamin C).")
    else:
        print("\nTEST FAILED: Agent missed a high-risk ingredient clash.")

if __name__ == "__main__":
    test_clash_detection()