import pygame
import math
from config import BLUE, WHITE

class Enzyme_Tower():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 100
        self.size = 20
        self.cooldown = 60 # frames between shots
        self.timer = 0
        self.cost = 100
        self.duration = 2
        self.durationTimer = self.duration * 60
        self.damage = 30

    def draw(self, win, mx, my):
        pygame.draw.circle(win, BLUE, (self.x, self.y), 20)
        distance = ((mx - self.x) ** 2 + (my - self.y) ** 2) ** 0.5
        if distance <= self.size:
            s = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA)
            pygame.draw.circle(s, (255, 255, 255, 100), (self.range, self.range), self.range)
            win.blit(s, (self.x - self.range, self.y - self.range))

    def apply_area_damage(self,enemies):
         if self.timer > 0:
            self.timer -= 1
            return
         else:
            for e in enemies:
                dist = math.hypot(e.x - self.x, e.y - self.y)
                self.timer = self.cooldown
                if dist <= self.range:
                    e.health -= self.damage
    def setTowerCooldown(self, cooldownSec):
        self.cooldown = cooldownSec

    def update(self):
        if self.durationTimer > 0:
            self.durationTimer -= 1
            return True  
        return False 
    
class DNase1(Enzyme_Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.damage = 20
        self.cooldown = 108
        self.duration = 20
        self.durationTimer = self.duration * 60
class Proteinase_K(Enzyme_Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.damage = 20
        self.cooldown = 72
        self.duration = 25
        self.durationTimer = self.duration * 60
class Dispersin_B(Enzyme_Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.damage = 20
        self.cooldown = 90
        self.duration = 20
        self.durationTimer = self.duration * 60

ENZYME_TOWER = {
    "DNsae1" : DNase1,
    "Proteinase_K" : Proteinase_K,
    "Dispersin_B" : Dispersin_B
}