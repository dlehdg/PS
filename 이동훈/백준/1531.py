# 백준 1531

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0]*100 for i in range(100)]

value = 0



for i in range(n):
    a, b, c, d = map(int, input().split())
    for i in range(a, c+1):
        for j in range(b, d+1):
            arr[i-1][j-1] += 1

for i in range(100):
    for j in range(100):
        if arr[i][j] > m:
            value += 1

    

print(value)