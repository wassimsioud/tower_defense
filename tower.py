# tower.py

import pygame
import math

from bullet import Bullet  # Import the bullet

class Tower:
    def __init__(self, position):
        self.image = pygame.image.load("assets/images/tawer1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect(center=position)
        self.range = 150
        self.cooldown = 60
        self.timer = 0
        self.bullets = []

    def draw(self, win):
        win.blit(self.image, self.rect)
        pygame.draw.circle(win, (0, 100, 255, 50), self.rect.center, self.range, 1)
        for bullet in self.bullets:
            bullet.draw(win)

    def update(self, enemies):
        self.timer += 1

        # Find first enemy in range to shoot
        for enemy in enemies:
            if not enemy.alive:
                continue
            dx = enemy.rect.centerx - self.rect.centerx
            dy = enemy.rect.centery - self.rect.centery
            distance = math.hypot(dx, dy)
            if distance <= self.range and self.timer >= self.cooldown:
                self.bullets.append(Bullet(self.rect.center, enemy.rect.center))
                self.timer = 0
                break

        # Update bullets and check collision
        for bullet in self.bullets[:]:  # Copy of list for safe removal
            bullet.update()

            for enemy in enemies:
                if bullet.rect.colliderect(enemy.rect) and enemy.alive:
                    enemy.hit(50)  # Deal 50 damage
                    self.bullets.remove(bullet)
                    break

