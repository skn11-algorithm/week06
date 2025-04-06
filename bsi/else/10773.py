import sys
input = sys.stdin.readline

k = int(input())
lst = []

for _ in range(k):
    n = int(input)
    if n != 0:
        lst.append(n)
    else:
        lst.pop()

print(sum(lst))