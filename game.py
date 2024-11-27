import random

# Function to display choices and rules
def display_instructions():
    print("\nWelcome to Rock-Paper-Scissors!")
    print("Rules: ")
    print(" - Rock beats Scissors")
    print(" - Scissors beat Paper")
    print(" - Paper beats Rock")
    print("Enter your choice as: rock, paper, or scissors\n")

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Main game function
def rock_paper_scissors():
    # Initialize scores
    user_score = 0
    computer_score = 0

    display_instructions()
    
    while True:
        # Get user's choice
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        while user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            user_choice = input("Enter your choice again: ").lower()

        # Generate computer's choice
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine and display the winner
        result = determine_winner(user_choice, computer_choice)
        if result == "user":
            print("You win this round! 🎉")
            user_score += 1
        elif result == "computer":
            print("Computer wins this round! 😞")
            computer_score += 1
        else:
            print("It's a tie! 🤝")

        # Display current score
        print(f"\nScore: You - {user_score} | Computer - {computer_score}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThank you for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("Congratulations! You are the overall winner! 🏆")
            elif user_score < computer_score:
                print("Computer wins overall! Better luck next time. 🤖")
            else:
                print("It's a tie overall! Well played. 👏")
            break

# Start the game
rock_paper_scissors()
