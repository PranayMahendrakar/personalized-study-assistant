"""Practice Problem Generator - Generate practice problems"""
from .base import LlamaClient

class PracticeProblemGenerator:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You create educational practice problems with detailed solutions."

    def generate_problems(self, topic: str, difficulty: str = "medium", num: int = 5) -> str:
        return self.client.generate(f"Create {num} {difficulty} practice problems for: {topic}\n\nProvide step-by-step solutions.", self.system_prompt)

    def generate_word_problems(self, topic: str, context: str = "real-world") -> str:
        return self.client.generate(f"Create word problems for {topic} with {context} context. Include solutions.", self.system_prompt)
