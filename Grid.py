#!/usr/bin/python3
# Grid.py
import random

class Grid:
    def __init__(self):
        self.grid = [[] for _ in list(range(4))] for _ in list(range(4))
        for i in list(range(random.randint(2,3))):
            n = random.randint(0, 15)
            self.grid[int(n/4)][n%4] = random.randint(1,2)*2
    def __str__(self):
        for xs in self.grid:
            print(" \t".join(map(str, xs)))
