import Pysics,pygame,sys
from math import *
PhysicsObject = Pysics.PhysicsObject
Vector2 = Pysics.Vector2

screenWidth = 1000
screenHeight = 500
screenSize = (screenWidth,screenHeight)
screen = pygame.display.set_mode(screenSize)


class ball():
    def __init__(self,name,color,startPos,mass,radius,bounciness):
        self.name = name
        self.color = color
        self.startPos = startPos
        self.mass = mass
        self.radius = radius
        self.bounciness = bounciness
        self.physics = PhysicsObject(startPos,mass,pi*radius*radius,[radius,radius],bounciness)
    def __str__(self):
        out = f"{self.name}:\n"
        out += f"mass: {self.mass}kg\n"
        out += f"radius: {self.radius}m\n"
        out += f"bounciness?: {self.mass}?\n"
        out += f"velocity: {self.physics.velocity}m/s\n"
        out += f"pos: {self.physics.pos}\n"
        return out
    def draw(self):
        pygame.draw.circle(screen,self.color,self.physics.pos.flist,self.radius)
    def reset(self):
        self.physics.setpos(self.startPos)
        self.physics.setvelocity(Vector2(0,0))
    def move(self,gravity):
        if gravity:
            self.physics.velocity.y += Pysics.GRAVITY
        self.physics.move()
        
        if self.physics.pos.y > screenHeight - self.radius:
            self.physics.pos -= self.physics.velocity
            self.physics.velocity = self.physics.velocity.bounceagainst(Vector2(1,0),self.bounciness)
        if self.physics.pos.x > screenWidth - self.radius or self.physics.pos.x < 0-self.radius:
            self.physics.pos -= self.physics.velocity
            self.physics.velocity = self.physics.velocity.bounceagainst(Vector2(0,1),self.bounciness)
            



FPS = 60
Pysics.GRAVITY /=FPS
clock = pygame.time.Clock()

o = ball("Ball1",(255,255,255),Vector2(100,10),10,6,1)
while True:
    screen.fill((0,0,0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    o.move(True)
    o.draw()
        


    pygame.display.update()
    clock.tick(FPS)
