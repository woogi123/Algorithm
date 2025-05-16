import sys
import heapq

input = sys.stdin.read
lines = input().strip().splitlines()

N = int(lines[0])
oils = []

for i in range(1, N+1):
    a, b = map(int, lines[i].split())
    oils.append((a, b))

town, fuel = map(int, lines[N+1].split())
oils.append((town, 0))
oils.sort()

heap = []
stop = 0

for a, b in oils:
    while fuel < a:
        if not heap:
            print(-1)
            stop = -1
            break
        fuel += -heapq.heappop(heap)
        stop += 1

    if stop == -1:
        break


    heapq.heappush(heap, -b)

if stop != -1:
    print(stop)
