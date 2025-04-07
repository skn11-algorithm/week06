import math

def is_prime(num):
    if num==2:
        return True 
    if num<2 or num%2==0: # 소수x
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num%i == 0:
            return False
    
    return True

m,n = map(int, input().split())

for i in range(m, n + 1):
    if is_prime(i):
        print(i)