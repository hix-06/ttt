
graph = {
    'A':['B','C'],
    'C':['D','G'],
    'B':[], # we can write it or ignore it both are OK
    'D':[],
    'G':[]
}


#BFS Graph

def bfs (graph,start,goal):
    queue=[[start]]
    visited=[]
    while queue :
        path=queue.pop(0)
        node=path[-1]
        if node in visited :
            continue 
        visited.append(node)
        if node==goal :
            return path, visited
        else:
            adj_nodes=graph.get(node,[])
            for node2 in adj_nodes:
                new_path=path.copy()
                new_path.append(node2)
                queue.append(new_path)
solution, visited = bfs(graph,'A','G')
print("Solution BFS nodes:",solution)
print("Visited BFS nodes:", visited)