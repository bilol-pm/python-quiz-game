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

def load_questions(path="questions.json"):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

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

if __name__ == "__main__":
    main()