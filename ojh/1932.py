import sys
input=sys.stdin.readline

n=int(input())
nums=[list(map(int,input().rstrip().split())) for _ in range(n)] 

maxx=0
# 삼각형 bottom-up으로 풀어야함
for i in range(n-2,-1,-1):
    for j in range(0,i+1): # 각 줄의 요소
        nums[i][j]+=max(nums[i+1][j],nums[i+1][j+1]) #밑에 있는 두 값 중 더 큰 거 더하기

print(nums[0][0])