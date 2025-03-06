n, m = map(int, input().split()) 

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())  
    edges.append((u, v, w))


INF = float('inf')
distance = {i: INF for i in range(1, n + 1)}
source = 1 

distance[source] = 0


for _ in range(n - 1):
    for u, v, w in edges:
        if distance[u] != INF and distance[u] + w < distance[v]:
            distance[v] = distance[u] + w


for u, v, w in edges:
    if distance[u] != INF and distance[u] + w < distance[v]:
        print("Negative cycle detected")
        break
else:
    for vertex in range(1, n + 1):
        print(distance[vertex] if distance[vertex] != INF else "INF")
