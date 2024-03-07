import pygame

class World:
    def __init__(self, WIDTH, HEIGHT):

        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.running = True

        self.screenDims = (WIDTH, HEIGHT)
        self.point = self.pos = [WIDTH / 2, HEIGHT / 2]
        self.momtm = [1, 0.25]
        self.lines = []

        # self.box = pygame.Rect(self.x, self.y, 100, 100)
        self.image = pygame.transform.scale(pygame.image.load("jjj.png").convert(), (100, 100))
        pygame.display.set_icon(self.image)
        
    
    
    def scrUpdate(self):
        self.screen.fill((100, 100, 100))
        self.pos[0] += self.momtm[0]
        self.pos[1] += self.momtm[1]
        for line in self.lines:
            pygame.draw.line(self.screen, (255, 0, 0), line[0], line[1])
        self.screen.blit(self.image, (self.pos[0], self.pos[1]))
        self.collision()

        # self.box.update(self.x, self.y, 100, 100)
        # pygame.draw.rect(self.screen, (100, 0, 75), self.box)

        pygame.display.flip()
       
    def collision(self):
        if self.pos[0] == self.screenDims[0] - 100 or self.pos[0] == 0:
            self.momtm[0] *= -1
            self.lineDraw(self.pos)
        if self.pos[1] == self.screenDims[1] - 100 or self.pos[1] == 0:
            self.momtm[1] *= -1
            self.lineDraw(self.pos)
            
    def lineDraw(self, point):
        self.lines.append([self.point, point])
        self.point = point


world = World(500, 398)
while world.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            world.running = False
 
    world.scrUpdate()
    
    pygame.time.wait(4)

pygame.quit()