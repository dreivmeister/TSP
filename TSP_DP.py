#optimal solution from start node to every other node
def setup(m, memo, S, N):
    for i in range(N):
        if i == S: continue
        memo[i][1 << S | 1 << i] = m[S][i]

def combs(set, at, r, n, subsets):
    if r == 0:
        subsets.append(set)
    else:
        for i in range(at, n):
            set = set | (1 << i)
            combs(set, i+1, r-1, n, subsets)
            set = set & ~(1 << i)

def combinations(r, N):
    subsets = []
    combs(0, 0, r, N, subsets)
    return subsets

def not_in(i, subset):
    return ((1 << i) & subset) == 0

def solve(m, memo, S, N):
    for r in range(3, N+1):
        for subset in combinations(r, N):
            if not_in(S, subset): continue
            for next in range(N):
                if next == S or not_in(next, subset): continue

                state = subset ^ (1 << next)
                min_dist = 10e6
                for e in range(N):
                    if e == S or e == next or not_in(e, subset): continue
                    new_dist = memo[e][state] + m[e][next]
                    if new_dist < min_dist: min_dist = new_dist
                memo[next][subset] = min_dist

def find_min_cost(m, memo, S, N):
    end_state = (1 << N) - 1
    min_tour_cost = 10e6

    for e in range(N):
        if e == S: continue

        tour_cost = memo[e][end_state] + m[e][S]
        if tour_cost < min_tour_cost:
            min_tour_cost = tour_cost
    return min_tour_cost

def find_optimal_tour(m, memo, S, N):
    last_index = S
    state = (1 << N) - 1
    tour = [0]*(N+1)

    for i in range(N-1, 0, -1):
        index = -1
        for j in range(N):
            if j == S or not_in(j, state): continue
            if index == -1: index = j
            prev_dist = memo[index][state] + m[index][last_index]
            new_dist = memo[j][state] + m[j][last_index]
            if new_dist < prev_dist: index = j
        
        tour[i] = index
        state = state ^ (1 << index)
        last_index = index
    tour[0] = tour[N] = S
    return tour

# finds min TSP tour cost
#m - 2D adjacency matrix
#S - start node
def tsp(m, S):
    #matrix size
    N = len(m)

    #Init memo table
    memo = [[None for j in range(2**N)] for i in range(N)]

    setup(m, memo, S, N)
    solve(m, memo, S, N)
    min_cost = find_min_cost(m, memo, S, N)
    tour = find_optimal_tour(m, memo, S, N)

    return min_cost, tour


#N - number of nodes

def calc_weights(N, W):
    from math import inf
    from random import randrange
    m = [[inf for j in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(N):
            if i==j: continue
            m[i][j] = m[j][i] = randrange(1, W)
    return m

N = 11
W = 50
m = calc_weights(N, W)
min_cost = 10e6
min_tour = []
for i in range(N):
    C, T = tsp(m, i)
    if C < min_cost:
        min_cost = C
        min_tour = T

print(min_cost)
print(min_tour)
