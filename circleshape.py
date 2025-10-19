import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    # ✅ Add this method below
    def collides_with(self, other):
        """Check if this circle collides with another CircleShape."""
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)
