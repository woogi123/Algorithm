# x > y
# 재귀함수의 일종
# 두 수의 최대공약수를 구하는 함수

def gcd(x,y):
  if y == 0:
    return x
  else:
    return gcd(x,y) == gcd(y,x % y)


print(gcd(5,2))