#!/usr/bin/env python3


#######################################################################################################
#                                   This shows basic functions
#######################################################################################################

def greet():
   print("Hello")
   print("Welcome to")
   print("My Function!")

greet()


#######################################################################################################
#                                   This tests basic fuctions allowing inputs
#######################################################################################################
#Paramater is "name"
#Argument is "Eric"
#######################################################################################################

def greet_with_name(name):
   print(f"Hello {name}")
   print("Welcome to")
   print("My Function!")

greet_with_name("Eric")

#######################################################################################################
#                                   Weeks Left exsersise with 1 input
#######################################################################################################


def life_in_weeks(age):
   Lived_weeks = age * 52
   weeks_left = 4696 - Lived_weeks
   print(f"You have {weeks_left} weeks left.")

life_in_weeks(30)

#######################################################################################################
#                           This tests basic functions with multiple inputs
#######################################################################################################
#Positional arguments are "Eric" and "Colorado" 

def greet_with(name, location):
   print(f"Hello, {name}")
   print(f"What is it like in {location}?")

greet_with("Eric", "Colorado")


#######################################################################################################
#                           This tests functions with keyword arguments
#######################################################################################################

def greet_with(name, location):
   print(f"Hello, {name}")
   print(f"What is it like in {location}?")

greet_with(location="Colorado", name="Eric")


#######################################################################################################
#                                      Love Calculator Exsersise
#######################################################################################################

def calculate_love_score(name1, name2):
   total_score = 0
   for letter in name1.lower() + name2.lower():
       for i in "truelove":
           if letter == i:
               total_score += 1

   print(total_score)

calculate_love_score(name1="eirc pribik", name2="rudy dog")


#######################################################################################################
#                                      Final Exsersise
#######################################################################################################

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
   encrypted_message = ""
   for letter in original_text:
       if letter == " ":
           encrypted_message += " "
       else:
           index = alphabet.index(letter)
           if index + shift_amount > 25:
               overflow_index = index - 26
               encrypted_message += alphabet[overflow_index + shift_amount] 
           else:
               encrypted_message += alphabet[index + shift_amount]

   print(encrypted_message)

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.


# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

encrypt(text, shift)



def caesar(original_text, shift_amount):
   output = ""
   for letter in original_text:
       if direction == "encode":
           shifted_position = alphabet.index(letter) + shift_amount
       elif direction == "decode":
           shifted_position = alphabet.index(letter) - shift_amount
       shifted_position %= len(alphabet)
       output += alphabet[shifted_position]
   print(f"Here is your encoded result: {output}")

caesar(original_text=text, shift_amount=shift)


#######################################################################################################
#                                      Final Exsersise
#######################################################################################################
#
#
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def decrpyt(original_text, shift_amount):
    decrpyted_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        decrpyted_text += alphabet[shifted_position]
    print(f"Here is the decrypted result: {decrpyted_text}")



def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1
        elif letter in alphabet: 
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

restart = input("Do you want to restart the program? yes/no\n").lower()
if restart == "no":
    should_continue = False
    print("Goodbye.")

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)