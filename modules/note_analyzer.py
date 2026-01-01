"""Note Analyzer - Analyze and structure lecture notes"""
from .base import LlamaClient

class NoteAnalyzer:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You are an expert at analyzing and organizing study materials."

    def extract_key_concepts(self, notes: str) -> str:
        return self.client.generate(f"Extract and list the key concepts from these notes:\n\n{notes}\n\nOrganize by importance and relationships.", self.system_prompt)

    def identify_gaps(self, notes: str, topic: str) -> str:
        return self.client.generate(f"Identify knowledge gaps in these notes about {topic}:\n\n{notes}\n\nWhat topics need more coverage?", self.system_prompt)
