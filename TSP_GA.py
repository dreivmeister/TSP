





distances = {}

num_cities = 5
pop_size = 500
population = []
fitness = []

curr_best_dist = 0
best_order = []
curr_best_order = []

import random
order = list(range(num_cities))
for i in range(pop_size):
    population[i] = random.sample(order, len(order))





def calc_distance(order):
    pass




def calc_fitness(population, fitness):
    curr_rec = 10e6
    for i in range(len(population)):
        d = calc_distance(population[i])
        if d < curr_best_dist:
            curr_best_dist=d
            best_order=population[i]
        if d < curr_rec:
            curr_rec=d
            curr_best_order=population[i]
        fitness[i]=1/(pow(d,8)+1)
    return fitness

def normalize_fitness(fitness):
    res = sum(fitness)
    return [x/res for x in fitness]

import random, copy
def pick_one(population, fitness):
    index = 0
    r = random.random()
    while r:
        r = r - fitness[index]
        index += 1
    index -= 1
    return copy.copy(population[index])

def crossover(order_a, order_b):
    st = random.randint(0,len(order_a)-1)
    en = random.randint(st+1, len(order_a)-1)
    new_order = order_a[st:en]

    for i in range(len(order_b)):
        city = order_b[i]
        if city not in new_order:
            new_order.append(city)
    return new_order

def mutate(order, mutation_rate):
    total_cities = len(order)
    for i in range(total_cities):
        if random.random() < mutation_rate:
            index_a = random.randint(0, len(order)-1)
            index_b = (index_a+1)%total_cities
            order[index_a],order[index_b]=order[index_b],order[index_a]

def next_generation(population, fitness):
    new_population = []
    for i in range(len(population)):
        order_a = pick_one(population, fitness)
        order_b = pick_one(population, fitness)
        order = crossover(order_a, order_b)
        mutate(order, 0.01)
        new_population[i]=order
    population=new_population
    return population

num_generation = 1000
curr_generation = 1
while curr_generation < num_generation:
    curr_generation += 1

    calc_fitness(population, fitness)
    normalize_fitness(fitness)
    next_generation(population, fitness)


#results