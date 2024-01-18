import pygame 

class Pokedex:
    def __init__(self):
        self.pokedex = {}
        self.type_chart = {}
        self.natures = {}
        self.moves = {}
        self.font = pygame.freetype.Font('Data/Game/Font/pokemon-emerald.ttf', 30)
        
        
    def load_pokedex(self):
        with open("Data/Pokedex.json", "r", encoding="utf8") as json_file:
            self.pokedex = json.load(json_file)

    def load_type_chart(self):
        with open("Data/Type_chart.json", "r", encoding="utf8") as json_file:
            self.type_chart = json.load(json_file)

    def load_natures(self):
        with open("Data/Nature.json", "r", encoding="utf8") as json_file:
            self.natures = json.load(json_file)

    def load_moves(self):
        with open("Data/Moves.json", "r", encoding="utf8") as json_file:
            self.moves = json.load(json_file)
    
    def get_pokemon(self, pokemon_name):
        return self.pokedex[pokemon_name]
    
    def get_type_chart(self):
        return self.type_chart
    
    def get_natures(self):
        return self.natures
    
    def get_moves(self):
        return self.moves
    
    def get_font(self):
        return self.font
    
    def get_pokemon_image(self, pokemon_name):
        return pygame.image.load(f"Data/Game/Sprites/Pokemon/{pokemon_name}.png")
    
    def get_pokemon_back_image(self, pokemon_name):
        return pygame.image.load(f"Data/Game/Sprites/Pokemon/{pokemon_name}_back.png")
    
    def get_pokemon_icon(self, pokemon_name):
        return pygame.image.load(f"Data/Game/Sprites/Pokemon/{pokemon_name}_icon.png")
    
    def get_pokemon_shiny_image(self, pokemon_name):
        return pygame.image.load(f"Data/Game/Sprites/Pokemon/{pokemon_name}_shiny.png")
    
    def get_pokemon_shiny_back_image(self, pokemon_name):
        return pygame.image.load(f"Data/Game/Sprites/Pokemon/{pokemon_name}_shiny_back.png")
    
    def get_pokemon_shiny_icon(self, pokemon_name):
        return pygame.image.load(f"Data/Game/Sprites/Pokemon/{pokemon_name}_shiny_icon.png")
    
    
    