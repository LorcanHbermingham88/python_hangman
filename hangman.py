import random
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

word = "dog lion pig deer tiger shark dinosaur python titan".split()

def getRandomWord(wordList):
    # function that displays a random string from a string passed in
    wordIndex = random.randint(0, len(wordList)-1)
    return word[wordIndex]
def displayBoard(HANGMAN, missedLetters, correctLetters, secretWord):
    print (HANGMAN[len(missedLetters)])

    print("missed letters : , end = " "")
    for letter in missedLetters:
        print ("letter, end =  " "")
    blanks = "_" * len(secretWord)

    for i in range (len(secretWord)):#replaces blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks: # show the secret word with spaces between each letter
        print(letter, end = " ")
def getGuess(alreadyGuessed):
    #returns the players letters entered, this function makes sure that the player enters a single letter
    while True:
        guess = input("Guess a Letter")
        guess = guess.lower()
        if len(guess) != 1:
            print("Please Enter a single letter")
        elif guess is alreadyGuessed:
            print("You have already guessed that letter, Choose again")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a letter")
        else:
            return guess

def playAgain():
    playAgain = input("Do you want to play again (Yes or No)")
    return playAgain.lower().startwith("y")

print(" H A N G M A N ")
missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(word)
gameisDone = False

while True:
    displayBoard(HANGMAN, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print("You Have WON the game, the secret word is " + secretWord)
            else:
                missedLetters = missedLetters + guess

                if len(missedLetters) == len(HANGMAN)-1:
                    displayBoard(HANGMAN, missedLetters, correctLetters, secretWord)
                    print("You hav run out of guesses!!!" + str(len(missedLetters)) + " missed guesses and " + str(len(correctLetters)) + " correct guesses, and the word is" + secretWord + "\"")
                    gameisDone = True



if gameisDone:
    if playAgain():
        missedLetters = ""
        correctLetter = ""
        gameisDone = False
        secretWord = getRandomWord(words)
    else:
        print("Game Has Ended")
    


    


            

        
        
        

    
    







































    
