import tkinter as tk
import random
import os
import sys
import subprocess

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("330x350")
root.config(bg="black")
player_boxes = []
ai_boxes = []
occupied_boxes = []
winner = ""
def resource_path(filename):
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, filename)

ximage = tk.PhotoImage(file=resource_path("x.png"))
ximage = ximage.subsample(5, 5)

oimage = tk.PhotoImage(file=resource_path("o.png"))
oimage = oimage.subsample(5, 5)

board_image = tk.PhotoImage(file=resource_path("board.png"))
pause_image = tk.PhotoImage(file=resource_path("pause.png"))
board_label = tk.Label(root, image=board_image)
board_label.place(x=0, y=0)

def check_win():
    global winner
    if 0 in player_boxes and 1 in player_boxes and 2 in player_boxes or 3 in player_boxes and 4 in player_boxes and 5 in player_boxes or 6 in player_boxes and 7 in player_boxes and 8 in player_boxes or 0 in player_boxes and 3 in player_boxes and 6 in player_boxes or 1 in player_boxes and 4 in player_boxes and 7 in player_boxes or 2 in player_boxes and 5 in player_boxes and 8 in player_boxes or 0 in player_boxes and 4 in player_boxes and 8 in player_boxes or 2 in player_boxes and 4 in player_boxes and 6 in player_boxes:
        winner = "player"
        win_label.config(text="YOU WON!", fg="lime")
    elif 0 in ai_boxes and 1 in ai_boxes and 2 in ai_boxes or 3 in ai_boxes and 4 in ai_boxes and 5 in ai_boxes or 6 in ai_boxes and 7 in ai_boxes and 8 in ai_boxes or 0 in ai_boxes and 3 in ai_boxes and 6 in ai_boxes or 1 in ai_boxes and 4 in ai_boxes and 7 in ai_boxes or 2 in ai_boxes and 5 in ai_boxes and 8 in ai_boxes or 0 in ai_boxes and 4 in ai_boxes and 8 in ai_boxes or 2 in ai_boxes and 4 in ai_boxes and 6 in ai_boxes:
        winner = "ai"
        win_label.config(text="AI WON!", fg="red")
def ai_move():
    
    if len(occupied_boxes) == 9:
        return

    ai_select = random.randint(0, 8)

    while ai_select in occupied_boxes:
        ai_select = random.randint(0, 8)

    ai_boxes.append(ai_select)
    occupied_boxes.append(ai_select)

    if ai_select == 0:
        button0.config(image=oimage)
    elif ai_select == 1:
        button1.config(image=oimage)
    elif ai_select == 2:
        button2.config(image=oimage)
    elif ai_select == 3:
        button3.config(image=oimage)
    elif ai_select == 4:
        button4.config(image=oimage)
    elif ai_select == 5:
        button5.config(image=oimage)
    elif ai_select == 6:
        button6.config(image=oimage)
    elif ai_select == 7:
        button7.config(image=oimage)
    elif ai_select == 8:
        button8.config(image=oimage)

    check_win()
def button0_click():

    if winner == "player" or winner == "ai":
     return
    if 0 in occupied_boxes:
        return
    player_boxes.append(0)
    occupied_boxes.append(0)
    button0.config(image=ximage)

    check_win()
    ai_move()


def button1_click():
    if winner == "player" or winner == "ai":
     return
    if 1 in occupied_boxes:
        return
    player_boxes.append(1)
    occupied_boxes.append(1)
    button1.config(image=ximage)
    check_win()

    ai_move()

def button2_click():
    if winner == "player" or winner == "ai":
     return
    if 2 in occupied_boxes:
        return
    player_boxes.append(2)
    occupied_boxes.append(2)
    button2.config(image=ximage)

    check_win()
    ai_move()

def button3_click():
    if winner == "player" or winner == "ai":
     return
    if 3 in occupied_boxes:
        return
    player_boxes.append(3)
    occupied_boxes.append(3)
    button3.config(image=ximage)

    check_win()
    ai_move()

def button4_click():
    if winner == "player" or winner == "ai":
     return
    if 4 in occupied_boxes:
        return
    player_boxes.append(4)
    occupied_boxes.append(4)
    button4.config(image=ximage)

    check_win()
    ai_move()
    
def button5_click():
    if winner == "player" or winner == "ai":
     return
    if 5 in occupied_boxes:
        return
    player_boxes.append(5)
    occupied_boxes.append(5)
    button5.config(image=ximage)

    check_win()
    ai_move()

def button6_click():
    if winner == "player" or winner == "ai":
     return
    if 6 in occupied_boxes:
        return
    player_boxes.append(6)
    occupied_boxes.append(6)
    button6.config(image=ximage)

    check_win()

    ai_move()

def button7_click():
    if winner == "player" or winner == "ai":
     return
    if 7 in occupied_boxes:
        return
    player_boxes.append(7)
    occupied_boxes.append(7)
    button7.config(image=ximage)

    check_win()

    ai_move()

def button8_click():
    if winner == "player" or winner == "ai":
     return
    if 8 in occupied_boxes:
        return
    player_boxes.append(8)
    occupied_boxes.append(8)
    button8.config(image=ximage)

    check_win()

    ai_move() 

win_label = tk.Label(
    root,
    text="",
    font=("Arial Black", 24),
    fg="lime",
    bg="black"
)
win_label.place(x=75, y=300)

button0 = tk.Button(root,
    text="",
    width=6,
    height=3,
    bg="black",
    activebackground="black",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=button0_click)

button0.place(x=26, y=20, width=65, height=65)

button1 = tk.Button(root,
    text="",
    width=6,
    height=3,
    bg="black",
    activebackground="black",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=button1_click
    )

button1.place(x=126, y=20, width=65, height=65)

button2 = tk.Button(root,
    text="",
    width=6,
    height=3,
    bg="black",
    activebackground="black",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=button2_click
    )

button2.place(x=220, y=20, width=65, height=65)

button3 = tk.Button(root,
    text="",
    width=6,
    height=3,
    bg="black",
    activebackground="black",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=button3_click
    )

button3.place(x=26, y=120, width=65, height=65)

button4 = tk.Button(root,
    text="",
    width=6,
    height=3,
    bg="black",
    activebackground="black",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=button4_click)

button4.place(x=120, y=120, width=65, height=65)

button5 = tk.Button(root,
    text="",
    width=6,
    height=3,
    bg="black",
    activebackground="black",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=button5_click)

button5.place(x=220, y=120, width=65, height=65)

button6 = tk.Button(root,
    text="",
    width=6,
    height=3,
    bg="black",
    activebackground="black",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=button6_click)

button6.place(x=26, y=210, width=65, height=65)

button7 = tk.Button(root,
    text="",
    width=6,
    height=3,
    bg="black",
    activebackground="black",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=button7_click)

button7.place(x=120, y=210, width=65, height=65)

button8 = tk.Button(root,
    text="",
    width=6,
    height=3,
    bg="black",
    activebackground="black",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=button8_click)

button8.place(x=220, y=210, width=65, height=65)

pause_frame = tk.Frame(root, bg="black")
pause_frame.place(x=0, y=0, width=330, height=350)
pause_frame.place_forget()

def restart_game():
    os.execl(sys.executable, sys.executable, *sys.argv)
def pause():
    pause_frame.place(x=0, y=0, width=330, height=350)
    pause_frame.lift()

def resume():
    pause_frame.place_forget()

black_label = tk.Label(pause_frame, text="", font=("Arial Black", 24), fg="white", bg="black")
black_label.pack(pady=10, padx=100)
reset_button = tk.Button(pause_frame, text="Reset", font=("Arial Black", 16), command=lambda: restart_game())
reset_button.pack(pady=10, padx=100)

pause_button = tk.Button(text="", image=pause_image, command=lambda: pause())
pause_button.place(x=300, y=5, width=30, height=30)

resume_button = tk.Button(pause_frame, text="Resume", font=("Arial Black", 16), command=lambda: resume())
resume_button.pack(pady=10, padx=100)

def close_game():
    subprocess.Popen([sys.executable, "main.py"])
    root.destroy()

close_button = tk.Button(
    pause_frame,
    text="Exit",
    command=close_game
)
close_button.place(x=5, y=5, width=50, height=30)

root.mainloop()