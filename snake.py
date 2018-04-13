import pygame
from random import randint
from math import floor, hypot
import os
import sys
import time

from pygame.locals import *
from utils import constrain


WIDTH = 600
HEIGHT = 600
FPS = 10


DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
FPSCLOCK = pygame.time.Clock()

BG_COLOR = (51, 51, 51)
WHITE = (255, 255, 255)

SCALE = 20


def keyPressed(snake):
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        snake.dir(0, -1)
    elif keys[K_DOWN]:
        snake.dir(0, 1)
    elif keys[K_RIGHT]:
        snake.dir(1, 0)
    elif keys[K_LEFT]:
        snake.dir(-1, 0)


class Food:

    def __init__(self):
        col = floor(WIDTH / SCALE)
        row = floor(HEIGHT / SCALE)
        self.x = floor(randint(0, col)) * SCALE
        self.y = floor(randint(0, row)) * SCALE
        self.x = constrain(self.x, 0, WIDTH - SCALE)
        self.y = constrain(self.y, 0, HEIGHT - SCALE)

    def show(self):
        COLOR = (255, 0, 100)
        pygame.draw.rect(DISPLAY, COLOR, (self.x, self.y, SCALE, SCALE))


class Snake:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_dir = 1
        self.y_dir = 0
        self.total = 0
        self.tail = [(self.x, self.y)]

    def update(self):
        self.tail.append((self.x, self.y))

        self.x += self.x_dir * SCALE
        self.y += self.y_dir * SCALE

        self.x = constrain(self.x, 0, WIDTH - SCALE)
        self.y = constrain(self.y, 0, HEIGHT - SCALE)

        while len(self.tail) > self.total + 1:
            self.tail.pop(0)

    def show(self):
        for x, y in self.tail:
            pygame.draw.rect(DISPLAY, WHITE, (x, y, SCALE, SCALE))

    def dir(self, x, y):
        self.x_dir = x
        self.y_dir = y

    def death(self):
        if len(set(self.tail)) != len(self.tail):
            return True
        elif self.x > WIDTH or self.x < 0:
            return True
        elif self.y > HEIGHT or self.y < 0:
            return True

    def eat(self, food):
        if hypot(food.x - self.x, food.y - self.y) == 0:
            self.total += 1
            return True
        else:
            return False


def setup():
    pygame.init()
    pygame.display.set_caption('Snake')


def main():
    setup()

    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print('Exiting...')
                pygame.quit()
                sys.exit()

        DISPLAY.fill(BG_COLOR)
        keyPressed(snake)
        snake.update()
        snake.show()
        food.show()
        if snake.eat(food):
            food = Food()

        if snake.death():
            snake = Snake()
            food = Food()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
