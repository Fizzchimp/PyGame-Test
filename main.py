import pygame

class World:
    def __init__(self, WIDTH, HEIGHT):

        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.running = True

        self.screenDims = (WIDTH, HEIGHT)
        self.pos = [WIDTH / 2, HEIGHT / 2]
        self.momtm = [1, 0.5]

        # self.box = pygame.Rect(self.x, self.y, 100, 100)
        self.image = pygame.transform.scale(pygame.image.load("krish.png").convert(), (100, 100))
        pygame.display.set_icon(self.image)
        
    
    
    def scrUpdate(self):
        self.screen.fill((100, 100, 100))
        self.pos[0] += self.momtm[0]
        self.pos[1] += self.momtm[1]
        self.screen.blit(self.image, (self.pos[0], self.pos[1]))
        self.collision()

        # self.box.update(self.x, self.y, 100, 100)
        # pygame.draw.rect(self.screen, (100, 0, 75), self.box)

        pygame.display.flip()
       
    def collision(self):
        if self.pos[0] == self.screenDims[0] - 100 or self.pos[0] == 0:
            self.momtm[0] *= -1
        if self.pos[1] == self.screenDims[1] - 100 or self.pos[1] == 0:
            self.momtm[1] *= -1


world = World(750, 500)
while world.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            world.running = False
 
    world.scrUpdate()
    
    pygame.time.wait(10)

pygame.quit()