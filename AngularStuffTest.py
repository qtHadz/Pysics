from PysicsTest import Projectile
import Pysics, pygame, sys, random
from math import *

Vector2 = Pysics.Vector2
Orbital = Pysics.Orbital

screenWidth = 500
screenHeight = 500
screenSize = (screenWidth,screenHeight)
screen = pygame.display.set_mode(screenSize)


object1 = Orbital(Vector2(250,250),Vector2(0,0),10,100000)
object2 = Projectile(Vector2(249,200),10,6*6*pi,[6,6],1)


print(object1.forceBetween(object2))


FPS = 60
deltaTime = (1/(FPS))
Pysics.deltaTime = deltaTime
clock = pygame.time.Clock()
time = 1
while True:
    screen.fill((0,0,0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.draw.circle(screen,(255,255,255),object1.pos.flist,object1.radius)
    pygame.draw.circle(screen,(255,255,255),object2.pos.flist,object2.radius)

    pygame.display.update()
    time += 1
    clock.tick(FPS)