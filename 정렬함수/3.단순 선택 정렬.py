# 가장 작은 원소부터 시작해 알맞은 위치로 이동하는 작업을 반복하는 알고리즘
# 서로 이웃하지 않고 떨어져 있는 원소를 비교하므로 안정적이지 않음 
# Ex. 중복된 숫자의 위치를 바꾸기도 함

def selection_sort(a):
  n = len(a)
  for i in range(n-1):
    min = i  # min을 i로 두는 이유 : 어차피 a[i]가 더 크면 min을 바꾸면 되므로
    for j in range(i + 1,n):
      if a[min] > a[j]:
        min = j   # min 찾기 (앞에서부터 쭉 스캔하면서 min을 찾음)
    a[min], a[i] = a[i], a[min]