# import sys
# input = sys.stdin.readline

# a=[]
# n = int(input())
# for _ in range(n):
#     a.append(list(map(int, input().split())))

# for lst in a:
#     if len(lst) == 1:
#         k = lst[0]
#     elif len(lst) == 2:
#         d = max(lst)        # 8
#         n = lst.index(d)  # 1
#         k += d              # 15
#     else:
#         d = max(lst[n], lst[n+1])   # 1 # 7 # 1
#         n = lst.index(d)    # 1 # 1 # 5
#         k += d              # 16    # 23

# print(k)

def max_path_sum(triangle):
    n = len(triangle)
    # 아래에서부터 위로 올라가면서 계산
    for i in range(n-2, -1, -1):
        for j in range(len(triangle[i])):
            # 현재 위치에서 아래층의 왼쪽, 오른쪽 중 더 큰 값을 더함
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    
    # 맨 위층의 값이 최대 합
    return triangle[0][0]

# 입력 받기
n = int(input())
triangle = []
for i in range(n):
    row = list(map(int, input().split()))
    triangle.append(row)

# 결과 출력
print(max_path_sum(triangle))