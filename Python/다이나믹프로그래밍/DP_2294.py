import sys

data = sys.stdin.read().strip()
lines = data.splitlines()

n, k = map(int, lines[0].split())
coin = [int(lines[i+1]) for i in range(n)]
dp = [100000] * (k + 1)
dp[0] = 0  

for i in coin:
    for j in range(i, k + 1): 
        dp[j] = min(dp[j], dp[j - i] + 1)

if dp[k] != 100000:
    print(dp[k])
else:
    print(-1)


# 점화식: dp[j] = min(dp[j]), dp[j-coin] + 1)
# 이때 dp[i]는 i를 만들 때 사용하는 coin 개수를 의미함.
# dp[j - coin] -> coin을 추가하기 전에 j - coin이 이미 완성된 경우
#                 coin을 더하면 목표값 완성