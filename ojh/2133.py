import sys
input=sys.stdin.readline
n = int(input())

dp = [0]*(n+1)

dp[0] = 1

if n  >= 2:
    dp[2] = 3

for i in range(4,n+1,2):
    dp[i] = dp[i-2] *dp[2]
    for j in range(0,i-2, 2):
        dp[i] += dp[j]*2

print(dp[n])

# 3*2 경우의 수 : 3
# 3*4 경우의 수 : 11
# 3*6 경우의 수 : 41 ( 3*4에 3*2가 붙음 : 11*3=33 , 3*2에 고유한 3*4가 붙음 : 3*2=6 , 고유한 3*6 개수 :2 ->33+6+2 = 41 )
# 3*8 경우의 수 : dp[i-2]*dp[2] + dp[i-4]*2 + dp[i-2]*2 + 2
# ...
