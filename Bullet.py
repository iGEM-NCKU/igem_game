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

class Penicillin_bullet(Bullet):
    def __init__(self, x, y, target):
        super().__init__(x, y, target)
        self.damage = 40
class Cephalosporin_bullet(Bullet):
    def __init__(self, x, y, target):
        super().__init__(x, y, target)
        self.damage = 50
class Tetracycline_bullet(Bullet):
    def __init__(self, x, y, target):
        super().__init__(x, y, target)
        self.damage = 35
class Macrolide_bullet(Bullet):
    def __init__(self, x, y, target):
        super().__init__(x, y, target)
        self.damage = 45


ANTIBIOTICS_BULLET = {
    "Penicillin": Penicillin_bullet,
    "Cephalosporin": Cephalosporin_bullet,
    "Tetracycline":Tetracycline_bullet,
    "Macrolide": Macrolide_bullet
}

