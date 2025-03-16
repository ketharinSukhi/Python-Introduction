
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def check_answer(self, given_answer):

        return self.answer.lower() == given_answer.lower()
        
        
class Quiz:
    def __init__(self, file_path):
        self.questions = self.questions_load(file_path)
        self.score = 0

    def questions_load(self, file_path):
        questions = []
        try:
            with open(file_path, "r") as file:
                for line in file:
                    text, answer = line.strip().split(",")
                    questions.append(Question(text, answer))
        except FileNotFoundError:
            print("Error: Quiz file not found")
            return []
        return questions
 


    







quiz =Quiz("Quiz.txt")
quiz.run_quiz()