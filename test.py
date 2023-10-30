import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk

def firstcommand():
    root.quit()

root = tk.Tk()
root.geometry("800x600")


# Define working directory
realwd = Path("Bilder/Romnes1.png")

# Create a canvas for the image
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# open image with TIL, resize it and convert to a tkinter object
fileplacement = Image.open(realwd)
newbackgroundimage = fileplacement.resize((800,600))
pic = ImageTk.PhotoImage(newbackgroundimage)

# Create the image and place it in the canvas
canvas.create_image(0, 0, image=pic, anchor="nw")

root.mainloop()