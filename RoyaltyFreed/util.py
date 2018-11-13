import pygame
from settings import *

class Util():
    def __init__(self):
        pass

    def returnImage(self,path):
        image = pygame.image.load(path)
        return image

    def blitImage(self, img, x,y,w,h):
        image = pygame.Surface((w,h))
        image.blit(img,(-x,-y))
        image = pygame.transform.scale2x(image)
        return image
