#! /usr/bin/env python3

#######################################################################################################
#                                   This is a basic For Loop
#######################################################################################################
#
# for item in list_of_items:
#    #Do Something to each item
#
#fruits = ["Apple", "Peach", "Pear"]
#for fruit in fruits:
#    print(fruit)
#    print(fruit + " pie")
#    print(fruits)
#
#
#######################################################################################################
#                                   This tests basic For Loops
#######################################################################################################
#student_scores = [178, 172, 192, 199, 49, 38, 193, 199, 24, 48, 183, 42, 173, 182, 199, 191, 89, 101, 102]
#
##Using sum function
#total_exam_score = sum(student_scores)
#print(total_exam_score)
#
##Primative way without sum function
#total_score = 0
#for score in student_scores:
#    total_score += score
#print(total_score)
#
##using max function
#print(max(student_scores))
#
##Primative way without max function
#highest_score = 0
#for score in student_scores:
#    if score > highest_score:
#        highest_score = score
#print(highest_score)
#
#
#######################################################################################################
#                                   This tests basic For Loops with range()
#######################################################################################################
#
#The range() allows you to generate a range of numbers to loop through, so you don't have to create a list
#The range () need to be in conjuction with another function i.e. For Loop and cannot stand on its own
#i.e print(range(1, 10, 2) would NOT work 
# Also, 10 would not be included in that range, only 1-9 are. The final number is the step (1 if left blank)
#
#for number in range(1, 10):
#    print(number)
#
#sum = 0
#for number in range(1, 101):
#    sum +=number
#print(sum)
#
#
#######################################################################################################
#                                   FizzBuzz Coding Challenge
#######################################################################################################
#
#for number in range(1, 101):
#    if number % 3 == 0 and number % 5 == 0:
#        print("FizzBuzz")
#    elif number % 3 == 0:
#        print("Fizz")
#    elif number % 5 == 0:
#        print("Buzz")
#    else:
#        print(number)
#
#
#######################################################################################################
#                                   Final Project
#######################################################################################################
#
#import random
#
##Lists for each possible character
#letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
#
##Inputs to select how many of each chararcter to choose
#print("Welcome to the PyPassword Generator!")
#nr_letters = int(input("How many letters would you like in your password\n"))
#nr_numbers = int(input("How many numbers would you like\n"))
#nr_symbols = int(input("How many symbols would you like\n"))
#
#password = []
#for letter_item in range(0, nr_letters):
#    new_letter = random.randint(0, 52)
#    temp_letter = letters[new_letter]
#    password.append(temp_letter)
#
#for number_item in range(0, nr_numbers):
#    new_number = random.randint(0, 10)
#    temp_number = numbers[new_number]
#    password.append(temp_number)
#
#for symbol_item in range(0, nr_symbols):
#    new_symbol = random.randint(0, 10)
#    temp_symbol = symbols[new_symbol]
#    password.append(temp_symbol)
#
#random.shuffle(password)
#print(*password, sep="")
#
#
#######################################################################################################
#                                   Final Project Answer
#######################################################################################################
#
import random
import string_utils

#Lists for each possible character
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

#Inputs to select how many of each chararcter to choose
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password\n"))
nr_numbers = int(input("How many numbers would you like\n"))
nr_symbols = int(input("How many symbols would you like\n"))

#Easy Level
password = ""
for char in range(0, nr_letters):
    password += random.choice(letters)

for char in range(0, nr_symbols):
    password += random.choice(symbols)

for char in range(0, nr_numbers):
    password += random.choice(numbers)

print(password)
