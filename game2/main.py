import pygame
from game_core.Game import Game
import traceback


    
def Main():
    try:
        game_instance = Game()
        game_instance.game_lunch()
    except Exception as exc:
        print("Fatal error while starting the client:")
        traceback.print_exc()
        pygame.quit()
    
if __name__ == "__main__":
    Main()





