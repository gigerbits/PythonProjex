#10/30/2019
import random
rang = [1,100]
guesses = 15
difficulty = "BOT"

def NumberGameRobo():
    import random
    tries = 0
    roboguess = 0.5
    global rang
    global guesses
    global difficulty
    while True:
        numb = input("Input a number for the robot to guess: ")
        if numb.isdigit():
            numb = int(numb)
            if numb in range(rang[0],rang[1]+1):
                break
            else:
                print("Number not in range")
        else:
            print("Invalid Input")
    print("\n\nDifficulty:",difficulty,"\nTotal Allowed Guesses:",guesses,"\nRange of numbers:",rang,"Your number:",numb,"\n\n")
    guess = rang[1]//(1/roboguess)
    
    tries += 1
    while tries != guesses and guess != numb:
        if guess > numb:
            print(guess)
            print("Guess Lower")
            roboguess = roboguess * 0.5
        else:
            print(guess)
            print("Guess Higher")
            roboguess = roboguess * 1.5
        guess = rang[1]//(1/roboguess)
        tries +=1
    if guess == numb:
        print("The robot wins!")
        print("The robot guessed it in",tries,"attempts")
    else:
        print("The robot loses :(")
        print("The robot guessed it in",tries,"attempts")



