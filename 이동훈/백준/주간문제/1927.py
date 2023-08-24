import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input().strip())

# 우선순위 큐
queue = PriorityQueue()

for i in range(n):
    m = int(input().strip())

    if m == 0:
        if queue.qsize() > 0:
            
          print(queue.get())

        else:
          print("0")

    else:
          queue.put(m)