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
        choice_rect.midright = (screen_w - 30, screen_h - 110)
        screen.blit(self.choice_box, choice_rect)

        # Calculate grid layout for menu options (2x2 grid)
        columns = 2
        rows = 2
        cell_w = choice_rect.width // columns
        cell_h = choice_rect.height // rows

        for index, option in enumerate(self.options):
            row = index // columns
            col = index % columns
            
            # Calculate position in the grid
            cell_x = choice_rect.x + col * cell_w + 20
            cell_y = choice_rect.y + row * cell_h + (cell_h - 40) // 2
            
            # Use blue bar for selected option, white bar for others
            if index == self.selected_option:
                bar_sprite = pygame.transform.scale(self.SPRITES.menu_bar_blue_pokemon, (cell_w - 40, 40))
            else:
                bar_sprite = pygame.transform.scale(self.SPRITES.menu_bar_pokemon, (cell_w - 40, 40))
            
            screen.blit(bar_sprite, (cell_x, cell_y))
            
            # Render text centered on the bar
            text_surface = self.font.render(option, True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.center = (cell_x + (cell_w - 40) // 2, cell_y + 20)
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
