import random
import os

from wordList import wordList
from hangmanArt import logo, stages

display = []  # holds underscores
livesLeft = 6  # player lives

randomIndex = random.randrange(len(wordList))  # generate random number
chosenWord = wordList[randomIndex]  # choose a random word from the list
endOfGame = False  # when the game will end

print(logo)
for i in chosenWord:  #displays as many underscores as there are chars in the string
    display.append('_')

print(chosenWord)
print(display)

while not endOfGame:  # keep going until the game ends
    guess = input("Guess a letter in the word: ").lower()  # get user's guess of what a char in the word could be

    os.system('cls')
    if guess in display:
      print(f"You have already correctly guessed {guess}.")
    for i in range(len(chosenWord)):  # go through each char in word
        if guess == chosenWord[i]:  # if the guess is correct
            display[i] = chosenWord[i]  # change underscore to letter

    if guess not in chosenWord:
      livesLeft -= 1
      print(f"You guessed {guess}, which is not in the word. You lose a life.")
    
    print(display)
    print(stages[livesLeft])
    print(livesLeft)

    if '_' not in display:  # means user correctly guessed all chars so end game
        endOfGame = True
        print("You Won!")
    elif livesLeft <= 0:  # user out of lives so end game
        endOfGame = True
        print("You lost!")