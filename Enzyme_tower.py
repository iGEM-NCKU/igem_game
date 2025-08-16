import pygame
import math
from config import BLUE

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
        self.show_range_timer = 0
    def draw(self, win, mx, my):
        pygame.draw.circle(win, BLUE, (self.x, self.y), 20)
        distance = ((mx - self.x) ** 2 + (my - self.y) ** 2) ** 0.5
        if distance <= self.size:
            s = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA)
            pygame.draw.circle(s, (225, 255, 255, 100), (self.range, self.range), self.range)
            win.blit(s, (self.x - self.range, self.y - self.range))
        if self.show_range_timer > 0:
                s = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA)
                pygame.draw.circle(s, (123, 255, 255, 30), (self.range, self.range), self.range)
                win.blit(s, (self.x - self.range, self.y - self.range))
                self.show_range_timer -= 1


    def apply_area_damage(self,enemies):

        if self.timer > 0:
            self.timer -= 1
            return
        else:
            for e in enemies:
                dist = math.hypot(e.x - self.x, e.y - self.y)
                self.timer = self.cooldown
                if dist <= self.range:
                    e.polsac -= self.damage
            self.timer = self.cooldown
            self.show_range_timer = 5
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
    def apply_area_damage(self,enemies):

        if self.timer > 0:
            self.timer -= 1
            return
        else:
            for e in enemies:
                dist = math.hypot(e.x - self.x, e.y - self.y)
                self.timer = self.cooldown
                if dist <= self.range:
                    e.Dna_membrane -= self.damage
            self.timer = self.cooldown
            self.show_range_timer = 5
class Proteinase_K(Enzyme_Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.damage = 20
        self.cooldown = 72
        self.duration = 25
        self.durationTimer = self.duration * 60
    def apply_area_damage(self,enemies):

        if self.timer > 0:
            self.timer -= 1
            return
        else:
            for e in enemies:
                dist = math.hypot(e.x - self.x, e.y - self.y)
                self.timer = self.cooldown
                if dist <= self.range:
                    e.protein_membrane -= self.damage
            self.timer = self.cooldown
            self.show_range_timer = 5
class Dispersin_B(Enzyme_Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.damage = 20
        self.cooldown = 90
        self.duration = 20
        self.durationTimer = self.duration * 60
    def apply_area_damage(self,enemies):

        if self.timer > 0:
            self.timer -= 1
            return
        else:
            for e in enemies:
                dist = math.hypot(e.x - self.x, e.y - self.y)
                self.timer = self.cooldown
                if dist <= self.range:
                    e.polysac -= self.damage
            self.timer = self.cooldown
            self.show_range_timer = 5

ENZYME_TOWER = {
    "DNsae1" : DNase1,
    "Proteinase_K" : Proteinase_K,
    "Dispersin_B" : Dispersin_B
}