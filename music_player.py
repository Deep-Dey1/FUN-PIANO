import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Load an audio file
pygame.mixer.music.load("myaudio.mp3")

# Play the audio
print("Playing music...")
pygame.mixer.music.play()

# Wait for the music to finish
while pygame.mixer.music.get_busy():
    time.sleep(1)

print("Music finished playing.")
