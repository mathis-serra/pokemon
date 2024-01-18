import pygame

class Screen:
    def __init__(self):
        # Initialisation de la fenêtre
        self.display: pygame.display = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Pokémon")

        # Initialisation de l'horloge pour le framerate
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.framerate: int = 144
        self.deltatime: float = 0.0

        # Initialisation de Pygame mixer et chargement de la musique
        pygame.mixer.init()
        pygame.mixer.music.load("song/PokemonAudio.mp3")  # Remplacez par le chemin réel de votre fichier musical
        pygame.mixer.music.play(-1)  # -1 signifie la lecture en boucle indéfiniment

    def update(self) -> None:
        # Mise à jour de l'affichage
        pygame.display.flip()
        pygame.display.update()

        # Contrôle du framerate
        self.clock.tick(self.framerate)
        self.display.fill((0, 0, 0))
        self.deltatime = self.clock.get_time()

    def get_delta_time(self) -> float:
        return self.deltatime

    def get_size(self) -> tuple[int, int]:
        return self.display.get_size()

    def get_display(self) -> pygame.display:
        return self.display