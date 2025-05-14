import sys
from collections import Counter

data = sys.stdin.read().strip()
lines = data.splitlines()

A = int(lines[0])
result = list(map(int, lines[1].split()))

dp = [1] * A

for i in range(1, A):
    for j in range(i):
        if result[i] > result[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))