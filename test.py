import pygame

pygame.init()

#Variables
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
background=pygame.image.load("Data/Combat/Combat_Sprite/Background/Forest_Background.png")
background = pygame.transform.scale(background, (largeur_fenetre, hauteur_fenetre))

pygame.display.set_caption("Pokemon Fight")

#Running Game et Event
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fenetre.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
