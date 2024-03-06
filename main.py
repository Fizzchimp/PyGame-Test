import pygame

class World:
    def __init__(self, HEIGHT, WIDTH):
        pygame.init()
        self.screen = pygame.display.set_mode([HEIGHT, WIDTH])
        self.running = True
        self.x = 125
        self.y = 300
        self.box = pygame.Rect(self.x, self.y, 100, 100)
        self.momentumX = self.momentumY = 1
    
    def scrUpdate(self):
        self.x += self.momentumX
        self.y += self.momentumY
        print(self.x)
        self.box.update(self.x, self.y, 100, 100)
        self.screen.fill((100, 100, 100))
        if self.collision():
            pygame.quit()
        pygame.draw.rect(self.screen, (100, 0, 75), self.box)
        pygame.display.flip()
       
    def collision(self):
        if self.x == 400 or self.x == 0:
            self.momentumX *= -1
        if self.y == 400 or self.y == 0:
            self.momentumY *= -1


world = World(500, 500)
while world.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            world.running = False
 
    world.scrUpdate()
    
    pygame.time.wait(10)

pygame.quit()