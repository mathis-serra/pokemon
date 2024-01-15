import pygame
from class_combat import Combat

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

    def change_text(self):
        self.dialogue_text = f"Je t'envoie {self.pokemon1['name']['french']} !"

    def pokemon1_interface(self):
        pokemon1_image=pygame.image.load(f"Data/Pokemon/Pokemon_Sprites/back/{self.pokemon1_id}.png")
        pokemon1_image=pygame.transform.scale(pokemon1_image, (200, 200))

        health1_bar_width = int(165 * (self.pokemon1['health'] / self.pokemon1['base']['HP']))
        health1_bar_rect = pygame.Rect(605, 335, health1_bar_width, 20)
        pygame.draw.rect(self.fenetre, ("#13a11a"), health1_bar_rect) 

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
        
        health2_bar_width = int(165 * (self.pokemon1['health'] / self.pokemon1['base']['HP']))
        health2_bar_rect = pygame.Rect(170, 122, health2_bar_width, 20)
        pygame.draw.rect(self.fenetre, ("#13a11a"), health2_bar_rect) 

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

    