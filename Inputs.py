#Logan Cannon
#9/9/2019
#Input Function
print("Input your username")
user_name = input()
print("Welcome",user_name)

print("Input Age Please")
user_age = input("Age here → ")
try:
    print("In",user_age,"years",user_name,"will be",int(user_age)+int(user_age),"years old")
except:
    print('''You fool, you absolute buffoon
You dare challenged me in my own home?
You have another thing coming for you if you
think that was a number, i dont belive that you
are actually''',user_age,'''years old. nor should you.
You fell for one of the classic blunders''')
input("Enter to close")
