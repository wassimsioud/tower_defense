import pygame
from enemy import Enemy
from tower import Tower
from path import PATH

pygame.init()

WIDTH, HEIGHT = 1530, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")

# Load the background image
background_image = pygame.image.load("./assets/images/background.png")

FPS = 60

# Game state
enemy_spawn_timer = 0
spawn_delay = 60  # 1 enemy per second
enemies = []
wave_size = 5
enemies_spawned = 0
towers = []

def draw_window():
    # Draw background image first
    WIN.blit(background_image, (0, 0))  # Draw background image


    # Draw towers
    for tower in towers:
        tower.draw(WIN)

    # Draw enemies
    for enemy in enemies:
        enemy.draw(WIN)

    pygame.display.update()

def main():
    global enemy_spawn_timer, enemies_spawned
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Left click to place tower
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                # Basic path collision check — skip if too close to any path point
                if all((abs(pos[0] - p[0]) > 30 or abs(pos[1] - p[1]) > 30) for p in PATH):
                    towers.append(Tower(pos))

        # Enemy spawn logic
        enemy_spawn_timer += 1
        if enemy_spawn_timer >= spawn_delay and enemies_spawned < wave_size:
            enemies.append(Enemy())
            enemies_spawned += 1
            enemy_spawn_timer = 0

        # Update enemies
        for enemy in enemies:
            enemy.move()

        # Update towers (for cooldown, etc.)
        for tower in towers:
            tower.update()

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()
