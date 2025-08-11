import pygame
import random

from Tower import ANTIBIOTICS_TOWER
from Enemy import Enemy
from Biofilm import Biofilm
from Loss_screen import loss_screen
from config import FPS, HEIGHT, WIDTH, BLACK, PATH, STAGE1, MAP_WIDTH, MAP_HEIGHT
from Enzyme_tower import ENZYME_TOWER
from draw_ui import draw_ui, CATEGORIES, CATEGORY_TO_ITEMS
def draw_window(win, enemies, towers, enzyme_towers, bullets, selected_tower_type,MONEY,escaped_count,holding_tower,biofilm,ui_level, selected_category):
    win.fill((200, 200, 200))
    for p in PATH:
        pygame.draw.circle(win, BLACK, p, 5)
    for e in enemies:
        e.draw(win)
    for t in towers:
        t.draw(win)
    for b in bullets:
        b.draw(win)
    for bi in biofilm:
        bi.draw(win)
    for en in enzyme_towers:
        en.draw(win)
    draw_ui(win, ui_level, selected_category, selected_tower_type)

    #money
    money_font = pygame.font.SysFont(None, 30)
    money_text = money_font.render(f"Money: ${MONEY}", True, BLACK)
    win.blit(money_text, (WIDTH - 150, HEIGHT - 40))

    #escaped
    escaped_font = pygame.font.SysFont(None, 30)
    escaped_text = escaped_font.render(f"Escaped_bectaria: {escaped_count}", True, BLACK)
    win.blit(escaped_text, (WIDTH-250, HEIGHT - 60))
    
    #holding
    if holding_tower:
        holding_tower.draw(win)

    pygame.display.update()

def main(win):

    #money
    MONEY = 100

    #stage
    stage = STAGE1
    #escaped
    escaped_count = 0

    run = True
    building_tower= False
    clock = pygame.time.Clock()

    ui_level = 1
    selected_category = None
    selected_tower_type = "Normal"
    
    enemies = []

    biofilm = []

    towers = []
    enzyme_towers = []

    bullets = []
    spawn_timer = 0
    UI_select_time = None
    holding_tower = None

    while run:
        clock.tick(FPS)

    #building_tower
        if building_tower and selected_tower_type != "":
            if selected_category == "A":
                tower_class = ANTIBIOTICS_TOWER[selected_tower_type]
                print("build")
                holding_tower = tower_class(mx, my)
            elif selected_category == "B":
                tower_class = ENZYME_TOWER[selected_tower_type]
                print("build")
                holding_tower = tower_class(mx, my)

        #UI check    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                y = HEIGHT - 50
                # 1
                if ui_level == 1:
                    #A.B
                    x = 10
                    for cat in CATEGORIES:
                        rect = pygame.Rect(x, y, 100, 40)
                        if rect.collidepoint((mx, my)):
                            selected_category = cat
                            ui_level = 2
                            selected_tower_type = ""
                            break
                        x += 110
                # 2
                elif ui_level == 2 and selected_category in CATEGORY_TO_ITEMS:    
                    back_rect = pygame.Rect(10, y - 45, 80, 35)
                    if back_rect.collidepoint((mx, my)):
                        ui_level = 1
                        selected_category = None
                        selected_tower_type = ""
                        holding_tower = None
                        building_tower = False
                        continue
                        # click tower
                    x = 10
                    items = CATEGORY_TO_ITEMS[selected_category]
                    for name in items:
                        rect = pygame.Rect(x, y, 100, 40)
                        if rect.collidepoint((mx, my)):
                            print(mx,my)
                            selected_tower_type = name
                            UI_select_time = pygame.time.get_ticks() + 1500  # 1.5sec
                            if selected_category == "A":
                                tower_class = ANTIBIOTICS_TOWER[selected_tower_type]
                            elif selected_category == "B":
                                tower_class = ENZYME_TOWER[selected_tower_type]
                            
                            holding_tower = tower_class(mx,my)
                            building_tower = True
                            break
                        x += 110

                        if holding_tower != None:
                            if selected_category == "A":
                                placing_tower = tower_class(mx, my)
                                towers.append(placing_tower)
                            elif selected_category == "B":
                                placing_tower = tower_class(mx, my)
                                enzyme_towers.append(placing_tower)

                            holding_tower = None
                            selected_tower_type = None
                            building_tower = False
                        

        # Check time ticks
        if UI_select_time and pygame.time.get_ticks() > UI_select_time:
            selected_tower_type = ""
            UI_select_time = None
        # holding_tower
        if holding_tower != None:
            holding_tower.x, holding_tower.y = pygame.mouse.get_pos()
        # Spawn enemies
        spawn_timer += 1
        if spawn_timer > 120:  # spawn every 2 seconds
            enemies.append(Enemy(PATH))
            spawn_timer = 0

        # Update enemies
        alive_enemies = []
        for e in enemies:
            alive = e.move()
            if not alive:
                if e.health > 0:
                    escaped_count += 1
            elif e.health > 0:
                alive_enemies.append(e)
            else:
                MONEY += 1
        enemies = alive_enemies


        
        # Towers shoot
        alive_towers = []
        for tower in towers:
            if tower.update():
                tower.shoot(enemies, bullets)
                alive_towers.append(tower)
        towers = alive_towers

        #Enzyme_tower aoe damage
        alive_enzyme_tower = []
        for enzyme_tower in enzyme_towers:
            if enzyme_tower.update():
                enzyme_tower.apply_area_damage(enemies)
                alive_enzyme_tower.append(enzyme_tower)
        enzyme_towers = alive_enzyme_tower

        # Update bullets
        new_bullets = []
        for bullet in bullets:
            if bullet.move():
                new_bullets.append(bullet)
        bullets = new_bullets


        if escaped_count >= stage:
            forming_biofilm = Biofilm(random.randint(10, MAP_WIDTH),random.randint(10, MAP_HEIGHT))
            biofilm.append(forming_biofilm)
            escaped_count = 0
            if len(biofilm) == 2:
                GAMERESTART = loss_screen()
                if GAMERESTART :
                    return
        for bi in biofilm:
            if bi != None:
                spawn_timer += 1
                if spawn_timer > 12:  # spawn every 2 seconds
                    enemies.append(Enemy(bi.myPath))
                    spawn_timer = 0
        # Draw everything
        draw_window(win, enemies, towers,enzyme_towers, bullets,selected_tower_type,MONEY,escaped_count,holding_tower,biofilm, ui_level, selected_category)

    pygame.quit()
