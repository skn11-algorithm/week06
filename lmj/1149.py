'''
집을 칠하는 경우는 빨 초 파
n개의 집을 모두 칠하는 최소 비용

연달아 같은 색의 집을 칠할 수 없음

각 줄의 최소값을 더하면 됨

'''
import sys
input = sys.stdin.readline
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)] # 입력될 숫자값 배열

dp = [[0] * 3 for _ in range(n)] # n개의 집의 r g b 배열

dp[0] = arr[0] #첫 행은 비용 그대로 초기화 

for i in range(1,n):
    # 현재 열을 제외한 i-1행의 열들 중 최솟값 + 현재 칸 비용
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

print(min(dp[n-1]))


