import pygame

class InterfaceFight:
    def __init__(self,x,y,width,height,color):
        self.rect=pygame.Rect(x,y,width,height)
        self.color=color

    def draw(self,surface):
        pygame.draw.rect(surface,self.color,self.rect)

    def display_rect(self,surface):
        self.draw(surface)

    @classmethod
    def deroulement(cls):
        return cls(0, 400, 800, 200, ("#a0e8b1"))
