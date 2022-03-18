from lib2to3.pygram import Symbols
import random

randomPassword = ""  # password that will be randomly generated

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
'W', 'X', 'Y', 'Z']  # letters to choose from 

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9 ']  # numbers to choose from 

# special characters to choose from
specialChars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '[', ']', '{', '}', '<', '>']  

letterCount = int(input("Welcome to the PyPassword Generator!\nHow many letters would you like in your password?\n"))
symbolCount = int(input("How many symbols would you like?\n"))
numberCount = int(input("How many numbers would you like?\n"))
 
for i in range(letterCount):  # iterate through number of letters user specified
    randomListIndex = random.randint(0, len(letters) - 1)  # generate a random number for index of list
    randomPassword += letters[randomListIndex]  # append to password

for i in range(symbolCount):  # iterate through number of specialChars user specified
    randomListIndex = random.randint(0, len(specialChars) - 1)  # generate a random number for index of list
    randomPassword += specialChars[randomListIndex]  # append to password

for i in range(numberCount):  # iterate through number of numbers user specified
    randomListIndex = random.randint(0, len(numbers) - 1)  # generate a random number for index of list
    randomPassword += numbers[randomListIndex]  # append to password

print("Here is your password:", randomPassword)