# # 계단 a b c d, 현재 b
# # b 에서 c 와 d 를 비교, 더 큰 값을 밟기
# # a를 밟았을 시에는, 무조건 d를 밟기

# a = int(input())
# lst=[]
# for _ in range(a):
#     lst.append(int(input()))

# add_lst = []
# add_lst.append(lst.pop())

# def stair(lst):
#     while len(lst) > 2:
#         if lst[-1]<lst[-2]:
#             lst.pop()
#             add_lst.append(lst.pop())
#         else:
#             add_lst(lst.pop())

import sys

input = sys.stdin.readline

n = int(input())

# 계단의 숫자를 초기화 합니다. 1층은 1번째(not 0번째) 인덱스에 저장합니다.
stairs = [0] * 301
for i in range(1, n + 1):
    stairs[i] = int(input())

# dp 배열을 초기화합니다.
dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

# 점화식을 계산합니다.
for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n])