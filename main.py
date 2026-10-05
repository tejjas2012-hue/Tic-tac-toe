import tkinter as tk
import subprocess
import sys
import os

root = tk.Tk()
root.title("Tic Tac Toe Launcher")
root.geometry("400x300")
root.config(bg="black")

def launch_gameai():
    subprocess.Popen([os.path.join(os.path.dirname(sys.executable), "game", "game.exe")])
    root.destroy()

def launch_game():
    subprocess.Popen([os.path.join(os.path.dirname(sys.executable), "game2", "game2.exe")])
    root.destroy()

play_button = tk.Button(
    root,
    text="PLAY WITH AI",
    font=("Arial Black", 16),
    command=launch_gameai
)

play_button.pack(pady=50)

playfriend = tk.Button(
    root,
    text="PLAY WITH FRIENDS",
    font=("Arial Black", 16),
    command=launch_game
)
playfriend.pack(pady=20)
root.mainloop()