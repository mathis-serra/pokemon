import pygame


class Screen:
    
    
    
    
    def __init__(self):
        pygame.init()

        print("the Screen is opening")
        self.display:pygame.display= pygame.display.set_mode((1280,720))


        pygame.display.set_caption('Pokemon RED')