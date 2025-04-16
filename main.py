import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")

    # Set Display settings
    print(f"Screen width: {SCREEN_WIDTH}\n"
          f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set fps
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        # Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Placeholder screen method
        screen.fill("black")

        # Set delta time (seconds)
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
