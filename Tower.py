import pygame
from config import BLUE
import math
from Bullet import Bullet, ANTIBIOTICS_BULLET

# 暫時使用已存在的圖片，避免崩潰
try:
    penicillin_image = pygame.transform.scale(pygame.image.load("src/penicillin_tower.png"), (60, 60))
except:
    penicillin_image = None
try:
    cephalosporin_image = pygame.transform.scale(pygame.image.load("src/cephalosporin_tower.png"), (60, 60))
except:
    cephalosporin_image = None
try:
    tetracycline_image = pygame.transform.scale(pygame.image.load("src/tetracycline_tower.png"), (60, 60))
except:
    tetracycline_image = None
try:
    macrolide_image = pygame.transform.scale(pygame.image.load("src/macrolide_tower.png"), (60, 60))
except:
    macrolide_image = None
try:
    antibiotics_tower_image = pygame.transform.scale(pygame.image.load("src/antibiotics_tower.png"), (60, 60))
except:
    antibiotics_tower_image = None

class Tower:
    def __init__(self, x, y, bullet = Bullet):
        self.x = x
        self.y = y
        self.size = 20
        self.range = 150
        self.cooldown = 60 # frames between shots
        self.timer = 0
        self.cost = 10
        self.duration = 2
        self.durationTimer = self.duration * 60
        self.bullet_class = bullet
    def draw(self, win, mx, my):
        # 繪製抗生素塔圖片 (如果圖片存在) 或畫圓圈
        if antibiotics_tower_image:
            img_rect = antibiotics_tower_image.get_rect(center=(self.x, self.y))
            win.blit(antibiotics_tower_image, img_rect)
        else:
            pygame.draw.circle(win, BLUE, (self.x, self.y), 20)
        
        distance = ((mx - self.x) ** 2 + (my - self.y) ** 2) ** 0.5
        if distance <= self.size:
            s = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA)
            pygame.draw.circle(s, (255, 255, 255, 100), (self.range, self.range), self.range)
            win.blit(s, (self.x - self.range, self.y - self.range))

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

    def update(self):
        if self.durationTimer > 0:
            self.durationTimer -= 1
            return True  
        return False 


class Penicillin(Tower):
    def __init__(self, x, y, bullet= ANTIBIOTICS_BULLET["Penicillin"]):
        super().__init__(x, y, bullet)
        self.duration = 90
        self.durationTimer = self.duration * 60
        self.cost = 15  # Penicillin 的價格
    
    def draw(self, win, mx, my):
        # 繪製Penicillin專屬圖片或藍圓圈
        if penicillin_image:
            img_rect = penicillin_image.get_rect(center=(self.x, self.y))
            win.blit(penicillin_image, img_rect)
        else:
            pygame.draw.circle(win, BLUE, (self.x, self.y), 20)
        
        distance = ((mx - self.x) ** 2 + (my - self.y) ** 2) ** 0.5
        if distance <= self.size:
            s = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA)
            pygame.draw.circle(s, (255, 255, 255, 100), (self.range, self.range), self.range)
            win.blit(s, (self.x - self.range, self.y - self.range))


class Cephalosporin(Tower):
    def __init__(self, x, y, bullet=ANTIBIOTICS_BULLET["Cephalosporin"]):
        super().__init__(x, y, bullet)
        self.duration = 90
        self.durationTimer = self.duration * 60
        self.cooldown = 54
        self.cost = 25  # Cephalosporin 的價格
    
    def draw(self, win, mx, my):
        # 繪製Cephalosporin專屬圖片
        img_rect = cephalosporin_image.get_rect(center=(self.x, self.y))
        win.blit(cephalosporin_image, img_rect)
        
        distance = ((mx - self.x) ** 2 + (my - self.y) ** 2) ** 0.5
        if distance <= self.size:
            s = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA)
            pygame.draw.circle(s, (255, 255, 255, 100), (self.range, self.range), self.range)
            win.blit(s, (self.x - self.range, self.y - self.range))

class Tetracycline(Tower):
    def __init__(self, x, y, bullet=ANTIBIOTICS_BULLET["Tetracycline"]):
        super().__init__(x, y, bullet)
        self.duration = 80
        self.durationTimer = self.duration * 60
        self.cooldown = 72
        self.cost = 20  # Tetracycline 的價格
    
    def draw(self, win, mx, my):
        # 繪製Tetracycline專屬圖片
        img_rect = tetracycline_image.get_rect(center=(self.x, self.y))
        win.blit(tetracycline_image, img_rect)
        
        distance = ((mx - self.x) ** 2 + (my - self.y) ** 2) ** 0.5
        if distance <= self.size:
            s = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA)
            pygame.draw.circle(s, (255, 255, 255, 100), (self.range, self.range), self.range)
            win.blit(s, (self.x - self.range, self.y - self.range))
class Macrolide(Tower):
    def __init__(self, x, y, bullet=ANTIBIOTICS_BULLET["Macrolide"]):
        super().__init__(x, y, bullet)
        self.duration = 80
        self.durationTimer = self.duration * 60
        self.cooldown = 48
        self.cost = 30  # Macrolide 的價格
    
    def draw(self, win, mx, my):
        # 繪製Macrolide專屬圖片
        img_rect = macrolide_image.get_rect(center=(self.x, self.y))
        win.blit(macrolide_image, img_rect)
        
        distance = ((mx - self.x) ** 2 + (my - self.y) ** 2) ** 0.5
        if distance <= self.size:
            s = pygame.Surface((self.range*2, self.range*2), pygame.SRCALPHA)
            pygame.draw.circle(s, (255, 255, 255, 100), (self.range, self.range), self.range)
            win.blit(s, (self.x - self.range, self.y - self.range))

ANTIBIOTICS_TOWER = {
    "Penicillin": Penicillin,
    "Cephalosporin": Cephalosporin,
    "Tetracycline":Tetracycline,
    "Macrolide": Macrolide
}
