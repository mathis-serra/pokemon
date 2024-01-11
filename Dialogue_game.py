import pygame
pygame.init()

class TextRect:
    def __init__(self, font, text, rect, color=(255, 255, 255)):
        self.font = font
        self.text = text
        self.color = color
        self.rect = pygame.Rect(rect)
        self.rendered_text = self.render_text()

    def render_text(self):
        words = self.text.split(' ')
        space_width, _ = self.font.size(' ')
        current_line = ''
        rendered_lines = []

        for word in words:
            test_line = current_line + word + ' '
            width, height = self.font.size(test_line)

            if width <= self.rect.width and height <= self.rect.height:
                current_line = test_line
            else:
                rendered_lines.append(current_line)
                current_line = word + ' '

        rendered_lines.append(current_line)

        rendered_texts = [self.font.render(line, True, self.color) for line in rendered_lines]

        total_height = sum([text.get_height() for text in rendered_texts])
        y = self.rect.y + (self.rect.height - total_height) // 2

        for text in rendered_texts:
            text_rect = text.get_rect(center=(self.rect.centerx, y))
            y += text_rect.height

        return rendered_texts

    def draw(self, surface):
        for text in self.rendered_text:
            surface.blit(text, text.get_rect())

# Exemple d'utilisation
pygame.font.init()
font = pygame.font.Font(None, 36)

text_content = "Ceci est un exemple de texte qui sera affiché dans un rectangle et qui passera à la ligne si nécessaire."

text_rect = TextRect(font, text_content, (50, 50, 800, 200))

# Initialisation de la fenêtre Pygame
screen = pygame.display.set_mode((900, 300))
pygame.display.set_caption("Exemple de Rectangle de Texte")

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effacement de l'écran
    screen.fill((0, 0, 0))

    # Dessin du rectangle de texte
    text_rect.draw(screen)

    # Rafraîchissement de l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
