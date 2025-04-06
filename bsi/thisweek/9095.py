# # 1. 3으로 나누었을 때
# # 2. 2로 나누었을 때
# # 3. 같아지는 경우?

# t = int(input())
# lst = []
# for _ in range(t):
#     lst.append(int(input()))
# result = []

# for n in lst:
#     k = n // 3
#     l = n % 3
#     a = 4 ** k
#     if l == 2:
#         a = a * 2
#     a = a * (k +1)
#     result.append(a)

# for i in result:
#     print(i)
    

#https://velog.io/@greene/백준-9095번-1-2-3-더하기-파이썬
import sys
input = sys.stdin.readline

def func(x):
  if x==1:
    return 1
  elif x==2:
    return 2
  elif x==3:
    return 4
  else:
    return func(x-1)+func(x-2)+func(x-3)

t = int(input())
for _ in range(t):
  n = int(input())
  print(func(n))