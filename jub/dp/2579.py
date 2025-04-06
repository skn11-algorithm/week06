# 계단 오르기
# 한번에 한계단 씩 또는 두 계단씩 오를 수 있음
# 연속된 세 개의 계단을 모두 밟아서는 안됨
# 시작점은 계단에 포함 안됨
# 마지막 도착 계단은 반드시 밟아야 함

import sys
input = sys.stdin.readline
n = int(input()) #계단 개수

s = [int(input()) for _ in range(n)] # 각 계단의 점수를 리스트로 입력 받음음
dp = [0] * (n) #dp 0으로 채워진 리스트 

if len(s) <= 2: # 계단 2개 이하일 때 그냥 더해서 출력
    print(sum(s))

else:
    dp[0] = s[0]
    dp[1]=s[0]+s[1]
    for i in range(2,n):# 3번째 계단부터 dp 점화식 이용
        dp[i] = max(dp[i-3]+s[i-1]+s[i],dp[i-2]+s[i])
        #  i-3까지의 계단 점수 최댓값과 i-1, i 계단의 합.
        #  i-2까지의 계단 점수 최댓값과 i 계단의 합
        #  3번째 계단부터 2계단을 연속으로 걸었을 때와, 1계단을 건너뛴 것을 비교해서 최댓값을 계속 갱신시켜나가는 것
    print(dp[-1])