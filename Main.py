
import pygame
import os
import cv2
from Screen import Screen
import time
from Menu import Menu

pygame.init()

screen = Screen()

chemin_video = os.path.join('Data/Intro/Pokemon_intro.mp4')
cap = cv2.VideoCapture(chemin_video)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error opening video file. Try installing OpenCV")
    pygame.quit()
    exit()

# Get the video's frame width and height
frame_width = 950  
frame_height = 720  

# Create a Pygame window with the same size as the video frame
window = pygame.display.set_mode((1280, 880))  
pygame.display.set_caption("pokemon")

# Load and play the music
pygame.mixer.music.load('Data/Intro/pokemon_sound.mp3')
pygame.mixer.music.play(-1)  # -1 means play the music on loop

# Read and display each frame of the video
intro = True
while intro:
    ret, frame = cap.read()
    if not ret:
        # If the video has ended, break out of the loop
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally (Y-axe)

    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
    
    # Resize the frame to fit the Pygame window
    frame = cv2.resize(frame, (frame_width, frame_height))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert the OpenCV image to a Pygame surface
    frame = pygame.surfarray.make_surface(frame)

    # Calculate the position to center the frame on the window
    if pygame.display.get_init():
        frame_x = (1280 - frame.get_width()) // 2  
        frame_y = (880 - frame.get_height()) // 2  

        # Blit the frame onto the window at the center position
        if pygame.display.get_active():
            window.blit(frame, (frame_x, frame_y))

            # Update the display
            pygame.display.flip()

    # Check for the user closing the window

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
            pygame.mixer.music.stop() 
            menu = Menu()
            menu.run()
            intro = False
            pygame.quit()
            
        

    # Decrease the delay between frames
    time.sleep(0.022)  

cap.release()
