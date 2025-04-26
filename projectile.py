import pygame
from circleshape import CircleShape
from constants import SHOT_SIZE, SHOT_SPEED

class Projectile(CircleShape):

    def __init__(self, x, y, direction, radius = SHOT_SIZE):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1).rotate(direction) * SHOT_SPEED
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt