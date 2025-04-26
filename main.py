import pygame
import pygame.freetype
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from projectile import Projectile

def game_over():
    print("Game over!")

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
    asteroids = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()

    # Add sprites types to corresponding containers
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Projectile.containers = (updateable, drawable, projectiles)

    # Instantiate player at screen center
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
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
        
        hits = []
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                game_over()
                return
            for projectile in projectiles:
                if asteroid.is_colliding(projectile):
                    hits.append((asteroid, projectile))
        
        for asteroid, projectile in hits:
            asteroid.split()
            projectile.kill()

        # Draw sprites
        for sprite in drawable:
            sprite.draw(screen)

        # Flip screen buffer to display new draw data
        pygame.display.flip()

        # Set delta time (seconds)
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
