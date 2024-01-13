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
        self.house_collision_data = None
        self.lamp_collision_data = None
        self.mountain_collision_data = None
        self.tree_collision_data = None 
        self.beach_collision_data = None
        self.fence_collision_data = None 
        self.group = None
        self.player = None

        self.switch_map("pokemonmap")

    def switch_map(self, map_name: str):
        self.tmx_data = pytmx.load_pygame(f"Data/MapsPokemon/{map_name}.tmx")
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 3
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=5)
        collision_layers = ["pokemon statut", "house", "Lampe and Buisson/mini abre, others",
                            "Montagne", "three", "Plage", "Barriere"]

        for collision_name in collision_layers:
            collision_layer = None
            for layer in self.tmx_data.visible_layers:
                if layer.name == collision_name:
                    collision_layer = layer
                    break

            collision_data = set()
            for x, y, gid in collision_layer:
                if gid:
                    collision_data.add((x, y))

            if collision_name == "pokemon statut":
                self.collision_data = collision_data
            elif collision_name == "house":
                self.house_collision_data = collision_data
            elif collision_name == "Lampe and Buisson/mini abre, others":
                self.lamp_collision_data = collision_data
            elif collision_name == "Montagne":
                self.mountain_collision_data = collision_data
            elif collision_name == "three":
                self.tree_collision_data = collision_data
            elif collision_name == "Plage":
                self.beach_collision_data = collision_data
            elif collision_name == "Barriere":
                self.fence_collision_data = collision_data

    def add_player(self, player):
        self.group.add(player)
        self.player = player

    def update(self):
        self.group.update()

        player_rect = self.player.rect
        player_tile_x = int(player_rect.center[0] / self.tmx_data.tilewidth)
        player_tile_y = int(player_rect.center[1] / self.tmx_data.tileheight)

        # Vérifier les collisions avec les différents calques de collision
        if (player_tile_x, player_tile_y) in self.collision_data or \
           (player_tile_x, player_tile_y) in self.house_collision_data or \
           (player_tile_x, player_tile_y) in self.lamp_collision_data or \
           (player_tile_x, player_tile_y) in self.mountain_collision_data or \
           (player_tile_x, player_tile_y) in self.tree_collision_data or \
           (player_tile_x, player_tile_y) in self.beach_collision_data or \
           (player_tile_x, player_tile_y) in self.fence_collision_data:
            # Le joueur est dans une zone de collision, arrêter les mouvements
            self.player.stop_movement()
        else:
            # Le joueur n'est pas dans une zone de collision, autoriser les mouvements
            self.player.allow_all_movement()

        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.get_display())