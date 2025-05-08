import sys
from heapq import heappush, heappop
from queue import PriorityQueue

data = sys.stdin.read()
lines = data.splitlines()

queue = PriorityQueue()
N = int(lines[0])
M = int(lines[1])

graph = [[] for _ in range(N + 1)]
for i in range(2, M + 2):
    start, end, cost = map(int, lines[i].split())
    graph[start].append((end, cost))
    


INF = int(10**12)
lists = [INF] * (N + 1)
start, end = map(int, lines[M + 2].split())

queue.put((0, start))


while not queue.empty():
    cost, node = queue.get()
    if lists[node] > cost:
        lists[node] = cost
        for next_node, num in graph[node]:
            if lists[next_node] > num + cost:
                queue.put((num + cost, next_node))
                
print(lists[end])


# queue에 넣을때 cost를 먼저 넣어줘야함: cost가 낮은 순서로 정렬되므로로
# 백준 - pypy3은 queue를 지원하지 않음. python으로 제출해야함.
