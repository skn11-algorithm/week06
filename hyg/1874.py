import sys
input = sys.stdin.readline

n = int(input())

cursor = 1
stack = []
result = []

for i in range(n):
    num = int(input())
    
    while cursor <= num:
        stack.append(cursor)
        result.append('+')
        cursor += 1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        result.clear()
        result.append('NO')
        break
    
for r in result:
    print(r)

