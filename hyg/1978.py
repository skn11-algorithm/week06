# 소수 찾기

import math

def is_prime(num):
    if num==2:
        return True
    if num<2 or num%2==0:
        return False
    
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num%i==0:
            return False
    
    return True

n = int(input())
arr = list(map(int, input().split()))

count = 0

for i in range(n):
    if is_prime(arr[i]):
        count += 1

print(count)