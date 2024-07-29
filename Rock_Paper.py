import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissor']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == 'rock' and computer_choice == 'scissor') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissor' and computer_choice == 'paper'):
        return "You win!"
    
    return "You lose!"

def main():
    print("Welcome to Rock-Paper-Scissor!")
    user_choice = input("Enter rock, paper, or scissor: ").lower()
    
    if user_choice not in ['rock', 'paper', 'scissor']:
        print("Invalid choice. Please enter rock, paper, or scissor.")
        return

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
      main()