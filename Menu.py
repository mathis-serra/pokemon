import pygame
from Screen import Screen
from Settings import Settings
from Settings import *
from Sprites import Sprites
from Button import Button
from Game import Game
from Pokedex import Pokedex
from Start_Combat import Start_Combat

import sys

class Menu():
    
    def __init__(self):
        pygame.init()
        
        self.SCREEN = Screen()
        self.SETTINGS = Settings()
        self.pokedex = Pokedex()  # Create an instance of the Pokedex class
        
    def main_menu(self):
        font = pygame.font.Font("Data/Game/Font/pokemon-emerald.ttf", 36)
        self.SCREEN.display.blit(self.SPRITES.main_menu_pokemon, (0, 0))
        new_game_button = Button(160, 60, self.SPRITES.menu_bar_pokemon, 1) 
        continue_button = Button(160, 150, self.SPRITES.menu_bar_pokemon, 1) 
        mysyery_gift_button = Button(160, 240, self.SPRITES.menu_bar_pokemon, 1) 
        settings_button = Button(160, 330, self.SPRITES.menu_bar_pokemon, 1)
        pokedex_button = Button(160, 420, self.SPRITES.menu_bar_pokemon, 1) 
        self.SCREEN.display.blit(self.SPRITES.menu_bar_pokemon, (160, 510))
        
        new_game_button.draw(self.SCREEN.display)
        continue_button.draw(self.SCREEN.display)
        mysyery_gift_button.draw(self.SCREEN.display)
        settings_button.draw(self.SCREEN.display)
        pokedex_button.draw(self.SCREEN.display)
        
        text_surface = font.render("NEW GAME", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(645, 102))
        text_surface2 = font.render("CONTINUE", True, (255, 255, 255))
        text_rect2 = text_surface2.get_rect(center=(645, 192))
        text_surface3 = font.render("MYSTERY GIFT", True, (255, 255, 255))
        text_rect3 = text_surface3.get_rect(center=(645, 282))
        text_surface4 = font.render("SETTINGS", True, (255, 255, 255))
        text_rect4 = text_surface4.get_rect(center=(645, 372))
        text_surface5 = font.render("POKEDEX", True, (255, 255, 255))
        text_rect5= text_surface4.get_rect(center=(645, 462))
        
        self.SCREEN.display.blit(text_surface, text_rect)
        self.SCREEN.display.blit(text_surface2, text_rect2)
        self.SCREEN.display.blit(text_surface3, text_rect3)
        self.SCREEN.display.blit(text_surface4, text_rect4)
        self.SCREEN.display.blit(text_surface5, text_rect5)
        
        # pygame.display.flip()  # Update the display
        
    def run(self):
        self.SPRITES = Sprites()

        new_game_button = Button(160, 60, self.SPRITES.menu_bar_pokemon, 1)
        continue_button = Button(160, 150, self.SPRITES.menu_bar_blue_pokemon, 1)
        mysyery_gift_button = Button(160, 240, self.SPRITES.menu_bar_pokemon, 1)
        settings_button = Button(160, 330, self.SPRITES.menu_bar_pokemon, 1)
        pokedex_button = Button(160, 420, self.SPRITES.menu_bar_pokemon, 1)
        self.SCREEN.display.blit(self.SPRITES.menu_bar_pokemon, (160, 510))

        state = "menu"
        current_state = self.main_menu()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if new_game_button.draw(self.SCREEN.display):
                        game = Game()
                        game.run()

                    if continue_button.draw(self.SCREEN.display):
                        combat = Start_Combat()
                        combat.run()
                        

                    if mysyery_gift_button.draw(self.SCREEN.display):
                        print("mysyery_gift_button")

                    if settings_button.draw(self.SCREEN.display):
                        pass

                    if pokedex_button.draw(self.SCREEN.display):
                        state = "pokedex"
                        current_menu = self.pokedex  # Use the Pokedex instance
                        
            if state == "pokedex":
                self.pokedex.show_screen()  # Call the show_screen() method of the Pokedex instance
                # pygame.display.update()
            elif state == "menu":
                self.main_menu()
            
            pygame.display.flip()
