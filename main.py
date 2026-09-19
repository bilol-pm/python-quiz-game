def show_menu():
    print("\n=== GAME HUB ===")
    print("1. Number Guessing Game")
    print("2. Quiz Game")
    print("3. High Scores")
    print("4. Quit")

def main():
    while True:
        show_menu()
        choice = input("> ").strip()

        if choice == "1":
            print("Number Guessing Game goes here.")
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