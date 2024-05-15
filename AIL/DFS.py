
graph = {
    'A':['B','C'],
    'C':['D','G'],
    'B':[], # we can write it or ignore it both are OK
    'D':[],
    'G':[]
}

#DFS Graph

def dfs (graph,start,goal):
    stack=[[start]]
    visited=[]
    while stack :
        path=stack.pop()
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
                stack.append(new_path)
solution, visited = dfs(graph,'A','G')
print("Solution DFS nodes:",solution)
print("Visited DFS nodes:", visited)