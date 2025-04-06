# 인접한 애들은 같은색X
import sys
input=sys.stdin.readline

n=int(input())
rgb=[list(map(int,input().rstrip().split())) for _ in range(n)]

dp=[[0,0,0] for _ in range(n)]
dp[0]=rgb[0]

for i in range(1,n):
    # 각 경우(색상)를 다 고려해서 최솟값을 유지
    dp[i][0]=rgb[i][0]+min(dp[i-1][1],dp[i-1][2])
    dp[i][1]=rgb[i][1]+min(dp[i-1][0],dp[i-1][2])
    dp[i][2]=rgb[i][2]+min(dp[i-1][0],dp[i-1][1])

print(min(dp[n-1]))