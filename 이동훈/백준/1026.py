# 백준 1026

n = int(input())

arr1 = []
arr2 = []

value = 0



x = list(map(int, input().split()))
y = list(map(int, input().split()))

x.sort(reverse=True)
y.sort()

# print(x, y)

for i in range(n):
    
    value += x[i] * y[i]
print(value)




