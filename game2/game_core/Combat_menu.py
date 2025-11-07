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

        # Draw the player pokemon status panel on the left inside the message box
        try:
            status_surf = self.SPRITES.player_pokemon_status
            status_rect = status_surf.get_rect()
            # Align bottom-left inside the message box with a small margin
            status_rect.bottomleft = (760, 500 )
            screen.blit(status_surf, status_rect)

            # Fetch stats provided by Combat (if any)
            ps = getattr(self, "player_stats", None)
            name = ""
            level = None
            cur_hp = None
            max_hp = None
            exp = None
            exp_to_next = None
            if ps:
                name = ps.get("name", f"#{ps.get('id', '?')}")
                level = ps.get("level", None)
                cur_hp = ps.get("current_hp", None)
                max_hp = ps.get("max_hp", None)
                exp = ps.get("exp", 0)
                exp_to_next = ps.get("exp_to_next", 100)

            # Ensure we have a usable font
            font = self.font if self.font else pygame.font.SysFont(None, 20)

            # Draw name and level
            name_surface = font.render(str(name), True, (10, 10, 10))
            name_rect = name_surface.get_rect(topleft=(status_rect.x + 12, status_rect.y + 10))
            screen.blit(name_surface, name_rect)

            if level is not None:
                level_surface = font.render(f"Lv {level}", True, (10, 10, 10))
                level_rect = level_surface.get_rect(topright=(status_rect.right - 12, status_rect.y + 10))
                screen.blit(level_surface, level_rect)

            # Draw HP text and bar
            hp_text = ""
            if cur_hp is not None and max_hp is not None:
                hp_text = f"{int(cur_hp)}/{int(max_hp)}"
            elif max_hp is not None:
                hp_text = f"{int(max_hp)}/{int(max_hp)}"

            hp_surface = font.render(hp_text, True, (10, 10, 10))
            hp_surface_rect = hp_surface.get_rect(topright=(status_rect.right - 12, status_rect.y + 46))
            screen.blit(hp_surface, hp_surface_rect)

            # HP bar background
            bar_x = status_rect.x + 12
            bar_y = status_rect.y + 44
            bar_w = status_rect.width - 44 - 100 if status_rect.width - 44 - 100 > 40 else status_rect.width - 40
            bar_h = 14
            hp_bg_rect = pygame.Rect(bar_x, bar_y, bar_w, bar_h)
            pygame.draw.rect(screen, (80, 80, 80), hp_bg_rect)

            # HP bar fill
            if cur_hp is None or max_hp is None or max_hp <= 0:
                hp_ratio = 1.0
            else:
                hp_ratio = max(0.0, min(1.0, float(cur_hp) / float(max_hp)))

            hp_fill_rect = pygame.Rect(bar_x, bar_y, int(bar_w * hp_ratio), bar_h)
            # green -> red gradient based on hp ratio (simple threshold)
            hp_color = (50, 200, 50) if hp_ratio > 0.25 else (220, 60, 60)
            pygame.draw.rect(screen, hp_color, hp_fill_rect)
            pygame.draw.rect(screen, (0, 0, 0), hp_bg_rect, 1)

            # EXP bar below HP
            exp_x = status_rect.x + 12
            exp_y = status_rect.y + 66
            exp_w = status_rect.width - 24
            exp_h = 8
            exp_bg = pygame.Rect(exp_x, exp_y, exp_w, exp_h)
            pygame.draw.rect(screen, (60, 60, 80), exp_bg)
            if exp is None or exp_to_next is None or exp_to_next <= 0:
                exp_ratio = 0.0
            else:
                exp_ratio = max(0.0, min(1.0, float(exp) / float(exp_to_next)))
            exp_fill = pygame.Rect(exp_x, exp_y, int(exp_w * exp_ratio), exp_h)
            pygame.draw.rect(screen, (50, 110, 220), exp_fill)
            pygame.draw.rect(screen, (0, 0, 0), exp_bg, 1)
        except Exception:
            # If anything about the status panel fails, continue without crashing
            pass

        # Draw the choice box on the right side inside the message box
        choice_rect = self.choice_box.get_rect()
        choice_rect.bottomright = (screen_w , screen_h)
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
