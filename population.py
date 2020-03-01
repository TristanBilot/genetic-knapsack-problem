from dna import DNA
import random
import math

class Population():
    def __init__(self, objects, MAX_WEIGHT):
        self.objects = objects
        self.MAX_WEIGHT = MAX_WEIGHT
        self.genes = []
        self.mating_pool = []
        self.generations = 0
        self.best_fitness = 0
        self.best = None
        self.max_pop = 30
        self.mutation_rate = 0.01
        self.values_sum = 0

        self.c_values_sum()
        self.generate_genes()
        self.c_fitness()

    def generate_genes(self):
        for i in range(self.max_pop):
            self.genes.append(DNA(
                self.objects,
                self.MAX_WEIGHT,
                self.values_sum,
                self.mutation_rate
            ))

    def c_values_sum(self):
        for o in self.objects:
            self.values_sum += o["value"]

    def c_fitness(self):
        for dna in self.genes:
            dna.c_fitness()

    def natural_selection(self):
        self.mating_pool = []
        for dna in self.genes:
            for i in range(int(dna.fitness * 100)):
                self.mating_pool.append(dna)

    def new_generation(self):
        self.genes = []
        for i in range(0,len(self.mating_pool)):
            if i == self.max_pop:
                break
            a = random.randint(0, len(self.mating_pool)-1)
            b = random.randint(0, len(self.mating_pool)-1)
            parent1 = self.mating_pool[a]
            parent2 = self.mating_pool[b]
            child = parent1.crossover(parent2)
            child.mutate()
            self.genes.append(child)
        self.generations += 1

    def evaluate(self):
        for dna in self.genes:
            if dna.fitness > self.best_fitness:
                self.best = dna
                self.best_fitness = dna.fitness
