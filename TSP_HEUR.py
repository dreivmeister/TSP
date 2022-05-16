def nearest_neighbor_heuristic(adj_matrix, num_cities, start_node):
    #returns list of order
    order = []
    curr_node = start_node
    for i in range(num_cities):
        order.append(curr_node)
        curr_node = min(range(num_cities), key=adj_matrix[curr_node].__getitem__)
    return order

def solve(adj_matrix, num_cities):
    from random import randint
    #generate first order
    best_dist = 10e6
    best_order = []
    
    #generate first order using randomness or some opening heuristic
    start_node = randint(0,num_cities-1)
    curr_order = nearest_neighbor_heuristic(adj_matrix, num_cities, start_node)
    no_change_count = 0
    while no_change_count<10:
        curr_dist = calc_distance(adj_matrix, curr_order)

        if curr_dist < best_dist:
            best_dist = curr_dist
            best_order = curr_order
        else:
            no_change_count+=1
        
        #generate new order using some improve heuristic