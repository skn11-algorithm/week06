import sys
input = sys.stdin.readline

def bcbc(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return bcbc(n-2) + bcbc(n-1)

k = int(input())
print(bcbc(k))