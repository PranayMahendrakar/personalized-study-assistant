"""Quiz Generator - Generate quizzes from study materials"""
from .base import LlamaClient

class QuizGenerator:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You are an educator creating comprehensive quizzes to test understanding."

    def generate_quiz(self, content: str, quiz_type: str = "mixed", num_questions: int = 10) -> str:
        return self.client.generate(f"Create a {quiz_type} quiz with {num_questions} questions from:\n\n{content}\n\nInclude: multiple choice, true/false, and short answer. Provide answer key at end.", self.system_prompt)

    def generate_practice_test(self, topics: str, difficulty: str = "medium") -> str:
        return self.client.generate(f"Create a practice test for topics: {topics}\nDifficulty: {difficulty}\n\nInclude varied question types and comprehensive coverage.", self.system_prompt)
