# 탑 쌓기 (자기보다 낮은 탑 다 꺼내는 )

import sys

n = int(sys.stdin.readline())
top = list(map(int, input().split()))
stack = []
answer = [0 for i in range(n)]
 
for i in range(n):
    while stack:
        if stack[-1][1] > top[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, top[i]])
 
print(*answer)