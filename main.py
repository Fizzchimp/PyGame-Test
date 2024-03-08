import pygame
from objects import *

class World:
    def __init__(self, WIDTH, HEIGHT):

        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.running = True

        self.screenDims = (WIDTH, HEIGHT)
        self.point = self.pos = [WIDTH / 2, HEIGHT / 2]
        self.lines = []
        self.boxes = [Box([200, 200], [400, 400], [-1, 0.25], "03_sopie.png"), Box([200, 200], [100, 100], [1, 0.25], "01_krish.png")]
        pygame.display.set_icon(self.boxes[0].image)
        
    
    
    def scrUpdate(self):
        self.screen.fill((100, 100, 100))
        #for line in self.lines:
        #    pygame.draw.line(self.screen, (255, 0, 0), line[0], line[1])
            
        for box in self.boxes:
            box.pos[0] += box.momtm[0]
            box.pos[1] += box.momtm[1]
            self.screen.blit(box.image, (box.pos[0], box.pos[1]))
            self.collision(box)
        
        pygame.display.flip()
       
    def collision(self, object):
        if object.pos[0] == self.screenDims[0] - object.dims[0] or object.pos[0] == 0:
            object.momtm[0] *= -1
            #for box2 in self.boxes():
             #   if object.pos == 
        if object.pos[1] == self.screenDims[1] - object.dims[1] or object.pos[1] == 0:
            object.momtm[1] *= -1
            #self.lineDraw(self.pos)
            
    def lineDraw(self, point):
        self.lines.append([self.point, point])
        self.point = point


world = World(1500, 800)
while world.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            world.running = False
 
    world.scrUpdate()
    
    pygame.time.wait(4)

pygame.quit()