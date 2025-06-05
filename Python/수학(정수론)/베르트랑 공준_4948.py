def finding(n):
    result = [True] * (n+1)
    if len(result) == 1:
        return [1]
    else:
        result[0] = result[1] = False

    for i in range(2, int(n**0.5) + 1):
        if result[i] == True:
            for j in range(i * i, n + 1, i):
                result[j] = False

    return [x for x in range(n + 1) if result[x]]



import sys

data = sys.stdin.read().strip()
lines = data.splitlines()

idx = 0
while True:
    n = int(lines[idx])
    if n == 0:
        break
    line = finding(2*n)

    num = 0
    for j in line:
        if j > n and j <= 2*n:
            num +=1
    idx +=1

    print(num)