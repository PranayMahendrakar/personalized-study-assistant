"""Vocabulary Builder - Build subject-specific vocabulary"""
from .base import LlamaClient

class VocabularyBuilder:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You are a vocabulary specialist who helps students master technical terms."

    def extract_vocabulary(self, content: str) -> str:
        return self.client.generate(f"Extract key vocabulary terms from:\n\n{content}\n\nProvide: term, definition, example usage, related terms.", self.system_prompt)

    def create_vocabulary_exercises(self, terms: str) -> str:
        return self.client.generate(f"Create vocabulary exercises for these terms: {terms}\n\nInclude matching, fill-in-blank, and usage exercises.", self.system_prompt)
