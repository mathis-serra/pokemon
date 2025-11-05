import pygame
from game_core.Screen import Screen
from game_core.Menu import Menu
from game_core.Combat import Combat
from game_core.Sprites import Sprites
from game_core.Settings import Settings



class Game:
    def __init__(self):
        pygame.init()
        self.screen = Screen()
        self.settings = Settings()
        self.sprites = Sprites()

        self.menu = Menu(self.screen, self.sprites, self.settings)
        self.combat = Combat(self.screen, self.sprites, self.settings)
        self.clock = pygame.time.Clock()
        self.framerate = 60

    def game_lunch(self):
        print("game launching")
        running = True
        while running:
            action = self.menu.handle_input()
            if action in ("QUIT", "Exit"):
                running = False
                break
            if action == "Start Game":
                combat_result = self.combat.run_combat()
                if combat_result == "QUIT":
                    running = False
                    break
                continue

            self.menu.display_menu()
            self.clock.tick(self.framerate)

        pygame.quit()


