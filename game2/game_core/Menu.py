import pygame
from pathlib import Path
from game_core.Sprites import Sprites
from game_core.Screen import Screen
from game_core.Settings import Settings


class Menu:
    def __init__(self, screen: Screen, sprites: Sprites, settings: Settings):
        self.SCREEN = screen
        self.SPRITES = sprites
        self.SETTINGS = settings
        self.options = ["Start Game", "Options", "Exit"]
        self.selected_option = 0
        
        
    
    
    def display_menu(self):
         
         
        # Sprites declaration 
        # self.SCREEN.display.blit(self.SPRITES.main_menu_pokemon, (0, 0)) 
        # Font declaration
        for index, option in enumerate(self.options):
             color = (255, 255, 255) if index == self.selected_option else (200, 200, 200)
             text_surface = self.SETTINGS.font_pokemon.render(option, True, color)
             text_rect = text_surface.get_rect(center=(self.SCREEN.display.get_width()//2, 360 + index * 50))
             self.SCREEN.display.blit(text_surface, text_rect)
        pygame.display.flip()  
        


    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    print(f"option selected")
                    return self.options[self.selected_option]
        return None
        
        


