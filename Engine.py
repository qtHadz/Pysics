from tkinter import *

class display():
    def __init__(self,dimensions,name):
        self.window = Tk(className = name)
        self.window.geometry(dimensions)
    def update(self):
        self.window.mainloop()
    def setsize(self,size):
        self.geometry(size)
    def fill(self,color):
        self.window.configure(bg=color)


canvas = Canvas()
class draw():
    def line(surface,start,end):
        canvas.create_line(start,end)
    
