import pygame
# just easier to manage if I leave them here

WIDTH = 500
HEIGHT = 500
SIZE = 25
FPS = 60
cell_number = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
