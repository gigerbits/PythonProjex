#Logan Cannon
#9/5/2019
#Stopwatch
floats = 55.001
minu = 59
sec = 0
hour = 00
while True:
    floats+=0.0025
    sec = floats // 1 
    if sec == 60.0:
        minu+=1
        floats-=60
    if minu==60:
        hour+=1
        minu-=60
    print(str(hour)+":"+str(minu)+":"+str(sec))
