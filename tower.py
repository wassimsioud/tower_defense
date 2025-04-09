# tower.py

import pygame

class Tower:
    def __init__(self, position):
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 100, 255), (20, 20), 20)
        self.rect = self.image.get_rect(center=position)
        self.range = 100  # Detection range
        self.cooldown = 60  # Frames between shots
        self.timer = 0

    def draw(self, win):
        win.blit(self.image, self.rect)
        # Draw range (optional for debugging)
        pygame.draw.circle(win, (0, 100, 255, 50), self.rect.center, self.range, 1)

    def update(self):
        self.timer += 1
