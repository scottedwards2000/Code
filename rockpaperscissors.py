""" This is a simple rock paper scissors game in Python. Here is how it works:

- It imports the random module to generate a random choice for the computer. 

- It defines a list of options - rock, paper, scissors.

- `get_computer_choice()` randomly picks one of these options to be the computer's choice.

- `get_player_choice()` prompts the user to enter their choice and validates that it is one of the valid options.

- `check_winner()` compares the player and computer choices to determine who won using some logic:
  - If they are the same, it's a tie.
  - It calls `beats()` to check if the player's choice beats the computer's, and returns a win for the player if so.
  - Otherwise, it returns a win for the computer.

- `beats()` has some predefined rules for what beats what in rock paper scissors.

- `play_game()` contains the main game loop:
  - It gets the player and computer choices
  - Prints the computer's choice
  - Calls `check_winner()` to print the result
  - Asks if the player wants to play again and breaks out of the loop if not.

- The `if __name__ == '__main__'` block calls `play_game()` to start the game when the module is run.

So in summary, it's a simple logic flow to get input, generate a computer choice, compare the choices, print results, and loop the game. The core logic is in `check_winner()` and `beats()`. """

import random

OPTIONS = ["rock", "paper", "scissors"]

def get_computer_choice():
  return random.choice(OPTIONS)

def get_player_choice():
  while True:
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if choice in OPTIONS:
      return choice

def check_winner(player, computer):
  if player == computer:
    return "Tie!"
  elif beats(player, computer):
    return "You won!"
  return "Computer won!"

def beats(one, two):
  wins = [('rock', 'scissors'), 
          ('paper', 'rock'),
          ('scissors', 'paper')]
  return (one, two) in wins

def play_game():
  while True:
    player = get_player_choice()
    computer = get_computer_choice()
    print("Computer played:", computer) 
    winner = check_winner(player, computer)
    print(winner)
    
    play_again = input("Play again? (y/n) ").lower()
    if play_again != 'y':
      break

if __name__ == '__main__':
  play_game()
