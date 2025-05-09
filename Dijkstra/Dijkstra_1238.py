import sys
from heapq import heappush, heappop

data = sys.stdin.read()
lines = data.splitlines()

N, M, X = map(int, lines[0].split())

graph = [[] for _ in range(N + 1)]
graph_rev = [[] for _ in range(N + 1)]

for i in range(1, M + 1):
    start, end, cost = map(int, lines[i].split())
    graph[start].append((end, cost))
    # graph_rev[end].append((start, cost))

INF = int(10**12)

def dijkstra(start, graph):
    lists = [INF] * (N + 1)

    heap = []
    heappush(heap, (0, start))

    while len(heap) != 0:
        cost, node = heappop(heap)
        if lists[node] > cost:
            lists[node] = cost
            for next_node, num in graph[node]:
                if lists[next_node] > num + cost:
                    heappush(heap, (num + cost, next_node))

    return lists

town_to_X = []
for i in range(N):
    town_to_X.append(dijkstra(i+1, graph))

X_to_town = dijkstra(X, graph)

# print(town_to_X,'\n')
# print(X_to_town)

max_num = 0
for i in range(1, N + 1):
    go = town_to_X[i-1][X]
    back = X_to_town[i]
    summ = go + back
    if summ > max_num:
        max_num = summ
print(max_num)


# X: 가야하는 마을
# 최단거리를 찾고, 이 중 가장 오래걸리는 학생 (최댓값)
# 1, 2, 3, 4 가 각 node 가는 방향 (정방향) + X -> 1, 2, 3, 4 역방향



