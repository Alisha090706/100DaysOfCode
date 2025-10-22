from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# ---------------------------- GLOBAL VARIABLES ------------------------------- #
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer",fg=GREEN)
    check_marks.config(text="")

    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps

    work_time_sec= WORK_MIN*60
    short_break_sec= SHORT_BREAK_MIN*60
    long_break_sec= LONG_BREAK_MIN*60

    reps+=1
    
    if reps%8==0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        
    else:
        count_down(work_time_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    "00:00 formating"
    minutes= count//60
    seconds= count%60
    if seconds<10:
        seconds=f"0{seconds}"
    if minutes<10:
        minutes=f"0{minutes}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if(count>0):
        timer=window.after(1000, count_down, count-1)
    else:
        start_time()
        if reps%2==0:
            ticks=""
            for _ in range(reps//2):
                ticks+="✔"
            check_marks.config(text=ticks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

window.config(padx=100, pady=50, bg=YELLOW)

### A canvas to put the tomato image and the timer text
canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text=canvas.create_text(103,130, text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)


### Label For the title
title_label=Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME,50,"bold"))
title_label.grid(column=1, row=0)


### Start Button
start_button=Button(text="Start", bg="white", highlightthickness=0, command=start_time)
start_button.grid(column=0, row=2)


### Reset Button
reset_button=Button(text="Reset", bg="white", highlightthickness=0, command=reset_time)
reset_button.grid(column=2, row=2)

### Check Marks
mark=""
check_marks=Label(text=mark, bg=YELLOW, fg=GREEN, font=(FONT_NAME,20,"bold"))
check_marks.grid(column=1, row=3)

window.mainloop()