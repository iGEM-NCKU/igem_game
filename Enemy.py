import pygame
import math
from config import RED, GREEN, BLACK, BLUE, GRAY

class Enemy:
    def __init__(self,PATH):
        self.path = PATH
        self.pos_index = 0
        self.x, self.y = self.path[0]
        self.speed = 2
        self.health = 100
        self.max_health = 100
        self.damage = 1
        self.Dna_membrane = 200
        self.Dna_membrane_max = 200
        self.protein_membrane = 0
        self.polysac_membrane = 0
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
        # sheild
        shield_width = (self.Dna_membrane / self.Dna_membrane_max) * 30 
        pygame.draw.rect(win, BLUE, (self.x - 15, self.y - 30, 30, 5)) 
        pygame.draw.rect(win, GRAY, (self.x - 15, self.y - 30, shield_width, 5))  

        # Health bar
        pygame.draw.rect(win, RED, (self.x - 15, self.y - 20, 30, 5))
        pygame.draw.rect(win, GREEN, (self.x - 15, self.y - 20, 30 * self.health / self.max_health, 5))

class S_aureus(Enemy):
    def __init__(self, PATH):
        super().__init__(PATH)
        self.speed = 2
        self.damage = 1
    def draw(self, win):
        pygame.draw.circle(win, BLACK, (int(self.x), int(self.y)), 10)
        # Health bar
        pygame.draw.rect(win, RED, (self.x - 15, self.y - 20, 30, 5))
        pygame.draw.rect(win, GREEN, (self.x - 15, self.y - 20, 30 * self.health / self.max_health, 5))

class Streptococcus(Enemy):
    def __init__(self, PATH):
        super().__init__(PATH)
        self.speed = 2.4
        self.damage = 1
class E_coli(Enemy):
    def __init__(self, PATH):
        super().__init__(PATH)
        self.speed = 2.2
        self.damage = 2
class P_aeruginosa(Enemy):
    def __init__(self, PATH):
        super().__init__(PATH)
        self.speed = 1.8
        self.damage = 3
class Mycobacterium(Enemy):
    def __init__(self, PATH):
        super().__init__(PATH)
        self.speed = 1.6
        self.damage = 3

ENEMY_TYPE = [S_aureus, Streptococcus, E_coli, P_aeruginosa, Mycobacterium]