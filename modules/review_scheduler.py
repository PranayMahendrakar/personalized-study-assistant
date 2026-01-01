"""Review Scheduler - Implement spaced repetition"""
from .base import LlamaClient
from datetime import datetime, timedelta

class ReviewScheduler:
    def __init__(self):
        self.client = LlamaClient()
        self.cards = {}
        self.intervals = [1, 3, 7, 14, 30, 60]

    def add_card(self, card_id: str, content: str):
        self.cards[card_id] = {"content": content, "level": 0, "next_review": datetime.now()}
        return f"Added card: {card_id}"

    def get_due_cards(self) -> list:
        now = datetime.now()
        return [c for c, data in self.cards.items() if data["next_review"] <= now]

    def update_card(self, card_id: str, correct: bool):
        if card_id in self.cards:
            if correct:
                self.cards[card_id]["level"] = min(self.cards[card_id]["level"] + 1, len(self.intervals) - 1)
            else:
                self.cards[card_id]["level"] = 0
            days = self.intervals[self.cards[card_id]["level"]]
            self.cards[card_id]["next_review"] = datetime.now() + timedelta(days=days)
        return f"Updated card: {card_id}"
