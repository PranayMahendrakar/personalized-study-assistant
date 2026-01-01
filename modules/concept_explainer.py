"""Concept Explainer - Explain difficult concepts"""
from .base import LlamaClient

class ConceptExplainer:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You explain complex concepts in simple, memorable ways using analogies."

    def explain_concept(self, concept: str, context: str = "", level: str = "undergraduate") -> str:
        return self.client.generate(f"Explain this concept at {level} level:\n{concept}\nContext: {context}\n\nUse analogies and examples.", self.system_prompt)

    def create_mnemonic(self, items: str) -> str:
        return self.client.generate(f"Create memorable mnemonics for: {items}", self.system_prompt)
