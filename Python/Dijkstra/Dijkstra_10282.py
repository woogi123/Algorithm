import sys
from heapq import heappush, heappop

data = sys.stdin.read()
lines = data.splitlines()

def dijkstra(c, graph):
        lists = [INF] * (n + 1)

        heap = []
        heappush(heap, (0, c))

        while len(heap) != 0:
            cost, node = heappop(heap)
            if lists[node] > cost:
                lists[node] = cost
                for next_node, num in graph[node]:
                    if lists[next_node] > num + cost:
                        heappush(heap, (num + cost, next_node))
        return lists


N = int(lines[0])

num = 1
for _ in range(N):
    n, d, c = map(int, lines[num].split())
    graph = [[] for _ in range(n + 1)]

    for i in range(num + 1, num + d+1):
        start, end, cost = map(int, lines[i].split())
        graph[end].append((start, cost))
    num += d + 1
    INF = int(10**12)

    lists = dijkstra(c, graph)
    count = 0
    max_num = 0
    for i in lists:
        if i != INF:
            if max_num < i:
                max_num = i 
            count+=1
        
    print(count, max_num)

# 코드가 굉장히 더럽지만, 그냥 다익스트라였다~