#! /usr/local/bin/python3
#######################################################################################################
#                                         Functions with outputs
#######################################################################################################
#
# def format_name(f_name, l_name):
#    formated_f_name = f_name.title()
#    formated_l_name = l_name.title()
# # When a function reaches a "return" it will know it is the end of the function
# # Anything after "return" will never run. It can only be "return" too
#    return f'{formated_f_name} {formated_l_name}'

# formatted_string = format_name("eric", "pribik")

# print(formatted_string)

# def function_1(text):
#    return text + text

# def function_2(text):
#    return text.title()

# #Example of a fuction using another function as its input
# output = function_2(function_2("hello"))
# print(output)

# #Using input with two functions for its fucntion input
# print(format_name(input("What is your first name?"), "What is your last name?"))

# #Example of using an if statement using return to end a fucntion
# def format_name(f_name, l_name):
#    if f_name == "" or l_name == "":
#        return
#    formated_f_name = f_name.title()
#    formated_l_name = l_name.title()
#
#
#
#######################################################################################################
#                                         Leap Year Exsersise
#######################################################################################################
#
#- on every year that is divisible by 4 with no remainder
#- except every year that is evenly divisible by 100 with no remainder 
#- unless the year is also divisible by 400 with no remainder  

# def is_leap_year(year):
#     # Write your code here. 
#     # Don't change the function name.
#     result = False
#     if year % 4 == 0:
#         if year % 100 != 0:
#             result = True
#         elif year % 100 == 0:
#             if year % 400 == 0:
#                 result = True
#     print(result)

# is_leap_year(1989)

#
#
#######################################################################################################
#                                         Docstrings
#######################################################################################################
#
# def outer_function(a, b):
#     def inner_function(c, d):
#         return c + d
#     return inner_function(a, b)
 
# result = outer_function(5, 10)
# print(result)
#
#
#######################################################################################################
#                                         Final Project
#######################################################################################################
#
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": "add",
    "-": "subtract",
    "*": "multiply",
    "/": "divide",
}

# first_num = int(input("What is the first number?\n"))
# opperation = input("Pick an opperation:\n+\n-\n*\n/\n")
# second_num = int(input("What is the second number?\n"))

#result = operations[opperation](n1 = first_num, n2 = second_num)

print(operations["*"](n1=5, n2=3))
