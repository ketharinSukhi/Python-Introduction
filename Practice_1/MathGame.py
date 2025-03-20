import random

def generate_question():
   number1 = random.randint(1, 10)
   number2 = random.randint(1, 10)
   operator = random.choice(["+","-","*","/"])

   if operator == "/":
        number1 = number1 * number2

   question = f"{number1}{operator}{number2}"
   answer = eval(question)

   return question, round(answer, 2)

def math_game():
    score = 0
    attempts =int(input("How many times you want to attempt the game : "))

    for _ in range(attempts):
        question, correct_answer = generate_question()
        print(f"Question : {question} = ?")

        try:
            user_answer = float(input("Your answer : "))
            if user_answer == correct_answer:
                print("✅ Correct!\n")
                score += 1
            
            else:
                print(f"❌ Wrong! The correct answer was {correct_answer}\n")
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.\n")

    print(f"Game over! Your final score: {score}/{attempts}")


def main():
    print("\n--------------------------------- WELCOME TO MATH GAME ---------------------------------\n")
    math_game()

if __name__ == "__main__":
    main()