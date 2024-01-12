import pygame
from Screen import Screen
from Pyvidplayer import Video 


pygame.init()


screen = Screen()
vid = Video("Data/Intro/Pokemon_intro.mp4")
vid.set_size(screen.get_size())

def intro():
    vid.draw(screen.get_display(), (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            vid.close()
            quit()

intro()




