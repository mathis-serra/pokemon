import pygame
from tool import Tool
from keylistener import KeyListener

class Entity(pygame.sprite.Sprite):
    def __init__(self, keylistener, collision_data):
        super().__init__()
        self.keylistener = keylistener
        self.collision_data = collision_data
        self.spritesheet = pygame.image.load("Data/Maps/assets/sprite/hero_01_red_m_walk.png")
        self.image = Tool.split_image(self.spritesheet, 0, 0, 24, 32)
        self.position = [0, 0]
        self.rect = pygame.Rect(0, 0, 16, 32)
        self.all_images = self.get_all_images()
        self.index_image = 0
        self.can_move = True

    def update(self):
        if self.can_move:
            self.check_move()
            self.handle_collision()
        self.rect.topleft = self.position

    def check_move(self):
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

    def get_all_images(self):
        all_images = {
            "down": [],
            "left": [],
            "right": [],
            "up": []
        }
        for i in range(4):
            for j, key in enumerate(all_images.keys()):
                all_images[key].append(Tool.split_image(self.spritesheet, i * 24, j*32, 24, 32))
        return all_images

    def stop_movement(self):
        self.can_move = False

    def allow_movement(self):
        self.can_move = True

    def handle_collision(self):
        player_tile_x = int(self.position[0] / 24)  # Adapté à la taille de votre tuile
        player_tile_y = int(self.position[1] / 32)  # Adapté à la taille de votre tuile

        # Obtenir les dimensions du calque
        map_width = self.collision_data.width
        map_height = self.collision_data.height

        # Vérifier les collisions
        if (player_tile_x, player_tile_y) in self.collision_data:
            # Le joueur est dans une zone de collision, ajuster la position pour éviter la collision
            self.position[0] = max(0, min((map_width - 1) * 24, self.position[0]))  # Adapté à la taille de votre tuile
            self.position[1] = max(0, min((map_height - 1) * 32, self.position[1]))  # Adapté à la taille de votre tuile
