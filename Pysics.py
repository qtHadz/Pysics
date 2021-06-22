from math import *


class vector2():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.mag = sqrt(x*x + y*y)
        self.angle = copysign(1,self.y)*acos(self.x/self.mag)
    def __str__(self):   
        return "["+str(self.x)+","+str(self.y)+"]" 
    def __mul__(self,other):
        if type(other) == type(1) or type(other) == type(1.1):
            return vector2(self.x*other,self.y*other)
    def __rmul__(self,other):
        if type(other) == type(1) or type(other) == type(1.1):
            return vector2(self.x*other,self.y*other)
    def __truediv__(self,other):
        if type(other) == type(1) or type(other) == type(1.1):
            return vector2(self.x/other,self.y/other)


