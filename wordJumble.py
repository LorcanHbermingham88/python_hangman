import random

words = ("phython","titan","fatcat","death","war","night")

word = random.choice(words)

correct = word

jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

#start Game
print(
    """                      Welcome to word J U M B L E
                             ---------------------------

                         Unjumble the letters to make a word

    """
    )
print("The word is : ", jumble)

guess = input("\n Your Guess : ")
while guess != correct and guess != "":
    print("Sorry thats not it")
    guess = input("your guess : ")
if guess == correct:
    print("Thats it!! You guessed it \n\n")

input("Press the enter button to quit")

    
