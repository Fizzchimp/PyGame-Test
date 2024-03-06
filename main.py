import pygame

class World:
    def __init__(self, HEIGHT, WIDTH):
        pygame.init()
        self.screen = pygame.display.set_mode([HEIGHT, WIDTH])
        self.running = True
        self.x = self.y = 125
        self.box = pygame.Rect(self.x, self.y, 100, 100)
        
    
    def scrUpdate(self):
        self.x += 1
        self.y += 1
        self.box.update(self.x, self.y, 100, 100)
        self.screen.fill((100, 100, 100))
        pygame.draw.rect(self.screen, (125, 0, 75), self.box)
        pygame.display.flip()


world = World(500, 500)
while world.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            world.running = False
 
    world.scrUpdate()
    
    pygame.time.wait(10)

pygame.quit()