from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REP = 0
Timer = 'None'


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(Timer)
    global REP
    REP = 0
    canvas.itemconfig(timer_text, text=f"00:00")
    Timer_label.config(text='Timer')
    check_label.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REP
    REP += 1

    if REP % 8 == 0:
        Timer_label.config(text='Long Break', fg=GREEN)
        time = LONG_BREAK_MIN * 60
        count_down(time)
    elif REP % 2 == 0:
        Timer_label.config(text='Short Break', fg=PINK)
        time = SHORT_BREAK_MIN * 60
        count_down(time)
    else:
        Timer_label.config(text='Work', fg=RED)
        time = WORK_MIN * 60
        count_down(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# function with great approach
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global Timer
        Timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        for i in range(math.floor(REP / 2)):
            marks += ' ✔'
        check_label.config(text=marks, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=20, pady=20, bg=YELLOW)

Timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 26, 'bold'))
Timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(101, 130, text=f"00:00", fill='white', font=(FONT_NAME, 20, 'bold'))
canvas.grid(row=1, column=1)

button_start = Button(text="Start", font=(FONT_NAME, 10, 'bold'), fg=RED, bg=YELLOW, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", font=(FONT_NAME, 10, 'bold'), fg=RED, bg=YELLOW, command=reset)
button_reset.grid(row=2, column=2)

check_label = Label(bg=YELLOW)
check_label.grid(row=3, column=1)

window.mainloop()
