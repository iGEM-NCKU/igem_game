import pygame
import math
from config import BLUE

# 安全載入Tower圖片
try:
    dnase1_image = pygame.transform.scale(pygame.image.load("src/dnase1_tower.png"), (60, 60))
except:
    dnase1_image = None
try:
    proteinase_k_image = pygame.transform.scale(pygame.image.load("src/proteinase_k_tower.png"), (60, 60))
except:
    proteinase_k_image = None
try:
    dispersin_b_image = pygame.transform.scale(pygame.image.load("src/dispersin_b_tower.png"), (60, 60))
except:
    dispersin_b_image = None
try:
    enzyme_tower_image = pygame.transform.scale(pygame.image.load("src/enzyme_tower.png"), (60, 60))
except:
    enzyme_tower_image = None

class Enzyme_Tower():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 60
        self.size = 20
        self.cooldown = 60 # frames between shots
        self.timer = 0
        self.cost = 10
        self.duration = 2
        self.durationTimer = self.duration * 60
        self.damage = 30
        self.show_range_timer = 0
    def draw(self, win, mx, my):
        # 繪製Tower圖片或藍圓圈
        if enzyme_tower_image:
            img_rect = enzyme_tower_image.get_rect(center=(self.x, self.y))
            win.blit(enzyme_tower_image, img_rect)
        else:
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
        self.duration = 60
        self.durationTimer = self.duration * 60
        self.cost = 18  # DNase1 的價格
    
    def draw(self, win, mx, my):
        # 繪製DNase1專屬圖片
        img_rect = dnase1_image.get_rect(center=(self.x, self.y))
        win.blit(dnase1_image, img_rect)
        
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
                    e.Dna_membrane -= self.damage
            self.timer = self.cooldown
            self.show_range_timer = 5
class Proteinase_K(Enzyme_Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.damage = 20
        self.cooldown = 72
        self.duration = 60
        self.durationTimer = self.duration * 60
        self.cost = 22  # Proteinase_K 的價格
    
    def draw(self, win, mx, my):
        # 繪製Proteinase_K專屬圖片
        img_rect = proteinase_k_image.get_rect(center=(self.x, self.y))
        win.blit(proteinase_k_image, img_rect)
        
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
                    e.protein_membrane -= self.damage
            self.timer = self.cooldown
            self.show_range_timer = 5
class Dispersin_B(Enzyme_Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.damage = 20
        self.cooldown = 90
        self.duration = 60
        self.durationTimer = self.duration * 60
        self.cost = 25  # Dispersin_B 的價格
    
    def draw(self, win, mx, my):
        # 繪製Dispersin_B專屬圖片
        img_rect = dispersin_b_image.get_rect(center=(self.x, self.y))
        win.blit(dispersin_b_image, img_rect)
        
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
                    e.polysac -= self.damage
            self.timer = self.cooldown
            self.show_range_timer = 5

ENZYME_TOWER = {
    "DNsae1" : DNase1,
    "Proteinase_K" : Proteinase_K,
    "Dispersin_B" : Dispersin_B
}