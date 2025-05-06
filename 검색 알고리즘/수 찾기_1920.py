import sys
N = int(input())
result = list(map(int, sys.stdin.readline().split()))
M = int(input())
find = list(map(int, sys.stdin.readline().split()))

result.sort()

for i in find:
    front = 0
    rear = len(result)-1
    while True:
        if front > rear:
            print(0)
            break
        mid = (front+rear) // 2

        if i == result[mid]:
            print(1)
            break
        elif i > result[mid]:
            front = mid+1
        else:
            rear = mid-1