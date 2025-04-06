# 오큰수
import sys

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
result = [-1] * N 
stack = []

for i in range(N):
    while stack and seq[i] > seq[stack[-1]] : # stack이 비어있지않고 현재 수열이 스택의 top보다 크면 
        result[stack.pop()] = seq[i] # pop한 수를 현재 값으로 설정
    stack.append(i)

print(*result)