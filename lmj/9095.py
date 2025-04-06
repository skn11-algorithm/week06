# 1, 2, 3 더하기
# 입력 : 테스트 케이스의 개수 t
# 출력 : 1,2,3의 합으로 나타내는 방법의 수
# 아이디어
# dp에 1,2,3 저장 후 이들의 조합으로 최적탐색

'''
dp[1] = 1 / 1
dp[2] = 11 2 / 2 
dp[3] = 111 12 21 3 / 4
dp[4] = 1111 112 121 22 211 13 31 / 7
dp[5] = 11111 1112 1121 1211 2111 221 212 122 113 131 311 23 32 / 13

점화식 dp[i] = dp[i]
'''

import sys
input = sys.stdin.readline
t = int(input()) # 테스트 케이스 수 

for _ in range(t):
    n = int(input()) # 입력받는 숫자 
    dp = [0] * (n+1)

    for i in range(1, n+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])
    