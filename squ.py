#Cale (Leafy Vegetable), Daniel, Austin (meme king/ Cowboy), Logan
#9/11/2019
#Doing geometries with python

#errors found by Kephryn
#syntax error
#logical error in spelling
#logical error in circle circumferance
#logical error if input is letter instead of number
#logical error if putting in floats
#logical spelling error again
#logical error, answer is out of order on triangle area
#logical error in shape of triangle
#logical error in austins error message, it's incomplete

print('')
#inputs



##Square
try:
    squ_side = float(input("Square Side Length → "))
except:
    squ_side = 1
    print("There was an error with the square side length, please make sure that you inputed ONLY numbers")
squ_area = float(squ_side) ** 2
squ_peri = float(squ_side) * 4
squr_pic = str.format(''' 
         _____     side = {2: 1.2f}
	|     |    p = {0: 1.2f}
	|     |    a = {1: 1.2f}
	|_____|''',squ_peri,squ_area,squ_side)
  
print(squr_pic)

#Triangle
try:
    tri_base = float(input("Triangle Base Length → "))
except:
  tri_base = 1
  print("There was an error with the Triangle Base Length, please make sure that you inputed ONLY numbers")
try:
    tri_height = float(input("Triangle Height Lenght → "))
except:
  tri_height = 1
  print("There was an error with the Triangle Heigth, please make sure that you inputed ONLY numbers")
area = float(tri_base) * float(tri_height) / 2
tri_pic = str.format('''
       /\       
      / |\      
     /  | \    
    /   |  \    Height = {0: 1.2f}
   /    |   \   Base = {1: 1.2f}
  /     |    \  
 /      |     \ 
/______________\
area = {2: 1.2f}
''',tri_height,tri_base,area)
print(tri_pic)



#Circle
try:
	circ_radius = float(input("Circle Radius → "))
except:
  circ_radius = 1
  print("Austins Error Text here")
print("Area of the Triagle is: " , area)
r= float(circ_radius)

pi=3.14

c=2*pi*r
circ_pic =str.format('''
                   ooo OOO OOO ooo
               oOO                 OOo
           oOO                         OOo
        oOO                               OOo
      oOO                                   OOo
    oOO                                       OOo
   oOO                                         OOo
  oOO                                           OOo
 oOO                                             OOo  Radius = {0: 1.2f}
 oOO                                             OOo  
 oOO                                             OOo
 oOO                                             OOo
 oOO                                             OOo  Circumfrance = {1: 1.2f}
  oOO                                            OOo
   oOO                                         OOo
    oOO                                       OOo
      oOO                                   OOo
        oO                                OOo
           oOO                         OOo
               oOO                 OOo
                   ooo OOO OOO ooo
                   ''',r,c)
#Cube
try:
	cube_side = float(input("Cube Side Length → "))
except:
  cube_side = 1
  print("err 404: Cube side is a string")
volume = float(cube_side) ** 3
pic_cube = str.format(''' 
 .___________,
 |`          :\\
 | `         : \\
 |  `        :  \\
 |   +-----------+
 |__ : ______:   :
 `   :        \\  :
  `  :         \\ : Side = {0: 1.2f}
   ` :          \\:
    `:___________>
    volume = {1: 1.2f}
''',cube_side,volume)
print(pic_cube)

input("Enter to Close")
