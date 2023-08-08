import pygame
from settings import *
import random

class Snake(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((SIZE, SIZE)) # rectangle size
        self.image.fill((74, 141, 176))

        self.rect = self.image.get_rect()
        #self.hitbox = self.rect.inflate(0, -26)

        # will be used for movement
        self.direction = (0,0)
        self.speed = 2


    def input(self):
        keys = pygame.key.get_pressed()
        move_dirs = {pygame.K_DOWN: (0, 1), pygame.K_UP: (0, -1), pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0)}

        for key,value in move_dirs.items():
            if keys[key]:
                self.direction = value

    def move(self):
        #self.hitbox.x += self.direction[0] * self.speed
        #self.hitbox.y += self.direction[1] * self.speed
        #self.rect.center = self.hitbox.center
        self.rect.x += self.direction[0] * self.speed #added
        self.rect.y += self.direction[1] * self.speed # added

        # this should handle wrapping the screen horizontally

        if self.rect.left > WIDTH:
            #self.hitbox.right = 0
            #self.rect.center = self.hitbox.center
            self.rect.right = 0 # added
        if self.rect.right < 0:
            #self.hitbox.left = WIDTH
            #self.rect.center = self.hitbox.center
            self.rect.left = WIDTH #added

        #likewise but vertically

        if self.rect.top > HEIGHT:
            #self.hitbox.bottom = 0
            #self.rect.center = self.hitbox.center
            self.rect.bottom = 0 #added
        if self.rect.bottom < 0:
           # self.hitbox.top = HEIGHT
           # self.rect.center = self.hitbox.center
             self.rect.top = HEIGHT

    def update(self):
        self.input()
        self.move()

class Fruit(pygame.sprite.Sprite):

    def __init__(self, color):

        super().__init__()
        # random generated coordinates
        self.x = random.randint(0, WIDTH - SIZE)
        self.y = random.randint(0, HEIGHT - SIZE)
        self.fruit_image = pygame.Surface((SIZE, SIZE))
        self.color = color

        self.fruit_image.fill(self.color) # should choose a random color
        self.rect = self.fruit_image.get_rect()
        self.rect.center = (self.x, self.y)
        #self.hitbox = self.rect.inflate(0, -26)


    def draw(self, surface):
        surface.blit(self.fruit_image, self.rect)