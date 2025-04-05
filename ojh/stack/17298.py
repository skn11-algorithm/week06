# 오큰수 = 자기자신보다 바로 큰 수(오른쪽에 위치한)
# 뒤에서부터 탐색하면서 오큰수가 아닌애들은 삭제
# 뒤에서 오큰수가 아니면 앞에 숫자의 오큰수가 될 수 없기 때문
import sys
input=sys.stdin.readline

n=int(input().rstrip())
A=list(map(int,input().rstrip().split()))
result=[-1]*n
stack=[]


for i in range(n-1,-1,-1):
    while stack and A[i]>=stack[-1]: # >= 가 아니라 >하면 틀림 # 원소에 같은 값이 올 수 있음
        stack.pop()
    if stack :
        result[i]=stack[-1]
    stack.append(A[i])

print(*result)
