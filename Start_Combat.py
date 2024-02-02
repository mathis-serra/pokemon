import pygame
import time
from Dialogue_game import InterfaceFight
from class_combat import Combat

class PokemonGameCombat():
    def __init__(self):

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


        # Variables
        grey = "#8c8c8c"
        black = "#000000"
        green = "#a0e8b1"
        white = "#ffffff"
        interface_fight = InterfaceFight(fenetre)
        count=0

        # Running Game et Event
        start_time = time.time()
        show_screen = True
        pokemon1_image = None
        what_will= None
        fight = False
        start = True
        finish=False
        leave=False
        fight2=False
        player1=False
        player2=False
        finish_1=False
        stop=False
        
        while show_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    show_screen = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and fight == False and start == True:
                        interface_fight.change_text(f"Je t'envoie {interface_fight.pokemon1['name']['french']} !")
                        pokemon1_image = True
                        count+=1
                        if count==2:
                            start=False
                            what_will=True
                    elif event.type == pygame.KEYDOWN and stop == True:
                        show_screen=False
                    elif event.type == pygame.KEYDOWN and fight==True and finish ==False and finish_1==False:
                            if event.key == pygame.K_RETURN:
                                interface_fight.fight2_dialogue()
                                fight = False
                                player2=True
                                player1=False
                                if interface_fight.combat_fini() and player2==True:
                                    interface_fight.finish_fight()
                                    finish = True
                    elif event.type == pygame.KEYDOWN and finish_1==True:
                        interface_fight.xp_interface()
                        stop = True

                    elif event.type == pygame.KEYDOWN and fight==False and start == False and finish == True:
                   
                        show_screen = False
                    elif event.type == pygame.KEYDOWN and fight==False and start == False:
                        what_will=True
            
                if event.type == pygame.MOUSEBUTTONDOWN and fight == False:
                    mouse_x, mouse_y = event.pos
                    if interface_fight.bouton_1.collidepoint(mouse_x, mouse_y):
                        fight = True
                        what_will=False
                        player1=True
                        player2=False
                        interface_fight.fight_dialogue()
                        if interface_fight.combat_fini() and player1==True:
                                interface_fight.finish_fight()
                                finish=True
                                finish_1=True
                    if interface_fight.bouton_2.collidepoint(mouse_x, mouse_y):
                        pass
                    if interface_fight.bouton_3.collidepoint(mouse_x, mouse_y):
                        pass
                    if interface_fight.bouton_4.collidepoint(mouse_x, mouse_y):
                        show_screen = False
                        
            current_time = time.time()
            elapsed_time = current_time - start_time

            if elapsed_time < 3.2:
                if int(elapsed_time / 0.1) % 2 == 0:
                    fenetre.fill(grey)
                else:
                    fenetre.fill(black)
            else:
                fenetre.blit(background, (0, 0))
                if pokemon1_image:
                    interface_fight.pokemon1_interface()
                fenetre.blit(text_img, (0, 400))
                interface_fight.display_message(interface_fight.dialogue_text)
                interface_fight.pokemon2_interface()
                if what_will:
                    interface_fight.what_you_will_do()


            pygame.display.flip()

        pygame.quit()