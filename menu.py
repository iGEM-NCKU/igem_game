import pygame

from config import WIDTH, HEIGHT, FPS, BLACK, GREEN, WHITE, BACKGROUND_IMAGE

background_image = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE),(WIDTH,HEIGHT))

def main_menu(WIN):
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