import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

first = arr[0]
sec = arr[1]
sum_num = first*K + sec

loop = K + 1

a = M // loop
b = M % loop

print(a * sum_num + b * first)