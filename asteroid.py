from circleshape import CircleShape
import pygame
import constants
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        random_angle = random.uniform(20, 50)
        rotate_direction_A = self.velocity.rotate(random_angle)
        rotate_direction_B = self.velocity.rotate(-random_angle)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        new_astroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        new_astroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        
        new_astroid_a.velocity = rotate_direction_A
        new_astroid_b.velocity = rotate_direction_B

        new_astroid_a.velocity *= 1.2
        new_astroid_b.velocity *= 1.2
