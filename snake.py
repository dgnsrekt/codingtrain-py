import pygame
from random import randint
import os
import sys
import time

from pygame.locals import *
from utils import remap


WIDTH = 600
HEIGHT = 600
FPS = 30


DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
FPSCLOCK = pygame.time.Clock()

BG_COLOR = (51, 51, 51)
WHITE = (255, 255, 255)


def setup():
    pygame.init()
    pygame.display.set_caption('Snake')


def main():
    setup()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print('Exiting...')
                pygame.quit()
                sys.exit()

        DISPLAY.fill(BG_COLOR)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
