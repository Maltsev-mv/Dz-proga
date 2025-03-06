n, m = map(int, input().split())  


adj_matrix = [[0] * n for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split()) 
    adj_matrix[u - 1][v - 1] = 1  


reversed_matrix = [[adj_matrix[j][i] for j in range(n)] for i in range(n)]


for row in reversed_matrix:
    print(" ".join(map(str, row)))
