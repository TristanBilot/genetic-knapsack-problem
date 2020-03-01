import numpy as np
import random
import math

class DNA():
    def __init__(self, objects, MAX_WEIGHT, values_sum, mutation_rate):
        self.initial_objetcs = objects
        self.objects = objects
        self.values_sum = values_sum
        self.MAX_WEIGHT = MAX_WEIGHT
        self.mutation_rate = mutation_rate
        np.random.shuffle(self.objects)

        self.fitness = 0
        self.usedSpace = 0
        self.value = 0
        self.c_fitness()

    def c_fitness(self):
        w = 0
        v = 0
        for i in range(0, len(self.objects)):
            if w + self.objects[i]['weight'] <= self.MAX_WEIGHT:
                w += self.objects[i]['weight']
                v += self.objects[i]['value']
            else:
                break
        self.value = v
        self.usedSpace = w
        self.fitness = v / self.values_sum

    def crossover(self, partner):
        objects = []
        i = 0
        while (len(objects) < len(self.objects)):
            if random.randint(0, 1) < 0.5 and self.objects[i] not in objects:
                objects.append(self.objects[i])
            elif partner.objects[i] not in objects:
                objects.append(partner.objects[i])
            i += 1
            if i == len(self.objects):
                i = 0
        return DNA(objects, self.MAX_WEIGHT, self.values_sum, self.mutation_rate)

    def mutate(self):
        l = len(self.objects)
        for i in range(l):
            swap = random.randint(math.floor(l / 2), l - 1)
            if random.random() < self.mutation_rate:
                tmp = self.objects[i]
                self.objects[i] = self.objects[swap]
                self.objects[swap] = tmp
