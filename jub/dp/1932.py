import sys
input = sys.stdin.readline
n = int(input())
a = [0]*n

for i in range(n):
    a[i]=list(map(int,input().split()))
for i in range(1,n): # 1 층부터 순회
    for j in range(len(a[i])): # 현재층의 모든 요소 탐색 
        if j == 0: # 첫번째 요소 
            a[i][j] = a[i][j]+a[i-1][j] #층의 첫번째 요소 
        elif j == len(a[i])-1: #마지막 
            a[i][j] = a[i][j]+a[i-1][j-1] # 층의 마지막 요소 
        else: # 중간 
            a[i][j]=max(a[i-1][j-1],a[i-1][j])+a[i][j]
    print(max(a[n-1]))