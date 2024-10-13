#! /usr/bin/env python3


#######################################################################################################
#                                   This shows basic dictionaries
#######################################################################################################
## dictionaries have keys and then values
##"Cap Off" dictionaries to make it easier to add items down the road (end with a comma)
#
##dictionary = {key: value}
##
##dictionary_multiple_keys = {key1: value1, key2: value2, key3: value3}
#
##Can create multiple lines for readability
#programming_dictionary = {
#    "Bug": "An error in a program that prevents the proram from running as expected",
#    "Function": "A piece of code that you can easily call over and over again",
#}
#
#
##Retieve an item from the Dictionary
#print(programming_dictionary["Bug"])
##Output:
##An error in a program that prevents the proram from running as expected
#
#
##Adding to a dictionary
#programming_dictionary["Loop"] = "The action of doing someting over and over again"
#print(programming_dictionary["Bug"])
#
#
##Creating an empty dictionary or wiping a dictionary
#empty_dictionary = {}
#
#
##Edit an item in a dictionary or add an item if the key does not exist
#programming_dictionary["Bug"] = "New definition that I want to assign to Bug"
#
#
##Loop through a dictionary
##The first print only prints the Key, you need to pass it through [ ] to print the key's values
#for key in programming_dictionary:
#    print(key)
#    print(programming_dictionary[key])
#
#
#
#######################################################################################################
#                                       Grading Program
#######################################################################################################
#
#student_scores = {
#    'Harry': 88,
#    'Ron': 78,
#    'Hermonie': 95,
#    'Draco': 75,
#    'Neville': 60
#}
#
#student_grades = {}
#
#for key in student_scores:
#    score = student_scores[key]
#    if score > 90:
#        student_grades[key] = "Outstanding"
#    if score > 80:
#        student_grades[key] = "Exceeds Expectations"
#    if score > 70:
#        student_grades[key] = "Acceptable"
#    if score < 70:
#        student_grades[key] = "Fail"
#
#print(student_scores)
#print(student_grades)

#
#
#######################################################################################################
#                                          Nesting
#######################################################################################################
#
#nested_dictionary = {
#    "key1": [list],
#    "key2": {dict},
#}
#
#capitals = {
#    "France": "Paris",
#    "Germany": "Berlin",
#}
#
##Nested List in Dictionary
########################################################################################################
#travel_log = {
#    "France": ["Paris", "Lille", "Dijon"],
#    "Germany": ["Berlin", "Stuttgart"],
#}
#
##Print/Access Lille
########################################################################################################
#print(travel_log["France"][1])
#
##Print/Access "D"
########################################################################################################
#nested_list = ["A", "B", ["C", "D"]]
#print(nested_list[2][1])
#
##Nested dictionary and lists
########################################################################################################
#travel_log2 = {
#    "France": {
#        "cities_visited": ["Paris", "Lille", "Dijon"],
#        "total_visits": 12
#    },
#    "Germany": {
#        "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
#        "total_visits": 5
#    }
#}
#
##Print/Access Stuttgart
########################################################################################################
#print(travel_log2["Germany"]["cities_visited"][2])

#
#
#######################################################################################################
#                                         Final Project
#######################################################################################################
#
from os import system

#Each person's name will be the key and their bid will be the value

participants = {}
should_continue = True

while should_continue == True:
    name = input("What is your name?:\n")
    bid = int(input("What is your bid?:\n"))
    participants[name] = bid
    continue_prompt = input("Are there any other bidders? Type 'yes or no:\n").lower
    if continue_prompt == "yes":
        system("clear")
    else:
        should_continue = False

highest_bidder = max(zip(participants.values(), participants.keys()))[1]
highest_bid = participants[highest_bidder]
print(f"The highest bidder is: {highest_bidder} with a bid of: {highest_bid}")

#
#
#######################################################################################################
#                                         Final Solution
#######################################################################################################
#
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
