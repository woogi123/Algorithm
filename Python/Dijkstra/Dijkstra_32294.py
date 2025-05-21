import sys
from heapq import heappush, heappop

data = sys.stdin.read()
lines = data.splitlines()

n = int(lines[0])
a = list(map(int, lines[1].split()))
b = list(map(int, lines[2].split()))

INF = int(10*12)

def dijkstra(c, graph):
    lists = [INF] * (n+5)

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

graph_end = [[] for _ in range(n + 2)]
graph_start = [[] for _ in range(n + 2)]

for i in range(n):
    jump = a[i]
    cost = b[i]
    now = i + 1

    if now - jump < 1:
        graph_start[now].append((0, cost))
    else:
        graph_start[now].append((now - jump, cost))

    if now + jump > n:
        graph_end[now].append((n+1, cost))
    else:
        graph_end[now].append((now + jump, cost))


for i in range(1, n + 1):
    lists_end = dijkstra(i, graph_end)
    lists_start = dijkstra(i, graph_start)

    if lists_end[n+1] > lists_start[0]:
        print(lists_start[0], end=" ")
    else:
        print(lists_end[n + 1], end=" ")





# 왼쪽으로 점프하는 경우 vs 오른쪽으로 점프하는 경우 해서 최솟값

# 모든 위치를 노드로 생각
# 수열 밖으로 나가는 위치(탈출 지점)를 도착 노드로 간주
# 0은 start, n은 end
# 각 위치에서 점프할 수 있는 곳으로 간선 (비용은 b[i])을 생성
# 다익스트라로 각 위치에서 탈출 노드까지의 최단 시간 계산