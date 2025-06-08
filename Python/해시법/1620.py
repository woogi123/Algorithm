import sys

N, M = map(int, sys.stdin.readline().split())

Dogam0 = dict()
Dogam1 = dict()
for i in range(1,N+1):
    PoketMon = str(sys.stdin.readline().rstrip())
    Dogam0[str(i)] = PoketMon
    Dogam1[PoketMon] = i

for i in range(M):
    Q = sys.stdin.readline().rstrip()
    if Q.isdigit() == True:
        print(Dogam0[Q])
    else:
        print(Dogam1[Q])