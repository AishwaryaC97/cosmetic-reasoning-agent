# Multi-Agent Cosmetic Analysis & Product Enablement System
**Track:** Battle #2 - Reasoning Agents with Microsoft Foundry (Custom Domain Adaptation)

## Project Overview
This project adapts the reasoning agent enterprise framework into an automated **Cosmetic Analysis & Product Enablement Agent**. The system helps retail advisors, product formulators, and consumers analyze skin product ingredient layers, detect complex chemical contraindications, and safely orchestrate application schedules based on lifestyle signals.

---

## Multi-Agent Architecture & Microsoft IQ

The solution implements a multi-step reasoning pipeline utilizing four distinct agents, mapping directly to the core tenets of the Microsoft IQ intelligence layers:

1. Ingredient Agent (Foundry IQ Grounding Layer): Simulates a multi-source knowledge base retrieval. It queries the product catalog database (`FOUNDRY_IQ_KNOWLEDGE_BASE`), extracts verified ingredient lists, and returns cited, permission-aware answers rather than hallucinated text.
2. **Dermal-Semantic Layer Agent (Fabric IQ Semantic Layer):** Operates as the business meaning framework. It maps the structural relationships between user skin profiles, target conditions, and active chemical compound ingredients. It evaluates complex multi-ingredient contraindications (such as `Retinol` + `L-Ascorbic Acid` interactions) using established relationship trees.
3. **Routine Orchestrator Agent (Work IQ Context Layer):** Captures individual environmental exposure context and daily user habits (such as peak UV sun exposure hours and routine complexity preferences) to logically construct and adapt safe AM/PM application schedules.
4. **Safety & Compliance Verifier (Responsible AI Guardrail):** Acts as an automated Verifier pattern to ensure no hazardous advice escaping the orchestration pipeline violates safe topical threshold limits.

---

## Evaluation & Test-Driven Safety
To satisfy the challenge requirement for robust application evaluation, implemented an automated safety verification framework (`tests/tests.py`). This script intentionally stress-tests the multi-agent system with known conflicting ingredients to assert that the **Fabric IQ Dermal Layer** successfully flags product interactions.

---

## Local Setup & Execution Instructions

### Prerequisites
* Python 3.10+
* Visual Studio Code

### Installation
1. Clone this repository to your local machine.
2. Create and activate your isolated virtual environment:
   ```bash
   py -m venv .venv
   .venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Create a .env file in the root directory and specify your Azure AI Project endpoints
AZURE_AI_PROJECT_ENDPOINT="[https://your-foundry-endpoint.openai.azure.com/](https://your-foundry-endpoint.openai.azure.com/)"
AZURE_AI_MODEL_DEPLOYMENT="gpt-4o"

5. To run the end-to-end multi-agent orchestration reasoning system
python src/app.py

6. To test it:
python tests/tests.py

Note: This project uses a fabricated data 
