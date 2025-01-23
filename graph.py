from collections import defaultdict

def criticalConnections(n, connections):
    # Step 1: Build the graph
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
    
    # Step 2: Arrays to store discovery time and the lowest discovery time reachable from each server
    discovery = [-1] * n  # To record when we first visit each server
    low = [-1] * n  # To record the earliest time we can reach another server from the current server
    
    # To store the result (critical connections)
    result = []
    
    # Time variable used to set discovery time
    time = 0
    
    def dfs(node, parent):
        nonlocal time
        discovery[node] = low[node] = time
        time += 1
        
        for neighbor in graph[node]:
            if neighbor == parent:  # Skip the edge leading back to the parent node
                continue
            if discovery[neighbor] == -1:  # If neighbor is not visited
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                
                # A critical connection is found if low[neighbor] > discovery[node]
                if low[neighbor] > discovery[node]:
                    result.append([node, neighbor])
            else:
                # Update the low-link value of the current node
                low[node] = min(low[node], discovery[neighbor])
    
    # Step 3: Start DFS from any node, usually node 0
    dfs(0, -1)
    
    return result

# Example usage:
n = 7
connections = [[0, 1], [1, 2], [2, 0], [1, 3],[0,2],[3,4]]
print(criticalConnections(n, connections))