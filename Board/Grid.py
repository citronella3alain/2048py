#!/usr/bin/python3
# Grid.py
import random

class Grid:
    def __init__(self):
        self.grid = [[[] for _ in list(range(4))] for _ in list(range(4))]
        self.unoccupied_ids = list(range(16))
        for i in list(range(random.randint(2,3))):
            self.insert_new_randoms()
    def __str__(self):
        str_out = ""
        for xs in self.grid:
            str_out += " \t".join(map(str, xs)) + "\n"
        return str_out
    def __eq__(self, other):
        #compare based on grids
        return self.grid == other.grid
    def insert_new_randoms(self):
        n = self.unoccupied_ids[random.randint(0, len(self.unoccupied_ids)-1)]
        self.unoccupied_ids.remove(n)
        self.grid[int(n/4)][n%4] = random.randint(1,2)*2
    def update_unoccupied_ids(self):
        self.unoccupied_ids = list(range(16))
        for i in list(range(len(self.grid))):
            for j in list(range(len(self.grid[i]))):
                if (self.grid[i][j]):
                    self.unoccupied_ids.remove(4*i+j)
    def shift_x(self, direction):
        #unit direction
        direction = int(direction/abs(direction))
        #positive direction shifts right 
        #negative & 0 direction shifts left
        #merges blocks if their values are equal
        for i in list(range(len(self.grid))):
            line = self.grid[i]
            if (direction <= 0):
                line.reverse()
            elements = []
            for j in list(range(len(line))):
                element = line[j]
                if element:
                    elements.append(element)
                    if (len(elements) > 1 and elements[-1] == elements[-2]):
                        elements.append(elements.pop() + elements.pop())
            if (direction <= 0):
                elements = elements[::-1] + [[] for _ in list(range(len(line)-len(elements)))]
            else:
                elements = [[] for _ in list(range(len(line)-len(elements)))] + elements
            self.grid[i] = elements
    def shift_y(self, direction):
        direction = int(direction/abs(direction))
        collection = [[] for _ in list(range(len(self.grid)))]
        for row in self.grid:
            for i in list(range(len(row))):
                if (row[i]):
                    if (direction > 0):
                        collection[i].append(row[i])
                        if (len(collection[i]) > 1 and collection[i][-1] == collection[i][-2]):
                            collection[i].append(collection[i].pop() + collection[i].pop())
                    else:
                        collection[i].insert(0, row[i])
                        if (len(collection[i]) > 1 and collection[i][0] == collection[i][1]):
                            collection[i].insert(0, collection[i].pop(0) + collection[i].pop(0))
        #insert blank lists
        for i in list(range(len(collection))):
            if (direction <= 0):
                collection[i] = [[] for _ in list(range(len(self.grid)-len(collection[i])))] + collection[i][::-1]
            else:
                collection[i] = collection[i] + [[] for _ in list(range(len(self.grid)-len(collection[i])))]
        for i in list(range(len(self.grid))):
            for j in list(range(len(self.grid[i]))):
                self.grid[i][j] = collection[j][i]
