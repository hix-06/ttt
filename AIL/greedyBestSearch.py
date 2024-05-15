graph = {
    'S' : [('A',3), ('B',2)],
    'B' : [('F',1), ('E',3)],
    'F' : [('I',2), ('G',3)],
    'E' : [('H',5)],
    'A' : [('C',4), ('D',1)],
}
H_table = {
    'A' : 12,
    'B' : 4,
    'C' : 7,
    'D' : 3,
    'E' : 8,
    'F' : 9,
    'H' : 4,
    'I' : 0,
    'S' : 13,
    'G': 2
}
def path_h_cost(path):
    g_cost = 0
    for (node, cost) in path:
        g_cost += cost
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    return h_cost, last_node
def Greedy_best_search (graph, start, goal):
    visited = []
    queue = [[(start,0)]]
    while queue:
        queue.sort(key=path_h_cost) # sorting by f-cost
        path = queue.pop(0)   # choosing least f-cost
        node = path[-1][0]
        if node in visited: 
            continue
        visited.append(node)  
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])  
            for (node2,cost) in adjacent_nodes: 
                    new_path = path.copy()  
                    new_path.append((node2,cost))  
                    queue.append(new_path) 
solution = Greedy_best_search(graph, 'S', 'G')
print('solution is', solution)
print('Cost of Solution is', path_h_cost(solution)[0])