"""Study Planner - Create personalized study schedules"""
from .base import LlamaClient

class StudyPlanner:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You are a study coach who creates effective learning plans."

    def create_schedule(self, topics: str, hours_available: int, exam_date: str = "") -> str:
        return self.client.generate(f"Create a study schedule:\nTopics: {topics}\nHours available: {hours_available}\nExam date: {exam_date}\n\nInclude spaced repetition and breaks.", self.system_prompt)

    def prioritize_topics(self, topics: str, strengths: str, weaknesses: str) -> str:
        return self.client.generate(f"Prioritize study topics:\nAll topics: {topics}\nStrengths: {strengths}\nWeaknesses: {weaknesses}", self.system_prompt)
