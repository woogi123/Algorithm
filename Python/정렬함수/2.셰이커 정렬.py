# 버블정렬의 파생
# 패스의 스캔 방향을 앞, 뒤 양쪽으로 번갈아가면서 하는것

def shaker_sort(a):
  left = 0
  right = len(a) -1
  while left < right:
    for j in range(right,left, -1):
      if a[j-1] > a[j]:
        a[j-1], a[j] = a[j], a[j-1]
        last = j
    left = last
  
    for j in range(left,right):
      if a[j] > a[j + 1]:
        a[j], a[j+1] = a[j+1], a[j]
        last = j
    right = last

n = int(input("원소 수를 입력해주세요: "))
a = [None] * n

for i in range(n):
  a[i] = int(input(f"a[{i}] = "))

shaker_sort(a)

for i in range(n):
  print(f"a[{i}] = {a[i]}")