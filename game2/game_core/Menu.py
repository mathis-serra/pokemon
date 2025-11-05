import pygame
from pathlib import Path
from game_core.Sprites import Sprites
from game_core.Screen import Screen
from game_core.Settings import Settings


class Menu:
    def __init__(self, screen: Screen, sprites: Sprites, settings: Settings):
        self.SCREEN = screen
        self.SPRITES = sprites
        self.SETTINGS = settings
        self.options = ["Start Game", "Options", "Exit"]
        self.selected_option = 0
        
        
    
    
    def display_menu(self):
        screen = self.SCREEN.display
        screen_w, screen_h = screen.get_size()
        
        # Draw the main menu background (already has menu bars drawn on it)
        screen.blit(self.SPRITES.main_menu_pokemon, (0, 0))
        
        # Use actual sprite dimensions (970x84) for menu bars
        bar_width = 970
        bar_height = 84
        
        # Position to match the bars in the background image
        # First bar starts at approximately y=60 based on the image
        menu_start_y = 60
        menu_spacing = 88  # Spacing between bars in the background (84px + small gap)
        x_pos = 155  # Left alignment to match background bars
        
        for index, option in enumerate(self.options):
            # Calculate position to overlay on background bars
            y_pos = menu_start_y + (index * menu_spacing)
            
            # Only draw colored bar for selected option
            if index == self.selected_option:
                bar_sprite = self.SPRITES.menu_bar_blue_pokemon
                screen.blit(bar_sprite, (x_pos, y_pos))
            
            # Render text centered on the bar
            text_surface = self.SETTINGS.font_pokemon.render(option, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(x_pos + bar_width // 2, y_pos + bar_height // 2))
            screen.blit(text_surface, text_rect)
        
        pygame.display.flip()  
        


    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    print(f"option selected")
                    return self.options[self.selected_option]
        return None
        
        


