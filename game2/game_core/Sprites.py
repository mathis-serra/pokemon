import pygame as pg
from pathlib import Path


class Sprites:
    def __init__(self, assets_root: Path | None = None):
        super().__init__()
        self.assets_root = Path(assets_root) if assets_root else Path(__file__).resolve().parents[2]

        # Combat Sprites #
        self.forest_background = self._load_and_scale("Data/Combat/Combat_Sprite/Background/Forest_Background.png", (1280, 500))
        self.desert_background = self._load_and_scale("Data/Combat/Combat_Sprite/Background/Desert_Background.png", (1280, 500))
        self.lake_background = self._load_and_scale("Data/Combat/Combat_Sprite/Background/Lake_Background.png", (1280, 500))
        self.sea_background = self._load_and_scale("Data/Combat/Combat_Sprite/Background/Sea_Background.png", (1280, 500))
        self.training_background = self._load_and_scale("Data/Combat/Combat_Sprite/Background/Training_Background.png", (1280, 500))

        # UI Sprites #
        self.bottom_message_box = self._load_and_scale("Data/Combat/Combat_Sprite/CombatUI/Bottom_Message_Box.png", (1280, 220))
        self.choice_box = self._load_and_scale("Data/Combat/Combat_Sprite/CombatUI/Choice_Box.png", (600, 220))
        self.choice_arrow = self._load_and_scale("Data/Combat/Combat_Sprite/CombatUI/Choice_Arrow.png", (40, 50))
        self.enemy_pokemon_status = self._load_and_scale("Data/Combat/Combat_Sprite/CombatUI/Enemy_Pokemon_Stats.png", (500, 150))
        self.player_pokemon_status = self._load_and_scale("Data/Combat/Combat_Sprite/CombatUI/Player_Pokemon_Stats.png", (500, 150))
        self.choice_move_box = self._load_and_scale("Data/Combat/Combat_Sprite/CombatUI/Move_Box.png", (1280, 220))

        # Menu Sprites #
        self.main_menu_pokemon = self._load_and_scale("Data/Game/Menu_Sprites/main_menu_pokemon.png", (1280, 720))
        self.menu_bar_pokemon = self._load_and_scale("Data/Game/Menu_Sprites/menu_bar_pokemon.png", (970, 84))
        self.menu_bar_blue_pokemon = self._load_and_scale("Data/Game/Menu_Sprites/menu_bar_blue_pokemon.png", (970, 84))

        # Pokedex Sprites #
        self.pokedex_pokemon = self._load_and_scale("Data/Game/Menu_Sprites/pokedex_background.png", (1280, 720))
        self.pokedex_button_up = self._load_and_scale("Data/Game/Menu_Sprites/button_up.png", (175, 130))
        self.pokedex_button_down = self._load_and_scale("Data/Game/Menu_Sprites/button_down.png", (175, 130))

        # Animation Cooldown #
        self.player_intro_speed = 250

    def _load_image(self, relative_path: str) -> pg.Surface:
        image_path = self.assets_root / relative_path
        if not image_path.exists():
            raise FileNotFoundError(f"Sprite not found: {image_path}")
        image = pg.image.load(str(image_path))

        surface = pg.display.get_surface()
        if surface:
            return image.convert_alpha() if image.get_alpha() else image.convert()

        return image
    
    def _load_and_scale(self, relative_path: str, size: tuple[int, int]) -> pg.Surface:
        return pg.transform.scale(self._load_image(relative_path), size)

    def get_pokemon_sprite(self, pokemon_id):
        sprite = self._load_image(f"Data/Pokemon_Sprites/front/{pokemon_id}.png")
        return pg.transform.scale(sprite, (300, 300))

    def get_combat_player_sprite(self, id):
        sprite = self._load_image(f"Data/Combat/Combat_Intro_Player/{id}.png")
        return pg.transform.scale(sprite, (sprite.get_width() * 6, sprite.get_height() * 6))