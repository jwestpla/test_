import tkinter as tk

class mainframe(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hello world")
        label.pack()
        label.bind("<1>", self.quit)


root = tk.Tk()
mainframe(root).pack()

root.mainloop()