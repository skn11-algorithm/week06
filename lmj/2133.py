# 타일 채우기 : 3 * n 크기의 벽을 2*1, 1*2 크기의 타일로 채우는 경우의 수
# 입력 : n
# 출력 : 경우의 수
'''
아이디어?
dp[2] 라고 치면 3*2의 경우 3가지 (그림참고)
dp[3] 이라고 치면 3*3 의 경우 만들 수 X ---> 홀수는 만들 수 없음 
dp[4]는 3*4 의 경우 3*2 (dp[2] * 2) + 
'''

import sys
n = int(sys.stdin.readline())

dp = [0] * 31   # Nd의 최대범위가 30이기때문에 31까지 초기화 
dp[2] = 3

for i in range(4, n + 1):
    if i % 2 == 0:   # 짝수만 모양채우기ㅇㅇ 
        dp[i] += dp[i - 2] * dp[2]

        for j in range(i - 4, -1, -2):
            dp[i] += dp[j] * 2 # dp[j]에 좌우 버전 2배 

        dp[i] += 2 # 특수한 모양 2개 추가

print(dp[n])



# https://fre2-dom.tistory.com/460 참고한 티스토리 