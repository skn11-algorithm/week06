import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

s = set(l)
result = list(s)
result.sort()

d = {}
for i in range(len(result)):
    d[result[i]] = i

for i in l:
    print(d[i], end=' ')