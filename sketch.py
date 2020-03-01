import time
from population import Population

MAX_WEIGHT = 240
w = [20, 30, 40, 50, 60, 20, 70, 2, 100, 90, 80] # must be distinct values
v = [17, 33, 8, 12, 36, 9, 30, 30, 50, 45, 22]
p = []

for i in range(len(v)):
    p.append({'weight': w[i], 'value': v[i]})
population = Population(p, MAX_WEIGHT)

def disp():
    print('[{}]\n Best: {}\n Fitness: {}'
    .format(population.generations, population.best.value, population.best.fitness))

# ---- BEGIN ----
start_time = time.time()

for i in range(100):
    population.natural_selection()
    population.new_generation()
    population.c_fitness()
    population.evaluate()
    disp()

# ---- END ----
print("--- %f seconds ---" % (time.time() - start_time))
