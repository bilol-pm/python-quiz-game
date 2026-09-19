import random
import json

def show_menu():
    print("\n=== GAME HUB ===")
    print("1. Number Guessing Game")
    print("2. Quiz Game")
    print("3. High Scores")
    print("4. Quit")

def play_number_guessing():
    secret = random.randint(1, 10)
    attempts = 0

    print("\nI'm thinking of a number between 1 and 10.")
    while True:
        guess = input("> ").strip()

        if not guess.isdigit():
            print("Print a valid number")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("Your guess is too low.")
        elif guess > secret:
            print("Your guess is too high.")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            return attempts



def main():
    while True:
        show_menu()
        choice = input("> ").strip()

        if choice == "1":
            attempts = play_number_guessing()
            print(f"Recorded: Solved in {attempts} attempts")
        elif choice == "2":
            print("Quiz Game goes here.")
        elif choice == "3":
                print("High Scores goes here.")
        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("Invalid option!")

def load_questions(path="questions.json"):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def ask_question(item, number):
    print(f"\nQ{number}: {item["question"]}")

    for i, option in enumerate(item["options"], start=1):
        print(f"{i}. {option}")

    while True:
        raw = input("Your answer (1-4): ").strip()

        if not raw.isdigit():
            print("Print a valid number")
            continue

        user_input = int(raw)

        if 1 <= user_input <= len(item["options"]):
            break
        print(f"Please select an option from 1-{len(item["options"])}")

    selected = item["options"][user_input - 1]

    if selected == item["answer"]:
        print("Correct!")
        return True
    else:
        print(f"Wrong. The correct answer was: {item['answer']}")
        return False

questions = load_questions()
ask_question(questions[0], 1)

if __name__ == "__main__":
    main()