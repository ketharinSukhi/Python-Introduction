
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        
        
class Quiz:
    def __init__(self, file_path):
        self.questions = self.questions_load(file_path)
        self.score = 0


    







quiz =Quiz("Quiz.txt")
quiz.run_quiz()