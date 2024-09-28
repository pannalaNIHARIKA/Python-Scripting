
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
def Guess_number_game():
  def check_answer(guess_number,Actual_number):
    if guess_number > Actual_number:
        print("Too high")
    elif guess_number < Actual_number:
        print("too low")
    else:
        print(f"you got it , the answer was {Actual_number}")
  def difficulty_level(level):
    if level == "easy":
      return 10
    else:
      return 5
    
  Actual_number = random.randint(1,100)
  print(logo)
  print("Welcome to Number Guessing Game")
  print("I am thinking of a number between 1 and 100")
  level = input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
  attempts = difficulty_level(level)
  while attempts > 0:    
      print(f"You have {attempts} attempts remaining to guess the number")
      guess_number = int(input("Make a guess:"))
      check_answer(guess_number,Actual_number)
      while guess_number == Actual_number:
        attempts = 0
      attempts = attempts-1
      if attempts == 0:
       print("you lose")

Guess_number_game()

  
  
  
