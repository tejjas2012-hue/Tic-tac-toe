import tkinter as tk
import os
import sys
import subprocess

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("330x350")
root.config(bg="black")
player1_boxes = []
player2_boxes = []
turn = "player1"
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
    if 0 in player1_boxes and 1 in player1_boxes and 2 in player1_boxes or 3 in player1_boxes and 4 in player1_boxes and 5 in player1_boxes or 6 in player1_boxes and 7 in player1_boxes and 8 in player1_boxes or 0 in player1_boxes and 3 in player1_boxes and 6 in player1_boxes or 1 in player1_boxes and 4 in player1_boxes and 7 in player1_boxes or 2 in player1_boxes and 5 in player1_boxes and 8 in player1_boxes or 0 in player1_boxes and 4 in player1_boxes and 8 in player1_boxes or 2 in player1_boxes and 4 in player1_boxes and 6 in player1_boxes:
        winner = "Player1"
        win_label.config(text="Player1 WON!", fg="lime")
    elif 0 in player2_boxes and 1 in player2_boxes and 2 in player2_boxes or 3 in player2_boxes and 4 in player2_boxes and 5 in player2_boxes or 6 in player2_boxes and 7 in player2_boxes and 8 in player2_boxes or 0 in player2_boxes and 3 in player2_boxes and 6 in player2_boxes or 1 in player2_boxes and 4 in player2_boxes and 7 in player2_boxes or 2 in player2_boxes and 5 in player2_boxes and 8 in player2_boxes or 0 in player2_boxes and 4 in player2_boxes and 8 in player2_boxes or 2 in player2_boxes and 4 in player2_boxes and 6 in player2_boxes:
        winner = "Player2"
        win_label.config(text="Player2 WON!", fg="red")

    check_win()
def make_move(number, button):
    global turn

    if winner != "":
        return

    if number in occupied_boxes:
        return

    if turn == "player1":
        player1_boxes.append(number)
        button.config(image=ximage)
        turn = "player2"
    else:
        player2_boxes.append(number)
        button.config(image=oimage)
        turn = "player1"

    occupied_boxes.append(number)
    check_win()

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
    command=lambda: make_move(0, button0)
)
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
    command=lambda: make_move(1, button1)
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
    command=lambda: make_move(2, button2)
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
    command=lambda: make_move(3, button3)
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
    command=lambda: make_move(4, button4)
)
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
    command=lambda: make_move(5, button5))

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
    command=lambda: make_move(6, button6)
)

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
    command=lambda: make_move(7, button7)
)
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
    command=lambda: make_move(8, button8)
)

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