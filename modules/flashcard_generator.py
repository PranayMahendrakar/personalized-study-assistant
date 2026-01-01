"""Flashcard Generator - Create flashcards from study materials"""
from .base import LlamaClient

class FlashcardGenerator:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You are an expert educator who creates effective flashcards for studying."

    def generate_flashcards(self, content: str, num_cards: int = 10) -> str:
        return self.client.generate(f"Create {num_cards} flashcards from this content:\n\n{content}\n\nFormat each as:\nQ: [question]\nA: [answer]\n\nFocus on key concepts, definitions, and important facts.", self.system_prompt)

    def generate_cloze_cards(self, content: str) -> str:
        return self.client.generate(f"Create cloze deletion flashcards from:\n\n{content}\n\nFormat: [sentence with ___blank___] → [missing word/phrase]", self.system_prompt)
