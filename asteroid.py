import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius == ASTEROID_MIN_RADIUS:
            self.kill()

        angle = random.uniform(20, 50)
        vector1 = self.velocity.copy().rotate(angle) * 1.2
        vector2 = self.velocity.copy().rotate(-angle) * 1.2
        asteroid1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        asteroid2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        asteroid1.velocity = vector1
        asteroid2.velocity = vector2
        self.kill()
