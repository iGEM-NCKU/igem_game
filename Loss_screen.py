import pygame
import sys

from config import WIDTH, HEIGHT, RED

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Loss Screen")


def loss_screen():
    font = pygame.font.SysFont(None, 80)
    small_font = pygame.font.SysFont(None, 40)
    clock = pygame.time.Clock()
    while True:
        screen.fill(RED)
        loss_text = font.render("YOU LOST!", True, (255, 255, 255))
        restart_text = small_font.render("Press R to Restart or Q to Quit", True, (200, 200, 200))

        screen.blit(loss_text, (WIDTH // 2 - loss_text.get_width() // 2, HEIGHT // 2 - 100))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    return True

        pygame.display.flip()
        clock.tick(60)