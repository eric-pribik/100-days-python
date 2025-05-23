#! /usr/bin/env python3

#
######################################################################################################
#                                  Scopes
######################################################################################################
#
#There are two different types of scopes, global and local scopes. Local scopes are within a function and gobal scopes are able to be accessed everywhere. 
#  
#
# Global constants are normally declared in ALL_CAPS with a underscore in between.
######################################################################################################
#                                  Modifyting Global Scope
######################################################################################################
#
#enemies = 1
#
#
#def increase_enemies():
#    global enemies
#    enemies += 1
#    print(f"enemies inside function: {enemies}")
#
#
#increase_enemies()
#print(f"enemies outside function: {enemies}")
#
#
#
######################################################################################################
#                                  Final Project
#####################################################################################################
#

import random


answer = random.randint(1,100)
print(answer)
difficutly = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficutly. Type 'easy' or 'hard': ").lower()

def game_mode(guesses,answer):
    while guesses > 0:
        print(f"You have {guesses} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess > answer:
            guesses -= 1
            print(f"Too high.\nGuess again.\nYou have {guesses} attempts remaining to guess the number")
        elif user_guess < answer:
            guesses -= 1
            print(f"Too low.\nGuess again.\nYou have {guesses} attempts remaining to guess the number")
        elif user_guess == answer:
            print(f"You selected the correct number with {guesses} guesses remaining!")
            return
    if guesses == 0:
        print("you ran out of guesses, please restart the program to play again.")

if difficutly == "easy":
    guesses = 10
    game_mode(guesses,answer)
elif difficutly == "hard":
    guesses = 5
    game_mode(guesses,answer)
else:
    print("You did not select a proper entry.")


######################################################################################################
#                                  Final Project Solution
#####################################################################################################

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
