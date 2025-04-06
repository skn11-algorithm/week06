import sys
import math

MAX_NUMBER = 1000000

prime = [True for _ in range(MAX_NUMBER + 1)]
prime[0] = prime[1] = False

for i in range(2, int(math.sqrt(MAX_NUMBER) + 1)):
    if prime[i]:
        for j in range(i*i, MAX_NUMBER + 1, i):
            prime[j] = False

def goldbach(n):
    for i in range(2, n):
        if prime[i] and prime[n-i]: 
            return i,n-i
    return None, None

while True:
    n = int(sys.stdin.readline())
    if n==0:
        break
    
    a,b = goldbach(n)
    if a:
        print('%d = %d + %d' %(n,a,b))
    else:
        print('Goldbach\'s conjecture is wrong.')