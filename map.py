import pygame

#Grid_size
GRID_SIZE = 40

TILE_MAP_WIDTH = 32
TILE_MAP_HEIGHT = 18

def get_grid_position(mx, my):
    grid_x = (mx // GRID_SIZE) * GRID_SIZE
    grid_y = (my // GRID_SIZE) * GRID_SIZE
    return grid_x, grid_y

top_t = pygame.transform.scale(pygame.image.load("src/top_t.png"), (GRID_SIZE, GRID_SIZE))
down_t = pygame.transform.scale(pygame.image.load("src/down_t.png"), (GRID_SIZE, GRID_SIZE))
cross = pygame.transform.scale(pygame.image.load("src/cross.png"), (GRID_SIZE, GRID_SIZE))
right_t = pygame.transform.scale(pygame.image.load("src/right_t.png"), (GRID_SIZE, GRID_SIZE))
right_top = pygame.transform.scale(pygame.image.load("src/right_top.png"), (GRID_SIZE, GRID_SIZE))
right_down = pygame.transform.scale(pygame.image.load("src/right_down.png"), (GRID_SIZE, GRID_SIZE))
left_t = pygame.transform.scale(pygame.image.load("src/left_t.png"), (GRID_SIZE, GRID_SIZE))
left_top = pygame.transform.scale(pygame.image.load("src/left_top.png"), (GRID_SIZE, GRID_SIZE))
left_down = pygame.transform.scale(pygame.image.load("src/left_down.png"), (GRID_SIZE, GRID_SIZE))
parallel = pygame.transform.scale(pygame.image.load("src/parallel.png"), (GRID_SIZE, GRID_SIZE))
terminal_top = pygame.transform.scale(pygame.image.load("src/terminal_top.png"), (GRID_SIZE, GRID_SIZE))
terminal_down = pygame.transform.scale(pygame.image.load("src/terminal_down.png"), (GRID_SIZE, GRID_SIZE))
terminal_right = pygame.transform.scale(pygame.image.load("src/terminal_right.png"), (GRID_SIZE, GRID_SIZE))
terminal_left = pygame.transform.scale(pygame.image.load("src/terminal_left.png"), (GRID_SIZE, GRID_SIZE))
map_background = pygame.transform.scale(pygame.image.load("src/map_background.png"), (GRID_SIZE, GRID_SIZE))
vertical = pygame.transform.scale(pygame.image.load("src/vertical.png"), (GRID_SIZE, GRID_SIZE))

TILE_IMAGES = {
    0: map_background,
    1: top_t,           
    2: down_t,           
    3: right_t,         
    4: cross,           
    5: left_t,          
    6: terminal_top,    
    7: terminal_down,  
    8: terminal_right, 
    9: terminal_left,   
    10: parallel,       
    11: right_top,      
    12: right_down,     
    13: left_top,       
    14: left_down,      
    15: vertical        
}

map_data = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,12,10,10,10,10,10,10,14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,15,0,0,0,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,15,0,0,0,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [8,10,10,10,10,10,13,0,0,0,0,0,0,11,10,10,10,10,10,14,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,10,10,10,10,10,14,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,10,10,10,10,10,9],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

class Tile:
    def __init__(self, col, row, tile_type):
        self.col = col
        self.row = row
        self.tile_type = tile_type
        self.x = col * GRID_SIZE
        self.y = row * GRID_SIZE
        self.width = GRID_SIZE
        self.height = GRID_SIZE

    @property
    def center(self):
        return self.x + self.width // 2, self.y + self.height // 2

    def is_path(self):
        return self.tile_type != 0

    def can_place_tower(self):
         return not self.is_path()

    def draw(self, screen):
        img = TILE_IMAGES[self.tile_type]
        screen.blit(img, (self.x, self.y))
