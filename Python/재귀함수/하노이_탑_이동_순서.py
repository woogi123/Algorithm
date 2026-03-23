import sys

def hanoi(n, start, end, sub):
    if n == 1:
        print(f"{start} {end}")
        return

    hanoi(n - 1, start, sub, end)
    
    print(f"{start} {end}")
    
    hanoi(n - 1, sub, end, start)

n = int(sys.stdin.readline())

print(2**n - 1)
hanoi(n, 1, 3, 2)