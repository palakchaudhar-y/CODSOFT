import random

def get_user_choice():
    print("Choose an option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter 1, 2, or 3: ")
    
    while choice not in ["1", "2", "3"]:
        print("Invalid input.")
        choice = input("Please enter 1 for Rock, 2 for Paper, or 3 for Scissors: ")
    
    choice_map = {"1": "rock", "2": "paper", "3": "scissors"}
    return choice_map[choice]

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock-Paper-Scissors (Numeric Edition)!")

    while True:
        user = get_user_choice()
        computer = get_computer_choice()

        print(f"\nYou chose {user.capitalize()}.")
        print(f"Computer chose {computer.capitalize()}.")

        winner = determine_winner(user, computer)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score => You: {user_score} | Computer: {computer_score}")

        play_again = input("\nPlay another round? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("\n🏁 Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()