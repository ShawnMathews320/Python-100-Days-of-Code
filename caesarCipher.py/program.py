from art import logo
from alphabet import letters

def getShiftedChar():  # returns new shifted string from alphabet list
    shiftedResult = ""  # holds the result of cipher

    for i in range(len(userMessage)):
        if userMessage[i] in letters:  # go through each char in string
            if encrytionType == "encode":
                shiftChar = letters[letters.index(userMessage[i]) + shiftNumber]  # get the shifted letter from alphabet list
            elif encrytionType == "decode":
                shiftChar = letters[letters.index(userMessage[i]) - shiftNumber]  # get the shifted letter from alphabet list
            shiftedResult += shiftChar  # append to our result string

    return shiftedResult

print(logo)  # ASCII art 
isDecodingEncoding = True  # determines if the loop will keep running

while isDecodingEncoding:
    encrytionType = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")  # decode or encode option
    userMessage = input("Type your message:\n").lower()  # what the user wants to encode or decode
    shiftNumber = int(input("Type the shift number:\n"))  # how many letters we will shift for cipher

    shiftedResult = getShiftedChar()    
    
    print(f"Here is the {encrytionType + 'd'} result: {shiftedResult}")  # show user result of caesar cipher on their message
    continueLoop = input("Type 'yes' if you want to continue. Otherwise type 'no'.\n")  # ask user if they want to continue

    if continueLoop == "no":  # end the loop because user doesn't want to continue
        isDecodingEncoding = False