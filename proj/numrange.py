#10/28/2019
import roboguess as robot
rang = [1,1]
guesses = 1
difficulty = "Unselected"
def Menu():
    menu = """
        MENU
    1: Difficulty Settings
    2: Play game
    3: Quit
    4: Computer Plays\n\n"""
    print(menu)
    while True:
        option = input("Choice: ")
        if option.isdigit():
            option = int(option)
            if option >= 1:
                if option == 1:
                    Difficulty()
                    break
                elif option == 2:
                    NumberGame()
                    break
                elif option == 3:
                    break
                elif option == 4:
                    robot.NumberGameRobo()
                    break
        else:
             print("Incorrect Choice")
                




def Difficulty():
    global rang
    global guesses
    global difficulty
    print("""Choose Your Difficulty:\n\n
1: Easy
2: Medium
3: Hard
4: Custom\n\n""")
    while True:
        x = input("Your Choice : ")
        if x.isdigit():
            x = int(x)
            if x == 1:
                difficulty = "Easy"
                rang[0] = 1
                rang[1] = 10
                guesses = 5
                Menu()
                break
            elif x == 2:
                difficulty = "Medium"
                rang[0] = 1
                rang[1] = 20
                guesses = 8
                Menu()
                break
            elif x == 3:
                difficulty = "Hard"
                rang[0] = 1
                rang[1] = 30
                guesses = 12
                Menu()
                break
            elif x == 4:
                while True:
                    j = input("Input Max Tries: ")
                    if j.isdigit():
                        j = int(j)
                        if j > 0:
                            guesses = j
                            break
                        else:
                            print("Max tries cant be 0")
                    else:
                        print("Max tries cant be a string")
                while True:
                    k = input("Input Minimum Range: ")
                    if k.isdigit():
                        k = int(k)
                        rang[0] = k
                        break
                    else:
                        print("Invalid Value")
                while True:
                    l = input("Input Maximum Range: ")
                    if l.isdigit():
                        l = int(l)
                        if l >= k:
                            rang[1] = l
                            break
                        else:
                            print("Maximum cant be lower than minimum!")
                    else:
                        print("Invalid Value")
                        
                difficulty = "Custom"
                Menu()
                break
        else:
            print("Error: not in range")


def NumberGame():
    import random
    tries = 0
    global rang
    global guesses
    global difficulty
    numb = random.randint(rang[0],rang[1])
    print("\n\nDifficulty:",difficulty,"\nTotal Allowed Guesses:",guesses,"\nRange of numbers",rang,"\n\n")
    guess = GetNumberInRange(rang)
    tries += 1
    while tries != guesses and guess != numb:
        if guess > numb:
            print("Guess Lower")
        else:
            print("Guess Higher")
        guess = GetNumberInRange(rang)
        tries +=1
    if guess == numb:
        print("You Win!")
        Menu()
    else:
        print("You Lose :(")
        Menu()
def GetNumberInRange(x):
    while True:
        inp = input("Input your guess")
        if inp.isdigit():
            inp = int(inp)
            if inp in range(x[0], x[1]+1):
                return inp
        print("not a good value")

Menu()
