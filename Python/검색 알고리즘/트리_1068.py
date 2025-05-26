def dfs(y):
    global count
    for i in tree[y]:
        if not visit[i] and i != drop:
            visit[i] = True
            if tree[i] == []:
                count += 1
            dfs(i)
        elif i == drop and len(tree[y]) == 1:
            count += 1

n = int(input())
tree = [[] for _ in range(n)]
root = list(map(int, input().split()))

for i in range(n):
    if root[i] != -1:
        tree[root[i]].append(i)
    else:
        t = i

drop = int(input())
count = 0
tree[drop] = []
visit = [False] * (n + 1)
visit[t] = True
dfs(t)
print(count)
