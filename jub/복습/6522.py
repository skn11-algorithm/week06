import sys
import math

# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다

def gold(n):
    prime = [True for _ in range (n+1)] #초기에 모든 수를 소수로 가정 
    prime[0] = prime[1] = False # 0,1은 소수가 아님 
    for i in range(2,int(math.sqrt(n))+1): # n의 제곱근까지 반복 
        if prime[i] == True: # 현재 수가 소수인 경우 
            for j in range(i*i,n+1,i): # 합성수로 표시 
                prime[j] = False # 합성수는 False 
    return prime

max_n = 1000000 #최대값
list = gold(max_n) 

while True:
    n = int(sys.stdin.readline())
    if n == 0: 
        break

    # 홀수만 찾으면 됨 -> 2씩 더함 
    for i in range(3,int(n/2)+1,2): # 3부터 n/2까지 홀수만 검사 
        if list[i] and list[n-i]: # 두 수가 모두 소수인 경우 
            print(f'{n} = {i} + {n-i}')
            break

    else:
        print("Goldbach's conjecture is wrong")