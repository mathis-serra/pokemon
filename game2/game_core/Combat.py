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

        # Build a minimal player stats dict (level, current/max hp, exp)
        # Try to read base HP and name from Pokedex.json; otherwise fallback to defaults
        self.player_stats = {
            "id": self.pokemon1_id,
            "name": f"#{self.pokemon1_id}",
            "level": 5,
            "current_hp": None,
            "max_hp": None,
            "exp": 0,
            "exp_to_next": 100,
        }
        try:
            import json
            pokedex_path = self.SPRITES.assets_root / "Data/Pokedex.json"
            if pokedex_path.exists():
                with open(pokedex_path, "r", encoding="utf-8") as f:
                    pokedex = json.load(f)
                # find entry by numeric 'num' field
                for key, val in pokedex.items():
                    try:
                        if int(val.get("num", -1)) == int(self.pokemon1_id):
                            self.player_stats["name"] = val.get("name", key)
                            base_hp = val.get("baseStats", {}).get("hp")
                            if base_hp:
                                # naive max hp: use base hp as max (simple placeholder)
                                self.player_stats["max_hp"] = int(base_hp)
                                self.player_stats["current_hp"] = int(base_hp)
                            break
                    except Exception:
                        continue
        except Exception:
            # if anything fails, keep placeholders
            if self.player_stats["max_hp"] is None:
                self.player_stats["max_hp"] = 10
                self.player_stats["current_hp"] = 10
   
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
        # provide current player stats to the menu UI (safe copy)
        try:
            self.MENU.player_stats = dict(self.player_stats)
        except Exception:
            self.MENU.player_stats = None
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


        self.player_rect.midbottom = (260, 550)
        self.SCREEN.display.blit(self.player_sprite, self.player_rect)