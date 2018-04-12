import pygame
from random import randint
import sys
import time

from pygame.locals import *
from utils import remap

WIDTH = 640
HEIGHT = 360
FPS = 30

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
FPSCLOCK = pygame.time.Clock()

RAIN_COLOR = (138, 43, 226)
BG_COLOR = (230, 230, 250)


def setup():
    pygame.init()
    pygame.display.set_caption('Purple Rain')


class Drop:

    def __init__(self):
        self.x = randint(0, WIDTH)
        self.y = randint(-HEIGHT, 0)
        self.z = randint(1, 20)

        self.length = remap(self.z, 0, 20, 10, 20)
        self.yspeed = remap(self.z, 0, 20, 1, 20)

    def fall(self):
        self.y += self.yspeed
        grav = remap(self.z, 0, 20, 0, 0.2)
        self.yspeed += grav

        if self.y > HEIGHT:
            self.y = randint(-HEIGHT, 0)
            self.yspeed = remap(self.z, 0, 20, 1, 20)

    def show(self):
        thickness = int(remap(self.z, 0, 20, 1, 3))
        pygame.draw.line(DISPLAY, RAIN_COLOR,
                         (self.x, self.y), (self.x, self.y + self.length), thickness)


def main():
    setup()

    drops = [Drop() for x in range(500)]

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print('Exiting...')
                pygame.quit()
                sys.exit()

        DISPLAY.fill(BG_COLOR)
        for drop in drops:
            drop.fall()
            drop.show()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
