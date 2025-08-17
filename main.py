import pygame
import random

from Tower import ANTIBIOTICS_TOWER
from Enemy import ENEMY_TYPE
from Biofilm import Biofilm
from Loss_screen import loss_screen
from config import FPS, HEIGHT, WIDTH,WHITE,YELLOW, PATH, STAGE1, GENERATION_WEIGHTS_STAGE_1
from Enzyme_tower import ENZYME_TOWER
from draw_ui import draw_ui, CATEGORIES, CATEGORY_TO_ITEMS
from map import GRID_SIZE, map_data, Tile, TILE_MAP_HEIGHT, TILE_MAP_WIDTH

pygame.mixer.init()
shot_fx = pygame.mixer.Sound('src/audio/shot.wav')

def draw_window(win, enemies, towers, enzyme_towers, bullets, selected_tower_type,MONEY,escaped_count,holding_tower,biofilm,ui_level, selected_category,minus_heart,map_tiles):
    win.fill((200, 200, 200))
    mx, my = pygame.mouse.get_pos()
    for row in map_tiles:
        for tile in row:
            tile.draw(win)

    for e in enemies:
        enemy_messege = f"{e.name}\nPolysac: {e.polysac}/{e.max_polysac}\nDNA Membrane: {e.Dna_membrane}/{e.max_Dna_membrane}\nProtein Membrane: {e.protein_membrane}/{e.max_protein_membrane}"
        e.draw(enemy_messege, win, mx,my)
    for t in towers:
        t.draw(win, mx, my)
    for b in bullets:
        b.draw(win)
    for bi in biofilm:
        bi.draw(win)
    for en in enzyme_towers:
        en.draw(win, mx, my)
    draw_ui(win, ui_level, selected_category, selected_tower_type,minus_heart)

    #money
    money_font = pygame.font.SysFont(None, 30)
    money_text = money_font.render(f"Money: ${MONEY}", True, YELLOW)
    win.blit(money_text, (WIDTH - 150, HEIGHT - 40))

    #escaped
    escaped_font = pygame.font.SysFont(None, 30)
    escaped_text = escaped_font.render(f"Escaped_bectaria: {escaped_count}", True, WHITE)
    win.blit(escaped_text, (WIDTH-250, HEIGHT - 60))
    
    #holding
    if holding_tower:
        holding_tower.draw(win,mx,my)

    pygame.display.update()

def main(win):
    #map
    map_tiles = [[Tile(col, row, map_data[row][col]) for col in range(TILE_MAP_WIDTH)] for row in range(TILE_MAP_HEIGHT)]

    #money
    MONEY = 100

    #escaped
    escaped_count = 0
    minus_heart = 0

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
                holding_tower = tower_class(tile_px, tile_py)
            elif selected_category == "B":
                tower_class = ENZYME_TOWER[selected_tower_type]
                print("build")
                holding_tower = tower_class(tile_px, tile_py)

        #UI check    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                grid_x, grid_y = get_grid_pos(mx, my)
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
                            tile_px, tile_py = grid_x * GRID_SIZE+ GRID_SIZE // 2, grid_y * GRID_SIZE+ GRID_SIZE // 2
                            holding_tower = tower_class(tile_px,tile_py)
                            building_tower = True
                            break
                        x += 110

                        if holding_tower != None:
                            tile_px, tile_py = grid_x * GRID_SIZE+ GRID_SIZE // 2, grid_y * GRID_SIZE+ GRID_SIZE // 2
                            row, col = get_tile_index(tile_px, tile_py)
                            tile = map_tiles[row][col]
                            if selected_category == "A" and not tile.is_path():
                                    placing_tower = tower_class(tile_px, tile_py)
                                    towers.append(placing_tower)
                            elif selected_category == "B" and not tile.is_path():
                                    placing_tower = tower_class(tile_px, tile_py)
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
            enemy_cls = random.choices(ENEMY_TYPE, weights =GENERATION_WEIGHTS_STAGE_1,k=1)[0] #return list[0]
            new_enemy = enemy_cls(PATH)
            enemies.append(new_enemy)
            spawn_timer = 0

        # Update enemies
        alive_enemies = []
        for e in enemies:
            alive = e.move()
            if not alive:
                if e.check_death() == False:
                    escaped_count += e.damage
                else:
                    MONEY += 1
            elif e.check_death() == False:
                alive_enemies.append(e)
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

        if escaped_count >= STAGE1["hearts"]:
            while True:
                row = random.randint(0, TILE_MAP_HEIGHT - 1)
                col = random.randint(0, TILE_MAP_WIDTH - 1)
                tile = map_tiles[row][col]
                if not tile.is_path(): 
                    break
            x = col * GRID_SIZE + GRID_SIZE // 2
            y = row * GRID_SIZE + GRID_SIZE // 2
            forming_biofilm = Biofilm(x, y)
            biofilm.append(forming_biofilm)
            minus_heart += 1
            escaped_count = 0
            if len(biofilm) == STAGE1["hearts"]:
                GAMERESTART = loss_screen()
                if GAMERESTART :
                    return
        for bi in biofilm:
             if bi != None:
                 spawn_timer += 1
                 if spawn_timer > bi.getTowerCooldown():  # spawn every 2 seconds
                    enemy_cls = random.choices(ENEMY_TYPE, weights =GENERATION_WEIGHTS_STAGE_1,k=1)[0] #return list[0]
                    new_enemy = enemy_cls(bi.myPath)
                    enemies.append(new_enemy)
                    spawn_timer = 0
        # Draw everything
        draw_window(win, enemies, towers,enzyme_towers, bullets,selected_tower_type,MONEY,escaped_count,holding_tower,biofilm, ui_level, selected_category,
                    minus_heart,map_tiles)

    pygame.quit()


def generate_enemy():
    enemy_class = random.choices(ENEMY_TYPE, weights=GENERATION_WEIGHTS_STAGE_1, k=1)[0]
    return enemy_class() 
def get_grid_pos(x, y):
    return x // GRID_SIZE, y // GRID_SIZE

def get_tile_index(mx, my):
    col = mx // GRID_SIZE
    row = my // GRID_SIZE
    return row, col