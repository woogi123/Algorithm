import sys

data = sys.stdin.read().strip()
lines = data.splitlines()

n = int(lines[0])
step = [0,]
for i in range(n):
    step.append(int(lines[i+1]))

dp = [0] * (n + 1)

if n >= 1:
    dp[1] = step[1]
if n >= 2:
    dp[2] = step[1] + step[2]
if n >= 3:
    dp[3] = max(step[1] + step[3], step[2] + step[3])

for i in range(4, n + 1):
    dp[i] = max(dp[i - 2] + step[i], dp[i - 3] + step[i - 1] + step[i])

print(dp[n])

# n이 1이면 step1, n이 2이면 step 1+2, n이 3이면 step 1+2 or 2+3 중 max값
# 점화식은
# 전전 계단에서 2칸 올라옴 dp[i-2] + step[i]
# 연속 2계단까지 밟음: dp[i-3] + step[i-1] + step[i]
# 이 중 max값 선택
