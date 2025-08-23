import pygame
from config import HEIGHT, GREEN, WHITE, BLACK,USER_HEART, STAGE1
from Tower import ANTIBIOTICS_TOWER
from Enzyme_tower import ENZYME_TOWER


heart_image = pygame.transform.scale(pygame.image.load(USER_HEART),(60,40))

CATEGORIES = ["A","B"]
CATEGORY_TO_ITEMS = {
    "A": ANTIBIOTICS_TOWER,
    "B": ENZYME_TOWER,
}
ALL_TOWER_INFO = {
    "Panicillin":"Penicillin, First antibiotics found in human history",
    "Cephalosorin":"Cephalosorin, a antibiotics",
    "Tetracycline":"Tetracycline, a antibiotics",
    "Macrolide":"Macrolide, a antibiotics"
}
def draw_ui(win, ui_level, selected_category, selected_tower_type,minus_heart):
    
    y = HEIGHT - 50
    x = 10
    mouse_pos = pygame.mouse.get_pos()
    font = pygame.font.SysFont(None, 24)

    #user heart
    heart_x = 10
    heart_y = 10
    hearts = STAGE1["hearts"] - minus_heart
    for i in range(hearts):
        win.blit(heart_image,(heart_x,heart_y))
        heart_x += 20

    #down ui
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

        back_rect = pygame.Rect(10, y - 45, 80, 35)
        pygame.draw.rect(win, (230,230,230), back_rect)
        pygame.draw.rect(win, (0,0,0), back_rect, 2)
        win.blit(font.render("Back", True, (0,0,0)), (20, y - 40))