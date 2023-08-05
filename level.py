import pygame
from snake import *


class Level:

    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.snake = Snake()




    def run(self):

        self.display_surface.fill((255, 183, 94))
        self.display_surface.blit(self.snake.image, self.snake.rect)

        self.snake.update()# calling our snake classes update method which calls other methods responsible for moving it

