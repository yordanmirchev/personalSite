import math
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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark_label.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    duration = 0

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Long break", fg=RED)
        duration = long_break_sec
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        duration = short_break_sec
    else:
        timer_label.config(text="Work", fg=GREEN)
        duration = work_sec


    count_down(duration)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = int(count % 60)

    if seconds < 10:
        seconds = f"0{seconds}"

    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps > 0 and reps % 2 == 0 :
            check_mark_label.config(text="✔")
        else:
            check_mark_label.config(text="")

# ---------------------------- UI SETUP ------------------------------- #
def do_something(text):
    print(text)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), foreground=GREEN, background=YELLOW)
timer_label.grid(row=0, column=1)

button_start = Button(text="Start", command=start_timer, font=(FONT_NAME, 15, "bold"), background=YELLOW,
                      highlightthickness=0)
button_start.grid(row=2, column=0)

button_reset = Button(text="Start", font=(FONT_NAME, 15, "bold"), background=YELLOW, highlightthickness=0, command=reset_timer)
button_reset.grid(row=2, column=2)

# canvas_tick = Canvas(width=50, height=50, bg=YELLOW)
# tick_photo = PhotoImage(file="resized_png.png")
# canvas_tick.create_image(40, 40, image=tick_photo)
# canvas_tick.grid(row=3,column=1)

check_mark_label = Label(foreground=GREEN, background=YELLOW)
check_mark_label.grid(row=3, column=1)

window.mainloop()
