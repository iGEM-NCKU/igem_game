import pygame
from Tower import Tower
from Enemy import Enemy

from config import FPS, HEIGHT, WIDTH, TOWER_TYPES, WHITE, GREEN, BLACK, PATH

pygame.init()
background_image = pygame.transform.scale(pygame.image.load("src/background.jpg"),(WIDTH,HEIGHT))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Tower Defense")

def draw_window(win, enemies, towers, bullets, selected_tower_type,MONEY,escaped_count):
    win.fill((200, 200, 200))
    for p in PATH:
        pygame.draw.circle(win, BLACK, p, 5)
    for e in enemies:
        e.draw(win)
    for t in towers:
        t.draw(win)
    for b in bullets:
        b.draw(win)
    draw_ui(win, selected_tower_type)

    #money
    money_font = pygame.font.SysFont(None, 30)
    money_text = money_font.render(f"Money: ${MONEY}", True, BLACK)
    win.blit(money_text, (WIDTH - 150, HEIGHT - 40))

    #escaped
    escaped_font = pygame.font.SysFont(None, 30)
    escaped_text = escaped_font.render(f"Escaped_bectaria: {escaped_count}", True, BLACK)
    win.blit(escaped_text, (WIDTH-250, HEIGHT - 60))

    pygame.display.update()

def draw_ui(win, selected_tower_type):
    y = HEIGHT - 50
    x = 10
    mouse_pos = pygame.mouse.get_pos()

    for name in TOWER_TYPES:
        rect = pygame.Rect(x, y, 100, 40)
        if rect.collidepoint(mouse_pos):
            color = (144, 255, 144)
        if selected_tower_type == name:
            color = GREEN  
        if not rect.collidepoint(mouse_pos) and selected_tower_type != name:
            color = WHITE  

        pygame.draw.rect(win, color, rect)
        pygame.draw.rect(win, BLACK, rect, 2)
        font = pygame.font.SysFont(None, 24)
        text = font.render(name, True, BLACK)
        win.blit(text, (x + 10, y + 10))
        x += 110

def main_menu():
    menu_run = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None,48)
    button_font = pygame.font.SysFont(None,36)
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
    quit_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 +100, 200, 50)

    while menu_run:
        clock.tick(FPS)
        WIN.blit(background_image,(0,0))

        title = font.render("NCKU_iGEM_Game",True, BLACK)
        WIN.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 100))

        mouse_pos = pygame.mouse.get_pos()

        if button_rect.collidepoint(mouse_pos):
            button_color = GREEN
        else:
            button_color = WHITE
        if quit_button_rect.collidepoint(mouse_pos):
            quit_button_color = GREEN
        else:
            quit_button_color = WHITE
        # Draw start button
        pygame.draw.rect(WIN, button_color, button_rect)
        pygame.draw.rect(WIN, BLACK, button_rect, 5)
        button_text = button_font.render("Start Game", True, BLACK)
        WIN.blit(button_text, (button_rect.x + 40, button_rect.y + 10))
       
        # Draw quit button
        pygame.draw.rect(WIN, quit_button_color, quit_button_rect)
        pygame.draw.rect(WIN, BLACK, quit_button_rect, 5)
        quit_button_text = button_font.render("Quit", True, BLACK)
        WIN.blit(quit_button_text,(quit_button_rect.x + 70, quit_button_rect.y +10))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    menu_run = False
                elif quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()
def main():

    #money
    MONEY = 100

    #escaped
    escaped_count = 0

    run = True
    building_tower= False
    clock = pygame.time.Clock()

    selected_tower_type = "Normal"
    enemies = []
    towers = [Tower(300, 400), Tower(500, 300)]
    bullets = []
    spawn_timer = 0
    UI_select_time = None
    while run:
        clock.tick(FPS)

        #UI check    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                x = 10
                y = HEIGHT - 50
                for name in TOWER_TYPES:
                    rect = pygame.Rect(x, y, 100, 40)
                    if rect.collidepoint((mx, my)):
                        print(mx,my)
                        selected_tower_type = name
                        UI_select_time = pygame.time.get_ticks() + 1500  # 1.5sec
                        building_tower = True
                        break
                    x += 110

                #building_tower
                if building_tower and selected_tower_type != "":
                        tower_info = TOWER_TYPES[selected_tower_type]
                        print("build")

                        building_tower = False
        # Check time ticks
        if UI_select_time and pygame.time.get_ticks() > UI_select_time:
            selected_tower_type = ""
            UI_select_time = None

        # Spawn enemies
        spawn_timer += 1
        if spawn_timer > 12:  # spawn every 2 seconds
            enemies.append(Enemy())
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
        for tower in towers:
            tower.shoot(enemies, bullets)

        # Update bullets
        new_bullets = []
        for bullet in bullets:
            if bullet.move():
                new_bullets.append(bullet)
        bullets = new_bullets

        # Draw everything
        draw_window(WIN, enemies, towers, bullets,selected_tower_type,MONEY,escaped_count)
        
    pygame.quit()

if __name__ == "__main__":
    main_menu()
    main()
