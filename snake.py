import pygame


class Snake(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((10, 10)) # rectangle size
        self.image.fill((74, 141, 176))

        self.rect = self.image.get_rect()
        self.hitbox = self.rect.inflate(0, -26)

        # will be used for movement
        self.direction = pygame.math.Vector2()
        self.speed = 4


    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            print('you pressed up')


    def update(self):
        self.input()
