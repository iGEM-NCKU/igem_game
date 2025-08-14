import pygame
from config import BLUE, WHITE
import math
from Bullet import Bullet, ANTIBIOTICS_BULLET

class Tower:
    def __init__(self, x, y, bullet = Bullet):
        self.x = x
        self.y = y
        self.size = 20
        self.range = 150
        self.cooldown = 60 # frames between shots
        self.timer = 0
        self.cost = 100
        self.duration = 2
        self.durationTimer = self.duration * 60
        self.bullet_class = bullet
    def draw(self, win, mx, my):
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
        self.duration = 30
        self.durationTimer = self.duration * 60


class Cephalosporin(Tower):
    def __init__(self, x, y, bullet=ANTIBIOTICS_BULLET["Cephalosporin"]):
        super().__init__(x, y, bullet)
        self.duration = 30
        self.durationTimer = self.duration * 60
        self.cooldown = 54

class Tetracycline(Tower):
    def __init__(self, x, y, bullet=ANTIBIOTICS_BULLET["Tetracycline"]):
        super().__init__(x, y, bullet)
        self.duration = 25
        self.durationTimer = self.duration * 60
        self.cooldown = 72
class Macrolide(Tower):
    def __init__(self, x, y, bullet=ANTIBIOTICS_BULLET["Macrolide"]):
        super().__init__(x, y, bullet)
        self.duration = 30
        self.durationTimer = self.duration * 60
        self.cooldown = 48

ANTIBIOTICS_TOWER = {
    "Penicillin": Penicillin,
    "Cephalosporin": Cephalosporin,
    "Tetracycline":Tetracycline,
    "Macrolide": Macrolide
}
