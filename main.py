import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")

    # Set Display settings & instantiate screen
    print(f"Screen width: {SCREEN_WIDTH}\n"
          f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set fps
    clock = pygame.time.Clock()
    dt = 0

    # Set up loop containers
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add sprites types to corresponding containers
    Player.containers = (updateable, drawable)

    # Instantiate player at screen center
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True:
        # Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Placeholder screen method
        screen.fill("black")

        # Update objects
        for object in updateable:
            object.update(dt)

        # Draw sprites
        for sprite in drawable:
            sprite.draw(screen)

        # Flip screen buffer to display new draw data
        pygame.display.flip()

        # Set delta time (seconds)
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
