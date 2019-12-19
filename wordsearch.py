PUZZLE = "P H C S Y N T A X M L P I Q R L R C F L O W C H A R T W N A R G A O B X W H I L E E M P N U W B N N A Z E Q U G F L T D I Y U G D C J P C P R I N T O N W A O D O A X P Y T H O N M T P S O I T M T I D L E B Q A E A H G C M S L E A N N K A K G R U L O U P G I N Z V U X K E A F E P Y B O R B A U X V A R M F E Y F I E R T E T R N P O E L P F V N L G T U W I T P Z T E X I O A S T R I N G O E O E L F L Q R W U P X Q I W N X R D E E W Y B O O L E A N D"


col0= [PUZZLE[0],PUZZLE[30],PUZZLE[60],PUZZLE[90],PUZZLE[120],PUZZLE[150],PUZZLE[180],PUZZLE[210],PUZZLE[240],PUZZLE[270],PUZZLE[300],PUZZLE[330],PUZZLE[360],PUZZLE[390],PUZZLE[420]]
col1= [PUZZLE[2],PUZZLE[32],PUZZLE[62],PUZZLE[92],PUZZLE[122],PUZZLE[152],PUZZLE[182],PUZZLE[212],PUZZLE[242],PUZZLE[272],PUZZLE[302],PUZZLE[332],PUZZLE[362],PUZZLE[392],PUZZLE[422]]
col2= [PUZZLE[4],PUZZLE[34],PUZZLE[64],PUZZLE[94],PUZZLE[124],PUZZLE[154],PUZZLE[184],PUZZLE[214],PUZZLE[244],PUZZLE[274],PUZZLE[304],PUZZLE[334],PUZZLE[364],PUZZLE[394],PUZZLE[424]]
col3= [PUZZLE[6],PUZZLE[36],PUZZLE[66],PUZZLE[96],PUZZLE[126],PUZZLE[156],PUZZLE[186],PUZZLE[216],PUZZLE[246],PUZZLE[276],PUZZLE[306],PUZZLE[336],PUZZLE[366],PUZZLE[396],PUZZLE[426]]
col4= [PUZZLE[8],PUZZLE[38],PUZZLE[68],PUZZLE[98],PUZZLE[128],PUZZLE[158],PUZZLE[188],PUZZLE[218],PUZZLE[248],PUZZLE[278],PUZZLE[308],PUZZLE[338],PUZZLE[368],PUZZLE[398],PUZZLE[428]]
col5= [PUZZLE[10],PUZZLE[40],PUZZLE[70],PUZZLE[100],PUZZLE[130],PUZZLE[160],PUZZLE[190],PUZZLE[220],PUZZLE[250],PUZZLE[280],PUZZLE[310],PUZZLE[340],PUZZLE[370],PUZZLE[400],PUZZLE[430]]
col6= [PUZZLE[12],PUZZLE[42],PUZZLE[72],PUZZLE[102],PUZZLE[132],PUZZLE[162],PUZZLE[192],PUZZLE[222],PUZZLE[252],PUZZLE[282],PUZZLE[310],PUZZLE[340],PUZZLE[370],PUZZLE[400],PUZZLE[430]]
col7= [PUZZLE[14],PUZZLE[44],PUZZLE[74],PUZZLE[104],PUZZLE[134],PUZZLE[164],PUZZLE[194],PUZZLE[224],PUZZLE[254],PUZZLE[284],PUZZLE[310],PUZZLE[340],PUZZLE[370],PUZZLE[400],PUZZLE[430]]
col8= [PUZZLE[16],PUZZLE[46],PUZZLE[76],PUZZLE[106],PUZZLE[136],PUZZLE[166],PUZZLE[196],PUZZLE[226],PUZZLE[256],PUZZLE[286],PUZZLE[310],PUZZLE[340],PUZZLE[370],PUZZLE[400],PUZZLE[430]]
col9= [PUZZLE[18],PUZZLE[48],PUZZLE[78],PUZZLE[108],PUZZLE[138],PUZZLE[168],PUZZLE[198],PUZZLE[228],PUZZLE[258],PUZZLE[288],PUZZLE[310],PUZZLE[340],PUZZLE[370],PUZZLE[400],PUZZLE[430]]
col10=[PUZZLE[20],PUZZLE[50],PUZZLE[80],PUZZLE[110],PUZZLE[140],PUZZLE[170],PUZZLE[200],PUZZLE[230],PUZZLE[260],PUZZLE[290],PUZZLE[320],PUZZLE[350],PUZZLE[380],PUZZLE[410],PUZZLE[440]]
col11=[PUZZLE[22],PUZZLE[52],PUZZLE[82],PUZZLE[112],PUZZLE[142],PUZZLE[172],PUZZLE[202],PUZZLE[232],PUZZLE[262],PUZZLE[292],PUZZLE[322],PUZZLE[352],PUZZLE[382],PUZZLE[412],PUZZLE[442]]
col12=[PUZZLE[24],PUZZLE[54],PUZZLE[84],PUZZLE[114],PUZZLE[144],PUZZLE[174],PUZZLE[204],PUZZLE[234],PUZZLE[264],PUZZLE[294],PUZZLE[324],PUZZLE[354],PUZZLE[384],PUZZLE[414],PUZZLE[444]]
col13=[PUZZLE[26],PUZZLE[56],PUZZLE[86],PUZZLE[116],PUZZLE[146],PUZZLE[176],PUZZLE[206],PUZZLE[236],PUZZLE[266],PUZZLE[296],PUZZLE[326],PUZZLE[356],PUZZLE[386],PUZZLE[416],PUZZLE[446]]
col14=[PUZZLE[28],PUZZLE[58],PUZZLE[88],PUZZLE[118],PUZZLE[148],PUZZLE[178],PUZZLE[208],PUZZLE[238],PUZZLE[268],PUZZLE[298],PUZZLE[328],PUZZLE[358],PUZZLE[388],PUZZLE[418],PUZZLE[448]]
puzzle2d = [col0,col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14]

PUZZLE = PUZZLE.replace(" ","")
words = ["python",
"import",
"print",
"integer",
"randomlib",
"while",
"syntax",
"append",
"file",
"random",
"binary",
"copy",
"concatenation",
"parameter",
"IDLE",
"google",
"flowchart",
"string",
"boolean",
"shuffle"]
questions = ["What was this file coded in",
"What is the function we use to put a library into our code",
"_____ is a function that outputs text into the console",
"Data type that can hold numbers without decimals",
"library that can take a list and shuffle it",
"loop that continues until false",
"error caused by a character in the wrong place",
"_____ adds an item to the end of a list",
"Everything is saved to a _____",
"made, done, happening, or chosen without method or conscious decision",
"Base language of the computer",
"comes before paste",
"stringing together multiple variables",
"a numerical or other measurable factor",
"Pythons prebuilt IDE",
"Most widespread search engine",
"used to graph out pseudocode",
"data type containing any ascii character",
"data type that can only contain two values",
"function from random that allows the re-arranging of the list"]
positions = [['46','57','68','79','810','911'],['94','104','114','124','134'],["04","05","06","07","08","09","010"],
             ['11','22','33','44','55','66','77','88','99'],['62','72','82','92','102'],['30','40','50','60','70','80'],
             ['149','1410','1411','1412','1413','1414'],['511','512','513','514'],['140','141','142','143','144','145'],
             ['69','610','611','612','613','614'],['47','48','49','410'],['21','32','43','54','65','76','87','98','109','1110','1211','1312','1413'],
             ['16','17','18','19','110','111','112','113','114'],['86','97','108','119'],['34','35','36','37','38','39'],
             ['31','41','51','61','71','81','91','101','111'],['712','812','912','1012','1112','1212'],['714','814','914','1014','1114','1214','1314'],
             ['26','27','28','29','210','211','212']]
#LOGAN CANNON
def display_puzzle(puzzle,x,y):
    """Displays a word puzzle from a string, a min and max"""
    y1 = y
    print("     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14")
    print("   |-----------------------------------------------------------|")
    for i in range(15):
        if x//15 < 10:
            print(" ",end="")
        print(x//15,"|",end="")
        for i in range(x,y):
            print("",puzzle[i],"|",end="")
        x+=y1
        y+=y1
        print("\n   |-----------------------------------------------------------|")
        

def instructions():
    """Displays the instructions for word search"""
    intructions = """
    Welcome to the word search!
    in order to play, you must
    know the instructions.
    in order to play, you will
    recieve a word you must guess.
    on the sheet are number for the
    positions of the letters.
    Enter your answer by giving
    the position numbers in
    xy, where x is the top and
    y is the left. For example:
    if the positions are 14x and
    14y your answer would be 1414
    but if your answer was 0x and 14y
    your answer would be 014. Each
    word will have multiple positions
    that you will have to enter one by one
    into the input, entering RESET to
    reset your answers

    Have a good day!"""
    print(intructions)

import random

def picked_question(words, questions, pos):
    picked = random.randint(0,len(words)-1)
    asked_words = words.pop(picked)
    asked_question = questions.pop(picked)
    asked_pos = pos.pop(picked)
    return asked_question, asked_words, asked_pos
def main():
    totguess = []
    instructions()
    input("enter to continue")
    display_puzzle(PUZZLE,0,15)
    while words:
        question, word, pos = picked_question(words, questions, positions)
        print(question)
        print(word)
        print(pos)
        while totguess != pos:
            posguess = input("Please input your position")
            print(posguess)
            totguess.append(posguess)
            
            if posguess == "RESET":
                totguess = []
            print(totguess)
        posguess = ""
        totguess = []
main()
        


