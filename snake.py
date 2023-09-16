import pygame
from settings import *
import random
from pygame.math import Vector2



class Snake(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()


        self.image = pygame.Surface((SIZE, SIZE)) # rectangle size
        self.snake_color = self.image.fill((74, 141, 176))
        #self.rect = self.image.get_rect()
        self.direction = (0,0)
        self.speed = 1
        self.display_surface = pygame.display.get_surface()

        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]


    def draw(self, surface):
        for block in self.body:
          block_rect = pygame.Rect(int(block.x * SIZE), int(block.y * SIZE), SIZE, SIZE)
          pygame.draw.rect(screen, (74, 141, 176), block_rect)


    def input(self):
        keys = pygame.key.get_pressed()
        move_dirs = {pygame.K_DOWN: (0, 1), pygame.K_UP: (0, -1), pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0)}

        for key, value in move_dirs.items():
            if keys[key]:
                self.direction = value

    def move(self):
        body_imitate = self.body[:-1]  #ignores last vector in list so its deleted
        body_imitate.insert(0, body_imitate[0] + self.direction) # new head is made at index 0 which is the previous position plus direction
        self.body = body_imitate[:]


        #self.rect.x += self.direction[0] * self.speed #added
        #self.rect.y += self.direction[1] * self.speed # added

        # this should handle wrapping the screen horizontally
        """
        if self.rect.left > WIDTH:
            self.rect.right = 0 # added
        if self.rect.right < 0:
            self.rect.left = WIDTH #added

        #likewise but vertically

        if self.rect.top > HEIGHT:
            self.rect.bottom = 0 #added
        if self.rect.bottom < 0:
             self.rect.top = HEIGHT
        """

    def add_nodes(self, node):
      pass

    def update(self):
        self.input()
        self.draw(self.display_surface)

class Fruit(pygame.sprite.Sprite):

    def __init__(self, color):

        super().__init__()
        # random generated coordinates

        self.x = random.randint(0, cell_number)
        self.y = random.randint(0, cell_number)
        """
        self.pos = Vector2(self.x, self.y)
        self.color = color

        self.rect = pygame.Rect(self.pos.x * SIZE, self.pos.y * SIZE, SIZE, SIZE)
        #self.rect.center = (self.x, self.y)
        """
        #self.x = 5
        #self.y = 4
        self.pos = Vector2(self.x, self.y)
        self.color = color

    def draw(self, surface):
       # surface.blit(self.fruit_image, self.rect)
        #pygame.draw.rect(surface, self.color, self.rect)
        fruit_rect = pygame.Rect(int(self.pos.x * SIZE), int(self.pos.y * SIZE), SIZE, SIZE)
        pygame.draw.rect(screen, self.color, fruit_rect)
