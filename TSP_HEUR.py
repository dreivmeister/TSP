import numpy as np
from tsp_class import tsp
def NN(A, start):
    """Nearest neighbor algorithm.
    A is an NxN array indicating distance between N locations
    start is the index of the starting location
    Returns the path and cost of the found solution
    """
    path = [start]
    N = A.shape[0]
    mask = np.ones(N, dtype=bool)  # boolean values indicating which
                                   # locations have not been visited
    mask[start] = False

    for i in range(N-1):
        last = path[-1]
        next_ind = np.argmin(A[last][mask]) # find minimum of remaining locations
        next_loc = np.arange(N)[mask][next_ind] # convert to original location
        path.append(next_loc)
        mask[next_loc] = False

    return list(path)

def opt_2(curr_order, c1, c2):
    #step1
    new_order = curr_order[0:c1+1]
    #step2
    r = curr_order[c1+1:c2+1]
    r = r[::-1]
    for i in range(len(r)):
        new_order.append(r[i])
    #step3
    e = curr_order[c2+1:]
    for i in range(len(e)):
        new_order.append(e[i])
    return new_order

def calc_distance(adj_matrix, order):
    print(order)
    sum = adj_matrix[order[-1]][order[0]]
    for i in range(len(order)-1):
        cityA = order[i]
        cityB = order[i+1]
        sum += adj_matrix[cityA][cityB]
    return sum

def solve(adj_matrix, num_cities, k=3):
    from random import randint
    #generate first order
    best_dist = 10e6
    best_order = []

    #generate first order using randomness or some opening heuristic
    start_node = randint(0,num_cities-1)
    curr_order = NN(np.array(adj_matrix), start_node)
    no_change_count = 0
    while no_change_count<10:
        curr_dist = calc_distance(adj_matrix, curr_order)

        if curr_dist < best_dist:
            best_dist = curr_dist
            best_order = curr_order
        else:
            no_change_count+=1

        #generate new order using some improve heuristic
        c1 = randint(1,num_cities-1)
        c2 = randint(c1+1,num_cities-1)
        curr_order = opt_2(curr_order, c1, c2)
    return (best_order, best_dist)


t = tsp(5, 50)
res = solve(t.adj_matrix, t.num_cities)

print(res)
