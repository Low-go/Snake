import pygame, sys
from level import *

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 600))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

        self.level = Level()



    def run(self): #basic game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(60)   # should regulate our frames per second


if __name__ == '__main__':
    game = Game()
    game.run()