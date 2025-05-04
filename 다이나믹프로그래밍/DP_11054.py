import sys
from collections import Counter

data = sys.stdin.read().strip()
lines = data.splitlines()

N = int(lines[0])
A = list(map(int, lines[1].split()))

dp = [0] * (N + 1)

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)
        

dp_re = [0] * (N + 1)
A_re = A[::-1]

for i in range(N):
    dp_re[i] = 1
    for j in range(i):
        if A_re[j] < A_re[i]:
            dp_re[i] = max(dp_re[i], dp_re[j] + 1)

result = 0
for i in range(N):
    if dp[i] + dp_re[N-i-1] > result:
        result = dp[i] + dp_re[N-i-1]

print(result-1)


# dp[i] = 길이를 의미함.
# 왼 -> 오 하는 dp, 오 -> 왼 하는 dp_re
# for j in range(i): 0부터 i까지 길이계산 후 dp[i] 업데이트
# 역방향도 마찬가지로 dp_re[i] 업데이트
# 양방향 dp를 더해 최댓값을 가지는 값 출력

