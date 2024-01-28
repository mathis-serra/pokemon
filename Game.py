import pygame
from Keyhandler import KeyListener
from Map import Map
from Player import Player
from Screen import Screen


class Game:
    def __init__(self):
        self.show_screen: bool = True
        self.screen: Screen = Screen()
        self.map: Map = Map(self.screen)
        self.keylistener: KeyListener = KeyListener()
        self.player: Player = Player(self.keylistener, self.screen, 512, 288)
        self.map.add_player(self.player)

    def run(self):
        while self.show_screen:
            self.handle_input()
            self.map.update()
            self.screen.update()

    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.show_screen= False
            elif event.type == pygame.KEYDOWN:
                self.keylistener.add_key(event.key)
            elif event.type == pygame.KEYUP:
                self.keylistener.remove_key(event.key)