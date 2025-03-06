n, m = map(int, input().split()) 

adj_list = {i: [] for i in range(1, n + 1)} 

for _ in range(m):
    u, v = map(int, input().split())  
    adj_list[u].append(v)  


for key in sorted(adj_list):
    print(key, "->", " ".join(map(str, adj_list[key])))
