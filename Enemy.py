import pygame
import math
from config import RED, GREEN, BLACK, GRAY, YELLOW

class Enemy:
    def __init__(self,PATH):
        self.path = PATH
        self.pos_index = 0
        self.x, self.y = self.path[0]
        self.speed = 2
        self.polysac = 0
        self.max_polysac = 0
        self.damage = 1
        self.Dna_membrane = 0
        self.max_Dna_membrane = 0
        self.protein_membrane = 0
        self.max_protein_membrane= 0
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

        if self.check_death():
            return False  # enemy is dead
        
        return True

    def draw(self, win):
        pygame.draw.circle(win, RED, (int(self.x), int(self.y)), 10)

    def check_death(self):
        if self.Dna_membrane <= 0 and self.protein_membrane <= 0 and self.polysac <= 0:
            return True
        return False

class S_aureus(Enemy):
    def __init__(self, PATH):
        super().__init__(PATH)
        self.speed = 2
        self.damage = 1
        self.polysac = 50
        self.max_polysac = 50
        self.protein_membrane = 70
        self.max_protein_membrane = 70
    def draw(self, win):
        pygame.draw.circle(win, BLACK, (int(self.x), int(self.y)), 10)
        # polysac bar
        if not self.polysac <= 0:
            pygame.draw.rect(win, RED, (self.x - 15, self.y - 28, 30, 5))
            pygame.draw.rect(win, GREEN, (self.x - 15, self.y - 28, 30 * self.polysac / self.max_polysac, 5))
        # protein bar
        if not self.protein_membrane <= 0:
            pygame.draw.rect(win, RED, (self.x - 15, self.y - 20, 30, 5))
            pygame.draw.rect(win, GRAY, (self.x - 15, self.y - 20, 30 * self.protein_membrane / self.max_protein_membrane, 5))
        
class Streptococcus(Enemy):
    def __init__(self, PATH):
        super().__init__(PATH)
        self.speed = 2.4
        self.damage = 1
        self.polysac = 50
        self.max_polysac = 50
    def draw(self, win):
        pygame.draw.circle(win, BLACK, (int(self.x), int(self.y)), 10)
        # polysac bar
        if not self.polysac <= 0:
            pygame.draw.rect(win, RED, (self.x - 15, self.y - 20, 30, 5))
            pygame.draw.rect(win, GREEN, (self.x - 15, self.y - 20, 30 * self.polysac / self.max_polysac, 5))

class E_coli(Enemy):
    def __init__(self, PATH):
        super().__init__(PATH)
        self.speed = 2.2
        self.damage = 2
        self.protein_membrane = 70
        self.max_protein_membrane = 70
        self.Dna_membrane = 40
        self.max_Dna_membrane = 40

    def draw(self, win):
        pygame.draw.circle(win, BLACK, (int(self.x), int(self.y)), 10)

        # dna
        if not self.Dna_membrane <= 0:
            pygame.draw.rect(win, RED, (self.x - 15, self.y - 28, 30, 5))
            pygame.draw.rect(win, GRAY, (self.x - 15, self.y - 28, 30 * self.Dna_membrane / self.max_Dna_membrane, 5))
        # protein bar
        if not self.protein_membrane <= 0:
            pygame.draw.rect(win, RED, (self.x - 15, self.y - 20, 30, 5))
            pygame.draw.rect(win, YELLOW, (self.x - 15, self.y - 20, 30 * self.protein_membrane / self.max_protein_membrane, 5))
class P_aeruginosa(Enemy):
    def __init__(self, PATH):
        super().__init__(PATH)
        self.speed = 1.8
        self.damage = 3
        self.polysac = 60
        self.max_polysac = 60
        self.Dna_membrane = 50
        self.max_Dna_membrane = 50
        self.protein_membrane = 70
        self.max_protein_membrane = 70
    def draw(self, win):
        pygame.draw.circle(win, BLACK, (int(self.x), int(self.y)), 10)
        # polysac bar
        if not self.polysac <= 0:
            pygame.draw.rect(win, RED, (self.x - 15, self.y - 36, 30, 5))
            pygame.draw.rect(win, GREEN, (self.x - 15, self.y - 36, 30 * self.polysac / self.max_polysac, 5))
        # dna
        if not self.Dna_membrane <= 0:
            pygame.draw.rect(win, RED, (self.x - 15, self.y - 28, 30, 5))
            pygame.draw.rect(win, GRAY, (self.x - 15, self.y - 28, 30 * self.Dna_membrane / self.max_Dna_membrane, 5))
        # protein bar
        if not self.protein_membrane <= 0:
            pygame.draw.rect(win, RED, (self.x - 15, self.y - 20, 30, 5))
            pygame.draw.rect(win, YELLOW, (self.x - 15, self.y - 20, 30 * self.protein_membrane / self.max_protein_membrane, 5))
        
class Mycobacterium(Enemy):
    def __init__(self, PATH):
        super().__init__(PATH)
        self.speed = 1.6
        self.damage = 3
        self.polysac = 80
        self.max_polysac = 80
        self.protein_membrane = 80
        self.max_protein_membrane = 80
    def draw(self, win):
        pygame.draw.circle(win, BLACK, (int(self.x), int(self.y)), 10)
        # polysac bar
        pygame.draw.rect(win, RED, (self.x - 15, self.y - 28, 30, 5))
        pygame.draw.rect(win, GREEN, (self.x - 15, self.y - 28, 30 * self.polysac / self.max_polysac, 5))
        # protein bar
        pygame.draw.rect(win, RED, (self.x - 15, self.y - 20, 30, 5))
        pygame.draw.rect(win, YELLOW, (self.x - 15, self.y - 20, 30 * self.protein_membrane / self.max_protein_membrane, 5))
        
ENEMY_TYPE = [S_aureus, Streptococcus, E_coli, P_aeruginosa, Mycobacterium]