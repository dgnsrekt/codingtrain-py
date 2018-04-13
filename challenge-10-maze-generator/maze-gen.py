import pygame
from random import randint, choice
from math import floor
import os
import sys
import time

from pygame.locals import *


WIDTH = 400
HEIGHT = 400
FPS = 30

DISPLAY = pygame.display.set_mode((WIDTH + 1, HEIGHT + 1))
FPSCLOCK = pygame.time.Clock()

BG_COLOR = (51, 51, 51)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255, 1)

W = 10

ROWS = floor(WIDTH/W)
COLS = floor(HEIGHT/W)


def index(row, col):
    if row < 0:
        return None
    if col < 0:
        return None
    if row > ROWS-1:
        return None
    if col > COLS-1:
        return None
    return row * ROWS + col


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.walls = {'Top': True, 'Right': True, 'Bottom': True,
                      'Left': True}  # top, right, bottom, left

        self.visited = False
        self.neigbors = {}

    def highlight(self):
        x = self.row * W
        y = self.col * W

        pygame.draw.rect(DISPLAY, PURPLE, (x, y, W-2, W-2), 1)

    def show(self):
        x = self.row * W
        y = self.col * W

        lines = {'Top': [(x, y), (x+W, y)],
                 'Right': [(x+W, y), (x+W, y+W)],
                 'Bottom': [(x+W, y+W), (x, y+W)],
                 'Left': [(x, y+W), (x, y)]}

        for wall in self.walls:
            if self.walls[wall]:
                pygame.draw.lines(DISPLAY, WHITE, True, lines[wall])

        # if self.visited:
            # pygame.draw.rect(DISPLAY, PURPLE, (x, y, W-2, W-2), 1)

    def checkNeigbors(self, grid):
        try:
            top = grid[index(self.row-1, self.col)]
            # print('top', top.visited, top)
            if top:
                if not top.visited:
                    self.neigbors['Top'] = top
        except TypeError:
            pass

        try:
            right = grid[index(self.row, self.col+1)]
            # print('right', right.visited, right)
            if right:
                if not right.visited:
                    self.neigbors['Right'] = right
        except TypeError:
            pass

        try:
            bottom = grid[index(self.row+1, self.col)]
            # print('bottom', bottom.visited, bottom)
            if bottom:
                if not bottom.visited:
                    self.neigbors['Bottom'] = bottom
        except TypeError:
            pass

        try:
            left = grid[index(self.row, self.col-1)]
            # print('left', left.visited, left)
            if left:
                if not left.visited:
                    self.neigbors['Left'] = left
        except TypeError:
            pass

        print(self.neigbors)
        if len(self.neigbors) > 0:
            wall = choice(list(self.neigbors.keys()))
            return self.neigbors[wall]
        else:
            return None

    def __repr__(self):
        return '(row:{}, col:{})'.format(self.row, self.col)


GRID = [Cell(row, col) for row in range(0, ROWS) for col in range(0, COLS)]


def removeWalls(a, b):
    x = a.row - b.row
    if x == 1:
        a.walls['Left'] = False
        b.walls['Right'] = False
    elif x == -1:
        a.walls['Right'] = False
        b.walls['Left'] = False
    y = a.col - b.col
    if y == 1:
        a.walls['Top'] = False
        b.walls['Bottom'] = False
    elif y == -1:
        a.walls['Bottom'] = False
        b.walls['Top'] = False


def setup():
    pygame.init()
    pygame.display.set_caption('Snake')


def main():
    setup()
    current_cell = GRID[0]

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print('Exiting...')
                pygame.quit()
                sys.exit()

        DISPLAY.fill(BG_COLOR)
        for cell in GRID:
            cell.show()

        current_cell.visited = True
        current_cell.highlight()
        next_cell = current_cell.checkNeigbors(GRID)

        if next_cell:
            next_cell.visited = True

            removeWalls(current_cell, next_cell)

            current_cell = next_cell

            print('current', current_cell)
            print('next', next_cell)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


main()
