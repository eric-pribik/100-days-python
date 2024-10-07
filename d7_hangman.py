#! /usr/bin/env python3

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word then print it

#TODO-2 - ask the user to guess a letter and assign their answer to a variable called guess. Mkae guess lowercase.

#TODO-3 - check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print right if it is, Wrong if it's not. 
import random


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word_list = list(chosen_word)
print(chosen_word)
guess = input("Guess a Letter: ").lower()

#if guess in chosen_word:
#    print("Right")
#else:
#    print("Wrong")

#print(chosen_word)
#for guess in chosen_word_list:
#    if guess in chosen_word_list:
#        print("Right")
#    else:
#        print("Wrong")

for i in range(len(chosen_word) + 1):
    if i == guess:
        print("Right")
    else:
        print("Wrong")
