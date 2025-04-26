import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_COOLDOWN
from projectile import Projectile

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.shot_clock = 0.0
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        # movement vector
        movement = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt
        self.position += movement
    
    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        x, y = (self.position + forward * self.radius)
        projectile = Projectile(x, y, self.rotation)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        
        self.shot_clock += dt
        if self.shot_clock >= PLAYER_SHOOT_COOLDOWN:
            if keys[pygame.K_SPACE]:
                self.shot_clock = 0.0
                self.shoot()