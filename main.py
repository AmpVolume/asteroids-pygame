import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfeild import AsteroidField

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids Clone")
clock = pygame.time.Clock()

# Sprite groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

# Assign containers
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
Shot.containers = (shots, updatable, drawable)

# Game objects
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroid_field = AsteroidField(group=asteroids)

score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    dt = clock.tick(60) / 1000  # Delta time in seconds

    # --- Event handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Update objects ---
    for obj in list(updatable):
        obj.update(dt)

    asteroid_field.update(dt)

    # --- Collision: shots vs asteroids ---
    for shot in list(shots):
        for asteroid in list(asteroids):
            distance = shot.position.distance_to(asteroid.position)
            if distance <= shot.radius + asteroid.radius:
                shot.kill()
                asteroid.kill()
                score += 100  # Increase score

    # --- Collision: player vs asteroids ---
    for asteroid in list(asteroids):
        distance = player.position.distance_to(asteroid.position)
        if distance <= player.radius + asteroid.radius:
            print("Game Over!")
            running = False

    # --- Draw everything ---
    screen.fill((0, 0, 0))
    for sprite in drawable:
        sprite.draw(screen)

    # Draw score
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

    pygame.display.flip()

pygame.quit()

