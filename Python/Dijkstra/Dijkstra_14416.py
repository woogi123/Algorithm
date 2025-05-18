import sys
from heapq import heappush, heappop

data = sys.stdin.read()
lines = data.splitlines()

N, T = map(int, lines[0].split())

farm = []
for N in range(N):
    farm.append([0] * N)

eat_time = []
for i in range(N+1):
    eat_time.append(list(map(int, lines[i+1].split())))

print(farm)
print(eat_time)
eat_count = 0 # 길 3번 건널때마다 밥먹

def dijkstra():
    INF = 10**12
    lists = [INF] * (N * N + 1)
    dest = [(0,1), (0,-1), (1,0), (-1,0)]

    heap = []
    heappush(heap, (eat_time[0][0]), 0)
    
    while len(heap) != 0:
        cost, node = heappop(heap)
        if lists[node] > cost:
            lists[node] = cost
            for a, b in dest:
                if node > 0 and node < N:
                    for next_node, num in eat_time[node]:
                        if eat_time[next_node] > 


    return heap

