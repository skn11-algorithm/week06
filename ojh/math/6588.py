import sys
input=sys.stdin.readline

def gold(arr,n=1000000):
    root_n=int(n**(1/2))
    for i in range(2,root_n):
        if arr[i]==True:
            for j in range(i*i,n,i):
                arr[j]=False

is_prime=[False,False]+[True]*999999
gold(is_prime)

while(True):
    n=int(input())
    if n == 0:
        break

    for i in range(3,n,2):
        if is_prime[i] and is_prime[n-i]:
            print(f"{n} = {i} + {n-i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")