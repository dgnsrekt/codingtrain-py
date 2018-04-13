import pygame
from random import randint
import os
import sys
import time

from pygame.locals import *
from utils import remap


WIDTH = 800
HEIGHT = 800
FPS = 30


DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
FPSCLOCK = pygame.time.Clock()

BG_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)
STARS = 800


class Star:

    def __init__(self):
        self.x = randint(-WIDTH, WIDTH)
        self.y = randint(-HEIGHT, HEIGHT)
        self.z = randint(0, WIDTH)
        self.pz = self.z

    def update(self):
        mouse = pygame.mouse.get_pos()[1]
        self.z -= remap(mouse, WIDTH / 2, WIDTH, 25, 1)
        if self.z < 1:
            self.x = randint(-WIDTH, WIDTH)
            self.y = randint(-HEIGHT, HEIGHT)
            self.z = randint(0, WIDTH)
            self.pz = self.z

    def show(self):
        try:
            k = (WIDTH / 2) / self.z
        except ZeroDivisionError:
            self.z = randint(WIDTH / 2, WIDTH)
            k = (WIDTH / 2) / self.z

        sx = int(self.x * k + WIDTH / 2)
        sy = int(self.y * k + HEIGHT / 2)
        r = int(remap(self.z, 0, WIDTH, 3, 0))
        pygame.draw.circle(DISPLAY, WHITE, (sx, sy), r)

        try:
            k = (WIDTH / 2) / self.pz
        except ZeroDivisionError:
            self.pz = self.z
            k = (WIDTH / 2) / self.pz

        px = int(self.x * k + WIDTH / 2)
        py = int(self.y * k + HEIGHT / 2)
        self.pz = self.z

        pygame.draw.line(DISPLAY, WHITE, (px, py), (sx, sy))


def setup():
    pygame.init()
    pygame.display.set_caption('Starfield')


def main():
    setup()

    stars = [Star() for x in range(STARS)]

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print('Exiting...')
                pygame.quit()
                sys.exit()

        DISPLAY.fill(BG_COLOR)

        for star in stars:
            star.show()
            star.update()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
