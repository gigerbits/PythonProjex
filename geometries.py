#Cale (Leafy Vegetable), Daniel, Austin (Meme Lord), Logan (dead Nerd)
#9/11/2019
#Doing geometries with python


print('')
#inputs



##Square
squ_side = input("Square Side Length → ")
squ_area = float(squ_side) ** 2
squ_peri = float(squ_side) * 4
print("Area of the square is",squ_area,sep=": ")
print("Perimiter of the square is",squ_peri,sep=": ")

squr_pic = str.format(''' _____
|  _   |    p = {}
| |{}| |
|__{}__|''',squ_peri,squ_area,squ_side)


print(squr_pic)

#Triangle
tri_base = input("Triangle Base Length → ")
tri_height = input("Triangle Height Lenght → ") 
area = float(tri_base) * float(tri_height) / 2
tri_pic = str.format('''
       /\       
      /| \      
     / |  \     
    /  |   \    
   /   |{}  \   
  /    |     \  
 /     |      \ 
/______{}_______\
               a = {}
''',tri_height,tri_base,area)
print(tri_pic)

#Circle
circ_radius = input("Circle Radius → ")
print("Area of the Triagle is: " , area)
r= float(circ_radius)

pi=3.14


c=2*pi*r
#Cube
cub_side = input("Cube Side Length → ")
Volume = float(cub_side) ** 3
pic_cube = str.format(''' 
 ._____A_____,
 |`          :\
 | `         : B
 |  `        :  \
 C   +-----A-----+
 |   :       :   :
 |__ : _A____:   :
 `   :        \  :
  `  :         B :
   ` :          \:
    `:_____A_____>
''')
#Print
print("~=~=~=~=~=~=~=~=~=~")


print("Volume of the Cube is",Volume,sep=": ")
print("Circumference is:  "  , c)

#names
#Leafy Vegetable
#Cowboy
#Daniel
#Gay Vegetable
