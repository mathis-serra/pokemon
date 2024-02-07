import pygame 
from Screen import Screen
from Button import Button
from Settings import Settings
from Sprites import Sprites
import pygame.freetype as ft

import json

class Pokedex:
    def __init__(self):
        pygame.init()
        self.SCREEN = Screen()
        self.SETTINGS = Settings()
        self.SPRITES = Sprites()
        
        self.pokedex = {}
        self.type_chart = {}
        self.natures = {}
        self.moves = {}
        self.font = pygame.font.Font('Data/Game/Font/pokemon-emerald.ttf', 30)
        self.pokemon_id = 1
        self.pokemon = self.load_pokedex()
        
        
        
    def load_pokedex(self):
        with open("Data/Pokedex.json", "r", encoding="utf8") as json_file:
            self.pokedex = json.load(json_file)
        for pokemon in self.pokedex:
            if pokemon["id"] == self.pokemon_id:
                return pokemon

    def load_type_chart(self):
        with open("Data/Type_chart.json", "r", encoding="utf8") as json_file:
            self.type_chart = json.load(json_file)

    def load_natures(self):
        with open("Data/Nature.json", "r", encoding="utf8") as json_file:
            self.natures = json.load(json_file)

    def load_moves(self):
        with open("Data/Moves.json", "r", encoding="utf8") as json_file:
            self.moves = json.load(json_file)
             
    
    def set_pokemon_id(self, pokemon_id):
        self.pokemon_id = max(1, min(pokemon_id, 386))
    
    def get_pokemon_id(self):
        return self.pokemon_id
    
    def get_type_chart(self):
        return self.type_chart
    
    def get_natures(self):
        return self.natures
    
    def get_moves(self):
        return self.moves
    
    def get_font(self):
        return self.font
    
    
    
    
    
        

    def show_screen(self):
        self.load_pokedex()
        self.load_type_chart()
        self.load_natures()
        self.load_moves()
        #draw the background
        self.SCREEN.display.blit(self.SPRITES.pokedex_pokemon, (0, 0))
        button_up = Button(530,180, self.SPRITES.pokedex_button_up, 1)
        button_down = Button(530, 480, self.SPRITES.pokedex_button_down, 1)
        self.SCREEN.display.blit(self.SPRITES.get_pokemon_sprite(1), (900, 200))
        #create the buttons
        button_up.draw(self.SCREEN.display)
        button_down.draw(self.SCREEN.display)

        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                self.font = pygame.font.Font('Data/Game/Font/pokemon-emerald.ttf', 50)
                if button_down.draw(self.SCREEN.display):
                    #This line is necessary to avoid the sprite to be drawn above the previous one
                    self.SCREEN.display.fill((0, 0, 0))
                    #This is necessary to rebuild the background
                    self.SCREEN.display.blit(self.SPRITES.pokedex_pokemon, (0, 0))
                    button_up = Button(530,180, self.SPRITES.pokedex_button_up, 1)
                    button_down = Button(530, 480, self.SPRITES.pokedex_button_down, 1)
                    
                    button_up.draw(self.SCREEN.display)
                    button_down.draw(self.SCREEN.display)
                    
                    
                    self.set_pokemon_id(self.get_pokemon_id() + 1)
                    self.pokemon["id"]+=1
                    pokemon_sprite = self.SPRITES.get_pokemon_sprite(self.get_pokemon_id())
                    
                    # Replace the n sprite with the n+1 sprite
                    if self.get_pokemon_id() == self.pokemon_id:
                        self.SCREEN.display.blit(pokemon_sprite, (900, 200))

                        # Display the name of the next Pokemon
                        next_pokemon_id = self.get_pokemon_id() + 1
                        next_pokemon = self.load_pokedex()
                        next_pokemon_name = next_pokemon["name"]["french"]
                        name_text = self.font.render(next_pokemon_name, True, (255, 255, 255))
                        self.SCREEN.display.blit(name_text, (150, 120))
                        
                        # Display the type of the next Pokemon
                        next_pokemon_type = str(next_pokemon["type"])  # Convert to string
                        type_text = self.font.render(next_pokemon_type, True, (255, 255, 255))
                        self.SCREEN.display.blit(type_text, (90, 300))
                        
                        
                        pygame.display.update()
                                            
                    
                    
                    
                    
                if button_up.draw(self.SCREEN.display):
                    #This line is necessary to avoid the sprite to be drawn above the previous one
                    self.SCREEN.display.fill((0, 0, 0))
                    #This is necessary to rebuild the background
                    self.SCREEN.display.blit(self.SPRITES.pokedex_pokemon, (0, 0))
                    button_up = Button(530,180, self.SPRITES.pokedex_button_up, 1)
                    button_down = Button(530, 480, self.SPRITES.pokedex_button_down, 1)
                    
                    button_up.draw(self.SCREEN.display)
                    button_down.draw(self.SCREEN.display)
                    
                    self.set_pokemon_id(self.get_pokemon_id() - 1)
                    self.SPRITES.get_pokemon_sprite(self.get_pokemon_id())
                    
                    # Replace the n sprite with the n+1 sprite
                    if self.get_pokemon_id() == self.pokemon_id:
                        self.SCREEN.display.blit(self.SPRITES.get_pokemon_sprite(self.get_pokemon_id()), (900, 200))
                        
                            # Display the name of the next Pokemon
                        next_pokemon_id = self.get_pokemon_id() - 1
                        next_pokemon = self.load_pokedex()
                        next_pokemon_name = next_pokemon["name"]["french"]
                        name_text = self.font.render(next_pokemon_name, True, (255, 255, 255))
                        self.SCREEN.display.blit(name_text, (150, 120))
                        
                        
                        next_pokemon_type = str(next_pokemon["type"])  # Convert to string
                        type_text = self.font.render(next_pokemon_type, True, (255, 255, 255))
                        self.SCREEN.display.blit(type_text, (90, 300))
                        
                        
                        pygame.display.update()





