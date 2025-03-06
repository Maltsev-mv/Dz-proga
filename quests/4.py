from collections import deque

n, m = map(int, input().split())  


adj_list = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split()) 
    adj_list[u].append(v)
    adj_list[v].append(u)


def bfs(start, visited):
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


visited = set()
components = 0
for vertex in range(1, n + 1):
    if vertex not in visited:
        bfs(vertex, visited)
        components += 1

print(components)
