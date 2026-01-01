"""Progress Tracker - Track learning progress"""
from .base import LlamaClient
import json

class ProgressTracker:
    def __init__(self):
        self.client = LlamaClient()
        self.progress = {}

    def record_session(self, topic: str, score: float, time_spent: int):
        if topic not in self.progress:
            self.progress[topic] = []
        self.progress[topic].append({"score": score, "time": time_spent})
        return f"Recorded: {topic} - Score: {score}%, Time: {time_spent} min"

    def get_recommendations(self) -> str:
        return self.client.generate(f"Based on this progress data, what should the student focus on?\n{json.dumps(self.progress)}", "You are a learning analytics expert.")

    def export_progress(self) -> str:
        return json.dumps(self.progress, indent=2)
