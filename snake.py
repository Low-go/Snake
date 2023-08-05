import pygame
from settings import *


class Snake(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((10, 10)) # rectangle size
        self.image.fill((74, 141, 176))

        self.rect = self.image.get_rect()
        self.hitbox = self.rect.inflate(0, -26)

        # will be used for movement
        self.direction = (0,0)
        self.speed = 2


    def input(self):
        keys = pygame.key.get_pressed()

        """
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        #else:
        #    self.direction.y = 0    there is always movment in snake, I shouldn't allow it to stand still

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        """

        """New code should make it so only one key pressed can be true. allowing one movment
         and making sure that no diagonal movments are allowed"""
        move_dirs = {pygame.K_DOWN: (0, 1), pygame.K_UP: (0, -1), pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0)}

        for key,value in move_dirs.items():
            if keys[key]:
                self.direction = value




    def move(self):
        self.hitbox.x += self.direction[0] * self.speed
        self.hitbox.y += self.direction[1] * self.speed
        self.rect.center = self.hitbox.center

        # this should handle wrapping the screen horizontally

        if self.rect.left > WIDTH:
            self.hitbox.right = 0
            self.rect.center = self.hitbox.center
        if self.rect.right < 0:
            self.hitbox.left = WIDTH
            self.rect.center = self.hitbox.center

        #likewise but vertically

        if self.rect.top > HEIGHT:
            self.hitbox.bottom = 0
            self.rect.center = self.hitbox.center
        if self.rect.bottom < 0:
            self.hitbox.top = HEIGHT
            self.rect.center = self.hitbox.center

    def update(self):
        self.input()
        self.move()

