import sys

data = sys.stdin.read()
lines = data.splitlines()

def dfs(graph, v, visited):
    visited[v] = True
    result.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

N = int(lines[0])

graph = [[] for _ in range(N+1)]

for i in range(1, N):
    a, b = map(int, lines[i].split())
    graph[a].append(b)
    graph[b].append(a)

check_list = list(map(int, lines[N].split()))

result = []

position = [0] * (N+1)
for i in range(N):
    position[check_list[i]] = i

def get_pos(x):
    return position[x]

for i in range(1, N + 1):
    graph[i].sort(key=get_pos)    


visited = [False] * (N+1)
dfs(graph, 1, visited)


if result == check_list:
    print(1)
else:
    print(0)