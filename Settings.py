import pygame
import json
import random
import pygame as pg
import pygame.freetype as ft
import sys

class Settings:
    def __init__(self):
        self.font = ft.Font('Data/Game/Font/pokemon-emerald.ttf', 30)
        
         # path to pokemon data #
        with open("Data/Pokemon/Pokedex.json", "r", encoding="utf8") as json_file:
            self.pokedex = json.load(json_file)

        # path to type chart #
        with open("Data/Pokemon/Type_chart.json", "r", encoding="utf8") as json_file:
            self.type_chart = json.load(json_file)

        # path to natures #
        with open("Data/Pokemon/Nature.json", "r", encoding="utf8") as json_file:
            self.natures = json.load(json_file)

        # path to moves #
        with open("Data/Pokemon/Moves.json", "r", encoding="utf8") as json_file:
            self.moves = json.load(json_file)
    
    def get_font(self):
        return self.font    
            
        