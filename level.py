import pygame
from snake import *

class Level:

    fruit_there = False
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.snake = Snake()

        self.fruit_interval = 4000
        self.last_fruit_time = pygame.time.get_ticks()   # start a timer
        self.fruits = None

    def run(self):

        self.display_surface.fill((255, 183, 94))
        self.fruit_creation() # putting this here allows my snake to be drawn over
        self.display_surface.blit(self.snake.image, self.snake.rect)
        self.snake.update()# calling our snake classes update method which calls other methods responsible for moving it
        self.collision()


    def fruit_creation(self):
        current_time = pygame.time.get_ticks()
        color = ['red', 'blue', 'green', 'yellow', 'black']

        if current_time - self.last_fruit_time >= self.fruit_interval and  Level.fruit_there == False:

            new_fruit = Fruit(random.choice(color))
            self.fruits = new_fruit   #test
            self.last_fruit_time = current_time


            Level.fruit_there = True

        if self.fruits: #test
           self.fruits.draw(self.display_surface)

    def collision(self):
        if self.fruits and self.snake.rect.colliderect(self.fruits.rect):
            self.fruits = None
            Level.fruit_there = False

