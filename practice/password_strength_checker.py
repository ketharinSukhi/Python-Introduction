import re

def check_password_strength(password):
     strength_criteria = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'\d', password)),
        'special_char': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    
     strength_score = sum(strength_criteria.values())
    
     if strength_score == 5:
        return "Strong"
     elif strength_score >= 3:
        return "Moderate"
     else:
        return "Weak"
     
def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")

if __name__ == "__main__":
     main()