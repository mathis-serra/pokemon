import pygame
from tool import Tool
from keylistener import KeyListener

class Entity(pygame.sprite.Sprite):
    def __init__(self, keylistener: KeyListener, map_instance):
        super().__init__()
        self.keylistener = keylistener
        self.map = map_instance
        self.spritesheet = pygame.image.load("Data/Maps/assets/sprite/hero_01_red_m_walk.png")
        self.position = [50, 0]
        self.rect = pygame.Rect(0, 0, 16, 32)
        self.all_images = self.get_all_images()
        self.index_image = 0
        self.allow_movement_flag = True
        self.image = self.all_images["down"][self.index_image]

    def update(self):
        self.check_move()
        self.handle_collision()
        self.rect.topleft = self.position

    def handle_collision(self):
        tile_width = self.map.tmx_data.tilewidth
        tile_height = self.map.tmx_data.tileheight

        tile_x_left = int(self.position[0] / tile_width)
        tile_x_right = int((self.position[0] + self.rect.width) / tile_width)
        tile_y_top = int(self.position[1] / tile_height)
        tile_y_bottom = int((self.position[1] + self.rect.height) / tile_height)

        # Vérifier la collision avec le calque "pokemon statut" ou "house"
        if (
            (tile_x_left, tile_y_top) in self.map.collision_data or
            (tile_x_right, tile_y_top) in self.map.collision_data or
            (tile_x_left, tile_y_bottom) in self.map.collision_data or
            (tile_x_right, tile_y_bottom) in self.map.collision_data or
            (tile_x_left, tile_y_top) in self.map.house_collision_data or
            (tile_x_right, tile_y_top) in self.map.house_collision_data or
            (tile_x_left, tile_y_bottom) in self.map.house_collision_data or
            (tile_x_right, tile_y_bottom) in self.map.house_collision_data
        ):
            # Si collision avec "pokemon statut" ou "house", ne rien faire (laisser le personnage dans sa position actuelle)
            pass
        else:
            # Si pas de collision, permettre le mouvement
            self.allow_movement_flag = True

    def check_move(self):
        if self.allow_movement_flag:
            if self.keylistener.key_pressed(pygame.K_q):
                self.move_left()
            elif self.keylistener.key_pressed(pygame.K_d):
                self.move_right()
            elif self.keylistener.key_pressed(pygame.K_z):
                self.move_up()
            elif self.keylistener.key_pressed(pygame.K_s):
                self.move_down()

    def move_left(self):
        if self.allow_movement_flag:
            self.position[0] -= 1
            self.image = self.all_images["left"][self.index_image]

    def move_right(self):
        if self.allow_movement_flag:
            self.position[0] += 1
            self.image = self.all_images["right"][self.index_image]

    def move_up(self):
        if self.allow_movement_flag:
            self.position[1] -= 1
            self.image = self.all_images["up"][self.index_image]

    def move_down(self):
        if self.allow_movement_flag:
            self.position[1] += 1
            self.image = self.all_images["down"][self.index_image]

    def allow_all_movement(self):
        self.allow_movement_flag = True

    def stop_movement(self):
        self.allow_movement_flag = False

    def get_all_images(self):
        all_images = {
            "down": [],
            "left": [],
            "right": [],
            "up": []
        }
        for i in range(4):
            for j, key in enumerate(all_images.keys()):
                all_images[key].append(Tool.split_image(self.spritesheet, i * 24, j * 32, 24, 32))
        return all_images
