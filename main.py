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
        self.boxes = [Box([100, 100], [700, 254], [-1, 1], "01_krish.png"),
                      Box([100, 100], [200, 300], [-0.5, 0.25], "02_angus.png"),
                      Box([100, 100], [10, 10], [1, -0.5], "03_sopie.png"),
                      Box([100, 100], [500, 100], [-0.25, 0.25], "04_hana.png"), 
                      Box([100, 100], [500, 300], [1, 0.5], "05_ella.png"),
                      Box([100, 100], [300, 300], [-1, -0.25], "06_rob.png"),
                      Box([100, 100], [800, 253], [-1, 0.5], "07_callum.png"),
                      Box([100, 100], [1200, 650], [0.25, 0.5], "08_isla.png"),
                      Box([100, 100], [1100, 400], [-0.5, 0.25], "09_willow.png"),]
        pygame.display.set_icon(pygame.image.load("00_image.png"))
        
    
    
    def scrUpdate(self):
        self.screen.fill((100, 100, 100))
        
            
        for i, box in enumerate(self.boxes):
            self.colDetect(box, i)

        for box in self.boxes:
            box.pos[0] += box.momtm[0]
            box.pos[1] += box.momtm[1]
            self.screen.blit(box.image, (box.pos[0], box.pos[1]))
            box.move(box.pos)
        
        pygame.display.flip()
       
    def colDetect(self, object,  i):
        for j, box2 in enumerate(self.boxes):
            if object.colRect.colliderect(box2.colRect) and i != j:

                if 1 <= object.colRect.right - box2.colRect.left <= 2:
                    object.momtm[0] = -abs(object.momtm[0])

                elif 1 <= box2.colRect.right - object.colRect.left <= 2:
                    object.momtm[0] = abs(object.momtm[0])


                if 1 <= object.colRect.bottom - box2.colRect.top <= 2:
                    object.momtm[1] = -abs(object.momtm[1])

                elif 1 <= box2.colRect.bottom - object.colRect.top <= 2:
                    object.momtm[1] = abs(object.momtm[1])

                    

        if object.pos[0] == self.screenDims[0] - object.dims[0] or object.pos[0] == 0:
            object.momtm[0] *= -1
            

        if object.pos[1] == self.screenDims[1] - object.dims[1] or object.pos[1] == 0:
            object.momtm[1] *= -1
            #self.lineDraw(self.pos)
            
    def lineDraw(self, point):
        self.lines.append([self.point, point])
        self.point = point


world = World(1496, 786)

while world.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            world.running = False
 
    world.scrUpdate()
    pygame.time.wait(4)

pygame.quit()