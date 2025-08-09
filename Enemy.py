import pygame
import math
from config import RED, GREEN

class Enemy:
    def __init__(self,PATH):
        self.path = PATH
        self.pos_index = 0
        self.x, self.y = self.path[0]
        self.speed = 6
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
