#! /usr/bin/env python3

import random

#######################################################################################################
#                                   This tests basic random fuctions
#######################################################################################################

#Prints a random number from (a, b)
random_integer = random.randint(1, 10)
print(random_integer)

#Picks a random foating number from 0-1
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

#Picks a random floating number from (a, b)
random_float = random.uniform(1,10)
print(random_float)


#######################################################################################################
#                                   This tests random coin toss
#######################################################################################################

coin_face = random.randint(0,1)
if coin_face == 0:
   print("Heads")
elif coin_face == 1:
   print("Tails")


#######################################################################################################
#                                   This explains lists
#######################################################################################################

#Creating a list
fruits = ["cherry", "apple", "pear"]
print(fruits[0])

#Change an item in a list
fruits[1] = "strawberry"

#Add an item to the end of the list
fruits.append("blueberry")

#Add multiple items to the end of a list
fruits.extend(["tomato", "grape", "watermelon"])


#######################################################################################################
#                                   This tests lists
#######################################################################################################

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#Option 1 (Prefered)
print(random.choice(friends))

#Option 2
print(friends[random.randint(0, 4)])

#Option 3
random_index = random.randint(0, 4)
print(friends[random_index])


#######################################################################################################
#                                   Nested Lists
#######################################################################################################

fruits = ["cherry", "apple", "pear"]
veggies = ["tomatos", "potatoes", "celery"]

foods = [fruits, veggies]

print(foods)
print(foods[0])
print(foods[0][1])


#######################################################################################################
#                                   Final Project
#######################################################################################################
#
rock = "o"
paper = "-"
scissors = "X"

game_images = [rock, paper, scissors]

player_choice = int(input("Welcome to Rock, Paper, Scissors! What do you choose?\n0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

print("\nYour Choice:")
print(game_images[player_choice])
print("\nComputer chose:\n")
print(game_images[computer_choice])


if player_choice >= 3 or player_choice < 0:
    print("you typed an invalid number, you lose!")
elif player_choice == 0 and computer_choice == 2:
    print("you won")
elif player_choice == 2 and computer_choice == 0:
    print("you lose")
elif player_choice > computer_choice:
    print("you win!")
elif computer_choice > player_choice:
    print("You lose")
elif computer_choice == player_choice:
    print("You Tied!")
