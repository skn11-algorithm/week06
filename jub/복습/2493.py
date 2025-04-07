import sys
input = sys.stdin.readline  

N = int(input())  # 탑 개수
T = list(map(int,input().split()))  # 탑 높이 
stack = []
stack.append([1, T[0]])  # [인덱스, 높이] 
ans = [0]  

for i in range(1, N):
    while stack:
        if stack[-1][1] >= T[i]:  
            ans.append(stack[-1][0])  
            stack.append([i + 1, T[i]])  
            break
        else:
            stack.pop()  
    if not stack:  # 스택이 비면
        ans.append(0)  
        stack.append([i + 1, T[i]])  

print(*ans, end=' ')
