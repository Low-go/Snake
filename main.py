import pygame, sys
from level import *
from settings import *

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        #hdihdihds

        self.level = Level()



    def run(self): #basic game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == SCREEN_UPDATE:

                    self.level.snake.move()

            screen.fill('black')
            self.level.run()

            pygame.display.update()
            self.clock.tick(FPS)   # should regulate our frames per second


if __name__ == '__main__':
    game = Game()
    game.run()