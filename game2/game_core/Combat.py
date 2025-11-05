import pygame
from game_core.Screen import Screen
from game_core.Sprites import Sprites
from game_core.Settings import Settings
from game_core.Combat_menu import Combat_menu


class Combat:
    def __init__(self, screen: Screen, sprites: Sprites, settings: Settings):
        self.SCREEN = screen
        self.SPRITES = sprites
        self.SETTINGS = settings
        self.MENU = Combat_menu(screen, sprites, settings)
        self.clock = pygame.time.Clock()
        self.framerate = 60
        self.screen_w, self.screen_h = self.SCREEN.display.get_size()

        self.trainer_sprite = self.SPRITES.get_combat_player_sprite(1)
        self.pokemon1_id = 1
        self.trainer_x = 80
        self.trainer_slide_delay = 1000  # ms
        self.trainer_slide_speed = 320   # px per second
        self.combat_start_time = pygame.time.get_ticks()
        self.trainer_left_screen = False

        pokemon_path = self.SPRITES.assets_root / f"Data/Pokemon_Sprites/back/{self.pokemon1_id}.png"
        pokemon_surface = pygame.image.load(str(pokemon_path))
        self.player_sprite = pygame.transform.scale(pokemon_surface, (200, 200))
        self.player_rect = self.player_sprite.get_rect()
   
    def run_combat(self):
        self._reset_state()

        running = True
        while running:
            dt_ms = self.clock.tick(self.framerate)
            
            # Handle input only once per frame
            menu_action = self.MENU.handle_input_menu()
            if menu_action == "QUIT":
                return "QUIT"
            elif menu_action:
                print(f"{menu_action} selected")

            self._update_trainer(dt_ms)
            self._render_frame()

    def _reset_state(self) -> None:
        self.trainer_x = 80
        self.trainer_left_screen = False
        self.combat_start_time = pygame.time.get_ticks()

    def _render_frame(self):
        self._render_terrain()
        self._render_trainer()
        self._render_pokemon()
        self.MENU.display_combat_menu()
        pygame.display.flip()

    def _render_terrain(self):
        # Background should be at the top, not stretched to full screen
        self.SCREEN.display.fill((0, 0, 0))  # Black background
        self.SCREEN.display.blit(self.SPRITES.forest_background, (0, 0))

    def _render_trainer(self):
        if self.trainer_left_screen or not self.trainer_sprite:
            return

        rect = self.trainer_sprite.get_rect()
        # Position trainer on the ground (background is 500px tall)
        background_h = self.SPRITES.forest_background.get_height()
        rect.midbottom = (int(self.trainer_x) + rect.width // 2, background_h)
        self.SCREEN.display.blit(self.trainer_sprite, rect)

    def _update_trainer(self, dt_ms: int) -> None:
        if self.trainer_left_screen or not self.trainer_sprite:
              return

        elapsed = pygame.time.get_ticks() - self.combat_start_time
        if elapsed >= self.trainer_slide_delay:
            delta = self.trainer_slide_speed * (dt_ms / 1000.0)
            self.trainer_x -= delta
            if self.trainer_x + self.trainer_sprite.get_width() <= 0:
                self.trainer_left_screen = True

    def _render_pokemon(self):
        if not self.trainer_left_screen:
            return

        # Position player's pokemon on the left side, on the ground
        background_h = self.SPRITES.forest_background.get_height()
        self.player_rect.midbottom = (180, background_h - 20)
        self.SCREEN.display.blit(self.player_sprite, self.player_rect)