import math

MAX_NUMBER = 123456*2

# 소수면 true인 배열 만들기
arr = [True for _ in range(0,MAX_NUMBER + 1)]

arr[0] = arr[1] = False

for i in range(2, int(math.sqrt(MAX_NUMBER)) + 1):  
    if arr[i]: 
        for j in range(i * i, MAX_NUMBER + 1, i):  # i의 배수들을 모두 제거
            arr[j] = False

# 소수의 개수 출력하기
while True:
    n = int(input())
    if n == 0:
        break
    
    print(sum(arr[n+1:2*n+1])) 
    
    
    
    
    