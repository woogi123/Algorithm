import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

lst = [input().strip().split() for _ in range(n)]

deq = deque()

for i in lst:
    if i[0] == 'push_front':
        deq.appendleft(i[1])
    elif i[0] == 'push_back':
        deq.append(i[1])
    
    elif i[0] == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif i[0] == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    
    elif i[0] == 'size':
        print(len(deq))
    
    elif i[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    
    elif i[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif i[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
