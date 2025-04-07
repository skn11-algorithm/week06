import sys 
input = sys.stdin.readline
t = int(input())
a = [0]* t
# 1번~N번 집
# N번 집의 색은 N-1 집의 색과 달라야됨
# 1번 집의 색은 2번 집의 색과 달라야됨
# i(2 <= i <= N-1) 은 i-1,i+1 색과 달라야됨

for i in range(t):
    a[i]= list(map(int,input().split()))
for i in range(1,t):
    a[i][0]= min(a[i-1][1],a[i-1][2]) + a[i][0]
    a[i][1]= min(a[i-1][0],a[i-1][2]) + a[i][1]
    a[i][2]= min(a[i-1][0],a[i-1][1]) + a[i][2]

print(min(a[t-1][0],a[t-1][1],a[t-1][2]))
