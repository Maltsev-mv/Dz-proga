n, m = map(int, input().split())  


adj_list = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split())  
    adj_list[u].append(v)
    adj_list[v].append(u)


visited = set()
def dfs(node):
    print(f"Enter {node}") 
    visited.add(node)
    for neighbor in sorted(adj_list[node]):
        if neighbor not in visited:
            dfs(neighbor)
    print(f"Exit {node}")  


for vertex in range(1, n + 1):
    if vertex not in visited:
        dfs(vertex)
