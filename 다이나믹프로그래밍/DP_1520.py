import sys

data = sys.stdin.read()
lines = data.splitlines()

M, N = map(int, lines[0].split())

maps = []
for i in range(M):
    maps.append(list(map(int, lines[i+1].split())))

dp = [[0] * (N) for _ in range(M)]
up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)

h_map = []
for x in range(M):
    for y in range(N):
        h_map.append((maps[x][y], x, y))
h_map.sort(reverse=True)

dp[0][0] = 1
for height, x, y in h_map:
    for a, b in (up, down, left, right):
        a, b = x + a, y + b
        if a >= 0 and a != M and b >= 0 and b != N:
            if maps[a][b] < maps[x][y]:
                dp[a][b] += dp[x][y]

print(dp[M-1][N-1])

# dp[i][j]: i 좌표에서 갈 수 있는 경우의 수 j
# 높이 기반으로 정렬하는게 키포인트