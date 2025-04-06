# 계단오르기 - 한개 또는 두개씩 오르되 연속된 세계의 계단을 밟을수는 없고, 마지막 계단은 꼭 밟아야함

# 입력 : 계단의 수
# 출력 : 총 점수의 최댓값

# 💡아이디어
# dp로 i번째 계단을 오르는 최적탐색
# 마지막 계단 i에 도착했을 경우, i i-1이 연속 or 연속되지 않게 도착


import sys
input = sys.stdin.readline

n = int(input())
stair = [0] * (n+1)

for i in range(1, n+1):
    stair[i] = int(input())

dp = [0] * (n+1) # 첫번째 계단으로 시작하기 위해 1을 더해주고 dp 배열 초기화

if n == 1:
    print(stair[1])
elif n == 2:
    print(stair[1] + stair[2])
else:
    dp[1] = stair[1] # 첫번째 계단까지 가는 방법 
    dp[2] = stair[1] + stair[2]

    # 세번째부터는 두가지 점화식으로 dp 계산
    for i in range(3, n+1):
        dp[i] = max(
            dp[i-2] + stair[i],
            dp[i-3] + stair[i-1] + stair[i]
        )

    print(dp[n])