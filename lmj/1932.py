# 정수 삼각형
# 입력 : 첫째 줄에 삼각형 크기, 둘째줄부터 정수 삼각형
# 출력 : 합이 최대가 되는 경로에 있는 수의 합 

'''
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5


dp[0][0] = 7
dp[1][0] = 3 / dp[1][1] = 8
dp[2][0] = 8 / dp[2][1] = 1 / dp[2][2] = 0
dp[3][0] = 2 / dp[3][1] = 7 / dp[3][2] = 4 / dp[3][3] = 4
dp[4][0] = 4 / dp[4][1] = 5 / dp[4][2] = 2 / dp[4][3] = 6 / dp[4][4] = 5

'''
n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

# DP 배열 초기화
dp = [[0] * n for _ in range(n)]
dp[0][0] = triangle[0][0]  # 시작점 초기화

# top-bottom
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            # 왼쪽 끝: 바로 위에서만 올 수 있음
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
        elif j == i:
            # 오른쪽 끝: 위의 오른쪽 대각선에서만 올 수 있음
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        else:
            # 중간: 위(j)와 왼쪽 대각선(j-1) 중 큰 값
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

# 마지막 줄 중 가장 큰 값이 정답!
print(max(dp[n - 1]))
