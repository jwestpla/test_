import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk

def firstcommand():
    root.quit()

root = tk.Tk()
root.geometry("800x600")

canvas = tk.Canvas(width=800, height=600, highlightthickness=5, highlightbackground="black")
canvas.pack()

button1 = tk.Button(text="Button 1")

canvas.create_window(100, 300, window=button1)

root.mainloop()