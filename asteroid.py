import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        angle = random.uniform(0, 360)
        speed = random.uniform(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED)
        self.velocity = pygame.Vector2(speed, 0).rotate(angle)

        # Determine asteroid size for scoring
        if radius > ASTEROID_MAX_RADIUS * 0.66:
            self.size = "large"
        elif radius > ASTEROID_MAX_RADIUS * 0.33:
            self.size = "medium"
        else:
            self.size = "small"

    def update(self, dt):
        self.position += self.velocity * dt

        # Screen wrap-around
        if self.position.x < 0:
            self.position.x += SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x -= SCREEN_WIDTH

        if self.position.y < 0:
            self.position.y += SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y -= SCREEN_HEIGHT

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # 💥 Split into smaller asteroids when destroyed
    def split(self):
        # Smallest asteroids just disappear
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []

        new_radius = self.radius / 2
        new_asteroids = []

        for _ in range(2):
            angle = random.uniform(0, 360)
            speed = random.uniform(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED)
            vel = pygame.Vector2(speed, 0).rotate(angle)
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = vel
            new_asteroids.append(asteroid)

        return new_asteroids

    # 🧮 Get score value based on asteroid size
    def get_score_value(self):
        if self.size == "large":
            return SCORE_LARGE
        elif self.size == "medium":
            return SCORE_MEDIUM
        else:
            return SCORE_SMALL
