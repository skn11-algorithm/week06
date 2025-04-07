import sys

input = sys.stdin.readline

n = int(input())
lst = []


for _ in range(n):
    lst = [list(input())]

for i in lst:
    nn = []
    for j in i:
        if j == '(':
            nn.append('(')
        else:
            nn.pop()
    if len(nn) == 0:
        print('YES')
    else:
        print('NO')