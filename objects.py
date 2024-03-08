import pygame

class Box():
    def __init__(self, dims, pos, momtm, image):
        self.dims = dims
        self.image = pygame.transform.scale(pygame.image.load(image).convert(), dims)
        self.pos = pos
        self.momtm = momtm
        self.colRect = pygame.Rect(pos, dims)