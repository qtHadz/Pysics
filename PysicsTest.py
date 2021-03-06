import Pysics,pygame,sys,random
from math import *
Projectile = Pysics.Projectile
Vector2 = Pysics.Vector2

screenWidth = 500
screenHeight = 500
screenSize = (screenWidth,screenHeight)
screen = pygame.display.set_mode(screenSize)


class ball():
    def randomBall():
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        rad = random.randint(4,8)
        newB = ball("",color,Vector2(screenWidth/2,screenHeight/2),10,rad,1)
        rvX = random.random()*random.randint(0,100)
        rvY = random.random()*random.randint(0,100)
        if random.randint(1,2) == 1:
            rvX *= -1
        if random.randint(1,2) == 1:
            rvY *= -1
        newB.physics.setvelocity(Vector2(rvX,rvY))
        return newB
    def __init__(self,name,color,startPos,mass,radius,bounciness):
        self.name = name
        self.color = color
        self.startPos = startPos
        self.mass = mass
        self.radius = radius
        self.bounciness = bounciness
        self.physics = Projectile(startPos,mass,pi*radius*radius,[radius,radius],bounciness)
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
    def move(self,doGravity):
        if doGravity:
            self.physics.applygravity()
        self.physics.move()
        
        if self.physics.pos.y > screenHeight - self.radius: #or self.physics.pos.y < 0 +self.radius:
            self.physics.pos -= self.physics.velocity*deltaTime
            self.physics.velocity = self.physics.velocity.bounceagainst(Vector2(1,0),self.bounciness)
            print(time)
        if self.physics.pos.x > screenWidth - self.radius or self.physics.pos.x < 0+self.radius:
            self.physics.pos -= self.physics.velocity*deltaTime
            self.physics.velocity = self.physics.velocity.bounceagainst(Vector2(0,1),self.bounciness)
            


FPS = 60
deltaTime = (1/(FPS))
Pysics.deltaTime = deltaTime
clock = pygame.time.Clock()
time = 1
balls = []
#balls.append(ball("",(255,255,255),Vector2(100,0),10,1,0.5))

for i in range(0,100):
    balls.append(ball.randomBall())

while True:
    screen.fill((0,0,0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            balls.append(ball.randomBall())

    #if time%1 == 0:
     #   balls.append(ball.randomBall())
            

    for b in balls:
        b.move(True)
        b.draw()
        
    pygame.display.update()
    time += 1
    clock.tick(FPS)
