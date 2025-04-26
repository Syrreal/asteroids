import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        # Each asteroid is a multiple of min radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        if new_radius:
            # Create 2 new asteroids with the new radius and update their velocities with random opposite directions
            rotation = random.uniform(20, 50)
            asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid1.velocity = self.velocity.rotate(rotation) * 1.2
            asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid2.velocity = self.velocity.rotate(-rotation) * 1.2
        
        self.kill()
