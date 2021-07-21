import sys
from math import *

class Vector2():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.list = [x,y]
        self.flist = [floor(x),floor(y)]
    def mag(self):
        return sqrt(self.x*self.x + self.y*self.y)
    def angle(self):
        mag = self.mag()
        if mag == 0:
            return 0
        else:
            return copysign(1,self.y)*acos(self.x/mag)
    def polar(angle,mag):
        y = -mag*sin(angle)
        x = mag*cos(angle)
        return Vector2(x,y)
    def __neg__(self):
        return Vector2(-self.x,-self.y)
    def __str__(self):
        return "["+str(self.x)+","+str(self.y)+"]"
    def __mul__(self,other):
        if type(other) == type(1) or type(other) == type(1.0):
            return Vector2(self.x*other,self.y*other)
        else:
            raise Exception("Not Supported")
    def __rmul__(self,other):
        if type(other) == type(1) or type(other) == type(1.0):
            return Vector2(self.x*other,self.y*other)
        else:
            raise Exception("Not Supported")
    def __truediv__(self,other):
        if type(other) == type(1) or type(other) == type(1.0):
            return Vector2(self.x/other,self.y/other)
        else:
            raise Exception("Not Supported")
    def __add__(self,other):
        if type(self) == type(other):
            return Vector2(self.x+other.x,self.y+other.y)
        elif type(other) == type([]):
            vs = []
            for v in other:
                vs.append([v[0]+self.x,v[1]+self.y])
            return vs
        else:
            raise Exception("Not Supported")
    def __sub__(self,other):
        if type(self) == type(other):
            return Vector2(self.x-other.x,self.y-other.y)
        else:
            raise Exception("Not Supported")
    def bounceagainst(self,barrier,bounciness):
        a1 = pi - self.angle()
        a2 = barrier.angle()
        a = pi +2*a2 - a1
        v = Vector2.polar(a,self.mag())
        v *= bounciness
        self = v
        return v

GRAVITY = 9.81
class PhysicsObject():
    def __init__(self,pos,mass,area,dims,bouncy):
        self.pos = pos
        self.velocity = Vector2(0,0)
        self.acceleration = Vector2(0,0)
        self.drag = Vector2(0,0)
        self.mass = mass
        self.dims = dims
        self.area = area
        self.density = mass/area
        self.bouncy = bouncy
    def applygravity(self):
        self.velocity.y += GRAVITY
    def applyacceleration(self,acc):
        self.velocity += acc
    def setacceleration(self,acc):
        self.velocity += acc
    def applyforce(self,force):
        self.velocity += force/self.mass
    def setvelocity(self,vel):
        self.velocity = vel
    def setpos(self,pos):
        self.pos = pos
    def move(self):
        self.pos += self.velocity

    
        
