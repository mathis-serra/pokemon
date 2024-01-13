import pygame
import pytmx
import pyscroll
from screen import Screen

class Map:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.tmx_data = None
        self.map_layer = None
        self.collision_data = None
        self.group = None
        self.player = None

        self.switch_map("pokemonmap")

    def switch_map(self, map_name: str):
        self.tmx_data = pytmx.load_pygame(f"Data/MapsPokemon/{map_name}.tmx")
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 3
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=5)

        collision_layer = None
        for layer in self.tmx_data.visible_layers:
            if layer.name == "pokemon statut":
                collision_layer = layer
                break

        collision_data = set()
        for x, y, gid in collision_layer:
            if gid:
                collision_data.add((x, y))

        self.collision_data = collision_data

    def add_player(self, player):
        self.group.add(player)
        self.player = player

    def update(self):
        self.group.update()

        player_rect = self.player.rect
        player_tile_x = int(player_rect.topleft[0] / self.tmx_data.tilewidth)
        player_tile_y = int(player_rect.topleft[1] / self.tmx_data.tileheight)

        if (player_tile_x, player_tile_y) in self.collision_data:
            # Le joueur est dans une zone de collision, arrêter les mouvements
            self.player.stop_movement()
        else:
            # Le joueur n'est pas dans une zone de collision, autoriser les mouvements
            self.player.allow_movement()

        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.get_display())