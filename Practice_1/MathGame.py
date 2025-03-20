import random

def generate_question():
   number1 = random.randint(1, 100)
   number2 = random.randint(1, 100)
   operator = random.choice(["+","-","*","/"])

   if operator == "/":
        number1 = number1 / number2

   question = f"{number1}{operator}{number2}"
   answer = eval(question)

   return question, round(answer, 2)

def math_game():
    score = 0
    attempts =10

    for _ in range(attempts):
        question, correct_answer = generate_question()
        print(f"Question : {question} = ?")

        try:
            user_answer = float(input("Your answer : "))
             if user_answer == correct_answer:
                    print("✅ Correct!\n")
                score += 1




def main():
    print("WELCOME TO MATH GAME")


if __name__=="__main":
    main()