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

        # Draw the bottom message box at the bottom of the screen
        message_rect = self.SPRITES.bottom_message_box.get_rect()
        message_rect.bottomleft = (0, screen_h)
        screen.blit(self.SPRITES.bottom_message_box, message_rect)

        # Draw the choice box on the right side inside the message box
        choice_rect = self.choice_box.get_rect()
        choice_rect.bottomright = (screen_w - 30, screen_h - 30)
        screen.blit(self.choice_box, choice_rect)

        # Calculate grid layout for menu options (2x2 grid)
        columns = 2
        rows = 2
        cell_w = choice_rect.width // columns
        cell_h = choice_rect.height // rows
        
        # Padding from the left edge of each cell for text
        text_offset_x = 60
        text_offset_y = 0

        for index, option in enumerate(self.options):
            row = index // columns
            col = index % columns
            
            # Calculate position for each cell - align text to left within cell
            cell_x = choice_rect.x + col * cell_w + text_offset_x
            cell_y = choice_rect.y + row * cell_h + cell_h // 2 + text_offset_y
            
            # Draw text with larger, darker color
            text_surface = self.font.render(option, True, (50, 50, 50))
            text_rect = text_surface.get_rect(midleft=(cell_x, cell_y))
            screen.blit(text_surface, text_rect)
            
            # Draw arrow for selected option
            if index == self.selected_option:
                arrow_rect = self.choice_arrow.get_rect()
                arrow_rect.midright = (cell_x - 15, cell_y)
                screen.blit(self.choice_arrow, arrow_rect)

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
