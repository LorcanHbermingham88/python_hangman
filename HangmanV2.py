import random
HANGMANV2 = (
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
max_wrong = len(HANGMANV2) -1
#tuple
words = ("animal", "chicken", "python", "panter", "beasttitan")
#randomly takes a word
word = random.choice(words)

so_far = "-" * len(word)

wrong = 0

used = []

print ("H A N G M A N")

while wrong < max_wrong and so_far != word:
    print (HANGMANV2[wrong])
    print("\nYou have used the following letters", used)
    print("\nSo far the word is : \n", so_far)
    guess = input("Enter your guess : ")
    #guess = guess.upper() #not sure

    while guess in used: # checks if a letter has already been entered and is appened to used
        print("You have already guessed that letter ", guess)
        guess = input("Enter a guess : ")
        guess = guess.lower()
    used.append(guess)

    if guess in word:
        print("\nYes ", guess, "is in the word!")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\n Sorry, ", guess, "isnt in the word")
        wrong += 1
if wrong == max_wrong:
    print(HANGMANV2[wrong])
    print("\n You have been H A N G E D")
else:
    print("\n C O R R E C T you got it")
print("\n The word was, ", word)

input("\n\n press the enter button to exit... ")


    
            
        

    
    
    
























