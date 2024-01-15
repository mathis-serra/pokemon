import pygame
import time
from Dialogue_game import InterfaceFight

pygame.init()
pygame.mixer.init()

# Fenetre
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
background = pygame.image.load("Data/Combat/Combat_Sprite/Background/Forest_Background.png")
background = pygame.transform.scale(background, (largeur_fenetre, hauteur_fenetre - 200))
text_img = pygame.image.load("Data/Combat/Combat_Sprite/CombatUi/Bottom_message_Box.png")
text_img = pygame.transform.scale(text_img, (largeur_fenetre, hauteur_fenetre - 400))
pygame.display.set_caption("Pokemon Fight")

# Son
pygame.mixer.music.load("song/WildFight.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(1)

# Variables
grey = "#8c8c8c"
black = "#000000"
green = "#a0e8b1"
white = "#ffffff"
interface_fight = InterfaceFight(fenetre,pokemon1_id=10, pokemon2_id=222)

# Running Game et Event
start_time = time.time()
running = True
pokemon1_image = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                interface_fight.change_text()
                pokemon1_image = True

    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time < 3.2:
        if int(elapsed_time / 0.1) % 2 == 0:
            fenetre.fill(grey)
        else:
            fenetre.fill(black)
    else:
        fenetre.blit(text_img, (0, 400))
        fenetre.blit(background, (0, 0))
        interface_fight.display_message(interface_fight.dialogue_text)
        pokemon2_image = pygame.image.load(f"Data/Pokemon/Pokemon_Sprites/front/{interface_fight.pokemon2_id}.png")
        pokemon2_image = pygame.transform.scale(pokemon2_image, (200, 200)) 
        fenetre.blit(pokemon2_image, (480, 75))
        if pokemon1_image:
            pokemon1_image = pygame.image.load(f"Data/Pokemon/Pokemon_Sprites/back/{interface_fight.pokemon1_id}.png")
            pokemon1_image = pygame.transform.scale(pokemon1_image, (200, 200))
            fenetre.blit(pokemon1_image, (100, 240))

    pygame.display.flip()

pygame.quit()
