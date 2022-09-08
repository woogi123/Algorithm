# 버블정렬 -> 이웃한 두 원소의 대소관계를 비교하여 필요에 따라 교환하는 알고리즘 
# 이웃한 두 원소로만 교환을 하기 때문에 안정성이 좋음
# 일련의 교환.과정을 "패스" 라고 칭함.

# 버블 정렬 (배열이 정해져 있을 때)
def bubble_sort(a):
  n = len(a)
  for i in range(n-1):
    for j in range(n-1,i,-1):
      if a[j-1] > a[j]:
        a[j-1], a[j] = a[j], a[j-1]

a = [3,1,475,623,472,57,45,73,568,346,24362,47,46,345]
bubble_sort(a)
print(a)


# 버블 정렬 (배열이 정해져 있지 않을 때)
def bubble_sort(a):
  n = len(a)
  for i in range(n-1):
    exchange = 0
    for j in range(n-1,i,-1):
      if a[j-1] > a[j]:
        a[j-1], a[j] = a[j], a[j-1]
        exchange += 1
    if exchange == 0:     # 패스 값이 0이라면, 이미 배열이 완료되어 있다는 뜻이므로 break  
      break
n = int(input("원소 수를 입력해주세요: "))
x = [None] * n

for i in range(n):
  x[i] = int(input(f"x[{i}] = "))

bubble_sort(x)

for i in range(n):
  print(f"x[{i}] = {x[i]}", end="   ")


# 버블 정렬 알고리즘 개선
def bubble_sort(a):
  n = len(a)
  k = 0
  while k < n-1:
    last = n - 1
    for j in range(n - 1, k, -1):
      if a[j-1] > a[j]:
        a[j-1], a[j] = a[j], a[j-1]
        last = j          # 마지막으로 바꾼 값이 j번째 이므로, 그 앞은 이미 정렬이 되어 있기 때문에
    k = last              # 다음 패스를 시작할 때 k = last(k를 마지막으로 바꾼 곳)로 설정하고 n-1부터 k 까지 -1씩 가는 것.

n = int(input("원소 수를 입력해주세요: "))
x = [None] * n

for i in range(n):
  x[i] = int(input(f"x[{i}] = "))

bubble_sort(x)

for i in range(n):
  print(f"x[{i}] = {x[i]}")

