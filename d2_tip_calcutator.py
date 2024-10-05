#!/usr/bin/env python3
#print("hello"[-2])

#len("12345")

#print(type(5))
#print(type(5.0))
#print(type("hello"))
#print(type(True))

#print("Number of leters in your name: \n" + str(len(input("Enter your name\n"))))

#test = input("Enter a name")
#print(type(test))


#print(7 // 4)

#height = 1.65 
#weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
#bmi = weight / height ** 2

#print(round(bmi, 2))


bill = float(input("Welcome to the tip calculator!\nwhat was the total bill? \n$"))
tip = int(input("what percent tip would you like to give? \n%"))
people = int(input("How many people to split the bill? \n"))
total = round(bill * (1 + tip / 100) / people, 2)
print(f"Each person will pay: ${total}")

#print("Each person will pay: $" (round(total, 2)))


#total = float(input("Welcome to the tip calculator!\nwhat was the total bill? \n$"))
#tip = int(input("what percent tip would you like to give? \n%"))
#people = int(input("How many people to split the bill? \n"))
#print(f"Each person will pay: $" + str(round((total) * (1 + tip / 100) / people ), 2))
