import tkinter as tk
import sys
import pathlib as Path
from PIL import Image, ImageTk

class MenuBar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)
        
        file_menu = tk.Menu(self)
        # Adds a menu option called "File"
        self.add_cascade(label="File", menu=file_menu)
        # Adds a button in the menu called "File"
        file_menu.add_command(label="Exit", command=self.quit)
        
        new_menu = tk.Menu(self)
        self.add_cascade(label="New", menu=new_menu)
        new_menu.add_command(label="exit2", command=self.quit)
        
    def quit(self):
        sys.exit()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Standard geometry
        self.title("First application")
        self.geometry("800x600")
        self.resizable(False, False)
    
        # Background image homescreen
        # # Define working directory    
        WdImage = Path.Path("Bilder/Romnes1.png")
        # # Create the canvas for the image
        canvas = tk.Canvas(self, width=800, height=600, highlightthickness=5, highlightbackground="black")
        canvas.pack()
        # # open image with TIL, resize it and convert to a tkinter object
        fileplacement = Image.open(WdImage)
        newbackgroundimage = fileplacement.resize((800,600))
        pic = ImageTk.PhotoImage(newbackgroundimage)
        # # Place the image in the canvas
        canvas.create_image(0, 0, image=pic, anchor="nw")
        
        
        # menubar configuration
        menubar = MenuBar(self)
        self.config(menu=menubar)
        
        self.mainloop()
        


a = App()
    