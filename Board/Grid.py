#!/usr/bin/python3
# Grid.py
import random

class Grid:
    def __init__(self):
        self.grid = [[[] for _ in list(range(4))] for _ in list(range(4))]
        self.unoccupied_ids = list(range(16))
        for i in list(range(random.randint(2,3))):
            self.__insert_new_randoms()
        print(self.unoccupied_ids)
    def __str__(self):
        str_out = ""
        for xs in self.grid:
            str_out += " \t".join(map(str, xs)) + "\n"
        return str_out
    def __insert_new_randoms(self):
        n = self.unoccupied_ids[random.randint(0, len(self.unoccupied_ids)-1)]
        self.unoccupied_ids.remove(n)
        self.grid[int(n/4)][n%4] = random.randint(1,2)*2
