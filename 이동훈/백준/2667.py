# 백준 2667

import sys
input = sys.stdin.readline

n = int(input())

arr = []
num = []

count = 0

for i in range(n):
    m = list(map(int, input().strip()))
    arr.append(m)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x, y):
    
    global count
    if x < 0 or x >= n or y < 0 or y >=n: # 범위를 벗어나면 false
        return False
    
    if arr[x][y] == 1: # 집이 있는경우에는 count를 1 증가시키고 다시 0으로 변경 그 후 for문을 통해 재귀
        
        count += 1
        arr[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    return False
        


# 그래프의 원소가 1일때만 dfs로 집을 방문한다.
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            # 
            num.append(count)
            count = 0

num.sort()  # 오름차순으로 정렬

print(len(num))  # 총 단지수 출력
for k in num:  # 각 단지마다 집의 수 출력
    print(k)