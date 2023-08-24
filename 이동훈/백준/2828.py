# 백준 2828

import sys
input = sys.stdin.readline

arr = []

n, m = map(int, input().split())

j = int(input())

for i in range(j):
    x = int(input())
    arr.append(x)

value = 1
cnt = 0

for i in arr:
    # print(i) # 1,5,3
    if value <= i and value + (m-1) >= i:
        pass
    elif value > i:
        cnt += abs(i - value) # abs는 절대값 함수
        value = i
    else:
        cnt += i - (m-1)- value 
        value = i - (m-1)      


print(cnt)

