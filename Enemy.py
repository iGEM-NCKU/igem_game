import pygame
import math
from config import RED, GREEN, BLACK, GRAY, YELLOW, WHITE, BLUE

s_a = pygame.transform.scale(pygame.image.load("src/enemy/staphylococcus-aureus.jpg"), (96, 80))
my = pygame.transform.scale(pygame.image.load("src/enemy/Mycobacterium.jpeg"), (96, 80))
ecoli = pygame.transform.scale(pygame.image.load("src/enemy/ecoli.jpg"), (96, 80))
p_a = pygame.transform.scale(pygame.image.load("src/enemy/P_aeruginosa.jpg"), (96, 80))
strept = pygame.transform.scale(pygame.image.load("src/enemy/Streptococcus.jpg"), (96, 80))
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
        self.name = ""
        self.info_range = 50
        self.pic = s_a

        self.health = 50
        self.max_health = 50
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
    
    def draw_info(self, win,message, mx,my):
        font = pygame.font.SysFont(None, 24)
        lines = message.split('\n')
        text_height = sum([font.get_height() for line in lines])
        tooltip_height = max(text_height, self.pic.get_height()) + 10
        tooltip_width = max([font.size(line)[0] for line in lines]) + 100
        pygame.draw.rect(win, WHITE, (mx + 5, my - 25, tooltip_width+ 10, tooltip_height + 10))
        pygame.draw.rect(win, YELLOW, (mx + 5, my - 25, tooltip_width + 10, tooltip_height + 10), 2)
        win.blit(self.pic, (mx + 10, my - 20))  

        y_offset = my - 12
        for line in lines:
            text = font.render(line, True, BLACK)
            win.blit(text, (mx + 15 + self.pic.get_width(), y_offset))  # 文字顯示在圖片右邊
            y_offset += font.get_height() 

    def draw(self, message, win, mx, my):
        pygame.draw.circle(win, RED, (int(self.x), int(self.y)), 10)
        font = pygame.font.SysFont(None, 24)
        text = font.render(message, True, BLACK)
        pygame.draw.rect(win, WHITE, (mx + 5, my - 25, text.get_width() + 10, text.get_height() + 10))
        pygame.draw.rect(win, BLACK, (mx + 5, my - 25, text.get_width() + 10, text.get_height() + 10), 2)
        win.blit(text, (mx + 10, my - 20))
    def check_death(self):
        if self.Dna_membrane <= 0 and self.protein_membrane <= 0 and self.polysac <= 0 and self.health <= 0:
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
        self.name = "Staphylococcus aureus"
        self.pic = s_a
        self.health = 50
        self.max_health = 50
    def draw(self, message, win, mx, my):
        distance = ((mx - self.x) ** 2 + (my - self.y) ** 2) ** 0.5
        pygame.draw.circle(win, BLACK, (int(self.x), int(self.y)), 10)

        # polysac bar
        if not self.polysac <= 0:
            pygame.draw.rect(win, RED, (self.x - 15, self.y - 36, 30, 5))
            pygame.draw.rect(win, BLUE, (self.x - 15, self.y - 36, 30 * self.polysac / self.max_polysac, 5))
        # protein bar
        if not self.protein_membrane <= 0:
            pygame.draw.rect(win, RED, (self.x - 15, self.y - 28, 30, 5))
            pygame.draw.rect(win, GRAY, (self.x - 15, self.y - 28, 30 * self.protein_membrane / self.max_protein_membrane, 5))
        #health bar
        pygame.draw.rect(win, RED, (self.x - 15, self.y - 20, 30, 5))
        pygame.draw.rect(win, GREEN, (self.x - 15, self.y - 20, 30 * self.health / self.max_health, 5))
        if distance < self.info_range:
            self.draw_info(win, message, mx, my)       
class Streptococcus(Enemy):
    def __init__(self, PATH):
        super().__init__(PATH)
        self.speed = 2.4
        self.damage = 1
        self.polysac = 50
        self.max_polysac = 50
        self.name = "Streptococcus"
        self.pic = strept
        self.health = 50
        self.max_health = 50
    def draw(self, message, win, mx, my):
        pygame.draw.circle(win, BLACK, (int(self.x), int(self.y)), 10)
        distance = ((mx - self.x) ** 2 + (my - self.y) ** 2) ** 0.5
        if distance < self.info_range:
            self.draw_info(win, message, mx, my)
        # polysac bar
        if not self.polysac <= 0:
            pygame.draw.rect(win, RED, (self.x - 15, self.y - 28, 30, 5))
            pygame.draw.rect(win, BLUE, (self.x - 15, self.y - 28, 30 * self.polysac / self.max_polysac, 5))
        #health bar
        pygame.draw.rect(win, RED, (self.x - 15, self.y - 20, 30, 5))
        pygame.draw.rect(win, GREEN, (self.x - 15, self.y - 20, 30 * self.health / self.max_health, 5))
        
        if distance < self.info_range:
            self.draw_info(win, message, mx, my)
class E_coli(Enemy):
    def __init__(self, PATH):
        super().__init__(PATH)
        self.speed = 2.2
        self.damage = 2
        self.protein_membrane = 70
        self.max_protein_membrane = 70
        self.Dna_membrane = 40
        self.max_Dna_membrane = 40
        self.name = "Escherichia coli"
        self.pic = ecoli
        self.health = 50
        self.max_health = 50
    def draw(self, message, win, mx, my):
        pygame.draw.circle(win, BLACK, (int(self.x), int(self.y)), 10)
        distance = ((mx - self.x) ** 2 + (my - self.y) ** 2) ** 0.5
        if distance < self.info_range:
            self.draw_info(win, message, mx, my)
        # dna
        if not self.Dna_membrane <= 0:
            pygame.draw.rect(win, RED, (self.x - 15, self.y - 36, 30, 5))
            pygame.draw.rect(win, GRAY, (self.x - 15, self.y - 36, 30 * self.Dna_membrane / self.max_Dna_membrane, 5))
        # protein bar
        if not self.protein_membrane <= 0:
            pygame.draw.rect(win, RED, (self.x - 15, self.y - 28, 30, 5))
            pygame.draw.rect(win, YELLOW, (self.x - 15, self.y - 28, 30 * self.protein_membrane / self.max_protein_membrane, 5))
        #health bar
        pygame.draw.rect(win, RED, (self.x - 15, self.y - 20, 30, 5))
        pygame.draw.rect(win, GREEN, (self.x - 15, self.y - 20, 30 * self.health / self.max_health, 5))
        
        if distance < self.info_range:
            self.draw_info(win, message, mx, my)
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
        self.name = "Pseudomonas aeruginosa"
        self.pic = p_a
        self.health = 50
        self.max_health = 50
    def draw(self, message, win, mx, my):
        pygame.draw.circle(win, BLACK, (int(self.x), int(self.y)), 10)
        distance = ((mx - self.x) ** 2 + (my - self.y) ** 2) ** 0.5
        if distance < self.info_range:
            self.draw_info(win, message, mx, my)
        # polysac bar
        if not self.polysac <= 0:
            pygame.draw.rect(win, RED, (self.x - 15, self.y - 44, 30, 5))
            pygame.draw.rect(win, BLUE, (self.x - 15, self.y - 44, 30 * self.polysac / self.max_polysac, 5))
        # dna
        if not self.Dna_membrane <= 0:
            pygame.draw.rect(win, RED, (self.x - 15, self.y - 36, 30, 5))
            pygame.draw.rect(win, GRAY, (self.x - 15, self.y - 36, 30 * self.Dna_membrane / self.max_Dna_membrane, 5))
        # protein bar
        if not self.protein_membrane <= 0:
            pygame.draw.rect(win, RED, (self.x - 15, self.y - 28, 30, 5))
            pygame.draw.rect(win, YELLOW, (self.x - 15, self.y - 28, 30 * self.protein_membrane / self.max_protein_membrane, 5))
        #health bar
        pygame.draw.rect(win, RED, (self.x - 15, self.y - 20, 30, 5))
        pygame.draw.rect(win, GREEN, (self.x - 15, self.y - 20, 30 * self.health / self.max_health, 5))
        
        if distance < self.info_range:
            self.draw_info(win, message, mx, my)
class Mycobacterium(Enemy):
    def __init__(self, PATH):
        super().__init__(PATH)
        self.speed = 1.6
        self.damage = 3
        self.polysac = 80
        self.max_polysac = 80
        self.protein_membrane = 80
        self.max_protein_membrane = 80
        self.name = "Mycobacterium"
        self.pic = my
        self.health = 50
        self.max_health = 50
    def draw(self, message, win, mx, my):
        pygame.draw.circle(win, BLACK, (int(self.x), int(self.y)), 10)
        distance = ((mx - self.x) ** 2 + (my - self.y) ** 2) ** 0.5
        if distance < self.info_range:
            self.draw_info(win, message, mx, my)
        # polysac bar
        pygame.draw.rect(win, RED, (self.x - 15, self.y - 36, 30, 5))
        pygame.draw.rect(win, BLUE, (self.x - 15, self.y - 36, 30 * self.polysac / self.max_polysac, 5))
        # protein bar
        pygame.draw.rect(win, RED, (self.x - 15, self.y - 28, 30, 5))
        pygame.draw.rect(win, YELLOW, (self.x - 15, self.y - 28, 30 * self.protein_membrane / self.max_protein_membrane, 5))
        #health bar
        pygame.draw.rect(win, RED, (self.x - 15, self.y - 20, 30, 5))
        pygame.draw.rect(win, GREEN, (self.x - 15, self.y - 20, 30 * self.health / self.max_health, 5))
        
        if distance < self.info_range:
            self.draw_info(win, message, mx, my)
ENEMY_TYPE = [S_aureus, Streptococcus, E_coli, P_aeruginosa, Mycobacterium]