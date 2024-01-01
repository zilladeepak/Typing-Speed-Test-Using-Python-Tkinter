import random
from tkinter import *
import tkinter.font as tkFont
import time

global start_time
start_time = None

root = Tk()
root.title("Typing Speed Test")
root.geometry("1750x1500")

root.configure(bg='#000000')
root.iconbitmap("icon.ico")

title = Label(root, text="TYPING SPEED TEST", anchor=CENTER, font="Arial 50 bold", bg="#000000", fg='#FFD566')
title.place(x=410, y=50)


fontStyle = tkFont.Font(family="Lucida Grande", size=25)
text = Label(root, height='6', width='40', fg='white', bg='#000000', font=fontStyle, wraplength=600, 
             anchor=CENTER, justify=CENTER)
text.place(x='360', y='150')


#inputtext
large_font = ('Times New Roman',30)
e = Entry(root, width='35', bg="#F2BC94", fg="black",font=large_font)
e.place(x=400, y=400)
e.focus()

def start_typing_timer(event):
    global start_time
    if start_time is None:
        start_time = time.time()

e.bind('<Key>', start_typing_timer)

def reset_timer():
    global start_time
    start_time = None

def randomTXT():
    reset_timer() 
    f = open('Sentence.txt').read()
    sentences = f.split('\n')
    display = random.choice(sentences)
    text.config(text=display)
    e.delete(0, 'end')
    total_words.config(text="Total Words: 0")
    time_taken.config(text="Time Taken: 0 seconds")
    speed.config(text="Speed:")
    start_time = time.time()

def calculate(*args,**kwargs):
    global start_time
    end_time=time.time()
    input_text = e.get()
    w_count = len(input_text.split())
    elapsed_time = end_time - start_time if start_time is not None else 0


    words_per_minute = int(w_count / (elapsed_time / 60)) if elapsed_time > 0 else 0

    total_words.config(text="Total Words: " + str(w_count))
    time_taken.config(text="Time Taken: " + str(round(elapsed_time, 2)) + " seconds")
    
    if elapsed_time >= 60:
        speed.config(text="Speed: POOR \U0001F44D")
    elif elapsed_time >= 30 and elapsed_time <= 60:
        speed.config(text="Speed: AVERAGE \U0001F44F")
    else:
        speed.config(text="Speed: EXCELLENT \U0001F44C")


total_words = Label(root, text="Total Words: 0", bg='#000000',fg='#FFD566',font='Arial,14')
total_words.place(x=390, y=590)
    
time_taken = Label(root, text="Time Taken: 0 seconds", bg='#000000',fg='red',font='Arial,14')
time_taken.place(x=690, y=590)

speed = Label(root, text="Speed:", width='25',bg='#000000', fg='#28D8FF',font='Arial,14')
speed.place(x=945, y=590)


def clearfunc():
    reset_timer() 
    e.delete(0, 'end')
    total_words.config(text="Total Words: 0")
    time_taken.config(text="Time Taken: 0 seconds")
    speed.config(text="Speed:")
    
    
switch = Button(root, text="SWITCH-UP", bg='red', fg='black', font="helvetica 20", padx=10, pady=10, relief=RAISED,
                command=randomTXT)
switch.place(x=660, y=650)

result_btn = Button(root, text="RESULT",bg='#FFD566', fg='black',font="helvetica 20", padx=10, pady=10, relief=RAISED,
                    command=calculate)
result_btn.place(x=970,y=650)

reset = Button(root, text="RESET", bg="#28D8FF", fg="black", font="helvetica 20", padx=20, pady=10, relief=RAISED,
               command=clearfunc)
reset.place(x=390, y=650)
      
root.mainloop()
