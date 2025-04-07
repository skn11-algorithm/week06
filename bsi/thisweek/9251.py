import sys
from itertools import combinations
input = sys.stdin.readline

lst1 = list(input())
lst1.pop()
lst2 = list(input())
coma = []
comb = []

for length in range(len(lst1)+1):
    for sub in combinations(lst1, length):
        coma.append(sub)


for length in range(len(lst2)+1):
    for sub in combinations(lst2, length):
        comb.append(sub)
k = list(set(coma).intersection(comb))

print(k)
lent = []
for i in k:
    lent.append(len(i))
print(max(lent))