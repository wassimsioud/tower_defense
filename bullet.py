# bullet.py

import pygame
import math

class Bullet:
    def __init__(self, position, target_pos):
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 0))  # Yellow bullet
        self.rect = self.image.get_rect(center=position)
        self.speed = 5

        dx, dy = target_pos[0] - position[0], target_pos[1] - position[1]
        distance = math.hypot(dx, dy)
        self.velocity = (dx / distance * self.speed, dy / distance * self.speed)

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def draw(self, win):
        win.blit(self.image, self.rect)
