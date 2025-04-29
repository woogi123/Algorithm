import sys

data = sys.stdin.read()
lines = data.splitlines()
a = int(lines[0])

line = [0] * 1001
line[1] = 1
line[2] = 2

def n_num(a):
    if line[a] == 0:
        line[a] = int(n_num(a-2)) + int(n_num(a-1))
        return line[a]
    else:
        return line[a]
    
print(n_num(a)%10007)


# 점화식이 N > 2일때, f(N-1) + f(N-2) = f(N)이다.
# 따라서 재귀함수로 해결