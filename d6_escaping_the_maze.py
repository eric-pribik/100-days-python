#! /usr/bin/env python3

#######################################################################################################
#                                   Functions
#######################################################################################################
#
# Functions are structured with it's name followed with a set of ( )
# What ever is inside the ( ) will be modified by the function as the input
#
#You can craete your own functions by def and includes (): to seperate it from a variable.
#They can be created a head of time and only run when they are called. 

#Step 1 Define the function
#Step 2 Define what it should do
#Step 3 Call the function
def my_fuction():
    print("Hello")
    print("bye")

my_fuction()
#
#
#######################################################################################################
#                                   While Loops
#######################################################################################################
#
#while something_is_true:
#   Do something repeatedly
count = 5
while count > 0:
    print(count)
    count -= 1

#######################################################################################################
#                                   While Loops
#######################################################################################################
#

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif not front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif not front_is_clear() and wall_on_right():
        turn_left()
