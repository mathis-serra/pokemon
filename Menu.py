import pygame
from Screen import Screen
from Settings import Settings
from Settings import *
from Sprites import Sprites
from Button import Button
import duel
import sys
import main as main

class Menu():
    
    def __init__(self):
        pygame.init()
        
        self.SCREEN = Screen()
        self.SETTINGS = Settings()
    
    
    def main_menu(self):
        font = pygame.font.Font("Data/Game/Font/pokemon-emerald.ttf", 36)
        self.SCREEN.display.blit(self.SPRITES.main_menu_pokemon, (0, 0))
        new_game_button = Button(160, 60, self.SPRITES.menu_bar_pokemon, 1) 
        continue_button = Button(160, 150, self.SPRITES.menu_bar_blue_pokemon, 1) 
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
        self.SCREEN.update()
            

    def run(self):
        self.SPRITES = Sprites()
        self.main_menu()
        
        
        
        
        while True:
            
            new_game_button = Button(160, 60, self.SPRITES.menu_bar_pokemon, 1) 
            continue_button = Button(160, 150, self.SPRITES.menu_bar_blue_pokemon, 1) 
            mysyery_gift_button = Button(160, 240, self.SPRITES.menu_bar_pokemon, 1) 
            settings_button = Button(160, 330, self.SPRITES.menu_bar_pokemon, 1)
            pokedex_button = Button(160, 420, self.SPRITES.menu_bar_pokemon, 1) 
            self.SCREEN.display.blit(self.SPRITES.menu_bar_pokemon, (160, 510))
            
            
                
                
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if new_game_button.draw(self.SCREEN.display):
                        self.SCREEN.display.fill((0, 0, 0))
                        pygame.display.update()
                        main()
                        self.main_menu()
                        
                    if continue_button.draw(self.SCREEN.display):
                        self.SCREEN.display.fill((0, 0, 0))
                        pygame.display.update()
                        duel.start()
                        self.main_menu()
                        
                    if mysyery_gift_button.draw(self.SCREEN.display):
                        self.SCREEN.display.fill((0, 0, 0))
                        pygame.display.update()
                        duel.start()
                        self.main_menu()
                        
                    if settings_button.draw(self.SCREEN.display):
                        self.SCREEN.display.fill((0, 0, 0))
                        pygame.display.update()
                        duel.start()
                        self.main_menu()
                        
                    if pokedex_button.draw(self.SCREEN.display):
                        self.SCREEN.display.fill((0, 0, 0))
                        pygame.display.update()
                        duel.start()
                        self.main_menu()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return True
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

