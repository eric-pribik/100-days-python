#! /usr/bin/env python3

#######################################################################################################
#                                   Final Project (My Attempt)
#######################################################################################################

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word then print it

#TODO-2 - ask the user to guess a letter and assign their answer to a variable called guess. Mkae guess lowercase.

#TODO-3 - check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print right if it is, Wrong if it's not. 

#TODO-4 Create a string = "placeholder" with the same number of blanks as the chosen word

#TODO-5 Create a "display" that puts the guess letter in the right 

#TODO-6 Use a while loop to let the user guess again

#TODO-7 Change the for loop so that you keep the previous correct 


import random
import string


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word_list = list(chosen_word)
chosen_word_lenght = len(chosen_word)
placeholder = ""
display = ""
lives = 6

print(chosen_word)


for i in range(chosen_word_lenght):
   placeholder += "_"

display = placeholder
#
print(placeholder)
guess = input("Guess a Letter: ").lower()


#for letter in chosen_word:
   if letter == guess:
       display += letter
   else:
       display += "_"

matched_letters_list = []
new_display = ""

game_over = False

while not game_over:
   print(display)
   guess = input("Guess a Letter: ").lower()
   for letter in chosen_word:
       if letter == guess:
           matched_letters_list.append(guess)
       elif "_" in display == False:
           print("You Won!")    

print(f"You lost! The word was {chosen_word}")
print(placeholder)
print("1")
print(display)
print("2")
print(new_display)
print("3")
print(matched_letters_list)
   print(f"You loose a life! your total lives remaining are {lives}.\n{display}")
       lives -= 1
   print(display)


#######################################################################################################
#                                   Final Project (Solution)
#######################################################################################################
#
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.

game_over = False
lives = 6
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""


# TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose!")
    if "_" not in display:
        print("You Win!")
        game_over = True
    else:
        print

    print(f"You have {lives} left!")    
#    print(stages[lives])
