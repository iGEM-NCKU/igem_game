import pygame
import math
from config import BLACK

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

    def setBulletDamage(self, damage):
        self.damage = damage