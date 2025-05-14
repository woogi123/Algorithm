import sys

data = sys.stdin.read()
lines = data.splitlines()

C = int(lines[0])
C_list = list(map(int, lines[1].split()))
B = int(lines[2])
B_list = list(map(int, lines[3].split()))

dp = [[-1] * 50001 for _ in range(C + 1)]
dp[0][0] = 1

for i in range(1, C + 1):
    a = C_list[i - 1]
    for j in range(50001):
        if dp[i - 1][j] == 1:
            dp[i][j] = 1
            if j + a <= 50000:
                dp[i][j + a] = 1
            if abs(j - a) <= 50000:
                dp[i][abs(j - a)] = 1

for i in B_list:
    if i > 50000:
        print('N', end=' ')
    elif dp[C][i] == 1:
        print('Y', end=' ')
    else:
        print('N', end=' ')

# dp[i][j] : i번째 추 까지 선택을 완료했을 때, 
# 구슬이 있는 곳의 무게가 반대편의 무게보다 j만큼 크게할 수 있다면 1, 없다면 0
# 점화식
# 추를 사용하지 않음: DP[i + 1][j] = DP[i][j]
# 추를 구슬과 같은 곳에 놓음: DP[i + 1][j] = DP[i][j + W[i]]
# 추를 구슬 반대 편에 놓음: DP[i + 1][j] = DP[i][j - W[i]]

# !구슬 반대편의 무게가 더 클 수도 있다.