import sys
import heapq

input = sys.stdin.read
lines = input().strip().splitlines()

T = int(lines[0])
n = 1
for _ in range(T):
    K = int(lines[n])
    case = list(map(int, lines[n+1].split()))
    case.sort()
    n+=2

    result = 0
    while True:
        if len(case) == 1:
            print(result)
            break
        num = 0
        num += heapq.heappop(case)
        num += heapq.heappop(case)
        result += num
        case.append(num)
