import Pysics,pygame
from math import *
PhysicsObject = Pysics.PhysicsObject
Vector2 = Pysics.Vector2

screen = pygame.display.set_mode((1000,600))

o = PhysicsObject(Vector2(100,100),10,pi*6*6,[6,6]) 
o.setvelocity(Vector2(3,-4))


FPS = 30

Pysics.GRAVITY /=FPS
#GRAVITY = GRAVITY/(FPS*100)
clock = pygame.time.Clock()
while True:
    screen.fill((0,0,0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            
    o.applygravity()
    o.move()
    pygame.draw.circle(screen,(255,255,255),o.pos.list,6)
    pygame.display.update()
    clock.tick(FPS)

