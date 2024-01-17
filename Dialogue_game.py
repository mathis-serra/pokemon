import pygame
from Class_combat import Combat

class InterfaceFight(Combat):
    def __init__(self, fenetre, pokemon1_id, pokemon2_id):
        Combat.__init__(self, pokemon1_id, pokemon2_id,)
        self.fenetre = fenetre
        self.largeur_fenetre = 800
        self.hauteur_fenetre = 600
        font = "Data/Game/Font/pokemon-emerald.ttf"
        self.font = pygame.font.Font(font,40)
        self.font_name = pygame.font.Font(font,30)
        self.font_health = pygame.font.Font(font,23)
        self.dialogue_text = f"Un {self.pokemon2['name']['french']} sauvage apparaît !"
        self.pokemon1_id = pokemon1_id
        self.pokemon2_id = pokemon2_id
        self.bouton_rect = pygame.Rect(50, 400, 200, 40)
        self.bouton_actif = False
        self.bouton_1 = pygame.Rect(450, 450, 140, 50)
        self.bouton_2 = pygame.Rect(620, 450, 90, 50)
        self.bouton_3 = pygame.Rect(450, 515, 150, 50)
        self.bouton_4 = pygame.Rect(620, 515, 90, 50)

    def display_message(self, message):
        lines = self.wrap_text(message, self.largeur_fenetre - 20)
        y_offset = self.hauteur_fenetre - 120

        for line in lines:
            text = self.font.render(line, True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.largeur_fenetre // 2, y_offset))
            self.fenetre.blit(text, text_rect)
            y_offset += self.font.get_height()

    def wrap_text(self, text, max_width):
        words = text.split(' ')
        lines = []
        current_line = words[0]

        for word in words[1:]:
            test_line = current_line + ' ' + word
            if self.font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        lines.append(current_line)
        return lines

    def change_text(self,new_text):
        self.dialogue_text = new_text

    def pokemon1_interface(self):
        pokemon1_image=pygame.image.load(f"Data/Pokemon/Pokemon_Sprites/back/{self.pokemon1_id}.png")
        pokemon1_image=pygame.transform.scale(pokemon1_image, (200, 200))

        ratio=self.pokemon1['health']/self.pokemon1['base']['HP']
        pygame.draw.rect(self.fenetre, ("#13a11a"), (605,335,165*ratio,20)) 

        pokemon1_stat=pygame.image.load(f"Data/Combat/Combat_Sprite/CombatUI/Player_Pokemon_Stats.png")
        pokemon1_stat=pygame.transform.scale(pokemon1_stat, (340, 90)) 
        self.fenetre.blit(pokemon1_image, (100, 250))
        self.fenetre.blit(pokemon1_stat, (450, 300))

        name1_text = self.font_name.render(f"{self.pokemon1['name']['french']}", True, ("#000000"))
        name1_text_rect = name1_text.get_rect(center=(550, 322))
        self.fenetre.blit(name1_text, name1_text_rect)

        health_text = self.font_health.render(f"{self.pokemon1['health']}/{self.pokemon1['base']['HP']}", True, ("#000000"))
        health_text_rect = health_text.get_rect(center=(720, 367))
        self.fenetre.blit(health_text, health_text_rect)

        lvl1_text = self.font_name.render(f"{self.lvl}", True, ("#000000"))
        lvl1_text_rect = lvl1_text.get_rect(center=(755,322))
        self.fenetre.blit(lvl1_text, lvl1_text_rect)

    def pokemon2_interface(self):
        pokemon2_image=pygame.image.load(f"Data/Pokemon/Pokemon_Sprites/front/{self.pokemon2_id}.png")
        pokemon2_image=pygame.transform.scale(pokemon2_image, (200, 200)) 

        ratio=self.pokemon2['health']/self.pokemon2['base']['HP']
        pygame.draw.rect(self.fenetre, ("#13a11a"), (170,122,165*ratio,20)) 

        pokemon2_stat=pygame.image.load(f"Data/Combat/Combat_Sprite/CombatUI/Enemy_Pokemon_Stats.png")
        pokemon2_stat=pygame.transform.scale(pokemon2_stat, (320, 90)) 
        self.fenetre.blit(pokemon2_image, (480, 75))
        self.fenetre.blit(pokemon2_stat, (50, 75))

        name2_text = self.font_name.render(f"{self.pokemon2['name']['french']}", True, ("#000000"))
        name2_text_rect = name2_text.get_rect(center=(130, 100))
        self.fenetre.blit(name2_text, name2_text_rect)

        lvl2_text = self.font_name.render(f"{self.lvl}", True, ("#000000"))
        lvl2_text_rect = lvl2_text.get_rect(center=(320, 102))
        self.fenetre.blit(lvl2_text, lvl2_text_rect)

    def what_you_will_do(self):

        pygame.draw.rect(self.fenetre, ("#13a11a"), self.bouton_1)
        pygame.draw.rect(self.fenetre, ("#13a11a"), self.bouton_2)
        pygame.draw.rect(self.fenetre, ("#13a11a"), self.bouton_3)
        pygame.draw.rect(self.fenetre, ("#13a11a"), self.bouton_4)

        pokemon_think=pygame.image.load(f"Data/Combat/Combat_Sprite/CombatUI/Choice_box.png")
        pokemon_think=pygame.transform.scale(pokemon_think, (self.largeur_fenetre//2, self.hauteur_fenetre - 400)) 
        self.fenetre.blit(pokemon_think, (self.largeur_fenetre//2, 400))

        pokemon2_think=pygame.image.load(f"Data/Combat/Combat_Sprite/CombatUI/Bottom_Message_Box.png")
        pokemon2_think=pygame.transform.scale(pokemon2_think, (self.largeur_fenetre//2, self.hauteur_fenetre - 400)) 
        self.fenetre.blit(pokemon2_think, (0, 400))

        text_choose=self.font.render(f"Que va faire",True,("#ffffff"))
        choose_rect=text_choose.get_rect(topleft=(30, 445))
        self.fenetre.blit(text_choose, choose_rect)

        text_pokemon=self.font.render(f"{self.pokemon1['name']['french']} ?",True,("#ffffff"))
        pokemon_rect=text_pokemon.get_rect(topleft=(30, 495))
        self.fenetre.blit(text_pokemon, pokemon_rect)

    def fight_dialogue(self):
        if self.pokemon1['health'] > 0:
            self.enlever_pv(self.pokemon1, self.pokemon2)
            ratio = self.pokemon2['health'] / self.pokemon2['base']['HP']
            nouvelle_largeur = 165 * ratio
            pygame.draw.rect(self.fenetre, ("#13a11a"), (170, 122, nouvelle_largeur, 20))
            self.change_text(f"{self.pokemon1['name']['french']} attaque !")

    def fight2_dialogue(self):
        if self.pokemon2['health'] > 0:
            self.enlever_pv(self.pokemon2, self.pokemon1)
            ratio = self.pokemon1['health'] / self.pokemon1['base']['HP']
            nouvelle_largeur = 165 * ratio
            pygame.draw.rect(self.fenetre, ("#13a11a"), (605,335,nouvelle_largeur,20))
            self.change_text(f"{self.pokemon2['name']['french']} attaque !")
    
    
    def finish_fight(self):
        self.pokemon_vainqueur()
        self.change_text(f"{self.vainqueur} est le vainqueur du combat")

    def xp_interface(self):
        self.change_text(f"Vous avez gagné 10 XP !")
        

