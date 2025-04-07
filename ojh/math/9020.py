import sys
input=sys.stdin.readline

def gold(arr,n=10000):
    root_n=int(n**(1/2))
    for i in range(2,root_n):
        if arr[i]==True:
            for j in range(i*i,n,i):
                arr[j]=False

t=int(input())
is_prime=[False,False]+[True]*9999
gold(is_prime)

for _ in range(t):
    n=int(input())
    for i in range(n//2,1,-1): # 2까지 체크해야해서 range(,2)가 아니라 range(,1)
        if is_prime[i] and is_prime[n-i]:
            print(i,n-i)
            break