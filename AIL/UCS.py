graph = {
    'A' : [('C',3), ('E',7), ('B',4)],
    'B' : [('A',4), ('C',6), ('D',5)],
    'C' : [('A',3), ('B',6), ('D',11), ('E',8)],
    'D' : [('C',11), ('E',2), ('B',5), ('G',10), ('F',2)],
    'E' : [('A',7), ('C',8), ('D',2), ('G',5)],
    'G' : [('F',3), ('E',5), ('D',10)],
    'F' : ['']
}

def path_cost(path):
    total_cost=0
    for(node,cost) in path:
        total_cost += cost
    return total_cost , path[-1][0]

def ucs(graph,start,goal) :
    visited=[]
    queue= [[(start,0)]]
    while queue:
        queue.sort(key=path_cost)
        path=queue.pop(0)
        node= path[-1][0]
        if node in visited :
            continue
        visited.append(node)
        if node==goal :
            return  path
        else:
            adjacent_nodes=graph.get(node,[])
            for(node2,cost) in adjacent_nodes:
                new_path=path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)

solution= ucs(graph,'A','F')
print('solution is ', solution)
print('cost of solution is ',path_cost(solution)[0])