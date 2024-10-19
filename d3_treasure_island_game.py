#!/usr/bin/env python3

#######################################################################################################
#                                   This tests IF ELSE statements
#######################################################################################################

print("Welcome to the rollercoaster!")
height = (int(input("What is your height in cm?\n")))

if height >= 120:
   print("You can ride the Rollercoaster")
else:
   print("You are not tall enought to ride the rollercoaster")


#This Tests IF ELSE statements

number = (int(input("Please choose a number\n")))

if number % 2 == 0:
   print("The number is even.")
else:
   print("The number is odd.")


#######################################################################################################
#                                This test nested IF ELSE statements
#######################################################################################################

print("Welcome to the rollercoaster")
height = (int(input("Please enter your height in CM:\n")))

if height >= 180:
   print("You can ride the rollercoaster")
   age = int(input("What is your age?\n"))
   if age >= 18:
       print("You will have to pay 12 Dollars")
   elif age <=12:
       print("You will have to pay 5 dollars")
   else:
       print("You will have to pay 7 dollars")
else:
   print("Sorry you cannot ride the rollercoaster.")


#######################################################################################################
#                              This testes multiple IF statements in sucession
#######################################################################################################

#print("Welcome to the rollercoaster")
height = int(input("Please enter your hight in CM\n"))
bill = 0

if height >= 180:
   print("You can ride the rollercoaster")
   age = int((input("Please enter your age\n")))
   if age >= 18:
       bill = 12
       print(f"Your price is {bill} dollars")
   elif age < 12:
       bill = 5
       print(f"Your price is {bill} dollars")
   elif age >= 45 and <=55:
       print(your price is free)
   else:
       bill = 7
       print (f"Your price is {bill} dollars")
   
   photo_answer = input("Do you want to have a picture taken? y or n\n")
   if photo_answer == "y":
       bill += 3
       print(f"your ticket price will cost {bill} dollars")
else:
   print("Sorry you cannot ride the rollercoaster")


#######################################################################################################
#                                   Pizza Order exercise
#######################################################################################################

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizzs do you want? S, M, or L: \n")
pepperoni = input("Do you want pepperoni on your pizza Y or N: \n")
extra_cheese = input("Do you want extra cheese? Y or N: \n")
total = 0

if size == "S" or "s":
   total += 15
elif size == "M" or "s":
   total += 20
elif size == "L" or "l":
   total += 25
else:
   print("You did not enter a correct size")

if pepperoni == "Y" or "y":
   if size == "S" or "s":
       total += 2
   else:
       total += 3
       
if extra_cheese == "Y" or "y":
   total += 1

print(f"your total bill is: ${total}.")


#######################################################################################################
#                                   Final Project
#######################################################################################################
#
print("Welcome to Treasure Island!\nYour mission is to find the treasire.\nYou're at a cross road. Where do you want to go?")
crossroad = input('       Type "left" or "right"\n').lower()
if crossroad == "left":
    lake = input("You've come to a lake. There is an island in the middle of the lake\n type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if lake == "wait":
        door = input("you arrived to the island unharmed. There is a house with 3 doors. One Red, one Yellow, one Blue. Which color do you choose?\n").lower()
        if door == "yellow":
            print("You found the teasure! You Win!")
        elif door == "red":
            print("You were burned by fire. Game Over.")
        elif door == "blue":
            print("You were eaten by beasts. Game Over")
        else:
            print("Game Over")
    else:
        print("You were eaten by a trout. Game Over.")
else:
    print("You Fell into a hole. Game Over.")