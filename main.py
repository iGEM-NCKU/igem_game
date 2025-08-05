import pygame
import math
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Tower Defense")

# Colors
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
BLACK = (0, 0, 0)

# Clock
FPS = 60

# Enemy Path
PATH = [(0, 300), (200, 300), (200, 500), (600, 500), (600, 100), (800, 100)]

class Enemy:
    def __init__(self):
        self.path = PATH
        self.pos_index = 0
        self.x, self.y = self.path[0]
        self.speed = 1.5
        self.health = 100
        self.max_health = 100

    def move(self):
        if self.pos_index + 1 >= len(self.path):
            return False  # reached end
        target_x, target_y = self.path[self.pos_index + 1]
        dx, dy = target_x - self.x, target_y - self.y
        dist = math.hypot(dx, dy)
        if dist < self.speed:
            self.pos_index += 1
        else:
            self.x += dx / dist * self.speed
            self.y += dy / dist * self.speed
        return True

    def draw(self, win):
        pygame.draw.circle(win, RED, (int(self.x), int(self.y)), 10)
        # Health bar
        pygame.draw.rect(win, RED, (self.x - 15, self.y - 20, 30, 5))
        pygame.draw.rect(win, GREEN, (self.x - 15, self.y - 20, 30 * self.health / self.max_health, 5))

class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 150
        self.cooldown = 60  # frames between shots
        self.timer = 0

    def draw(self, win):
        pygame.draw.circle(win, BLUE, (self.x, self.y), 20)
        pygame.draw.circle(win, WHITE, (self.x, self.y), self.range, 1)

    def shoot(self, enemies, bullets):
        if self.timer > 0:
            self.timer -= 1
            return
        for e in enemies:
            dist = math.hypot(e.x - self.x, e.y - self.y)
            if dist <= self.range:
                bullets.append(Bullet(self.x, self.y, e))
                self.timer = self.cooldown
                break

class Bullet:
    def __init__(self, x, y, target):
        self.x = x
        self.y = y
        self.target = target
        self.speed = 6
        self.damage = 20

    def move(self):
        dx, dy = self.target.x - self.x, self.target.y - self.y
        dist = math.hypot(dx, dy)
        if dist < self.speed or self.target.health <= 0:
            self.target.health -= self.damage
            return False  # bullet disappears
        self.x += dx / dist * self.speed
        self.y += dy / dist * self.speed
        return True

    def draw(self, win):
        pygame.draw.circle(win, BLACK, (int(self.x), int(self.y)), 5)

def draw_window(win, enemies, towers, bullets):
    win.fill((200, 200, 200))
    for p in PATH:
        pygame.draw.circle(win, BLACK, p, 5)
    for e in enemies:
        e.draw(win)
    for t in towers:
        t.draw(win)
    for b in bullets:
        b.draw(win)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    enemies = []
    towers = [Tower(300, 400), Tower(500, 300)]
    bullets = []
    spawn_timer = 0

    while run:
        clock.tick(FPS)

        # Quit check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Spawn enemies
        spawn_timer += 1
        if spawn_timer > 120:  # spawn every 2 seconds
            enemies.append(Enemy())
            spawn_timer = 0

        # Update enemies
        enemies = [e for e in enemies if e.move() and e.health > 0]

        # Towers shoot
        for tower in towers:
            tower.shoot(enemies, bullets)

        # Update bullets
        new_bullets = []
        for bullet in bullets:
            if bullet.move():
                new_bullets.append(bullet)
        bullets = new_bullets

        # Draw everything
        draw_window(WIN, enemies, towers, bullets)

    pygame.quit()

if __name__ == "__main__":
    main()
