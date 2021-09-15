import pygame
import sys
from math import *
import random
pygame.init()

screenHeight = 500
screenWidth = 500
screenSize = [screenWidth,screenHeight]

screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

GRAVITY = 9.81 #m/s
G = 6.67 * pow(10,-11)
FPS = 120

RUNSPEED = 3

class Vector2():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def mag(self):
        return sqrt(self.x*self.x + self.y*self.y)
    def normalised(self):
        if self.mag() == 0:
            return 0
        return self/self.mag()
    def angle(self):
        mag = self.mag()
        if mag == 0:
            return 0
        else:
            return copysign(1,self.y)*acos(self.x/mag)
    def perpendicular(self):
        return Vector2.toEuclid(self.angle()+pi/2,1)
    def flist(self):
        return [self.x,self.y]
    def toPolar(self):
        return [self.mag(),self.angle()]
    def toEuclid(angle,mag):
        return Vector2(-mag*cos(angle),-mag*sin(angle))
    def __str__(self):
        return f"{self.x},{self.y}"
    def __add__(self,other):
        return Vector2(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector2(self.x-other.x,self.y-other.y)
    def __truediv__(self,other):
        return self* (1/other)
    def __mul__(self,other):
        return Vector2(self.x*other,self.y*other)
    def __rmul__(self,other):
        return Vector2(self.x*other,self.y*other)
    def bounceAgainst(self,other,bounce):
        a1 = pi - self.angle()
        a2 = other.angle()
        a = pi +2*a2 - a1
        v = Vector2.toEuclid(a,self.mag())
        v.x = -v.x
        v *= sqrt(bounce)
        return v


class Object():
    def __init__(self,name,color,mass,size,pos,vel):
        self.name = name
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.size = size
        self.color = color

    def sayName(self):
        print(self.name)
        return None

    def update(self,others):
        #collision stuff
        for other in others:
            if other != self:
                if (other.pos+(other.vel*RUNSPEED/(2*FPS)) - (self.pos+(self.vel*RUNSPEED/(2*FPS)))).mag() <= (self.size[0]/2 + other.size[0]/2):           
                    #did some research for these (https://courses.lumenlearning.com/boundless-physics/chapter/collisions/)
                    out1X = (self.mass - other.mass)*self.vel.x/(other.mass+self.mass) + 2*other.mass*other.vel.x/(other.mass+self.mass)
                    out1Y = (self.mass - other.mass)*self.vel.y/(other.mass+self.mass) + 2*other.mass*other.vel.y/(other.mass+self.mass)
                    out2X = (other.mass - self.mass)*other.vel.x/(other.mass+self.mass) + 2*self.mass*self.vel.x/(other.mass+self.mass)
                    out2Y = (other.mass - self.mass)*other.vel.y/(other.mass+self.mass) + 2*self.mass*self.vel.y/(other.mass+self.mass)
                    
                    # betweenVec = other.pos - self.pos
                    # vecToBounce = Vector2.perpendicular(betweenVec.normalised())
                    # print(betweenVec.normalised(),vecToBounce)
                    # print(self.vel)
                    # self.vel = Vector2.bounceAgainst(Vector2(out1X,out1Y),vecToBounce,1)
                    # print(self.vel)
                    # other.vel = Vector2.bounceAgainst(Vector2(out2X,out2Y),vecToBounce,1)
                    
                    self.vel = Vector2(out1X,out1Y)
                    other.vel = Vector2(out2X,out2Y)

        #gravitatioanl field stuff
        for other in others:
            if other != self:
                r = (other.pos - self.pos).mag()
                forceMag = G*self.mass*other.mass/(r*r)
                forceAngle = (self.pos - other.pos).angle()
                force = Vector2.toEuclid(forceAngle,forceMag)*RUNSPEED
                self.applyForce(force,RUNSPEED/FPS)
                #print(force,self.vel,self.name)
      

        self.draw()
        #self.applyGravity(RUNSPEED/FPS)
        self.applyVelocity(RUNSPEED/FPS)

    def bounce(self,against):
        self.vel = self.vel.bounceAgainst(against,1)

    def applyGravity(self,deltaTime): #no longer in use, all objects attracted to earth object by gravity using proper equations
        self.vel += Vector2(0,GRAVITY*deltaTime)

    def applyVelocity(self,deltaTime):
        self.pos += self.vel*deltaTime;

        if (self.pos.y+self.size[1]/2 > screenHeight): #or self.pos.y-self.size[1]/2 < 0):
            self.pos -= self.vel*deltaTime
            self.bounce(Vector2(1,0))
        if (self.pos.x+self.size[0]/2 > screenWidth or self.pos.x-self.size[0]/2 < 0):
            self.pos -= self.vel*deltaTime
            self.bounce(Vector2(0,1))
        #if self.pos.y >= self.pos.x + screenHeight/2 - self.size[0]/2: #losers way of doing collision with line
        #  self.pos -= self.vel*deltaTime
        #  self.bounce(Vector2(-1,1))

    def applyForce(self,force,deltaTime):
        #F = MA => A = F/M
        self.vel += (force * 1/self.mass)*deltaTime

class Ball(Object):
    def draw(self):
        pygame.draw.circle(screen,self.color,self.pos.flist(),self.size[0]/2)

class Rectangle(Object):
    def draw(self):
        r = ((self.pos-Vector2(self.size[0]/2,self.size[1]/2)).flist(),self.size)
        pygame.draw.rect(screen,self.color,r)
class OtherObject(Object):
    def draw(self):
        return

def GenerateBalls(num):  

    balls = []
    for i in range(0,noBalls):
        rRad = random.randint(10,20)
        rPos = Vector2(random.randint(100,400),random.randint(100,300))
        rVel = Vector2(random.randint(-20,20),random.randint(-20,20))
        color = (random.randint(100,255),random.randint(100,255),random.randint(100,255))
        self = Ball(str(i),color,rRad,[rRad,rRad],rPos,rVel)
        balls.append(self)
    return balls

noBalls = 10
balls = []

balls = GenerateBalls(noBalls)
earth = OtherObject("Earth",(100,100,100),5.972*pow(10,24),[6371000*2,6371000*2],Vector2(screenWidth/2,screenHeight+6371000),Vector2(0,0))
balls.append(earth)

# b1 = Ball("1",(0,150,150),1000000,[20,20],Vector2(screenWidth/2,screenHeight/2-100),Vector2(-12,0))
# b2 = Ball("2",(255,255,255),1000000,[10,10],Vector2(screenWidth/2,screenHeight/2+100),Vector2(12,0))
# balls.append(b1)
# balls.append(b2)



while True:
    screen.fill((0,0,0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for ball in balls:
        ball.update(balls)
    
    #print(balls[1].pos,balls[1].vel)
    
    pygame.display.flip()

    clock.tick(FPS)