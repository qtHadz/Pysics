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
    canvas = Canvas()
    def line(start,end,color,width):
        canvas.create_line(start,end,width=width,fill=color)
        canvas.pack(fill=BOTH, expand=1)
    def polyb(vertices,color,width):
        canvas.create_line(vertices,vertices[0],fill=color,width=width)
        canvas.pack(fill=BOTH, expand=1)
    def poly(vertices,color):
        points = []
        for vertex in vertices:
            points.append(vertex[0])
            points.append(vertex[1])
        canvas.create_polygon(points,fill=color)
        canvas.pack(fill=BOTH, expand=1)
