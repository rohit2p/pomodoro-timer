"""creating a pomodoro timer using tkinter module"""

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfigure(timer_text, text="00:00")
    timer_lable.config(text="Timer")
    tick_lable.config(text="")
    global reps
    reps = 0  # setting reps to zero so that all labels can reset also


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global reps
    reps += 1

    # converting time in seconds
    work_sec = WORK_MIN * 60
    short_brake_sec = SHORT_BREAK_MIN * 60
    long_brake_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_brake_sec)
        timer_lable.config(text="Brake", fg=RED)
    elif reps % 2 == 0:
        count_down(short_brake_sec)
        timer_lable.config(text="Brake", fg=PINK)
    else:
        count_down(work_sec)
        timer_lable.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()
        marks = ""
        works_session = math.floor(reps / 2)
        for _ in range(works_session):
            marks += "✔️"
        tick_lable.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# creating the window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# creating canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# creating "00:00" text that will overlap the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# creating the timer label
timer_lable = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
timer_lable.grid(column=1, row=0)

# creating the tick label
tick_lable = Label(fg=GREEN)
tick_lable.grid(column=1, row=4)

# creating the start button
start_button = Button(text="start", command=start_time)
start_button.grid(column=0, row=2)

# creating the reset button
reset_button = Button(text="reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
