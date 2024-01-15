import pygame
from class_combat import Combat

class InterfaceFight(Combat):
    def __init__(self, fenetre, pokemon1_id, pokemon2_id):
        Combat.__init__(self, pokemon1_id, pokemon2_id)
        self.fenetre = fenetre
        self.largeur_fenetre = 800
        self.hauteur_fenetre = 600
        font = "Font/Pokemon_font.ttf"
        self.font = pygame.font.Font(font,30)
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
