import pygame
from tool import Tool
from keylistener import KeyListener

class Entity(pygame.sprite.Sprite):
    def __init__(self, keylistener: KeyListener, map_instance):
        super().__init__()
        self.keylistener = keylistener
        self.map = map_instance
        self.spritesheet = pygame.image.load("Data/Maps/assets/sprite/hero_01_red_m_walk.png")
        self.image = Tool.split_image(self.spritesheet, 0, 0, 24, 32)
        self.position = [0, 0]
        self.rect = pygame.Rect(0, 0, 16, 32)
        self.prev_position = list(self.position)
        self.all_images = self.get_all_images()
        self.index_image = 0
        self.allow_movement_flag = True

    def update(self):
        self.check_move()
        self.handle_collision()
        self.rect.topleft = self.position

    def handle_collision(self):
        tile_width = self.map.tmx_data.tilewidth
        tile_height = self.map.tmx_data.tileheight

        tile_x = int(self.position[0] / tile_width)
        tile_y = int(self.position[1] / tile_height)

        if (tile_x, tile_y) in self.map.collision_data:
            self.position = self.prev_position
            self.stop_movement()
        else:
            self.prev_position = list(self.position)
            self.allow_movement() 

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
        self.position[0] -= 1
        self.image = self.all_images["left"][self.index_image]

    def move_right(self):
        self.position[0] += 1
        self.image = self.all_images["right"][self.index_image]

    def move_up(self):
        self.position[1] -= 1
        self.image = self.all_images["up"][self.index_image]

    def move_down(self):
        self.position[1] += 1
        self.image = self.all_images["down"][self.index_image]

    def allow_movement(self):
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