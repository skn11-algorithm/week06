import sys

k = int(sys.stdin.readline())

stack=[]
for i in range(k):
    n = int(sys.stdin.readline())

    if n==0:
        stack.pop()
    else:
        stack.append(n)

sum = 0
for s in stack:
    sum += s

print(sum)