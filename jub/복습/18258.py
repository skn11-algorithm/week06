
import sys
from collections import deque # 시간초과 해결 양쪽에서 삽입삭제가 가능한 자료구조 O(1)으로 시간복잡도 됨됨
n=int(sys.stdin.readline())
s=deque([])

for i in range(n):
    a = sys.stdin.readline().split()
# a의 0번째 인덱스로 비교한다
    if a[0] == 'push':
        s.append(a[1])
    elif a[0] == 'pop':
        if len(s) == 0:
            print(-1)
        else:
            print(s.popleft()) #큐방식 pop

    elif a[0] == 'size':
        print(len(s))
    elif a[0] == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)

    elif a[0] == 'front':
        if len(s) == 0:
            print(-1)
        else:
            print(s[0])
    elif a[0] == 'back':
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])      

    
    
