# 백준 11403

# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
# visited = [0] * n

# def dfs(x):
#     for i in range(n):
#         if graph[x][i] == 1 and visited[i] == 0:
#             visited[i] = 1
#             dfs(i)

# visited = [0 for _ in range(n)]
# for i in range(n):
#     dfs(i)
#     for j in range(n):
#         if visited[j] == 1:
#             print(1, end=' ')
#         else:
#             print(0, end=' ')
#     print()
#     visited = [0 for _ in range(n)]


import sys

input = sys.stdin.readline
n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j]=1

for r in graph:
    for c in r:
        print(c, end = " ")
    print()