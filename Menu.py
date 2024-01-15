import pygame
from Screen import Screen
from Settings import Settings
from Settings import *
from Sprites import Sprites
import sys

class Menu():
    
    def __init__(self):
        pygame.init()
        
        self.SCREEN = Screen()
        self.SETTINGS = Settings()
    
    
    def main_menu(self):
        self.SCREEN.display.blit(self.SPRITES.main_menu_pokemon, (0, 0))
        self.SCREEN.display.blit(self.SPRITES.menu_bar_blue_pokemon, (160, 60))
        
        # Render "NEW GAME" text
        # font = pygame.font.Font(self.SETTINGS.font, 36)  # Modified line
        # text_surface = font.render("NEW GAME", True, (255, 255, 255))
        # text_rect = text_surface.get_rect(center=(320, 90))
        
        # Blit the text onto the menu_bar_blue_pokemon surface
        # self.SCREEN.display.blit(text_surface, text_rect)
        
        self.SCREEN.display.blit(self.SPRITES.menu_bar_pokemon, (160, 150))
        self.SCREEN.display.blit(self.SPRITES.menu_bar_pokemon, (160, 240))
        self.SCREEN.display.blit(self.SPRITES.menu_bar_pokemon, (160, 330))
        self.SCREEN.display.blit(self.SPRITES.menu_bar_pokemon, (160, 420))
        self.SCREEN.display.blit(self.SPRITES.menu_bar_pokemon, (160, 510))
        self.SCREEN.update()
        

    def run(self):
        self.SPRITES = Sprites()
        self.main_menu()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return True
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    menu = Menu()
    menu.run()
