# Name: Darlene Bruce
# Program Purpose: Pordle (PVCC Wordle): Word Guessing Game
#     The user has a choice of four categories including animals, 
#     flowers, fruits, and birds. The program chooses a random word
#     from a file of words. The user tries to figure out the word in 
#     the fewest guesses by guessing letters in the word. This 
#     program uses an input FILE, LISTS, and STRING SLICES (section of the string).

import random

def main():
    playAgain = True  #set value to True to start and until user enters "n" or "N"
    while playAgain:  #continue to play as long as user enters something other than "n" or "N"

        printHeadings()  #print to screen the intro for the game

        inFile = printMenu()  #get the file or category choice from the user

        playGame(inFile)  #send the file or category choice to function to play the game

        yesno = input("Would you like to play again? (Y/N) ")
        if yesno == "n" or yesno == "N":
            playAgain = False
            print("Thank you for playing PORDLE!")

def printHeadings():
    print("\nWelcome to PORDLE! The PVCC Wordle Game")
    print("I will think of a word and you try to guess the letters in the word.")
    print("The number of dashes indicates the number of letters in the word.")

def printMenu():
    print("\nChoose a PORDLE category: ")
    print("\t1. Animals")
    print("\t2. Flowers")
    print("\t3. Fruits")
    print("\t4. Birds")
    category = input("Please enter the category number: ")

    #ask user for category choice and return the correct file name for word list
    #if integer other than 1, 2, 3, or 4 is entered then default to Animals category
    if category == "1":
        inFile = "animals.txt"
        print("You chose Animals.")
    elif category == "2":
        inFile = "flowers.txt"
        print("You chose Flowers.")
    elif category == "3":
        inFile = "fruits.txt"
        print("You chose Fruits.")
    elif category == "4":
        inFile = "birds.txt"
        print("You chose Birds.")    
    else:
        inFile = "animals.txt"
        print("Incorrect input. Animals category chosen for you.")
    return inFile


def playGame(inFile):
    numguesses = 1
    lettersUsed = []   #create an empty list for letters guessed
    wordList = []      #create an empty words list used in game
    wordList.clear()   #set the list to empty from any previous rounds

    wordFile = open(inFile, "r")     #open the file for READ
    for textLine in wordFile:         #read in a line of text from the file
        for word in textLine.split(): #split the line of text into words
            wordList.append(word)     #add each word to the word list
    wordFile.close()

    wordChosen = random.choice(wordList)  #choose a random word from the list
    pordle = wordChosen                   #set chosen word to another variable to manipulate
    for i in range (len(pordle)):
        pordle = pordle[0:i] + "_" + pordle[i+1:] #use SLICE to replace each letter with a "_"
    print (" ".join(pordle)) #the JOIN will put a space between each underscore

    while pordle != wordChosen: #keep asking the player until player guesses the word
        letterGuess = input("Please enter a letter: ")
        letterGuess = letterGuess.lower()
        lettersUsed.append(letterGuess) #add the players letter to the list of guessed letters
        print ("Number of guesses: " + str(numguesses))

        for i in range(len(wordChosen)): #search through the letters to find a match
            if wordChosen[i] == letterGuess:
                pordle = pordle[0:i] + letterGuess + pordle[i+1:]

        print("Used letters: ")
        print(lettersUsed)
        print(" ".join(pordle)) #Print the string with guessed letters with spaces in between
        numguesses = numguesses + 1

    print("Well done! You guessed in " + str(numguesses - 1) + " guesses!")

main()

