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

          

    def pokemon_seen(self):   

        with open("Data/Pokedex_See.json", "r", encoding="utf8") as json_file:

           return json.load(json_file)

            

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

        # Chargement des données initiales

        self.load_pokedex()

        self.load_type_chart()

        self.load_natures()

        self.load_moves()



        # Affichage de l'interface graphique

        self.SCREEN.display.blit(self.SPRITES.pokedex_pokemon, (0, 0))

        button_up = Button(530, 180, self.SPRITES.pokedex_button_up, 1)

        button_down = Button(530, 480, self.SPRITES.pokedex_button_down, 1)

        button_up.draw(self.SCREEN.display)

        button_down.draw(self.SCREEN.display)



        # Afficher les informations de Bulbizarre au démarrage

        self.update_pokemon_info()



        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    self.return_to_menu()

                    



            # Déplacement vers le Pokémon suivant

            if button_down.draw(self.SCREEN.display):

                self.set_pokemon_id(self.get_pokemon_id() + 1)

                self.update_pokemon_info()



            # Déplacement vers le Pokémon précédent

            if button_up.draw(self.SCREEN.display):

                self.set_pokemon_id(self.get_pokemon_id() - 1)

                self.update_pokemon_info()



            pygame.display.update()



    def update_pokemon_info(self):

        # Effacer l'écran

        self.SCREEN.display.fill((0, 0, 0))



        # Réafficher le fond d'écran

        self.SCREEN.display.blit(self.SPRITES.pokedex_pokemon, (0, 0))



        # Chargement des informations sur le Pokémon actuel

        self.pokemon = self.load_pokedex()

        pokemon_id = self.get_pokemon_id()

        pokemon_sprite = self.SPRITES.get_pokemon_sprite(pokemon_id)



        # Affichage du sprite du Pokémon

        self.SCREEN.display.blit(pokemon_sprite, (900, 200))



        # Affichage du nom et du type du Pokémon

        pokemon_name = self.pokemon["name"]["french"]

        pokemon_type = str(self.pokemon["type"])

        self.display_text(pokemon_name, 150, 120)

        self.display_text(pokemon_type, 90, 300)



        # Vérification du statut vu/non vu du Pokémon

        pokemon_seen_data = self.pokemon_seen()

        next_pokemon_seen = pokemon_id in pokemon_seen_data

        seen_text = "[seen]" if next_pokemon_seen else "[not seen]"

        self.display_text(seen_text, 90, 600)







    def display_text(self, text, x, y):

        #dispalay text on the screen on coordinates x and y

        text_render = self.font.render(text, True, (255, 255, 255))

        self.SCREEN.display.blit(text_render, (x, y))

        

        

        # pokemon_seen_data = self.pokemon_seen()

        # print(pokemon_seen_data)





# pok = Pokedex()

# pok.show_screen()

    def return_to_menu(self):

            from Menu import Menu

            menu = Menu()

            menu.run()