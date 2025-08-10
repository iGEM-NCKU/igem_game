import pygame
from config import WIDTH, HEIGHT
from main import main
from menu import main_menu

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Simple Tower Defense")


if __name__ == "__main__":
    main_menu(WIN)
    main(WIN)
