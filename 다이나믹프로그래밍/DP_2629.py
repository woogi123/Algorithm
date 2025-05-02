import sys
input = sys.stdin.readline

C = int(input())
C_list = list(map(int, input().split()))
B = int(input())
B_list = list(map(int, input().split()))

MAX = 50000

for i in B:
    dp = [[False] * (MAX + 1) for _ in range(C + 1)]
    dp[0][0] = True
    for k in range(C):
        for j in range(MAX+1):
            if dp[i][j]:
                dp[i+1][j] = True
                if dp[i+1][j] + C_list[k]:
                    dp[i+1][j+C_list[k]] = True
                dp[i+1][j-C_list[k]] = True





        

# 가치를 크게할 수 있으면 1, 아니면 0으로 놓고 해보기
# 추를 안달았을 때 dp[i][j]
# 구슬이 있는 곳에 추를 달았을 때 dp[i][j + w]
# 구슬이 없는 곳에 추를 달았을 때 dp[i][j - w]