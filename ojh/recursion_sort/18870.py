import sys

input=sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
sort_nums=sorted(list(set(nums)))
result = {num:i for i,num in enumerate(sort_nums)}

for num in nums:
    print(result[num],end=' ')