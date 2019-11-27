#hang man
#logan cannon
#october 9 2019


#hang man except its a horrible version of it by me
#random word
#player guesses
#one letter at time
#fails = hang man gets hanged

#imports
import random

#constants
HANGMAN = ('''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''')

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("OVERUSED","CLAM","GUAM","TAFFETA","PYTHON","CALE","HANGMAN","LEEEEEROOYJENKINS")



# initailizie variables
word = random.choice(WORDS)#the word to be guessed
so_far = "-" * len(word)#dashes for letter
wrong = 0
used =[]

print("Welcome to hangman.  Good luck")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n",used)
    print("\nSo far, the word is:\n", so_far)

    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()
    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("\n\nEnter your guess: ")
        guess = guess.upper()
        
    used.append(guess)
    if guess in word:
        print("\nYes!", guess, "is in the word!")

        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry,", guess, "isn't in the word.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYour bad english has made this man die!\nFor shame!")
else:
    print("\nYou have the good english, man!")
print("\nThe word was", word)
input("\n\nPress the enter key to exit.")





