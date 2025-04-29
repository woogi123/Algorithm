import sys

data = sys.stdin.read()
lines = data.splitlines()
a = int(lines[0])

step = []
for i in range(a):
    step.append(int(lines[i+1]))

line = [0] * 1000001

line[1] = 1
line[2] = 2
line[3] = 4

for i in range(4, max(step) + 1):
    line[i] = (line[i-1] + line[i-2] + line[i-3]) % 1000000009

for i in step:
    print(line[i])


# DP 문제 중 하나. 
# 점화식은 N > 4일때, N-3 + N-2 + N-1이다.

# 1. 아래와 같이 문제를 풀어보니 RecursionError 발생 -> 반복문으로 대체 후 해결
# def summ(a):
#     a = int(a)
#     if line[a] == 0:
#         line[a] = int(summ(a-1)) + int(summ(a-2)) + int(summ(a-3))
#         return line[a]
#     else:
#         return line[a]
    