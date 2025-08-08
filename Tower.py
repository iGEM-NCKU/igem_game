import pygame
from config import BLUE, WHITE
import math
from Bullet import Bullet
class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 150
        self.cooldown = 60 # frames between shots
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
    def setTowerCooldown(self, cooldownSec):
        self.cooldown = cooldownSec