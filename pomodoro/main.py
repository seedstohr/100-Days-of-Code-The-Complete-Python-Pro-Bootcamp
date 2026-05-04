#create pomodoro app with tkinter
#the app will be a 25-min timer that when you hit start starts a timer and goes to the background when time is up it poop to the front of the screen
import tkinter as tk
from tkinter import PhotoImage

#colors
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#f9f9f9"
FONT_NAME = "Monospace"

#time values
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#global variable
reps = 0
timer = None

def reset_timer():
    '''create a function to reset the timer'''
    #stop timer
    window.after_cancel(timer)

    #reset timer label
    timer_label.config(text="Timer", fg=GREEN)

    #reset timer text
    canvas.itemconfig(timer_text, text="00:00")

    #reset check mark label
    check_mark_label.config(text="")

    #reset reps
    global reps
    reps = 0


def start_timer():
    '''have the timer start from 25 minutes and go to the background after the first three sets of WORK_MIN the counter
            changes to SHORT_BREAK_MIN after each WORK_MIN and after every 4th WORK_MIN the counter changes
             to LONG_BREAK_MIN'''

    #create global variable to keep track of the number of sets
    global reps
    reps += 1

    #set time values to seconds
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)

    #check if 4 reps are completed before changing the timer label
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)

    #check if 1 rep is completed before changing the timer label
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

    #set label to work when not break
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

def count_down(count):
    '''function to count down the timer from 25 minutes to 00:00 and have the window come back to foreground'''

    #convert seconds to minutes and seconds
    count_minutes = count // 60
    count_seconds = count % 60

    #update the timer text on the canvas
    canvas.itemconfig(timer_text, text=f"{count_minutes:02d}:{count_seconds:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = (reps // 2)
        for _ in range(work_sessions):
           marks += "✔️"
        check_mark_label.config(text=marks)
#create window
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

#create tomato image and add it to canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill=WHITE, font=(FONT_NAME, 33, "bold"))
canvas.grid(row=1, column=1)

#create timer label
timer_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)

#create start button
start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

#create reset button
reset_button =tk.Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=3)

#create check mark tally
check_mark_label = tk.Label(fg=GREEN, bg=YELLOW)
check_mark_label.grid(row=3, column=1)

#start the main loop of the application
window.mainloop()