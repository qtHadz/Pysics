from Engine import *

Window = display("600x600","test")
Window.fill("white")

draw.line([25,25],[100,25],"red",3)
draw.polyb([[25,25],[100,25],[100,125]],"blue",3)
draw.poly([[25,25],[100,25],[100,125]],"green")
Window.update()
