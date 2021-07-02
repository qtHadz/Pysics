import Pysics,pygame,sys
from math import *
PhysicsObject = Pysics.PhysicsObject
Vector2 = Pysics.Vector2

screen = pygame.display.set_mode((1000,600))

o = PhysicsObject(Vector2(100,-1000),10,pi*6*6,[6,6],0.1) 
o.setvelocity(Vector2(0,0))


FPS = 60
Pysics.GRAVITY /=FPS

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
    if o.pos.y > 600-6:
        o.pos -= o.velocity
        o.velocity = o.velocity.bounceagainst(Vector2(1,0),o.bouncy)
        o.pos += o.velocity
    pygame.draw.circle(screen,(255,255,255),o.pos.list,6)
    pygame.draw.line(screen,(255,0,0),[0,500],[1000,500],2)
    pygame.display.update()
    clock.tick(FPS)

