import pygame
import math
from path import PATH

class Enemy:
    def __init__(self):
        self.image = pygame.Surface((20, 30))
        self.image.fill((255, 0, 0))  # Red square
        self.rect = self.image.get_rect()
        self.path = PATH
        self.current_point = 0
        self.rect.center = self.path[self.current_point]
        self.speed = 2

    def move(self):
        if self.current_point + 1 >= len(self.path):
            return  # Reached end

        target = self.path[self.current_point + 1]
        dx, dy = target[0] - self.rect.centerx, target[1] - self.rect.centery
        distance = math.hypot(dx, dy)
        if distance < self.speed:
            self.current_point += 1
        else:
            dx, dy = dx / distance, dy / distance
            self.rect.centerx += dx * self.speed
            self.rect.centery += dy * self.speed

    def draw(self, win):
        win.blit(self.image, self.rect)
