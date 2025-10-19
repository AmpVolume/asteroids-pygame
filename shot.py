#shot.py

import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def update(self, dt):
        self.position += self.velocity * dt
        # Kill if off-screen
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
