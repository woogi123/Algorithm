import sys
from heapq import heappush, heappop

data = sys.stdin.read()
lines = data.splitlines()

N, T = map(int, lines[0].split())

farm = []
for N in range(N):
    farm.append([] * N)

eat_time = []
for i in range(N+1):
    eat_time.append(list(map(int, lines[i+1].split())))

print(eat_time)
eat_count = 0 # 길 3번 건널때마다 밥먹

def dijkstra():
    INF = 10**12
    lists = [INF] * (N * N + 1)

    heap = []
    heappush(heap, (eat_time[0][0]), 0)
    
    while len(heap) != 0:
        cost, node = heappop(heap)
        if lists[node] > cost:
            lists[node] = cost
            dest = [(0,1), (0,-1), (1,0), (-1,0)]
            if node > 0 and node < N:
                for move in dest:
                    for next_node


    return heap

