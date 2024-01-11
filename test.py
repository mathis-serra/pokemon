import pygame
import time

pygame.init()
pygame.mixer.init()

#Fenetre
largeur_fenetre=800
hauteur_fenetre=600
fenetre=pygame.display.set_mode((largeur_fenetre,hauteur_fenetre))
background=pygame.image.load("Data/Combat/Combat_Sprite/Background/Forest_Background.png")
background=pygame.transform.scale(background,(largeur_fenetre,hauteur_fenetre-200))
text_img=pygame.image.load("Data/Combat/Combat_Sprite/CombatUi/Bottom_message_Box.png")
text_img=pygame.transform.scale(text_img,(largeur_fenetre,hauteur_fenetre-200))
pygame.display.set_caption("Pokemon Fight")


#Son
pygame.mixer.music.load("song/WildFight.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(1) 


#Variables
grey="#8c8c8c"
black="#000000"
green="#a0e8b1"


#Running Game et Event
start_time=time.time()
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    current_time=time.time()
    elapsed_time=current_time - start_time

    if elapsed_time < 3.2:
        if int(elapsed_time/0.1) % 2 == 0:
            fenetre.fill(grey)
        else:
            fenetre.fill(black)
    else:
        fenetre.blit(background, (0, 0))
        fenetre.blit(text_img, (0, 400))
        
    pygame.display.flip()

pygame.quit()
