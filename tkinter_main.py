import tkinter as tk
import sys
import pathlib as Path
from PIL import Image, ImageTk
from tkmacosx import Button

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


class HomeScreenButtons(tk.Button):
    def __init__(self, parent):
        super().__init__(parent)
        """
        A known problem on mac is not being able to color in buttons, which is why tkmacosx is imported
        This lets us change the color of a button with no problem at all! :-)
        """
        
        button1 = Button(parent, text="Button 1", font=("Times new Roman", 25), bg="#5B786F", fg="#CBD2C6", command=self.click, width=125, highlightthickness=5, highlightbackground="black")
        button2 = Button(parent, text="Button 2", font=("Times new Roman", 25), bg="#5B786F", fg="#CBD2C6", command=self.click, width=125, highlightthickness=5, highlightbackground="black")
        
        parent.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")
        parent.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1, uniform="a")

        button1.grid(row=3, column=1, sticky="e")
        button2.grid(row=3, column=3, sticky="w")
        
    def click(self):
        pass

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
        canvas.place(x=0, y=0)
        # # open image with TIL, resize it and convert to a tkinter object
        fileplacement = Image.open(WdImage)
        newbackgroundimage = fileplacement.resize((800,600))
        pic = ImageTk.PhotoImage(newbackgroundimage)
        # # Place the image in the canvas
        canvas.create_image(0, 0, image=pic, anchor="nw")
        
        
        # Text on image
        intro_label = tk.Label(canvas, font=("Times new Roman", 40), text="Romnes Moreller", bg="#5B786F",
                               fg="#CBD2C6", padx=10, pady=5, highlightthickness=5, highlightbackground="black", relief="raised")
        intro_label.pack()
        canvas.create_window(400, 125, window=intro_label)

        
        HomeScreenButtons(self)
        
        # menubar configuration
        menubar = MenuBar(self)
        self.config(menu=menubar)
        
        self.mainloop()
        


a = App()
    