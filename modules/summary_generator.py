"""Summary Generator - Generate study summaries"""
from .base import LlamaClient

class SummaryGenerator:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You create concise, effective study summaries."

    def generate_summary(self, content: str, length: str = "medium") -> str:
        return self.client.generate(f"Create a {length} study summary of:\n\n{content}\n\nHighlight key points and relationships.", self.system_prompt)

    def create_cheat_sheet(self, topic: str, content: str) -> str:
        return self.client.generate(f"Create a one-page cheat sheet for {topic}:\n\n{content}\n\nInclude formulas, key terms, and quick references.", self.system_prompt)
