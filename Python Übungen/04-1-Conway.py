# Aufgabe:  Conway's Game of Life
from os import system, name
from time import sleep

import random


class Grid:
    def __init__(self, width, height, alive_sign, dead_sign):
        self.width = width
        self.height = height
        self.alive_sign = alive_sign
        self.dead_sign = dead_sign

        # Erstelle das Spielfeld mit der Größe und fülle alles mit 0
        self.grid = [[random.getrandbits(1) for _ in range(width)] for _ in range(height)]

    def draw(self):
        clear_console()
        for line in self.grid:
            print([self.alive_sign if x == 1 else self.dead_sign for x in line])

    def tick(self):
        new_grid = [[0 for _ in range(width)] for _ in range(height)]
        for x in range(self.width):
            for y in range(self.height):
                value = self.grid[y][x]
                live = self.get_live_neighbours(x,y)

                # Regel 1
                if value == 0 and live == 3:
                    new_grid[y][x] = 1
                # Regel 2
                elif value == 1 and live < 2:
                    new_grid[y][x] = 0
                # Regel 3
                elif value == 1 and 2 <= live <= 3:
                    new_grid[y][x] = value
                # Regel 4
                elif value == 1 and live > 3:
                    new_grid[y][x] = 0

        self.grid = new_grid

def get_live_neighbours(self, x, y):
    live = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                pass
            else:
                if 0 <= x+i <= self.width - 1\
                    and  0 <= y+j <= self.height - 1:
                    live += self.grid[y+j][x+i]
    return live


def clear_console():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac und Linux (name == 'posix')
    else:
        _ = system('clear')


width = int(input("Width: "))
height = int(input("Height: "))

grid = Grid(width, height, '█', '░')

while True:
    grid.tick()
    grid.draw()
    sleep(1)