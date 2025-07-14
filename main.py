# main.py

import pygame
from constants import *

def main():
    pygame.init()  # ✅ Initialize pygame

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # ✅ Create window

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # ✅ Allow window to close properly

        screen.fill((0, 0, 0))  # ✅ Fill the screen with black
        pygame.display.flip()   # ✅ Refresh the display

if __name__ == "__main__":
    main()

