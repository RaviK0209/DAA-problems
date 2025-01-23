def is_cycle_util(v, visited, parent, adj):  
    visited[v] = True
    for i in adj[v]:
        if not visited[i]:
            if is_cycle_util(i, visited, v, adj):   
                return True
        elif i != parent:
            return True
    return False

def is_cycle(V, adj):
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            if is_cycle_util(i, visited, -1, adj):    
                return True
    return False

V = 5
adj = [[] for _ in range(V)]         
adj[0].append(1)
adj[1].append(0)
adj[1].append(2)
adj[2].append(1)
adj[2].append(3)
adj[3].append(2)
adj[3].append(4)
adj[4].append(3)
adj[4].append(1)
adj[1].append(4)

print(is_cycle(V, adj))  
