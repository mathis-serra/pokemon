import pygame
from game_core.Screen import Screen
from game_core.Sprites import Sprites
from game_core.Settings import Settings


class Combat:
    def __init__(self, screen: Screen, sprites: Sprites, settings: Settings):
        self.SCREEN = screen
        self.SPRITES = sprites
        self.SETTINGS = settings
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

    def run_combat(self):
        running = True
        while running:
            dt_ms = self.clock.tick(self.framerate)

            if self._handle_events():
                return "QUIT"

            self._update_trainer(dt_ms)
            self._render_frame()

    def _handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return True
        return False

    def _render_frame(self):
        self._render_terrain()
        self._render_trainer()
        self._render_pokemon1()
        self._render_message_box()
        pygame.display.flip()

    def _render_terrain(self):
        self.SCREEN.display.blit(self.SPRITES.forest_background, (0, 0))

    def _render_message_box(self):
        box_h = self.SPRITES.bottom_message_box.get_height()
        self.SCREEN.display.blit(self.SPRITES.bottom_message_box, (0, self.screen_h - box_h))

    def _render_trainer(self):
            box_h = self.SPRITES.bottom_message_box.get_height()
            rect = self.trainer_sprite.get_rect()
            rect.bottomleft = (int(self.trainer_x), self.screen_h - box_h)
            self.SCREEN.display.blit(self.trainer_sprite, rect)

    def _update_trainer(self, dt_ms: int) -> None:
        if self.trainer_left_screen:
            return

        elapsed = pygame.time.get_ticks() - self.combat_start_time
        if elapsed >= self.trainer_slide_delay:
            delta = self.trainer_slide_speed * (dt_ms / 1000.0)
            self.trainer_x -= delta
            if self.trainer_x + self.trainer_sprite.get_width() <= 0:
                self.trainer_left_screen = True 
            
    def _render_pokemon1(self):
        if not self.trainer_left_screen:
            return

        box_h = self.SPRITES.bottom_message_box.get_height()
        x = 150
        y = self.screen_h - box_h - self.player_sprite.get_height()
        self.SCREEN.display.blit(self.player_sprite, (x, y))
            
        