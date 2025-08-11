import pygame
from config import HEIGHT, GREEN, WHITE, BLACK
from Tower import ANTIBIOTICS_TOWER
from Enzyme_tower import ENZYME_TOWER

CATEGORIES = ["A","B"]
CATEGORY_TO_ITEMS = {
    "A": ANTIBIOTICS_TOWER,
    "B": ENZYME_TOWER,
}

def draw_ui(win, ui_level, selected_category, selected_tower_type):
    
    y = HEIGHT - 50
    x = 10
    mouse_pos = pygame.mouse.get_pos()
    font = pygame.font.SysFont(None, 24)

    if ui_level == 1:
        for cat in CATEGORIES:
            rect = pygame.Rect(x, y, 100, 40)
            color = (255, 255, 255)
            if rect.collidepoint(mouse_pos): color = (144, 255, 144)
            if selected_category == cat:     color = (0, 200, 0)

            pygame.draw.rect(win, color, rect)
            pygame.draw.rect(win, (0,0,0), rect, 2)
            text = font.render(cat, True, (0,0,0))
            win.blit(text, (x + 10, y + 10))
            x += 110
    elif ui_level == 2 and selected_category in CATEGORY_TO_ITEMS:

        for name in CATEGORY_TO_ITEMS[selected_category]:
            rect = pygame.Rect(x, y, 100, 40)
            if rect.collidepoint(mouse_pos):
                color = (144, 255, 144)
            if selected_tower_type == name:
                color = GREEN  
            if not rect.collidepoint(mouse_pos) and selected_tower_type != name:
                color = WHITE  

            pygame.draw.rect(win, color, rect)
            pygame.draw.rect(win, BLACK, rect, 2)
            text = font.render(name, True, BLACK)
            win.blit(text, (x + 10, y + 10))
            x += 110