import pygame
from config import RED, WHITE


class Biofilm:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 150
        self.cooldown = 6 # frames between shots
        self.timer = 0

    def draw(self, win):
        pygame.draw.circle(win, RED, (self.x, self.y), 20)
        pygame.draw.circle(win, WHITE, (self.x, self.y), self.range, 1)

    def generate_enemy(self, enemies):
        if self.timer > 0:
            self.timer -= 1
            return
        
    def setTowerCooldown(self, cooldownSec):
        self.cooldown = cooldownSec