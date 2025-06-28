import random

def rock_paper_scissors(me):
    """Игра "Камень, Ножницы, Бумага"""
    # Проверяем, что пользователь ввел корректный выбор
    choices = ["rock", "paper", "scissors"]
    # Выбор компьютера случайным образом
    computer = random.choice(choices)
    print("Computer choose:", computer)
    # Проверяем, сопоставляем выборы
    if me == computer:
        return "It's a tie!"
    elif (me == "rock" and computer == "scissors") or \
         (me == "scissors" and computer == "paper") or \
         (me == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"
# Основной код игры   
print("Welcome to Rock, Paper, Scissors!")
me = input("Enter rock, paper, or scissors: ").lower()
if me not in ["rock", "paper", "scissors"]:
    print("Invalid choice! Please enter rock, paper, or scissors.")

print(rock_paper_scissors(me))