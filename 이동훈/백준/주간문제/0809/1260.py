# 백준 1260번 DFS와 BFS
# import sys
# input = sys.stdin.readline
from collections import deque

# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
n, m, v = map(int, input().split())

arr = [[] for i in range(n+1)]

visited = [0] * (n+1)
visited2 = [0] * (n+1)



for i in range(1,m+1):
    a, b = map(int, input().split())
    
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
  i.sort()

def dfs(arr, num, visited):
  visited[num] = 1
  print(num, end=' ')
  for j in arr[num]:
    
    
    if visited[j] == 0:
      dfs(arr, j, visited)
  


def bfs(arr, num, visited2):
  queue = deque()
  queue.append(num)
  visited2[num] = 1
  # print(queue)
  while queue:
    value = queue.popleft()
    print(value, end=' ')
    for j in arr[value]:
        if visited2[j] == 0:
          visited2[j] = 1
          queue.append(j)
          
  
          



      
dfs(arr, v, visited)
print()

bfs(arr, v, visited2)
