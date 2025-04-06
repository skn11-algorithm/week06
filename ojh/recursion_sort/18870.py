import sys

input=sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
sort_nums=sorted(list(set(nums)))
result = []
for i in range(n):
    result.append(sort_nums.index(nums[i]))
print(*result)