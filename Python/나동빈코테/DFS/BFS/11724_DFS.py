import sys

data = sys.stdin.read()
lines = data.splitlines()

def dfs(graph, v, visited):
    visited[v] = True
    result.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

N, M = map(int, lines[0].split())


result = []
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, lines[i+1].split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

result_list = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(graph, i, visited)
        result_list +=1

print(result_list)