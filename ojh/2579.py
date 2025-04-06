# 한번에 한계단 또는 두계단
# 세계단 연속해서 X
# 마지막 계단은 반드시 밟아야함
# dp[i] = i번째 계단까지 올라왔을 때 얻을수 있는 최대 점수

# dp[i] = dp[i-3] + point[i-1]+ point[i] # 한칸거리
# dp[i] = dp[i-2] + point[i] # 두칸거리
# 이 중에 max 값을 선택하면 됨

# 두칸거리에서 dp[i-3] + point[i-2] + point[i]는
# dp[i-3] 전에 이미 한칸 연속해서 갔을수 있기 때문에
# + point[i-2]는 세칸 연속해버릴 수 있음
# 그래서 dp[i-2] + point[i] 로 표현

import sys
input=sys.stdin.readline

n=int(input())
point=[0]+[int(input()) for _ in range(n)]

if n==1:
    print(point[1])
elif n==2:
    print(point[1]+point[2])
else:
    dp=[0]*(n+1)
    dp[1]=point[1]
    dp[2]=dp[1]+point[2]

    for i in range(3,n+1):
        dp[i]=max(dp[i-3]+point[i-1]+point[i],dp[i-2]+point[i])

    print(dp[-1])



