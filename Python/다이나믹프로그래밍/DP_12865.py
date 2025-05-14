import sys

data = sys.stdin.read()
lines = data.splitlines()
N, K = map(int, lines[0].split())

item = []
for i in range(N):
    W, V = map(int, lines[i+1].split())
    item.append((W, V))

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = item[i-1]
    for j in range(1, K + 1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - w] + v)

print(dp[N][K])

