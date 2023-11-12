import random

def generate_random_number(min, max):
    """
    Generate a random integer between min and max.
    """
    return random.randint(min, max)

def choose_random_operator():
    return random.choice(['+', '-', '*'])

def calculate_expression(num1, num2, operator):
    expression = f"{num1} {operator} {num2}"
    if operator == '+': result = num1 + num2
    elif operator == '-': result = num1 - num2
    else: result = num1 * num2
    return expression, result

def run_math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_number(1, 10)
        num2 = generate_random_number(1, 5)
        operator = choose_random_operator()

        problem, answer = calculate_expression(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")
        user_answer = int(user_answer)

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    run_math_quiz()
