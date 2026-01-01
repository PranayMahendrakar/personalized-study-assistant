#!/usr/bin/env python3
"""Personalized Study Assistant - Author: Pranay M"""
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.markdown import Markdown
from modules import *

console = Console()

def main():
    console.print(Panel("📚 PERSONALIZED STUDY ASSISTANT 📚\nYour AI-Powered Learning Companion", style="bold blue"))
    
    mods = [("Generate Flashcards", FlashcardGenerator()), ("Create Quiz", QuizGenerator()),
            ("Analyze Notes", NoteAnalyzer()), ("Plan Study", StudyPlanner()),
            ("Explain Concept", ConceptExplainer()), ("Track Progress", ProgressTracker()),
            ("Generate Summary", SummaryGenerator()), ("Practice Problems", PracticeProblemGenerator()),
            ("Build Vocabulary", VocabularyBuilder()), ("Review Schedule", ReviewScheduler())]
    
    while True:
        table = Table(title="Study Tools")
        for i,(n,_) in enumerate(mods,1): table.add_row(str(i), n)
        table.add_row("0", "Exit")
        console.print(table)
        
        c = Prompt.ask("Select", choices=[str(i) for i in range(len(mods)+1)])
        if c == "0": break
        
        idx = int(c) - 1
        if idx == 0:  # Flashcards
            content = Prompt.ask("Paste your notes/content")
            num = int(Prompt.ask("Number of flashcards", default="10"))
            result = mods[idx][1].generate_flashcards(content, num)
        elif idx == 1:  # Quiz
            content = Prompt.ask("Paste content for quiz")
            result = mods[idx][1].generate_quiz(content)
        elif idx == 2:  # Notes
            notes = Prompt.ask("Paste your notes")
            result = mods[idx][1].extract_key_concepts(notes)
        elif idx == 3:  # Planner
            topics = Prompt.ask("Topics to study")
            hours = int(Prompt.ask("Hours available", default="10"))
            result = mods[idx][1].create_schedule(topics, hours)
        elif idx == 4:  # Explainer
            concept = Prompt.ask("Concept to explain")
            result = mods[idx][1].explain_concept(concept)
        elif idx == 5:  # Progress
            result = mods[idx][1].get_recommendations()
        elif idx == 6:  # Summary
            content = Prompt.ask("Content to summarize")
            result = mods[idx][1].generate_summary(content)
        elif idx == 7:  # Problems
            topic = Prompt.ask("Topic for practice problems")
            result = mods[idx][1].generate_problems(topic)
        elif idx == 8:  # Vocabulary
            content = Prompt.ask("Content for vocabulary extraction")
            result = mods[idx][1].extract_vocabulary(content)
        else:  # Review
            result = f"Due cards: {mods[idx][1].get_due_cards()}"
        
        console.print(Panel(Markdown(str(result)), title=mods[idx][0], border_style="blue"))

if __name__ == "__main__": main()
