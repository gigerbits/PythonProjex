#Logan cannon 9/25/2019 Name Function
import random
#Get Name code
def get_name():
    while True:
        name = input("Whats is your name → ")
        if " " in name:
            name = name.replace(" ", "QZRX") 
        if name.isalpha():
            name = name.replace("QZRX", " ")
            name = name.title()
            return name
        else:
            print("Invalid Syntax")

#Mathing code
def math_fun():
 while True:
    x = input("enter a number less than 100 → ")
    y = input("enter a number less than 1000 → ")
    if x.isdigit() and y.isdigit() and len(x) <2 and len(y) <2:
        x=int(x)
        y=int(y)
        total =x*y
        return total
    else:
        return "You suck at math"


#Coin Flip code
def coin_flip(x):
    if x.isdigit():
        x=int(x)
        if x>0:
            for i in range(x):
                side = random.randint(0,1)
                if side == 1:
                    print("heads")
                    
                else:
                    print("tails")
        else:
            print("Not a positive range")
    else:
        print("Not a correct range")
#The option menu
def intro(name):
    print("""
    Welcome to """+name+"""
    please choose an option
    from the list below

    1: option 1
    2: option 2
    3: option 3
    4: quit
""")
#Option 1
def option1():
    print("option 1")
#Option 2
def option2():
    print("option 2")
#Option 3
def option3():
    print("option 3")
#Option 4
def option4():
    verify = input("Are you sure you want to quit")
    verify = verify.lower()
    if "y" in verify:
        return True
    else:
        return False
#Combining the option menu and all the other functions inbetween
def menu():
    while True:
        intro("Examplien")
        choice = input("pick an option 1, 2, 3, or 4")
        if choice == "1":
                option1()
        elif choice == "2":
                option2()
        elif choice == "3":
                option3()
        elif choice == "4":
                verify = option4()
                if verify:
                    break
                else:
                    continue
        else:
                print("Invalid Choice")
menu()
input("Enter to texit")
            
