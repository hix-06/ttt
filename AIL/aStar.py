graph = {
    'A' : [('C',3), ('E',7), ('B',4)],
    'B' : [('A',4), ('C',6), ('D',5)],
    'C' : [('A',3), ('B',6), ('D',11), ('E',8)],
    'D' : [('C',11), ('E',2), ('B',5), ('G',10), ('F',2)],
    'E' : [('A',7), ('C',8), ('D',2), ('G',5)],
    'G' : [('F',3), ('E',5), ('D',10)],
    'F' : ['']
}
H_table = {
    'A' : 28,
    'B' : 30,
    'C' : 56,
    'D' : 60,
    'E' : 44,
    'F' : 10,
    'G': 36
}


def path_f_cost(path):
    g_cost = 0
    for (node, cost) in path:
        g_cost += cost
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    f_cost = g_cost + h_cost
    return f_cost, last_node


def a_star_search(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_f_cost)
        path = queue.pop(0)
        node = path[-1][0]

        if node in visited:
            continue
        visited.append(node)

        if node == goal:
            return path
        else:
            for (neighbor, cost) in graph[node]:
                new_path = path.copy()
                new_path.append((neighbor, cost))
                queue.append(new_path)


solution = a_star_search(graph, 'A', 'F')
print('solution is', solution)
print('Cost of Solution is', path_f_cost(solution)[0])