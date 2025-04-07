import sys
input=sys.stdin.readline
n = int(input())
arr=[[' ']*n for _ in range(n)]

# 9등분하고 가운데 빼고 별로 채우기
def star(x,y,n):
    if n==1:
        arr[x][y]='*'
        return
    for i in range(3):
        for j in range(3):
            if i!=1 or j!=1:
                star(x+(n//3)*i,y+(n//3)*j,(n//3))

star(0,0,n)
for stars in arr:
    print(''.join(stars)) # 밑에꺼보다 시간 줄어듦듦

# for i in range(n):
#     for j in range(n):
#         print(arr[i][j],end="")
#     print("\n",end="")