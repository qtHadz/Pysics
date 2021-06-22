import sys
from math import *

class Vector2():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def compare(self,vector):
        xl = self.x - 0.00005
        xh = self.x + 0.00005
        yl = self.y - 0.00005
        yh = self.y +0.00005
        if vector.x < xh and vector.x > xl and vector.y < yh  and vector.y > yl:
            return True
        else:
            return False
    def asList(self):
        return [self.x,self.y]
    def asVector(point):
        return Vector2(point[0],point[1])
    def __neg__(self):
        return Vector2(-self.x,-self.y)
    def __str__(self):
        return f"[{self.x},{self.y}]"
    def __lt__(self,other):
        if type(self) == type(other):
            if self.x < other.x and self.y < other.y:
                return True
        else:
            raise Exception("Not Supported")
    def __gt__(self,other):
        if type(self) == type(other):
            if self.x > other.x and self.y > other.y:
                return True
        else:
            raise Exception("Not Supported")
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
    def abs(self): #absolute value
        return sqrt(self.x*self.x + self.y*self.y)
    def mag(self):
        return sqrt(self.x*self.x + self.y*self.y)
    def normalise(self):
        return self/self.abs()
    def angle(self): #angle to horizontal
        mag = self.mag()
        if self.x != 0:
            a1 = atan(self.y/self.x)
        else:
            a1 = pi/2
        v = Vector2.poltovec(mag,a1)     
        return a1
    def poltovec(mag,angle):
        return Vector2(mag*cos(angle),-mag*sin(angle))
    def anglebetween(fromm,to): #angle between two vectors
        if type(fromm) == type(to):
            return fromm.angle() - to.angle()
        else:
            raise Exception("Not Supported")
    def angleto(self,to): # angle between two vectors
        if type(self) == type(to):
            return self.angle() - to.angle()
        else:
            raise Exception("Not Supported")
    def rotate(self,centre,direction,angle): #rotate around a point
        px = self.x-centre.x
        py = self.y-centre.y
        x = cos(angle)*px -direction*sin(angle)*py
        y = direction*sin(angle)*px + cos(angle)*py
        self.x = x +centre.x
        self.y = y +centre.y
        return self
    def rotateorigin(self,direction,angle): #rotate around the origin
        x = cos(angle)*self.x -direction*sin(angle)*self.y
        y = direction*sin(angle)*self.x + cos(angle)*self.y
        self = Vector(x,y)
        return self
    def vectorto(self,destination): #returns vector that goes to destination
        if type(self) == type(destination):
            x = destination.x - self.x
            y = destination.y - self.y
            return Vector2(x,y)
    def vectortoward(self,destination): #returns unit vector in direction of destination
        return self.vectorto(destination).normalise()
    def bounceagainst(self,barrier,bounciness):
        angle = (self.angleto(barrier))
        angle += barrier.angle()
        mag = self.mag()*bounciness
        v = Vector2.poltovec(mag,angle)
        print(self,v)
        return v

class GameObject():
    def __init__(self,pos,rotation,size,bounds,gravity,mass,bouncy):
        self.pos = pos
        self.velocity = Vector2(0,0)
        self.rotation  = rotation
        self.gravity = gravity
        self.acceleration = Vector2(0,0)
        self.bounds = bounds
        self.bouncy = bouncy
        self.size = size
    def update(self):
        self.addvelocity(Vector2(0,self.gravity))
        self.addvelocity(self.acceleration)
        self.move()
    def addvelocity(self,acceleration):
        self.velocity += acceleration
    def setvelocity(self,velocity):
        self.velocity = velocity
    def applyforce(self,force):
        self.acceleration += force/self.mass
    def applyforceresult(self,force,angle):
        fVec = Vector2(force*cos(angle),force*sin(angle))
        self.acceleration += fVec/self.mass
    def setacc(self,acc):
        self.acceleration = acc
    def setacceleration(self,acceleration):
        self.acceleration = acceleration
    def move(self):
        self.pos += self.velocity
        if self.pos.y > self.bounds.y-(self.size.y/2):
            self.pos -= self.velocity
            self.velocity = self.velocity.bounceagainst(Vector2(1,0),self.bouncy)
            self.pos += self.velocity
        if self.pos.x > self.bounds.x-(self.size.x/2) or self.pos.x <= 0:
            self.pos -= self.velocity
            self.velocity = self.velocity.bounceagainst(Vector2(0,1),self.bouncy)
            self.pos += self.velocity            
        
    def setpos(self,pos):
        self.pos = pos








