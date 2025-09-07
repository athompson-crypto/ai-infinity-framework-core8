"""
AI Infinity Framework™ — Core8 Public Edition
Author: Andre Thompson Sr. © 2024–2025
Trademark: AI Infinity Framework™ (USPTO Serial No. 98728996)

This file provides a reference Python implementation of the Core8 logic evaluator.
"""

from typing import Dict, Any


class Core8Framework:
    def __init__(self, case: str = ""):
        self.case = case
        self.dimensions: Dict[str, Any] = {
            "WHO": None,
            "WHAT": None,
            "WHEN": None,
            "WHERE": None,
            "WHY": None,
            "HOW": None,
            "IF": None,
            "IMPACT": None,
        }

    def set_dimension(self, key: str, value: Any) -> None:
        """Assign a value to one of the Core8 dimensions."""
        if key not in self.dimensions:
            raise KeyError(f"{key} is not part of Core8.")
        self.dimensions[key] = value

    def evaluate(self) -> Dict[str, Any]:
        """Return a structured evaluation across all eight dimensions."""
        return {
            "case": self.case,
            "evaluation": self.dimensions
        }


# Example usage
if __name__ == "__main__":
    framework = Core8Framework(case="Public Example")

    framework.set_dimension("WHO", "Researchers, educators, contributors")
    framework.set_dimension("WHAT", "Evaluate Core8 as open framework logic")
    framework.set_dimension("WHEN", "2025 and beyond")
    framework.set_dimension("WHERE", "Global STEM ecosystem")
    framework.set_dimension("WHY", "Advance safe, structured AI reasoning")
    framework.set_dimension("HOW", "Open-source collaboration & testing")
    framework.set_dimension("IF", "Conditions, risks, and assumptions documented")
    framework.set_dimension("IMPACT", "Shared understanding, improved AI governance")

    print(framework.evaluate())
