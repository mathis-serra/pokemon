import pygame
import os
import cv2
from Screen import Screen
pygame.init()

# class Screen:
#     def __init__(self):
#         self.size = (1280, 7200)
    
#     def get_size(self):
#         return self.size

screen = Screen()

chemin_video = os.path.join('Data/Intro/Pokemon_intro.mp4')
cap = cv2.VideoCapture(chemin_video)

ret, frame = cap.read()
if not ret:
    # Return to the beginning
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Resize the image to the size of the Pygame window
frame = cv2.resize(frame, (1280, 720))
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Convert the OpenCV image to a Pygame surface
frame = pygame.surfarray.make_surface(frame)

# Create a Pygame window
window = pygame.display.set_mode(screen.get_size())
pygame.display.set_caption("pokemon")

# Blit the frame onto the window
window.blit(frame, (0, 0))
pygame.display.flip()

# Wait for the user to close the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False

cap.release()
pygame.quit()
