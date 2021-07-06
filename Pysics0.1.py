from math import *
import sys

class Vector2():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def mag(self):
        m = sqrt(x*x + y*y)
        return m
    def angle(self):
        a = copysign(1,self.y)*acos(x/self.mag())
        return a
