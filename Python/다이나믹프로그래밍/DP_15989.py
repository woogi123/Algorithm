import sys

data = sys.stdin.read().strip()
lines = data.splitlines()

T = int(lines[0])
case = []
for i in range(T):
    case.append(int(lines[i+1]))

num = max(case)

dp = [[0] * 4 for i in range(num + 1)]

dp[1][1] = 1
if num >= 2:
    dp[2][1] = 1
    dp[2][2] = 1
if num >= 3:
    dp[3][1] = 1
    dp[3][2] = 1 # 1 2
    dp[3][3] = 1

for i in range(4, num+1):
    dp[i][1] = dp[i-1][1]
    dp[i][2] = dp[i-2][1] + dp[i-2][2]
    dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3]

for i in case:
    print(dp[i][1] + dp[i][2] + dp[i][3])



# 아이디어: 오름차순으로 정렬한다.
# -> 숫자 2가 나오면 뒤에 + 1을 붙일 수 없고, 숫자 3이 나오면 뒤에 +1, +2를 붙일 수 없음.
# ex. 1 + 2 + 1 처럼 오름차순이 아니면 올바르지 않음
# 
# 점화식: DP[i][j] = 마지막 숫자가 j일때 i를 1, 2, 3의 합으로 표현한 오름차순의 경우의 수
# DP[i][j] = DP[i-1][j]
# ex.i=4일 때, DP[4][1] = DP[3][1] -> (1, 1, 1, +1 (j))
