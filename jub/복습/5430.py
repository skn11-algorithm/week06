import sys
from collections import deque 
input = sys.stdin.readline

t = int(input()) #테스트 케이스 개수

for _ in range(t):
    p = input()
    n = int(input())
    arr = input()[1:-2].split(',')

    r = 0
    flag = True

    if n == 0:
        queue = deque()
    else:
        queue = deque(arr)
    
    for f in p:
        if f == 'R':
            r += 1
        elif f == 'D':
            if len(queue) == 0:
                print('error')
                flag = False
                break
            else:
                if r % 2 == 1:
                    queue.pop()
                else:
                    queue.popleft()
    
    if flag:
        if r % 2 == 1:
            queue.reverse()
        result = ','.join(map(str, queue))
        print(f'[{result}]')
    

