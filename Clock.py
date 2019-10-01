import time
import calendar
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound
#9/27/2019

h = 0
m = 0
s = 0
t = "am"

def current_time():
    global h
    global m
    global s
    global t
    total_seconds = calendar.timegm(time.gmtime())
    current_second = total_seconds%60

    totalMinutes = total_seconds//60
    current_minute = totalMinutes%60

    total_hours = totalMinutes//60
    current_hour = total_hours%24-6

    am_pm = " "
    if current_hour>=12:
        current_hour=current_hour-12
        am_pm="PM"
        if current_hour==0:
            current_hour=current_hour+12
    else:
        am_pm="AM"
        if current_hour==0:
            current_hour=current_hour+12
    alarm= str(h)+":"+str(m)+":"+str(s)+t
    timex = str(current_hour)+":"+str(current_minute)+":"+str(current_second)+am_pm
    return timex

    if timex == alarm:
        beep()
def beep():
    for i in range(10):
        winsound.Beep(640,5000)
def show_time():
    global h
    global m
    global s
    global t
    time= current_time()
    txt.set(time)
    root.after(1000,show_time)

def get_alarm(*args):
    global h
    h=input("what hour")
    global m
    m=input("what minute")
    global s
    s=input("what second")
    global t
    t=input("am or pm").upper()
def quit(*args):
    root.destroy()
#creat root window
root= Tk()
root.geometry("500x200")
root.attributes("-fullscreen",False)
root.title("Clock: Clock 2 Electric boogaloo")

#set window background color
root.configure(background='black')
root.bind("x",quit)
root.bind("a", get_alarm)
root.after(1000,show_time)
fnt=font.Font(family='Consolas', size=60, weight='bold')
txt=StringVar()
    
#display time and set up the colors of text and background
lbl = ttk.Label(root, textvariable = txt, font=fnt, foreground="Green",background="yellow")
#place the time in the center of shrteen
lbl.place(relx=0.5, rely=0.5, anchor = CENTER)
#loop
root.mainloop()

