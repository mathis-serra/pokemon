import pygame
from game_core.Sprites import Sprites
from game_core.Screen import Screen
from game_core.Settings import Settings
from pathlib import Path



class Combat_menu:
    
    def __init__(self, screen: Screen, sprites: Sprites, settings: Settings):
        self.SCREEN = screen
        self.SPRITES = sprites
        self.SETTINGS = settings
        self.options = ["Attacks", "Bag", "Pokemon", "Run"]
        self.selected_option = 0
        self.box_h = self.SPRITES.bottom_message_box.get_height()
        self.box_w = self.SPRITES.bottom_message_box.get_width()
        self.choice_box = self.SPRITES.choice_box
        self.choice_arrow = self.SPRITES.choice_arrow
        self.font = self.SETTINGS.font_pokemon
    
    def display_combat_menu(self):
        screen = self.SCREEN.display
        screen_w, screen_h = screen.get_size()

        message_rect = self.SPRITES.bottom_message_box.get_rect()
        message_rect.bottomleft = (0, screen_h)
        screen.blit(self.SPRITES.bottom_message_box, message_rect)

        padding = 24
        choice_rect = self.choice_box.get_rect()
        choice_rect.bottomright = (screen_w - padding, screen_h - padding)
        screen.blit(self.choice_box, choice_rect)

        columns = 2
        rows = 2
        cell_w = choice_rect.width // columns
        cell_h = choice_rect.height // rows

        for index, option in enumerate(self.options):
            row = index // columns
            col = index % columns
            cell_x = choice_rect.x + col * cell_w
            cell_y = choice_rect.y + row * cell_h

            if index == self.selected_option:
                highlight_rect = pygame.Rect(cell_x + 12, cell_y + 12, cell_w - 24, cell_h - 24)
                pygame.draw.rect(screen, (255, 255, 255), highlight_rect, border_radius=12)
                pygame.draw.rect(screen, (53, 110, 173), highlight_rect, width=3, border_radius=12)

                arrow_rect = self.choice_arrow.get_rect()
                arrow_rect.midleft = (highlight_rect.left - 18, highlight_rect.centery)
                screen.blit(self.choice_arrow, arrow_rect)

                text_color = (38, 76, 141)
            else:
                text_color = (255, 255, 255)

            text_surface = self.font.render(option, True, text_color)
            text_rect = text_surface.get_rect(center=(cell_x + cell_w // 2, cell_y + cell_h // 2))
            screen.blit(text_surface, text_rect)

    def handle_input_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "QUIT"
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key in (pygame.K_UP, pygame.K_w):
                    self.selected_option = (self.selected_option - 2) % len(self.options)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    self.selected_option = (self.selected_option + 2) % len(self.options)
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    return self.options[self.selected_option]
        return None
