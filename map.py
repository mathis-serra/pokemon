import pygame
import pytmx

pygame.init()
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Affichage de la carte Tiled avec Pygame")

# Charger la carte Tiled
carte = pytmx.load_pygame("Data/Maps/map0.tmx")

def afficher_carte():
    for layer in carte.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            # Traitement des tuiles
            for x, y, gid in layer:
                tile = carte.get_tile_image_by_gid(gid)
                if tile:
                    fenetre.blit(tile, (x * carte.tilewidth, y * carte.tileheight))
        elif isinstance(layer, pytmx.TiledObjectGroup):
            # Traitement des objets
            for obj in layer:
                if obj.image:
                    fenetre.blit(obj.image, (obj.x, obj.y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    fenetre.fill((255, 255, 255))
    afficher_carte()
    pygame.display.flip()

pygame.quit()