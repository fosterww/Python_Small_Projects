import random

def rock_paper_scissors(me):
    """Game "Rock, Paper, Scissors"""
    choices = ["rock", "paper", "scissors"]
    # Random computer selection
    computer = random.choice(choices)
    print("Computer choose:", computer)
    # We check and compare the elections
    if me == computer:
        return "It's a tie!"
    elif (me == "rock" and computer == "scissors") or \
         (me == "scissors" and computer == "paper") or \
         (me == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"
# Main code 
print("Welcome to Rock, Paper, Scissors!")
me = input("Enter rock, paper, or scissors: ").lower()
if me not in ["rock", "paper", "scissors"]:
    print("Invalid choice! Please enter rock, paper, or scissors.")

print(rock_paper_scissors(me))