
import pygame as pg
from Colors import Colors




class Sprites():

    def __init__(self):
        super().__init__()
        # Combat Sprites #
        self.forest_background = pg.transform.scale(pg.image.load("Data/Combat/Combat_Sprite/Background/Forest_Background.png"), (1280, 500))
        self.desert_background = pg.transform.scale(pg.image.load("Data/Combat/Combat_Sprite/Background/Desert_Background.png"), (1280, 500))
        self.lake_background = pg.transform.scale(pg.image.load("Data/Combat/Combat_Sprite/Background/Lake_Background.png"), (1280, 500))
        self.sea_background = pg.transform.scale(pg.image.load("Data/Combat/Combat_Sprite/Background/Sea_Background.png"), (1280, 500))
        self.training_background = pg.transform.scale(pg.image.load("Data/Combat/Combat_Sprite/Background/Training_Background.png"), (1280, 500))

        # UI Sprites #
        self.bottom_message_box = pg.transform.scale(pg.image.load("Data/Combat/Combat_Sprite/CombatUI/Bottom_Message_Box.png"), (1280, 220))
        self.choice_box = pg.transform.scale(pg.image.load("Data/Combat/Combat_Sprite/CombatUI/Choice_Box.png"), (600, 220))
        self.choice_arrow = pg.transform.scale(pg.image.load("Data/Combat/Combat_Sprite/CombatUI/Choice_Arrow.png"), (40, 50))
        self.enemy_pokemon_status = pg.transform.scale(pg.image.load("Data/Combat/Combat_Sprite/CombatUI/Enemy_Pokemon_Stats.png"), (500, 150))
        self.player_pokemon_status = pg.transform.scale(pg.image.load("Data/Combat/Combat_Sprite/CombatUI/Player_Pokemon_Stats.png"), (500, 150))
        self.choice_move_box = pg.transform.scale(pg.image.load("Data/Combat/Combat_Sprite/CombatUI/Move_Box.png"), (1280, 220))
        
        
        #Menu Sprites
        self.main_menu_pokemon = pg.transform.scale(pg.image.load("Data/Game/Menu_Sprites/main_menu_pokemon.png"), (1280, 720))
        self.menu_bar_pokemon = pg.transform.scale(pg.image.load("Data/Game/Menu_Sprites/menu_bar_pokemon.png"), (970, 84))
        self.menu_bar_blue_pokemon = pg.transform.scale(pg.image.load("Data/Game/Menu_Sprites/menu_bar_blue_pokemon.png"), (970, 84))

        # Animation Cooldown #
        self.player_intro_speed = 250

    def get_pokemon_sprite(self, pokemon_id, position):
        sprite = pg.image.load(f"Data/Pokemon/Pokemon_Sprites/{position}/{pokemon_id}.png").convert_alpha()
        return pg.transform.scale(sprite, (300, 300))

    def get_combat_player_sprite(self, id):
        sprite = pg.image.load(f"Data/Combat/Combat_Intro_Player/{id}.png")
        return pg.transform.scale(sprite, (sprite.get_width() * 6, sprite.get_height() * 6))
