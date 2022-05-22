
class Ant:
    def __init__(self) -> None:
        self.curr_tour = []
        self.len_tour = 0



class Colony:
    def __init__(self, graph, num_ants, alpha, beta, Q) -> None:
        self.graph = graph
        self.phero_matrix = [[]] #do that
        self.num_ants = num_ants
        self.alpha = alpha
        self.beta = beta
        self.Q = Q
        self.colony = []
    
    def generate_solutions(self):
        #Generates a stochastic solution for each ant (num_ants)
        #based on pheromone diffusion
        #At the start of each iteration

        for i in range(self.num_ants):
            self.colony.append(([], ))



ant = []

dist_matrix = [[0,5,7],
               [5,0,3],
               [7,3,0]]

#contains phero level for each edge (i,j) betw. node i and node j
#like so: phero_table[(i,j)] = x
#phero_table[(i,j)] = phero_table[(j,i)] = x
def init_phero_table(num_nodes, dist_matrix):
    from random import random
    phero_table = {}
    for i in range(num_nodes):
        for j in range(num_nodes):
            #check if edge exists in graph
            if dist_matrix[i][j] == -1:
                continue
            phero_table[(i,j)] = random()
    return phero_table

def add_next_step(num_nodes, curr_state, phero_table, dist_matrix, alpha, beta):
    from random import choices
    #calculate for all neighbors, draw next edge with these probs.
    curr_node = curr_state[-1]

    #all neighbor nodes
    probabilities = []
    s = 0
    for j in range(num_nodes):
        #abbruchkriterium
        if j in curr_state:
            continue
        s += phero_table[(curr_node, j)]**alpha * (1/dist_matrix[curr_node][j])**beta
    
    for j in range(num_nodes):
        if j in curr_state:
            probabilities.append(0.0)
            continue
        val = phero_table[(curr_node, j)]**alpha * (1/dist_matrix[curr_node][j])**beta
        probabilities.append(val/s)
    next_node = choices(population=list(range(num_nodes)), weights=probabilities, k=1)
    #returns next node to add to construction path
    return next_node[0]

def get_p_best_edges(num_nodes, solutions, lengths, p=0.25):
    from math import floor
    #solutions-full paths of all ants
    #lengths-length of each solution lengths[k]=length of path at solutions[k]
    #returns all edges which are used in all of the top p percent solutions
    num_nodes_p = floor(p*num_nodes)
    solutions_sorted = [x for _, x in sorted(zip(lengths, solutions))]
    top_p_percent_sols = solutions_sorted[:num_nodes_p]
    
    def intersection(first, *others):
        return set(first).intersection(*others)

    return intersection(top_p_percent_sols[0], top_p_percent_sols[1:])
#IMPLEMENT ANT SYSTEM BY DORIGO
def update_pheros(num_nodes, top_sols, phero_matrix):
    pass


#generate n solutions
    #while still unvis nodes in neighborhood
    #add new node to current sol based on equation probability equation
#after all sols generated
    #calc delta sum for all edges
    #calc new val for all edges

#[1,2,3]->[(1,2),(2,3)]



    

