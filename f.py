#Cale (Leafy Vegetable), Daniel, Austin (meme king/ Cowboy), Logan
#9/11/2019
#Doing geometries with python


print('')
#inputs



##Square
#To make sure that you cant just input a string and break the program, we put in the try command
try:
    squ_side = int(input("Square Side Length → "))
except:
    squ_side = 1
    print("There was an error with the square side length, please make sure that you inputed ONLY numbers")
#testing for negative numbers
if squ_side < 0:
  print("There was an incorrect sidelength")
  squ_side = 1 
#Calculations
squ_area = float(squ_side) ** 2
squ_peri = float(squ_side) * 4
if squ_side <= 0:
  print("There was an incorrect sidelength")
  squ_side = 1
#Picture formatting
squr_pic = str.format(''' 
   _____     side = {2: 1.2f}
	|     |    p = {0: 1.2f}
	|     |    a = {1: 1.2f}
	|_____|''',squ_peri,squ_area,squ_side)
  
print(squr_pic)
