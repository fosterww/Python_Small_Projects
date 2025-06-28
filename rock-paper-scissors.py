def rock_paper_scissors(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"
    
# Example usage:
player1 = input("Player 1, enter rock, paper, or scissors: ").lower()
player2 = input("Player 2, enter rock, paper, or scissors: ").lower()
print(rock_paper_scissors(player1, player2))