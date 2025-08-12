import pygame
from config import RED, PATH

class Biofilm:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cooldown = 120 # frames between shots
        self.timer = 0
        self.closest_index, self.closest_spot = min(
                                            enumerate(PATH),
                                            key=lambda p: ((p[1][0] - self.x)**2 + (p[1][1] - self.y)**2)**0.5
                                        )
        self.myPath = [(self.x,self.y)]+PATH[self.closest_index:]
    def draw(self, win):
        pygame.draw.circle(win, RED, (self.x, self.y), 20)
        
    def getTowerCooldown(self):
        return self.cooldown


